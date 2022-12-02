FROM python:latest
WORKDIR /app/
ADD test_run.py /app
RUN pip install pytest
RUN pip install selenium
CMD pytest -s -v test_run.py