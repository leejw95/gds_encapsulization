from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A00_NmosWithDummy_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A01_PmosWithDummy_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A02_NbodyContact_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A03_PbodyContact_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A04_NbodyContactPhyLen_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A05_PbodyContactPhyLen_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A06_NbodyRing_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A07_PbodyRing_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A08_PolyRes_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A09_Ncap_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A10_ViaM0toM1_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A11_ViaM1toM2_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A12_ViaM2toM3_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A13_ViaM3toM4_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A14_ViaM4toM5_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A15_ViaM5toM6_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A16_ViaM6toM7_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A17_ViaM7toM8_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A18_ViaStack_KJH

## ########################################################################################################################################################## Class_HEADER
class _PmosWithDummy_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

#PMOS
_PMOSNumberofGate	= None,
_PMOSChannelWidth	= None,
_PMOSChannellength	= None,
_GateSpacing		= None,
_SDWidth			= None,
_XVT				= None,
_PCCrit				= None,

#Source_node_ViaM1M2
_Source_Via_TF = None,

#Drain_node_ViaM1M2
_Drain_Via_TF = None,

#POLY dummy setting
_PMOSDummy = None, #TF
    #if _PMOSDummy == True
_PMOSDummy_length = None, #None/Value
_PMOSDummy_placement = None, #None/Up/Dn/

                                        )

    ## Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                        )

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

#PMOS
_PMOSNumberofGate	= None,
_PMOSChannelWidth	= None,
_PMOSChannellength	= None,
_GateSpacing		= None,
_SDWidth			= None,
_XVT				= None,
_PCCrit				= None,

#Source_node_ViaM1M2
_Source_Via_TF = None,

#Drain_node_ViaM1M2
_Drain_Via_TF = None,

#POLY dummy setting
_PMOSDummy = None, #TF
    #if _PMOSDummy == True
