Set up instructions
===================

$ docker build --tag albertoaj_com .



Running the app
===============

Replacing "<public-port>" with the port you want to bind the app to:
$ docker run -d -p <public-port>:80 albertoaj_com