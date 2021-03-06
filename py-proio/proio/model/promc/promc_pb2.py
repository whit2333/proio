# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proio/model/promc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proio/model/promc.proto',
  package='proio.model.promc',
  syntax='proto3',
  serialized_pb=_b('\n\x17proio/model/promc.proto\x12\x11proio.model.promc\"\xfc\x01\n\x08Particle\x12\x0e\n\x06gen_id\x18\x01 \x01(\r\x12\x0e\n\x06pdg_id\x18\x02 \x01(\x11\x12\x0e\n\x06status\x18\x03 \x01(\r\x12\x0c\n\x04mass\x18\x04 \x01(\x04\x12\n\n\x02Px\x18\x05 \x01(\x12\x12\n\n\x02Py\x18\x06 \x01(\x12\x12\n\n\x02Pz\x18\x07 \x01(\x12\x12\x0f\n\x07parents\x18\x08 \x03(\x04\x12\x10\n\x08\x63hildren\x18\t \x03(\x04\x12\x0f\n\x07\x62\x61rcode\x18\n \x01(\x11\x12\t\n\x01X\x18\x0b \x01(\x11\x12\t\n\x01Y\x18\x0c \x01(\x11\x12\t\n\x01Z\x18\r \x01(\x11\x12\t\n\x01T\x18\x0e \x01(\r\x12\x0e\n\x06weight\x18\x0f \x01(\x04\x12\x0e\n\x06\x63harge\x18\x10 \x01(\x11\x12\x0e\n\x06\x65nergy\x18\x11 \x01(\x12\x42I\n\x0bproio.modelB\x05PromcZ3github.com/decibelcooper/proio/go-proio/model/promcb\x06proto3')
)




_PARTICLE = _descriptor.Descriptor(
  name='Particle',
  full_name='proio.model.promc.Particle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gen_id', full_name='proio.model.promc.Particle.gen_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pdg_id', full_name='proio.model.promc.Particle.pdg_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='proio.model.promc.Particle.status', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mass', full_name='proio.model.promc.Particle.mass', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Px', full_name='proio.model.promc.Particle.Px', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Py', full_name='proio.model.promc.Particle.Py', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Pz', full_name='proio.model.promc.Particle.Pz', index=6,
      number=7, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parents', full_name='proio.model.promc.Particle.parents', index=7,
      number=8, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='proio.model.promc.Particle.children', index=8,
      number=9, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barcode', full_name='proio.model.promc.Particle.barcode', index=9,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='X', full_name='proio.model.promc.Particle.X', index=10,
      number=11, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='proio.model.promc.Particle.Y', index=11,
      number=12, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Z', full_name='proio.model.promc.Particle.Z', index=12,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='T', full_name='proio.model.promc.Particle.T', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='proio.model.promc.Particle.weight', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge', full_name='proio.model.promc.Particle.charge', index=15,
      number=16, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='energy', full_name='proio.model.promc.Particle.energy', index=16,
      number=17, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=299,
)

DESCRIPTOR.message_types_by_name['Particle'] = _PARTICLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Particle = _reflection.GeneratedProtocolMessageType('Particle', (_message.Message,), dict(
  DESCRIPTOR = _PARTICLE,
  __module__ = 'proio.model.promc_pb2'
  # @@protoc_insertion_point(class_scope:proio.model.promc.Particle)
  ))
_sym_db.RegisterMessage(Particle)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\013proio.modelB\005PromcZ3github.com/decibelcooper/proio/go-proio/model/promc'))
# @@protoc_insertion_point(module_scope)
