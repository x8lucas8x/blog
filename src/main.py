from typing import Optional

import typer

app = typer.Typer()


@app.command()
def serve(port: int=8000):
    """
    Serve the site in dev mode, where it reloads due to changes.
    """
    from src.app import run_server
    run_server(port=port)


@app.command()
def generate(name: Optional[str] = None):
    """
    Genererate the site and outputs them to be served by CDNs.
    """
    from src.generate_static import run_generate_static
    run_generate_static()


if __name__ == "__main__":
    app()