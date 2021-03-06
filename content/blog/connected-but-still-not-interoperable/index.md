---
title: "Connected, but still not interoperable"
date: "2015-09-04T19:30:00.000Z"
tags:
  - iot
---

Cisco call it the Internet of Everything (IoE), most players would rather
name it the Internet of Things (IoT) and, although less common, you probably
heard the term the Industrial Internet too. And if you ever read any post
or whitepaper about one of those buzzwords, especially those written by big
players in the market (e.g. Cisco, IBM), you probably saw a trend in
depicting scenarios where your things (e.g. car, appliances, lighting, HVAC)
are interconnected and, somehow, interacting among themselves independently
of human interference. Great vision, but how far are we from it?

Right now IoT is composed by a jungle of different solutions. You can probably outline
those that seem more promising. In the networking spectrum there is a whole stack
solutions, which tries to provide you not only data link layer features but also
routing, addressing and some even encryption, those are mainly Zigbee, Z-Wave,
Bluetooth and WirelessHart. On the other hand you also have WIFI, raw IEEE 802.15.4,
GPRS and all sort of radios operating in sub-gigahertz frequency ranges. Each has
an use case of its own. Z-Wave, for instance, is more present in home automation,
Bluetooth V4 is usually the right one for wearables, WirelessHart is an adaption
of the Highway Addressable Remote Transducer Protocol (HART) protocol for industrial
wireless networks and Zigbee is the wild card among them (i.e. thanks to DIGI's
amazing AT programming interface).

Along with that there is also efforts to bring the IP protocol to the constrained devices
like those that use IEEE 802.15.4 and its variations. Well, the advantages are many. First
there is the seamless exchange of information between devices utilizing any IP-enabled
MAC/PHY (e.g. Wi-Fi, Ethernet). Second we cannot forget the battle-tested tooling all
those years of IP predominance have provided us (e.g. ping, traceroute, netcat, wireshark,
tcpdump). The [IPSO Alliance] is one of the major advocates in this matter. They have several
whitepapers publicising standards like [6LowPan], an IPV6-compatible addressing with better
header compression, and [RPL], a mesh-enabled routing protocol for low power and lossy networks.
The [Zigbee Alliance] also realised the advantages of IPv6-based wireless mesh networking and
created ZigBee IP, and open standard built on top of IEEE 802.15.4 that provides end-to-end
IPv6 networking.

On top of IP, on the application level, [MQTT] and [COAP] shine. The first is a lightweight
PUB-SUB protocol based on TCP. Now you may wonder if [MQTT] is appropriate for wireless
sensor networks. In fact anything TCP based is not by design, but in such cases you can use
[MQTT-SN], a UDP based variation of [MQTT] that is especially tailored for low-cost and
low-power sensor devices that run over bandwidth-constrained wireless networks. While [COAP]
is a lightweight HTTP compatible protocol, based on UDP, with support for multicasting and
service discovery. Both of them are quite popular and you can probably find an implementation
for your favourite programming language or IoT platform (e.g. [Contiki OS], [Arduino]).
Unfortunately, given a non-IP network, developing a gateway to map your custom protocol
in the interface your backend/server uses and vice-versa is a necessary burden.

So, there is certainly no doubt there were major progresses on the connectivity front, but
still something is absent in this equation. Connectivity is certainly necessary but IoT is as
much about connectivity as the internet is about the web. That vision those big players describe
of smart Xs, being X anything, autonomously interacting among themselves is heavily dependent
of those devices being able to discover each other and access their functionalities, without
being explicitly pre-programmed to do so. You probably saw companies like [Smart Things],
[Ninja Blocks] or the former [Revolv], bought by [Nest], stating that their platforms/hubs
supports different vendors or "play well with others", which is great but has its own limitations.

Up to now, in platforms like the aforementioned, integration of new products occurs in an
incremental fashion. So if you want to support Phillip's [Hue] or [LIFX] lamps, you will have
to read the documentation of their REST API. Which seems great given REST apis are easy to
integrate, but the crude reality of IoT is way less welcoming. In most you cases, you will
find yourself with vertically integrated systems that do not permit easy third-party integration.
And even if they permitted, the manual process of integrating with new devices and/or platforms
have two problems.

First, a great deal of products does not provide public documented APIs for third-parties.
And the reason is that, currently, most vendors tend to sell a solution, from hardware to user
interface, therefore not caring for those who want to use their products differently from what
they envisaged (i.e. makers suffer :/). Consider [Plugwise], for instance, they have one of the
most complete energy management solutions out there, but without a consistent effort to provide
a public API or SDK. You may even find unofficial libraries, made by someone who probably had
to sniffer [Plugwise]'s devices in order to reverse engineer their proprietary protocol. But
using those, you would not have any guarantee of future support. Besides that it is common
for unofficial libraries not to be feature complete, so good luck if you want to use the most
recent capabilities.

Second, manual integration does not scale. Vendors may try to pinpoint the most popular
products, to focus their integrations efforts, or form partnerships, but that degree of
interoperability will come at the expense of tight vendor integration with specific
partners.

To solve those problems, devices need to discover and access each other functionalities, not
necessarily directly like M2M scenarios portrait. And for such two things are required. First
a data model that could explicitly state what each piece of data is about, so that you do not
have to read a manual to realise that a sensor is measuring temperature in Celsius. Ontologies
are usually the answer in such cases, but [OWL] and [RDF] are not appropriate given the bandwidth
limitations. The [IPSO Alliance] tried to fill this gap with its [Smart Objects] specification,
which describes a reusable data model for IoT. That data model defines a set of data types
and structures that can be used by different devices, in order to enable them to interoperate
since the semantics is now in the data itself. Still, despite the [Smart Objects] specification,
ontologies have an important role at the users level, as the tooling from semantic web
technologies (e.g. [SPARQL], [OWL], [RDF]) can provide great value for those interested in
composing their own IoT solutions by accessing higher level services.

Although being able to determine the content of the messages sent by sensors is important, no
equivalent exists in terms of actuation. And that is key to a large adoption of IoT, especially
in the end-consumer market. Right now, businesses can get value by tracking trends and analysing
data, but for end-consumers automation is the real killer application. And by automation I mean
not only actuation, that translates itself in an event in the physical world, but also remote
configuration of these devices. All that provided, without devices being pre-programmed to do
so, would be huge. But, unfortunately, no lightweight UPnP exist for the IoT yet.

[ipso alliance]: http://www.ipso-alliance.org/
[zigbee alliance]: http://www.zigbee.org/
[plugwise]: https://www.plugwise.com/
[nest]: https://nest.com/
[revolv]: http://revolv.com/
[ninja blocks]: https://ninjablocks.com/
[smart things]: http://www.smartthings.com/
[hue]: http://www2.meethue.com/pt-br/
[lifx]: https://www.lifx.com/
[owl]: http://www.w3.org/2001/sw/wiki/OWL
[rdf]: http://www.w3.org/2001/sw/wiki/RDF
[sparql]: http://www.w3.org/2001/sw/wiki/SPARQL
[smart objects]: http://www.ipso-alliance.org/smart-object-guidelines
[contiki os]: http://contiki-os.org/
[arduino]: https://tools.ietf.org/html/rfc7390
[mqtt]: http://mqtt.org/news
[mqtt-sn]: http://mqtt.org/news
[coap]: https://tools.ietf.org/html/rfc7252
[6lowpan]: http://www.ipso-alliance.org/downloads/6LoWPAN
[rpl]: http://www.ipso-alliance.org/downloads/RPL
