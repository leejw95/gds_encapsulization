from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

class _ViaMet72Met8(StickDiagram_KJH0._StickDiagram_KJH):
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



if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A14_ViaMet72Met8_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _ViaMet72Met8NumberOfCOX=9,
        _ViaMet72Met8NumberOfCOY=9,
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
    LayoutObj = _ViaMet72Met8(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateViaMet72Met8DesignParameter(**InputParams)
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