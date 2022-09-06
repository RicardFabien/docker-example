FROM python:3
EXPOSE 5000

COPY /frontend /frontend
WORKDIR /frontend/

RUN pip install -r requirements.txt
CMD python mainPage.py