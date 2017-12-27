FROM ubuntu:latest
MAINTAINER Anuj Gupta "anuj6.gupta@aricent.com"
ENV http_proxy "http://165.225.104.34:80"
ENV https_proxy "http://165.225.104.34:80"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV http_proxy ""
ENV https_proxy ""
ENTRYPOINT ["python"]
CMD ["client-server.py"]
