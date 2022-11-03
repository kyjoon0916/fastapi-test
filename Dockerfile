FROM python:3.10.5-slim

WORKDIR /src

COPY ./requirements.txt /src/

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY src/* /src/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
