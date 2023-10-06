
FROM python:alpine
WORKDIR /app
COPY Scores.txt /app/scores.txt
COPY Mainscore.py /app/Mainscore.py
RUN pip install flask
CMD python Mainscore.py
