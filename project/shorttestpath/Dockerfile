FROM python:3
RUN apt-get update
RUN git clone https://github.com/sambapython/Usbatch.git
RUN cp -rf ./Usbatch/project/shorttestpath ./
ENTRYPOINT ["shorttestpath/entry.sh"]
