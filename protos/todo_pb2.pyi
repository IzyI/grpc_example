from protos import approver_pb2 as _approver_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTodoRequest(_message.Message):
    __slots__ = ["completed", "day", "name"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    day: int
    name: str
    def __init__(self, name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class CreateTodoResponse(_message.Message):
    __slots__ = ["todo"]
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class DeleteTodoRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteTodoResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListTodosRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListTodosResponse(_message.Message):
    __slots__ = ["todos"]
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[Todo]
    def __init__(self, todos: _Optional[_Iterable[_Union[Todo, _Mapping]]] = ...) -> None: ...

class ReadTodoApproverResponse(_message.Message):
    __slots__ = ["approver", "todo"]
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    TODO_FIELD_NUMBER: _ClassVar[int]
    approver: _approver_pb2.Approver
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ..., approver: _Optional[_Union[_approver_pb2.Approver, _Mapping]] = ...) -> None: ...

class ReadTodoRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ReadTodoResponse(_message.Message):
    __slots__ = ["todo"]
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...

class Todo(_message.Message):
    __slots__ = ["completed", "day", "id", "name"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    day: int
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ..., day: _Optional[int] = ...) -> None: ...

class UpdateTodoRequest(_message.Message):
    __slots__ = ["completed", "id", "name"]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ...) -> None: ...

class UpdateTodoResponse(_message.Message):
    __slots__ = ["todo"]
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: Todo
    def __init__(self, todo: _Optional[_Union[Todo, _Mapping]] = ...) -> None: ...
