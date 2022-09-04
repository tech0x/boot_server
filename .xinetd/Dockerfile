FROM ubuntu:18.04

CMD ["bash"]

ENV DEBIAN_FRONTEND=noninteractive
ENV container=docker LC_ALL=C TINI_VERSION=v0.19.0

RUN apt update --fix-missing
RUN apt install -y xinetd tftpd mc

#ENTRYPOINT ["sh" ""]
