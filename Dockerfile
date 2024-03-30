# first stage build
FROM --platform=$BUILDPLATFORM python:3.9

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN exit

RUN apt-get update && apt install -y apt-utils

RUN apt-get remove -y libodbc2 libodbcinst2 odbcinst unixodbc-common

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# copy requirements
COPY requirements.txt ./

# install requirements
RUN pip install -r requirements.txt

# create app dir
WORKDIR /app
# copy everything to app dir
COPY . /app

RUN chmod +x execute.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]