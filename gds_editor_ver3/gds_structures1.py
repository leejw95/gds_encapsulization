
import warnings
from gds_editor_ver3 import user_define_exceptions
import struct
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record
from gds_editor_ver3 import gds_elements

class GDS_STRUCTURE():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNSTR = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRNAME = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRCLASS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = []
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDSTR = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNSTR.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRNAME.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRCLASS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRCLASS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS) > 20):
            _227690d7c3030c812d93d4e09295831f6e820ab866e0d851852f1b5e4c50c5d2.warn('Demo version supports maximum 20 elements per structure.')
        for _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS[:20]:
            _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDSTR.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BGNSTR']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNSTR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BGNSTR()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNSTR.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRNAME']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRNAME = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_STRNAME()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRNAME.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRNAME']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRCLASS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_STRCLASS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRCLASS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDSTR']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDSTR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ENDSTR()
                del a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5
                break
            elif ((a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOUNDARY']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PATH']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SREF']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['AREF']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['TEXT']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['NODE']) or (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOX'])):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDEL']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _4ee048060104cbc41a2f153e20d14b3ffb1930c274f401b4c4a29d19d3c4999f = d35f141520a155cbc70cb48892971a1fd6e0470f7e6eecba9792cb9da15bf110.GDS_ELEMENT()
                        _4ee048060104cbc41a2f153e20d14b3ffb1930c274f401b4c4a29d19d3c4999f.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.append(_4ee048060104cbc41a2f153e20d14b3ffb1930c274f401b4c4a29d19d3c4999f)
                        _4ee048060104cbc41a2f153e20d14b3ffb1930c274f401b4c4a29d19d3c4999f = None
                        del _4ee048060104cbc41a2f153e20d14b3ffb1930c274f401b4c4a29d19d3c4999f
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
