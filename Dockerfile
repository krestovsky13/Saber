FROM python:3.10

WORKDIR app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app/src/"
ENV PYTHONPATH "${PYTHONPATH}:/app/src/api/"

RUN python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
