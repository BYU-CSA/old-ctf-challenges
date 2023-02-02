# syntax=docker/dockerfile:1

FROM python@sha256:6441e2f0bd2e566de0df6445cb8e7e395ea1a376dd702de908d70401d3700961

WORKDIR /app

COPY requirements.txt requirements.txt
# RUN ls -A ~/.cache/pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
