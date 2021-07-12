from designs import StickDiagram
from designs import DesignParameters
from gds_editor_ver3 import user_define_exceptions
from designs import DRC

import ftplib
from ftplib import FTP
import base64


class _ViaMet12Met2(StickDiagram._StickDiagram):
    _ParametersForDesignCalculation= dict(_NumberOfCOX=None, _NumberOfCOY=None )
    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Met2Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0],_Datatype=DesignParameters._LayerMapping['METAL2'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],_Datatype=DesignParameters._LayerMapping['METAL1'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['VIA12'][0],_Datatype=DesignParameters._LayerMapping['VIA12'][1], _XYCoordinates=[],_XWidth=400, _YWidth=400),
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)


                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateViaMet12Met2DesignParameter(self, _NumberOfCOX=None, _NumberOfCOY=None ):
        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp




        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')


    def _CalculateViaMet12Met2DesignParameterMinimumEnclosureX(self, _NumberOfCOX=None, _NumberOfCOY=None ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])



        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp


        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

    def _CalculateViaMet12Met2DesignParameterMinimumEnclosureY(self, _NumberOfCOX=None, _NumberOfCOY=None ):

        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

        ###############################################Check the number of CO On Via Contact###########################################################################################
        if _NumberOfCOX ==0 or _NumberOfCOY==0:
            print('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
        ###############################################################################################################################################################################
        _DRCObj=DRC.DRC()
        _XYCoordinateOfViaMet12Met2 = [[0,0]]


        print('#############################     Met1 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        self._DesignParameter['_Met1Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met1Layer']['_XWidth']=_DRCObj._VIAxMinWidth+ (_NumberOfCOX - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])
        self._DesignParameter['_Met1Layer']['_YWidth']=_DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)* _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        print('#############################     Met2 Layer Calculation   ##############################################')
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )

        self._DesignParameter['_Met2Layer']['_XYCoordinates']=_XYCoordinateOfViaMet12Met2
        self._DesignParameter['_Met2Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOX - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        self._DesignParameter['_Met2Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_NumberOfCOY - 1)*  _LengthViaMet12Met2BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])



        print('#############################     Cont Layer Calculation   ##############################################')

        tmp=[]
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth
        _LengthViaMet12Met2BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_NumberOfCOX,NumOfVIAxY=_NumberOfCOY )
        for i in range(0, _NumberOfCOX):
            for j in range(0, _NumberOfCOY):

                if (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 0 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX / 2 - 0.5) * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2  * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY / 2 - 0.5 )*_LengthViaMet12Met2BtwCO + j*_LengthViaMet12Met2BtwCO]

                elif (_NumberOfCOX % 2) == 1 and (_NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet12Met2[0][0] - (_NumberOfCOX -1) / 2 * _LengthViaMet12Met2BtwCO + i * _LengthViaMet12Met2BtwCO,
                                        _XYCoordinateOfViaMet12Met2[0][1] - (_NumberOfCOY-1)/2 * _LengthViaMet12Met2BtwCO +j*_LengthViaMet12Met2BtwCO]
                tmp.append(_xycoordinatetmp)


        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp
        del _DRCObj
        print('#########################################################################################################')
        print('                                    {}  ViaMet12Met2 Calculation End                                    '.format(self._DesignParameter['_Name']['_Name']))
        print('#########################################################################################################')

if __name__=='__main__':
    ViaMet12Met2Obj1=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test1')
    ViaMet12Met2Obj1._CalculateViaMet12Met2DesignParameter(_NumberOfCOX=3, _NumberOfCOY=4 )
    ViaMet12Met2Obj2=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test2')
    ViaMet12Met2Obj2._CalculateViaMet12Met2DesignParameterMinimumEnclosureY(_NumberOfCOX=3, _NumberOfCOY=4 )
    ViaMet12Met2Obj3=_ViaMet12Met2(_DesignParameter=None, _Name='ViaMet12Met2test3')
    ViaMet12Met2Obj3._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(_NumberOfCOX=3, _NumberOfCOY=4 )
    #ViaMet12Met2Obj=_ViaMet12Met2(_ViaMet12Met2DesignParameter=DesignParameters.ViaMet12Met2DesignParameter, _ViaMet12Met2Name='ViaMet12Met22test')
    #ViaMet12Met2Obj=_ViaMet12Met2(_Technology=DesignParameters._Technology, _XYCoordinatePbody=[0,0], _NumberOfPbodyCO=2, _WidthXPbodyOD=890, _WidthYPbodyOD=420, _WidthXPbodyNP=1250, _WidthYPbodyNP=780, _WidthPbodyCO=220, _LengthPbodyBtwCO=470, _WidthXPbodyMet1=810, _WidthYPbodyMet1=340, _PbodyName='ViaMet12Met2')
    ViaMet12Met2Obj1._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj1._DesignParameter)
    ViaMet12Met2Obj2._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj2._DesignParameter)
    ViaMet12Met2Obj3._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary= ViaMet12Met2Obj3._DesignParameter)

    testStreamFile=open('./testStreamFile1.gds','wb')

    tmp1=ViaMet12Met2Obj1._CreateGDSStream(ViaMet12Met2Obj1._DesignParameter['_GDSFile']['_GDSFile'])

    tmp1.write_binary_gds_stream(testStreamFile)
    testStreamFile=open('./testStreamFile2.gds','wb')

    tmp2=ViaMet12Met2Obj2._CreateGDSStream(ViaMet12Met2Obj2._DesignParameter['_GDSFile']['_GDSFile'])

    tmp2.write_binary_gds_stream(testStreamFile)

    testStreamFile=open('./testStreamFile3.gds','wb')

    tmp3=ViaMet12Met2Obj3._CreateGDSStream(ViaMet12Met2Obj3._DesignParameter['_GDSFile']['_GDSFile'])

    tmp3.write_binary_gds_stream(testStreamFile)

    testStreamFile.close()
    print('###############open ftp connection & update gds file to cadence server###################')
    ftp_cadence_server=ftplib.FTP('141.223.86.109')
    ftp_cadence_server.login(base64.b64decode('YWxlY25ldzE='),base64.b64decode('NzNoazNhYWs='))
    if DesignParameters._Technology =='065nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/design_automation')
    elif DesignParameters._Technology =='180nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC018')
    elif DesignParameters._Technology =='045nm':
        ftp_cadence_server.cwd('/home/alecnew1/OPUS/DesignAutomationTSMC45')
    print(ftp_cadence_server.pwd())
    testStreamFile=open('./testStreamFile1.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile1.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile2.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile2.gds', testStreamFile)
    testStreamFile.close()
    testStreamFile=open('./testStreamFile3.gds','rb')
    ftp_cadence_server.storbinary('STOR testStreamFile3.gds', testStreamFile)
    testStreamFile.close()
    print('close ftp connection')
    ftp_cadence_server.quit()
    testStreamFile.close()

    print('##########################################################################################')