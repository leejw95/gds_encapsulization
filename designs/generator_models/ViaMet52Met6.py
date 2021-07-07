from designs import StickDiagram
from designs import DesignParameters
from gds_editor_ver3 import user_define_exceptions
from designs import DRC

import ftplib
from ftplib import FTP
import base64


class _ViaMet52Met6(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_NumberOfCOX=None, _NumberOfCOY=None,
                                          _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'),
                                          )



    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met6Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL6'][0],_Datatype=DesignParameters._LayerMapping['METAL6'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met5Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL5'][0],_Datatype=DesignParameters._LayerMapping['METAL5'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA56'][0],_Datatype=DesignParameters._LayerMapping['VIA56'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
                                                   )

        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name

    def _CalculateViaMet52Met6DesignParameter(self, _NumberOfCOX=None, _NumberOfCOY=None,
                                              _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):
        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet52Met6 = [[0,0]]


        print('#############################     Met5 Layer Calculation   ##############################################')
        if _MetalType['METAL6'] == 'X':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Y':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_NumberOfCOX,NumOfVIAyY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Z':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_NumberOfCOX,NumOfVIAzY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'R':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_NumberOfCOX,NumOfVIArY=_NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')


        print('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        # self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
        # self._DesignParameter['_Met6Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        # self._DesignParameter['_Met6Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


    def _CalculateViaMet52Met6DesignParameterMinimumEnclosureX(self, _NumberOfCOX=None, _NumberOfCOY=None,
                                                               _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet52Met6 = [[0,0]]


        print('#############################     Met5 Layer Calculation   ##############################################')
        if _MetalType['METAL6'] == 'X':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Y':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_NumberOfCOX,NumOfVIAyY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Z':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_NumberOfCOX,NumOfVIAzY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'R':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_NumberOfCOX,NumOfVIArY=_NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        # self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
        # self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        # self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        print('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        # self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
        # self._DesignParameter['_Met6Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        #
        # self._DesignParameter['_Met6Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        #
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')


        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        # self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

    def _CalculateViaMet52Met6DesignParameterMinimumEnclosureY(self, _NumberOfCOX=None, _NumberOfCOY=None,
                                                               _MetalType = dict(METAL1 = 'X', METAL2 = 'X', METAL3 = 'X', METAL4 = 'X', METAL5 = 'X', METAL6 = 'X', METAL7 = 'X', METAL8 = 'Z', METAL9 = 'Z'), ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet52Met6 = [[0,0]]


        print('#############################     Met5 Layer Calculation   ##############################################')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        if _MetalType['METAL6'] == 'X':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Y':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAyMinWidth + _DRCObj.DRCVIAyMinSpace(NumOfVIAyX=_NumberOfCOX,NumOfVIAyY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'Z':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_NumberOfCOX,NumOfVIAzY=_NumberOfCOY )
        elif _MetalType['METAL6'] == 'R':
            _LengthViaMet52Met6BtwCO = _DRCObj._VIArMinWidth + _DRCObj.DRCVIArMinSpace(NumOfVIArX=_NumberOfCOX,NumOfVIArY=_NumberOfCOY )
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
        # self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        # self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met5Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met5Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met5Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        print('#############################     Met2 Layer Calculation   ##############################################')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        # self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
        # self._DesignParameter['_Met6Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        #
        # self._DesignParameter['_Met6Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAyMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO])
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO])
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_Met6Layer']['_XYCoordinates']=_XYCoordinateOfViaMet52Met6
            self._DesignParameter['_Met6Layer']['_XWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOX - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2, _DRCObj._MetalyMinEnclosureCO2, _DRCObj._MetalzMinEnclosureCO2, _DRCObj._MetalrMinEnclosureCO2])
            self._DesignParameter['_Met6Layer']['_YWidth']=_DRCObj._VIArMinWidth + (_NumberOfCOY - 1)* _LengthViaMet52Met6BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO, _DRCObj._MetalyMinEnclosureCO, _DRCObj._MetalzMinEnclosureCO, _DRCObj._MetalrMinEnclosureCO])
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')

        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        # self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        # self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        if _MetalType['METAL6'] == 'X':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        elif _MetalType['METAL6'] == 'Y':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAyMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAyMinWidth
        elif _MetalType['METAL6'] == 'Z':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        elif _MetalType['METAL6'] == 'R':
            self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIArMinWidth
            self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIArMinWidth
        else:
            raise user_define_exceptions.IncorrectInputError('_MetalType should have a value among X Y Z R')
        # _LengthViaMet52Met6BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet52Met6BtwCO + j*_LengthViaMet52Met6BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet52Met6[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet52Met6BtwCO + i * _LengthViaMet52Met6BtwCO,
                                        _XYCoordinateOfViaMet52Met6[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet52Met6BtwCO +j*_LengthViaMet52Met6BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet52Met6 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

if __name__=='__main__':
    pass