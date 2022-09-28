FROM python:3
EXPOSE 8080

COPY / /backend
WORKDIR /backend/

RUN pip install -r requirements.txt
CMD python api.py