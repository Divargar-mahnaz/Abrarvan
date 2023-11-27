FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN ln -snf /usr/share/zoneinfo/"Asia/Tehran" /etc/localtime && echo "Asia/Tehran" > /etc/timezone

WORKDIR /ip_detection
COPY requirement.txt /ip_detection/
RUN pip install -r requirement.txt
RUN pip install psycopg2
COPY . /ip_detection/

CMD   python /ip_detection/manage.py makemigrations && python /ip_detection/manage.py migrate &&  python /ip_detection/manage.py runserver 0.0.0.0:8000