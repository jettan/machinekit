# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: machinetalk/protobuf/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from machinetalk.protobuf import nanopb_pb2 as machinetalk_dot_protobuf_dot_nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='machinetalk/protobuf/config.proto',
  package='machinetalk',
  syntax='proto2',
  serialized_pb=_b('\n!machinetalk/protobuf/config.proto\x12\x0bmachinetalk\x1a!machinetalk/protobuf/nanopb.proto\"V\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12*\n\x08\x65ncoding\x18\x02 \x02(\x0e\x32\x18.machinetalk.FileContent\x12\x0c\n\x04\x62lob\x18\x03 \x01(\x0c:\x06\x92?\x03H\xc8\x01\"\x95\x01\n\x0b\x41pplication\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12*\n\x04type\x18\x03 \x01(\x0e\x32\x1c.machinetalk.ApplicationType\x12\x0e\n\x06weburi\x18\x04 \x01(\t\x12\x1f\n\x04\x66ile\x18\x05 \x03(\x0b\x32\x11.machinetalk.File:\x06\x92?\x03H\xc9\x01\"1\n\nStdoutLine\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x0c\n\x04line\x18\x02 \x01(\t:\x06\x92?\x03H\xca\x01\"Y\n\x0bMachineInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x0f\n\x07variant\x18\x04 \x01(\t:\x06\x92?\x03H\xcb\x01\"\xc8\x02\n\x08Launcher\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12 \n\x05image\x18\x04 \x01(\x0b\x32\x11.machinetalk.File\x12&\n\x04info\x18\x05 \x01(\x0b\x32\x18.machinetalk.MachineInfo\x12\x0f\n\x07running\x18\x06 \x01(\x08\x12\x13\n\x0bterminating\x18\x07 \x01(\x08\x12\x0f\n\x07\x63ommand\x18\x08 \x01(\t\x12\r\n\x05shell\x18\t \x01(\x08\x12\'\n\x06output\x18\n \x03(\x0b\x32\x17.machinetalk.StdoutLine\x12\x12\n\nreturncode\x18\x0b \x01(\x05\x12\x0f\n\x07workdir\x18\x0c \x01(\t\x12\x10\n\x08priority\x18\r \x01(\r\x12\x12\n\nimportance\x18\x0e \x01(\r:\x06\x92?\x03H\xcc\x01*<\n\x0f\x41pplicationType\x12\x0b\n\x07QT5_QML\x10\x01\x12\x0c\n\x08GLADEVCP\x10\x02\x12\x0e\n\nJAVASCRIPT\x10\x03*&\n\x0b\x46ileContent\x12\r\n\tCLEARTEXT\x10\x01\x12\x08\n\x04ZLIB\x10\x02')
  ,
  dependencies=[machinetalk_dot_protobuf_dot_nanopb__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_APPLICATIONTYPE = _descriptor.EnumDescriptor(
  name='ApplicationType',
  full_name='machinetalk.ApplicationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='QT5_QML', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLADEVCP', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JAVASCRIPT', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=798,
  serialized_end=858,
)
_sym_db.RegisterEnumDescriptor(_APPLICATIONTYPE)

ApplicationType = enum_type_wrapper.EnumTypeWrapper(_APPLICATIONTYPE)
_FILECONTENT = _descriptor.EnumDescriptor(
  name='FileContent',
  full_name='machinetalk.FileContent',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLEARTEXT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZLIB', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=860,
  serialized_end=898,
)
_sym_db.RegisterEnumDescriptor(_FILECONTENT)

FileContent = enum_type_wrapper.EnumTypeWrapper(_FILECONTENT)
QT5_QML = 1
GLADEVCP = 2
JAVASCRIPT = 3
CLEARTEXT = 1
ZLIB = 2



_FILE = _descriptor.Descriptor(
  name='File',
  full_name='machinetalk.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='machinetalk.File.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='machinetalk.File.encoding', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blob', full_name='machinetalk.File.blob', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\310\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=171,
)


_APPLICATION = _descriptor.Descriptor(
  name='Application',
  full_name='machinetalk.Application',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='machinetalk.Application.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='machinetalk.Application.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='machinetalk.Application.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weburi', full_name='machinetalk.Application.weburi', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file', full_name='machinetalk.Application.file', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\311\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=323,
)


_STDOUTLINE = _descriptor.Descriptor(
  name='StdoutLine',
  full_name='machinetalk.StdoutLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='machinetalk.StdoutLine.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line', full_name='machinetalk.StdoutLine.line', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\312\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=374,
)


_MACHINEINFO = _descriptor.Descriptor(
  name='MachineInfo',
  full_name='machinetalk.MachineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='machinetalk.MachineInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='machinetalk.MachineInfo.manufacturer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='machinetalk.MachineInfo.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant', full_name='machinetalk.MachineInfo.variant', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\313\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=465,
)


_LAUNCHER = _descriptor.Descriptor(
  name='Launcher',
  full_name='machinetalk.Launcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='machinetalk.Launcher.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='machinetalk.Launcher.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='machinetalk.Launcher.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image', full_name='machinetalk.Launcher.image', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='machinetalk.Launcher.info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='running', full_name='machinetalk.Launcher.running', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='terminating', full_name='machinetalk.Launcher.terminating', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='machinetalk.Launcher.command', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shell', full_name='machinetalk.Launcher.shell', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='machinetalk.Launcher.output', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='returncode', full_name='machinetalk.Launcher.returncode', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='workdir', full_name='machinetalk.Launcher.workdir', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='machinetalk.Launcher.priority', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='importance', full_name='machinetalk.Launcher.importance', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\314\001')),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=796,
)

