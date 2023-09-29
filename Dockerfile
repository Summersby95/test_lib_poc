FROM python:3.10.12-slim-bullseye

EXPOSE 8000

ENV APP_HOME=/usr/src/test/src

RUN mkdir -p /usr/src/test
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY dependencies/requirements.txt ./

RUN python3 -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY ./src $APP_HOME

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8000"]
