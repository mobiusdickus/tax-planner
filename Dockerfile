FROM python:3.6-alpine3.6

WORKDIR /srv

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
RUN pipenv run python setup.py develop

ENV FLASK_APP src
CMD pipenv run flask run --host 0.0.0.0 --port 8080
