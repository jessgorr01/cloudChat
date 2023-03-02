FROM ubuntu
RUN apt-get update
RUN apt-get install -y mysql
RUN apt-get clean
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
