---
slug: zeroless
title: Zeroless
authors:
- Lucas Lira Gomes
created_date: 2015-08-18 20:40
category: Code
tags:
- zeromq
- python
---

I have been an enthusiast of ZeroMQ for quite some time. If there was an opportunity
that required some sockets on steroids, I would not think twice. Ah, how those three
messaging pattern were useful (i.e., Request/Reply, Push/Pull, Publish/Subscribe).
They had the remarkable trait of being able to drastically streamline the development of
distributed systems. And its portability, with wrappers for more than 30 languages,
brokerlessness and amazing documentation made it a no-brainer for me to favour ZeroMQ
over other messaging alternatives.

Using [ZeroMQ] in Python with [PyZMQ], however, always made me feel like I'm coding in
C/C++, which I also love by the way. Unfortunately, that lack of [PyZMQ] API's, if I
may say, “pythonicity”, just felt wrong to me. And by the end of last January, I
decided to do something about it. So, that is how [Zeroless] was born.

My mission was to leverage on [PyZMQ] to build a more elegant wrapper for [ZeroMQ].
Something more aligned with the python way of doing things. And, to a certain degree,
I have succeeded. However, I have never made a comprehensive effort to publicise
[Zeroless] in any way so, in this post, I hope not only to explain how [Zeroless]
differs from [PyZMQ] but also to reach a greater audience, that may be as enthusiastic
about [ZeroMQ] as myself. Therefore, without further ado, here goes some of the design
decisions I have made for [Zeroless]:

##### TCP only for the win

Ok, I know PGM, INPROC and IPC have their use cases. PGM, for instance, provides a
Publish/Subscribe specific transport, that scales better than TCP in the
Publish/Subscribe use case, as it cut out the ACK flood publishers gets on
every new message. There are also some extra reliability, that you also cannot
find in TCP. IPC, on the other hand, is a pattern agnostic way of providing more
efficient inter-process communication than traditional networking, but is Unix-like
only. As for INPROC's particular case, which efficient applicability is being
hindered by the Python's GIL, I do not see why bother with it.

Nevertheless, I have a feeling that the vast majority of the users, like myself,
are ok with just TCP being supported. Which is precisely what you need when building really
horizontally scalable networked services, especially in this time of a renewed
vision for SOA, with microservices having a lot of attention. So let us just use
TCP and free our minds to think about other matters.

##### No more contexts

[PyZMQ] applications require users to create a context, in order to instantiate
sockets. Technically, a context serves as a container for all your sockets and
usually one of it, per process, is just what you require. As a matter of fact, you
could have more, but why bother your runtime with more event loops, for your
socket stuff, when one suffices? Moreover, if you are using INPROC as transport,
you may also need to share a context for the communication to happen. But again,
if INPROC is not that useful in Python as aforementioned, do we really need
explicitly manage contexts?

Not at all, so that is why in [Zeroless] you just have to manage Clients, sockets
that connect, and Servers, sockets that bind, without concerning yourself with
contexts ;). For instance, in order to instantiate a client you would:

```python
client = Client()

# You could use connect_local(port=12345) as well
client.connect(ip='127.0.0.1', port=12345)
```

Similarly, for servers, you would:

```python
server = Server(port=12345) # No need to call bind here
```

Finally, note that no real connect/bind will occur unless you instantiate a
messaging pattern, which are the subject of our next topic.

##### Like a factory method pattern

One thing I never liked about [PyZMQ] sockets's instantiation is that we have to call
a method called socket, which receives an enum representing the type of the socket.
Why don't they just provide a separate method for every socket possible, like as if
it were a factory method pattern kind of interface? That would allow a more
straightforward experience for developers, that could then rely on their favourite
IDE's code complete to quickly understand what kind of sockets and parameters they
could set. That enum approach, however, will probably make your users go to the
documentation, but solely because of the way the [PyZMQ]'s interface is.

In [Zeroless], we fixed that, so you don't need to check the documentation every
time you want to instantiate a socket, instead just have a decent code complete
support, and you are done. For instance, compare how you would instantiate a
publisher socket with [Zeroless]:

```python
pub = Server(port=12345).pub(topic=b'')
```

##### Connections awareness

