FROM ubuntu:20.04
MAINTAINER Lys

RUN apt-get update && apt-get install -qy xinetd
RUN useradd -m ais3shell
RUN chown -R root:root /home/ais3shell
RUN chmod -R 755 /home/ais3shell

CMD ["/usr/sbin/xinetd","-dontfork"]
