FROM nginx:1.22.1
COPY nginx.conf /etc/nginx/templates/default.conf.template

FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
