FROM ubuntu

MAINTAINER yulng yulng2000@163.com

ADD sources.list /etc/apt/sources.list 
#RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential curl net-tools vim nginx vim


RUN mkdir -p /home/socket_test 
COPY socket_server.py /home/socket_test/socket_server.py 
COPY socket_addr.py /home/socket_test/socket_addr.py

WORKDIR /home/socket_test

EXPOSE 5000

CMD ["python", "socket_server.py"] 
