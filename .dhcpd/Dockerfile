FROM ubuntu:18.04

CMD ["bash"]

ENV DEBIAN_FRONTEND=noninteractive
ENV container=docker LC_ALL=C TINI_VERSION=v0.19.0

RUN apt update
RUN apt update --fix-missing
RUN apt install -y isc-dhcp-server mc

#ENTRYPOINT ["bash" ""]
