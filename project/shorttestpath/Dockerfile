FROM python:3
RUN apt-get update
RUN git clone https://github.com/sambapython/Usbatch.git
RUN cp -rf ./Usbatch/project/shorttestpath ./
RUN pip install -r shorttestpath/requirements.txt
CMD python shorttestpath/manage.py runserver 0.0.0.0:8000
