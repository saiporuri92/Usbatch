FROM python:3
RUN apt-get update
RUN git clone https://github.com/sambapython/Usbatch.git
RUN cp -rf ./Usbatch/project/shorttestpath ./
RUN pip install -r shorttestpath/requirements.txt
ENTRYPOINT ["entry.sh"]
