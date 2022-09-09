FROM python:3
EXPOSE 80

COPY / /backend
WORKDIR /backend/

RUN pip install -r requirements.txt
CMD python api.py