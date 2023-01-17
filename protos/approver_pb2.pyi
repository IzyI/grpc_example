from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Approver(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _wrappers_pb2.BoolValue
    def __init__(self, status: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ReadApproverRequest(_message.Message):
    __slots__ = ["day"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    day: int
    def __init__(self, day: _Optional[int] = ...) -> None: ...

class ReadApproverResponse(_message.Message):
    __slots__ = ["approver"]
    APPROVER_FIELD_NUMBER: _ClassVar[int]
    approver: Approver
    def __init__(self, approver: _Optional[_Union[Approver, _Mapping]] = ...) -> None: ...
