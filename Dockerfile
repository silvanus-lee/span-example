FROM python:3.7 AS builder

WORKDIR /build

COPY requirements-serve-build.txt protos/serve.proto ./

RUN pip install --no-cache-dir -r requirements-serve-build.txt && \
    mkdir /grpc_temp && \
    python3 -m grpc_tools.protoc -I . --python_out=/grpc_temp --grpc_python_out=/grpc_temp serve.proto


FROM python:3.7

WORKDIR /app

COPY requirements-serve.txt .

RUN pip install --no-cache-dir -r requirements-serve.txt

COPY . .
COPY --from=builder /grpc_temp .

EXPOSE 50051

CMD ["python3", "./serve.py"]
