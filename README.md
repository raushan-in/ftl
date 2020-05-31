# An assignment by FullThrottle Lab


## Introduction
This repository hosts the code for FullThrottle Lab's assignment backend. Written in Python and using Django web framework, this project aims to develop a RESTful API to consume HTTP request.

### Technical Stack
- Python 3.7.0+
- Django 3.0.6+
- Django Rest Framework (DRF) 3.8.0+
- SqlLite3

### Steps to setup server.
- First, ensure that Python is installed. 
- install the poetry (dependency manager) using command
```shell 
pip install poetry
```
- Top directory of the project contains .tomal file. Open terminal on this directory and run command:
```shell 
poetry install
```
- Once the all dependencies get installed, create virtual environment by 
```shell 
poetry shell
``` 
- go to 'ftl' directory.
- In 'ftl' directory you will find a file 'manage.py'.
- To start backend server type below command in terminal:
```shell
python manage.py runserver
```
- open http://127.0.0.1:8000/ in a browser.
- And, done! Hopefully, it should work now. If not, contact me at raushan.br.in@gmail.com.
