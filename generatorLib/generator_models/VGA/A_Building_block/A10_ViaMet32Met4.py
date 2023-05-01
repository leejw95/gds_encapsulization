from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

class _ViaMet32Met4(StickDiagram_KJH0._StickDiagram_KJH):
    _ParametersForDesignCalculation= dict(_ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None )


    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met4Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL4'][0],_Datatype=DesignParameters._LayerMapping['METAL4'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met3Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL3'][0],_Datatype=DesignParameters._LayerMapping['METAL3'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA34'][0],_Datatype=DesignParameters._LayerMapping['VIA34'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name
    # def __init__(self, _ViaMet32Met4DesignParameter=None, _ViaMet32Met4Name=None):
    #
    #     if _ViaMet32Met4DesignParameter!=None:
    #         self._ViaMet32Met4DesignParameter=_ViaMet32Met4DesignParameter
    #     else:
    #         self._ViaMet32Met4DesignParameter=dict(_Technology=[0, None, '065nm'],
    #                                                _XYCoordinateOfViaMet32Met4=[1, None, [0,0]],
    #
    #
    #
    #                                                _XYCoordinateOfMet2=[1, None, [[0,0]]], _XWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],60], _YWidthOfMet2=[2, DesignParameters._LayerMapping['METAL2'][0],400] ,
    #                                                _XYCoordinateOfCO=[1, None, [[0,0]]], _WidthOfCO=[2, DesignParameters._LayerMapping['VIA23'][0],60],
    #                                                _XYCoordinateOfMet3=[1, None, [[0,0]]], _XWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],90], _YWidthOfMet3=[2, DesignParameters._LayerMapping['METAL3'][0],430],
    #
    #                                                _ViaMet32Met4Name=[0, None,'ViaMet32Met4'], _ViaMet32Met4GDSStructure=[4,None,[]],
    #                                                )
    #
    #
    #
    #
    #     if _ViaMet32Met4Name != None:
    #         self._ViaMet32Met4DesignParameter['_ViaMet32Met4Name'][2]=_ViaMet32Met4Name
            

    def _CalculateViaMet32Met4DesignParameter(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateViaMet32Met4DesignParameterMinimumEnclosureX(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

    def _CalculateViaMet32Met4DesignParameterMinimumEnclosureY(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None ):

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX ==0 or _ViaMet32Met4NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0,0]]


        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        self._DesignParameter['_Met3Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_ViaMet32Met4NumberOfCOX - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met3Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)* _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )

        self._DesignParameter['_Met4Layer']['_XYCoordinates']=_XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1)*  _LengthViaMet32Met4BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print ('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX,NumOfVIAxY=_ViaMet32Met4NumberOfCOY )
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):

                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2  * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5 )*_LengthViaMet32Met4BtwCO + j*_LengthViaMet32Met4BtwCO]

                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX -1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY-1)/2 * _LengthViaMet32Met4BtwCO +j*_LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')


    def _CalculateDesignParameterSameEnclosure(self, _ViaMet32Met4NumberOfCOX=None, _ViaMet32Met4NumberOfCOY=None):
        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _ViaMet32Met4NumberOfCOX == 0 or _ViaMet32Met4NumberOfCOY == 0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj = DRC.DRC()
        _XYCoordinateOfViaMet32Met4 = [[0, 0]]

        print ('#############################     Met3 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        self._DesignParameter['_Met3Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met3Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met3Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet32Met4
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOX - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet32Met4NumberOfCOY - 1) * _LengthViaMet32Met4BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        print ('#############################     Cont Layer Calculation   ##############################################')
        tmp = []
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet32Met4BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet32Met4NumberOfCOX, NumOfVIAxY=_ViaMet32Met4NumberOfCOY)
        for i in range(0, _ViaMet32Met4NumberOfCOX):
            for j in range(0, _ViaMet32Met4NumberOfCOY):
                if (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5) * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 0 and (_ViaMet32Met4NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX / 2 - 0.5) * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY - 1) / 2 * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX - 1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY / 2 - 0.5) * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                elif (_ViaMet32Met4NumberOfCOX % 2) == 1 and (_ViaMet32Met4NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet32Met4[0][0] - (_ViaMet32Met4NumberOfCOX - 1) / 2 * _LengthViaMet32Met4BtwCO + i * _LengthViaMet32Met4BtwCO,
                                        _XYCoordinateOfViaMet32Met4[0][1] - (_ViaMet32Met4NumberOfCOY - 1) / 2 * _LengthViaMet32Met4BtwCO + j * _LengthViaMet32Met4BtwCO]
                tmp.append(_xycoordinatetmp)
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        print ('#########################################################################################################')
        print(('                                    {}  ViaMet32Met4 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name'])))
        print ('#########################################################################################################')

if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A10_ViaMet32Met4_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ViaMet32Met4NumberOfCOX=5,
        _ViaMet32Met4NumberOfCOY=5,
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
    LayoutObj = _ViaMet32Met4(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateViaMet32Met4DesignParameter(**InputParams)
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