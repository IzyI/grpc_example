# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/user.proto\x12\x04user\x1a\x1bgoogle/protobuf/empty.proto\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\",\n\x10ReadUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User2I\n\x0bUserService\x12:\n\x08ReadUser\x12\x16.google.protobuf.Empty\x1a\x16.user.ReadUserResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USER._serialized_start=56
  _USER._serialized_end=88
  _READUSERRESPONSE._serialized_start=90
  _READUSERRESPONSE._serialized_end=134
  _USERSERVICE._serialized_start=136
  _USERSERVICE._serialized_end=209
# @@protoc_insertion_point(module_scope)
