FROM python:3.9
WORKDIR /deploy_speckle_compute
COPY requirements.txt /deploy_speckle_compute/
RUN pip install -r requirements.txt
COPY . /deploy_speckle_compute
CMD python main.py