One of the questions you may ask is to whom your clients are connected to. And
for that, [PyZMQ] cannot help you. Unless you manage that list of connections by
yourself, you wouldn't be able to get it afterwards. Therefore, in [Zeroless],
we provide an addresses property, so that you can retrieve all your IP and port
pairs as a list of tuples. But that is only for clients of course, as there is
no way to know which sockets are connected to your server without building
some sort of infrastructure for that yourself.

##### Subscribe should not be tricky

In terms of interface, the subscribe case is particularly problematic in [PyZMQ].
One must use the not so intuitive [setsockopt()][setsockopt_method] method, in
order to define the topics it subscribes to. Like in the following snippet:

```python
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"") # Subscribe to all topics
```

I believe most new [ZeroMQ]'s user get this wrong at first, as they suppose no
topic means you are subscribed to all topics, and keep asking himself/herself why
that damn subscriber socket does not receive your published messages.

In [Zeroless], we fixed that, so that you don't have to instantiate your socket
and set something as essential as a topic, in the subscribe case, via some kind
of “obscure” method. Just compare how you would instantiate a subscriber socket
with [Zeroless]:

```python
listen_for_pub = client.sub(topics=[b''])
```

##### Generators and high-order functions as first class citizens

[PyZMQ] sockets tend to use [send()][send_method] and [recv()][recv_method] methods
for the message exchange part. However, it always felt wrong to me to do stuff like:

```python
while True:
    data = socket.recv()
    # do something with data
```

That is, if Python has built-in support for iterables, or generators if you prefer,
why don't we just do something like:

```python
listen_for_push = Server(port=12345).pull()

for data in listen_for_push:
    # do something with data
```

Way more idiomatic to read incoming messages that way, right? As for sending them,
I also followed a different path.

```python
push = client.push()
push(b"Msg1")
```

Therefore, in [Zeroless], every time you instantiate a message pattern that is
supposed to send messages, use it as a function. Otherwise, treat it as a generator.

##### Multi-part made easy

In [PyZMQ], if you want to send a multipart message, you have to use the
[recv_multipart()][recv_multipart_method] and [send_multipart()][send_multipart_method]
methods. Methods that, instead of a single message, will deal with a list of them.
In [Zeroless], I favoured consistency for a quicker and easier learning path. Therefore,
there is no difference between the single part and the multipart API.

If you want to send a multipart message, just consider that your send function have
a printf like interface, and you are set. So, for instance, if you wish to send an
id separated from your message body, you could:

```python
push = client.push()
push(b'1', b'OK')
```

Additionally, if someone sends you a multipart message, your generator will return a
tuple with all of its parts. As a result of that, to get the message from the previous
example you would need to:

```python
listen_for_push = Server(port=12345).pull()
for id, msg in listen_for_push:
    # do something with id and msg
```

##### The future

Although feature parity was never part of my plans, there are still some of [PyZMQ]'s
functionalities I would like to provide in [Zeroless]. Like both [poller][poller_api]
and [devices][devices_api] APIs, for instance. So expect more on the way o/. While
that, if you felt compelled to help shape this project, please clone our [repository]
and see our [guidelines].

[zeromq]: http://zeromq.org/
[pyzmq]: https://github.com/zeromq/pyzmq
[zeroless]: https://github.com/zmqless/python-zeroless
[repository]: https://github.com/zmqless/python-zeroless.git
[guidelines]: http://python-zeroless.readthedocs.org/en/latest/development.html#contributing
[poller_api]: https://zeromq.github.io/pyzmq/api/zmq.html#poller
[devices_api]: https://zeromq.github.io/pyzmq/api/zmq.devices.html
[recv_method]: https://zeromq.github.io/pyzmq/api/zmq.html#zmq.Socket.recv
[recv_multipart_method]: https://zeromq.github.io/pyzmq/api/zmq.html#zmq.Socket.recv_multipart
[send_method]: https://zeromq.github.io/pyzmq/api/zmq.html#zmq.Socket.send
[send_multipart_method]: https://zeromq.github.io/pyzmq/api/zmq.html#zmq.Socket.send_multipart
[setsockopt_method]: https://zeromq.github.io/pyzmq/api/zmq.html#zmq.Context.setsockopt
