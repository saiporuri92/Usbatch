FROM python:3
RUN apt-get update
RUN git clone https://github.com/sambapython/Usbatch.git
RUN cp -rf ./Usbatch/project/shorttestpath ./
RUN chmod -R 777 ./shorttestpath
ENTRYPOINT ["shorttestpath/entry.sh"]
