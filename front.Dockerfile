FROM python:3
EXPOSE 5000

COPY /backend /backend
WORKDIR /backend/

RUN pip install -r requirements.txt
CMD python mainPage.py