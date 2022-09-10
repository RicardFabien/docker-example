FROM python:3
EXPOSE 8888

COPY / /frontend
WORKDIR /frontend/

RUN pip install -r requirements.txt
CMD python mainPage.py