FROM python:3.6-slim

ENV PYTHONBUFFERED True

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./

RUN pip install backports.zoneinfo==0.2.1

RUN pip install -r requirements.txt

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

CMD ["python", "scrape_googlenews.py"]