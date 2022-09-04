FROM ubuntu:18.04

CMD ["bash"]

ENV DEBIAN_FRONTEND=noninteractive
ENV container=docker LC_ALL=C TINI_VERSION=v0.19.0

RUN apt update --fix-missing
RUN apt install -y python3-markupsafe python3-pip mc
RUN pip3 install flask uwsgi

#ENTRYPOINT ["sh" ""]
