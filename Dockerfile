FROM	python:3.9.5-slim

ADD	src/ /src/

RUN	pip install -r /src/requirements.txt

EXPOSE	8080

CMD	["python", "/src/demo.py"]
