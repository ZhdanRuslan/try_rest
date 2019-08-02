FROM python:3.7.3
ENV PYTHONUNBUFFERED=1
ADD . /
WORKDIR /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["./run_app.sh"]

