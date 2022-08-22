from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

class _NbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict( _NumberOfNbodyCOX=None, _NumberOfNbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None)
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),  #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _NPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NIMP'][0],_Datatype=DesignParameters._LayerMapping['NIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    # _PDKLayer=dict(_DesignParametertype=1,_Layer=DesignParameters._LayerMapping['PDK'][0], _Datatype=DesignParameters._LayerMapping['PDK'][1],_XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateNbodyContactDesignParameter(self, _NumberOfNbodyCOX=None, _NumberOfNbodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None ):
        print ('#########################################################################################################')
        print(('                                  {}  NbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        _DRCObj=DRC.DRC()
        _XYCoordinateOfNbodyContact=[[0,0]]

        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfNbodyCOX,NumOfCOY=_NumberOfNbodyCOY )


        print ('#############################     DIFF Layer Calculation    ##############################################')

        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfNbodyContact

        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOX - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOY - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        print ('#############################     NIMP  Layer Calculation    ##############################################')
        if not DesignParameters._Technology == 'SS28nm':
            self._DesignParameter['_NPLayer']['_XYCoordinates']=_XYCoordinateOfNbodyContact
            self._DesignParameter['_NPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._NpMinExtensiononNactive
            self._DesignParameter['_NPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._NpMinExtensiononNactive



        print ('###########################     Metal1  Layer Calculation    ##############################################')


        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfNbodyContact

        if _Met1XWidth==None and _Met1YWidth == None:
            self._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_Met1Layer']['_YWidth']  = self._DesignParameter['_ODLayer']['_YWidth']
        elif _Met1XWidth!=None and _Met1YWidth == None:
            self._DesignParameter['_Met1Layer']['_XWidth']  = _Met1XWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        elif _Met1XWidth==None and _Met1YWidth != None:
            self._DesignParameter['_Met1Layer']['_XWidth']  = self._DesignParameter['_ODLayer']['_XWidth']
            self._DesignParameter['_Met1Layer']['_YWidth'] = _Met1YWidth

        else:
            self._DesignParameter['_Met1Layer']['_XWidth'] =_Met1XWidth
            self._DesignParameter['_Met1Layer']['_YWidth'] =_Met1YWidth


        print ('#############################     CONT Layer Caculation    ##############################################')

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmp=[]
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfNbodyCOX,NumOfCOY=_NumberOfNbodyCOY )


        for i in range(0, _NumberOfNbodyCOX):
            for j in range(0, _NumberOfNbodyCOY):

                if (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]
                elif (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY-1)/2*_LengthNbodyBtwCO +j*_LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 1 and (_NumberOfNbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX -1) / 2  * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 1 and (_NumberOfNbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX -1) / 2  * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY-1)/2*_LengthNbodyBtwCO +j*_LengthNbodyBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp






        del _DRCObj

        print ('#########################################################################################################')
        print(('                                  {}  NbodyContact Calculation End                                       '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')





