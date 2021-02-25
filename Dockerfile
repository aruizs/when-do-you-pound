FROM python:3.8-alpine

ENV FLASK_APP wdoiupound.py
ENV FLASK_CONFIG production

RUN adduser -D wdoiupound
USER wdoiupound

WORKDIR /home/wdoiupound

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY wdoiupound.py boot.sh ./

# run-time configuration
EXPOSE 80
ENTRYPOINT ["./boot.sh"]
