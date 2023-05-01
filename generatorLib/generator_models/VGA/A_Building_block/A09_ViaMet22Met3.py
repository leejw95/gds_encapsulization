from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC


class _ViaMet22Met3(StickDiagram_KJH0._StickDiagram_KJH):

    _ParametersForDesignCalculation= dict(_ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA23'][0],_Datatype=DesignParameters._LayerMapping['VIA23'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateViaMet22Met3DesignParameter(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateDesignParameterSameEnclosure(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None):
        '''
            It is different with _CalculateViaMet22Met3DesignParameter()
            _Metal1MinEnclosureVia12 -> _Metal1MinEnclosureVia3
            _MetalxMinEnclosureCO2   -> _MetalxMinEnclosureVia3
        '''
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX == 0 or _ViaMet22Met3NumberOfCOY == 0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj = DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY)
        self._DesignParameter['_Met3Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1) * _LengthViaMet22Met3BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met3Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1) * _LengthViaMet22Met3BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY)
        self._DesignParameter['_Met2Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1) * _LengthViaMet22Met3BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1) * _LengthViaMet22Met3BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp = []
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY)
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):
                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5) * _LengthViaMet22Met3BtwCO + j * _LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY - 1) / 2 * _LengthViaMet22Met3BtwCO + j * _LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX - 1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5) * _LengthViaMet22Met3BtwCO + j * _LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX - 1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY - 1) / 2 * _LengthViaMet22Met3BtwCO + j * _LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateViaMet22Met3DesignParameterMinimumEnclosureX(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

    def _CalculateViaMet22Met3DesignParameterMinimumEnclosureY(self, _ViaMet22Met3NumberOfCOX=None, _ViaMet22Met3NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet22Met3NumberOfCOX ==0 or _ViaMet22Met3NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet22Met3 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)* _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet22Met3
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOX - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet22Met3NumberOfCOY - 1)*  _LengthViaMet22Met3BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet22Met3BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet22Met3NumberOfCOX,NumOfVIAxY=_ViaMet22Met3NumberOfCOY )
        for i in range(0, _ViaMet22Met3NumberOfCOX):
            for j in range(0, _ViaMet22Met3NumberOfCOY):

                if (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 0 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX / 2 - 0.5) * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2  * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY / 2 - 0.5 )*_LengthViaMet22Met3BtwCO + j*_LengthViaMet22Met3BtwCO]

                elif (_ViaMet22Met3NumberOfCOX % 2) == 1 and (_ViaMet22Met3NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet22Met3[0][0] - (_ViaMet22Met3NumberOfCOX -1) / 2 * _LengthViaMet22Met3BtwCO + i * _LengthViaMet22Met3BtwCO,
                                        _XYCoordinateOfViaMet22Met3[0][1] - (_ViaMet22Met3NumberOfCOY-1)/2 * _LengthViaMet22Met3BtwCO +j*_LengthViaMet22Met3BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet22Met3 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A09_ViaMet22Met3_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ViaMet22Met3NumberOfCOX=4,
        _ViaMet22Met3NumberOfCOY=4,
    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
            InputParams['_NMOSNumberofGate'] = DRCchecker.RandomParam(start=2, stop=20, step=1)         # DRCchecker.RandomParam(start=2, stop=20, step=1)
            InputParams['_NMOSChannelWidth'] = DRCchecker.RandomParam(start=400, stop=1000, step=2)     # DRCchecker.RandomParam(start=200, stop=1000, step=2)
            InputParams['_NMOSChannellength'] = DRCchecker.RandomParam(start=10, stop=20, step=2)
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _ViaMet22Met3(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateViaMet22Met3DesignParameter(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    Checker.Upload2FTP()
    #Checker.DRCchecker()

    print('#############################      Finished      ################################')
	# end of 'main():' ---------------------------------------------------------------------------------------------