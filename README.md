# gRPC_example
gRPC example

команда для генерации интерфейсов из protobaf файлов:  
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto