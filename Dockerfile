FROM python
COPY . /calculator_app
WORKDIR /calculator_app
CMD ['python',calc_app.py]
