from designs import StickDiagram
from designs import DesignParameters
from gds_editor_ver3 import user_define_exceptions
from designs import DRC
import ftplib
from ftplib import FTP
import base64

class _PbodyContact(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict( _NumberOfBodyCOX=None, _NumberOfBodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],_Datatype=DesignParameters._LayerMapping['DIFF'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400), #boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],_Datatype=DesignParameters._LayerMapping['PIMP'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],_Datatype=DesignParameters._LayerMapping['CONT'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    # _PDKLayer=dict(_DesignParametertype=1,_Layer=DesignParameters._LayerMapping['PDK'][0], _Datatype=DesignParameters._LayerMapping['PDK'][1],_XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),

                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


        
    def _CalculatePbodyContactDesignParameter(self,  _NumberOfBodyCOX=None, _NumberOfBodyCOY=None,  _Met1XWidth=None, _Met1YWidth=None ):
        print('#########################################################################################################')
        print('                                  {}  PbodyContact Calculation Start                                     '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')
        _DRCObj=DRC.DRC()
        _XYCoordinateOfPbodyContact = [[0,0]]





        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfBodyCOX,NumOfCOY=_NumberOfBodyCOY )

        print('#############################     DIFF Layer Calculation    ##############################################')

        self._DesignParameter['_ODLayer']['_XYCoordinates']=_XYCoordinateOfPbodyContact

        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfBodyCOX - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfBodyCOY - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide




        print('#############################     PIMP  Layer Calculation    ##############################################')
        self._DesignParameter['_PPLayer']['_XYCoordinates']=_XYCoordinateOfPbodyContact
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

        print('###########################     Metal1  Layer Calculation    ##############################################')


        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfPbodyContact

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


        print('#############################     CONT Layer Caculation    ##############################################')

        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        tmp=[]
        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfBodyCOX,NumOfCOY=_NumberOfBodyCOY )


        for i in range(0, _NumberOfBodyCOX):
            for j in range(0, _NumberOfBodyCOY):

                if (_NumberOfBodyCOX % 2) == 0 and (_NumberOfBodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfBodyCOX / 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfBodyCOY / 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]
                elif (_NumberOfBodyCOX % 2) == 0 and (_NumberOfBodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfBodyCOX / 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfBodyCOY-1)/2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]

                elif (_NumberOfBodyCOX % 2) == 1 and (_NumberOfBodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfBodyCOX -1) / 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfBodyCOY / 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                elif (_NumberOfBodyCOX % 2) == 1 and (_NumberOfBodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfBodyCOX -1) / 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfBodyCOY-1)/2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp






        del _DRCObj
        print('#########################################################################################################')
        print('                                  {}  PbodyContact Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')
        



if __name__=='__main__':


    PbodyContactObj=_PbodyContact(_DesignParameter=None, _Name='PbodyContact')
    PbodyContactObj._CalculatePbodyContactDesignParameter(_NumberOfBodyCOX=3, _NumberOfBodyCOY=1, _Met1XWidth=1000, _Met1YWidth=500)
    #PbodyContactObj=_PbodyContact(_PbodyContactDesignParameter=DesignParameters.PbodyDesignParameter, _PbodyContactName='PbodyContact2')
    #PbodyContactObj=_PbodyContact(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet1=810, _WidthYPbodyMet1=340, _PbodyName='PbodyContact')
    PbodyContactObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=PbodyContactObj._DesignParameter)
    testStreamFile=open('./testStreamFile.gds','wb')

    tmp=PbodyContactObj._CreateGDSStream(PbodyContactObj._DesignParameter['_GDSFile']['_GDSFile'])

    tmp.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    

    print('##########################################################################################')