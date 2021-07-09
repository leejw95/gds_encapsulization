
from gds_editor_ver3 import user_define_exceptions
import struct
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record

class GDS_ELEMENT():

    def __init__(self, gds_data=None, _GDS_ELEMENT_NAME=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY = []
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEL = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GDS_ELEMENT_NAME = _7fb0fe5566ef655302a9f983d637f6f6ec5323abc767041933f3584479763122

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        "\n        if '_BOUNDARY' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_PATH' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_SREF' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_AREF' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_TEXT' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_NODE' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        elif '_BOX' in dir(self._ELEMENTS):\n            self._ELEMENTS.write_binary_gds_stream( binary_gds_stream)\n        "
        if _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GDS_ELEMENT_NAME:
            _8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2 = _83c801bbfa84fb042b256d9960a33d4eb4af5dd7c2f9f9013bc53447b38d0de8()
            _8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2._PROPATTR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPATTR()
            _8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2._PROPATTR.propattr = 126
            _8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2._PROPVALUE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPVALUE()
            _8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2._PROPVALUE.propvalue = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GDS_ELEMENT_NAME
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY.append(_8b3da8ce535d92a34dbc06b1b05a827a21e68d317029b4023bd224ccae8977c2)
            _40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b = _83c801bbfa84fb042b256d9960a33d4eb4af5dd7c2f9f9013bc53447b38d0de8()
            _40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b._PROPATTR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPATTR()
            _40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b._PROPATTR.propattr = 61
            _40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b._PROPVALUE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPVALUE()
            _40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b._PROPVALUE.propvalue = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GDS_ELEMENT_NAME
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY.append(_40959bc3241b7a9569ef55d96d04a2f93cf599e48ec88c0931ac30aa91e80b4b)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY != []):
            for de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(0, _71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY)):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY[de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7].write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEL.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOUNDARY']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _2bf3c770706d15db96cf48c8cc1e81ed39a8b024af466daefcb5ae8184cd03ab()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PATH']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _26e010dee60c880a20909a1be854e27fe46f6fff261f516b7961ec861e5de783()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SREF']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = d8270ec5148dd8c20ef81ae2bf9d20ff0497f031da90a5cb98717cb0221dacd9()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['AREF']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _337b53eaf77ced06e88cc8de7732de4d83961bcab5ecf0fa17be525d87ca7ec2()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['TEXT']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRING']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _3d5e1cc9df34e2e19138d5900f8e482ccd472f5bac21720408568c570bf2e46e()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['NODE']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _3ad6272e18968eb95290fb29bbf523de31e9ed3ddc8e922ca4c4f45c527d6925()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOX']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS = _17244e098d31db3d376043fab0d0773afa528ee66670f368e68b0ff3e396ef69()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELEMENTS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PROPATTR']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                c0c040aaacf44e69432ae3b759b62fbfadebb156ff3ffe8fe01d55c844134bd1 = _83c801bbfa84fb042b256d9960a33d4eb4af5dd7c2f9f9013bc53447b38d0de8()
                c0c040aaacf44e69432ae3b759b62fbfadebb156ff3ffe8fe01d55c844134bd1.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY.append(c0c040aaacf44e69432ae3b759b62fbfadebb156ff3ffe8fe01d55c844134bd1)
                c0c040aaacf44e69432ae3b759b62fbfadebb156ff3ffe8fe01d55c844134bd1 = None
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b, c0c040aaacf44e69432ae3b759b62fbfadebb156ff3ffe8fe01d55c844134bd1
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDEL']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEL = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ENDEL()
                break
        for fc9184134ae5672878413fff088dd0a1db30d18dc2a855da6345c7ab592ac46f in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPERTY:
            if (fc9184134ae5672878413fff088dd0a1db30d18dc2a855da6345c7ab592ac46f._PROPATTR.propattr is 61):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._GDS_ELEMENT_NAME = fc9184134ae5672878413fff088dd0a1db30d18dc2a855da6345c7ab592ac46f._PROPVALUE.propvalue.decode()
                break

