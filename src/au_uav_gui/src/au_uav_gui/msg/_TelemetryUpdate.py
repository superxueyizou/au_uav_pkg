"""autogenerated by genpy from AU_UAV_GUI/TelemetryUpdate.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class TelemetryUpdate(genpy.Message):
  _md5sum = "53cd950963d7a5c403c785f8c0a2ffa7"
  _type = "AU_UAV_GUI/TelemetryUpdate"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Header telemetryHeader
int32 planeID
float64 currentLatitude
float64 currentLongitude
float64 currentAltitude
float64 destLatitude
float64 destLongitude
float64 destAltitude
float64 groundSpeed
float64 targetBearing
int64 currentWaypointIndex
float64 distanceToDestination

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['telemetryHeader','planeID','currentLatitude','currentLongitude','currentAltitude','destLatitude','destLongitude','destAltitude','groundSpeed','targetBearing','currentWaypointIndex','distanceToDestination']
  _slot_types = ['std_msgs/Header','int32','float64','float64','float64','float64','float64','float64','float64','float64','int64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       telemetryHeader,planeID,currentLatitude,currentLongitude,currentAltitude,destLatitude,destLongitude,destAltitude,groundSpeed,targetBearing,currentWaypointIndex,distanceToDestination

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TelemetryUpdate, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.telemetryHeader is None:
        self.telemetryHeader = std_msgs.msg.Header()
      if self.planeID is None:
        self.planeID = 0
      if self.currentLatitude is None:
        self.currentLatitude = 0.
      if self.currentLongitude is None:
        self.currentLongitude = 0.
      if self.currentAltitude is None:
        self.currentAltitude = 0.
      if self.destLatitude is None:
        self.destLatitude = 0.
      if self.destLongitude is None:
        self.destLongitude = 0.
      if self.destAltitude is None:
        self.destAltitude = 0.
      if self.groundSpeed is None:
        self.groundSpeed = 0.
      if self.targetBearing is None:
        self.targetBearing = 0.
      if self.currentWaypointIndex is None:
        self.currentWaypointIndex = 0
      if self.distanceToDestination is None:
        self.distanceToDestination = 0.
    else:
      self.telemetryHeader = std_msgs.msg.Header()
      self.planeID = 0
      self.currentLatitude = 0.
      self.currentLongitude = 0.
      self.currentAltitude = 0.
      self.destLatitude = 0.
      self.destLongitude = 0.
      self.destAltitude = 0.
      self.groundSpeed = 0.
      self.targetBearing = 0.
      self.currentWaypointIndex = 0
      self.distanceToDestination = 0.

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
      buff.write(_struct_3I.pack(_x.telemetryHeader.seq, _x.telemetryHeader.stamp.secs, _x.telemetryHeader.stamp.nsecs))
      _x = self.telemetryHeader.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i8dqd.pack(_x.planeID, _x.currentLatitude, _x.currentLongitude, _x.currentAltitude, _x.destLatitude, _x.destLongitude, _x.destAltitude, _x.groundSpeed, _x.targetBearing, _x.currentWaypointIndex, _x.distanceToDestination))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.telemetryHeader is None:
        self.telemetryHeader = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.telemetryHeader.seq, _x.telemetryHeader.stamp.secs, _x.telemetryHeader.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.telemetryHeader.frame_id = str[start:end].decode('utf-8')
      else:
        self.telemetryHeader.frame_id = str[start:end]
      _x = self
      start = end
      end += 84
      (_x.planeID, _x.currentLatitude, _x.currentLongitude, _x.currentAltitude, _x.destLatitude, _x.destLongitude, _x.destAltitude, _x.groundSpeed, _x.targetBearing, _x.currentWaypointIndex, _x.distanceToDestination,) = _struct_i8dqd.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.telemetryHeader.seq, _x.telemetryHeader.stamp.secs, _x.telemetryHeader.stamp.nsecs))
      _x = self.telemetryHeader.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i8dqd.pack(_x.planeID, _x.currentLatitude, _x.currentLongitude, _x.currentAltitude, _x.destLatitude, _x.destLongitude, _x.destAltitude, _x.groundSpeed, _x.targetBearing, _x.currentWaypointIndex, _x.distanceToDestination))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.telemetryHeader is None:
        self.telemetryHeader = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.telemetryHeader.seq, _x.telemetryHeader.stamp.secs, _x.telemetryHeader.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.telemetryHeader.frame_id = str[start:end].decode('utf-8')
      else:
        self.telemetryHeader.frame_id = str[start:end]
      _x = self
      start = end
      end += 84
      (_x.planeID, _x.currentLatitude, _x.currentLongitude, _x.currentAltitude, _x.destLatitude, _x.destLongitude, _x.destAltitude, _x.groundSpeed, _x.targetBearing, _x.currentWaypointIndex, _x.distanceToDestination,) = _struct_i8dqd.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_i8dqd = struct.Struct("<i8dqd")
