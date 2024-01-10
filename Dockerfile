# pull official base image
FROM python:3.11.3

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# port where the Django app runs 
EXPOSE 8000

# start server 
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]