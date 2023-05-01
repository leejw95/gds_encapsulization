from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

class _PMOS(StickDiagram_KJH0._StickDiagram_KJH):
    _ParametersForDesignCalculation = dict(_PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None,
                                           _PMOSDummy=False, _GateSpacing=None, _SDWidth=None, _XVT=None, _PCCrit=None)

    def __init__(self, _DesignParameter=None, _Name=None):

        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _ODLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                          _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),  # boundary type:1, #path type:2, #sref type: 3, #gds data type: 4, #Design Name data type: 5,  #other data type: ?
                _ODLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _POLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _POLayerPINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                    _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                    _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _Met1Layer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                            _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _METAL1PINDrawing=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                   _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                   _XYCoordinates=[], _XWidth=400, _YWidth=400),
                _PPLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                          _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _COLayer=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['CONT'][0],
                                                          _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                          _XYCoordinates=[],_XWidth=400, _YWidth=400),
                _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                _XYCoordinatePMOSSupplyRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSOutputRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                _XYCoordinatePMOSGateRouting=dict(_DesignParametertype=7,_XYCoordinates=[]),
                # DistanceXBtwPoly=self._SizeInfoDeclaration(_DesignSizesInList=None)
            )

        if _Name != None:
            self._DesignParameter['_Name']['_Name'] = _Name

    def _CalculateDesignParameter(self, _PMOSNumberofGate=None, _PMOSChannelWidth=None, _PMOSChannellength=None,
                                      _PMOSDummy=False, _GateSpacing=None, _SDWidth=None, _XVT=None, _PCCrit=None):
        print ('#########################################################################################################')
        print ('                                    {}  PMOS Calculation Start                                    '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')

        _DRCObj = DRC.DRC()
        _XYCoordinateOfPMOS = [[0,0]]

        _LengthPMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth

        if DesignParameters._Technology == '028nm':
            _LengthPMOSBtwPO = _DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength) + _PMOSChannellength
        else:
            _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + _PMOSChannellength
        if _GateSpacing:
            _LengthPMOSBtwPO = _GateSpacing + _PMOSChannellength
        print ('#############################     POLY (PO/PC) Layer Calculation    ##############################################')
        # POLY Layer Coordinate Calc
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO,
                                    _XYCoordinateOfPMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwPO + i * _LengthPMOSBtwPO,
                                    _XYCoordinateOfPMOS[0][1]]
            tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_POLayer']['_XWidth'] = _PMOSChannellength
        self._DesignParameter['_POLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_PMOSChannellength)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXYs

        print('#############################     POLY Dummy Layer Calculation    ##############################################')
        _PODummyLayer = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['POLY'][0],
            _Datatype=DesignParameters._LayerMapping['POLY'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[
                [a + b for a, b in zip(self._DesignParameter['_POLayer']['_XYCoordinates'][0], [-_LengthPMOSBtwPO, 0])],
                [a + b for a, b in zip(self._DesignParameter['_POLayer']['_XYCoordinates'][-1], [_LengthPMOSBtwPO, 0])]
            ])

        if _PMOSDummy == False :
            _PODummyLayer['_XWidth'] = 0
            _PODummyLayer['_YWidth'] = 0

            self._DesignParameter['_PODummyLayer'] = _PODummyLayer

        elif _PMOSDummy:

            if DesignParameters._Technology != '028nm':
                a = 0
            else:
                a = 16

            _PODummyLayer['_XWidth'] = _PMOSChannellength
            _PODummyLayer['_YWidth'] = _PMOSChannelWidth + 2 * a

            self._DesignParameter['_PODummyLayer'] = _PODummyLayer

            ##modified for dummy drc
            if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:
                self._DesignParameter['_PODummyLayer']['_YWidth'] = self.CeilMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing * 2)

            else:
                pass
            ##End of modification (by 1joon)

        #     if float(self._DesignParameter['_PODummyLayer']['_XWidth']) * float(self._DesignParameter['_PODummyLayer']['_YWidth']) < _DRCObj._PODummyMinArea:  # Should check at TSMC
        #         self._DesignParameter['_PODummyLayer']['_YWidth'] = self.CeilMinSnapSpacing(float(_DRCObj._PODummyMinArea) / float(self._DesignParameter['_PODummyLayer']['_XWidth']), _DRCObj._MinSnapSpacing*2)
        #         if DesignParameters._Technology != 'SS28nm':
        #             self._DesignParameter['_POLayer']['_YWidth'] = self._DesignParameter['_PODummyLayer']['_YWidth']
        #     else:
        #         pass
        # else:
        #     pass


        print ('#############################     DIFF (OD/RX) Layer Calculation    ##############################################')
        if _PMOSDummy and DesignParameters._Technology != '028nm':
            XWidth_OD = self._DesignParameter['_PODummyLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] + _PMOSChannellength + 2 * _DRCObj._PolygateMinExtensionOnODX
        else:
            XWidth_OD = _LengthPMOSBtwPO * _PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_XWidth'] = XWidth_OD
        self._DesignParameter['_ODLayer']['_YWidth'] = _PMOSChannelWidth
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS


        print ('#############################     METAL1 Layer Calculation    ##############################################')
        # METAL1 Layer Coordinate Setting
        _LengthPMOSBtwMet1 = _LengthPMOSBtwPO
        _tmpCOYNum = max(2,int(float(self._DesignParameter['_ODLayer']['_YWidth']
                                       - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])
                                       + _DRCObj._CoMinSpace)
                                 / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth)))


        tmpXYs = []
        for i in range(0, _PMOSNumberofGate + 1):  # the number of the metal = the number of the gate + 1
            if (_PMOSNumberofGate % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                    _XYCoordinateOfPMOS[0][1]]
            else:
                _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                    _XYCoordinateOfPMOS[0][1]]
            tmpXYs.append(_xycoordinatetmp)


        if _SDWidth == None :
            self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        else :
            self._DesignParameter['_Met1Layer']['_XWidth'] = _SDWidth

        self._DesignParameter['_Met1Layer']['_YWidth'] = (_tmpCOYNum - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2

        # if _SDMinHeight == True :
        #     self._DesignParameter['_Met1Layer']['_YWidth'] = (_tmpCOYNum - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2
        # else :
        #     self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs
        #del _tmpCOYNum

        if DesignParameters._Technology == '028nm':
            self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']
            self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']
            self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']


        print ('############################# CONT (Source/Drain) Layer Calculation    ##############################################')
        # CONT XNum/YNum Calculation
        _XNumberOfCOInPMOS = _PMOSNumberofGate + 1
        _YNumberOfCOInPMOS = max(2,int(float(self._DesignParameter['_ODLayer']['_YWidth']
                                       - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])
                                       + _DRCObj._CoMinSpace)
                                 / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth)))

        # Check the number of CO On PMOS TR
        if (_XNumberOfCOInPMOS == 0) or (_YNumberOfCOInPMOS == 0):
            print ('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0

        # CONT XY coordinates Calculation
        tmpXYs = []
        for i in range(0, _XNumberOfCOInPMOS):
            for j in range(0, _YNumberOfCOInPMOS):
                if (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                elif (_XNumberOfCOInPMOS % 2) == 1 and (_YNumberOfCOInPMOS% 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                elif (_XNumberOfCOInPMOS % 2) == 0 and (_YNumberOfCOInPMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                else:
                    _xycoordinatetmp = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                                        _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                tmpXYs.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs



        # XVT Layer Calculation
        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = '_' + _XVT + 'Layer'
                _XVTLayerMappingName = _XVT
            elif (DesignParameters._Technology == 'TSMC65nm') and _XVT in ('LVT', 'HVT'):
                _XVTLayer = '_P' + _XVT + 'Layer'
                _XVTLayerMappingName = 'P' + _XVT
            elif (DesignParameters._Technology == 'TSMC65nm') and (_XVT == None):
                _XVTLayer = None

            elif DesignParameters._Technology == '028nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for 028nm".format(_XVT))
            elif DesignParameters._Technology == 'TSMC65nm':
                raise NotImplementedError("Invalid '_XVT' argument({}) for TSMC65nm".format(_XVT))
            else:
                raise NotImplementedError("Not Implemented in other technology : {}".format(DesignParameters._Technology))

            if _XVTLayer != None:
                print ('#############################     {0} Layer Calculation    ##############################################'.format(_XVTLayer))
                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
                    _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
                    _XWidth=self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX,
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY,
                    _XYCoordinates=self._DesignParameter['_ODLayer']['_XYCoordinates']
                )

        except Exception as e:
            print('Error Occurred', e)
            raise NotImplementedError

        print ('#############################     PIMP (PP/BP) Layer Calculation    ####################')  # Need to check
        if (DesignParameters._Technology == 'TSMC65nm') and (_PMOSDummy == True):
            XWidth_PP_byPO = self._DesignParameter['_PODummyLayer']['_XWidth'] \
                             + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] -
                                self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) \
                             + 2 * _DRCObj._PpMinEnclosureOfPo
        else:
            XWidth_PP_byPO = 0

        XWidth_PP_byOD = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive

        self._DesignParameter['_PPLayer']['_XWidth'] = max(XWidth_PP_byPO, XWidth_PP_byOD)
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter[_XVTLayer]['_YWidth']#self._DesignParameter['_POLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPo
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS



        if DesignParameters._Technology == '028nm' and _PCCrit!=False:
            print ('#############################     PCCRIT Layer Calculation    ##############################################')
            if self._DesignParameter['_POLayer']['_XWidth'] in (30, 34):
                self._DesignParameter['_PCCRITLayer'] = self._BoundaryElementDeclaration(
                    _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                    _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                    _XWidth=_PMOSNumberofGate * _LengthPMOSBtwMet1 + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension,
                    _YWidth=self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension,
                    _XYCoordinates=_XYCoordinateOfPMOS
                )
            else:
                pass


        print ('#########################     Supply Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0,(_PMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Output Routing Coordinates Calculation    ##################################')
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate // 2):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0, (_PMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + (i * 2 + 1) * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'] = tmpXYs


        print ('#########################     Gate Routing Coordinates Calculation   ##################################')
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            if (_PMOSNumberofGate % 2) == 0:
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate / 2 - 0.5) * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
            else:
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'] = tmpXYs


        if DesignParameters._Technology == '028nm':  # ?
            print ('##################################################### Diff Pin Generation & Coordinates ####################################################')
            self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] / 2 - (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)
            self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

            self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [
                [(self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                  _XYCoordinateOfPMOS[0][1]],
                [0 - (self._DesignParameter['_ODLayer']['_XWidth'] / 2 + (self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][-1][0] + self._DesignParameter['_POLayer']['_XWidth'] / 2)) / 2,
                 _XYCoordinateOfPMOS[0][1]]
            ]


            print ('##################################################### POLayer Pin Generation & Coordinates ####################################################')
            self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']
            self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2
            tmp1 = []
            tmp2 = []
            for i in range(0, len(self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
                tmp1.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], - (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
                tmp2.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

            if _PMOSNumberofGate == 1:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
            else:
                self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1

        # self._DesignParameter['DistanceXBtwPoly']['_DesignSizesInList'] = _LengthPMOSBtwMet1

        print ('#########################################################################################################')
        print ('                                    {}  PMOS Calculation End                                   '.format(self._DesignParameter['_Name']['_Name']))
        print ('#########################################################################################################')



if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A02_PMOSWithDummy'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        _PMOSNumberofGate=20,
        _PMOSChannelWidth=500,
        _PMOSChannellength=30,
        _PMOSDummy=True,
        _GateSpacing=None,
        _SDWidth=None,
        _XVT='LVT',
        _PCCrit=None,
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
    LayoutObj = _PMOS(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
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
    Checker.DRCchecker()

    print('#############################      Finished      ################################')
	# end of 'main():' ---------------------------------------------------------------------------------------------