# pull official base image
FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# set work directory
RUN mkdir /digitaloffice

WORKDIR /digitaloffice

COPY . /digitaloffice/

RUN pip install --upgrade pip && \
    pip install -r requirements/production.txt 

# # copy project
# COPY requirements/production.txt production.txt 
# COPY requirements/base.txt base.txt

# COPY requirements/ .

# # install dependencies
# RUN pip install --upgrade pip
# RUN pip install -r production.txt
# # create directory for the app user
# RUN mkdir -p /home/app

# # create the app user
# RUN addgroup -S app && adduser -S app -G app

# # create the appropriate directories
# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/static
# RUN mkdir $APP_HOME/media
# RUN chown -R app:app $APP_HOME
# RUN chown -R app:app $APP_HOME/static
# RUN chown -R app:app $APP_HOME/media
# WORKDIR $APP_HOME

# # copy entrypoint.sh
# COPY ./entrypoint.sh $APP_HOME

# # copy project
# COPY . $APP_HOME

# # VOLUME
# # VOLUME /home/app/web/mediafiles


# # chown all the files to the app user
# RUN chown -R app:app $APP_HOME

# # change to the app user
# USER app

# # run entrypoint.prod.sh
# RUN ["chmod", "+x", "/home/app/web/entrypoint.sh"]
# ENTRYPOINT ["/home/app/web/entrypoint.sh"]
    
