
import warnings
from gds_editor_ver3 import user_define_exceptions
import struct
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record
from gds_editor_ver3 import gds_structures
'_HEADER=None\n_BGNLIB=None\n_LIBDIRSIZE=None\n_SRFNAME=None\n_LIBSECUR=None\n_LIBNAME=None\n_REFLIBS=None\n_FONTS=None\n_ATTRTABLE=None\n_GENERATIONS=None\n_FORMATTYPE=None\n_UNITS=None\n_STRUCTURES=None\n_ENDLIB=None'

class GDS_STREAM():

    def __init__(self):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._HEADER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNLIB = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBDIRSIZE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SRFNAME = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBSECUR = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBNAME = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._REFLIBS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FONTS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ATTRTABLE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GENERATIONS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FORMATTYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._UNITS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRUCTURES = []
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDLIB = None
    '\n    \n    read binary record data --> classify the binary data  \n    \n    record\n    [record header:[record length, record type,data type], data]\n    \n    '

    def read_record(self, gds_file):
        _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.read(4)
        if ((not _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a) or (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a) < 4)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.EndofFileError
        (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82) = _04b84ba1d4f1d361b3c997cde2a41d0b6bc74b60bcda9e7651f4c9b4dd6e1e70.unpack('>HH', _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a)
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb < 4):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectRecordSize('record size is too small')
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb % 2):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectRecordSize('incorrect record size')
        ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb -= 4
        _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596 = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.read(ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb)
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb != _71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.EndofFileError
        _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51 = (c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82 & 255)
        _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a = ((c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82 >> 8) & 255)
        _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.seek((- (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4)), 1)
        _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.read((ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4))
        ' return record size, record tag, record type, record data type, record data, record binary stream'
        return [(ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4), c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c]

    def write_binary_gds_stream(self, gds_file):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._HEADER.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNLIB.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBDIRSIZE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBDIRSIZE.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SRFNAME != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SRFNAME.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBSECUR != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBSECUR.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBNAME.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._REFLIBS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._REFLIBS.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FONTS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FONTS.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ATTRTABLE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ATTRTABLE.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GENERATIONS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GENERATIONS.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FORMATTYPE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FORMATTYPE.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._UNITS.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRUCTURES) > 20):
            _227690d7c3030c812d93d4e09295831f6e820ab866e0d851852f1b5e4c50c5d2.warn('Demo version supports maximum 20 structure.')
        for _520cdb563bf80b193aab6aad62781a9647c75dbf76748117299c7dac0ae63a87 in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRUCTURES[:20]:
            _520cdb563bf80b193aab6aad62781a9647c75dbf76748117299c7dac0ae63a87.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDLIB.write_binary_gds_stream(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)

    def read_binary_gds_stream(self, gds_file):
        '\n        read record binary stream separately\n        '
        while True:
            'extract binary gds data until units'
            [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.read_record(gds_file=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
            if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['HEADER'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._HEADER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_HEADER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._HEADER.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BGNLIB'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNLIB = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BGNLIB()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNLIB.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LIBDIRSIZE'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBDIRSIZE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LIBDIRSIZE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBDIRSIZE.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SRFNAME'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SRFNAME = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_SRFNAME()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SRFNAME.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LIBSECUR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBSECUR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LIBSECUR()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBSECUR.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LIBNAME'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBNAME = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LIBNAME()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LIBNAME.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['REFLIBS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._REFLIBS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_REFLIBS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._REFLIBS.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['FONTS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FONTS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_FONTS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FONTS.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ATTRTABLE'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ATTRTABLE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ATTRTABLE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ATTRTABLE.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['GENERATIONS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GENERATIONS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_GENERATIONS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GENERATIONS.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['FORMAT'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                'extract FORMATTYPE binary data'
                while True:
                    [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.read_record(gds_file=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
                    if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['UNITS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FORMATTYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_FORMATTYPE()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._FORMATTYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
                        del a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5
                        _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.seek((- ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb), 1)
                        break
                    else:
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['UNITS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._UNITS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_UNITS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._UNITS.read_binary_gds_stream(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
                break
            "    \n            elif gds_tags.DICT['FORMAT']==record_tag:\n                self._FORMATTYPE.append(record_binary_stream)\n            "
            "\n                while True: \n                    [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)\n                    if gds_tags.DICT['MASK']==record_tag:\n                        self._FORMATTYPE.append(record_binary_stream)\n                    elif gds_tags.DICT['ENDMASKS']:\n                        self._FORMATTYPE.append(record_binary_stream)\n                        break\n                    elif gds_tags.DICT['UNITS']==record_tag:\n            "
            '\n                        gds_file.seek(-record_size,1)\n                        break\n            '
        'extract structures & endlib'
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
            a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = None
            [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.read_record(gds_file=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
            if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BGNSTR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                'extract each binary structure data'
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                while True:
                    [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.read_record(gds_file=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
                    if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDSTR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = _6d423e1f15dd9480c4c0e66185d073ba511a802de60979d6a6d9c66f079ee2a7.GDS_STRUCTURE()
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRUCTURES.append(a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5)
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = None
                        del a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5
                        break
                    else:
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDLIB'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDLIB = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ENDLIB()
                del a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5
                'delete temp=[] in the while loop'
                break
    '\n    _HEADER=None\n    _BGNLIB=None\n    _LIBDIRSIZE=None\n    _SRFNAME=None\n    _LIBSECUR=None\n    _LIBNAME=None\n    _REFLIBS=None\n    _FONTS=None\n    _ATTRTABLE=None\n    _GENERATIONS=None\n    _FORMATTYPE=None\n    _UNITS=None\n    _STRUCTURES=None\n    _ENDLIB=None\n    '
    '\n    _gds_stream=(_HEADER, _BGNLIB, _LIBDIRSIZE,_SRFNAME,_LIBSECUR, _LIBNAME,                 _REFLIBS, _FONTS, _ATTRTABLE,_GENERATIONS,_FORMATTYPE,_UNITS,                _STRUCTURES,_ENDLIB)\n                '
    '\n    GDS stream format:\n        .. productionlist::\n            library: HEADER\n                   : BGNLIB\n                   : [LIBDIRSIZE]\n                   : [SRFNAME]\n                   : [LIBSECUR]\n                   : LIBNAME\n                   : [REFLIBS]\n                   : [FONTS]\n                   : [ATTRTABLE]\n                   : [GENERATIONS]\n                   : [`format`]\n                   : UNITS\n                   : {`structure`}*\n                   : ENDLIB\n            format: FORMAT\n                  : [MASK+ ENDMASKS]\n    '
