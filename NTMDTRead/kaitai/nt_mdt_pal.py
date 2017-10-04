# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
import struct


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from .nt_mdt_color_table import NtMdtColorTable
class NtMdtPal(KaitaiStruct):
    """It is a color scheme for visualising SPM scans."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.signature = self._io.ensure_fixed_contents(struct.pack('26b', 78, 84, 45, 77, 68, 84, 32, 80, 97, 108, 101, 116, 116, 101, 32, 70, 105, 108, 101, 32, 32, 49, 46, 48, 48, 33))
        self.count = self._io.read_u4be()
        self.meta = [None] * (self.count)
        for i in range(self.count):
            self.meta[i] = self._root.Meta(self._io, self, self._root)

        self.unkn = self._io.read_bytes(3)

    class Meta(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unkn00 = self._io.read_bytes(3)
            self.color_table_ptr = self._io.read_u4le()
            self.colors_count = self._io.read_u4le()
            self.unkn11 = self._io.read_bytes(1)
            self.unkn12 = self._io.read_bytes(2)
            self.title_len = self._io.read_u2be()

        @property
        def color_table(self):
            if hasattr(self, '_m_color_table'):
                return self._m_color_table if hasattr(self, '_m_color_table') else None

            io = self._root._io
            _pos = io.pos()
            io.seek(self.color_table_ptr)
            self._m_color_table = NtMdtColorTable(self.colors_count, self.title_len, io)
            io.seek(_pos)
            return self._m_color_table if hasattr(self, '_m_color_table') else None



