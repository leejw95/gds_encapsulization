from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
import time
from generatorLib import DRC
from generatorLib import CoordinateCalc as CoordCalc
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import ViaMet22Met3
from generatorLib.generator_models import MUX_PI_4to2
from generatorLib.generator_models import MUX_PI_4to2_half
from generatorLib.generator_models import Inverter
from generatorLib.generator_models import SupplyRails


class PI_clk_sel_8p_s(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='PI_clk_sel_8p_s'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_v2(self,
                                     TristateInv1_Finger=1,
                                     TristateInv1_PMOSWidth=500,
                                     TristateInv1_NMOSWidth=250,
                                     TristateInv1_VDD2PMOS=None,            # Option (Not work when finger >= 3)
                                     TristateInv1_VSS2NMOS=None,            # Option (Not work when finger >= 3)
                                     TristateInv1_YCoordOfInputA=None,      # Option
                                     TristateInv1_YCoordOfInputEN=None,     # Option
                                     TristateInv1_YCoordOfInputENb=None,    # Option

                                     TristateInv2_Finger=2,
                                     TristateInv2_PMOSWidth=400,
                                     TristateInv2_NMOSWidth=200,
                                     TristateInv2_VDD2PMOS=None,            # Option (Not work when finger >= 3)
                                     TristateInv2_VSS2NMOS=None,            # Option (Not work when finger >= 3)
                                     TristateInv2_YCoordOfInputA=None,      # Option
                                     TristateInv2_YCoordOfInputEN=None,     # Option
                                     TristateInv2_YCoordOfInputENb=None,    # Option

                                     Inv_Finger=1,
                                     Inv_PMOSWidth=400,
                                     Inv_NMOSWidth=200,
                                     Inv_VDD2PMOS=None,                     # Option
                                     Inv_VSS2NMOS=None,                     # Option
                                     Inv_YCoordOfInOut=None,                # Option

                                     Inv2_Finger=1,
                                     Inv2_PMOSWidth=400,
                                     Inv2_NMOSWidth=200,
                                     Inv2_VDD2PMOS=None,                    # Option
                                     Inv2_VSS2NMOS=None,                    # Option
                                     Inv2_YCoordOfInOut=None,               # Option

                                     ChannelLength=30,
                                     GateSpacing=100,
                                     XVT='SLVT',
                                     CellHeight=1800,   # option
                                     SupplyRailType=2
                                     ):

        """
        top

        """

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        unitPitch = ChannelLength + GateSpacing

        # Minimum CellHeight Calculation
        ParametersForMinHeightCalc_MUX4to2 = dict(
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
        minCellHeight_MUX4to2Half = self._DesignParameter['MuxHalf_CalcMinHeight']['_DesignObj']._CalculateMinHeight(**ParametersForMinHeightCalc_MUX4to2)

        ParametersForMinHeightCalc_Inv2 = dict(
            _Finger=Inv2_Finger,
            _ChannelWidth=Inv2_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv2_PMOSWidth / Inv2_NMOSWidth,
            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            # _SDWidth=SDWidth,
            _SupplyRailType=SupplyRailType
        )
        self._DesignParameter['INV2_CalcMinHeight'] = self._SrefElementDeclaration(_DesignObj=Inverter._Inverter(_Name='INV2_CalcMinHeightIn{}'.format(_Name)))[0]
        minCellHeight_INV = self._DesignParameter['INV2_CalcMinHeight']['_DesignObj']._CalcMinHeight(**ParametersForMinHeightCalc_Inv2)
        minCellHeight = max(minCellHeight_MUX4to2Half, minCellHeight_INV)

        #
        ParametersForMinHeightCalc2_MUX4to2 = ParametersForMinHeightCalc_MUX4to2
        ParametersForMinHeightCalc2_MUX4to2['CellHeight'] = minCellHeight
        self._DesignParameter['MuxHalf_CalcMinHeight2'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2_half.MUX_PI_4to2_half(_Name='MuxHalf_CalcMinHeight2In{}'.format(_Name)))[0]
        self._DesignParameter['MuxHalf_CalcMinHeight2']['_DesignObj']._CalculateDesignParamter_v2(**ParametersForMinHeightCalc2_MUX4to2)

        self._DesignParameter['MuxHalf_CalcMinHeight2']['_XYCoordinates'] = [[0, 0]]     # tmp
        self._DesignParameter['INV2_CalcMinHeight']['_XYCoordinates'] = [[0, 0]]        # tmp
        pplayerYWidthMux = minCellHeight_MUX4to2Half - self.getXYBot('MuxHalf_CalcMinHeight2', '_PPLayerForPMOS')[0][1]
        pplayerYWidthInv2 = minCellHeight_INV - self.getXYBot('INV2_CalcMinHeight', '_PMOS', '_PPLayer')[0][1]
        ppLayerYWidthMax = max(pplayerYWidthMux, pplayerYWidthInv2)
        topBoundaryOD_max = minCellHeight - ppLayerYWidthMax - drc._OdMinSpace2Pp

        tmpStr1 = 'NMOS' if TristateInv1_Finger in (1,2) else 'NM1'
        tmpStr2 = 'NMOS' if TristateInv2_Finger in (1,2) else 'NM1'

        topBoundaryOD_MuxTSINV1 = self.getXYTop('MuxHalf_CalcMinHeight2', 'TristateInv0', tmpStr1, '_ODLayer')[0][1]
        topBoundaryOD_MuxTSINV2 = self.getXYTop('MuxHalf_CalcMinHeight2', 'TristateInv2', tmpStr2, '_ODLayer')[0][1]
        topBoundaryOD_MuxINV = self.getXYTop('MuxHalf_CalcMinHeight2', 'Inv0', '_NMOS', '_ODLayer')[0][1]
        topBoundaryOD_Mux = max(topBoundaryOD_MuxTSINV1, topBoundaryOD_MuxTSINV2, topBoundaryOD_MuxINV)
        topBoundaryOD_INV2 = self.getXYTop('INV2_CalcMinHeight', '_NMOS', '_ODLayer')[0][1]
        topBoundaryOD_forMinCalc = max(topBoundaryOD_Mux, topBoundaryOD_INV2)

        if topBoundaryOD_forMinCalc > topBoundaryOD_max:
            minCellHeight = minCellHeight + (topBoundaryOD_forMinCalc - topBoundaryOD_max)


        del self._DesignParameter['MuxHalf_CalcMinHeight']
        del self._DesignParameter['MuxHalf_CalcMinHeight2']
        del self._DesignParameter['INV2_CalcMinHeight']

        if CellHeight == None:
            _CellHeight = minCellHeight
        elif CellHeight < minCellHeight:
            raise NotImplementedError(f"Input CellHeight={CellHeight}, but minimum value is {minCellHeight}")
        else:
            _CellHeight = CellHeight


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
                          CellHeight=_CellHeight,
                          SupplyRailType=SupplyRailType,)

        self._DesignParameter['Mux1'] = self._SrefElementDeclaration(
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux1In{}'.format(_Name)))[0]
        self._DesignParameter['Mux1']['_DesignObj']._CalculateDesignParameter_v2(**Parameters)
        self._DesignParameter['Mux1']['_XYCoordinates'] = [[0,0]]

        self._DesignParameter['Mux2'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0,
            _DesignObj=MUX_PI_4to2.MUX_PI_4to2(_Name='Mux2In{}'.format(_Name)))[0]
        self._DesignParameter['Mux2']['_DesignObj']._CalculateDesignParameter_v2(**Parameters)
        self._DesignParameter['Mux2']['_XYCoordinates'] = [[0, 4*_CellHeight]]

        Parameters_Inv = dict(
            _Finger=Inv2_Finger,
            _ChannelWidth=Inv2_NMOSWidth,
            _ChannelLength=ChannelLength,
            _NPRatio=Inv2_PMOSWidth/Inv2_NMOSWidth,

            _VDD2VSSHeight=_CellHeight,
            _VDD2PMOSHeight=Inv2_VDD2PMOS,
            _VSS2NMOSHeight=Inv2_VSS2NMOS,
            _YCoordOfInput=Inv2_YCoordOfInOut,

            _Dummy=True,
            _XVT=XVT,
            _GateSpacing=GateSpacing,
            _SDWidth=66,
            _SupplyRailType=SupplyRailType,
        )


        self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
        self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
        self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv2'] = self._SrefElementDeclaration(
            _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv2In{}'.format(_Name)))[0]
        self._DesignParameter['Inv2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
        self._DesignParameter['Inv3'] = self._SrefElementDeclaration(
            _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv3In{}'.format(_Name)))[0]
        self._DesignParameter['Inv3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)

        XCoord_Inv = self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + self._DesignParameter['Inv2']['_DesignObj'].CellXWidth / 2

        self._DesignParameter['Inv0']['_XYCoordinates'] = [[XCoord_Inv, 0]]
        self._DesignParameter['Inv1']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
        self._DesignParameter['Inv2']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
        self._DesignParameter['Inv3']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 4]]

        # PODummy - INVerter InputVia0
        if Parameters_Inv['_Finger'] in (1, 2):
            tmpStrPMOS = 'PMOS' if Parameters['TristateInv2_Finger'] in (1, 2) else 'PM2'  # check
            tmpStrNMOS = 'NMOS' if Parameters['TristateInv2_Finger'] in (1, 2) else 'NM2'
            xDistance = self.getXYLeft('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][0] - CoordCalc.getXYCoords_MaxX(self.getXYRight('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer'))[0][0]
            yDistancePMOS = self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer')[0][1] - self.getXYTop('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][1]
            yDistanceNMOS = self.getXYBot('Inv0', '_VIAPoly2Met1_F1', '_POLayer')[0][1] - self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrNMOS, '_PODummyLayer')[0][1]
            if xDistance ** 2 + min(abs(yDistancePMOS), abs(yDistanceNMOS)) ** 2 < drc._PolygateMinSpace ** 2 or yDistancePMOS < 0 or yDistanceNMOS < 0:
                yDistance_min_byDRC = self.CeilMinSnapSpacing(math.sqrt(drc._PolygateMinSpace ** 2 - xDistance ** 2), drc._MinSnapSpacing)
                yMax = min(self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrPMOS, '_PODummyLayer')[0][1], self.getXYBot('Inv0', '_PMOS', '_PODummyLayer')[0][1]) - yDistance_min_byDRC
                yMin = max(self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3', tmpStrNMOS, '_PODummyLayer')[0][1], self.getXYTop('Inv0', '_NMOS', '_PODummyLayer')[0][1]) + yDistance_min_byDRC
                if yMax - yMin < self.getYWidth('Inv0', '_VIAPoly2Met1_F1', '_POLayer'):
                    raise NotImplementedError
                else:
                    # re calculate Inverter
                    del self._DesignParameter['Inv0']
                    del self._DesignParameter['Inv1']
                    del self._DesignParameter['Inv2']
                    del self._DesignParameter['Inv3']
                    Parameters_Inv['_YCoordOfInput'] = (yMax + yMin) / 2
                    self._DesignParameter['Inv0'] = self._SrefElementDeclaration(
                        _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv0In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv0']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv1'] = self._SrefElementDeclaration(
                        _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv1In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv1']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv2'] = self._SrefElementDeclaration(
                        _Reflect=[0, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv2In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv2']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)
                    self._DesignParameter['Inv3'] = self._SrefElementDeclaration(
                        _Reflect=[1, 0, 0], _Angle=0, _DesignObj=Inverter._Inverter(_Name='Inv3In{}'.format(_Name)))[0]
                    self._DesignParameter['Inv3']['_DesignObj']._CalculateDesignParameter_v3(**Parameters_Inv)

                    XCoord_Inv = self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + self._DesignParameter['Inv2']['_DesignObj'].CellXWidth / 2
                    self._DesignParameter['Inv0']['_XYCoordinates'] = [[XCoord_Inv, 0]]
                    self._DesignParameter['Inv1']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
                    self._DesignParameter['Inv2']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 2]]
                    self._DesignParameter['Inv3']['_XYCoordinates'] = [[XCoord_Inv, _CellHeight * 4]]
            else:
                pass  # No DRC Error
        else:
            pass







        ''' --- TristateInverter3 - LastInverter '''
        if TristateInv2_Finger == 1:
            # shift right inv0123
            xCoord_inv_recalc = self.getXY('Inv0')[0][0] + unitPitch
            self._DesignParameter['Inv0']['_XYCoordinates'][0][0] = xCoord_inv_recalc
            self._DesignParameter['Inv1']['_XYCoordinates'][0][0] = xCoord_inv_recalc
            self._DesignParameter['Inv2']['_XYCoordinates'][0][0] = xCoord_inv_recalc
            self._DesignParameter['Inv3']['_XYCoordinates'][0][0] = xCoord_inv_recalc

            #
            self._DesignParameter['Met1Path01'] = self._PathElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _Width=66,)
            xy1 = [self.getXY('Inv0', 'InputMet1')[0][0], self.getXY('Inv0', 'InputMet1')[0][1]]
            xy2 = [self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + unitPitch / 2, self.getXY('Inv0', 'InputMet1')[0][1]]

            d1 = abs((self.getXY('Inv0', 'InputMet1')[0][1] + self.getWidth('Met1Path01') / 2) - self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3','InputVia_A', '_Met1Layer')[0][1])
            d2 = abs((self.getXY('Inv0', 'InputMet1')[0][1] + self.getWidth('Met1Path01') / 2) - self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3','InputVia_A', '_Met1Layer')[0][1])
            d3 = abs((self.getXY('Inv0', 'InputMet1')[0][1] - self.getWidth('Met1Path01') / 2) - self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3','InputVia_A', '_Met1Layer')[0][1])
            d4 = abs((self.getXY('Inv0', 'InputMet1')[0][1] - self.getWidth('Met1Path01') / 2) - self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3','InputVia_A', '_Met1Layer')[0][1])
            if min(d1, d2, d3, d4) > drc._Metal1MinSpaceAtCorner:
                XYList = [[xy1, xy2]]
            else:
                topBoundary1 = self.getXYBot('Mux1', 'MuxHalf1', 'TristateInv3','InputVia_A', '_Met1Layer')[0][1] - drc._Metal1MinSpaceAtCorner - self.getWidth('Met1Path01') / 2
                topBoundary2 = self.getXY('Inv0', 'InputMet1')[0][1] - drc._Metal1MinSpaceAtCorner
                topBoundary = min(topBoundary1, topBoundary2)
                botBoundary = self.getXYTop('Mux1', 'MuxHalf1', 'TristateInv3','NMOS', '_Met1Layer')[0][1] + drc._Metal1MinSpaceAtCorner + self.getWidth('Met1Path01') / 2
                if topBoundary < botBoundary:
                    raise NotImplementedError
                xy3 = [self.getXYRight('Mux1', 'MuxHalf1', 'VDDRail')[0][0] + unitPitch / 2, topBoundary]
                xy4 = [self.getXY('Mux1', 'MuxHalf1', 'TristateInv3')[0][0], topBoundary]
                XYList = [[xy1, xy2, xy3, xy4]]
            self._DesignParameter['Met1Path01']['_XYCoordinates'] = XYList


            #
            self._DesignParameter['VSSRail1'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VSSRail1In{}'.format(_Name)))[0]
            self._DesignParameter['VDDRail1'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='VDDRail1In{}'.format(_Name)))[0]
            self._DesignParameter['VSSRail1']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=1, UnitPitch=(GateSpacing + ChannelLength),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True, deleteViaAndMet1=True))
            self._DesignParameter['VDDRail1']['_DesignObj']._CalculateDesignParameter(
                **dict(NumPitch=1, UnitPitch=(ChannelLength + GateSpacing),
                       Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False, deleteViaAndMet1=True))
            rightBoundary = self.getXYLeft('Inv0', 'PbodyContact', '_ODLayer')[0][0]
            leftBoundary = self.getXYRight('Mux1', 'MuxHalf1', 'TristateInv3', 'VSSRail', '_ODLayer')[0][0]
            self._DesignParameter['VSSRail1']['_XYCoordinates'] = [
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 0],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 2],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 4]
            ]
            self._DesignParameter['VDDRail1']['_XYCoordinates'] = [
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 3]
            ]


            self._DesignParameter['XVTLayer'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping[XVT][0],
                _Datatype=DesignParameters._LayerMapping[XVT][1],
                _XWidth=rightBoundary - leftBoundary,
                _YWidth=_CellHeight * 4,
                _XYCoordinates=[
                    [(rightBoundary + leftBoundary) / 2, _CellHeight * 2]
                ]
            )

            pass
        elif TristateInv2_Finger == 2:
            rightBoundary = self.getXYRight('Inv0', 'InputMet1')[0][0]
            leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', 'TristateInv3', 'met1_output_5')[0][0]
            self._DesignParameter['Met1Boundary01'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=rightBoundary - leftBoundary,
                _YWidth=66,
                _XYCoordinates=[
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv0', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv1', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv2', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv3', 'InputMet1')[0][1]],
                ]
            )
        else:
            rightBoundary = self.getXYRight('Inv0', 'InputMet1')[0][0]
            leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', 'TristateInv3', 'Met1RouteY_Out')[0][0]
            self._DesignParameter['Met1Boundary01'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                _XWidth=rightBoundary-leftBoundary,
                _YWidth=66,
                _XYCoordinates=[
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv0', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv1', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv2', 'InputMet1')[0][1]],
                    [(rightBoundary + leftBoundary) / 2, self.getXY('Inv3', 'InputMet1')[0][1]],
                ]
            )

        # NW
        rightBoundary = self.getXYRight('Inv0', '_NWLayerBoundary')[0][0]
        leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', '_NWLayer')[0][0]

        botBoundary1 = self.getXYBot('Inv0', '_NWLayerBoundary')[0][1]
        botBoundary2 = self.getXYBot('Mux1', 'MuxHalf1', '_NWLayer')[0][1]
        YWidth = 2*(_CellHeight - min(botBoundary1, botBoundary2))

        self._DesignParameter['_NWLayer'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['NWELL'][0],
            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=YWidth,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 3]
            ]
        )

        # BP
        rightBoundary = self.getXYRight('Inv0', '_PMOS', '_PPLayer')[0][0]
        leftBoundary = self.getXYLeft('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][0]

        topBoundary1 = self.getXYTop('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][1]
        botBoundary1 = self.getXYBot('Mux1', 'MuxHalf1', '_PPLayerForPMOS')[0][1]
        topBoundary2 = self.getXYTop('Inv0', '_PMOS', '_PPLayer')[0][1]
        botBoundary2 = self.getXYBot('Inv0', '_PMOS', '_PPLayer')[0][1]
        topBoundary = max(topBoundary1, topBoundary2)
        botBoundary = min(botBoundary1, botBoundary2)
        YCoord_PPLayer1 = (topBoundary + botBoundary) / 2

        self._DesignParameter['_PPLayerForPMOS'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['PIMP'][0],
            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
            _XWidth=rightBoundary - leftBoundary,
            _YWidth=topBoundary-botBoundary,
            _XYCoordinates=[
                [(rightBoundary + leftBoundary) / 2, YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 - YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 2 + YCoord_PPLayer1],
                [(rightBoundary + leftBoundary) / 2, _CellHeight * 4 - YCoord_PPLayer1],

            ]
        )

        # pin
        xy1 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf1')[0], self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met3Route_temp01']['_XYCoordinates'][0][0])
        xy2 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf1')[0], self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met3Route_temp01']['_XYCoordinates'][1][0])
        self._DesignParameter['PIN_clk_selnb0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selnb<0>',
            _XYCoordinates=[xy1]
        )
        self._DesignParameter['PIN_clk_seln0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_seln<0>',
            _XYCoordinates=[xy2]
        )
        self._DesignParameter['PIN_clk_selnb1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selnb<1>',
            _XYCoordinates=[self.getXY('Mux1', 'MuxHalf1', 'Via2_temp05')[0]]
        )
        self._DesignParameter['PIN_clk_seln1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_seln<1>',
            _XYCoordinates=[self.getXY('Mux1', 'MuxHalf1', 'Via2_temp05')[1]]
        )

        #
        # ['qwerqwer[0]', 'Mux2[0]', 'MuxHalf1[0]', 'Met3Route_temp01[0][0]']
        # ['qwer[0]', 'Mux2[0]', 'MuxHalf1[0]', 'Via2_temp00[0]']
        # ['qwerqwer[0]', 'Mux2[0]', 'MuxHalf1[0]', 'Via2_temp05[0]']
        # ['qwerqwer[0]', 'Mux2[0]', 'MuxHalf1[0]', 'Met3Route_temp06[0][0]']
        xy1 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf1')[0], self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met3Route_temp01']['_XYCoordinates'][0][0])
        xy2 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf1')[0], self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met3Route_temp01']['_XYCoordinates'][1][0])
        self._DesignParameter['PIN_clk_selpb0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selpb<0>',
            _XYCoordinates=[self.getXY('Mux2', 'MuxHalf1', 'Via2_temp00')[0]]
        )
        self._DesignParameter['PIN_clk_selp0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selp<0>',
            _XYCoordinates=[self.getXY('Mux2', 'MuxHalf1', 'Via2_temp00')[1]]
        )
        self._DesignParameter['PIN_clk_selpb1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selpb<1>',
            _XYCoordinates=[self.getXY('Mux2', 'MuxHalf1', 'Via2_temp05')[0]]
        )
        self._DesignParameter['PIN_clk_selp1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL3PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL3PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_selp<1>',
            _XYCoordinates=[self.getXY('Mux2', 'MuxHalf1', 'Via2_temp05')[1]]
        )

        #
        self._DesignParameter['PIN_clkn'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clkn',
            _XYCoordinates=[self.getXY('Mux1', 'MuxHalf2', 'Inv0', 'PIN_Y')[0]]
        )
        self._DesignParameter['PIN_clkp'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clkp',
            _XYCoordinates=[self.getXY('Mux2', 'MuxHalf2', 'Inv0', 'PIN_Y')[0]]
        )
        # out
        self._DesignParameter['PIN_clkb_odd'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clkb_odd',
            _XYCoordinates=[self.getXY('Inv0', 'PIN_Y')[0]]
        )
        self._DesignParameter['PIN_clk_odd'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_odd',
            _XYCoordinates=[self.getXY('Inv1', 'PIN_Y')[0]]
        )
        self._DesignParameter['PIN_clk_even'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_even',
            _XYCoordinates=[self.getXY('Inv2', 'PIN_Y')[0]]
        )
        self._DesignParameter['PIN_clkb_even'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clkb_even',
            _XYCoordinates=[self.getXY('Inv3', 'PIN_Y')[0]]
        )
        # 5 7 3 1 0 2 6 4
        #['qwer[0]', 'Mux1[0]', 'MuxHalf1[0]', 'Met2Route_temp8[0][0]']
        # ['qwer[0]', 'Mux1[0]', 'MuxHalf2[0]', 'Met2Route_temp8[0][0]']
        # ['qwer[0]', 'Mux2[0]', 'MuxHalf2[0]', 'Met2Route_temp8[0][0]']
        # ['qwer[0]', 'Mux2[0]', 'MuxHalf1[0]', 'Met2Route_temp8[0][0]']
        xy1 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf1')[0],  self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1])
        xy2 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf1')[0],  self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1])
        xy3 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf2')[0],  [self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][0], -self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][1]])
        xy4 = CoordCalc.Add(self.getXY('Mux1', 'MuxHalf2')[0],  [self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][0], -self._DesignParameter['Mux1']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][1]])

        self._DesignParameter['PIN_clk_in5'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<5>',
            _XYCoordinates=[xy1]
        )
        self._DesignParameter['PIN_clk_in7'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<7>',
            _XYCoordinates=[xy2]
        )
        self._DesignParameter['PIN_clk_in3'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<3>',
            _XYCoordinates=[xy3]
        )
        self._DesignParameter['PIN_clk_in1'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<1>',
            _XYCoordinates=[xy4]
        )

        xy8 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf1')[0],
                            [self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][0],
                             -self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][1]])
        xy7 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf1')[0],
                            [self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][0],
                             -self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf1']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][1]])
        xy6 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf2')[0], [
            self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][0], +
            self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][1][-1][1]])
        xy5 = CoordCalc.Add(self.getXY('Mux2', 'MuxHalf2')[0], [
            self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][0], +
            self._DesignParameter['Mux2']['_DesignObj']._DesignParameter['MuxHalf2']['_DesignObj']._DesignParameter['Met2Route_temp8']['_XYCoordinates'][0][-1][1]])

        self._DesignParameter['PIN_clk_in0'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<0>',
            _XYCoordinates=[xy5]
        )
        self._DesignParameter['PIN_clk_in2'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<2>',
            _XYCoordinates=[xy6]
        )
        self._DesignParameter['PIN_clk_in6'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<6>',
            _XYCoordinates=[xy7]
        )
        self._DesignParameter['PIN_clk_in4'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='clk_in<4>',
            _XYCoordinates=[xy8]
        )
        #
        self._DesignParameter['PIN_VSS'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='VSS',
            _XYCoordinates=[[0, 0], [0, 2 * _CellHeight], [0, 4 * _CellHeight]]
        )
        self._DesignParameter['PIN_VDD'] = self._TextElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL2PIN'][0],
            _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1],
            _Presentation=[0, 1, 1], _Reflect=[0, 0, 0], _Mag=0.01, _Angle=0, _TEXT='VDD',
            _XYCoordinates=[[0, _CellHeight], [0, 3 * _CellHeight]]
        )

        ''' -------------------------------------------------------------------------------------------------------- '''
        print(''.center(105, '#'))
        print('     {} Calculation End     '.format(_Name).center(105, '#'))
        print(''.center(105, '#'))


