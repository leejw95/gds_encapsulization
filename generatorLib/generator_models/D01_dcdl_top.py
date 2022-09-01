############################################################################################################################################################ BASIC Modules
from KJH91_Projects.Project_DCDL.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_DCDL.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_DCDL.Library_and_Engine import DRC

import copy
import math
import numpy as np

from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A00_NMOSWithDummy_v2
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A01_NSubRing
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A02_PMOSWithDummy
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A03_PSubRing
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A04_NbodyContact
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A05_PbodyContact
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A06_ViaStack
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A07_ViaPoly2Met1
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A08_ViaMet12Met2
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A09_ViaMet22Met3
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A10_ViaMet32Met4
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A11_ViaMet42Met5
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A12_ViaMet52Met6
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A13_ViaMet62Met7
from KJH91_Projects.Project_DCDL.Layoutgen_code.A_Building_cells import A14_ViaMet72Met8

#from SthPack import CoordCalc

from KJH91_Projects.Project_DCDL.Layoutgen_code.B_Building_block import B18_Driver_v1
from KJH91_Projects.Project_DCDL.Layoutgen_code.C_Building_block import C01_cap_array_v4
from KJH91_Projects.Project_DCDL.Layoutgen_code.D_Building_block import D00_dcdl_v6

############################################################################################################################################################ Class_HEADER
class _DCDL_top(StickDiagram_KJH0._StickDiagram_KJH): 

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                           )

    #Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name='_DCDL'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                        )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,

#Driver
    #Driver1
        #Driver1 common
_Driver1_GateLength                     = 30,
_Driver1_XVT                            = 'SLVT',
        #No switch stacked driver
_Driver1_NoSwStack_GateFinger           = 3,
_Driver1_NoSwStack_Pmos_GateWidth       = 800,
_Driver1_NoSwStack_Nmos_GateWidth       = 400,
        #Switch stacked driver
_Driver1_SwStack_GateFinger_Array       = [4,3,2,1],
_Driver1_SwStack_Pmos_GateWidth_Array   = [700, 700, 600, 500],
_Driver1_SwStack_Nmos_GateWidth_Array   = [350, 350, 300, 250],
    #Driver2
_Driver2_GateLength                     = 30 ,
_Driver2_XVT                            = 'SLVT',
_Driver2_SwStack_GateFinger_Array       = [8,7,6,5,4],
_Driver2_SwStack_Pmos_GateWidth_Array   = [800, 800, 800, 500, 500],
_Driver2_SwStack_Nmos_GateWidth_Array   = [400, 400, 400, 250, 250],
    #Driver3
_Driver3_GateLength                     = 60,
_Driver3_XVT                            = 'SLVT',
_Driver3_NoSwStack_GateFinger           = 30,
_Driver3_NoSwStack_Pmos_GateWidth       = 1500,
_Driver3_NoSwStack_Nmos_GateWidth       = 750,

    #Driver Guardring
_Pside_Nbody_Length                     = 2000,
_Nside_Pbody_Length                     = 2000,
_PNside_Nbody_Contact                   = 10,

    #Driver Powerline
_Pside_M4_Powerline_Width               = 1000,
_Nside_M4_Powerline_Width               = 1000,

    #Driver IN/OUT
_Distance_Between_Pside_and_Nside       = 2200,
_Driver1_Input_M1_Width                 = 100,
_Driver1_Output_M2_Width                = 100,
_Driver2_Input_M1_Width                 = 100,
_Driver2_Output_M2_Width                = 100,
_Driver3_Input_M1_Width                 = 100,
_Driver3_Output_M2_Width                = 100,

#Capbank
    #capcell
_Capcell_TransGate_Finger               = 5,
_Capcell_Cap_Finger                     = 3,
_Capcell_TransGate_Pmos_GateWidth       = 500,
_Capcell_TransGate_Nmos_GateWidth       = 250,
_Capcell_TransGate_GateLength           = 30,
_Capcell_XVT                            = 'SLVT',
_Capcell_Cap_Nmos_GateWidth             = 800,
_Capcell_Cap_Pmos_GateWidth             = 400,
_Capcell_Cap_GateLength                 = 80,
    #capbank size
_Capbank1_Nside_ArraySize               = [3,8],
_Capbank1_Pside_ArraySize               = [2,5],
_Capbank2_Nside_ArraySize               = [4,4],
_Capbank2_Pside_ArraySize               = [1,15] ,
    #guardring
_Capbank_PbodyNbody_Contact             = 5,


                                 ):