_FILE.fields_by_name['encoding'].enum_type = _FILECONTENT
_APPLICATION.fields_by_name['type'].enum_type = _APPLICATIONTYPE
_APPLICATION.fields_by_name['file'].message_type = _FILE
_LAUNCHER.fields_by_name['image'].message_type = _FILE
_LAUNCHER.fields_by_name['info'].message_type = _MACHINEINFO
_LAUNCHER.fields_by_name['output'].message_type = _STDOUTLINE
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['Application'] = _APPLICATION
DESCRIPTOR.message_types_by_name['StdoutLine'] = _STDOUTLINE
DESCRIPTOR.message_types_by_name['MachineInfo'] = _MACHINEINFO
DESCRIPTOR.message_types_by_name['Launcher'] = _LAUNCHER
DESCRIPTOR.enum_types_by_name['ApplicationType'] = _APPLICATIONTYPE
DESCRIPTOR.enum_types_by_name['FileContent'] = _FILECONTENT

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(
  DESCRIPTOR = _FILE,
  __module__ = 'machinetalk.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.File)
  ))
_sym_db.RegisterMessage(File)

Application = _reflection.GeneratedProtocolMessageType('Application', (_message.Message,), dict(
  DESCRIPTOR = _APPLICATION,
  __module__ = 'machinetalk.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.Application)
  ))
_sym_db.RegisterMessage(Application)

StdoutLine = _reflection.GeneratedProtocolMessageType('StdoutLine', (_message.Message,), dict(
  DESCRIPTOR = _STDOUTLINE,
  __module__ = 'machinetalk.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.StdoutLine)
  ))
_sym_db.RegisterMessage(StdoutLine)

MachineInfo = _reflection.GeneratedProtocolMessageType('MachineInfo', (_message.Message,), dict(
  DESCRIPTOR = _MACHINEINFO,
  __module__ = 'machinetalk.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.MachineInfo)
  ))
_sym_db.RegisterMessage(MachineInfo)

Launcher = _reflection.GeneratedProtocolMessageType('Launcher', (_message.Message,), dict(
  DESCRIPTOR = _LAUNCHER,
  __module__ = 'machinetalk.protobuf.config_pb2'
  # @@protoc_insertion_point(class_scope:machinetalk.Launcher)
  ))
_sym_db.RegisterMessage(Launcher)


_FILE.has_options = True
_FILE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\310\001'))
_APPLICATION.has_options = True
_APPLICATION._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\311\001'))
_STDOUTLINE.has_options = True
_STDOUTLINE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\312\001'))
_MACHINEINFO.has_options = True
_MACHINEINFO._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\313\001'))
_LAUNCHER.has_options = True
_LAUNCHER._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\003H\314\001'))
# @@protoc_insertion_point(module_scope)
