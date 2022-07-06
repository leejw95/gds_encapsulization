from generatorLib import StickDiagram
from generatorLib import DesignParameters
from generatorLib import DRC

class _ViaMet72Met8(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_ViaMet72Met8NumberOfCOX=None, _ViaMet72Met8NumberOfCOY=None )


    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met7Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL7'][0],_Datatype=DesignParameters._LayerMapping['METAL7'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met8Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL8'][0],_Datatype=DesignParameters._LayerMapping['METAL8'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA78'][0],_Datatype=DesignParameters._LayerMapping['VIA78'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name
    

    def _CalculateViaMet72Met8DesignParameter(self, _ViaMet72Met8NumberOfCOX=None, _ViaMet72Met8NumberOfCOY=None ):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet72Met8NumberOfCOX ==0 or _ViaMet72Met8NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet72Met8 = [[0,0]]


        print ('#############################     Met7 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met7Layer']['_XWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOX - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])
        self._DesignParameter['_Met7Layer']['_YWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])

        print ('#############################     Met8 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )

        self._DesignParameter['_Met8Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met8Layer']['_XWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOX - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])
        self._DesignParameter['_Met8Layer']['_YWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        for i in range(0, _ViaMet72Met8NumberOfCOX):
            for j in range(0, _ViaMet72Met8NumberOfCOY):

                if (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2  * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2 * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateViaMet72Met8DesignParameterMinimumEnclosureX(self, _ViaMet72Met8NumberOfCOX=None, _ViaMet72Met8NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet72Met8NumberOfCOX ==0 or _ViaMet72Met8NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet72Met8 = [[0,0]]


        print ('#############################     Met7 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAzMinWidth+ (_ViaMet72Met8NumberOfCOX - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([1,_DRCObj._MetalzMinEnclosureCO])
        self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])

        print ('#############################     Met8 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )

        self._DesignParameter['_Met8Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met8Layer']['_XWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOX - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([1,_DRCObj._MetalzMinEnclosureCO])

        self._DesignParameter['_Met8Layer']['_YWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        for i in range(0, _ViaMet72Met8NumberOfCOX):
            for j in range(0, _ViaMet72Met8NumberOfCOY):

                if (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2  * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2 * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

    def _CalculateViaMet72Met8DesignParameterMinimumEnclosureY(self, _ViaMet72Met8NumberOfCOX=None, _ViaMet72Met8NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet72Met8NumberOfCOX ==0 or _ViaMet72Met8NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet72Met8 = [[0,0]]


        print ('#############################     Met7 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        self._DesignParameter['_Met7Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met7Layer']['_XWidth']=_DRCObj._VIAzMinWidth+ (_ViaMet72Met8NumberOfCOX - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])
        self._DesignParameter['_Met7Layer']['_YWidth']=_DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)* _LengthViaMet72Met8BtwCO+ 2 * max([1,_DRCObj._MetalzMinEnclosureCO])

        print ('#############################     Met8 Layer Calculation   ##############################################')
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )

        self._DesignParameter['_Met8Layer']['_XYCoordinates']=_XYCoordinateOfViaMet72Met8
        self._DesignParameter['_Met8Layer']['_XWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOX - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([12,_DRCObj._MetalzMinEnclosureCO2])

        self._DesignParameter['_Met8Layer']['_YWidth'] = _DRCObj._VIAzMinWidth + (_ViaMet72Met8NumberOfCOY - 1)*  _LengthViaMet72Met8BtwCO+ 2 * max([1,_DRCObj._MetalzMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAzMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAzMinWidth
        _LengthViaMet72Met8BtwCO = _DRCObj._VIAzMinWidth + _DRCObj.DRCVIAzMinSpace(NumOfVIAzX=_ViaMet72Met8NumberOfCOX,NumOfVIAzY=_ViaMet72Met8NumberOfCOY )
        for i in range(0, _ViaMet72Met8NumberOfCOX):
            for j in range(0, _ViaMet72Met8NumberOfCOY):

                if (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 0 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX / 2 - 0.5) * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2  * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY / 2 - 0.5 )*_LengthViaMet72Met8BtwCO + j*_LengthViaMet72Met8BtwCO]

                elif (_ViaMet72Met8NumberOfCOX % 2) == 1 and (_ViaMet72Met8NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet72Met8[0][0] - (_ViaMet72Met8NumberOfCOX -1) / 2 * _LengthViaMet72Met8BtwCO + i * _LengthViaMet72Met8BtwCO,
                                        _XYCoordinateOfViaMet72Met8[0][1] - (_ViaMet72Met8NumberOfCOY-1)/2 * _LengthViaMet72Met8BtwCO +j*_LengthViaMet72Met8BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet72Met8 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

if __name__=='__main__':
    pass