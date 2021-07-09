
from gds_editor_ver3 import gds_stream
from gds_editor_ver3 import gds_structures
from gds_editor_ver3 import gds_tags
from gds_editor_ver3 import gds_record
from gds_editor_ver3 import gds_elements
import gds_editor_ver3
from datetime import datetime, MINYEAR
from gds_editor_ver3 import user_define_exceptions
from designs import DesignParameters
import copy

class _StickDiagram():

    def __init__(self):
        pass

    def exec_pass(self, code, library_manager):
        for _82a3537ff0dbce7eec35d69edc3a189ee6f17d82f353a553f9aa96cb0be3ce89 in e05e2801a9f798ed571be1d4534b0cd8622d526d8f6191a359a2bcc21fe4a045.class_name_dict:
            e9e8d4b193cfa45adf2725ec439027bfe4fe40e008978ea499817bbb547cd6e7()[_82a3537ff0dbce7eec35d69edc3a189ee6f17d82f353a553f9aa96cb0be3ce89] = e05e2801a9f798ed571be1d4534b0cd8622d526d8f6191a359a2bcc21fe4a045.libraries[_82a3537ff0dbce7eec35d69edc3a189ee6f17d82f353a553f9aa96cb0be3ce89]
        _2706c619fe73f0cf112473c6ee02e66c04e1c01c110b0c37b88d8eb509630c9f(_5694d08a2e53ffcae0c3103e5ad6f6076abd960eb1f8a56577040bc1028f702b)

    def RoundupMinSnapSpacing(self, _DesignParameter=None, _MinSnapSpacing=None):
        if ((_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 == None) or (e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc == None)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_DesignParameter or _MinSnapSpacing has incorrect valuse')
        return ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8((_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 / e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc)) + 1) * e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc)

    def RounddownMinSnapSpacing(self, _DesignParameter=None, _MinSnapSpacing=None):
        if ((_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 == None) or (e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc == None)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_DesignParameter or _MinSnapSpacing has incorrect valuse')
        return (_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8((_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 / e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc)) * e0709db7d8885ba475f59d3929e0d6d16e77f9dc79a28b229b144fdf0ff2b8dc)

    def TopLeft(self, element_name, hierarchy_list=None):
        if ('_DesignParameter' not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.__dict__):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('There is no DesignParameter.')
        if (aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714 not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid element name.')
        if (_2ed7d18ddc603c4554c3d52545864b0572478f0dfc887717b5f2823337471114 == None):
            _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
            if (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignParametertype'] == 1):
                return (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0], (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1] + _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_YWidth']))
        else:
            if (_2ed7d18ddc603c4554c3d52545864b0572478f0dfc887717b5f2823337471114[0] not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
                raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid Hierachy element Name.')
            _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[_2ed7d18ddc603c4554c3d52545864b0572478f0dfc887717b5f2823337471114[0]]
            for _2f77b64ea21be4b1bed5eaaf4c99ab0cc932fa574c8692154f111c256623adc8 in _2ed7d18ddc603c4554c3d52545864b0572478f0dfc887717b5f2823337471114:
                if (_2f77b64ea21be4b1bed5eaaf4c99ab0cc932fa574c8692154f111c256623adc8 not in _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DeisgnObj']._DesignParameter):
                    raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Ivalid Hierarchy element Name.')
                _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignObj']._DesignParameter[_2f77b64ea21be4b1bed5eaaf4c99ab0cc932fa574c8692154f111c256623adc8]
            _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignObj']._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
            return (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0], (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1] + _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_YWidth']))

    def TopRight(self, element_name):
        if ('_DesignParameter' not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.__dict__):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('There is no DesignParameter.')
        if (aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714 not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid element name.')
        _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
        if (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignParametertype'] == 1):
            return ((_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0] + _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XWidth']), (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1] + _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_YWidth']))

    def BottomLeft(self, element_name):
        if ('_DesignParameter' not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.__dict__):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('There is no DesignParameter.')
        if (aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714 not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid element name.')
        _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
        if (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignParametertype'] == 1):
            return (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0], _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1])

    def BottomRight(self, element_name):
        if ('_DesignParameter' not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.__dict__):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('There is no DesignParameter.')
        if (aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714 not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid element name.')
        _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
        if (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignParametertype'] == 1):
            return ((_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0] + _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XWidth']), _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1])

    def Center(self, element_name):
        if ('_DesignParameter' not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.__dict__):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('There is no DesignParameter.')
        if (aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714 not in _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter):
            raise b4fe3d529dee467ddcf2b21faec5869a5a0e45a7b30670dbbc23da077ca58e8a('Invalid element name.')
        _445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._DesignParameter[aeccc1cb8a10eef19d04843896453d785ecc15d3cf5a6e93b7268feaf7174714]
        if (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_DesignParametertype'] == 1):
            return ((_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][0] + (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XWidth'] / 2)), (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_XYCoordinates'][0][1] + (_445929267209c034d1e324834c17e0c8305df3dcb21d1710a639ac6ca08c648b['_YWidth'] / 2)))

    def XYCoordinate2MinMaxXY(self, _XYCoordinates):
        _78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a = []
        c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397 = []
        for de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(0, _71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8)):
            _78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a.append(_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8[de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7][0])
            c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397.append(_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8[de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7][1])
        _78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a = a330395cc0a53ad1207736546afff4735940937564bbf75ce1edad40780d9139(_6ee0eb490ff832101cf82a3d387c35f29e4230be786978f7acf9e811febf6723(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a))
        c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397 = a330395cc0a53ad1207736546afff4735940937564bbf75ce1edad40780d9139(_6ee0eb490ff832101cf82a3d387c35f29e4230be786978f7acf9e811febf6723(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397))
        return (_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a, c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)

    def MinMaxXY2XYCoordinate(self, _MinMaxXY):
        (_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a, c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397) = d5b91d04363f7e9d00747fb75ea9cfb3a9733faea62d2dc0c796e128672f3280
        return [[_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a), _1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)], [_9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a), _1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)], [_9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a), _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)], [_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a), _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)], [_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a), _1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)]]

    def XYCoordinate2CenterCoordinateAndWidth(self, _XYCoordinates):
        (_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a, c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397) = _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.XYCoordinate2MinMaxXY(_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8)
        _2cc126c23ebbb47628a845538c56b6597f7c00f2c19c87fdb1e3b0aeba40ce17 = ((_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18((_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a) + _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a))) / 2), (_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18((_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397) + _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397))) / 2))
        e19e940f57f57d0903faa8be95f1fc0be3c42f26f339b9303554dd6037a0a425 = _78da4a596a88bc5114f071ba590793bf3b37329d761230f33129983a747f414e((_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a) - _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a)))
        _243abc5fbb567a88f26b3683f156ee57bf7ddde89988c8073f5a7ebead3a7809 = _78da4a596a88bc5114f071ba590793bf3b37329d761230f33129983a747f414e((_1f6fa6f69d185e6086d04e7330361bf9001a3b8d0ce511171055dc34eb90c1c5(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397) - _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6(c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397)))
        return (_2cc126c23ebbb47628a845538c56b6597f7c00f2c19c87fdb1e3b0aeba40ce17, e19e940f57f57d0903faa8be95f1fc0be3c42f26f339b9303554dd6037a0a425, _243abc5fbb567a88f26b3683f156ee57bf7ddde89988c8073f5a7ebead3a7809)

    def CenterCoordinateAndWidth2XYCoordinate(self, _XYCenter, _WidthX, _WidthY):
        _78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a = [(_11d39f152f4f8d80af1981d434922caec912fb99e7ec4ec412e46a08e34f2fad[0] - (_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18(_3850e19a7728f02dadf177079631f5a87b80dd1c584d40ba25edb03fe98b693b) / 2)), (_11d39f152f4f8d80af1981d434922caec912fb99e7ec4ec412e46a08e34f2fad[0] + (_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18(_3850e19a7728f02dadf177079631f5a87b80dd1c584d40ba25edb03fe98b693b) / 2))]
        c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397 = [(_11d39f152f4f8d80af1981d434922caec912fb99e7ec4ec412e46a08e34f2fad[1] - (_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18(_19334a3bc33e62ec89da235509015c6a8830b8894f57455554828e7537582453) / 2)), (_11d39f152f4f8d80af1981d434922caec912fb99e7ec4ec412e46a08e34f2fad[1] + (_76a7e234dc54e9c605b2cc9fdf71279526150df48c574bdfa69e436e0b3d5c18(_19334a3bc33e62ec89da235509015c6a8830b8894f57455554828e7537582453) / 2))]
        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.MinMaxXY2XYCoordinate([_78ebada914a359d8d542cd21bb94dae3e38c3f224c7c4af647c9ac743481171a, c5af77a2bafe87cc51e8e50f24c4bbf0956261469d1a05989738ae35bb591397])

    def _CreateGDSStream(self, _GDSStructures=[]):
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47 = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_stream.GDS_STREAM()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._BGNLIB = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_BGNLIB()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._BGNLIB.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['BGNLIB']
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._BGNLIB.time_access = _2763d133c5e59ca4ad13b9314864224f3fe33b759a4c3e72fcc03b85ce71384d.now()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._BGNLIB.time_modi = _2763d133c5e59ca4ad13b9314864224f3fe33b759a4c3e72fcc03b85ce71384d.now()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._LIBNAME = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_LIBNAME()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._LIBNAME.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['LIBNAME']
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._LIBNAME.libname = 'testLib'
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._UNITS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_UNITS()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._UNITS.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['UNITS']
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._UNITS.unit_meter = 1e-09
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._UNITS.unit_user = 0.001
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._STRUCTURES = _71673baad254149b036158f70a1e0e41f849c83ff7ed55ee714850a6f29f8e9f
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._HEADER = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_HEADER()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._HEADER.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['HEADER']
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._HEADER.gds_version = 5
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._ENDLIB = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDLIB()
        _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47._ENDLIB.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDLIB']
        return _70804cc99bfef70dbe51567b319daa876ba4eee7623b2b1cce43836d2c054e47

    def _CreateGDSStructure(self, _GDSStructureName=None):
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_structures.GDS_STRUCTURE()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._BGNSTR = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_BGNSTR()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._BGNSTR.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['BGNSTR']
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._BGNSTR.time_creation = _2763d133c5e59ca4ad13b9314864224f3fe33b759a4c3e72fcc03b85ce71384d.now()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._BGNSTR.time_modi = _2763d133c5e59ca4ad13b9314864224f3fe33b759a4c3e72fcc03b85ce71384d.now()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._STRNAME = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_STRNAME()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._STRNAME.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['STRNAME']
        if (cc5d03386ad2ccefe616a5aa51118a154683e19e90ae7b6998abd0cc64d9a2d4 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_GDSStructureName should have correct datatype')
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._STRNAME.strname = cc5d03386ad2ccefe616a5aa51118a154683e19e90ae7b6998abd0cc64d9a2d4
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._ENDSTR = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDLIB()
        _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e._ENDSTR.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDSTR']
        return _5aad79a781b665d407ebe5e0a572ed941168cf0aa185b7d67b7f0da64166195e

    def _CreateGDSBoundaryElement(self, _Layer=None, _Datatype=None, _XYCoordinates=None, _ElementName=None):
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15 = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_ELEMENT()
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_BOUNDARY()
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._BOUNDARY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_BOUNDARY()
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._BOUNDARY.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['BOUNDARY']
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._LAYER = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_LAYER()
        if (efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Layer should have correct data type')
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._LAYER.layer = efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._LAYER.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['LAYER']
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._DATATYPE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_DATATYPE()
        if (_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Datatype should have correct data type')
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._DATATYPE.datatype = _170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._DATATYPE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['DATATYPE']
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._XY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_XY()
        if (_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_XYCoordinates should have correct data type')
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._XY.xy = _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ELEMENTS._XY.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['XY']
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ENDEL = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDEL()
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._ENDEL.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDEL']
        _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15._GDS_ELEMENT_NAME = _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16
        return _0409c89eb0fa412f0cc83066057c6bba8049a3a12c373aeba756de7e1d0daf15

    def _CreateGDSPathElement(self, _Layer=None, _Datatype=None, _Width=None, _XYCoordinates=None, _ElementName=None):
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44 = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_ELEMENT()
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_PATH()
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._PATH = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_PATH()
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._PATH.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['PATH']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._LAYER = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_LAYER()
        if (efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd == None):
            ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('_ElementName: ', _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Layer should have correct data type')
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._LAYER.layer = efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._LAYER.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['LAYER']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._DATATYPE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_DATATYPE()
        if (_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4 == None):
            ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('_ElementName: ', _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Datatype should have correct data type')
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._DATATYPE.datatype = _170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._DATATYPE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['DATATYPE']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._WIDTH = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_WIDTH()
        if (e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None):
            ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('_ElementName: ', _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Width should have correct data type')
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._WIDTH.width = e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._WIDTH.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['WIDTH']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._XY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_XY()
        if (_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 == None):
            ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('_ElementName: ', _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_XYCoordinates should have correct data type')
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._XY.xy = _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._XY.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['XY']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._PATHTYPE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_PATHTYPE()
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._PATHTYPE.pathtype = 0
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ELEMENTS._PATHTYPE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['PATHTYPE']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ENDEL = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDEL()
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._ENDEL.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDEL']
        _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44._GDS_ELEMENT_NAME = _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16
        return _88d1498a025edc40b2b5917f41316fbd3b874ce368193ecbda2d031ed6adba44

    def _CreateGDSSrefElement(self, _SREFName=None, _XYCoordinates=None, _ElementName=None, _Reflect=None, _Angle=None):
        if (_66c12412817ed5f2659cd08ef1b829808c59a4e837e7608549852736e0d1bfae == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_SREFName should have correct data type')
        if (_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_XYCoordinates should have correct data type')
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_ELEMENT()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_SREF()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._SREF = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_SREF()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._SREF.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['SREF']
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._SNAME = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_SNAME()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._SNAME.sname = _66c12412817ed5f2659cd08ef1b829808c59a4e837e7608549852736e0d1bfae
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._SNAME.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['SNAME']
        if (_4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0 or (_5f5278fd16a2bb911853ce64c7d0e5441ea1f5a067dc5c269310cc2e3a42607c != None)):
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_STRANS()
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._STRANS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_STRANS()
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._STRANS.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['STRANS']
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._STRANS.reflection = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[0]
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._STRANS.abs_mag = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[1]
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._STRANS.abs_angle = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[2]
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._ANGLE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ANGLE()
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._ANGLE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ANGLE']
            _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._STRANS._ANGLE.angle = _5f5278fd16a2bb911853ce64c7d0e5441ea1f5a067dc5c269310cc2e3a42607c
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._XY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_XY()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._XY.xy = _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ELEMENTS._XY.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['XY']
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ENDEL = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDEL()
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._ENDEL.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDEL']
        _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa._GDS_ELEMENT_NAME = _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16
        return _9b8d59ad84942e34af7d8eea8a9259ad4d72a835c51808051c41d711e0f21faa

    def _CreateGDSTextElement(self, _Layer=None, _Datatype=None, _Presentation=None, _Reflect=None, _XYCoordinates=None, _Mag=None, _Angle=None, _TEXT=None, _ElementName=None):
        if (d7c0135ec675c3db49c3290d5b6ae003f3c475fad3328ed5a8778996743fb703 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_TEXT should have string data to be written as text')
        if (_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_XYCoordinates should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_ELEMENT()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_TEXT()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXT = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_TEXT()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXT.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['TEXT']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._LAYER = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_LAYER()
        if (efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Layer should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._LAYER.layer = efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._LAYER.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['LAYER']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_TEXTBODY()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._TEXTTYPE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_TEXTTYPE()
        if (_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Datatype(_Texttype) should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._TEXTTYPE.texttype = _170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._TEXTTYPE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['TEXTTYPE']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._PRESENTATION = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_PRESENTATION()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._PRESENTATION.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['PRESENTATION']
        if (f06e2d692842da6f5a5d417027247a77a4fed0cc03585ac775b4e9d7d38ddab3 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_Presentation should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._PRESENTATION.font = f06e2d692842da6f5a5d417027247a77a4fed0cc03585ac775b4e9d7d38ddab3[0]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._PRESENTATION.vertical_presentation = f06e2d692842da6f5a5d417027247a77a4fed0cc03585ac775b4e9d7d38ddab3[1]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._PRESENTATION.horizontal_presentation = f06e2d692842da6f5a5d417027247a77a4fed0cc03585ac775b4e9d7d38ddab3[2]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_elements.GDS_STRANS()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._STRANS = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_STRANS()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._STRANS.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['STRANS']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._STRANS.reflection = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[0]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_mag = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[1]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._STRANS.abs_angle = _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0[2]
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._MAG = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_MAG()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._MAG.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['MAG']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._MAG.mag = _99d6c01194c781d2a5704c368e8d803b953176ad7db771d42fc02e25aa716a95
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._ANGLE = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ANGLE()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._ANGLE.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ANGLE']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRANS._ANGLE.angle = _5f5278fd16a2bb911853ce64c7d0e5441ea1f5a067dc5c269310cc2e3a42607c
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._XY = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_XY()
        if (_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_XYCoordinates should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._XY.xy = _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._XY.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['XY']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRING = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_STRING()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRING.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['STRING']
        if (d7c0135ec675c3db49c3290d5b6ae003f3c475fad3328ed5a8778996743fb703 == None):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectInputError('_TEXT should have correct data type')
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ELEMENTS._TEXTBODY._STRING.string_data = d7c0135ec675c3db49c3290d5b6ae003f3c475fad3328ed5a8778996743fb703
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ENDEL = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_record.GDS_ENDEL()
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._ENDEL.tag = aa81995bf65fd75fdc23e234d0dcf9a24c3a1dd25e5ae8f377398d6ba80bdb07.gds_tags.DICT['ENDEL']
        _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a._GDS_ELEMENT_NAME = _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16
        return _003277bed84509f40371dcd405aa3a2788ae0b936ae1e5333355964c0046655a

    def _ReadLayerMapFile(self, _LayerMapFile):
        _8627a3340dad83c960bffca08be1af1c864e04d1d270a46aa8dd83722230b048 = {}
        c69f812b449f47511c4257dfaf90329a27fa012a960874f5bced9ec86c46b27b = _71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_7cbe6768c1d3b103d8747b896029d65db3e11f2f8cc056b317890564a155a747.readlines())
        _7cbe6768c1d3b103d8747b896029d65db3e11f2f8cc056b317890564a155a747.seek(0)
        for de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(0, c69f812b449f47511c4257dfaf90329a27fa012a960874f5bced9ec86c46b27b):
            cf10d3eb4b80f1fdd74306ab6e6152f1822b19451b959eba448ba2d0b2beb22b = _7cbe6768c1d3b103d8747b896029d65db3e11f2f8cc056b317890564a155a747.readline()
            _6e3cc34e3b25cdb0cf2211b484b3508ea618b075d8f9e5c99bc214ed31f54c46 = cf10d3eb4b80f1fdd74306ab6e6152f1822b19451b959eba448ba2d0b2beb22b.split()
            _8627a3340dad83c960bffca08be1af1c864e04d1d270a46aa8dd83722230b048[(_6e3cc34e3b25cdb0cf2211b484b3508ea618b075d8f9e5c99bc214ed31f54c46[0], _6e3cc34e3b25cdb0cf2211b484b3508ea618b075d8f9e5c99bc214ed31f54c46[1])] = (_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(_6e3cc34e3b25cdb0cf2211b484b3508ea618b075d8f9e5c99bc214ed31f54c46[2]), _6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(_6e3cc34e3b25cdb0cf2211b484b3508ea618b075d8f9e5c99bc214ed31f54c46[3]))
        return _8627a3340dad83c960bffca08be1af1c864e04d1d270a46aa8dd83722230b048

    def _UpdateDesignParameter2GDSStructure(self, _DesignParameterInDictionary=None):
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('#########################################################################################################')
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('                                    {}  Update2GDS Start                                    '.format(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_Name']['_Name']))
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('#########################################################################################################')
        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'] = [_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSStructure(_GDSStructureName=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_Name']['_Name'])]
        for _9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920:
            ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('*********** ', _9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435, ' is updating to GDS **********')
            if ((_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 1) and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Ignore'] == None)):
                if ((b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology != '180nm') and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Layer'] == b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._LayerMapping['WELLBODY'][0])):
                    pass
                elif ((b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology != '065nm') and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Layer'] == b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._LayerMapping['PDK'][0])):
                    pass
                else:
                    for b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates']:
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSBoundaryElement(_Layer=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Layer'], _Datatype=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Datatype'], _XYCoordinates=_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d, _WidthX=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XWidth'], _WidthY=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_YWidth']), _ElementName=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName']))
            elif ((_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 2) and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Ignore'] == None)):
                for _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates']:
                    _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb = _6f5a6034e770acbfb3f797e6a7eb7948d470d45f9928f92b7d72dc7c45e6d0cd.deepcopy(_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8)
                    b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd = 0
                    while True:
                        if (b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd < (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb) - 1)):
                            if ((_8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd][0] == _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)][0]) and (_8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd][1] == _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)][1])):
                                del _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)]
                            else:
                                b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd = (b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)
                        else:
                            break
                    if (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(_8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb) >= 2):
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSPathElement(_Layer=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Layer'], _Datatype=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Datatype'], _Width=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Width'], _XYCoordinates=_8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb, _ElementName=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName']))
                    del _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb
            elif ((_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 3) and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignObj'] != None) and (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Ignore'] == None)):
                _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignObj']._DesignParameter)
                _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'] = (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'] + _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignObj']._DesignParameter['_GDSFile']['_GDSFile'])
                for b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates']:
                    _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSSrefElement(_SREFName=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignObj']._DesignParameter['_Name']['_Name'], _XYCoordinates=[b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d], _Reflect=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Reflect'], _Angle=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Angle'], _ElementName=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName']))
            elif (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 8):
                for b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates']:
                    _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSTextElement(_Layer=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Layer'], _Datatype=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Datatype'], _Presentation=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Presentation'], _Reflect=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Reflect'], _XYCoordinates=[b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d], _Mag=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Mag'], _Angle=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Angle'], _TEXT=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_TEXT']))
            elif (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 6):
                for _4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9 in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_Rails']:
                    for b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d in _4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9['_XYCoordinates']:
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSBoundaryElement(_Layer=_4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9['_Layer'], _Datatype=_4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9['_Datatype'], _XYCoordinates=_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d, _WidthX=_4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9['_XWidth'], _WidthY=_4a3835663b42b4104930395b1d63cdc1a44eaf76906891bbc58db8add87a11d9['_YWidth'])))
                for ecae307f428dc99da7356768aadea414ec8bb52bdda804ceaa4abd8708d2e265 in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ViaArrays']:
                    ecae307f428dc99da7356768aadea414ec8bb52bdda804ceaa4abd8708d2e265['_DesignObj']._UpdateDesignParameter2GDSStructure()
                    _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'] = (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'] + ecae307f428dc99da7356768aadea414ec8bb52bdda804ceaa4abd8708d2e265['_DesignObj']._DesignParameter['_GDSFile']['_GDSFile'])
                    for b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d in ecae307f428dc99da7356768aadea414ec8bb52bdda804ceaa4abd8708d2e265['_XYCoordinates']:
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSSrefElement(_SREFName=ecae307f428dc99da7356768aadea414ec8bb52bdda804ceaa4abd8708d2e265['_DesignObj']._DesignParameter['_Name']['_Name'], _XYCoordinates=[b79f9984c24df305dc062b5fa6637c5ddca5d6c65759b743d30c09570fc72d3d]))
            elif (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_DesignParametertype'] == 901):
                if (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_DesignParametertype'] == 1):
                    for _45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_NumofArray']):
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSBoundaryElement(_Layer=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Layer'], _Datatype=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Datatype'], _XYCoordinates=_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[_09f5ffef28309853265c4a98d0e56e1be522b6b402d8193594fd05103064fc6a(_769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca) for _769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca in _4a70fe9aa6436e02c2dea340fbd1e352e4ef2d8ce6ca52ad25d4b95471fc8bf2(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates'][0], [(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 * _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XOffset']), (_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 * _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_YOffset'])])], _WidthX=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_XWidth'], _WidthY=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_YWidth']), _ElementName=(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName'] + _8c25cb3686462e9a86d2883c5688a22fe738b0bbc85f458d2d2b5f3f667c6d5a(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0))))
                elif (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_DesignParametertype'] == 2):
                    for _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_XYCoordinates']:
                        _7542e93710436b6687fbe3d2cb3d51270fa90ac312803bd2f21d157ad077c7d0 = []
                        for f9693b55f9307ef2bd3e6f1027900efe4dd3236c0e57bbfa79e98ebfde796bb4 in _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb:
                            _7542e93710436b6687fbe3d2cb3d51270fa90ac312803bd2f21d157ad077c7d0.append([_09f5ffef28309853265c4a98d0e56e1be522b6b402d8193594fd05103064fc6a(_769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca) for _769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca in _4a70fe9aa6436e02c2dea340fbd1e352e4ef2d8ce6ca52ad25d4b95471fc8bf2(f9693b55f9307ef2bd3e6f1027900efe4dd3236c0e57bbfa79e98ebfde796bb4, [(- _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[0][0]), (- _8f82217a1b9982ae036329ecbec224c0e0f03b13c404282e648355441e0e97fb[0][1])])])
                        for _45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_NumofArray']):
                            _9352550e2e5f9c467d50de26dc018e464c9a043084d9ac8476fa19bbde820054 = [_09f5ffef28309853265c4a98d0e56e1be522b6b402d8193594fd05103064fc6a(_769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca) for _769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca in _4a70fe9aa6436e02c2dea340fbd1e352e4ef2d8ce6ca52ad25d4b95471fc8bf2([(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XOffset'] * _45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0), (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_YOffset'] * _45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0)], _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates'][0])]
                            for _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8 in _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_XYCoordinates']:
                                b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310 = []
                                for de4ec5c3d3b2b85e33cef0ff3cd12ea0c0e3c5d8cfd29ee3635f2948b07f033b in _7542e93710436b6687fbe3d2cb3d51270fa90ac312803bd2f21d157ad077c7d0:
                                    b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310.append([_09f5ffef28309853265c4a98d0e56e1be522b6b402d8193594fd05103064fc6a(_769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca) for _769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca in _4a70fe9aa6436e02c2dea340fbd1e352e4ef2d8ce6ca52ad25d4b95471fc8bf2(de4ec5c3d3b2b85e33cef0ff3cd12ea0c0e3c5d8cfd29ee3635f2948b07f033b, _9352550e2e5f9c467d50de26dc018e464c9a043084d9ac8476fa19bbde820054)])
                                b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd = 0
                                while True:
                                    if (b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd < (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310) - 1)):
                                        if ((b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310[b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd][0] == b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)][0]) and (b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310[b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd][1] == b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)][1])):
                                            del b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310[(b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)]
                                        else:
                                            b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd = (b56a143db52348191f94548bdcb7c1412fd138d7d83a110f8f9e649856e027cd + 1)
                                    else:
                                        break
                                if (_71fa9faaa6f884aa11f4cea21477b2204a48a4fa7f05cecad00a1250eeeffb4c(b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310) >= 2):
                                    _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSPathElement(_Layer=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Layer'], _Datatype=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Datatype'], _Width=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Width'], _XYCoordinates=b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310, _ElementName=(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName'] + _8c25cb3686462e9a86d2883c5688a22fe738b0bbc85f458d2d2b5f3f667c6d5a(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0))))
                                del b05de1a476e7e2f3e2b3239d56ca80bff8cadc18df29da32da9e66dcf6453310
                elif (_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_DesignParametertype'] == 3):
                    for _45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 in _2269c0be009b610cfdbb8cfe9253ad37cf95062fb3f5a7560268ff259ea9f087(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_NumofArray']):
                        _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile'][0]._ELEMENTS.append(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CreateGDSSrefElement(_SREFName=(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_DesignObj']._DesignParameter['_Name']['_Name'] + _8c25cb3686462e9a86d2883c5688a22fe738b0bbc85f458d2d2b5f3f667c6d5a(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0)), _XYCoordinates=[_09f5ffef28309853265c4a98d0e56e1be522b6b402d8193594fd05103064fc6a(_769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca) for _769a4e6d0003189c7e96c5d9b7e810a0d11c3a12832527ec94b0f86d277f51ca in _4a70fe9aa6436e02c2dea340fbd1e352e4ef2d8ce6ca52ad25d4b95471fc8bf2(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XYCoordinates'][0], [(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 * _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_XOffset']), (_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0 * _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_YOffset'])])], _Reflect=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Reflect'], _Angle=_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_BaseElement']['_Angle'], _ElementName=(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920[_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435]['_ElementName'] + _8c25cb3686462e9a86d2883c5688a22fe738b0bbc85f458d2d2b5f3f667c6d5a(_45a0d6debd7eee3258fad345360014e5e12bff4e6ecdaa931006a022153470f0))))
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('#########################################################################################################')
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('                                    {}  Update2GDS End                                    '.format(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_Name']['_Name']))
        ce953a0eb08246617b7f849486c4b26a7af37e9d2e8f0e13b3ae1bf0da8a70a2('#########################################################################################################')
        return _98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920['_GDSFile']['_GDSFile']

    def _PathElementDeclaration(self, _Layer=None, _Datatype=None, _XYCoordinates=[], _Width=None, _ElementName=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=2, _Layer=efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd, _Datatype=_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4, _XYCoordinates=_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8, _Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _Ignore=None, _ElementName=_93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)

    def _BoundaryElementDeclaration(self, _Layer=None, _Datatype=None, _XYCoordinates=[], _XWidth=None, _YWidth=None, _ElementName=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=1, _Layer=efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd, _Datatype=_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4, _XYCoordinates=_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8, _XWidth=_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647, _YWidth=b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb, _Ignore=None, _ElementName=_93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)

    def _SrefElementDeclaration(self, _DesignObj=None, _XYCoordinates=[], _Reflect=None, _Angle=None, _ElementName=None):
        return (_6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=3, _DesignObj=_0e50a8d405c4a9f0a50295b7dafbf67ca3b9c3edfe787d90dbe71dd37433df6e, _XYCoordinates=_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8, _Reflect=None, _Angle=None, _Ignore=None, _ElementName=_93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16),)

    def _ElementArrayDeclaration(self, _BaseElement=None, _XYCoordinates=[], _NumofArray=1, _XOffset=0, _YOffset=0, _Reflect=None, _Angle=None, _ElementName=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=901, _BaseElement=_332589c62bc364943c052862b8ab4f92107b2824332476b2d09e071342ea3ecb, _XYCoordinates=_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8, _NumofArray=_4bc479f46b177c034dd6c7b0bbdd9543bef56fa760a2d50c156be7a848a26451, _XOffset=_9c43a6b1060b5da70aedccab91500452feffc4690100b0073bcc48a56592f734, _YOffset=_3ee6d50e995fb8c3a07cf56a5c0b2cea584ba1da80e8baf85fbe10ad42b8ae81, _Reflect=None, _Angle=None, _Ignore=None, _ElementName=_93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)

    def _NameDeclaration(self, _Name=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=5, _Name=_7563a16a547855ae85f461c6ade6e8a9d7d7a2aca7f877614e0d0459fb25d1e6)

    def _GDSObjDeclaration(self, _GDSFile=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=4, _GDSFile=_13864ddbaab63577bb07db6dcc11d8a2f724a0784933aedad515ce4a6fd2e256)

    def _TextElementDeclaration(self, _Layer=None, _Datatype=None, _Presentation=None, _Reflect=None, _XYCoordinates=[], _Mag=None, _Angle=None, _TEXT=None, _ElementName=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=8, _Layer=efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd, _Datatype=_170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4, _Presentation=f06e2d692842da6f5a5d417027247a77a4fed0cc03585ac775b4e9d7d38ddab3, _Reflect=_4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0, _XYCoordinates=_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8, _Mag=_99d6c01194c781d2a5704c368e8d803b953176ad7db771d42fc02e25aa716a95, _Angle=_5f5278fd16a2bb911853ce64c7d0e5441ea1f5a067dc5c269310cc2e3a42607c, _TEXT=d7c0135ec675c3db49c3290d5b6ae003f3c475fad3328ed5a8778996743fb703, _ElementName=_93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16)

    def _XYCoordinateInfoDeclaration(self, _XYCoordinateInfo=[]):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=7, _XYCoordinates=f01bb7cf44ec91244dd4d6a633fdc60fea0f779f1913fb231bea45605d945e9d)

    def _BitInfoDeclaraion(self, _BitNumber=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=7, _BitNumber=a6ddbf47e31ad20f53a521dfd4e5d14a6247a78d7724720a0f8131f3046a40fe)

    def _SizeInfoDeclaraion(self, _DesignSizesInList=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=7, _DesignSizesInList=_1e75322a36bd590def2331e92af901597cec95f820e7d6040d57e84a2524d11d)

    def _SupplyRailDeclaration(self, _HorizontalSupplyRailArea=[], _VerticalSupplyRailArea=[], _ViaArrays=[], _Rails=[], _SupplyNodeName=None):
        return _6ab47d70854a8c690a0c2035be903f3d812cbab06f9e442e9b10ad70b1acd446(_DesignParametertype=6, _HorizontalSupplyRailArea=a8203452a9462653ba5804c3a24d542911e02fe71b0c583f5359265bd2458d20, _VerticalSupplyRailArea=_1bf6c4836516328620aabbb0f5cd2f937f3bbf679afe5c1ad57042afccf57c52, _ViaArrays=_91a40571f2b85ac0baa2f9e13a297f0b79c7c8250f56069843825a63a349c340, _Rails=f7120562a7bd23835b2cd1f4564f66e1bea6b252b34a12d11632b27c5b815576, _SupplyNodeName=fb0014962fd3da5e81468cab51556c7bc6491ed2e3dad657665650b8f24011fc)