_PMOSDummy_length = None, #None/Value
_PMOSDummy_placement = None, #None/Up/Dn/

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### POLY_Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _PMOSChannelWidth + 2 * _DRCObj.DRCPolygateMinExtensionOnOD(_PMOSChannellength)

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _PMOSChannellength

        #Define Boundary_element _XYCoordinates
            #Define _LengthPMOSBtwPO
        _LengthPMOSBtwPO = _DRCObj.DRCPolygateMinSpace(_DRCObj.DRCPolyMinSpace(_Width=_PMOSChannelWidth, _ParallelLength=_PMOSChannellength)) + _PMOSChannellength
                #Applying GateSpacing
        if _GateSpacing != None:
            if (_GateSpacing + _PMOSChannellength) < _LengthPMOSBtwPO:
                raise NotImplementedError(f"Invalid input arg: GateSpacing({_GateSpacing})")
            else:
                _LengthPMOSBtwPO = _GateSpacing + _PMOSChannellength
        elif _GateSpacing == None:
            _GateSpacing = _DRCObj._PolygateMinSpace

            #Calculate Sref XYcoord
                #initialize coordinate
        self._DesignParameter['_POLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[[0,0]]
        for i in range(0,_PMOSNumberofGate-1):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_POLayer')
            target_coord = tmp1[i][0]['_XY_cent']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_POLayer')
            approaching_coord = tmp2[0][0]['_XY_cent']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_POLayer')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] + _LengthPMOSBtwPO
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_POLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### POLY_Dummy_Layer
        #Define Boundary_element
        self._DesignParameter['_PODummyLayer'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
            #SS28nm DRC(a varies depending on channel width)
        a = 16
            #SS28nm If dummy or not
        if _PMOSDummy == False:
            self._DesignParameter['_PODummyLayer']['_YWidth'] = 0
        elif _PMOSDummy:
            self._DesignParameter['_PODummyLayer']['_YWidth'] = _PMOSChannelWidth + 2 * a

        #Define Boundary_element _XWidth
        if _PMOSDummy == False:
            self._DesignParameter['_PODummyLayer']['_XWidth'] = 0
        elif _PMOSDummy:
            self._DesignParameter['_PODummyLayer']['_XWidth'] = _PMOSChannellength

            #Calculate Sref XYcoord
                #initialized Sref coordinate
        self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[]
        for i in [0,-1]:
            if i == 0:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_POLayer')
                target_coord = tmp1[i][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_PODummyLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_PODummyLayer')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord[0] = New_Scoord[0] - _LengthPMOSBtwPO
                tmpXY.append(New_Scoord)
            else:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_POLayer')
                target_coord = tmp1[i][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_PODummyLayer')
                approaching_coord = tmp2[0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_PODummyLayer')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord[0] = New_Scoord[0] + _LengthPMOSBtwPO
                tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### DIFF(OD/RX)_Dummy_Layer
        #Define Boundary_element
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _PMOSChannelWidth

        #Define Boundary_element _XWidth
        XWidth_OD = _LengthPMOSBtwPO * _PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD
        self._DesignParameter['_ODLayer']['_XWidth'] = XWidth_OD

        #Calculate Sref XYcoord
            #initialize coordinate
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = [[0,0]]
        tmpXY=[]

            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_POLayer')
                    #Target_coordx
        target_coordx = 0.5 * ( tmp1[-1][0]['_XY_right'][0] + tmp1[0][0]['_XY_left'][0] )
                    #Target_coordy
        target_coordy = 0.5 * ( tmp1[0][0]['_XY_up'][1] + tmp1[0][0]['_XY_down'][1] )
        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ODLayer')
        approaching_coord = tmp2[0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ODLayer')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### METAL1_Layer
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        _tmpCOYNum = int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max([_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2])  + _DRCObj._CoMinSpace) / (_DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        self._DesignParameter['_Met1Layer']['_YWidth'] = (_tmpCOYNum - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) + _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element _XWidth
            #SDWidth
        if _SDWidth == None:
            XWidth_Met1 = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        else:
            if _SDWidth < _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO:
                raise NotImplementedError(f"Invalid Value _SDWidth({_SDWidth})")
            else:
                XWidth_Met1 = _SDWidth			
        self._DesignParameter['_Met1Layer']['_XWidth'] = XWidth_Met1

        #Calculate Sref XYcoord
            #get _XYCoordinateOfPMOS
        tmp = self.get_param_KJH3('_ODLayer')
        _XYCoordinateOfPMOS = [tmp[0][0]['_XY_cent']]
            #get _LengthPMOSBtwMet1
        _LengthPMOSBtwMet1 = _LengthPMOSBtwPO
            #Cal coord
        tmpXYs = []
        for i in range(0, _PMOSNumberofGate + 1):
            XY = [_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                  _XYCoordinateOfPMOS[0][1]]
            tmpXYs.append(XY)
            #Define coord
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmpXYs

            ## ################################################################################################################### CONT_Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        #Calculate Sref XYcoord
            #Get _XYCoordinateOfPMOS
        tmp = self.get_param_KJH3('_ODLayer')
        _XYCoordinateOfPMOS = [tmp[0][0]['_XY_cent']]
        
            #CONT XNum/YNum Calculation
        _XNumberOfCOInPMOS = _PMOSNumberofGate + 1
        _YNumberOfCOInPMOS = _tmpCOYNum
                #Check the number of CO On PMOS TR
        if _XNumberOfCOInPMOS == 0 or _YNumberOfCOInPMOS == 0:
            print('************************* Error occurred in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name']))
            if DesignParameters._DebugMode == 0:
                return 0
                
            #Define _LengthPMOSBtwCO
        _LengthPMOSBtwCO = _DRCObj._CoMinSpace + _DRCObj._CoMinWidth
                
            #Cal coord
        tmpXYs = []
        for i in range(0, _XNumberOfCOInPMOS):
            for j in range(0, _YNumberOfCOInPMOS):
                XY = [_XYCoordinateOfPMOS[0][0] - (_XNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                      _XYCoordinateOfPMOS[0][1] - (_YNumberOfCOInPMOS - 1) / 2 * _LengthPMOSBtwCO + j * _LengthPMOSBtwCO]
                tmpXYs.append(XY)
                
            #Define coord
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmpXYs

            ## ################################################################################################################### XVT_Layer

        try:
            if (DesignParameters._Technology == '028nm') and _XVT in ('SLVT', 'LVT', 'RVT', 'HVT'):
                _XVTLayer = '_' + _XVT + 'Layer'
                _XVTLayerMappingName = _XVT
                
            elif DesignParameters._Technology in ('028nm'):
                raise NotImplementedError(f"Invalid '_XVT' argument({_XVT}) for {DesignParameters._Technology}")
                
            else:
                raise NotImplementedError(f"Not Yet Implemented in other technology : {DesignParameters._Technology}")

            if _XVTLayer != None:

                #Define Boundary_element
                self._DesignParameter[_XVTLayer] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping[_XVTLayerMappingName][0],
                                                                                        _Datatype=DesignParameters._LayerMapping[_XVTLayerMappingName][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

                #Define Boundary_element _YWidth
                self._DesignParameter[_XVTLayer]['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODY

                #Define Boundary_element _XWidth
                self._DesignParameter[_XVTLayer]['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._XvtMinEnclosureOfODX

                #Define coord
                self._DesignParameter[_XVTLayer]['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

        except Exception as e:
            import traceback
            traceback.print_exc()
            print('Error Occurred', e)
            raise NotImplementedError

            ## ################################################################################################################### PIMP (PP/BP) Layer
        #Define Boundary_element
        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinEnclosureOfPactiveY

        #Define Boundary_element _XWidth
        if (DesignParameters._Technology == 'TSMC65nm') and (_PMOSDummy == True):
            XWidth_PP_byPODummy = self._DesignParameter['_PODummyLayer']['_XWidth'] + (self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0] - self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) + 2 * _DRCObj._PpMinEnclosureOfPo
        else:
            XWidth_PP_byPODummy = 0

        XWidth_PP_byOD = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinEnclosureOfPactiveX

        self._DesignParameter['_PPLayer']['_XWidth'] = max(XWidth_PP_byPODummy, XWidth_PP_byOD)

        #Define coord
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS

            ## ################################################################################################################### PCCrit_Layer
        #If pccrit
        if DesignParameters._Technology == '028nm' and _PCCrit != False:
            
            #Make PCCrit if gatelentgh is either 30 or 34
            if self._DesignParameter['_POLayer']['_XWidth'] in (30, 34):
            
                #Define Boundary_element
                self._DesignParameter['_PCCRITLayer'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PCCRIT'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PCCRIT'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

                #Define Boundary_element _YWidth
                self._DesignParameter['_PCCRITLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PCCRITExtension

                #Define Boundary_element _XWidth
                self._DesignParameter['_PCCRITLayer']['_XWidth'] = _LengthPMOSBtwMet1 * _PMOSNumberofGate + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByOD + 2 * _DRCObj._PCCRITExtension

                #Define coord
                self._DesignParameter['_PCCRITLayer']['_XYCoordinates'] = _XYCoordinateOfPMOS
            
            
                if self._DesignParameter['_POLayer']['_XWidth'] == 30 :
                    if _GateSpacing not in (96, 222, 100, 230) :
                        raise NotImplementedError
                elif self._DesignParameter['_POLayer']['_XWidth'] == 34 :
                    if _GateSpacing not in (96, 226) :
                        raise NotImplementedError
                        
            #Do not make PCcrit if gatelenght is not either 30 or 34
            else:
                pass


            ## ################################################################################################################### Not generated Layer but used in the Pindrawing: _XYCoordinatePMOSSupplyRouting/ _XYCoordinatePMOSOutputRouting/ _XYCoordinatePMOSGateRouting
                ## ##################################################################################################### _XYCoordinatePMOSSupplyRouting = M1 source coordinates
        #Define Boundary_element
        self._DesignParameter['_XYCoordinatePMOSSupplyRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )
                                                                                       
        tmpXYs = []
        if (_PMOSNumberofGate % 2) == 0:
            for i in range(0, _PMOSNumberofGate // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - _PMOSNumberofGate / 2 * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        else:
            for i in range(0, (_PMOSNumberofGate - 1) // 2 + 1):
                tmpXYs.append([_XYCoordinateOfPMOS[0][0] - ((_PMOSNumberofGate + 1) / 2 - 0.5) * _LengthPMOSBtwMet1 + i * 2 * _LengthPMOSBtwMet1,
                               _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'] = tmpXYs
        
                ## ##################################################################################################### _XYCoordinatePMOSOutputRouting = M1 drain coordinate
        #Define Boundary_element
        self._DesignParameter['_XYCoordinatePMOSOutputRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )
                                                                                       
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
        
                ## ##################################################################################################### _XYCoordinatePMOSGateRouting = gate poly coordinate
       #Define Boundary_element
        self._DesignParameter['_XYCoordinatePMOSGateRouting'] = dict(
                                                                        _DesignParametertype=7,
                                                                        _XYCoordinates=[ ],
                                                                       )

        tmpXYs = []
        for i in range(0, _PMOSNumberofGate):
            tmpXYs.append([_XYCoordinateOfPMOS[0][0] - (_PMOSNumberofGate - 1) / 2 * _LengthPMOSBtwMet1 + i * _LengthPMOSBtwMet1,
                           _XYCoordinateOfPMOS[0][1]])
        self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'] = tmpXYs

            ## ################################################################################################################### _METAL1PINDrawing
        #Define Boundary_element
        self._DesignParameter['_METAL1PINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['M1PIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['M1PIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_METAL1PINDrawing']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_METAL1PINDrawing']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']

        #Define coord
        self._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'] = self._DesignParameter['_Met1Layer']['_XYCoordinates']

            ## ################################################################################################################### _ODLayerPINDrawing
        #Define Boundary_element
        self._DesignParameter['_ODLayerPINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['RXPIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['RXPIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_ODLayerPINDrawing']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_ODLayer')
        tmp2 = self.get_param_KJH3('_POLayer')

        self._DesignParameter['_ODLayerPINDrawing']['_XWidth'] = abs( tmp1[0][0]['_XY_right'][0] - tmp2[-1][0]['_XY_right'][0] )

        #Define coord
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = [[0,0]]

            #Calculate1
                #Target_coord
        tmp1 = self.get_param_KJH3('_ODLayer') 
        target_coord = tmp1[0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            
            #Calculate2
                #Target_coord
        tmp1 = self.get_param_KJH3('_ODLayer')
        target_coord = tmp1[0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ODLayerPINDrawing')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ODLayerPINDrawing')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)		

            #Define
        self._DesignParameter['_ODLayerPINDrawing']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _POLayerPINDrawing
        #Define Boundary_element
        self._DesignParameter['_POLayerPINDrawing'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PCPIN'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PCPIN'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayerPINDrawing']['_YWidth'] = (self._DesignParameter['_POLayer']['_YWidth'] - self._DesignParameter['_ODLayer']['_YWidth']) / 2

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayerPINDrawing']['_XWidth'] = self._DesignParameter['_POLayer']['_XWidth']

        #Define coord
        tmp1 = []
        tmp2 = []
        for i in range(0, len(self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'])):
            tmp1.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], - (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])
            tmp2.append([self._DesignParameter['_XYCoordinatePMOSGateRouting']['_XYCoordinates'][i][0], (self._DesignParameter['_ODLayer']['_YWidth'] / 2 + self._DesignParameter['_POLayerPINDrawing']['_YWidth'] / 2)])

        if _PMOSNumberofGate == 1:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1 + tmp2
        else:
            self._DesignParameter['_POLayerPINDrawing']['_XYCoordinates'] = tmp1

            ## ################################################################################################################### _Met1Layer_Source
        #Define Boundary_element
        self._DesignParameter['_Met1Layer_Source'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer_Source']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer_Source']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']

        #Define coord
            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH3('_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if i%2 == 0 :
                tmp3 = tmp1[i][0]['_XY_cent'] 
                tmpXY.append(tmp3)
            #Drain
            else:
                pass

        self._DesignParameter['_Met1Layer_Source']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _Met1Layer_Drain
        #Define Boundary_element
        self._DesignParameter['_Met1Layer_Drain'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer_Drain']['_YWidth'] = self._DesignParameter['_Met1Layer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer_Drain']['_XWidth'] = self._DesignParameter['_Met1Layer']['_XWidth']

        #Define coord
            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH3('_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if i%2 != 0 :
                tmp3 = tmp1[i][0]['_XY_cent'] 
                tmpXY.append(tmp3)
            #Drain
            else:
                pass

        self._DesignParameter['_Met1Layer_Drain']['_XYCoordinates'] = tmpXY

        if _Source_Via_TF == True:
            ## ################################################################################################################### _Source_ViaM1M2
            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['_Source_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Source_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Source_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Source_ViaM1M2']['_Angle'] = 0

            #Calcuate _COX
            _Caculation_Parameters['_COX'] = 1

            #Calcuate _COY
                #Calculate Number of V1
            tmp   		= self.get_param_KJH3('_Met1Layer')
            M1_ywidth	= tmp[0][0]['_Ywidth']
            Num_V1      = int( ( M1_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) ) + 0
                #Define Num of V1
            _Caculation_Parameters['_COY'] = Num_V1

            #Generate Metal(x), Metal(x+1) and C0(Viax) layer
            self._DesignParameter['_Source_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Source_ViaM1M2']['_XYCoordinates'] = [[0,0]]

                #Define flag
            flag = 1

                #For num of M1 in Nmos
            tmp1 = self.get_param_KJH3('_Met1Layer')
            tmpXY = []
            for i in range(0,len(tmp1)):

                #Source
                if flag == 1:
                        #Calculate
                            #Target_coord
                    tmp1 = self.get_param_KJH3('_Met1Layer')
                    target_coord = tmp1[i][0]['_XY_up']
                            #Approaching_coord
                    tmp2 = self.get_param_KJH3('_Source_ViaM1M2','_ViaM1M2','_Met1Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_up']
                            #Sref coord
                    tmp3 = self.get_param_KJH3('_Source_ViaM1M2')
                    Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord = np.round(New_Scoord,2)
                    tmpXY.append(New_Scoord)

                    flag = -1
                #Drain
                else:
                    flag = +1

            self._DesignParameter['_Source_ViaM1M2']['_XYCoordinates'] = tmpXY

        if _Drain_Via_TF == True:
            ## ################################################################################################################### _Drain_ViaM1M2
            #Define ViaX Parameter
            _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_Layer1'] 	= 1
            _Caculation_Parameters['_Layer2'] 	= 2
            _Caculation_Parameters['_COX'] 		= None
            _Caculation_Parameters['_COY'] 		= None

            #Sref ViaX declaration
            self._DesignParameter['_Drain_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Drain_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Drain_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Drain_ViaM1M2']['_Angle'] = 0

            #Calcuate _COX
            _Caculation_Parameters['_COX'] = 1

            #Calcuate _COY
                #Calculate Number of V1
            tmp   		= self.get_param_KJH3('_Met1Layer')
            M1_ywidth	= tmp[0][0]['_Ywidth']
            Num_V1      = int( ( M1_ywidth - 2 * _DRCObj._Metal1MinEnclosureVia3) / (_DRCObj._VIAxMinWidth + _DRCObj._VIAxMinSpace) ) + 0
                #Define Num of V1
            _Caculation_Parameters['_COY'] = Num_V1

            #Generate Metal(x), Metal(x+1) and C0(Viax) layer
            self._DesignParameter['_Drain_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Drain_ViaM1M2']['_XYCoordinates'] = [[0,0]]

                #Define flag
            flag = 1

                #For num of M1 in Nmos
            tmp1 = self.get_param_KJH3('_Met1Layer')
            tmpXY = []
            for i in range(0,len(tmp1)):

                #Source
                if flag == 1:
                    flag = -1
                #Drain
                else:
                        #Calculate
                            #Target_coord
                    tmp1 = self.get_param_KJH3('_Met1Layer')
                    target_coord = tmp1[i][0]['_XY_up']
                            #Approaching_coord
                    tmp2 = self.get_param_KJH3('_Drain_ViaM1M2','_ViaM1M2','_Met1Layer')
                    approaching_coord = tmp2[0][0][0][0]['_XY_up']
                            #Sref coord
                    tmp3 = self.get_param_KJH3('_Drain_ViaM1M2')
                    Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord = np.round(New_Scoord,2)
                    New_Scoord[1] = New_Scoord[1] -64
                    tmpXY.append(New_Scoord)

                    flag = +1

            self._DesignParameter['_Drain_ViaM1M2']['_XYCoordinates'] = tmpXY

        if _PMOSDummy == True:
            ## ################################################################################################################### POLY_Dummy_Layer2:manual setting

                ## ##################################################################################################### POLY_Dummy_Layer2:manual setting:dummy_length
            if _PMOSDummy_length == None:
                pass
            else:
                self._DesignParameter['_PODummyLayer']['_YWidth'] = _PMOSDummy_length

                ## ##################################################################################################### POLY_Dummy_Layer2:manual setting:dummy_placement
            if _PMOSDummy_placement == None:
                pass
            elif _PMOSDummy_placement == 'Up':
                    #Calculate Sref XYcoord
                        #initialized Sref coordinate
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = [[0,0]]

                tmpXY=[]
                for i in [0,-1]:
                    if i == 0:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_POLayer')
                        target_coord = tmp1[i][0]['_XY_up']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_PODummyLayer')
                        approaching_coord = tmp2[0][0]['_XY_up']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_PODummyLayer')
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord[0] = New_Scoord[0] - _LengthPMOSBtwPO
                        tmpXY.append(New_Scoord)
                    else:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_POLayer')
                        target_coord = tmp1[i][0]['_XY_up']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_PODummyLayer')
                        approaching_coord = tmp2[0][0]['_XY_up']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_PODummyLayer')
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord[0] = New_Scoord[0] + _LengthPMOSBtwPO
                        tmpXY.append(New_Scoord)

                    #Define
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = tmpXY

            elif _PMOSDummy_placement == 'Dn':

                    #Calculate Sref XYcoord
                        #initialized Sref coordinate
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = [[0,0]]

                tmpXY=[]
                for i in [0,-1]:
                    if i == 0:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_POLayer')
                        target_coord = tmp1[i][0]['_XY_down']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_PODummyLayer')
                        approaching_coord = tmp2[0][0]['_XY_down']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_PODummyLayer')
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord[0] = New_Scoord[0] - _LengthPMOSBtwPO
                        tmpXY.append(New_Scoord)
                    else:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_POLayer')
                        target_coord = tmp1[i][0]['_XY_down']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_PODummyLayer')
                        approaching_coord = tmp2[0][0]['_XY_down']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_PODummyLayer')
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord[0] = New_Scoord[0] + _LengthPMOSBtwPO
                        tmpXY.append(New_Scoord)

                    #Define
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = tmpXY

            else:
                pass



        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A01_PmosWithDummy_KJH_89'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

#PMOS
_PMOSNumberofGate	= 5,
_PMOSChannelWidth	= 500,
_PMOSChannellength	= 30,
_GateSpacing		= None,
_SDWidth			= None,
_XVT				= 'SLVT',
_PCCrit				= None,

#Source_node_ViaM1M2
_Source_Via_TF = True,

#Drain_node_ViaM1M2
_Drain_Via_TF = True,

#POLY dummy setting
_PMOSDummy = True, #TF
    #if _PMOSDummy == True
_PMOSDummy_length = None, #None/Value
_PMOSDummy_placement = 'Dn', #None/'Up'/'Dn'/


    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _PmosWithDummy_KJH(_DesignParameter=None, _Name=cellname)
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
    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




