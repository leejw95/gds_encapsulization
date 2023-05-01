'''


'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A00_NMOSWithDummy_v3
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A01_NSubRing
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A02_PMOSWithDummy
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A03_PSubRing
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A04_NbodyContact
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A05_PbodyContact
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A06_ViaStack
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A07_ViaPoly2Met1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A08_ViaMet12Met2_v2
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A09_ViaMet22Met3
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A10_ViaMet32Met4
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A11_ViaMet42Met5
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A12_ViaMet52Met6
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A13_ViaMet62Met7
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A14_ViaMet72Met8
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A16_UNITR

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

import numpy as np
import copy
import math


## ########################################################################################################################################################## Class_HEADER
class _pmos_sw_and_pmos_cs(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= None,
_Cs_PMOSChannelWidth	= None,
_Cs_PMOSChannellength	= None,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= None,
_Cs_PCCrit				= None,
    #Source Via
_Cs_Source_Via_TF		= None,
    #Drain Via
_Cs_Drain_Via_TF		= None,
    #PMOS Dummy
_Cs_PMOSDummy			= None,
        #IF PMOS Dummy == True
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= None,
_Sw_PMOSChannelWidth	= None,
_Sw_PMOSChannellength	= None,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= None,
_Sw_PCCrit				= None,
    #Source Via
_Sw_Source_Via_TF		= None,
    #Drain Via
_Sw_Drain_Via_TF		= None,
    #PMOS Dummy
_Sw_PMOSDummy			= None,
        #IF PMOS Dummy == True
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,



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

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= None,
_Cs_PMOSChannelWidth	= None,
_Cs_PMOSChannellength	= None,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= None,
_Cs_PCCrit				= None,
    #Source Via
_Cs_Source_Via_TF		= None,
    #Drain Via
_Cs_Drain_Via_TF		= None,
    #PMOS Dummy
_Cs_PMOSDummy			= None,
        #IF PMOS Dummy == True
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= None,
_Sw_PMOSChannelWidth	= None,
_Sw_PMOSChannellength	= None,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= None,
_Sw_PCCrit				= None,
    #Source Via
_Sw_Source_Via_TF		= None,
    #Drain Via
_Sw_Drain_Via_TF		= None,
    #PMOS Dummy
_Sw_PMOSDummy			= None,
        #IF PMOS Dummy == True
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,


                                    ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')
        
            ## ################################################################################################################### Gen Pmos Current source
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A01_PmosWithDummy_KJH._PmosWithDummy_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_PMOSNumberofGate'] 	= _Cs_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] 	= _Cs_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] 	= _Cs_PMOSChannellength
        _Caculation_Parameters['_GateSpacing'] 			= _Cs_GateSpacing
        _Caculation_Parameters['_SDWidth'] 				= _Cs_SDWidth
        _Caculation_Parameters['_XVT'] 					= _Cs_XVT
        _Caculation_Parameters['_PCCrit'] 				= _Cs_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] 		= _Cs_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] 		= _Cs_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy'] 			= _Cs_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length'] 	= _Cs_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] 	= _Cs_PMOSDummy_placement

        # Generate Sref
        self._DesignParameter['_Cs_pmos'] = self._SrefElementDeclaration(_DesignObj=A01_PmosWithDummy_KJH._PmosWithDummy_KJH(_DesignParameter=None, _Name='{}:_Cs_pmos'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Cs_pmos']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Cs_pmos']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Cs_pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Cs_pmos']['_XYCoordinates'] = [[0, 0]]

            ## ################################################################################################################### Pmos_Current_Source Drain M2 connection
                ## ##################################################################################################### Pmos_Current_Source Drain M2 connection : Vtc_M2
        # pre-defined values
        y_distance = 150

        # Define Boundary_element
        self._DesignParameter['_Cs_pmos_drain_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Cs_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
        self._DesignParameter['_Cs_pmos_drain_m2_vtc']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos', '_Met1Layer_Drain')
        tmp2 = self.get_param_KJH3('_Cs_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')

        self._DesignParameter['_Cs_pmos_drain_m2_vtc']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]) + y_distance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_pmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Cs_pmos', '_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')
            approaching_coord = tmp2[0][0]['_XY_down']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Cs_pmos_drain_m2_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Current_Source Drain M2 connection : Hrz_M2
        # Define Boundary_element
        self._DesignParameter['_Cs_pmos_drain_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')
        self._DesignParameter['_Cs_pmos_drain_m2_hrz']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )																						

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')
        self._DesignParameter['_Cs_pmos_drain_m2_hrz']['_YWidth'] = tmp1[0][0]['_Xwidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_pmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')  		
        target_coord = tmp1[0][0]['_XY_up_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')  
        approaching_coord = tmp2[0][0]['_XY_down_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_pmos_drain_m2_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Current_Source_PolyConnection
                ## ##################################################################################################### Pmos_Current_Source_PolyConnection: Poly Vtc
        # pre-defined values
        Vtc_poly_ydistance = 80

        # Define Boundary_element
        self._DesignParameter['_Cs_pmos_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Cs_pmos', '_POLayer')
        self._DesignParameter['_Cs_pmos_vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        self._DesignParameter['_Cs_pmos_vtc_poly']['_YWidth'] = Vtc_poly_ydistance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_pmos_vtc_poly']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Cs_pmos', '_POLayer')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_pmos', '_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_pmos_vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Cs_pmos_vtc_poly')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Cs_pmos_vtc_poly']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Current_Source_PolyConnection: Poly Hrz
        # Pre-defined
        Horz_poly_ywidth = 50

        # Define Boundary_element
        self._DesignParameter['_Cs_pmos_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )
        
        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Cs_pmos_vtc_poly')
        self._DesignParameter['_Cs_pmos_hrz_poly']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        self._DesignParameter['_Cs_pmos_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_pmos_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Cs_pmos_vtc_poly')  		
        target_coord = tmp1[0][0]['_XY_down_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Cs_pmos_hrz_poly')  
        approaching_coord = tmp2[0][0]['_XY_up_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Cs_pmos_hrz_poly')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_pmos_hrz_poly']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Current_Source_gate_ViaM0M4
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 0
        _Caculation_Parameters['_Layer2'] 	= 4
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Cs_gate_ViaM0M4'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Cs_gate_ViaM0M4'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Cs_gate_ViaM0M4']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Cs_gate_ViaM0M4']['_Angle'] = 0

        #Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        #Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Cs_gate_ViaM0M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_gate_ViaM0M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Cs_pmos_hrz_poly') 
        target_coord = tmp1[0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Cs_gate_ViaM0M4','_ViaM0M1','_POLayer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Cs_gate_ViaM0M4')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_gate_ViaM0M4']['_XYCoordinates'] = tmpXY


            ## ################################################################################################################### Gen Pmos Switch
        #Pre-defined
        poly_to_xvt_distance = 150

        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A01_PmosWithDummy_KJH._PmosWithDummy_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_PMOSNumberofGate'] 	= _Sw_PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth'] 	= _Sw_PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] 	= _Sw_PMOSChannellength
        _Caculation_Parameters['_GateSpacing'] 			= _Sw_GateSpacing
        _Caculation_Parameters['_SDWidth'] 				= _Sw_SDWidth
        _Caculation_Parameters['_XVT'] 					= _Sw_XVT
        _Caculation_Parameters['_PCCrit'] 				= _Sw_PCCrit
        _Caculation_Parameters['_Source_Via_TF'] 		= _Sw_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] 		= _Sw_Drain_Via_TF
        _Caculation_Parameters['_PMOSDummy'] 			= _Sw_PMOSDummy
        _Caculation_Parameters['_PMOSDummy_length'] 	= _Sw_PMOSDummy_length
        _Caculation_Parameters['_PMOSDummy_placement'] 	= _Sw_PMOSDummy_placement

        # Generate Sref
        self._DesignParameter['_Sw_pmos'] = self._SrefElementDeclaration(_DesignObj=A01_PmosWithDummy_KJH._PmosWithDummy_KJH(_DesignParameter=None, _Name='{}:_Sw_pmos'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Sw_pmos']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Sw_pmos']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Sw_pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Sw_pmos']['_XYCoordinates'] = [[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos']['_XYCoordinates'] = [[0,0]]
            #Calculate

                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH3('_Cs_pmos','_PODummyLayer')  		
        target_coordx = tmp1_1[0][-1][0]['_XY_right'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH3('_Cs_pmos','_{}Layer'.format(_Cs_XVT))  		
        target_coordy = tmp1_2[0][0][0]['_XY_down'][1]
                    #Target_coord
        target_coord = [target_coordx,target_coordy]

                #Approaching_coord
                    #x
        tmp2_1 = self.get_param_KJH3('_Sw_pmos','_PODummyLayer')  
        approaching_coordx = tmp2_1[0][0][0]['_XY_left'][0]
                    #y
        tmp2_2 = self.get_param_KJH3('_Sw_pmos','_{}Layer'.format(_Sw_XVT))  
        approaching_coordy = tmp2_2[0][0][0]['_XY_down'][1]
                    #Approching coord
        approaching_coord = [ approaching_coordx, approaching_coordy ]

                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_pmos')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] + poly_to_xvt_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_pmos']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Switch_Source_M2_connection
                ## ##################################################################################################### Pmos_Switch_Source_M2_connection : Vtc_M2
        # pre-defined values
        y_distance = 150

        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_source_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')
        self._DesignParameter['_Sw_pmos_source_m2_vtc']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Sw_pmos', '_Met1Layer_Source')
        tmp2 = self.get_param_KJH3('_Sw_pmos','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')

        self._DesignParameter['_Sw_pmos_source_m2_vtc']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]) + y_distance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_source_m2_vtc']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Sw_pmos', '_Met1Layer_Source')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Sw_pmos','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_vtc')
            approaching_coord = tmp2[0][0]['_XY_down']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Sw_pmos_source_m2_vtc')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Sw_pmos_source_m2_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Switch_Source_M2_connection : Hrz_M2
        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_source_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos_source_m2_vtc')
        self._DesignParameter['_Sw_pmos_source_m2_hrz']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )																						

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Sw_pmos_source_m2_vtc')
        self._DesignParameter['_Sw_pmos_source_m2_hrz']['_YWidth'] = tmp1[0][0]['_Xwidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_source_m2_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Sw_pmos_source_m2_vtc')  		
        target_coord = tmp1[0][0]['_XY_up_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')  
        approaching_coord = tmp2[0][0]['_XY_down_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_pmos_source_m2_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Switch_Drain_M2_connection
                ## ##################################################################################################### Pmos_Switch_Drain_M2_connection : Vtc_M2
        # pre-defined values
        y_distance = 150

        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_drain_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
        self._DesignParameter['_Sw_pmos_drain_m2_vtc']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Sw_pmos', '_Met1Layer_Drain')
        tmp2 = self.get_param_KJH3('_Sw_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')

        self._DesignParameter['_Sw_pmos_drain_m2_vtc']['_YWidth'] = -abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1]) + y_distance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Sw_pmos', '_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Sw_pmos','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Sw_pmos_drain_m2_vtc')
            approaching_coord = tmp2[0][0]['_XY_up']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Sw_pmos_drain_m2_vtc')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Sw_pmos_drain_m2_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Switch_Drain_M2_connection : Hrz_M2
        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_drain_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos_drain_m2_vtc')
        self._DesignParameter['_Sw_pmos_drain_m2_hrz']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )																						

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Sw_pmos_drain_m2_vtc')
        self._DesignParameter['_Sw_pmos_drain_m2_hrz']['_YWidth'] = tmp1[0][0]['_Xwidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Sw_pmos_drain_m2_vtc')  		
        target_coord = tmp1[0][0]['_XY_down_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Sw_pmos_drain_m2_hrz')  
        approaching_coord = tmp2[0][0]['_XY_up_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_pmos_drain_m2_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_pmos_drain_m2_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Current_Source_gate_ViaM2M3
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 2
        _Caculation_Parameters['_Layer2'] 	= 3
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_drain_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Sw_drain_ViaM2M3'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Sw_drain_ViaM2M3']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Sw_drain_ViaM2M3']['_Angle'] = 0

        #Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        #Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_drain_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_drain_ViaM2M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Sw_pmos_drain_m2_hrz') 
        target_coord = tmp1[0][0]['_XY_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Sw_drain_ViaM2M3','_ViaM2M3','_Met2Layer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_drain_ViaM2M3')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_drain_ViaM2M3']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Switch_PolyConnection
                ## ##################################################################################################### Pmos_Switch_PolyConnection: Poly Vtc
        # pre-defined values
        MxtoMxdistance = 150

        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos', '_POLayer')
        self._DesignParameter['_Sw_pmos_vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Cs_gate_ViaM0M4','_ViaM3M4','_Met4Layer')
        tmp2 = self.get_param_KJH3('_Sw_pmos', '_POLayer')
        self._DesignParameter['_Sw_pmos_vtc_poly']['_YWidth'] = abs( tmp2[0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_down'][1] ) + MxtoMxdistance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_vtc_poly']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Sw_pmos', '_POLayer')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Sw_pmos', '_POLayer')
            target_coord = tmp1[0][i][0]['_XY_down']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Sw_pmos_vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_up']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Sw_pmos_vtc_poly')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Sw_pmos_vtc_poly']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Switch_PolyConnection: Poly Hrz
        # Pre-defined
        Horz_poly_ywidth = 50

        # Define Boundary_element
        self._DesignParameter['_Sw_pmos_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )
        
        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Sw_pmos_vtc_poly')
        self._DesignParameter['_Sw_pmos_hrz_poly']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        self._DesignParameter['_Sw_pmos_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_pmos_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Sw_pmos_vtc_poly')  		
        target_coord = tmp1[0][0]['_XY_down_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Sw_pmos_hrz_poly')  
        approaching_coord = tmp2[0][0]['_XY_up_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_pmos_hrz_poly')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_pmos_hrz_poly']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Switch_gate_ViaM0M4
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 0
        _Caculation_Parameters['_Layer2'] 	= 4
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_gate_ViaM0M4'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Sw_gate_ViaM0M4'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Sw_gate_ViaM0M4']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Sw_gate_ViaM0M4']['_Angle'] = 0

        #Calcuate _COX
        _Caculation_Parameters['_COX'] = 2

        #Calcuate _COY
        _Caculation_Parameters['_COY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_gate_ViaM0M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_gate_ViaM0M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Sw_pmos_hrz_poly') 
        target_coord = tmp1[0][0]['_XY_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Sw_gate_ViaM0M4','_ViaM0M1','_POLayer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Sw_gate_ViaM0M4')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_gate_ViaM0M4']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Cs_Drain and Pmos_Sw_source M2 connection 
                ## ##################################################################################################### Pmos_Cs_Drain and Pmos_Sw_source M2 connection:Hrz
        # Define Boundary_element
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_hrz'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[],
                                                                                                        )
        
        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_hrz']['_XWidth'] = abs( tmp2[0][0]['_XY_left'][0] - tmp1[0][0]['_XY_right'][0] )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')
        if tmp1[0][0]['_XY_up'][1] >= tmp2[0][0]['_XY_up'][1] :
            ywiddth = tmp1[0][0]['_Ywidth']
        else:
            ywiddth = tmp2[0][0]['_Ywidth']

        self._DesignParameter['_Cs_drain_sw_source_m2_connection_hrz']['_YWidth'] = ywiddth


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_hrz']['_XYCoordinates'] = [[0,0]]

        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')

        if tmp1[0][0]['_XY_up'][1] >= tmp2[0][0]['_XY_up'][1] :
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
            target_coord = tmp1[0][0]['_XY_right']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            approaching_coord = tmp2[0][0]['_XY_left']

        else:
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')
            target_coord = tmp1[0][0]['_XY_left']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            approaching_coord = tmp2[0][0]['_XY_right']

                #Sref coord
        tmp3 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_hrz']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Pmos_Cs_Drain and Pmos_Sw_source M2 connection:Vtc
        # Define Boundary_element
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[],
                                                                                                        )

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_vtc')
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc']['_XWidth'] = tmp1[0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')

        if tmp1[0][0]['_XY_up'][1] >= tmp2[0][0]['_XY_up'][1] :
            tmp3 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            tmp4 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')
            self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc']['_YWidth'] = abs( tmp3[0][0]['_XY_up'][1] - tmp4[0][0]['_XY_up'][1] )

        else:
            tmp3 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            tmp4 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
            self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc']['_YWidth'] = abs( tmp3[0][0]['_XY_up'][1] - tmp4[0][0]['_XY_up'][1] )

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc']['_XYCoordinates'] = [[0,0]]

        tmp1 = self.get_param_KJH3('_Cs_pmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH3('_Sw_pmos_source_m2_hrz')

        if tmp1[0][0]['_XY_up'][1] >= tmp2[0][0]['_XY_up'][1] :
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            target_coord = tmp1[0][0]['_XY_up_right']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_vtc')
            approaching_coord = tmp2[0][0]['_XY_up_left']

        else:
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_hrz')
            target_coord = tmp1[0][0]['_XY_up_left']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_vtc')
            approaching_coord = tmp2[0][0]['_XY_up_right']

                #Sref coord
        tmp3 = self.get_param_KJH3('_Cs_drain_sw_source_m2_connection_vtc')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Cs_drain_sw_source_m2_connection_vtc']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pmos_Cs_Drain and Pmos_Sw_source XVT cover-up
        #Check Cs and Sw XVT
        if _Cs_XVT == _Sw_XVT :

            # Define Boundary_element
            self._DesignParameter['_Cs_drain_sw_source_xvt_coverup'] = self._BoundaryElementDeclaration(
                _Layer=DesignParameters._LayerMapping['{}'.format(_Cs_XVT)][0],
                _Datatype=DesignParameters._LayerMapping['{}'.format(_Cs_XVT)][1],
                _XWidth=None,
                _YWidth=None,
                _XYCoordinates=[],
            )

            # check boundary
            tmp1 = self.get_param_KJH3('_Cs_pmos','_{}Layer'.format(_Cs_XVT))
            tmp2 = self.get_param_KJH3('_Sw_pmos','_{}Layer'.format(_Sw_XVT))
                # Most down
            if tmp1[0][0][0]['_XY_down'][1] >= tmp2[0][0][0]['_XY_down'][1] :
                mostdown = tmp2[0][0][0]['_XY_down'][1]
            else:
                mostdown = tmp1[0][0][0]['_XY_down'][1]
                # Most up
            if tmp1[0][0][0]['_XY_up'][1] >= tmp2[0][0][0]['_XY_up'][1] :
                mostup = tmp1[0][0][0]['_XY_up'][1]
            else:
                mostup = tmp2[0][0][0]['_XY_up'][1]

            # Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH3('_Cs_pmos','_{}Layer'.format(_Cs_XVT))
            tmp2 = self.get_param_KJH3('_Sw_pmos','_{}Layer'.format(_Sw_XVT))

            self._DesignParameter['_Cs_drain_sw_source_xvt_coverup']['_XWidth'] = abs( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

            # Define Boundary_element _YWidth
            self._DesignParameter['_Cs_drain_sw_source_xvt_coverup']['_YWidth'] = mostup - mostdown

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Cs_drain_sw_source_xvt_coverup']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Cs_pmos','_{}Layer'.format(_Cs_XVT))
            target_coord = [ tmp1[0][0][0]['_XY_left'][0], mostdown ]
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_drain_sw_source_xvt_coverup')
            approaching_coord = tmp2[0][0]['_XY_down_left']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Cs_drain_sw_source_xvt_coverup')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Cs_drain_sw_source_xvt_coverup']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_F2_building_block'
    cellname = 'F00_pmos_sw_and_pmos_cs_68'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= 2,
_Cs_PMOSChannelWidth	= 1600,
_Cs_PMOSChannellength	= 300,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= 'SLVT', ## Sw and Cs are same
_Cs_PCCrit				= None,
    #Source Via
_Cs_Source_Via_TF		= False,  ## fixed
    #Drain Via
_Cs_Drain_Via_TF		= True,   ## fixed
    #PMOS Dummy
_Cs_PMOSDummy			= True,   ## fixed
        #IF PMOS Dummy == True
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= 2,
_Sw_PMOSChannelWidth	= 1600,
_Sw_PMOSChannellength	= 30,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= 'SLVT', ## Sw and Cs are same
_Sw_PCCrit				= None,
    #Source Via
_Sw_Source_Via_TF		= True,  ## fixed
    #Drain Via
_Sw_Drain_Via_TF		= True,  ## fixed
    #PMOS Dummy
_Sw_PMOSDummy			= True,  ## fixed
        #IF PMOS Dummy == True
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,





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
    LayoutObj = _pmos_sw_and_pmos_cs(_DesignParameter=None, _Name=cellname)
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

    Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
