FROM python:3.6-alpine3.6

WORKDIR /srv

# Install uwsgi
RUN apk add --no-cache uwsgi-python3

# Install supervisord
#RUN apk add --no-cache supervisor

# Install pipenv
RUN pip install pipenv

# Create an app user and run as that
RUN adduser -S app
RUN chown -R app /srv
USER app

# Install Python dependencies
ADD Pipfile Pipfile.lock ./
RUN pipenv install

# Add the project
ADD setup.py ./
ADD src ./src
ADD tax-planner.ini ./
ADD prestart.sh ./
RUN pipenv run python setup.py develop

USER root
RUN chown -R app tax-planner.ini
RUN chown -R app prestart.sh
USER app
RUN sh prestart.sh

ENV FLASK_APP src

#CMD pipenv run flask run --host 0.0.0.0 --port 8080
CMD uwsgi tax-planner.ini
