from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_PI_4to2_half


class MUX_PI_4to2(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='MUX_PI_4to2'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_v2(self,
                                    TristateInv1_Finger=1,
                                    TristateInv1_PMOSWidth=500,
                                    TristateInv1_NMOSWidth=250,
                                    TristateInv1_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv1_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv1_YCoordOfInputA=None,  # Optional
                                    TristateInv1_YCoordOfInputEN=None,  # Optional
                                    TristateInv1_YCoordOfInputENb=None,  # Optional

                                    TristateInv2_Finger=2,
                                    TristateInv2_PMOSWidth=400,
                                    TristateInv2_NMOSWidth=200,
                                    TristateInv2_VDD2PMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv2_VSS2NMOS=None,  # Optional (Not work when finger >= 3)
                                    TristateInv2_YCoordOfInputA=None,  # Optional
                                    TristateInv2_YCoordOfInputEN=None,  # Optional
                                    TristateInv2_YCoordOfInputENb=None,  # Optional

                                    Inv_Finger=1,
                                    Inv_PMOSWidth=400,
                                    Inv_NMOSWidth=200,
                                    Inv_VDD2PMOS=None,  # Optional
                                    Inv_VSS2NMOS=None,  # Optional
                                    Inv_YCoordOfInOut=None,  # Optional

                                    CellHeight=1800,
                                    ChannelLength=30,
                                    GateSpacing=100,
                                    XVT='SLVT',
                                    SupplyRailType=1,
                                    ):
        """
        top function

        """
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        UnitPitch = ChannelLength + GateSpacing


        Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
                          TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
                          TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
                          TristateInv1_VDD2PMOS=TristateInv1_VDD2PMOS,            # Optional (Not work when finger >= 3)
                          TristateInv1_VSS2NMOS=TristateInv1_VSS2NMOS,            # Optional (Not work when finger >= 3)
                          TristateInv1_YCoordOfInputA=TristateInv1_YCoordOfInputA,      # Optional
                          TristateInv1_YCoordOfInputEN=TristateInv1_YCoordOfInputEN,     # Optional
                          TristateInv1_YCoordOfInputENb=TristateInv1_YCoordOfInputENb,    # Optional

                          TristateInv2_Finger=TristateInv2_Finger,
                          TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
                          TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
                          TristateInv2_VDD2PMOS=TristateInv2_VDD2PMOS,            # Optional (Not work when finger >= 3)
                          TristateInv2_VSS2NMOS=TristateInv2_VSS2NMOS,            # Optional (Not work when finger >= 3)
                          TristateInv2_YCoordOfInputA=TristateInv2_YCoordOfInputA,      # Optional
                          TristateInv2_YCoordOfInputEN=TristateInv2_YCoordOfInputEN,     # Optional
                          TristateInv2_YCoordOfInputENb=TristateInv2_YCoordOfInputENb,    # Optional

                          Inv_Finger=Inv_Finger,
                          Inv_NMOSWidth=Inv_NMOSWidth,
                          Inv_PMOSWidth=Inv_PMOSWidth,
                          Inv_VDD2PMOS=Inv_VDD2PMOS,                 # Optional
                          Inv_VSS2NMOS=Inv_VSS2NMOS,                 # Optional
                          Inv_YCoordOfInOut=Inv_YCoordOfInOut,                # Optional

                          ChannelLength=ChannelLength,
                          GateSpacing=GateSpacing,
                          XVT=XVT,
                          CellHeight=CellHeight,
                          SupplyRailType=SupplyRailType,)


        if CellHeight == None:
            ParametersForMinHeightCalc = dict(
                TristateInv1_Finger=TristateInv1_Finger,
                TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
                TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
                TristateInv2_Finger=TristateInv2_Finger,
                TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
                TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
                Inv_Finger=Inv_Finger,
                Inv_NMOSWidth=Inv_NMOSWidth,
                Inv_PMOSWidth=Inv_PMOSWidth,
                ChannelLength=ChannelLength,
                GateSpacing=GateSpacing,
                XVT=XVT,
                SupplyRailType=SupplyRailType)
            # additional valid check?
            self._DesignParameter['MuxHalf_CalcMinHeight'] = self._SrefElementDeclaration(
                _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf_CalcMinHeightIn{}'.format(_Name)))[0]
            minCellHeight = self._DesignParameter['MuxHalf_CalcMinHeight']['_DesignObj']._CalculateMinHeight(**ParametersForMinHeightCalc)





            Parameters['CellHeight'] = minCellHeight
            _CellHeight = minCellHeight
            print(f"Input CellHeigth={CellHeight}, it is set to minimum value({Parameters['CellHeight']}). ")
        else:
            _CellHeight = CellHeight

        self._DesignParameter['MuxHalf1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf1In{}'.format(_Name)))[0]
        self._DesignParameter['MuxHalf1']['_DesignObj']._CalculateDesignParamter_v2(**Parameters)
        self._DesignParameter['MuxHalf1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['MuxHalf2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf2In{}'.format(_Name)))[0]
        self._DesignParameter['MuxHalf2']['_DesignObj']._CalculateDesignParamter_v2(**Parameters)
        self._DesignParameter['MuxHalf2']['_XYCoordinates'] = [[0, 2*_CellHeight]]

        ''' Between Inverter1 and TristateInverter2 '''
        # Path
        self._DesignParameter['Met2Path1'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path2'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path3'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        self._DesignParameter['Met2Path4'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
            _Width=66
        )
        if TristateInv2_Finger == 1:

            # YCoordOftempRoute1 = 1033
            # YCoordOftempRoute2 = 2567
            YCoordOftempRoute1 = self.getXYTop('MuxHalf1', 'Via1_temp2_3', '_Met2Layer')[0][1] + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            YCoordOftempRoute2 = self.getXYBot('MuxHalf2', 'Via1_temp2_3', '_Met2Layer')[0][1] - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, YCoordOftempRoute1]]   ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, YCoordOftempRoute2]]   ##
            ]

        elif TristateInv2_Finger == 2:
            # YCoordOftempRoute1 = 1033
            # YCoordOftempRoute2 = 2567
            YCoordOftempRoute1 = max(self.getXYTop('MuxHalf1', 'Via1_temp23', '_Met2Layer')[0][1], self.getXYTop('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1]) + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            YCoordOftempRoute2 = min(self.getXYBot('MuxHalf2', 'Via1_temp23', '_Met2Layer')[0][1], self.getXYBot('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1]) - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]     ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]     ##
            ]
        else:
            # YCoordOftempRoute1 = 1066
            # YCoordOftempRoute2 = 2534
            YCoordOftempRoute1 = max(self.getXYTop('MuxHalf1', 'Via1_temp23', '_Met2Layer')[0][1],
                                     self.getXYTop('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1],
                                     self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getYWidth('MuxHalf1', 'Via1_temp23', '_Met2Layer')) \
                                 + drc._MetalxMinSpaceAtCorner + self.getWidth('Met2Path2') / 2
            if self.getXYBot('MuxHalf1', 'TristateInv2', 'via1ForPM1', '_Met2Layer')[0][1] - (YCoordOftempRoute1 + self.getWidth('Met2Path2') / 2) < drc._MetalxMinSpaceAtCorner:
                raise NotImplementedError
            YCoordOftempRoute2 = min(self.getXYBot('MuxHalf2', 'Via1_temp23', '_Met2Layer')[0][1],
                                     self.getXYBot('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1],
                                     self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getYWidth('MuxHalf1', 'Via1_temp23', '_Met2Layer')) \
                                 - drc._MetalxMinSpaceAtCorner - self.getWidth('Met2Path4') / 2
            self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
            ]
            self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]      ##
            ]
            self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
            ]
            self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
                [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
                 [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
                 [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]      ##
            ]

        # Via2
        self._DesignParameter['Via2ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath1In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath2In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath2']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath3In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
        self._DesignParameter['Via2ForPath4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath4In{}'.format(_Name)))[0]
        self._DesignParameter['Via2ForPath4']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)

        self._DesignParameter['Via2ForPath1']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path1') / 2 + self.getYWidth('Via2ForPath1', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath2']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path2') / 2 + self.getYWidth('Via2ForPath2', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath3']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path3') / 2 - self.getYWidth('Via2ForPath3', '_Met2Layer') / 2]
        ]
        self._DesignParameter['Via2ForPath4']['_XYCoordinates'] = [
            [self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][0],
             self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path4') / 2 - self.getYWidth('Via2ForPath4', '_Met2Layer') / 2]
        ]

        # Met3
        topBoundary = max(self.getXYTop('Via2ForPath3', '_Met3Layer')[0][1], self.getXYTop('Via2ForPath4', '_Met3Layer')[0][1])
        botBoundary = min(self.getXYBot('Via2ForPath1', '_Met3Layer')[0][1], self.getXYBot('Via2ForPath2', '_Met3Layer')[0][1])
        self._DesignParameter['Met3Boundary5'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('Via2ForPath1', '_Met3Layer'),
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[[self.getXY('Via2ForPath1', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
        )
        self._DesignParameter['Met3Boundary6'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _XWidth=self.getXWidth('Via2ForPath2', '_Met3Layer'),
            _YWidth=topBoundary - botBoundary,
            _XYCoordinates=[[self.getXY('Via2ForPath2', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
        )

        # Via1
        self._DesignParameter['Via1ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath1In{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
        self._DesignParameter['Via1ForPath1']['_XYCoordinates'] = self.getXY('Via2ForPath1')
        self._DesignParameter['Via1ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath3In{}'.format(_Name)))[0]
        self._DesignParameter['Via1ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
        self._DesignParameter['Via1ForPath3']['_XYCoordinates'] = self.getXY('Via2ForPath1')

        # met1
        rightBoundary = self.getXYRight('Met3Boundary6')[0][0]
        leftBoundary = CoordCalc.getXYCoords_MaxX(self.getXY('MuxHalf1', 'Inv1', 'PIN_Y'))[0][0] - self.getWidth('MuxHalf1', 'Inv1', '_OutputRouting') / 2
        self._DesignParameter['Met1Boundary7'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=rightBoundary-leftBoundary,
            _YWidth=66
        )
        self._DesignParameter['Met1Boundary8'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=self.getXWidth('Met1Boundary7'),
            _YWidth=self.getYWidth('Met1Boundary7')
        )

        yCoord = self.getXYTop('Via1ForPath1', '_Met1Layer')[0][1] - self.getYWidth('Met1Boundary7') / 2        # prev.

        # calc.  boundary = centerCoord
        topBoundary_via1Met1 = self.getXYTop('Via1ForPath1', '_Met1Layer')[0][1] - self.getYWidth('Met1Boundary7') / 2
        botBoundary_via1Met1 = self.getXYBot('Via1ForPath1', '_Met1Layer')[0][1] + self.getYWidth('Met1Boundary7') / 2
        topBoundary_invPmos = self.getXYBot('MuxHalf1', 'Inv1', '_PMOS', '_Met1Layer')[0][1] - drc._Metal1MinSpaceAtCorner - self.getYWidth('Met1Boundary7') / 2
        botBoundary_invNmos = self.getXYTop('MuxHalf1', 'Inv1', '_NMOS', '_Met1Layer')[0][1] + drc._Metal1MinSpaceAtCorner + self.getYWidth('Met1Boundary7') / 2
        topBoundary = min(topBoundary_via1Met1, topBoundary_invPmos)
        botBoundary = max(botBoundary_via1Met1, botBoundary_invNmos)
        if topBoundary < botBoundary:
            raise NotImplementedError
        else:
            yCoord = (topBoundary + botBoundary) / 2

        self._DesignParameter['Met1Boundary7']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, yCoord]
        ]
        self._DesignParameter['Met1Boundary8']['_XYCoordinates'] = [
            [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 - self.getXY('Met1Boundary7')[0][1]]
        ]

        ''' Met3 '''
        self._DesignParameter['Met3boundary09'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=66
        )
        self._DesignParameter['Met3boundary10'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )
        self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[0],
             self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[0]]
        ]
        self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[1],
             self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[1]]
        ]

        self._DesignParameter['Met3boundary11'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )
        self._DesignParameter['Met3boundary12'] = self._PathElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
            _Width=self.getWidth('Met3boundary09')
        )

        self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[0],
             self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[0]]
        ]
        self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
            [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[1],
             self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[1]]
        ]


    # def _CalculateDesignParamter(self,
    #                              TristateInv1_Finger=1,
    #                              Inv_Finger=1,
    #                              TristateInv2_Finger=2,
    #
    #                              TristateInv1_PMOSWidth=500,
    #                              TristateInv1_NMOSWidth=250,
    #                              TristateInv1_VDD2PMOS=None,
    #                              TristateInv1_VSS2NMOS=None,
    #
    #                              TristateInv2_PMOSWidth=400,
    #                              TristateInv2_NMOSWidth=200,
    #                              TristateInv2_VDD2PMOS=None,
    #                              TristateInv2_VSS2NMOS=None,
    #
    #                              TristateInv3_NumFinger_NM1=3,
    #                              TristateInv3_NumFinger_NM2=3,
    #                              TristateInv3_Width_NM1=250,
    #                              TristateInv3_Width_NM2=250,
    #                              TristateInv3_Width_PM1=500,
    #                              TristateInv3_Width_PM2=500,
    #                              TristateInv3_YCoord_InputA=750,
    #
    #                              Inv_NMOSWidth=200,
    #                              Inv_PMOSWidth=400,
    #
    #                              ChannelLength=30,
    #                              GateSpacing=100,
    #                              XVT='SLVT',
    #                              CellHeight=1800,
    #                              SupplyRailType=1,
    #
    #                              ):
    #
    #     drc = DRC.DRC()
    #     _Name = self._DesignParameter['_Name']['_Name']
    #
    #     UnitPitch = ChannelLength + GateSpacing
    #
    #
    #     Parameters = dict(TristateInv1_Finger=TristateInv1_Finger,
    #                       Inv_Finger=Inv_Finger,
    #                       TristateInv2_Finger=TristateInv2_Finger,
    #
    #                       TristateInv1_PMOSWidth=TristateInv1_PMOSWidth,
    #                       TristateInv1_NMOSWidth=TristateInv1_NMOSWidth,
    #                       TristateInv1_VDD2PMOS=TristateInv1_VDD2PMOS,
    #                       TristateInv1_VSS2NMOS=TristateInv1_VSS2NMOS,
    #
    #                       TristateInv2_PMOSWidth=TristateInv2_PMOSWidth,
    #                       TristateInv2_NMOSWidth=TristateInv2_NMOSWidth,
    #                       TristateInv2_VDD2PMOS=TristateInv2_VDD2PMOS,
    #                       TristateInv2_VSS2NMOS=TristateInv2_VSS2NMOS,
    #
    #                       TristateInv3_NumFinger_NM1=TristateInv3_NumFinger_NM1,
    #                       TristateInv3_NumFinger_NM2=TristateInv3_NumFinger_NM2,
    #                       TristateInv3_Width_NM1=TristateInv3_Width_NM1,
    #                       TristateInv3_Width_NM2=TristateInv3_Width_NM2,
    #                       TristateInv3_Width_PM1=TristateInv3_Width_PM1,
    #                       TristateInv3_Width_PM2=TristateInv3_Width_PM2,
    #                       TristateInv3_YCoord_InputA=TristateInv3_YCoord_InputA,
    #
    #                       Inv_NMOSWidth=Inv_NMOSWidth,
    #                       Inv_PMOSWidth=Inv_PMOSWidth,
    #
    #                       ChannelLength=ChannelLength,
    #                       GateSpacing=GateSpacing,
    #                       XVT=XVT,
    #                       CellHeight=CellHeight,
    #                       SupplyRailType=SupplyRailType,)
    #
    #     self._DesignParameter['MuxHalf1'] = self._SrefElementDeclaration(
    #         _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf1In{}'.format(_Name)))[0]
    #     self._DesignParameter['MuxHalf1']['_DesignObj']._CalculateDesignParamter(**Parameters)
    #     self._DesignParameter['MuxHalf1']['_XYCoordinates'] = [[0,0]]
    #
    #     self._DesignParameter['MuxHalf2'] = self._SrefElementDeclaration(
    #         _Reflect=[1, 0, 0], _Angle=0,
    #         _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf2In{}'.format(_Name)))[0]
    #     self._DesignParameter['MuxHalf2']['_DesignObj']._CalculateDesignParamter(**Parameters)
    #     self._DesignParameter['MuxHalf2']['_XYCoordinates'] = [[0, 2*CellHeight]]
    #
    #     ''' Between Inverter1 and TristateInverter2 '''
    #     # Path
    #     self._DesignParameter['Met2Path1'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path2'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path3'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met2Path4'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL2'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL2'][1],
    #         _Width=66
    #     )
    #     if TristateInv2_Finger == 1:
    #
    #         YCoordOftempRoute1 = 1033
    #         YCoordOftempRoute2 = 2567
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #
    #     elif TristateInv2_Finger == 2:
    #         YCoordOftempRoute1 = 1033
    #         YCoordOftempRoute2 = 2567
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NMOS', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #     else:
    #         YCoordOftempRoute1 = 1066
    #         YCoordOftempRoute2 = 2534
    #         self._DesignParameter['Met2Path1']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV2_A')[0][0], self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, self.getXYBot('MuxHalf1', 'Via1_TSINV2_A', '_Met2Layer')[0][1] + self.getWidth('Met2Path1') / 2]]
    #         ]
    #         self._DesignParameter['Met2Path2']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf1', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute1],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, YCoordOftempRoute1]]
    #         ]
    #         self._DesignParameter['Met2Path3']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV2_A')[0][0], self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 1 * UnitPitch, self.getXYTop('MuxHalf2', 'Via1_TSINV2_A', '_Met2Layer')[0][1] - self.getWidth('Met2Path3') / 2]],
    #         ]
    #         self._DesignParameter['Met2Path4']['_XYCoordinates'] = [
    #             [[self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][1]],
    #              [self.getXY('MuxHalf2', 'Via1_TSINV3_A')[0][0], YCoordOftempRoute2],
    #              [self.getXY('MuxHalf1', 'TristateInv2', 'NM2', '_Met1Layer')[-1][0] - 2 * UnitPitch, YCoordOftempRoute2]]
    #         ]
    #
    #     # Via2
    #     self._DesignParameter['Via2ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath1In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath2'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath2In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath2']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath3In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #     self._DesignParameter['Via2ForPath4'] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name='Via2ForPath4In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via2ForPath4']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet22Met3NumberOfCOX=1, _ViaMet22Met3NumberOfCOY=2)
    #
    #     self._DesignParameter['Via2ForPath1']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path1']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path1') / 2 + self.getYWidth('Via2ForPath1', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath2']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path2']['_XYCoordinates'][0][-1][1] - self.getWidth('Met2Path2') / 2 + self.getYWidth('Via2ForPath2', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath3']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path3']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path3') / 2 - self.getYWidth('Via2ForPath3', '_Met2Layer') / 2]
    #     ]
    #     self._DesignParameter['Via2ForPath4']['_XYCoordinates'] = [
    #         [self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][0],
    #          self._DesignParameter['Met2Path4']['_XYCoordinates'][0][-1][1] + self.getWidth('Met2Path4') / 2 - self.getYWidth('Via2ForPath4', '_Met2Layer') / 2]
    #     ]
    #
    #     # Met3
    #     topBoundary = max(self.getXYTop('Via2ForPath3', '_Met3Layer')[0][1], self.getXYTop('Via2ForPath4', '_Met3Layer')[0][1])
    #     botBoundary = min(self.getXYBot('Via2ForPath1', '_Met3Layer')[0][1], self.getXYBot('Via2ForPath2', '_Met3Layer')[0][1])
    #     self._DesignParameter['Met3Boundary5'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _XWidth=self.getXWidth('Via2ForPath1', '_Met3Layer'),
    #         _YWidth=topBoundary-botBoundary,
    #         _XYCoordinates=[[self.getXY('Via2ForPath1', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
    #     )
    #     self._DesignParameter['Met3Boundary6'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _XWidth=self.getXWidth('Via2ForPath2', '_Met3Layer'),
    #         _YWidth=topBoundary - botBoundary,
    #         _XYCoordinates=[[self.getXY('Via2ForPath2', '_Met3Layer')[0][0], (topBoundary + botBoundary) / 2]]
    #     )
    #
    #     # Via1
    #     self._DesignParameter['Via1ForPath1'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath1In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via1ForPath1']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
    #     self._DesignParameter['Via1ForPath1']['_XYCoordinates'] = self.getXY('Via2ForPath1')
    #     self._DesignParameter['Via1ForPath3'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='Via1ForPath3In{}'.format(_Name)))[0]
    #     self._DesignParameter['Via1ForPath3']['_DesignObj']._CalculateDesignParameterSameEnclosure(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2)
    #     self._DesignParameter['Via1ForPath3']['_XYCoordinates'] = self.getXY('Via2ForPath1')
    #
    #     # met1
    #     rightBoundary = self.getXYRight('Met3Boundary6')[0][0]
    #     leftBoundary = CoordCalc.getXYCoords_MaxX(self.getXY('MuxHalf1', 'Inv1', 'PIN_Y'))[0][0] - self.getWidth('MuxHalf1', 'Inv1', '_OutputRouting') / 2
    #     self._DesignParameter['Met1Boundary7'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL1'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    #         _XWidth=rightBoundary-leftBoundary,
    #         _YWidth=66
    #     )
    #     self._DesignParameter['Met1Boundary8'] = self._BoundaryElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL1'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL1'][1],
    #         _XWidth=self.getXWidth('Met1Boundary7'),
    #         _YWidth=self.getYWidth('Met1Boundary7')
    #     )
    #     self._DesignParameter['Met1Boundary7']['_XYCoordinates'] = [
    #         [(rightBoundary + leftBoundary) / 2, self.getXYTop('Via1ForPath1', '_Met1Layer')[0][1] - self.getYWidth('Met1Boundary7') / 2]
    #     ]
    #     self._DesignParameter['Met1Boundary8']['_XYCoordinates'] = [
    #         [(rightBoundary + leftBoundary) / 2, CellHeight * 2 - self.getXY('Met1Boundary7')[0][1]]
    #     ]
    #
    #     ''' Met3 '''
    #     self._DesignParameter['Met3boundary09'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=66
    #     )
    #     self._DesignParameter['Met3boundary10'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #     self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[0],
    #          self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[0]]
    #     ]
    #     self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp00', '_Met3Layer')[1],
    #          self.getXYTop('MuxHalf2', 'Via2_temp00', '_Met3Layer')[1]]
    #     ]
    #
    #     self._DesignParameter['Met3boundary11'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #     self._DesignParameter['Met3boundary12'] = self._PathElementDeclaration(
    #         _Layer=DesignParameters._LayerMapping['METAL3'][0],
    #         _Datatype=DesignParameters._LayerMapping['METAL3'][1],
    #         _Width=self.getWidth('Met3boundary09')
    #     )
    #
    #     self._DesignParameter['Met3boundary09']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[0],
    #          self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[0]]
    #     ]
    #     self._DesignParameter['Met3boundary10']['_XYCoordinates'] = [
    #         [self.getXYBot('MuxHalf1', 'Via2_temp05', '_Met3Layer')[1],
    #          self.getXYTop('MuxHalf2', 'Via2_temp05', '_Met3Layer')[1]]
    #     ]


