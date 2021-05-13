# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from grasping_msgs/GraspPlanningGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import grasping_msgs.msg
import sensor_msgs.msg
import shape_msgs.msg
import std_msgs.msg

class GraspPlanningGoal(genpy.Message):
  _md5sum = "1c3f3ed2a31c4c865c3032a4789c0df9"
  _type = "grasping_msgs/GraspPlanningGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
###########################################################
# This action is used when planning grasps for a single,
#  already known object, one object at a time.

# Object for which grasp planning is requested
Object object

# Name of group to plan with (optional)
string group_name

================================================================================
MSG: grasping_msgs/Object
###########################################################
# This message describes an object.

# Many of the geometric items below lack a stamp/frame_id,
# header stamp/frame_id should be used there
std_msgs/Header header

# An object might have a name
string name

# An object might have a known (named) support surface
string support_surface

# Objects might have properties, such as type/class, or color, etc.
ObjectProperty[] properties

###########################################################
# Objects have many possible descriptions
#  The following are the possible description formats

# Perception modules often represent an object as a cluster of points
#  Is considered valid if number of points > 0
sensor_msgs/PointCloud2 point_cluster

# MoveIt prefers solid primitives or meshes as a description of objects
shape_msgs/SolidPrimitive[] primitives
geometry_msgs/Pose[] primitive_poses

shape_msgs/Mesh[] meshes
geometry_msgs/Pose[] mesh_poses

# An object representing a support surface might be described by a plane
# Is considered valid if coefficients are not all 0s.
shape_msgs/Plane surface

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: grasping_msgs/ObjectProperty
###########################################################
# Other generic properties of an object
string name
string value

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field

================================================================================
MSG: shape_msgs/SolidPrimitive
# Define box, sphere, cylinder, cone 
# All shapes are defined to have their bounding boxes centered around 0,0,0.

uint8 BOX=1
uint8 SPHERE=2
uint8 CYLINDER=3
uint8 CONE=4

# The type of the shape
uint8 type


# The dimensions of the shape
float64[] dimensions

# The meaning of the shape dimensions: each constant defines the index in the 'dimensions' array

# For the BOX type, the X, Y, and Z dimensions are the length of the corresponding
# sides of the box.
uint8 BOX_X=0
uint8 BOX_Y=1
uint8 BOX_Z=2


# For the SPHERE type, only one component is used, and it gives the radius of
# the sphere.
uint8 SPHERE_RADIUS=0


# For the CYLINDER and CONE types, the center line is oriented along
# the Z axis.  Therefore the CYLINDER_HEIGHT (CONE_HEIGHT) component
# of dimensions gives the height of the cylinder (cone).  The
# CYLINDER_RADIUS (CONE_RADIUS) component of dimensions gives the
# radius of the base of the cylinder (cone).  Cone and cylinder
# primitives are defined to be circular. The tip of the cone is
# pointing up, along +Z axis.

uint8 CYLINDER_HEIGHT=0
uint8 CYLINDER_RADIUS=1

uint8 CONE_HEIGHT=0
uint8 CONE_RADIUS=1

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: shape_msgs/Mesh
# Definition of a mesh

# list of triangles; the index values refer to positions in vertices[]
MeshTriangle[] triangles

# the actual vertices that make up the mesh
geometry_msgs/Point[] vertices

================================================================================
MSG: shape_msgs/MeshTriangle
# Definition of a triangle's vertices
uint32[3] vertex_indices

================================================================================
MSG: shape_msgs/Plane
# Representation of a plane, using the plane equation ax + by + cz + d = 0

# a := coef[0]
# b := coef[1]
# c := coef[2]
# d := coef[3]

