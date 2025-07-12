import asyncio
from collections.abc import Generator

from anyio import Path, open_file
from yaml import safe_load


async def items() -> Generator[tuple[dict, str], None, None]:
    tasks = []
    async for path in Path("content").glob("**/*.md"):
        async with asyncio.TaskGroup() as tg:
            tasks.append(tg.create_task(read_file(path)))

    async for task in asyncio.as_completed(tasks):
        input_path_file, input_file_content = task.result()
        _, front_matter_str, content = input_file_content.split("---", 2)

        metadata = safe_load(front_matter_str)

        metadata["parent_dir"] = str(input_path_file.parent)

        if metadata.get("draft", False):
            continue

        if not isinstance(metadata.get("tags", []), list):
            metadata["tags"] = [metadata.get("tags")]

        yield (
            metadata,
            content,
        )


async def read_file(input_path_file: Path) -> None:
    async with await open_file(input_path_file, "rt") as file:
        return input_path_file, (await file.read())
