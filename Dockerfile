FROM frolvlad/alpine-python2
MAINTAINER Miguel Gonzalez Sanchez

COPY chime.py chime.py

RUN mkdir /chime && chmod 755 /chime
VOLUME /chime

ENTRYPOINT ["python", "chime.py", "/chime/"]
