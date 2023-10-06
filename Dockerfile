
FROM python:alpine
WORKDIR /app
COPY scores.txt /app/scores.txt
COPY Mainscore.py /app/Mainscore.py
RUN pip install flask
CMD python Mainscore.py
