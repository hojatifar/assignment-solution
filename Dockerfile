FROM python:3.9
ADD requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /path to/app
ADD main.py .
ADD input_log_files.py .
ADD operation.py .
ADD output_txt.py .
ENTRYPOINT ["python", "main.py"]
