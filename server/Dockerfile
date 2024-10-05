FROM python:3.9-alpine

# Copy and install requirements
RUN apk update && apk add \
    gcc \
    g++ \
    freetype-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    python3-dev \
    cairo-dev \
    dcron

# Codebase setup
RUN mkdir /srv/weatherboard/
WORKDIR /srv/weatherboard/
RUN pip3 install requests pillow flask gunicorn pytz pycairo openai python-dotenv numpy

# Add code
ENV PYTHONPATH /srv/weatherboard/server
ADD . /srv/weatherboard/
COPY .env /srv/weatherboard/.env

# Add fonts
RUN mkdir /usr/share/fonts && cp /srv/weatherboard/fonts/Roboto* /usr/share/fonts && fc-cache

# Copy crontab and install it
COPY crontab /etc/cron.d/weatherauto
COPY cronimage /etc/cron.d/cronimage
COPY cronweather /srv/cron.d/cronupdateweather
RUN chmod 0644 /etc/cron.d/weatherauto
RUN chmod 0644 /etc/cron.d/cronimage
RUN chmod 0644 /srv/cron.d/cronupdateweather

# Ensure the cron job is registered for root user
RUN crontab /etc/cron.d/weatherauto
RUN crontab /etc/cron.d/cronimage
RUN crontab /srv/cron.d/cronupdateweather
# Create the log file to be able to run tail later
RUN touch /var/log/cron.log

# Runtime
ENV PORT 8080
CMD ["/bin/sh", "-c", "crond -l 2 && exec gunicorn --bind :$PORT --workers 1 --threads 8 server:app"]