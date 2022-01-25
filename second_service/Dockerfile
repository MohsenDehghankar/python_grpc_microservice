FROM python:3.6

RUN mkdir /service

COPY protos/ /service/protos/

COPY second_service/ /service/second_service/

COPY scripts/run_service.sh /service/second_service/

WORKDIR /service/second_service

RUN python -m pip install --upgrade pip

RUN python -m pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I .. --python_out=. --grpc_python_out=. ../protos/first_service/v1/first_service.proto \
     ../protos/second_service/v1/second_service.proto

EXPOSE 50051

ENTRYPOINT [ "./run_service.sh" ]
