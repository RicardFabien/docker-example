FROM python:3
EXPOSE 5000

COPY / /backend
WORKDIR /backend/

RUN pip install -r requirements.txt
CMD python secondPage.py
#CMD python mainPage.py