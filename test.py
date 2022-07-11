from generatorLib import DRC
from generatorLib import DesignParameters
from generatorLib import DRC
from datetime import datetime, MAXYEAR

from gds_editor_ver3 import user_define_exceptions
class _ViaMet62Met7(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet62Met7NumberOfCOX=None, _ViaMet62Met7NumberOfCOY=None,
                                          _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'),
                                          )



    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met7Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0],_Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met6Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA67'][0],_Datatype=DesignParameters._LayerMapping['VIA67'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
                                                   )

        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


print ("SSSSSS")