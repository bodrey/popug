FROM python:3

RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN apt-get update && apt-get install -y --no-install-recommends supervisor && apt-get install -y locales locales-all
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
# ENV LC_ALL ru_RU.UTF-8
# ENV LANG ru_RU.UTF-8
# ENV LANGUAGE ru_RU.UTF-8

# COPY ./src /app/src
# COPY ./supervisor-app.conf /etc/supervisor/conf.d/

# CMD python /app/src/manage.py migrate && python /app/src/manage.py collectstatic -v0 --noinput && supervisord -n