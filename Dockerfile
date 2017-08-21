FROM python:3.6

RUN curl -sL https://bootstrap.pypa.io/get-pip.py | python
COPY . /app
WORKDIR /app
RUN pip install -r test-requires.txt
