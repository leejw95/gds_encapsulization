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
import time

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

## Ncap
    #Ncap
_E_XWidth		=None, 		## Poly Xwidthh
_E_YWidth		=None,		## OD Ywidht
_E_NumofGates	=None,			## Column
_E_NumofOD	    =None,			## Row

    #M1 Routing: Connecting gates
_E_Routing_flag = None,

    #PbodyRing
_E_NumContTop		= None,
_E_NumContBottom	= None,
_E_NumContLeft		= None,
_E_NumContRight		= None,
_E_right_margin 	= None,
_E_left_margin 		= None,
_E_up_margin 		= None,
_E_down_margin 		= None,

## Pbias Current source pmos
    #Pmos current source
        #PMOS
_F_Cs_PMOSNumberofGate	= None,
_F_Cs_PMOSChannelWidth	= None,
_F_Cs_PMOSChannellength	= None,
_F_Cs_GateSpacing		= None,
_F_Cs_SDWidth			= None,
_F_Cs_XVT				= None, 
_F_Cs_PCCrit			= None,

        #Pmos dummy option
_F_Cs_PMOSDummy_length	    = None,
_F_Cs_PMOSDummy_placement   = None,

    # PMOS Switch
        #PMOS
_F_Sw_PMOSNumberofGate	= None,
_F_Sw_PMOSChannelWidth	= None,
_F_Sw_PMOSChannellength	= None,
_F_Sw_GateSpacing		= None,
_F_Sw_SDWidth			= None,
_F_Sw_XVT				= None,
_F_Sw_PCCrit			= None,

        #Pmos dummy option
_F_Sw_PMOSDummy_length	    = None,
_F_Sw_PMOSDummy_placement   = None,

    # NbodyRing
_F_NumCont			= None,
_F_right_margin 	= None,
_F_left_margin 		= None,
_F_up_margin 		= None,
_F_down_margin 		= None,

    # Placement
_F_Array_size = None,

    #_Pbias
_F_Pbias_M4_hrz_width = None,
_F_Pbias_M3_vtc_width = None,

    #_Nbias
_F_Nbias_M3_vtc_width = None,

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

## Ncap
    #Ncap
_E_XWidth		=None, 		## Poly Xwidthh
_E_YWidth		=None,		## OD Ywidht
_E_NumofGates	=None,			## Column
_E_NumofOD	    =None,			## Row

    #M1 Routing: Connecting gates
_E_Routing_flag = None,

    #PbodyRing
_E_NumContTop		= None,
_E_NumContBottom	= None,
_E_NumContLeft		= None,
_E_NumContRight		= None,
_E_right_margin 	= None,
_E_left_margin 		= None,
_E_up_margin 		= None,
_E_down_margin 		= None,


## Pbias Current source pmos
    #Pmos current source
        #PMOS
_F_Cs_PMOSNumberofGate	= None,
_F_Cs_PMOSChannelWidth	= None,
_F_Cs_PMOSChannellength	= None,
_F_Cs_GateSpacing		= None,
_F_Cs_SDWidth			= None,
_F_Cs_XVT				= None, 
_F_Cs_PCCrit			= None,

        #Pmos dummy option
_F_Cs_PMOSDummy_length	    = None,
_F_Cs_PMOSDummy_placement   = None,

    # PMOS Switch
        #PMOS
_F_Sw_PMOSNumberofGate	= None,
_F_Sw_PMOSChannelWidth	= None,
_F_Sw_PMOSChannellength	= None,
_F_Sw_GateSpacing		= None,
_F_Sw_SDWidth			= None,
_F_Sw_XVT				= None,
_F_Sw_PCCrit			= None,

        #Pmos dummy option
_F_Sw_PMOSDummy_length	    = None,
_F_Sw_PMOSDummy_placement   = None,

    # NbodyRing
_F_NumCont			= None,
_F_right_margin 	= None,
_F_left_margin 		= None,
_F_up_margin 		= None,
_F_down_margin 		= None,

    # Placement
_F_Array_size = None,

    #_Pbias
_F_Pbias_M4_hrz_width = None,
_F_Pbias_M3_vtc_width = None,

    #_Nbias
