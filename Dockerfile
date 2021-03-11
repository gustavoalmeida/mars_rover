FROM python:3.9
RUN mkdir /cli 
COPY /cli /cli
COPY rover.py /
COPY pyproject.toml /
COPY Makefile /
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev