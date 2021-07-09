
import re
import math
from gds_editor_ver3 import user_define_exceptions
from designs import DesignParameters

class DRCMultiplicantForMinEdgeWidth():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth = 1
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth = 1
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth = 0
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth = 0
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth = 0

    def DRCMinEdgeWidth(self, _MinWidth=None):
        return (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MultiplicantForMinEdgeWidth * _27046bacaa3ff7a0d4ab80f2b0bcab5b07574ebc3188e6646b2005aca9a47c08)

class DRCMinSnapSpacing():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MinSnapSpacing = 5
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MinSnapSpacing = 5
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MinSnapSpacing = 5
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MinSnapSpacing = 5
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MinSnapSpacing = 5

class DRCOD():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinWidth = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace3 = 100
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinWidth = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace3 = 130
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinWidth = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace2 = 160
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinWidth = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace = 210
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinWidth = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace = 280

    def DRCODMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
            elif ((120 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (140 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace3
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
            elif ((150 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (200 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace3
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
            elif ((300 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (230 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._OdMinSpace

class DRCPP():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinWidth = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinExtensiononPactive = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPo = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPtypePoRes = 140
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinWidth = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinExtensiononPactive = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPo = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPtypePoRes = 200
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinWidth = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinSpace = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinExtensiononPactive = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPo = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPtypePoRes = 200
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinWidth = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinSpace = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinExtensiononPactive = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPo = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPtypePoRes = 200
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinWidth = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinSpace = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinExtensiononPactive = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPo = 320
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PpMinEnclosureOfPtypePoRes = 180

class DRCNP():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinWidth = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinExtensiononNactive = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinEnclosureOfPo = 110
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinWidth = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinExtensiononNactive = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinEnclosureOfPo = 150
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinWidth = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinSpace = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinExtensiononNactive = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinEnclosureOfPo = 200
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinWidth = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinSpace = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinExtensiononNactive = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinEnclosureOfPo = 200
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinWidth = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinSpace = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinExtensiononNactive = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NpMinEnclosureOfPo = 320

class DRCPOLYGATE():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinWidth = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2Co = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2OD = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2PolygateInSameRPO = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinExtensionOnOD = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth1 = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth2 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth3 = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpaceAtCorner = 110
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinWidth = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2 = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2Co = 55
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2OD = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2PolygateInSameRPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinExtensionOnOD = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpaceAtCorner = 140
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinWidth = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2 = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2Co = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2OD = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2PolygateInSameRPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinExtensionOnOD = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpaceAtCorner = 140
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinWidth = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2Co = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2OD = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2PolygateInSameRPO = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinExtensionOnOD = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpaceAtCorner = 180
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinWidth = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace = 375
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2Co = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2OD = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2PolygateInSameRPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinExtensionOnOD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpaceAtCorner = 375

    def DRCPolygateMinSpace(self, _TmpLengthBtwPolyEdge=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if (_9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428 <= _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth1):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth1
            elif (_9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428 <= _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth2):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth2
            elif (_9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428 <= _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth3):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateOnODMinWidth3
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            return _9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return _9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return _9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _9a861adacb541e4a7ec96943af6efeec554d3afce7759a1cd4779b9e3a8ad428

    def DRCPolyMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
            elif ((120 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (140 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
            elif ((130 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (180 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
            elif ((230 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (300 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._PolygateMinSpace

class DRCCO():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2 = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceDifferentNet = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceFor3neighboring = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByOD = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPO = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide = 20
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2 = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceDifferentNet = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceFor3neighboring = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByOD = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPO = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide = 40
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceDifferentNet = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceFor3neighboring = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByOD = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPO = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide = 50
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2 = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceDifferentNet = 210
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceFor3neighboring = 210
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByOD = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPO = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide = 120
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2 = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceDifferentNet = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpaceFor3neighboring = 300
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByOD = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPO = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide = 100

    def DRCCOMinSpace(self, NumOfCOX=None, NumOfCOY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) and (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
            elif (((2 < a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 <= bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)) or ((2 <= a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 < bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) and (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
            elif (((2 < a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 <= bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)) or ((2 <= a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 < bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) and (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
            elif (((2 < a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 <= bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)) or ((2 <= a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (2 < bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            if ((bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) and (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
            elif ((4 <= a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (4 <= bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            if ((bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) and (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace
            elif ((4 <= a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d) and (4 <= bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinSpace

    def DRCCOFillAtOD2Met1(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if ((4 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (4 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if ((4 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (4 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByODAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)

    def DRCCOFillAtPoly2Met1(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if ((4 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (4 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=None, NumOfCOY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if ((4 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (4 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinEnclosureByPOAtLeastTwoSide)) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCCOMinSpace(NumOfCOX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfCOY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._CoMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)

class DRCMETAL1():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinWidth = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2 = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace21 = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace22 = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace23 = 210
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO2 = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia1 = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia12 = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinArea = 21500
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinWidth = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2 = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace21 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO2 = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia1 = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia12 = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinArea = 42000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinWidth = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2 = 170
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia1 = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia12 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinArea = 58000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinWidth = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2 = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3 = 600
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia1 = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia12 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinArea = 122000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinWidth = 230
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace = 230
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2 = 600
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureCO2 = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia1 = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinEnclosureVia12 = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinArea = 202000

    def DRCMETAL1MinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
            elif ((170 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (270 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((240 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (270 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((310 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (400 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        if ((620 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (620 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                            if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3
                            else:
                                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace23
                        else:
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace22
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace21
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
            elif ((200 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (380 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((420 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (420 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace4
                        else:
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace21
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
            elif ((300 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (520 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace4
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
            elif ((300 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1000 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 10000) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 > 10000)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 10000) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 > 10000)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpace

    def DRCMETAL1MinSpaceAtCorner(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._Metal1MinSpaceAtCorner
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETAL1MinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETAL1MinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETAL1MinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)

class DRCNW():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinWidth = 340
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpace = 340
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinEnclosurePactive = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpacetoNactive = 80
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinWidth = 470
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpace = 470
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinEnclosurePactive = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpacetoNactive = 160
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinWidth = 620
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpace = 620
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinEnclosurePactive = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpacetoNactive = 220
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinWidth = 620
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpace = 620
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinEnclosurePactive = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpacetoNactive = 310
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinWidth = 860
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpace = 1400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinEnclosurePactive = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._NwMinSpacetoNactive = 430

class DRCVIAx():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2 = 90
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceDifferentNet = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceFor3neighboring = 98
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetx = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetxTwoOppositeSide = 30
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2 = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceDifferentNet = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceFor3neighboring = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetx = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetxTwoOppositeSide = 40
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth = 130
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2 = 170
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceDifferentNet = 170
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceFor3neighboring = 190
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetx = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetxTwoOppositeSide = 50
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth = 190
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2 = 290
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceDifferentNet = 290
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceFor3neighboring = 310
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetx = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetxTwoOppositeSide = 50
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth = 260
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace = 260
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceDifferentNet = 260
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpaceFor3neighboring = 260
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetx = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinEnclosureByMetxTwoOppositeSide = 60

    def DRCVIAxMinSpace(self, NumOfVIAxX=None, NumOfVIAxY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((_6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952 == None) and (_01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
            elif (((2 < _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 <= _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952)) or ((2 <= _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 < _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((_6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952 == None) and (_01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
            elif (((2 < _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 <= _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952)) or ((2 <= _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 < _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((_6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952 == None) and (_01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
            elif (((2 < _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 <= _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952)) or ((2 <= _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (2 < _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            if ((_6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952 == None) and (_01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
            elif ((3 <= _01fe9fc77292b42eef0f8c3e86bb79c7d1b8270d5dd9e769ec35677c4a022295) and (3 <= _6b126bd98b0847cab6c761fc70ca8116dc76d4eb4c3d6a3492e2cd13ac1f5952)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinSpace

    def DRCVIAxFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6 = bc21643bd5ba8ee75814ccf6a49295bcf1703e78fadbbd465c17bf37f9099950()
        _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956 = _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8()
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if ((3 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (3 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAxY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6._Metal1MinEnclosureVia12, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAxMinSpace(NumOfVIAxX=None, NumOfVIAxY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAxMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        del _733b565db085ca23370331ed5187ac7ad4ffaed97f1811eb3cac2759b18c25b6
        del _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956

class DRCVIAy():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceDifferentNet = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceFor3neighboring = 175
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMety = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 45
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2 = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceDifferentNet = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceFor3neighboring = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMety = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 50
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth = 260
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace = 300
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2 = 370
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceDifferentNet = 370
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceFor3neighboring = 390
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMety = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxOrMetyTwoOppositeSide = 50
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceDifferentNet = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceFor3neighboring = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxTwoOppositeSide = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceDifferentNet = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpaceFor3neighboring = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIAyMinSpace(self, NumOfVIAyX=None, NumOfVIAyY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((_6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0 == None) and (_7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
            elif (((2 < _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 <= _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0)) or ((2 <= _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 < _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((_6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0 == None) and (_7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
            elif (((2 < _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 <= _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0)) or ((2 <= _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 < _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((_6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0 == None) and (_7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
            elif (((2 < _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 <= _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0)) or ((2 <= _7f133fdcfd1e15bbdfb1db0de782ade3281a88ba72fe614cf41bbdb22aa34a15) and (2 < _6cff9740b6bb09f0644e0f91db542df4404474040c1ee94b51b14c929cbf8cd0))):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

    def DRCVIAyFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c = cbbebd9f678a28018225449b7dbccdb36bf97d755d67aae4387353bdef9f5ad5()
        _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956 = _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8()
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=None, NumOfVIAyY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAyMinSpace(NumOfVIAyX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAyY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAyMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None
        del d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c
        del _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956

class DRCVIAz():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth = 360
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace = 340
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2 = 540
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpaceFor3neighboring = 560
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMety = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth = 360
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace = 340
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2 = 540
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpaceFor3neighboring = 560
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMety = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpaceFor3neighboring = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMety = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxOrMetyTwoOppositeSide = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpaceFor3neighboring = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxTwoOppositeSide = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpaceFor3neighboring = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIAzMinSpace(self, NumOfVIAzX=None, NumOfVIAzY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((_12e63c131468dbc80dce5a148a2361d03b9537c22f527c14fa3cb9da83161e4f == None) and (_434ffca563df64ac2b69b18aa65c21539bfe553a1cea460587fb916e86731454 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace
            elif ((2 <= _434ffca563df64ac2b69b18aa65c21539bfe553a1cea460587fb916e86731454) and (2 <= _12e63c131468dbc80dce5a148a2361d03b9537c22f527c14fa3cb9da83161e4f)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((_12e63c131468dbc80dce5a148a2361d03b9537c22f527c14fa3cb9da83161e4f == None) and (_434ffca563df64ac2b69b18aa65c21539bfe553a1cea460587fb916e86731454 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace
            elif ((2 <= _434ffca563df64ac2b69b18aa65c21539bfe553a1cea460587fb916e86731454) and (2 <= _12e63c131468dbc80dce5a148a2361d03b9537c22f527c14fa3cb9da83161e4f)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

    def DRCVIAzFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19 = _467ef556e98765ad382a6d87c083bd6b7e7ec656f92f836198574803cc06fcd7()
        d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c = cbbebd9f678a28018225449b7dbccdb36bf97d755d67aae4387353bdef9f5ad5()
        _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956 = _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8()
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=None, NumOfVIAzY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIAzMinSpace(NumOfVIAzX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIAzY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIAzMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None
        del _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19
        del d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c
        del _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956

class DRCVIAr():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth = 460
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace20 = 660
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace21 = 540
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpaceFor3neighboring = 660
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMety = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth = 460
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace = 440
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace20 = 660
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace21 = 540
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpaceFor3neighboring = 660
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMety = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = 80
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMety = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxOrMetyTwoOppositeSide = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxTwoOppositeSide = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetx = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinEnclosureByMetxTwoOppositeSide = None

    def DRCVIArMinSpace(self, NumOfVIArX=None, NumOfVIArY=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((_72361a6aa1ee8b8fe9e338e458df6c44e8581a2f38e1774e12342ffadcb3660c == None) and (_798b95a934292f4f48602a72b352adc601d6d0afb904d3d1a8cecce328d229d5 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace
            elif ((2 <= _798b95a934292f4f48602a72b352adc601d6d0afb904d3d1a8cecce328d229d5) and (2 <= _72361a6aa1ee8b8fe9e338e458df6c44e8581a2f38e1774e12342ffadcb3660c)):
                return _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace20, _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace21])
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((_72361a6aa1ee8b8fe9e338e458df6c44e8581a2f38e1774e12342ffadcb3660c == None) and (_798b95a934292f4f48602a72b352adc601d6d0afb904d3d1a8cecce328d229d5 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace
            elif ((2 <= _798b95a934292f4f48602a72b352adc601d6d0afb904d3d1a8cecce328d229d5) and (2 <= _72361a6aa1ee8b8fe9e338e458df6c44e8581a2f38e1774e12342ffadcb3660c)):
                return _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace20, _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace21])
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

    def DRCVIArFill(self, XWidth=None, YWidth=None, NumOfCOX=None, NumOfCOY=None):
        _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe = _171f5f7c537f5ce71a79da325fb71a0fbe138e9b60fcff82d38ac13c57447bef()
        _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19 = _467ef556e98765ad382a6d87c083bd6b7e7ec656f92f836198574803cc06fcd7()
        d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c = cbbebd9f678a28018225449b7dbccdb36bf97d755d67aae4387353bdef9f5ad5()
        _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956 = _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8()
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
            _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=None, NumOfVIArY=None) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            if (((2 < _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 <= _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)) or ((2 <= _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310) and (2 < _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab))):
                _2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310 = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b == None) else bd5fa335513872b26ba6867b6b71e098be5a991322c1a3161f293366dffb483b)
                _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab = ((_6da88c34ba124c41f977db66a4fc5c1a951708d285c81bb0d47c3206f4c27ca8(((_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143 - (2 * _9baf3a40312f39849f46dad1040f2f039f1cffa1238c41e9db675315cfad39b6([d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c._MetalyMinEnclosureCO2, _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19._MetalzMinEnclosureCO2, _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe._MetalrMinEnclosureCO2, _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956._MetalxMinEnclosureCO2]))) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143))) / (_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCVIArMinSpace(NumOfVIArX=_56408a3dae39f69047cbec447380549f816229a9b7faa772b2af4e47fe2c9177, NumOfVIArY=_6779737e82daa09ea754c503ba05ec800362c6eb2f1337d99dcca9ba381ff143) + _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._VIArMinWidth)) if (a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d == None) else a4460c3a53ebcef2f11f984188d38c65f6440f21afde957c898df8d60b74912d)
            return (_2a83290a282ef13b50d3718e5b164948dbf1cc85f3f653a6480e1eedcbb36310, _55a0e331ff508ab46fd73040acf1508733ac766f3130d81a6d9d4a102073f9ab)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None
        del _37c0b32e47043aaa6d84e358ee0ddd798ce6a7820ade3e0fd5cbf58178ab46fe
        del _42d1b648a7f939698b05ad53c053624f92612bec384b9ab9a303ce1187c77d19
        del d5f2292a275eb902ab53aac17511341621ec210d582d5bd98ae2dfdcac473a8c
        del _1ccafa3cd8c1ccf0717a443343b7c6750ee17ae918a9b70c67eac988458bb956

class DRCMETALx():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinWidth = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace = 70
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2 = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace21 = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace22 = 150
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace23 = 210
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO2 = 30
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinArea = 27000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinWidth = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace = 100
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2 = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace21 = 160
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner = 110
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO2 = 40
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinArea = 52000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinWidth = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2 = 190
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinArea = 70000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinWidth = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace = 210
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2 = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3 = 600
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO = 5
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinArea = 144000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinWidth = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2 = 600
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceWhenRunWidth200Length380 = 120
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceWhenRunWidth1500Length1500 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceWhenRunWidth4500Length4500 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinEnclosureCO2 = 60
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinArea = 202000

    def DRCMETALxMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
            elif ((170 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (270 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((240 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (270 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((310 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (400 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        if ((620 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (620 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                            if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3
                            else:
                                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace23
                        else:
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace22
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace21
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
            elif ((200 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (380 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((420 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (420 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace4
                        else:
                            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace21
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
            elif ((210 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (520 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace4
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
            elif ((390 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1000 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((10000 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (10000 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 10000) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 > 10000)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpace

    def DRCMETALxMinSpaceAtCorner(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalxMinSpaceAtCorner
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETALxMinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETALxMinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4.DRCMETALxMinSpace(_Width=e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f, _ParallelLength=caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)

class DRCMETALy():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinWidth = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace = 140
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2 = 190
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO2 = 45
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinArea = 70000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinWidth = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace = 200
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2 = 240
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace4 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO = 0
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinArea = 144000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinWidth = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace = 280
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO = 10
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO2 = 50
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinArea = 140000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinArea = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinArea = None

    def DRCMetalyMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
            elif ((210 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (520 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace4
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
            elif ((390 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1000 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace4
                    else:
                        return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
            elif ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalyMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

class DRCMETALz():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinWidth = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO2 = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinArea = 565000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinWidth = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2 = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO2 = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinArea = 565000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinArea = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinArea = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinArea = None

    def DRCMetalzMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace
            elif ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace
            elif ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalzMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

class DRCMETALr():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinWidth = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2 = 650
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO2 = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinArea = 1000000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinWidth = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMaxWidth = 12000
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace = 500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2 = 650
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3 = 1500
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO = 20
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO2 = 80
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinArea = 1000000
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinArea = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinArea = None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMaxWidth = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinEnclosureCO2 = None
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinArea = None

    def DRCMetalrMinSpace(self, _Width=None, _ParallelLength=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace
            elif ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if ((e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f == None) and (caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822 == None)):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace
            elif ((1500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (1500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                if ((4500 < e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f) and (4500 < caf59c2b571e01453efe1e0196f1fd478347cba02f64703bd53b100ecdaf0822)):
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace3
                else:
                    return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace2
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._MetalrMinSpace
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return None
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return None

class DRCRPO():

    def __init__(self):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinWidth = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace = 400
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2OD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2CO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2UnrelatedPO = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um = 300
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOSmallerThan430nm = 300
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinWidth = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2OD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2CO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2UnrelatedPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um = 300
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinWidth = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2OD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2CO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2UnrelatedPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um = 300
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinWidth = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2OD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2CO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2UnrelatedPO = 180
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um = 300
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinWidth = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace = 430
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2OD = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2CO = 220
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinSpace2UnrelatedPO = 250
            _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO = 220

    def DRCRPOMinExtensionOnPO(self, _Width=None):
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '045nm'):
            if (e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 100000):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um
            elif (e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 430):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOSmallerThan430nm
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '065nm'):
            if (e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 100000):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '090nm'):
            if (e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f > 100000):
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPOLargerThan10um
            else:
                return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '130nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO
        if (b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._Technology == '180nm'):
            return _06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4._RPOMinExtensionOnPO

class DRC(_7ab5a00f9bab96617739ffcbd8bd1c6e40ff50d07154ce04feb4fde93f2aa7d8, _1e34a83ecceffcab0b7efb8cfa373ede09ff7d29295ddb6fd3ef7ed61e28e1d9, _9ec06cf3eb9a0094aeead9c588b6b5b08fc32229da09bfc2bb4ac41d71494460, _65edcb348d4867dd28dd7555368812aa6c14c954a3f93138d5dab2f440671112, _2ca478ecada4f4a1780897f5c2a3bdaf58ee7f5730f3444b1a7b85c75ad88bdc, a8e31c33072a98a995d13978612e9665b6fd6b18ce4f64ab6251d0e8bff758d5, bc21643bd5ba8ee75814ccf6a49295bcf1703e78fadbbd465c17bf37f9099950, cbbebd9f678a28018225449b7dbccdb36bf97d755d67aae4387353bdef9f5ad5, f553c34af8321009731fe2f8657548fb92b970e5d2173f06f9b353395f1f806b, _467ef556e98765ad382a6d87c083bd6b7e7ec656f92f836198574803cc06fcd7, _398e7535a96a954532fb15da8bc1e7d422e15f07593f38046f47e18f5c5e4e49, _171f5f7c537f5ce71a79da325fb71a0fbe138e9b60fcff82d38ac13c57447bef, _396e873f485301e6e91022d5c78c1160909ba68a9a3c53e07258a78e2cf38d1f, _0ad05b9617ee862b52accca6f825fcc929dc43b2b2d9bbbd82653f6bded3bfea, ffa567dc6d42d8c398baf4fe2641a63eb5223a1d2593b3d78a03f89b25c03d48, _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8, _35276085c67b7bf7ca05d0230872922dcda75f0e6a7427cdaa352c75017f8252, _7daeda62653513d82d0793c03a91510e673a8be0857872ad94982e1d012f08d4):

    def __init__(self):
        _0ad05b9617ee862b52accca6f825fcc929dc43b2b2d9bbbd82653f6bded3bfea.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _1e34a83ecceffcab0b7efb8cfa373ede09ff7d29295ddb6fd3ef7ed61e28e1d9.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _9ec06cf3eb9a0094aeead9c588b6b5b08fc32229da09bfc2bb4ac41d71494460.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _65edcb348d4867dd28dd7555368812aa6c14c954a3f93138d5dab2f440671112.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _2ca478ecada4f4a1780897f5c2a3bdaf58ee7f5730f3444b1a7b85c75ad88bdc.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        a8e31c33072a98a995d13978612e9665b6fd6b18ce4f64ab6251d0e8bff758d5.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        bc21643bd5ba8ee75814ccf6a49295bcf1703e78fadbbd465c17bf37f9099950.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        ffa567dc6d42d8c398baf4fe2641a63eb5223a1d2593b3d78a03f89b25c03d48.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _5b40cd78425304ee19734dc39cbcdbfdcf179ee43dc98794765aa713cb1553f8.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        f553c34af8321009731fe2f8657548fb92b970e5d2173f06f9b353395f1f806b.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        cbbebd9f678a28018225449b7dbccdb36bf97d755d67aae4387353bdef9f5ad5.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _398e7535a96a954532fb15da8bc1e7d422e15f07593f38046f47e18f5c5e4e49.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _467ef556e98765ad382a6d87c083bd6b7e7ec656f92f836198574803cc06fcd7.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _396e873f485301e6e91022d5c78c1160909ba68a9a3c53e07258a78e2cf38d1f.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _171f5f7c537f5ce71a79da325fb71a0fbe138e9b60fcff82d38ac13c57447bef.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _35276085c67b7bf7ca05d0230872922dcda75f0e6a7427cdaa352c75017f8252.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
        _7daeda62653513d82d0793c03a91510e673a8be0857872ad94982e1d012f08d4.__init__(_06c604b332b386b6cce8355ccf27fffd3a98b7a7a5b9b3a550c039c6ebae38e4)
