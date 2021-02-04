FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt 
CMD python live_ticker_bot_optional.py