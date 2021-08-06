FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements .
RUN pip install -r requirements
COPY . /app/
CMD /app/docker-entrypoint.sh