float64[4] coef
"""
  __slots__ = ['object','group_name']
  _slot_types = ['grasping_msgs/Object','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       object,group_name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GraspPlanningGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.object is None:
        self.object = grasping_msgs.msg.Object()
      if self.group_name is None:
        self.group_name = ''
    else:
      self.object = grasping_msgs.msg.Object()
      self.group_name = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.object.header.seq, _x.object.header.stamp.secs, _x.object.header.stamp.nsecs))
      _x = self.object.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.support_surface
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.object.properties)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.properties:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.object.point_cluster.header.seq, _x.object.point_cluster.header.stamp.secs, _x.object.point_cluster.header.stamp.nsecs))
      _x = self.object.point_cluster.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.object.point_cluster.height, _x.object.point_cluster.width))
      length = len(self.object.point_cluster.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.point_cluster.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.object.point_cluster.is_bigendian, _x.object.point_cluster.point_step, _x.object.point_cluster.row_step))
      _x = self.object.point_cluster.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.point_cluster.is_dense
      buff.write(_get_struct_B().pack(_x))
      length = len(self.object.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.primitives:
        _x = val1.type
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.dimensions))
      length = len(self.object.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.primitive_poses:
        _v1 = val1.position
        _x = _v1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.object.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(_get_struct_3I().pack(*val2.vertex_indices))
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.object.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.mesh_poses:
        _v3 = val1.position
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.orientation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(_get_struct_4d().pack(*self.object.surface.coef))
      _x = self.group_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.object is None:
        self.object = grasping_msgs.msg.Object()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.object.header.seq, _x.object.header.stamp.secs, _x.object.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.support_surface = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.support_surface = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.properties = []
      for i in range(0, length):
        val1 = grasping_msgs.msg.ObjectProperty()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.value = str[start:end]
        self.object.properties.append(val1)
      _x = self
      start = end
      end += 12
      (_x.object.point_cluster.header.seq, _x.object.point_cluster.header.stamp.secs, _x.object.point_cluster.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.point_cluster.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.point_cluster.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.object.point_cluster.height, _x.object.point_cluster.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.point_cluster.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.object.point_cluster.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.object.point_cluster.is_bigendian, _x.object.point_cluster.point_step, _x.object.point_cluster.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.object.point_cluster.is_bigendian = bool(self.object.point_cluster.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.object.point_cluster.data = str[start:end]
      start = end
      end += 1
      (self.object.point_cluster.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.object.point_cluster.is_dense = bool(self.object.point_cluster.is_dense)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dimensions = s.unpack(str[start:end])
        self.object.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v5 = val1.position
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v6 = val1.orientation
        _x = _v6
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.object.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = _get_struct_3I().unpack(str[start:end])
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.object.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v7 = val1.position
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v8 = val1.orientation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.object.mesh_poses.append(val1)
      start = end
      end += 32
      self.object.surface.coef = _get_struct_4d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.group_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.group_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.object.header.seq, _x.object.header.stamp.secs, _x.object.header.stamp.nsecs))
      _x = self.object.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.support_surface
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.object.properties)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.properties:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.value
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.object.point_cluster.header.seq, _x.object.point_cluster.header.stamp.secs, _x.object.point_cluster.header.stamp.nsecs))
      _x = self.object.point_cluster.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.object.point_cluster.height, _x.object.point_cluster.width))
      length = len(self.object.point_cluster.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.point_cluster.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.object.point_cluster.is_bigendian, _x.object.point_cluster.point_step, _x.object.point_cluster.row_step))
      _x = self.object.point_cluster.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.object.point_cluster.is_dense
      buff.write(_get_struct_B().pack(_x))
      length = len(self.object.primitives)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.primitives:
        _x = val1.type
        buff.write(_get_struct_B().pack(_x))
        length = len(val1.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.dimensions.tostring())
      length = len(self.object.primitive_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.primitive_poses:
        _v9 = val1.position
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = val1.orientation
        _x = _v10
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.object.meshes)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.meshes:
        length = len(val1.triangles)
        buff.write(_struct_I.pack(length))
        for val2 in val1.triangles:
          buff.write(val2.vertex_indices.tostring())
        length = len(val1.vertices)
        buff.write(_struct_I.pack(length))
        for val2 in val1.vertices:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      length = len(self.object.mesh_poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.object.mesh_poses:
        _v11 = val1.position
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = val1.orientation
        _x = _v12
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(self.object.surface.coef.tostring())
      _x = self.group_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.object is None:
        self.object = grasping_msgs.msg.Object()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.object.header.seq, _x.object.header.stamp.secs, _x.object.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.support_surface = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.support_surface = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.properties = []
      for i in range(0, length):
        val1 = grasping_msgs.msg.ObjectProperty()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.value = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.value = str[start:end]
        self.object.properties.append(val1)
      _x = self
      start = end
      end += 12
      (_x.object.point_cluster.header.seq, _x.object.point_cluster.header.stamp.secs, _x.object.point_cluster.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.object.point_cluster.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.object.point_cluster.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.object.point_cluster.height, _x.object.point_cluster.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.point_cluster.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.object.point_cluster.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.object.point_cluster.is_bigendian, _x.object.point_cluster.point_step, _x.object.point_cluster.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.object.point_cluster.is_bigendian = bool(self.object.point_cluster.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.object.point_cluster.data = str[start:end]
      start = end
      end += 1
      (self.object.point_cluster.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.object.point_cluster.is_dense = bool(self.object.point_cluster.is_dense)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.primitives = []
      for i in range(0, length):
        val1 = shape_msgs.msg.SolidPrimitive()
        start = end
        end += 1
        (val1.type,) = _get_struct_B().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.object.primitives.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.primitive_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v13 = val1.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = val1.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.object.primitive_poses.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.meshes = []
      for i in range(0, length):
        val1 = shape_msgs.msg.Mesh()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.triangles = []
        for i in range(0, length):
          val2 = shape_msgs.msg.MeshTriangle()
          start = end
          end += 12
          val2.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
          val1.triangles.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.vertices = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.vertices.append(val2)
        self.object.meshes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.object.mesh_poses = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose()
        _v15 = val1.position
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v16 = val1.orientation
        _x = _v16
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.object.mesh_poses.append(val1)
      start = end
      end += 32
      self.object.surface.coef = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=4)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.group_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.group_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_IBI = None
def _get_struct_IBI():
    global _struct_IBI
    if _struct_IBI is None:
        _struct_IBI = struct.Struct("<IBI")
    return _struct_IBI