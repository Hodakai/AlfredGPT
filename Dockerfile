# use a python container
FROM python:3.7-slim

# installing rasa
RUN python -m pip install rasa

# setting the current work directory, env
# and copying the repo into the container
WORKDIR /app
ENV HOME=/app
COPY . .

# Training the model
# PS: can be removed to avoid training at every launch
RUN rasa train

# Forcing an user to avoid launching some stuff in root
USER 1001

ENTRYPOINT ["rasa"]

# Starting the Rasa project
CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--debug"]

# Exposing rasa's default port for the API
EXPOSE 5005