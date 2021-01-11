#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp LoginPage_SQLite.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install pyotp" >> tempdir/Dockerfile
echo "RUN sudo apt-get isntall curl" >> tempdir/Dockerfile
echo "COPY  ./static /home/login/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/login/templates/" >> tempdir/Dockerfile
echo "COPY  LoginPage_SQLite.py /home/login/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/login/LoginPage_SQLite.py ">> tempdir/Dockerfile

cd tempdir
docker build -t loginapp .
docker run -t -d -p 5050:5050 --name loginrunning loginapp
docker ps -a 