_F_Nbias_M3_vtc_width = None,

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

        _Caculation_Parameters['_In_Source_Via_TF'] 		= True

        _Caculation_Parameters['_In_Drain_Via_TF'] 			= True

        _Caculation_Parameters['_In_NMOSDummy'] 			= True

        _Caculation_Parameters['_In_NMOSDummy_length'] 		= None
        _Caculation_Parameters['_In_NMOSDummy_placement'] 	= None

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
        tmp2_1 =self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')
        tmp2_2 =self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')
        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0][0][0]['_XY_left'][0] + tmp2_2[0][0][0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Top','_BoundaryElement')
        approaching_coordy = tmp2_3[0][0][0][0][0][0]['_XY_up'][1]
            
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
        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_source_ViaM2M5','_ViaM4M5','_Met5Layer')
        tmp2 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')
        YWidth = abs( tmp2[0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0][0][0][0][0]['_XY_up'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_B_load_res','_Res_p','_M5_conn_res_res')
        XWidth = tmp3[0][0][0][0]['_Xwidth']
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A19_Boundary_element_KJH._Boundary_element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] 	= 'METAL5'
        _Caculation_Parameters['_XWidth'] 		    = XWidth
        _Caculation_Parameters['_YWidth'] 	        = YWidth
        
            # Generate Sref
        self._DesignParameter['_BG_M5conn_vtc'] = self._SrefElementDeclaration(_DesignObj=A19_Boundary_element_KJH._Boundary_element_KJH(_DesignParameter=None, _Name='{}:_BG_M5conn_vtc'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_BG_M5conn_vtc']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_BG_M5conn_vtc']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_BG_M5conn_vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
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
                tmp2 = self.get_param_KJH3('_BG_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_up']   
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
                tmp2 = self.get_param_KJH3('_BG_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_up']   
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
        tmp1_1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')
        tmp1_2 = self.get_param_KJH3('_G_input_tr','_Input_n','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')
        target_coordx = 0.5 * ( tmp1_1[0][0][0][0][0][0]['_XY_left'][0] + tmp1_2[0][0][0][0][0][0]['_XY_right'][0] )
                    #y
        tmp1_3 = self.get_param_KJH3('_G_input_tr','_Input_p','_Pbodyring','_ExtenMet1Layer_Bottom','_BoundaryElement')
        target_coordy = tmp1_3[0][0][0][0][0][0]['_XY_down'][1]

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
        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_G_input_tr','_Input_p','_Dummy','_Tr_parallel','_Unit_tr_drain_ViaM2M5','_ViaM4M5','_Met5Layer')
        tmp2 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        YWidth = abs( tmp1[0][0][0][0][0][0][0][0]['_XY_down'][1] - tmp2[0][0][0]['_XY_up'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        XWidth= tmp3[0][0][0]['_Xwidth']
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A19_Boundary_element_KJH._Boundary_element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] 	= 'METAL5'
        _Caculation_Parameters['_XWidth'] 		    = XWidth
        _Caculation_Parameters['_YWidth'] 	        = YWidth
        
            # Generate Sref
        self._DesignParameter['_GC_M5conn_vtc'] = self._SrefElementDeclaration(_DesignObj=A19_Boundary_element_KJH._Boundary_element_KJH(_DesignParameter=None, _Name='{}:_GC_M5conn_vtc'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_GC_M5conn_vtc']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_GC_M5conn_vtc']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_GC_M5conn_vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
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
                tmp2 = self.get_param_KJH3('_GC_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_down']   
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
                tmp2 = self.get_param_KJH3('_GC_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_down']   
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
        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        tmp2 = self.get_param_KJH3('_D_tail_cs','_Left_side','_Sw_drain_M4_hrz')
        YWidth = abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_C_source_degen','_res_M5conn_vtc')
        XWidth= tmp3[0][0][0]['_Xwidth']
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A19_Boundary_element_KJH._Boundary_element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] 	= 'METAL5'
        _Caculation_Parameters['_XWidth'] 		    = np.ceil(XWidth)
        _Caculation_Parameters['_YWidth'] 	        = YWidth
        
            # Generate Sref
        self._DesignParameter['_CD_M5conn_vtc'] = self._SrefElementDeclaration(_DesignObj=A19_Boundary_element_KJH._Boundary_element_KJH(_DesignParameter=None, _Name='{}:_CD_M5conn_vtc'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_CD_M5conn_vtc']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_CD_M5conn_vtc']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_CD_M5conn_vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
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
                tmp2 = self.get_param_KJH3('_CD_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_up']   
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
                target_coord = tmp1[0][-1][0]['_XY_down_left']
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_CD_M5conn_vtc','_BoundaryElement')  
                approaching_coord = tmp2[0][0][0]['_XY_up_left']
                            #Sref coord
                tmp3 = self.get_param_KJH3('_CD_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.floor(New_Scoord) ##--> fucking
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
        
            ## ################################################################################################################### E_Building_block: Ncap for Nbias
            #Pre-defined
        E_Building_block_y_distance = 300
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(E01_guardring._guardring._ParametersForDesignCalculation)
        _Caculation_Parameters['_XWidth'] 		    = _E_XWidth
        _Caculation_Parameters['_YWidth'] 	        = _E_YWidth
        _Caculation_Parameters['_NumofGates'] 	    = _E_NumofGates
        _Caculation_Parameters['_NumofOD'] 		    = _E_NumofOD
        
        _Caculation_Parameters['_Routing_flag'] 	= _E_Routing_flag
        
        _Caculation_Parameters['_Nbias_hrz_legnth'] = None
        
        _Caculation_Parameters['_NumContTop'] 		= _E_NumContTop
        _Caculation_Parameters['_NumContBottom'] 	= _E_NumContBottom
        _Caculation_Parameters['_NumContLeft'] 		= _E_NumContLeft
        _Caculation_Parameters['_NumContRight'] 	= _E_NumContRight
        _Caculation_Parameters['_right_margin'] 	= _E_right_margin
        _Caculation_Parameters['_left_margin'] 		= _E_left_margin
        _Caculation_Parameters['_up_margin'] 	    = _E_up_margin
        _Caculation_Parameters['_down_margin'] 		= _E_down_margin

            # Define Sref Relection
        tmp2_1 =self.get_param_KJH3('_D_tail_cs','_Right_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_right_extension_Met1Layer')
        tmp2_2 =self.get_param_KJH3('_D_tail_cs','_Left_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_right_extension_Met1Layer')
         
        _Caculation_Parameters['_Nbias_hrz_legnth'] = abs ( tmp2_1[0][0][0][0][0][0][0]['_XY_right'][0] - tmp2_2[0][0][0][0][0][0][0]['_XY_right'][0] )

            # Generate Sref
        self._DesignParameter['_E_Ncap_for_Nbias'] = self._SrefElementDeclaration(_DesignObj=E01_guardring._guardring(_DesignParameter=None, _Name='{}:_E_Ncap_for_Nbias'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_E_Ncap_for_Nbias']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_E_Ncap_for_Nbias']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_E_Ncap_for_Nbias']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_E_Ncap_for_Nbias']['_XYCoordinates'] = [[0,0]]


        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_E_Ncap_for_Nbias']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_D_tail_cs','_Right_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_right_extension_Met1Layer')
        tmp2_2 =self.get_param_KJH3('_D_tail_cs','_Left_side','_Placement','_Unit_0_{}'.format(len(_D_Array_Cs_NMOSNumberofGate[0])-1),'_Guardring','_Unit_Vtc_pbody_right_extension_Met1Layer')
        target_coordx = 0.5 * ( tmp2_1[0][0][0][0][0][0][0]['_XY_right'][0] + tmp2_2[0][0][0][0][0][0][0]['_XY_right'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Placement','_Unit_{}_0'.format(len(_D_Array_Cs_NMOSNumberofGate)-1),'_Guardring','_Unit_Hrz_pbody_lower_extension_Me1Layer')
        target_coordy = tmp2_3[0][0][0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Right','_BoundaryElement')
        tmp2_2 =self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')

        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0][0]['_XY_right'][0] + tmp2_2[0][0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 =self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Top','_BoundaryElement')
        approaching_coordy = tmp2_3[0][0][0][0][0]['_XY_up'][1]
            
        approaching_coord = [approaching_coordx,approaching_coordy]
              
                #Sref coord
        tmp3 = self.get_param_KJH3('_E_Ncap_for_Nbias')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - E_Building_block_y_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_E_Ncap_for_Nbias']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### D_Building_block -- E_Building_block: M3 connection
                ## ##################################################################################################### D_Building_block -- E_Building_block: M3 connection vtc
        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Cs_gate_M3_vtc_0')
        tmp2 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Nbias','_Nbias_m3')
        YWidth = abs( tmp1[0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Cs_gate_M3_vtc_0')
        XWidth= tmp3[0][0][0][0]['_Xwidth']
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A19_Boundary_element_KJH._Boundary_element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] 	= 'METAL3'
        _Caculation_Parameters['_XWidth'] 		    = int(XWidth)
        _Caculation_Parameters['_YWidth'] 	        = int(YWidth)
        
            # Generate Sref
        self._DesignParameter['_DE_M3conn_vtc'] = self._SrefElementDeclaration(_DesignObj=A19_Boundary_element_KJH._Boundary_element_KJH(_DesignParameter=None, _Name='{}:_DE_M3conn_vtc'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_DE_M3conn_vtc']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_DE_M3conn_vtc']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_DE_M3conn_vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_DE_M3conn_vtc']['_XYCoordinates'] = [[0,0]]


            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_DE_M3conn_vtc']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
                for j in range(0,len(_D_Array_Cs_NMOSNumberofGate[0])):
                            #Calculate
                                #Target_coord
                    tmp1 = self.get_param_KJH3('_D_tail_cs','_Left_side','_Cs_gate_M3_vtc_{}'.format(j)) 		
                    target_coord = tmp1[0][0][0][0]['_XY_cent']  
                                #Approaching_coord
                    tmp2 = self.get_param_KJH3('_DE_M3conn_vtc','_BoundaryElement')  
                    approaching_coord = tmp2[0][0][0]['_XY_up']   
                                #Sref coord
                    tmp3 = self.get_param_KJH3('_DE_M3conn_vtc')
                    Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord = np.round(New_Scoord,2)
                    tmpXY.append(New_Scoord)
            #Nside
            else:
                for j in range(0,len(_D_Array_Cs_NMOSNumberofGate[0])):
                            #Calculate
                                #Target_coord
                    tmp1 = self.get_param_KJH3('_D_tail_cs','_Right_side','_Cs_gate_M3_vtc_{}'.format(j)) 			
                    target_coord = tmp1[0][0][0][0]['_XY_cent']
                                #Approaching_coord
                    tmp2 = self.get_param_KJH3('_DE_M3conn_vtc','_BoundaryElement')  
                    approaching_coord = tmp2[0][0][0]['_XY_up']
                                #Sref coord
                    tmp3 = self.get_param_KJH3('_DE_M3conn_vtc')
                    Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord = np.round(New_Scoord,2)
                    tmpXY.append(New_Scoord)
                
                #Define
        self._DesignParameter['_DE_M3conn_vtc']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### F_Building_block: Pbias_cs
            #Pre-defined
        F_Building_block_y_distance = 300
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(F04_routing._routing._ParametersForDesignCalculation)
        _Caculation_Parameters['_Cs_PMOSNumberofGate'] 		= _F_Cs_PMOSNumberofGate
        _Caculation_Parameters['_Cs_PMOSChannelWidth'] 	    = _F_Cs_PMOSChannelWidth
        _Caculation_Parameters['_Cs_PMOSChannellength'] 	= _F_Cs_PMOSChannellength
        _Caculation_Parameters['_Cs_GateSpacing'] 		    = _F_Cs_GateSpacing
        _Caculation_Parameters['_Cs_SDWidth'] 	            = _F_Cs_SDWidth
        _Caculation_Parameters['_Cs_XVT']                   = _F_Cs_XVT
        _Caculation_Parameters['_Cs_PCCrit']                = _F_Cs_PCCrit

        _Caculation_Parameters['_Cs_PMOSDummy_length'] 		= _F_Cs_PMOSDummy_length
        _Caculation_Parameters['_Cs_PMOSDummy_placement'] 	= _F_Cs_PMOSDummy_placement
        
        _Caculation_Parameters['_Sw_PMOSNumberofGate'] 		= _F_Sw_PMOSNumberofGate
        _Caculation_Parameters['_Sw_PMOSChannelWidth'] 	    = _F_Sw_PMOSChannelWidth
        _Caculation_Parameters['_Sw_PMOSChannellength'] 	= _F_Sw_PMOSChannellength
        _Caculation_Parameters['_Sw_GateSpacing'] 		    = _F_Sw_GateSpacing
        _Caculation_Parameters['_Sw_SDWidth'] 	            = _F_Sw_SDWidth
        _Caculation_Parameters['_Sw_XVT'] 		            = _F_Sw_XVT
        _Caculation_Parameters['_Sw_PCCrit'] 		        = _F_Sw_PCCrit

        _Caculation_Parameters['_Sw_PMOSDummy_length'] 		= _F_Sw_PMOSDummy_length
        _Caculation_Parameters['_Sw_PMOSDummy_placement'] 	= _F_Sw_PMOSDummy_placement

        _Caculation_Parameters['_NumCont'] 	= _F_NumCont
        _Caculation_Parameters['_right_margin'] 		    = _F_right_margin
        _Caculation_Parameters['_left_margin'] 	            = _F_left_margin
        _Caculation_Parameters['_up_margin'] 		        = _F_up_margin
        _Caculation_Parameters['_down_margin'] 		        = _F_down_margin

        _Caculation_Parameters['_Array_size'] 		        = _F_Array_size

        _Caculation_Parameters['_Pbias_M4_hrz_width'] 		= _F_Pbias_M4_hrz_width
        _Caculation_Parameters['_Pbias_M3_vtc_width'] 		= _F_Pbias_M3_vtc_width

        _Caculation_Parameters['_Nbias_M3_vtc_width'] 		= _F_Nbias_M3_vtc_width

            # Generate Sref
        self._DesignParameter['_F_Pbias_Cs'] = self._SrefElementDeclaration(_DesignObj=F04_routing._routing(_DesignParameter=None, _Name='{}:_F_Pbias_Cs'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_F_Pbias_Cs']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_F_Pbias_Cs']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_F_Pbias_Cs']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_F_Pbias_Cs']['_XYCoordinates'] = [[0,0]]

        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_F_Pbias_Cs']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Right','_BoundaryElement')
        tmp2_2 =self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Left','_BoundaryElement')
        target_coordx = 0.5 * ( tmp2_1[0][0][0][0][0]['_XY_right'][0] + tmp2_2[0][0][0][0][0]['_XY_left'][0] )
                    #y
        tmp2_3 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Pbodyring','_ExtenMet1Layer_Bottom','_BoundaryElement')
        target_coordy = tmp2_3[0][0][0][0][0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
                    #x
        tmp2_1 =self.get_param_KJH3('_F_Pbias_Cs','_Placement','_Unit_row0_column0','_Unit','_Nbodyring','_ExtenMet1Layer_Left')
        tmp2_2 =self.get_param_KJH3('_F_Pbias_Cs','_Placement','_Unit_row0_column{}'.format(_F_Array_size[1]-1),'_Unit','_Nbodyring','_ExtenMet1Layer_Right')

        approaching_coordx = 0.5 * ( tmp2_1[0][0][0][0][0][0][0]['_XY_left'][0] + tmp2_2[0][0][0][0][0][0][0]['_XY_right'][0] )
                    #y
        tmp2_3 =self.get_param_KJH3('_F_Pbias_Cs','_Placement','_Unit_row0_column0','_Unit','_Nbodyring','_ExtenMet1Layer_Top')
        approaching_coordy = tmp2_3[0][0][0][0][0][0][0]['_XY_up'][1]
            
        approaching_coord = [approaching_coordx,approaching_coordy]
              
                #Sref coord
        tmp3 = self.get_param_KJH3('_F_Pbias_Cs')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - E_Building_block_y_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_F_Pbias_Cs']['_XYCoordinates'] = tmpXY


            ## ################################################################################################################### E_Building_block -- F_Building_block: M4 connection
                ## ##################################################################################################### E_Building_block -- F_Building_block: M4 connection vtc
        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Nbias','_Port1_ViaM1M4','_ViaM3M4','_Met4Layer')
        tmp2 = self.get_param_KJH3('_F_Pbias_Cs','_Nbias_m4_hrz')
        YWidth = abs( tmp1[0][0][0][0][0][0]['_XY_cent'][1] - tmp2[0][0][0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Nbias','_Port1_ViaM1M4','_ViaM3M4','_Met4Layer')
        XWidth= tmp3[0][0][0][0][0][0]['_Xwidth']
            
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A19_Boundary_element_KJH._Boundary_element_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layermapping'] 	= 'METAL4'
        _Caculation_Parameters['_XWidth'] 		    = int(XWidth)
        _Caculation_Parameters['_YWidth'] 	        = int(YWidth)
        
            # Generate Sref
        self._DesignParameter['_EF_M4conn_vtc'] = self._SrefElementDeclaration(_DesignObj=A19_Boundary_element_KJH._Boundary_element_KJH(_DesignParameter=None, _Name='{}:_EF_M4conn_vtc'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_EF_M4conn_vtc']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_EF_M4conn_vtc']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_EF_M4conn_vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_EF_M4conn_vtc']['_XYCoordinates'] = [[0,0]]


            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_EF_M4conn_vtc']['_XYCoordinates'] = [[0,0]]
        

                #Calculate
                    #Target_coord
        tmp1 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Nbias','_Port1_ViaM1M4','_ViaM3M4','_Met4Layer')	
        target_coord = tmp1[0][0][0][0][0][0]['_XY_cent']  
                    #Approaching_coord
        tmp2 = self.get_param_KJH3('_EF_M4conn_vtc','_BoundaryElement')  
        approaching_coord = tmp2[0][0][0]['_XY_up']   
                    #Sref coord
        tmp3 = self.get_param_KJH3('_EF_M4conn_vtc')
        Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)

                
                #Define
        self._DesignParameter['_EF_M4conn_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### E_Building_block -- F_Building_block: M4 connection hrz
        #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_EF_M4conn_hrz'] = self._PathElementDeclaration(          
                                                                                    _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                    _XYCoordinates=[],
                                                                                    _Width=None,
                                                                                )

        #P1--P2 Width
        tmp1 = self.get_param_KJH3('_F_Pbias_Cs','_Nbias_m4_hrz')
        self._DesignParameter['_EF_M4conn_hrz']['_Width'] = tmp1[0][0][0]['_Ywidth']
        
        tmpXY = []
        #P1--P2 coordiantes
        tmp2 = self.get_param_KJH3('_F_Pbias_Cs','_Nbias_m4_hrz')
        tmp3 = self.get_param_KJH3('_E_Ncap_for_Nbias','_Nbias','_Port1_ViaM1M4','_ViaM3M4','_Met4Layer')
        
            #P1 calculation
                #most left
        if tmp2[0][0][0]['_XY_left'][0] > tmp3[0][0][0][0][0][0]['_XY_left'][0]:
            mostleft = tmp3[0][0][0][0][0][0]['_XY_left'][0]
        else:
            mostleft = tmp2[0][0][0]['_XY_left'][0]
        P1 = [mostleft,tmp2[0][0][0]['_XY_cent'][1]]
        
            #P2 calculation
                #most right
        if tmp2[0][0][0]['_XY_right'][0] > tmp3[0][0][0][0][0][0]['_XY_right'][0]:
            mostright = tmp2[0][0][0]['_XY_right'][0]
        else:
            mostright = tmp3[0][0][0][0][0][0]['_XY_right'][0]

        P2 = [mostright,tmp2[0][0][0]['_XY_cent'][1]]
            #P1_P2
        P1_P2 = [P1,P2]
        tmpXY.append(P1_P2)
            #Cal tmpXY
        self._DesignParameter['_EF_M4conn_hrz']['_XYCoordinates'] = tmpXY
        
       
    
        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
