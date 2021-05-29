FROM ubuntu:20.04

MAINTAINER K1a <kia@csie.io>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y xinetd

RUN adduser --disabled-password --gecos ""  gemini

COPY ./gemini /home/gemini
COPY ./xinetd /etc/xinetd.d/gemini

RUN chown -R root:root /home/gemini
RUN chmod -R 755 /tmp
RUN chmod -R 755 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run

CMD ["/usr/sbin/xinetd","-dontfork"]