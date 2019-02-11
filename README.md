# span-example

## Training

```bash
# get the source code
git clone git@github.com:span-ai/span-example.git
cd span-example/

# for this demo the training step serialises the model as model.pickle
python3 train.py
```

## Serving

```bash
# build the server docker image
docker build -t winequality .

# run the server (CTRL-C to stop)
docker run --rm -p 50051:50051 --name wine winequality
```

Test the server from another terminal.

```bash
# create a python environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements-serve.txt

# generate the grpc stubs
python3 -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. serve.proto

# run the client
python3 client.py
```
