'''
d

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
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A19_Boundary_element_KJH

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B06_pos_neg
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C05_routing_v2
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D05_pos_neg_side
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.E_Building_block import E01_guardring
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.F2_Building_block import F04_routing
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G04_input_pn

## ########################################################################################################################################################## Class_HEADER
class _Final(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

## Load Resistor
    #polyres
_Array_Polyres_R_X_width  = None,
_Array_Polyres_R_Y_length = None,
_Array_Polyres_CoXNum     = None,
_Array_Polyres_CoYNum     = None,
_Array_Polyres_Dummy      = None,
_Array_Polyres_N_Parallel = None,

    #pmos_sw
_Array_PMOSNumberofGate     = None,
_Array_PMOSChannelWidth     = None,
_Array_PMOSChannellength    = None,
_Array_PMOSDummy            = None,
_Array_GateSpacing          = None,
_Array_SDWidth              = None,
_Array_XVT                  = None,
_Array_PCCrit               = None,

    #Guardring
        #vtc nbodycontact
_Array_vtc_btw_res_sw_NbodyContCount_of_Width = None,
        #hrz nbodycontact
_Array_hrz_NbodyContCount_of_Width_upper_unit = None,
        #leftright vtc nbodycontact
_LeftRight_NbodyContCount_of_Width = None,
        #Middle vtc nbodycontact
_Middle_NbodyContCount_of_Width = None,

## NMOS INPUT TR
    #NMOS
_In_NMOSNumberofGate 	= None,
_In_NMOSChannelWidth 	= None,
_In_NMOSChannellength 	= None,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= None,
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= None,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= None,
    #POLY dummy setting
_In_NMOSDummy 			= None, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/

    # NMOS Parallel
_Num_NMOS				= None,

    # PbodyRing
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeftRight	= None,
_NumContMiddle		= None,
_right_margin 		= None,
_left_margin 		= None,
_up_margin 			= None,
_down_margin 		= None,

## Source degeneration transistor
    # polyres
_C_Array_Polyres_R_X_width    = None,
_C_Array_Polyres_R_Y_length   = None,
_C_Array_Polyres_CoXNum       = None,
_C_Array_Polyres_CoYNum       = None,
_C_Array_Polyres_N_Parallel   = None,
_C_Array_Polyres_Dummy        = None,
_C_Array_Poly_up_connect      = None,

    # nmos_sw
_C_Array_NMOSNumberofGate     = None,
_C_Array_NMOSChannelWidth     = None,
_C_Array_NMOSChannellength    = None,
_C_Array_NMOSDummy            = None,
_C_Array_GateSpacing          = None,
_C_Array_SDWidth              = None,
_C_Array_XVT                  = None,
_C_Array_PCCrit               = None,

    # vtc pbodycontact btw res and sw
_C_Array_vtc_btw_res_sw_PbodyContCount_of_Width   = None,
    # hrz pbodycontact btw unit
_C_Array_hrz_btw_units_PbodyContCount_of_Width    = None,
    # vtc left pbodycontact
_C_Vtc_left_PbodyContCount_of_Width               = None,
    # vtc right pbodycontact
_C_Vtc_right_PbodyContCount_of_Width              = None,

## Tail current source
 # ## Guardring_gen
    # Current source nmos
_D_Array_Cs_NMOSNumberofGate    = None, 
_D_Array_Cs_NMOSChannelWidth    = None,
_D_Array_Cs_NMOSChannellength   = None,
_D_Array_Cs_NMOSDummy           = None, 
_D_Array_Cs_GateSpacing         = None, 
_D_Array_Cs_SDWidth             = None,
_D_Array_Cs_XVT                 = None,
_D_Array_Cs_PCCrit              = None,

    # SW nmos
_D_Array_Sw_NMOSNumberofGate    = None,
_D_Array_Sw_NMOSChannelWidth    = None,
_D_Array_Sw_NMOSChannellength   = None,
_D_Array_Sw_NMOSDummy           = None, 
_D_Array_Sw_GateSpacing         = None,
_D_Array_Sw_SDWidth             = None, 
_D_Array_Sw_XVT                 = None,
_D_Array_Sw_PCCrit              = None,

    # Vtc_pbodycontact
_D_Vtc_PbodyContCount_of_Width = None,
    # Hrz_pbodycontact
_D_Hrz_PbodyContCount_of_Width = None,
    # Dummy_indication
_D_Array_dummy_indication = None,

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

## Load Resistor
    #polyres
_Array_Polyres_R_X_width  = None,
_Array_Polyres_R_Y_length = None,
_Array_Polyres_CoXNum     = None,
_Array_Polyres_CoYNum     = None,
_Array_Polyres_Dummy      = None,
_Array_Polyres_N_Parallel = None,

    #pmos_sw
_Array_PMOSNumberofGate     = None,
_Array_PMOSChannelWidth     = None,
_Array_PMOSChannellength    = None,
_Array_PMOSDummy            = None,
_Array_GateSpacing          = None,
_Array_SDWidth              = None,
_Array_XVT                  = None,
_Array_PCCrit               = None,

    #Guardring
        #vtc nbodycontact
_Array_vtc_btw_res_sw_NbodyContCount_of_Width = None,
        #hrz nbodycontact
_Array_hrz_NbodyContCount_of_Width_upper_unit = None,
        #leftright vtc nbodycontact
_LeftRight_NbodyContCount_of_Width = None,
        #Middle vtc nbodycontact
_Middle_NbodyContCount_of_Width = None,

## NMOS INPUT TR
    #NMOS
_In_NMOSNumberofGate 	= None,
_In_NMOSChannelWidth 	= None,
_In_NMOSChannellength 	= None,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= None,
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= None,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= None,
    #POLY dummy setting
_In_NMOSDummy 			= None, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/

    # NMOS Parallel
_Num_NMOS				= None,

    # PbodyRing
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeftRight	= None,
_NumContMiddle		= None,
_right_margin 		= None,
_left_margin 		= None,
_up_margin 			= None,
_down_margin 		= None,

## Source degeneration transistor
    # polyres
_C_Array_Polyres_R_X_width    = None,
_C_Array_Polyres_R_Y_length   = None,
_C_Array_Polyres_CoXNum       = None,
_C_Array_Polyres_CoYNum       = None,
_C_Array_Polyres_N_Parallel   = None,
_C_Array_Polyres_Dummy        = None,
_C_Array_Poly_up_connect      = None,

    # nmos_sw
_C_Array_NMOSNumberofGate     = None,
_C_Array_NMOSChannelWidth     = None,
_C_Array_NMOSChannellength    = None,
_C_Array_NMOSDummy            = None,
_C_Array_GateSpacing          = None,
_C_Array_SDWidth              = None,
_C_Array_XVT                  = None,
_C_Array_PCCrit               = None,

    # vtc pbodycontact btw res and sw
_C_Array_vtc_btw_res_sw_PbodyContCount_of_Width   = None,
    # hrz pbodycontact btw unit
_C_Array_hrz_btw_units_PbodyContCount_of_Width    = None,
    # vtc left pbodycontact
_C_Vtc_left_PbodyContCount_of_Width               = None,
    # vtc right pbodycontact
_C_Vtc_right_PbodyContCount_of_Width              = None,


## Tail current source
 # ## Guardring_gen
    # Current source nmos
_D_Array_Cs_NMOSNumberofGate    = None, 
_D_Array_Cs_NMOSChannelWidth    = None,
_D_Array_Cs_NMOSChannellength   = None,
_D_Array_Cs_NMOSDummy           = None, 
_D_Array_Cs_GateSpacing         = None, 
_D_Array_Cs_SDWidth             = None,
_D_Array_Cs_XVT                 = None,
_D_Array_Cs_PCCrit              = None,

    # SW nmos
_D_Array_Sw_NMOSNumberofGate    = None,
_D_Array_Sw_NMOSChannelWidth    = None,
_D_Array_Sw_NMOSChannellength   = None,
_D_Array_Sw_NMOSDummy           = None, 
_D_Array_Sw_GateSpacing         = None,
_D_Array_Sw_SDWidth             = None, 
_D_Array_Sw_XVT                 = None,
_D_Array_Sw_PCCrit              = None,

    # Vtc_pbodycontact
_D_Vtc_PbodyContCount_of_Width = None,
    # Hrz_pbodycontact
_D_Hrz_PbodyContCount_of_Width = None,
    # Dummy_indication
_D_Array_dummy_indication = None,

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

            ## ################################################################################################################### B_Building_block: Load_Resistor
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(B06_pos_neg._pos_neg._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Polyres_R_X_width'] 						= _Array_Polyres_R_X_width
        _Caculation_Parameters['_Array_Polyres_R_Y_length'] 					= _Array_Polyres_R_Y_length
        _Caculation_Parameters['_Array_Polyres_CoXNum'] 						= _Array_Polyres_CoXNum
        _Caculation_Parameters['_Array_Polyres_CoYNum'] 						= _Array_Polyres_CoYNum
        _Caculation_Parameters['_Array_Polyres_Dummy'] 							= _Array_Polyres_Dummy
        _Caculation_Parameters['_Array_Polyres_N_Parallel'] 					= _Array_Polyres_N_Parallel

        _Caculation_Parameters['_Array_PMOSNumberofGate'] 						= _Array_PMOSNumberofGate
        _Caculation_Parameters['_Array_PMOSChannelWidth'] 						= _Array_PMOSChannelWidth
        _Caculation_Parameters['_Array_PMOSChannellength'] 						= _Array_PMOSChannellength
        _Caculation_Parameters['_Array_PMOSDummy'] 								= _Array_PMOSDummy
        _Caculation_Parameters['_Array_GateSpacing'] 							= _Array_GateSpacing
        _Caculation_Parameters['_Array_SDWidth'] 								= _Array_SDWidth
        _Caculation_Parameters['_Array_XVT'] 									= _Array_XVT
        _Caculation_Parameters['_Array_PCCrit'] 								= _Array_PCCrit

        _Caculation_Parameters['_Array_vtc_btw_res_sw_NbodyContCount_of_Width'] = _Array_vtc_btw_res_sw_NbodyContCount_of_Width
        _Caculation_Parameters['_Array_hrz_NbodyContCount_of_Width_upper_unit'] = _Array_hrz_NbodyContCount_of_Width_upper_unit

        _Caculation_Parameters['_LeftRight_NbodyContCount_of_Width'] 			= _LeftRight_NbodyContCount_of_Width
        _Caculation_Parameters['_Middle_NbodyContCount_of_Width'] 				= _Middle_NbodyContCount_of_Width

            # Generate Sref
        self._DesignParameter['_B_load_res'] = self._SrefElementDeclaration(_DesignObj=B06_pos_neg._pos_neg(_DesignParameter=None, _Name='{}:_B_load_res'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_B_load_res']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_B_load_res']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_B_load_res']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_B_load_res']['_XYCoordinates'] = [[0,0]]
       
            ## ################################################################################################################### G_Building_block: Input Transistor
            #Pre-defined
        G_Building_block_y_distance = 300
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(G04_input_pn._input_pn._ParametersForDesignCalculation)
        _Caculation_Parameters['_In_NMOSNumberofGate'] 		= _In_NMOSNumberofGate
        _Caculation_Parameters['_In_NMOSChannelWidth'] 		= _In_NMOSChannelWidth
        _Caculation_Parameters['_In_NMOSChannellength'] 	= _In_NMOSChannellength
        _Caculation_Parameters['_In_GateSpacing'] 			= _In_GateSpacing
        _Caculation_Parameters['_In_SDWidth'] 				= _In_SDWidth
        _Caculation_Parameters['_In_XVT'] 					= _In_XVT
        _Caculation_Parameters['_In_PCCrit'] 				= _In_PCCrit

        _Caculation_Parameters['_In_Source_Via_TF'] 		= _In_Source_Via_TF

        _Caculation_Parameters['_In_Drain_Via_TF'] 			= _In_Drain_Via_TF

        _Caculation_Parameters['_In_NMOSDummy'] 			= _In_NMOSDummy

        _Caculation_Parameters['_In_NMOSDummy_length'] 		= _In_NMOSDummy_length
        _Caculation_Parameters['_In_NMOSDummy_placement'] 	= _In_NMOSDummy_placement

        _Caculation_Parameters['_Num_NMOS'] 				= _Num_NMOS

        _Caculation_Parameters['_NumContTop'] 				= _NumContTop
        _Caculation_Parameters['_NumContBottom'] 			= _NumContBottom
        _Caculation_Parameters['_NumContLeftRight'] 		= _NumContLeftRight
        _Caculation_Parameters['_NumContMiddle'] 			= _NumContMiddle

        _Caculation_Parameters['_right_margin'] 			= _right_margin
        _Caculation_Parameters['_left_margin'] 				= _left_margin
        _Caculation_Parameters['_up_margin'] 				= _up_margin
        _Caculation_Parameters['_down_margin'] 				= _down_margin

            # Generate Sref
        self._DesignParameter['_G_input_tr'] = self._SrefElementDeclaration(_DesignObj=G04_input_pn._input_pn(_DesignParameter=None, _Name='{}:_G_input_tr'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_G_input_tr']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_G_input_tr']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_G_input_tr']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_G_input_tr']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_G_input_tr']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #x
        tmp1_1 = self.get_param_KJH3('_B_load_res','_Res_n','_Array_with_ring','_Right_nbodycontact','_Met1Layer')
        tmp1_2 = self.get_param_KJH3('_B_load_res','_Res_p','_Array_with_ring','_Right_nbodycontact','_Met1Layer')
        target_coordx = 0.5 * ( tmp1_1[0][0][0][0][0][0]['_XY_right'][0] + tmp1_2[0][0][0][0][0][0]['_XY_right'][0] ) 
                    #y
        tmp1_3 = self.get_param_KJH3('_B_load_res','_Res_n','_Array_with_ring','_Right_metal1')
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Left')
        tmp2_2 =self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Left')
        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0][0]['_XY_left'][0] + tmp2_2[0][0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Top')
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_up'][1]
            
        approaching_coord = [approaching_coordx,approaching_coordy]
              
                #Sref coord
        tmp3 = self.get_param_KJH3('_G_input_tr')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - G_Building_block_y_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_G_input_tr']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### B_Building_block -- G_Building_block: M5 connection
                ## ##################################################################################################### B_Building_block -- G_Building_block: M5 connection vtc
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_BG_M5conn_vtc'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')
        tmp2 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')
        self._DesignParameter['_BG_M5conn_vtc']['_YWidth'] = abs( tmp2[0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')
        self._DesignParameter['_BG_M5conn_vtc']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_BG_M5conn_vtc']['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_BG_M5conn_vtc']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #P side
            if i ==0:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')  		
                target_coord = tmp1[0][0][0][0]['_XY_down']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_BG_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_BG_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_B_load_res','_Res_n','_M5_conn_res_res')  		
                target_coord = tmp1[0][0][0][0]['_XY_down']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_BG_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_BG_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                
                #Define
        self._DesignParameter['_BG_M5conn_vtc']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### B_Building_block -- G_Building_block: M5 connection hrz
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_BG_M5conn_hrz'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')
        
        self._DesignParameter['_BG_M5conn_hrz']['_YWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')
        tmp3 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')
        self._DesignParameter['_BG_M5conn_hrz']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_left'][0] - tmp3[0][0][0][0][0][0][0][0]['_XY_right'][0] )

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_BG_M5conn_hrz']['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_BG_M5conn_hrz']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
        
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')		
                target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_right']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_BG_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_left']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_BG_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_G_input_tr','_Input_n','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')		
                target_coord = tmp1[0][0][0][0][0][0][0][0]['_XY_right']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_BG_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_right']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_BG_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
                #Define
        self._DesignParameter['_BG_M5conn_hrz']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### C_Building_block: Degen resistor
            #Pre-defined
        C_Building_block_y_distance = 300
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(C05_routing_v2._routing._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Polyres_R_X_width'] 		= _C_Array_Polyres_R_X_width
        _Caculation_Parameters['_Array_Polyres_R_Y_length'] 	= _C_Array_Polyres_R_Y_length
        _Caculation_Parameters['_Array_Polyres_CoXNum'] 	    = _C_Array_Polyres_CoXNum
        _Caculation_Parameters['_Array_Polyres_CoYNum'] 		= _C_Array_Polyres_CoYNum
        _Caculation_Parameters['_Array_Polyres_N_Parallel'] 	= _C_Array_Polyres_N_Parallel
        _Caculation_Parameters['_Array_Polyres_Dummy'] 			= _C_Array_Polyres_Dummy
        _Caculation_Parameters['_Array_Poly_up_connect'] 		= _C_Array_Poly_up_connect

        _Caculation_Parameters['_Array_NMOSNumberofGate'] 		= _C_Array_NMOSNumberofGate
        _Caculation_Parameters['_Array_NMOSChannelWidth'] 		= _C_Array_NMOSChannelWidth
        _Caculation_Parameters['_Array_NMOSChannellength'] 		= _C_Array_NMOSChannellength
        _Caculation_Parameters['_Array_NMOSDummy'] 		        = _C_Array_NMOSDummy
        _Caculation_Parameters['_Array_GateSpacing'] 	        = _C_Array_GateSpacing
        _Caculation_Parameters['_Array_SDWidth'] 				= _C_Array_SDWidth
        _Caculation_Parameters['_Array_XVT'] 				    = _C_Array_XVT
        _Caculation_Parameters['_Array_PCCrit'] 			    = _C_Array_PCCrit
        
        _Caculation_Parameters['_Array_vtc_btw_res_sw_PbodyContCount_of_Width'] = _C_Array_vtc_btw_res_sw_PbodyContCount_of_Width
        _Caculation_Parameters['_Array_hrz_btw_units_PbodyContCount_of_Width'] 	= _C_Array_hrz_btw_units_PbodyContCount_of_Width
        _Caculation_Parameters['_Vtc_left_PbodyContCount_of_Width'] 			= _C_Vtc_left_PbodyContCount_of_Width
        _Caculation_Parameters['_Vtc_right_PbodyContCount_of_Width'] 			= _C_Vtc_right_PbodyContCount_of_Width


            # Generate Sref
        self._DesignParameter['_C_source_degen'] = self._SrefElementDeclaration(_DesignObj=C05_routing_v2._routing(_DesignParameter=None, _Name='{}:_C_source_degen'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_C_source_degen']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_C_source_degen']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_C_source_degen']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_C_source_degen']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_C_source_degen']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #x
        tmp1_1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Left')
        tmp1_2 = self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Left')
        target_coordx = 0.5 * ( tmp1_1[0][0][0][0][0]['_XY_left'][0] + tmp1_2[0][0][0][0][0]['_XY_right'][0] ) 
                    #y
        tmp1_3 = self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Bottom')
        target_coordy = tmp1_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Vtc_right_PbodyContact')
        tmp2_2 =self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Vtc_left_PbodyContact')
        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0]['_XY_left'][0] + tmp2_2[0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_0')
        approaching_coordy = tmp2_3[0][0][0][0]['_XY_up'][1]
            
        approaching_coord = [approaching_coordx,approaching_coordy]
              
                #Sref coord
        tmp3 = self.get_param_KJH3('_C_source_degen')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - C_Building_block_y_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_C_source_degen']['_XYCoordinates'] = tmpXY
        
            ## ################################################################################################################### G_Building_block -- C_Building_block: M5 connection
                ## ##################################################################################################### G_Building_block -- C_Building_block: M5 connection vtc
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_GC_M5conn_vtc'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')
        tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        self._DesignParameter['_GC_M5conn_vtc']['_YWidth'] = abs( tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        self._DesignParameter['_GC_M5conn_vtc']['_XWidth'] = tmp3[0][0][0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_GC_M5conn_vtc']['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_GC_M5conn_vtc']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc') 		
                target_coord = tmp1[0][0][0]['_XY_up']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_GC_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_down']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_GC_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc') 		
                target_coord = tmp1[0][-1][0]['_XY_up']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_GC_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_down']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_GC_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                
                #Define
        self._DesignParameter['_GC_M5conn_vtc']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### G_Building_block -- C_Building_block: M5 connection hrz
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_GC_M5conn_hrz'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')

        self._DesignParameter['_GC_M5conn_hrz']['_YWidth'] = tmp1[0][0][0][0][0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        tmp3 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')
        
            #most right
        if tmp2[0][0][0]['_XY_right'][0] > tmp3[0][0][0][0][0][0][0][0]['_XY_right'][0]:
            mostright = tmp2[0][0][0]['_XY_right']
        else:
            mostright = tmp3[0][0][0][0][0][0][0][0]['_XY_right']
            
            #most left
        if tmp2[0][0][0]['_XY_left'][0] > tmp3[0][0][0][0][0][0][0][0]['_XY_left'][0]:
            mostleft = tmp3[0][0][0][0][0][0][0][0]['_XY_left']
        else:
            mostleft = tmp2[0][0][0]['_XY_left']


        self._DesignParameter['_GC_M5conn_hrz']['_XWidth'] = abs( mostright[0] - mostleft[0] )

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_GC_M5conn_hrz']['_XYCoordinates'] = [[0,0]]

        
            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_GC_M5conn_hrz']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
        
                        #Calculate
                            #Target_coord
                tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
                tmp3 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')
                
                    #most right
                if tmp2[0][0][0]['_XY_right'][0] > tmp3[0][0][0][0][0][0][0][0]['_XY_right'][0]:
                    mostright = tmp2[0][0][0]['_XY_right']
                else:
                    mostright = tmp3[0][0][0][0][0][0][0][0]['_XY_right']
                   
                target_coordx =  mostright[0]
                target_coordy = tmp3[0][0][0][0][0][0][0][0]['_XY_cent'][1]
                target_coord = [target_coordx,target_coordy]
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_GC_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_right']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_GC_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
                tmp3 = self.get_param_KJH3('_G_input_tr','_Input_n','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')
                
                    #most right
                if tmp2[0][-1][0]['_XY_right'][0] > tmp3[0][0][0][0][0][0][0][0]['_XY_right'][0]:
                    mostright = tmp2[0][-1][0]['_XY_right']
                else:
                    mostright = tmp3[0][0][0][0][0][0][0][0]['_XY_right']
                   
                target_coordx =  mostright[0]
                target_coordy = tmp3[0][0][0][0][0][0][0][0]['_XY_cent'][1]
                target_coord = [target_coordx,target_coordy]
                
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_GC_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_right']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_GC_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
                #Define
        self._DesignParameter['_GC_M5conn_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### D_Building_block: Tail current source
            #Pre-defined
        D_Building_block_y_distance = 300
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(D05_pos_neg_side._pos_neg_side._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Cs_NMOSNumberofGate'] 		= _D_Array_Cs_NMOSNumberofGate
        _Caculation_Parameters['_Array_Cs_NMOSChannelWidth'] 	    = _D_Array_Cs_NMOSChannelWidth
        _Caculation_Parameters['_Array_Cs_NMOSChannellength'] 	    = _D_Array_Cs_NMOSChannellength
        _Caculation_Parameters['_Array_Cs_NMOSDummy'] 		        = _D_Array_Cs_NMOSDummy
        _Caculation_Parameters['_Array_Cs_GateSpacing'] 	        = _D_Array_Cs_GateSpacing
        _Caculation_Parameters['_Array_Cs_SDWidth'] 			    = _D_Array_Cs_SDWidth
        _Caculation_Parameters['_Array_Cs_XVT'] 		            = _D_Array_Cs_XVT
        _Caculation_Parameters['_Array_Cs_PCCrit'] 		            = _D_Array_Cs_PCCrit

        _Caculation_Parameters['_Array_Sw_NMOSNumberofGate'] 		= _D_Array_Sw_NMOSNumberofGate
        _Caculation_Parameters['_Array_Sw_NMOSChannelWidth'] 		= _D_Array_Sw_NMOSChannelWidth
        _Caculation_Parameters['_Array_Sw_NMOSChannellength'] 		= _D_Array_Sw_NMOSChannellength
        _Caculation_Parameters['_Array_Sw_NMOSDummy'] 		        = _D_Array_Sw_NMOSDummy
        _Caculation_Parameters['_Array_Sw_GateSpacing'] 	        = _D_Array_Sw_GateSpacing
        _Caculation_Parameters['_Array_Sw_SDWidth'] 				= _D_Array_Sw_SDWidth
        _Caculation_Parameters['_Array_Sw_XVT'] 				    = _D_Array_Sw_XVT
        _Caculation_Parameters['_Array_Sw_PCCrit'] 			        = _D_Array_Sw_PCCrit
        
        _Caculation_Parameters['_Vtc_PbodyContCount_of_Width']      = _D_Vtc_PbodyContCount_of_Width
        _Caculation_Parameters['_Hrz_PbodyContCount_of_Width'] 	            = _D_Hrz_PbodyContCount_of_Width
        _Caculation_Parameters['_Array_dummy_indication'] 	        = _D_Array_dummy_indication


            # Generate Sref
        self._DesignParameter['_D_tail_cs'] = self._SrefElementDeclaration(_DesignObj=D05_pos_neg_side._pos_neg_side(_DesignParameter=None, _Name='{}:_D_tail_cs'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_D_tail_cs']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_D_tail_cs']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_D_tail_cs']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_D_tail_cs']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_D_tail_cs']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Vtc_right_PbodyContact')
        tmp2_2 =self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Vtc_left_PbodyContact')
        target_coordx = 0.5 * ( tmp2_1[0][0][0][0]['_XY_left'][0] + tmp2_2[0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_C_source_degen','_Routing_guardring','_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(len(_C_Array_NMOSNumberofGate)),)
        target_coordy = tmp2_3[0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_D_tail_cs','_Right_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_left_extension_Met1Layer')
        tmp2_2 =self.get_param_KJH3('_D_tail_cs','_Left_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_left_extension_Met1Layer')

        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0][0][0][0]['_XY_right'][0] + tmp2_2[0][0][0][0][0][0][0]['_XY_right'][0] )
                    #y
        tmp2_3 =self.get_param_KJH3('_D_tail_cs','_Right_side','_Placement','_Unit_0_0','_Guardring','_Unit_Hrz_pbody_upper_extension_Me1Layer')
        approaching_coordy = tmp2_3[0][0][0][0][0][0][0]['_XY_up'][1] 
            
        approaching_coord = [approaching_coordx,approaching_coordy]
              
                #Sref coord
        tmp3 = self.get_param_KJH3('_D_tail_cs')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - D_Building_block_y_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_D_tail_cs']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### C_Building_block -- D_Building_block: M5 connection
                ## ##################################################################################################### C_Building_block -- D_Building_block: M5 connection vtc
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_CD_M5conn_vtc'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        tmp2 = self.get_param_KJH3('_D_tail_cs','_Left_side','_Sw_drain_M4_hrz')
        self._DesignParameter['_CD_M5conn_vtc']['_YWidth'] = abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        self._DesignParameter['_CD_M5conn_vtc']['_XWidth'] = np.ceil(tmp3[0][0][0]['_Xwidth'])

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_CD_M5conn_vtc']['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_CD_M5conn_vtc']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc') 		
                target_coord = tmp1[0][0][0]['_XY_down']  
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc') 		
                target_coord = tmp1[0][-1][0]['_XY_down']
                target_coord = np.round(target_coord)
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']
                approaching_coord = np.round(approaching_coord)
                            #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord)
                tmpXY.append(New_Scoord)
                
                #Define
        self._DesignParameter['_CD_M5conn_vtc']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### C_Building_block -- D_Building_block: M5 connection hrz
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_CD_M5conn_hrz'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')

        self._DesignParameter['_CD_M5conn_hrz']['_YWidth'] = tmp1[0][0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        tmp3 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
        
            #most right
        if tmp2[0][-1][0]['_XY_right'][0] > tmp3[0][0][0][0][0]['_XY_right'][0]:
            mostright = tmp2[0][-1][0]['_XY_right']
        else:
            mostright = tmp3[0][0][0][0][0]['_XY_right']
            
            #most left
        if tmp2[0][-1][0]['_XY_left'][0] > tmp3[0][0][0][0][0]['_XY_left'][0]:
            mostleft = tmp3[0][0][0][0][0]['_XY_left']
        else:
            mostleft = tmp2[0][-1][0]['_XY_left']


        self._DesignParameter['_CD_M5conn_hrz']['_XWidth'] = abs( mostright[0] - mostleft[0] )

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_CD_M5conn_hrz']['_XYCoordinates'] = [[0,0]]

        
            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_CD_M5conn_hrz']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
        
                        #Calculate
                            #Target_coord
                tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
                tmp3 = self.get_param_KJH3('_D_tail_cs','_Left_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
                
                    #most right
                if tmp2[0][0][0]['_XY_right'][0] > tmp3[0][0][0][0][0]['_XY_left'][0]:
                    mostright = tmp2[0][0][0]['_XY_right']
                else:
                    mostright = tmp3[0][0][0][0][0]['_XY_left']
                   
                target_coordx =  mostright[0]
                target_coordy = tmp3[0][0][0][0][0]['_XY_cent'][1]
                target_coord = [target_coordx,target_coordy]
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_right']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
            #Nside
            else:
                        #Calculate
                            #Target_coord
                tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
                tmp3 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
                
                    #most right
                if tmp2[0][-1][0]['_XY_right'][0] > tmp3[0][0][0][0][0]['_XY_right'][0]:
                    mostright = tmp2[0][-1][0]['_XY_right']
                else:
                    mostright = tmp3[0][0][0][0][0]['_XY_right']
                   
                target_coordx =  mostright[0]
                target_coordy = tmp3[0][0][0][0][0]['_XY_cent'][1]
                target_coord = [target_coordx,target_coordy]
                
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_hrz')  
                approaching_coord = tmp2[0][0]['_XY_right']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_hrz')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
                #Define
        self._DesignParameter['_CD_M5conn_hrz']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### C_Building_block -- D_Building_block: ViaM4M5
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 4
        _Caculation_Parameters['_Layer2'] 	= 5
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_CD_M5conn_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_CD_M5conn_ViaM4M5'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_CD_M5conn_ViaM4M5']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_CD_M5conn_ViaM4M5']['_Angle'] = 0

        #Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
        tmp2 = self.get_param_KJH3('_CD_M5conn_hrz')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0],tmp2[-1][0])

        #Calcuate _COX and _COY
        _COX, _COY= self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'],Ovlpcoord[0]['_Ywidth'],None)  ## None or 'MinEnclosureX' or 'MinEnclosureY'

        #Define _COX and _COY
        _Caculation_Parameters['_COX'] 		= _COX
        _Caculation_Parameters['_COY'] 		= _COY

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_CD_M5conn_ViaM4M5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_CD_M5conn_ViaM4M5']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i == 0:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_D_tail_cs','_Left_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
                target_coord = tmp1[0][0][0][0][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_ViaM4M5','_ViaM4M5','_Met4Layer')  
                approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_ViaM4M5')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            #Nside
            else:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Sw_drain_hrz_Via3_M3M4','_Met4Layer')
                target_coord = tmp1[0][0][0][0][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_ViaM4M5','_ViaM4M5','_Met4Layer')  
                approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_ViaM4M5')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                
            #Define
        self._DesignParameter['_CD_M5conn_ViaM4M5']['_XYCoordinates'] = tmpXY
        
        
        
        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_H_building_block'
    cellname = 'H00_Final_69'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

## Load_Resistor
    #polyres
_Array_Polyres_R_X_width  = [500, 1500, 1000, 800,1100,],
_Array_Polyres_R_Y_length = [600, 800, 850, 1000,700,],
_Array_Polyres_CoXNum     = [None,None,None,None,None,],
_Array_Polyres_CoYNum     = [None,None,None,None,None,],
_Array_Polyres_Dummy      = False,
_Array_Polyres_N_Parallel = [1,1,1,1,1],

    #pmos_sw
_Array_PMOSNumberofGate     = [0, 3, 6, 2, 8,],
_Array_PMOSChannelWidth     = [500, 700, 600, 400, 580],
_Array_PMOSChannellength    = [30,30,30,80,30,],
_Array_PMOSDummy            = [True,True,True,True,True],
_Array_GateSpacing          = [None,None,None,None,None],
_Array_SDWidth              = [None,None,None,None,None],
_Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT','SLVT'],
_Array_PCCrit               = [None,None,None,None,None],

    # Guardring
        #vtc nbodycontact
_Array_vtc_btw_res_sw_NbodyContCount_of_Width = [4,4,4,4,2],
        #hrz nbodycontact
_Array_hrz_NbodyContCount_of_Width_upper_unit = [3,3,3,3,3,4],
        #leftright vtc nbodycontact
_LeftRight_NbodyContCount_of_Width = 5,
        #Middle vtc nbodycontact
_Middle_NbodyContCount_of_Width = 3,


## NMOS INPUT UNIT TR
    #NMOS
_In_NMOSNumberofGate 	= 5,
_In_NMOSChannelWidth 	= 625,
_In_NMOSChannellength 	= 40,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= 'RVT',
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= True,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= True,
    #POLY dummy setting
_In_NMOSDummy 			= True, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/

    # NMOS Parallel
_Num_NMOS				= 7,

    # PbodyRing : _NumContTop
_NumContTop			= 3,
_NumContBottom		= 4,
_NumContLeftRight	= 5,
_NumContMiddle		= 6,

_right_margin 		= 150,
_left_margin 		= 142,
_up_margin 			= 131,
_down_margin 		= 120,

## Source degeneration transistor
    # polyres
_C_Array_Polyres_R_X_width    = [ 1500, 2000, 1500, 2000, 1500, 2000, 1800, 1000],
_C_Array_Polyres_R_Y_length   = [ 850, 500,850, 500,850, 500, 700, 500],
_C_Array_Polyres_CoXNum       = [ None, None,None, None,None, None, None, None],
_C_Array_Polyres_CoYNum       = [ None, None,None, None,None, None, None, None],
_C_Array_Polyres_N_Parallel   = [ 2,2,2,2,2, 1, 2, 8],
_C_Array_Polyres_Dummy        = [ True, True,True, True,True, True, True, True],
_C_Array_Poly_up_connect      = [ True, True,True, True,True, True, True, True],

    # nmos_sw
_C_Array_NMOSNumberofGate     = [8,7,10,3,1, 5, 8, 0],
_C_Array_NMOSChannelWidth     = [1500,1000,400,500,600, 400, 800, 1000],
_C_Array_NMOSChannellength    = [30, 30, 30, 30,30, 30, 30, 30],
_C_Array_NMOSDummy            = [True, True, True, True,True, True, True, True],
_C_Array_GateSpacing          = [None, None, None, None,None, None, None, None],
_C_Array_SDWidth              = [None, None, None, None,None, None, None, None],
_C_Array_XVT                  = ['SLVT', 'SLVT', 'SLVT', 'SLVT','SLVT', 'SLVT', 'SLVT', 'SLVT'],
_C_Array_PCCrit               = [None, None, None, None,None, None, None, None],

    # vtc pbodycontact btw res and sw
_C_Array_vtc_btw_res_sw_PbodyContCount_of_Width   = [5, 5, 5, 5, 5, 5, 5, 5],
    # hrz pbodycontact btw unit
_C_Array_hrz_btw_units_PbodyContCount_of_Width    = [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
    # vtc left pbodycontact
_C_Vtc_left_PbodyContCount_of_Width               = 5,
    # vtc right pbodycontact
_C_Vtc_right_PbodyContCount_of_Width              = 5,

## Tail current source
 # ## Guardring_gen
    # Current source nmos
_D_Array_Cs_NMOSNumberofGate    =[ [2, 2,2,2, 1,1, 2,2],[2, 2,2,2,2,2,2, 2],[2, 2,2,2,2,2, 1, 2] ], 
_D_Array_Cs_NMOSChannelWidth    =[ [1000, 1000,1000,1000, 500,500, 1000,1000,], [1000, 1000,1000,1000,1000,1000,1000, 1000,], [1000, 1000,1000,1000,1000,1000, 500, 1000,] ] ,
_D_Array_Cs_NMOSChannellength   =[ [200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200] ] ,
_D_Array_Cs_NMOSDummy           =True, 
_D_Array_Cs_GateSpacing         =None, 
_D_Array_Cs_SDWidth             =None,
_D_Array_Cs_XVT                 ='SLVT',
_D_Array_Cs_PCCrit              =None,

    # SW nmos
_D_Array_Sw_NMOSNumberofGate    =[ [1, 1,1,1, 1,1, 1,1,],[1, 1,1,1,1,1,1, 1],[1, 1,1,1,1,1, 1, 1,] ] ,
_D_Array_Sw_NMOSChannelWidth    =[ [1000, 1000,1000,1000, 1000,1000, 1000,1000,], [1000, 1000,1000,1000,1000,1000,1000, 1000,],[1000, 1000,1000,1000,1000,1000, 1000, 1000,] ] ,
_D_Array_Sw_NMOSChannellength   =[ [30, 30,30,30, 30,30, 30,30,], [30, 30,30,30,30,30,30, 30],[30, 30,30,30,30,30, 30, 30,]],
_D_Array_Sw_NMOSDummy           =True, 
_D_Array_Sw_GateSpacing         =None,
_D_Array_Sw_SDWidth             =None, 
_D_Array_Sw_XVT                 ='SLVT',
_D_Array_Sw_PCCrit              =None,

    # Vtc_pbodycontact
_D_Vtc_PbodyContCount_of_Width = 3,
    # Hrz_pbodycontact
_D_Hrz_PbodyContCount_of_Width = 3,
    # Dummy_indication
_D_Array_dummy_indication =[ [1, 0,0,0, 0,0, 1,1,],[1, 0,0,0,0,0,0, 1],[1, 0,0,0,0,0, 0, 1,] ] ,



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
    LayoutObj = _Final(_DesignParameter=None, _Name=cellname)
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
