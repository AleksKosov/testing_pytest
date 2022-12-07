FROM python:latest
WORKDIR /app/
ADD test_yandex.py /app
RUN pip install pytest && pip install selenium && pip install allure-pytest
CMD pytest