################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        #Load DRC library
        _DRCobj = DRC.DRC()

        #Define _name
        _Name = self._DesignParameter['_Name']['_Name']



        ############################################################################################################################################################ Constraints


        # #### Pmos side

        #Pmos side에서 가장 왼쪽 vtc Nbody
        _PMOSPOWER_NbodyContact_1_Length  = _Pside_Nbody_Length,
        _PMOSPOWER_NbodyContact_1_Contact = _PNside_Nbody_Contact,
        _PMOSPOWER_NbodyContact_1_Vert    = 1, #Fixed

        #Pmos side에서 1번째 driver
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_default    = _Driver1_NoSwStack_GateFinger,
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_default    = _Driver1_NoSwStack_Pmos_GateWidth, 
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_default   = _Driver1_GateLength,
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_stack_bank = _Driver1_SwStack_GateFinger_Array, 
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_stack_bank = _Driver1_SwStack_Pmos_GateWidth_Array,  #큰거부터 writing
            #Make array
        tmp =[]
        for i in range(0,len(_Driver1_SwStack_GateFinger_Array)):
            tmp.append(_Driver1_GateLength)
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_stack_bank= tmp,
        
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSDummy                   = True,
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_XVT                         = _Driver1_XVT,
        _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PCCrit                      = True, #fixed

        #Pmos side에서 가장 왼쪽에서 2번째 vtc Nbody
        _PMOSPOWER_NbodyContact_2_Length  = _Pside_Nbody_Length,
        _PMOSPOWER_NbodyContact_2_Contact = _PNside_Nbody_Contact,
        _PMOSPOWER_NbodyContact_2_Vert    = 1, #Fixed

        #Pmos side에서 2번째 driver
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSNumberofGate_stack_bank    = _Driver2_SwStack_GateFinger_Array, 
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannelWidth_stack_bank    = _Driver2_SwStack_Pmos_GateWidth_Array,
            #Make array
        tmp1 =[]
        for i in range(0,len(_Driver2_SwStack_GateFinger_Array)):
            tmp1.append(_Driver2_GateLength)            
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannellength_stack_bank   = tmp1, 
        
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSDummy 				     = True,
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_XVT							 = _Driver2_XVT,
        _PMOSPOWER_PMOS_STACK_ONLY_BANK_PCCrit						 = True,

        #Pmos side에서 가장 왼쪽에서 3번째 vtc Nbody
        _PMOSPOWER_NbodyContact_3_Length  = _Pside_Nbody_Length,
        _PMOSPOWER_NbodyContact_3_Contact = _PNside_Nbody_Contact,
        _PMOSPOWER_NbodyContact_3_Vert    = 1,

        #Pmos side에서 가장 마지막 driver
        _PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSNumberofGate_default   = _Driver3_NoSwStack_GateFinger,
        _PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannelWidth_default   = _Driver3_NoSwStack_Pmos_GateWidth,
        _PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannellength_default  = _Driver3_GateLength,
        _PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSDummy                  = True,
        _PMOSPOWER_PMOS_DEFAULT_ONLY_XVT                        =_Driver3_XVT,
        _PMOSPOWER_PMOS_DEFAULT_ONLY_PCCrit                     =True,

        #Pmos side에서 가장 오른쪽에 Nbody
        _PMOSPOWER_NbodyContact_4_Length  = _Pside_Nbody_Length,
        _PMOSPOWER_NbodyContact_4_Contact = _PNside_Nbody_Contact,
        _PMOSPOWER_NbodyContact_4_Vert    = 1,

        #Pmos side에서 아래 쪽으로 vtc Nbody를 연결하는 PP의 굵기
        _PMOSPOWER_RX_and_PP_on_the_top_Width = 100, #Fix

        #Pmos side에서의 M4 Power의 굵기
        _PMOSPOWER_PMOS_M4_Power_Width = _Pside_M4_Powerline_Width,

        
        
        
        # #### Nmos side
        
        #nmos side에서 가장 왼쪽 vtc pbody
        _NMOSPOWER_PbodyContact_1_Length  = _Nside_Pbody_Length, 
        _NMOSPOWER_PbodyContact_1_Contact = _PNside_Nbody_Contact,
        _NMOSPOWER_PbodyContact_1_Vert    = 1, #Fixed

    
        #nmos side 1번째 driver
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_default    = _Driver1_NoSwStack_GateFinger, 
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_default    = _Driver1_NoSwStack_Nmos_GateWidth,
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_default   = _Driver1_GateLength,
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_stack_bank = _Driver1_SwStack_GateFinger_Array, 
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_stack_bank = _Driver1_SwStack_Nmos_GateWidth_Array,
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_stack_bank= _PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_stack_bank
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSDummy                   = True,
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_XVT                         = _Driver1_XVT,
        _NMOSPOWER_NMOS_STACK_CONTROL_PIN_PCCrit                      = True,

        #nmos side에서 2번째 vtc pbody
        _NMOSPOWER_PbodyContact_2_Length  = _Nside_Pbody_Length, # 2000
        _NMOSPOWER_PbodyContact_2_Contact = _PNside_Nbody_Contact,
        _NMOSPOWER_PbodyContact_2_Vert    = 1,

        #nmos side 2번째 driver
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSNumberofGate_stack_bank     = _Driver2_SwStack_GateFinger_Array,
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannelWidth_stack_bank     = _Driver2_SwStack_Nmos_GateWidth_Array,
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannellength_stack_bank    = _PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannellength_stack_bank,
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSDummy 				        = True,
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_XVT							    = _Driver2_XVT,
        _NMOSPOWER_NMOS_STACK_ONLY_BANK_PCCrit						    = True,

        #nmos side에서 3번째 vtc pbody
        _NMOSPOWER_PbodyContact_3_Length  = _Nside_Pbody_Length, #2000
        _NMOSPOWER_PbodyContact_3_Contact = _PNside_Nbody_Contact,
        _NMOSPOWER_PbodyContact_3_Vert    = 1,

        #nmos side에서 3번째 driver
        _NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSNumberofGate_default  =_Driver3_NoSwStack_GateFinger, #10
        _NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannelWidth_default  =_Driver3_NoSwStack_Nmos_GateWidth,
        _NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannellength_default =_Driver3_GateLength,
        _NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSDummy                  = True,
        _NMOSPOWER_NMOS_DEFAULT_ONLY_XVT                        =_Driver3_XVT,
        _NMOSPOWER_NMOS_DEFAULT_ONLY_PCCrit                     =True,

        #nmos side에서 4번째 vtc pbody
        _NMOSPOWER_PbodyContact_4_Length  = _Nside_Pbody_Length, #2000
        _NMOSPOWER_PbodyContact_4_Contact = _PNside_Nbody_Contact,
        _NMOSPOWER_PbodyContact_4_Vert    = 1,

        #nmos side에서 vtc pbody 잇는 hrz pp 두께
        _NMOSPOWER_RX_and_PP_on_the_top_Width = 100,

        #nmos side에서 M4 power 두께
        _NMOSPOWER_NMOS_M4_Power_Width = _Nside_M4_Powerline_Width,



        # ##### Driver
        
        #Pside와 Nside 사이 거리: Input M1 metal ylength로 정의됨
        _INOUT_Metal_Ywidth                         = _Distance_Between_Pside_and_Nside,
        
        #첫번째 driver에서 input M1 metal의 두께
        _Input_M1_NMOS_STACK_CONTROL_PIN_Xwidth     = _Driver1_Input_M1_Width,
        
        #두번째 driver에서 input M1 metal의 두께
        _Input_M1_NMOS_STACK_ONLY_BANK_Xwidth       = _Driver2_Input_M1_Width,
        
        #세번째 driver에서 input M1 metal의 두께
        _Input_M1_NMOS_DEFAULT_ONLY_Xwidth          = _Driver3_Input_M1_Width,
        
        #첫번째 driver에서 output M2 metal의 두께
        _Output_M2_NMOS_STACK_CONTROL_PIN_Xwidth    = _Driver1_Output_M2_Width,
        
        #두번째 driver에서 output M2 metal의 두께
        _Output_M2_NMOS_STACK_ONLY_BANK_Xwidth      = _Driver2_Output_M2_Width,
        
        #세번째 driver에서 output M2 metal의 두께
        _Output_M2_NMOS_DEFAULT_ONLY_Xwidth         = _Driver3_Output_M2_Width,





        # ##### Nside 에서 1번째 driver에 연결되는 Capbank에서

        #Cap cell에 대하여
        _Capbank1_Nside_dcdl_cap_tg_pmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank1_Nside_dcdl_cap_tg_nmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank1_Nside_dcdl_cap_cap_gate           =_Capcell_Cap_Finger,
        _Capbank1_Nside_dcdl_cap_tg_gate_spacing    =None,
        _Capbank1_Nside_dcdl_cap_cap_gate_spacing   =None,
        _Capbank1_Nside_dcdl_cap_tg_nmos_width      =_Capcell_TransGate_Nmos_GateWidth,
        _Capbank1_Nside_dcdl_cap_tg_pmos_width      =_Capcell_TransGate_Pmos_GateWidth,
        _Capbank1_Nside_dcdl_cap_tg_length          =_Capcell_TransGate_GateLength,
        _Capbank1_Nside_dcdl_cap_tg_sdwidth         =None,
        _Capbank1_Nside_dcdl_cap_cap_sdwidth        =None,
        _Capbank1_Nside_dcdl_cap_tg_dummy           =False,
        _Capbank1_Nside_dcdl_cap_cap_dummy          =False,
        _Capbank1_Nside_dcdl_cap_tg_xvt             =_Capcell_XVT,
        _Capbank1_Nside_dcdl_cap_cap_xvt            =_Capcell_XVT,
        _Capbank1_Nside_dcdl_cap_tg_pmos_y          =None,
        _Capbank1_Nside_dcdl_cap_tg_nmos_y          =None,
        _Capbank1_Nside_dcdl_cap_cap_nmos_width     =_Capcell_Cap_Nmos_GateWidth,
        _Capbank1_Nside_dcdl_cap_cap_pmos_width     =_Capcell_Cap_Pmos_GateWidth,
        _Capbank1_Nside_dcdl_cap_cap_length         =_Capcell_Cap_GateLength,
        _Capbank1_Nside_dcdl_cap_cap_pmos_gate_y    =None,
        _Capbank1_Nside_dcdl_cap_cap_nmos_gate_y    =None,

        #cap array
        _Capbank1_Nside_dcdl_cap_array = _Capbank1_Nside_ArraySize,
        
        #No flip(fixed)
        _Capbank1_Nside_dcdl_cap_Pside_or_Nside = 1, #If Nside, value = 1
        
        #cap xvt to xvt xdistance
        _Capbank1_Nside_dcdl_cap_cap_to_cap_xdistance = 200, #fixed
        
        #cap xvt to powerline ydistance
        _Capbank1_Nside_dcdl_cap_cap_to_powerline_ydistance = 200, #fixed

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank1_Nside_Just_for_cal_PbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank1_Nside_Just_for_cal_PbodyCont_Length = 1500, #Fixed
            #Hrz이므로 fixed
        _Capbank1_Nside_Just_for_cal_PbodyContact_Vert = 0, #Fixed

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank1_Nside_Just_for_cal_NbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank1_Nside_Just_for_cal_NbodyCont_Length = 1500, #Fixed
            # Hrz이므로 fixed
        _Capbank1_Nside_Just_for_cal_NbodyContact_Vert = 0, #Fixed




        # ##### Pside 에서 1번째 driver에 연결되는 Capbank에서

        #Cap cell에 대하여
        _Capbank1_Pside_dcdl_cap_tg_pmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank1_Pside_dcdl_cap_tg_nmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank1_Pside_dcdl_cap_cap_gate           =_Capcell_Cap_Finger,
        _Capbank1_Pside_dcdl_cap_tg_gate_spacing    =None,
        _Capbank1_Pside_dcdl_cap_cap_gate_spacing   =None,
        _Capbank1_Pside_dcdl_cap_tg_nmos_width      =_Capcell_TransGate_Nmos_GateWidth,
        _Capbank1_Pside_dcdl_cap_tg_pmos_width      =_Capcell_TransGate_Pmos_GateWidth,
        _Capbank1_Pside_dcdl_cap_tg_length          =_Capcell_TransGate_GateLength,
        _Capbank1_Pside_dcdl_cap_tg_sdwidth         =None,
        _Capbank1_Pside_dcdl_cap_cap_sdwidth        =None,
        _Capbank1_Pside_dcdl_cap_tg_dummy           =False,
        _Capbank1_Pside_dcdl_cap_cap_dummy          =False,
        _Capbank1_Pside_dcdl_cap_tg_xvt             =_Capcell_XVT,
        _Capbank1_Pside_dcdl_cap_cap_xvt            =_Capcell_XVT,
        _Capbank1_Pside_dcdl_cap_tg_pmos_y          =None,
        _Capbank1_Pside_dcdl_cap_tg_nmos_y          =None,
        _Capbank1_Pside_dcdl_cap_cap_nmos_width     =_Capcell_Cap_Nmos_GateWidth,
        _Capbank1_Pside_dcdl_cap_cap_pmos_width     =_Capcell_Cap_Pmos_GateWidth,
        _Capbank1_Pside_dcdl_cap_cap_length         =_Capcell_Cap_GateLength,
        _Capbank1_Pside_dcdl_cap_cap_pmos_gate_y    =None,
        _Capbank1_Pside_dcdl_cap_cap_nmos_gate_y    =None,

        #cap array
        _Capbank1_Pside_dcdl_cap_array = _Capbank1_Pside_ArraySize,
        #No flip(fixed)
        _Capbank1_Pside_dcdl_cap_Pside_or_Nside = 0, #If Nside, value = 1          #1                        
        #cap xvt to xvt xdistance
        _Capbank1_Pside_dcdl_cap_cap_to_cap_xdistance = 200,
        #cap xvt to powerline ydistance
        _Capbank1_Pside_dcdl_cap_cap_to_powerline_ydistance = 200, #100

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank1_Pside_Just_for_cal_PbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank1_Pside_Just_for_cal_PbodyCont_Length = 1500,
            #Hrz이므로 fixed
        _Capbank1_Pside_Just_for_cal_PbodyContact_Vert = 0,

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank1_Pside_Just_for_cal_NbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank1_Pside_Just_for_cal_NbodyCont_Length = 1500,
            # Hrz이므로 fixed
        _Capbank1_Pside_Just_for_cal_NbodyContact_Vert = 0,



        # ##### Nside 에서 2번째 driver에 연결되는 Capbank에서
        #Cap cell에 대하여
        _Capbank2_Nside_dcdl_cap_tg_pmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank2_Nside_dcdl_cap_tg_nmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank2_Nside_dcdl_cap_cap_gate           =_Capcell_Cap_Finger,
        _Capbank2_Nside_dcdl_cap_tg_gate_spacing    =None,
        _Capbank2_Nside_dcdl_cap_cap_gate_spacing   =None,
        _Capbank2_Nside_dcdl_cap_tg_nmos_width      =_Capcell_TransGate_Nmos_GateWidth,
        _Capbank2_Nside_dcdl_cap_tg_pmos_width      =_Capcell_TransGate_Pmos_GateWidth,
        _Capbank2_Nside_dcdl_cap_tg_length          =_Capcell_TransGate_GateLength,
        _Capbank2_Nside_dcdl_cap_tg_sdwidth         =None,
        _Capbank2_Nside_dcdl_cap_cap_sdwidth        =None,
        _Capbank2_Nside_dcdl_cap_tg_dummy           =False,
        _Capbank2_Nside_dcdl_cap_cap_dummy          =False,
        _Capbank2_Nside_dcdl_cap_tg_xvt             =_Capcell_XVT,
        _Capbank2_Nside_dcdl_cap_cap_xvt            =_Capcell_XVT,
        _Capbank2_Nside_dcdl_cap_tg_pmos_y          =None,
        _Capbank2_Nside_dcdl_cap_tg_nmos_y          =None,
        _Capbank2_Nside_dcdl_cap_cap_nmos_width     =_Capcell_Cap_Nmos_GateWidth,
        _Capbank2_Nside_dcdl_cap_cap_pmos_width     =_Capcell_Cap_Pmos_GateWidth,
        _Capbank2_Nside_dcdl_cap_cap_length         =_Capcell_Cap_GateLength,
        _Capbank2_Nside_dcdl_cap_cap_pmos_gate_y    =None,
        _Capbank2_Nside_dcdl_cap_cap_nmos_gate_y    =None,
        
        #cap array
        _Capbank2_Nside_dcdl_cap_array = _Capbank2_Nside_ArraySize,
        #No flip(fixed)
        _Capbank2_Nside_dcdl_cap_Pside_or_Nside = 1, #If Nside, value = 1
        #cap xvt to xvt xdistance
        _Capbank2_Nside_dcdl_cap_cap_to_cap_xdistance = 200,
        #cap xvt to powerline ydistance
        _Capbank2_Nside_dcdl_cap_cap_to_powerline_ydistance = 200, #100

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank2_Nside_Just_for_cal_PbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank2_Nside_Just_for_cal_PbodyCont_Length = 1500,
            #Hrz이므로 fixed
        _Capbank2_Nside_Just_for_cal_PbodyContact_Vert = 0,

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank2_Nside_Just_for_cal_NbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank2_Nside_Just_for_cal_NbodyCont_Length = 1500,
            # Hrz이므로 fixed
        _Capbank2_Nside_Just_for_cal_NbodyContact_Vert = 0,





        # ##### Pside 에서 2번째 driver에 연결되는 Capbank에서
        #Cap cell에 대하여
        _Capbank2_Pside_dcdl_cap_tg_pmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank2_Pside_dcdl_cap_tg_nmos_gate       =_Capcell_TransGate_Finger, #5
        _Capbank2_Pside_dcdl_cap_cap_gate           =_Capcell_Cap_Finger,
        _Capbank2_Pside_dcdl_cap_tg_gate_spacing    =None,
        _Capbank2_Pside_dcdl_cap_cap_gate_spacing   =None,
        _Capbank2_Pside_dcdl_cap_tg_nmos_width      =_Capcell_TransGate_Nmos_GateWidth,
        _Capbank2_Pside_dcdl_cap_tg_pmos_width      =_Capcell_TransGate_Pmos_GateWidth,
        _Capbank2_Pside_dcdl_cap_tg_length          =_Capcell_TransGate_GateLength,
        _Capbank2_Pside_dcdl_cap_tg_sdwidth         =None,
        _Capbank2_Pside_dcdl_cap_cap_sdwidth        =None,
        _Capbank2_Pside_dcdl_cap_tg_dummy           =False,
        _Capbank2_Pside_dcdl_cap_cap_dummy          =False,
        _Capbank2_Pside_dcdl_cap_tg_xvt             =_Capcell_XVT,
        _Capbank2_Pside_dcdl_cap_cap_xvt            =_Capcell_XVT,
        _Capbank2_Pside_dcdl_cap_tg_pmos_y          =None,
        _Capbank2_Pside_dcdl_cap_tg_nmos_y          =None,
        _Capbank2_Pside_dcdl_cap_cap_nmos_width     =_Capcell_Cap_Nmos_GateWidth,
        _Capbank2_Pside_dcdl_cap_cap_pmos_width     =_Capcell_Cap_Pmos_GateWidth,
        _Capbank2_Pside_dcdl_cap_cap_length         =_Capcell_Cap_GateLength,
        _Capbank2_Pside_dcdl_cap_cap_pmos_gate_y    =None,
        _Capbank2_Pside_dcdl_cap_cap_nmos_gate_y    =None,
        
        #cap array
        _Capbank2_Pside_dcdl_cap_array = _Capbank2_Pside_ArraySize,
        #No flip(fixed)
        _Capbank2_Pside_dcdl_cap_Pside_or_Nside = 0, #If Nside, value = 1   #1
        #cap xvt to xvt xdistance
        _Capbank2_Pside_dcdl_cap_cap_to_cap_xdistance = 200,
        #cap xvt to powerline ydistance
        _Capbank2_Pside_dcdl_cap_cap_to_powerline_ydistance = 200, #100
        
        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank2_Pside_Just_for_cal_PbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank2_Pside_Just_for_cal_PbodyCont_Length = 1000,
            #Hrz이므로 fixed
        _Capbank2_Pside_Just_for_cal_PbodyContact_Vert = 0,

        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Capbank2_Pside_Just_for_cal_NbodyContCount_of_Width = _Capbank_PbodyNbody_Contact,
            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Capbank2_Pside_Just_for_cal_NbodyCont_Length = 1000,
            # Hrz이므로 fixed
        _Capbank2_Pside_Just_for_cal_NbodyContact_Vert = 0,




        #Nside에서 capbank에서 왼쪽 gruardring 두께관련된 contact 갯수
        #Nside_Side_Guard_bodyContCount_of_Width = _Capbank_Side_PbodyNbody_Contact,
        Nside_Side_Guard_bodyContCount_of_Width = 2,
        
        #Nside에서 capbank의 가장 끝 capcell까지 거리 (Nw또는OD부터 Xvt까지 거리)
        Nside_Left_Side_Guard_to_Capbank_distance = 200,
        
        #Pside에서 capbank에서 왼쪽 gruardring 두께관련된 contact 갯수
        #Pside_Side_Guard_bodyContCount_of_Width = _Capbank_Side_PbodyNbody_Contact,
        Pside_Side_Guard_bodyContCount_of_Width = 2,
        
        #Pside에서 capbank의 가장 끝 capcell까지 거리 (Nw또는OD부터 Xvt까지 거리)
        Pside_Left_Side_Guard_to_Capbank_distance = 200,
                                
        


        ############################################################################################################################################################ Sref_generation:D00_DCDLv5
        #Driver
        _Caculation_Parameters = copy.deepcopy(D00_dcdl_v6._DCDL._ParametersForDesignCalculation)
                                #Pmos side에서 가장 왼쪽 vtc Nbody
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_1_Length']  								=_PMOSPOWER_NbodyContact_1_Length[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_1_Contact']  								=_PMOSPOWER_NbodyContact_1_Contact[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_1_Vert']  									=_PMOSPOWER_NbodyContact_1_Vert[0]
        
                                #Pmos side에서 1번째 driver
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_default']  		=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_default']  		=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_default']  		=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_stack_bank']  	=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSNumberofGate_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_stack_bank']  	=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannelWidth_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_stack_bank']  	=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSChannellength_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSDummy']  						=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PMOSDummy[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_XVT']  							=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_XVT[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PCCrit']  						=_PMOSPOWER_PMOS_STACK_CONTROL_PIN_PCCrit[0]
        
                        #Pmos side에서 가장 왼쪽에서 2번째 vtc Nbody
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_2_Length']  								=_PMOSPOWER_NbodyContact_2_Length[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_2_Contact']  								=_PMOSPOWER_NbodyContact_2_Contact[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_2_Vert']  									=_PMOSPOWER_NbodyContact_2_Vert[0]
        
                        #Pmos side에서 2번째 driver
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSNumberofGate_stack_bank']  		=_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSNumberofGate_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannelWidth_stack_bank']  		=_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannelWidth_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannellength_stack_bank']  	=_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSChannellength_stack_bank[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSDummy']  						=_PMOSPOWER_PMOS_STACK_ONLY_BANK_PMOSDummy[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_XVT']  								=_PMOSPOWER_PMOS_STACK_ONLY_BANK_XVT[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_STACK_ONLY_BANK_PCCrit']  							=_PMOSPOWER_PMOS_STACK_ONLY_BANK_PCCrit[0]
        
                        #Pmos side에서 가장 왼쪽에서 3번째 vtc Nbody
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_3_Length']  								=_PMOSPOWER_NbodyContact_3_Length[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_3_Contact']  								=_PMOSPOWER_NbodyContact_3_Contact[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_3_Vert']  									=_PMOSPOWER_NbodyContact_3_Vert[0]
        
                        #Pmos side에서 가장 마지막 driver
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSNumberofGate_default']  			=_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSNumberofGate_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannelWidth_default']  			=_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannelWidth_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannellength_default']  			=_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSChannellength_default[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSDummy']  							=_PMOSPOWER_PMOS_DEFAULT_ONLY_PMOSDummy[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_XVT']  								=_PMOSPOWER_PMOS_DEFAULT_ONLY_XVT[0]
        _Caculation_Parameters['_PMOSPOWER_PMOS_DEFAULT_ONLY_PCCrit']  								=_PMOSPOWER_PMOS_DEFAULT_ONLY_PCCrit[0]
        
                        #Pmos side에서 가장 오른쪽에 Nbody
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_4_Length']  								=_PMOSPOWER_NbodyContact_4_Length[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_4_Contact']  								=_PMOSPOWER_NbodyContact_4_Contact[0]
        _Caculation_Parameters['_PMOSPOWER_NbodyContact_4_Vert']  									=_PMOSPOWER_NbodyContact_4_Vert[0]
        
                        #Pmos side에서 아래 쪽으로 vtc Nbody를 연결하는 PP의 굵기
        _Caculation_Parameters['_PMOSPOWER_RX_and_PP_on_the_top_Width']  							=_PMOSPOWER_RX_and_PP_on_the_top_Width[0]
        
                        #Pmos side에서의 M4 Power의 굵기
        _Caculation_Parameters['_PMOSPOWER_PMOS_M4_Power_Width']  									=_PMOSPOWER_PMOS_M4_Power_Width[0]
        
                        # #### Nmos side
                        #nmos side에서 가장 왼쪽 vtc pbody
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  								=_NMOSPOWER_PbodyContact_1_Length[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Contact']  								=_NMOSPOWER_PbodyContact_1_Contact[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Vert']  									=_NMOSPOWER_PbodyContact_1_Vert[0]
        
                        #nmos side 1번째 driver
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_default']  		=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_default']  		=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_default']  		=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_stack_bank']  	=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSNumberofGate_stack_bank[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_stack_bank']  	=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannelWidth_stack_bank[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_stack_bank']  	=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSChannellength_stack_bank[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSDummy']  						=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_NMOSDummy[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_XVT']  							=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_XVT[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_CONTROL_PIN_PCCrit']  						=_NMOSPOWER_NMOS_STACK_CONTROL_PIN_PCCrit[0]
        
                        #nmos side에서 2번째 vtc pbody
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_2_Length']  								=_NMOSPOWER_PbodyContact_2_Length[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_2_Contact']  								=_NMOSPOWER_PbodyContact_2_Contact[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_2_Vert']  									=_NMOSPOWER_PbodyContact_2_Vert[0]
        
                        #nmos side 2번째 driver
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSNumberofGate_stack_bank']  		=_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSNumberofGate_stack_bank[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannelWidth_stack_bank']  		=_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannelWidth_stack_bank[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannellength_stack_bank']  	=_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSChannellength_stack_bank[0][0] #------------------------
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSDummy']  						=_NMOSPOWER_NMOS_STACK_ONLY_BANK_NMOSDummy[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_XVT']  								=_NMOSPOWER_NMOS_STACK_ONLY_BANK_XVT[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_STACK_ONLY_BANK_PCCrit']  							=_NMOSPOWER_NMOS_STACK_ONLY_BANK_PCCrit[0]
        
                        #nmos side에서 3번째 vtc pbody
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_3_Length']  								=_NMOSPOWER_PbodyContact_3_Length[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_3_Contact']  								=_NMOSPOWER_PbodyContact_3_Contact[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_3_Vert']  									=_NMOSPOWER_PbodyContact_3_Vert[0]
        
                        #nmos side에서 3번째 driver
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSNumberofGate_default']  			=_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSNumberofGate_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannelWidth_default']  			=_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannelWidth_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannellength_default']  			=_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSChannellength_default[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSDummy']  							=_NMOSPOWER_NMOS_DEFAULT_ONLY_NMOSDummy[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_XVT']  								=_NMOSPOWER_NMOS_DEFAULT_ONLY_XVT[0]
        _Caculation_Parameters['_NMOSPOWER_NMOS_DEFAULT_ONLY_PCCrit']  								=_NMOSPOWER_NMOS_DEFAULT_ONLY_PCCrit[0]
        
                        #nmos side에서 4번째 vtc pbody
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_4_Length']  								=_NMOSPOWER_PbodyContact_4_Length[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_4_Contact']  								=_NMOSPOWER_PbodyContact_4_Contact[0]
        _Caculation_Parameters['_NMOSPOWER_PbodyContact_4_Vert']  									=_NMOSPOWER_PbodyContact_4_Vert[0]
        
                        #nmos side에서 vtc pbody 잇는 hrz pp 두께
        _Caculation_Parameters['_NMOSPOWER_RX_and_PP_on_the_top_Width']  							=_NMOSPOWER_RX_and_PP_on_the_top_Width[0]
        
                        #nmos side에서 M4 power 두께
        _Caculation_Parameters['_NMOSPOWER_NMOS_M4_Power_Width']  									=_NMOSPOWER_NMOS_M4_Power_Width[0]
        
                        # ##### Driver
                        #Pside와 Nside 사이 거리: Input M1 metal ylength로 정의됨
        _Caculation_Parameters['_INOUT_Metal_Ywidth']  												=_INOUT_Metal_Ywidth[0]
        
                        #첫번째 driver에서 input M1 metal의 두께
        _Caculation_Parameters['_Input_M1_NMOS_STACK_CONTROL_PIN_Xwidth']  							=_Input_M1_NMOS_STACK_CONTROL_PIN_Xwidth[0]
        
                        #두번째 driver에서 input M1 metal의 두께
        _Caculation_Parameters['_Input_M1_NMOS_STACK_ONLY_BANK_Xwidth']  							=_Input_M1_NMOS_STACK_ONLY_BANK_Xwidth[0]
        
                        #세번째 driver에서 input M1 metal의 두께
        _Caculation_Parameters['_Input_M1_NMOS_DEFAULT_ONLY_Xwidth']  								=_Input_M1_NMOS_DEFAULT_ONLY_Xwidth[0]
        
                        #첫번째 driver에서 output M2 metal의 두께
        _Caculation_Parameters['_Output_M2_NMOS_STACK_CONTROL_PIN_Xwidth']  						=_Output_M2_NMOS_STACK_CONTROL_PIN_Xwidth[0]
        
                        #두번째 driver에서 output M2 metal의 두께
        _Caculation_Parameters['_Output_M2_NMOS_STACK_ONLY_BANK_Xwidth']  							=_Output_M2_NMOS_STACK_ONLY_BANK_Xwidth[0]
        
                        #세번째 driver에서 output M2 metal의 두께
        _Caculation_Parameters['_Output_M2_NMOS_DEFAULT_ONLY_Xwidth']  								=_Output_M2_NMOS_DEFAULT_ONLY_Xwidth[0]
  
  
                        # ##### Nside 에서 1번째 driver에 연결되는 Capbank에서
                        #Cap cell에 대하여
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_pmos_gate']  				= _Capbank1_Nside_dcdl_cap_tg_pmos_gate[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_nmos_gate']  				= _Capbank1_Nside_dcdl_cap_tg_nmos_gate[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_gate']  					= _Capbank1_Nside_dcdl_cap_cap_gate[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_gate_spacing']  			= _Capbank1_Nside_dcdl_cap_tg_gate_spacing[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_gate_spacing']  			= _Capbank1_Nside_dcdl_cap_cap_gate_spacing[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_nmos_width']  				= _Capbank1_Nside_dcdl_cap_tg_nmos_width[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_pmos_width']  				= _Capbank1_Nside_dcdl_cap_tg_pmos_width[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_length']  					= _Capbank1_Nside_dcdl_cap_tg_length[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_sdwidth']  					= _Capbank1_Nside_dcdl_cap_tg_sdwidth[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_sdwidth']  				= _Capbank1_Nside_dcdl_cap_cap_sdwidth[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_dummy']  					= _Capbank1_Nside_dcdl_cap_tg_dummy[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_dummy']  					= _Capbank1_Nside_dcdl_cap_cap_dummy[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_xvt']  						= _Capbank1_Nside_dcdl_cap_tg_xvt[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_xvt']  					= _Capbank1_Nside_dcdl_cap_cap_xvt[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_pmos_y']  					= _Capbank1_Nside_dcdl_cap_tg_pmos_y[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_tg_nmos_y']  					= _Capbank1_Nside_dcdl_cap_tg_nmos_y[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_nmos_width']  				= _Capbank1_Nside_dcdl_cap_cap_nmos_width[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_pmos_width']  				= _Capbank1_Nside_dcdl_cap_cap_pmos_width[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_length']  					= _Capbank1_Nside_dcdl_cap_cap_length[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_pmos_gate_y']  			= _Capbank1_Nside_dcdl_cap_cap_pmos_gate_y[0]
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_nmos_gate_y']  			= _Capbank1_Nside_dcdl_cap_cap_nmos_gate_y[0]
        
                        #cap array
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_array']  						= _Capbank1_Nside_dcdl_cap_array[0]
        
                        #No flip(fixed)
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_Pside_or_Nside']  				= _Capbank1_Nside_dcdl_cap_Pside_or_Nside[0]
        
                        #cap xvt to xvt xdistance
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_to_cap_xdistance'] 		= _Capbank1_Nside_dcdl_cap_cap_to_cap_xdistance[0]
        
                        #cap xvt to powerline ydistance
        _Caculation_Parameters['_Capbank1_Nside_dcdl_cap_cap_to_powerline_ydistance'] 	= _Capbank1_Nside_dcdl_cap_cap_to_powerline_ydistance[0]
        
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
                            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_PbodyContCount_of_Width']  = _Capbank1_Nside_Just_for_cal_PbodyContCount_of_Width[0]
        
                            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_PbodyCont_Length']  		= _Capbank1_Nside_Just_for_cal_PbodyCont_Length[0]
                            #Hrz이므로 fixed
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_PbodyContact_Vert']  		= _Capbank1_Nside_Just_for_cal_PbodyContact_Vert[0]
        
                                # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
                            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_NbodyContCount_of_Width']  = _Capbank1_Nside_Just_for_cal_NbodyContCount_of_Width[0]
                            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_NbodyCont_Length']  		= _Capbank1_Nside_Just_for_cal_NbodyCont_Length[0]
                            # Hrz이므로 fixed
        _Caculation_Parameters['_Capbank1_Nside_Just_for_cal_NbodyContact_Vert']  		= _Capbank1_Nside_Just_for_cal_NbodyContact_Vert[0]



                        # ##### Pside 에서 1번째 driver에 연결되는 Capbank에서
                        #Cap cell에 대하여
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_pmos_gate']  					= _Capbank1_Pside_dcdl_cap_tg_pmos_gate[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_nmos_gate']  					= _Capbank1_Pside_dcdl_cap_tg_nmos_gate[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_gate']  						= _Capbank1_Pside_dcdl_cap_cap_gate[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_gate_spacing']  				= _Capbank1_Pside_dcdl_cap_tg_gate_spacing[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_gate_spacing']  				= _Capbank1_Pside_dcdl_cap_cap_gate_spacing[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_nmos_width']  					= _Capbank1_Pside_dcdl_cap_tg_nmos_width[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_pmos_width']  					= _Capbank1_Pside_dcdl_cap_tg_pmos_width[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_length']  						= _Capbank1_Pside_dcdl_cap_tg_length[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_sdwidth']  						= _Capbank1_Pside_dcdl_cap_tg_sdwidth[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_sdwidth']  					= _Capbank1_Pside_dcdl_cap_cap_sdwidth[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_dummy']  						= _Capbank1_Pside_dcdl_cap_tg_dummy[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_dummy']  						= _Capbank1_Pside_dcdl_cap_cap_dummy[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_xvt']  							= _Capbank1_Pside_dcdl_cap_tg_xvt[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_xvt']  						= _Capbank1_Pside_dcdl_cap_cap_xvt[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_pmos_y']  						= _Capbank1_Pside_dcdl_cap_tg_pmos_y[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_tg_nmos_y']  						= _Capbank1_Pside_dcdl_cap_tg_nmos_y[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_nmos_width']  					= _Capbank1_Pside_dcdl_cap_cap_nmos_width[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_pmos_width']  					= _Capbank1_Pside_dcdl_cap_cap_pmos_width[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_length']  						= _Capbank1_Pside_dcdl_cap_cap_length[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_pmos_gate_y']  				= _Capbank1_Pside_dcdl_cap_cap_pmos_gate_y[0]
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_nmos_gate_y']  				= _Capbank1_Pside_dcdl_cap_cap_nmos_gate_y[0]
        
                        #cap array
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_array']  							= _Capbank1_Pside_dcdl_cap_array[0]
                        #No flip(fixed)
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_Pside_or_Nside']  					= _Capbank1_Pside_dcdl_cap_Pside_or_Nside[0]
                        #cap xvt to xvt xdistance
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_to_cap_xdistance']  			= _Capbank1_Pside_dcdl_cap_cap_to_cap_xdistance[0]
                        #cap xvt to powerline ydistance
        _Caculation_Parameters['_Capbank1_Pside_dcdl_cap_cap_to_powerline_ydistance']  		= _Capbank1_Pside_dcdl_cap_cap_to_powerline_ydistance[0]
        
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
                            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_PbodyContCount_of_Width']  	= _Capbank1_Pside_Just_for_cal_PbodyContCount_of_Width[0]
                            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_PbodyCont_Length']  			= _Capbank1_Pside_Just_for_cal_PbodyCont_Length[0]
                            #Hrz이므로 fixed
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_PbodyContact_Vert']  			= _Capbank1_Pside_Just_for_cal_PbodyContact_Vert[0]
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
                            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_NbodyContCount_of_Width']  	= _Capbank1_Pside_Just_for_cal_NbodyContCount_of_Width[0]
                            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_NbodyCont_Length']  			= _Capbank1_Pside_Just_for_cal_NbodyCont_Length[0]
                            # Hrz이므로 fixed
        _Caculation_Parameters['_Capbank1_Pside_Just_for_cal_NbodyContact_Vert']  			= _Capbank1_Pside_Just_for_cal_NbodyContact_Vert[0]




                        # ##### Nside 에서 2번째 driver에 연결되는 Capbank에서
                        #Cap cell에 대하여
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_pmos_gate']  					= _Capbank2_Nside_dcdl_cap_tg_pmos_gate[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_nmos_gate']  					= _Capbank2_Nside_dcdl_cap_tg_nmos_gate[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_gate']  						= _Capbank2_Nside_dcdl_cap_cap_gate[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_gate_spacing']  				= _Capbank2_Nside_dcdl_cap_tg_gate_spacing[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_gate_spacing']  				= _Capbank2_Nside_dcdl_cap_cap_gate_spacing[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_nmos_width']  					= _Capbank2_Nside_dcdl_cap_tg_nmos_width[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_pmos_width']  					= _Capbank2_Nside_dcdl_cap_tg_pmos_width[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_length']  						= _Capbank2_Nside_dcdl_cap_tg_length[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_sdwidth']  						= _Capbank2_Nside_dcdl_cap_tg_sdwidth[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_sdwidth']  					= _Capbank2_Nside_dcdl_cap_cap_sdwidth[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_dummy']  						= _Capbank2_Nside_dcdl_cap_tg_dummy[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_dummy']  						= _Capbank2_Nside_dcdl_cap_cap_dummy[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_xvt']  							= _Capbank2_Nside_dcdl_cap_tg_xvt[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_xvt']  						= _Capbank2_Nside_dcdl_cap_cap_xvt[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_pmos_y']  						= _Capbank2_Nside_dcdl_cap_tg_pmos_y[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_tg_nmos_y']  						= _Capbank2_Nside_dcdl_cap_tg_nmos_y[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_nmos_width']  					= _Capbank2_Nside_dcdl_cap_cap_nmos_width[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_pmos_width']  					= _Capbank2_Nside_dcdl_cap_cap_pmos_width[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_length']  						= _Capbank2_Nside_dcdl_cap_cap_length[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_pmos_gate_y']  				= _Capbank2_Nside_dcdl_cap_cap_pmos_gate_y[0]
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_nmos_gate_y']  				= _Capbank2_Nside_dcdl_cap_cap_nmos_gate_y[0]
        
                        #cap array
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_array']  							= _Capbank2_Nside_dcdl_cap_array[0]
                        #No flip(fixed)
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_Pside_or_Nside']  					= _Capbank2_Nside_dcdl_cap_Pside_or_Nside[0]
                        #cap xvt to xvt xdistance
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_to_cap_xdistance']  			= _Capbank2_Nside_dcdl_cap_cap_to_cap_xdistance[0]
                        #cap xvt to powerline ydistance
        _Caculation_Parameters['_Capbank2_Nside_dcdl_cap_cap_to_powerline_ydistance']  		= _Capbank2_Nside_dcdl_cap_cap_to_powerline_ydistance[0]
        
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
                            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_PbodyContCount_of_Width']  	= _Capbank2_Nside_Just_for_cal_PbodyContCount_of_Width[0]
                            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_PbodyCont_Length']  			= _Capbank2_Nside_Just_for_cal_PbodyCont_Length[0]
                            #Hrz이므로 fixed
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_PbodyContact_Vert']  			= _Capbank2_Nside_Just_for_cal_PbodyContact_Vert[0]
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
                            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_NbodyContCount_of_Width']  	= _Capbank2_Nside_Just_for_cal_NbodyContCount_of_Width[0]
                            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_NbodyCont_Length']  			= _Capbank2_Nside_Just_for_cal_NbodyCont_Length[0]
                            # Hrz이므로 fixed
        _Caculation_Parameters['_Capbank2_Nside_Just_for_cal_NbodyContact_Vert']  			= _Capbank2_Nside_Just_for_cal_NbodyContact_Vert[0]



                        # ##### Pside 에서 2번째 driver에 연결되는 Capbank에서
                        #Cap cell에 대하여
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_pmos_gate']  					= _Capbank2_Pside_dcdl_cap_tg_pmos_gate[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_nmos_gate']  					= _Capbank2_Pside_dcdl_cap_tg_nmos_gate[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_gate']  						= _Capbank2_Pside_dcdl_cap_cap_gate[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_gate_spacing']  				= _Capbank2_Pside_dcdl_cap_tg_gate_spacing[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_gate_spacing']  				= _Capbank2_Pside_dcdl_cap_cap_gate_spacing[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_nmos_width']  					= _Capbank2_Pside_dcdl_cap_tg_nmos_width[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_pmos_width']  					= _Capbank2_Pside_dcdl_cap_tg_pmos_width[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_length']  						= _Capbank2_Pside_dcdl_cap_tg_length[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_sdwidth']  						= _Capbank2_Pside_dcdl_cap_tg_sdwidth[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_sdwidth']  					= _Capbank2_Pside_dcdl_cap_cap_sdwidth[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_dummy']  						= _Capbank2_Pside_dcdl_cap_tg_dummy[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_dummy']  						= _Capbank2_Pside_dcdl_cap_cap_dummy[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_xvt']  							= _Capbank2_Pside_dcdl_cap_tg_xvt[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_xvt']  						= _Capbank2_Pside_dcdl_cap_cap_xvt[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_pmos_y']  						= _Capbank2_Pside_dcdl_cap_tg_pmos_y[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_tg_nmos_y']  						= _Capbank2_Pside_dcdl_cap_tg_nmos_y[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_nmos_width']  					= _Capbank2_Pside_dcdl_cap_cap_nmos_width[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_pmos_width']  					= _Capbank2_Pside_dcdl_cap_cap_pmos_width[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_length']  						= _Capbank2_Pside_dcdl_cap_cap_length[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_pmos_gate_y']  				= _Capbank2_Pside_dcdl_cap_cap_pmos_gate_y[0]
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_nmos_gate_y']  				= _Capbank2_Pside_dcdl_cap_cap_nmos_gate_y[0]
        
                        #cap array
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_array']  							= _Capbank2_Pside_dcdl_cap_array[0]
                        #No flip(fixed)
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_Pside_or_Nside']  					= _Capbank2_Pside_dcdl_cap_Pside_or_Nside[0]
                        #cap xvt to xvt xdistance
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_to_cap_xdistance']  			= _Capbank2_Pside_dcdl_cap_cap_to_cap_xdistance[0]
                        #cap xvt to powerline ydistance
        _Caculation_Parameters['_Capbank2_Pside_dcdl_cap_cap_to_powerline_ydistance']  		= _Capbank2_Pside_dcdl_cap_cap_to_powerline_ydistance[0]
        
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 Pbody가 있어야 계산할수 있는데 그때 사용됨
                            #cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_PbodyContCount_of_Width']  	= _Capbank2_Pside_Just_for_cal_PbodyContCount_of_Width[0]
                            #cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_PbodyCont_Length']  			= _Capbank2_Pside_Just_for_cal_PbodyCont_Length[0]
                            #Hrz이므로 fixed
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_PbodyContact_Vert']  			= _Capbank2_Pside_Just_for_cal_PbodyContact_Vert[0]
        
                        # ##C01_cap_array에서 cap array간의 ydistance 구할때 가상의 nbody가 있어야 계산할수 있는데 그때 사용됨
                            # cap array에서 pbody의 두께와 관련된 contact 갯수, 이값은 실제 가상계산 및 실제 layout에서도 반영된다.
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_NbodyContCount_of_Width']  	= _Capbank2_Pside_Just_for_cal_NbodyContCount_of_Width[0]
                            # cap array에서 pbody의 두께를 정확하게 계산하려면 대략적인 length가 필요하다. 이값은 가상 계산에서만 반영되며 실제 length는 Nside1,2를 붙이고 그 거리를 계산하여 결정된다.
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_NbodyCont_Length']  			= _Capbank2_Pside_Just_for_cal_NbodyCont_Length[0]
                            # Hrz이므로 fixed
        _Caculation_Parameters['_Capbank2_Pside_Just_for_cal_NbodyContact_Vert']  			= _Capbank2_Pside_Just_for_cal_NbodyContact_Vert[0]

                        #Nside에서 capbank에서 왼쪽 gruardring 두께관련된 contact 갯수
        _Caculation_Parameters['Nside_Side_Guard_bodyContCount_of_Width']  			    = Nside_Side_Guard_bodyContCount_of_Width[0]
                        #Nside에서 capbank의 가장 끝 capcell까지 거리 (Nw또는OD부터 Xvt까지 거리)
        _Caculation_Parameters['Nside_Left_Side_Guard_to_Capbank_distance']  			= Nside_Left_Side_Guard_to_Capbank_distance[0]
                        #Pside에서 capbank에서 왼쪽 gruardring 두께관련된 contact 갯수
        _Caculation_Parameters['Pside_Side_Guard_bodyContCount_of_Width']  			    = Pside_Side_Guard_bodyContCount_of_Width[0]
                        #Pside에서 capbank의 가장 끝 capcell까지 거리 (Nw또는OD부터 Xvt까지 거리)
        _Caculation_Parameters['Pside_Left_Side_Guard_to_Capbank_distance']  			= Pside_Left_Side_Guard_to_Capbank_distance[0]





        #Generate Sref
        self._DesignParameter['_Dcdl_top'] = self._SrefElementDeclaration(_DesignObj=D00_dcdl_v6._DCDL( _DesignParameter=None, _Name='{}:_Dcdl_top'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Dcdl_top']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Dcdl_top']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Dcdl_top']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Dcdl_top']['_XYCoordinates']=[[0, 0]]



        print('###############      For Debugging      #####################################################################################')

