# Build the app image
FROM python:3.12.7-alpine

ENV APP_HOME=/home/ecobe/api

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN pip install pip --upgrade && pip install -e . && rm -rf ~/.cache/pip
RUN addgroup -S ecobe && adduser -S ecobe -G ecobe
RUN chown -R ecobe:ecobe $APP_HOME
USER ecobe

CMD ["uvicorn","infra.api.app:app","--host=0.0.0.0","--port=8000","--reload"]

