FROM python:3.6

ENV SRC=python_ni_app
ENV PROJ=/var/www/python_ni_app

COPY $SRC $PROJ

WORKDIR $PROJ

RUN useradd django

RUN mv /etc/apt/trusted.gpg.d /etc/apt/trusted.gpg.d.bak

RUN apt-get update && apt-get install -y --allow-unauthenticated\
  vim \
  htop \
  supervisor

RUN chown django:django -R $PROJ
RUN mkdir -p /var/log/supervisor
RUN chown django:django -R /var/log/supervisor


RUN pip install -r requirements.txt

CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]