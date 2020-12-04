FROM python
RUN pip install flask
RUN pip install pyotp
COPY  ./static /home/login/static/
COPY  ./templates /home/login/templates/
COPY  LoginPage_SQLite.py /home/login/
EXPOSE 5050
CMD python /home/login/LoginPage_SQLite.py 