class GDS_BOUNDARY():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOUNDARY = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOUNDARY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOUNDARY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOUNDARY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BOUNDARY()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PLEX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PLEX()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['DATATYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_DATATYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_PATH():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATH = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNEXTN = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEXTN = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATH.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNEXTN != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNEXTN.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEXTN != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEXTN.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PATH']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATH = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PATH()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PLEX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PLEX()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['DATATYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_DATATYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DATATYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PATHTYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PATHTYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['WIDTH']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_WIDTH()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BGNEXTN']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNEXTN = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BGNEXTN()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BGNEXTN.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ENDEXTN']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEXTN = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ENDEXTN()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ENDEXTN.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_SREF():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SREF = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SREF.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SREF']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SREF = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_SREF()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SNAME']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_SNAME()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRANS']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                if ((_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['MAG']) or (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE'])):
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                    if (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE']):
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = aefca0b9ec2d55ca7da7ec3234e1a491568b3b1fce052526b7dd87899d8c90f4()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_AREF():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._AREF = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._COLROW = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._AREF.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._COLROW.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['AREF']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._AREF = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_AREF()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['SNAME']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_SNAME()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._SNAME.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRANS']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                if ((_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['MAG']) or (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE'])):
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                    if (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE']):
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = aefca0b9ec2d55ca7da7ec3234e1a491568b3b1fce052526b7dd87899d8c90f4()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['COLROW']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._COLROW = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_COLROW()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._COLROW.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_TEXT():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXT = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTBODY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXT.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTBODY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['TEXT']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXT = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_TEXT()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PLEX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PLEX()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['TEXTTYPE']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                while True:
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRING']):
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTBODY = _9955856d4a273e12d982e7961c709df623347781abb9f1d918d3bb93be0da5bd()
                        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTBODY.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                        del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
                        break
                    else:
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                break

class GDS_NODE():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODETYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODETYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['NODE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_NODE()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PLEX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PLEX()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['NODETYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODETYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_NODETYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NODETYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_BOX():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOX = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOXTYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOXTYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BOX()
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ELFLAGS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ELFLAGS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ELFLAGS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PLEX']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PLEX()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PLEX.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['LAYER']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_LAYER()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._LAYER.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['BOXTYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOXTYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_BOXTYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._BOXTYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_TEXTBODY():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTTYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PRESENTATION = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRING = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTTYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PRESENTATION != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PRESENTATION.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRING.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['TEXTTYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTTYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_TEXTTYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._TEXTTYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PRESENTATION']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PRESENTATION = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PRESENTATION()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PRESENTATION.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PATHTYPE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PATHTYPE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PATHTYPE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['WIDTH']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_WIDTH()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._WIDTH.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRANS']):
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                if ((_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['MAG']) or (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE'])):
                    a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                    d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                    if (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089[0][0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE']):
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
                        d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b.append(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = aefca0b9ec2d55ca7da7ec3234e1a491568b3b1fce052526b7dd87899d8c90f4()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.read_binary_gds_stream(d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b)
                d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b = []
                del d69954748849ed25f53cd0e75f87cebb8329aedc9e4077455f4188a5f3f5463b
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['XY']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_XY()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._XY.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRING']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRING = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_STRING()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRING.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break

class GDS_STRANS():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MAG = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ANGLE = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MAG != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MAG.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        if (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ANGLE != None):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ANGLE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['STRANS']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_STRANS()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._STRANS.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['MAG']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MAG = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_MAG()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MAG.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['ANGLE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ANGLE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_ANGLE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._ANGLE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            if (_54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089 == []):
                break

class GDS_PROPERTY():

    def __init__(self, gds_data=None):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPATTR = None
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPVALUE = None

    def write_binary_gds_stream(self, binary_gds_stream):
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPATTR.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)
        _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPVALUE.write_binary_gds_stream(b0176a223292ebdf290c7fea9db298a8a87263365a6e650fa9a177dc0310fe3c)

    def read_binary_gds_stream(self, gds_data):
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = _54d8ed55630b9293d7edf4a8934ac7c509efbb9abc936084cf748a086b1e7089.pop(0)
            if (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PROPATTR']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPATTR = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPATTR()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPATTR.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
            elif (a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0] == _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f.DICT['PROPVALUE']):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPVALUE = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.GDS_PROPVALUE()
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PROPVALUE.read_binary_gds_stream(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[0], a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5[1])
                break
