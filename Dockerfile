FROM ubuntu:18.04

RUN apt-get update -y \
  && apt-get install python3-pip -y \
  && apt-get install nginx -y \
  && pip3 install pip --upgrade \
  && apt-get clean

COPY ./app /app
COPY ./config/gunicorn.conf.py /app
WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

#COPY start.sh /app/start.sh
#RUN chmod +x /app/start.sh

#CMD ["/app/start.sh"]
CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "main:app"]
EXPOSE 8000