FROM python:3.6
WORKDIR /app
COPY . /app
RUN pip install discord.py bs4 lxml pandas requests html5lib
CMD python multiple_bot.py