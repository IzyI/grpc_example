# Simple gRPC example in python

This simple gRPC server has a structure:  
fast-api --> todo --> aprover   
fast-api --> user  

The service includes examples:
- health-check
- Token auth
- Reflectin
- The call chain (timeout, deadline)
- Error handling
- Tracing (opentelemetry)




Command to generate interfaces from protobuf files:  
python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto  
---
Run services:

uvicorn api:app --host 0.0.0.0 --port 5000  
python server_user_grpc.py  
python server_todo_grpc.py  
python server_approver_grpc.py  

---
Example grpcurl for the project: 

grpcurl  -H 'rpc-auth:bsduyfwe7r23f556re23fdtcvwai' -plaintext 0.0.0.0:50053 list  

grpcurl -plaintext -d '{"name":"5t 555 55","day":5,"completed":false}' 0.0.0.0:50051 todo.TodoService.CreateTodo  

grpcurl  -H 'rpc-auth:bsduyfwe7r23f556re23fdtcvwai' -plaintext 0.0.0.0:50053 grpc.health.v1.Health/Check  

grpcurl  -H 'rpc-auth:bsduyfwe7r23f556re23fdtcvwai' -plaintext 0.0.0.0:50053 user.UserService/ReadUser  
