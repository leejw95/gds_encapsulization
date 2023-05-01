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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B05_routing

## ########################################################################################################################################################## Class_HEADER
class _pos_neg(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

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

#vtc nbodycontact
_Array_vtc_btw_res_sw_NbodyContCount_of_Width = None,

#hrz nbodycontact
_Array_hrz_NbodyContCount_of_Width_upper_unit = None,

    #leftright vtc nbodycontact
_LeftRight_NbodyContCount_of_Width = None,

    #Middle vtc nbodycontact
_Middle_NbodyContCount_of_Width = None,

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

#vtc nbodycontact
_Array_vtc_btw_res_sw_NbodyContCount_of_Width = None,

#hrz nbodycontact
_Array_hrz_NbodyContCount_of_Width_upper_unit = None,

    #leftright vtc nbodycontact
_LeftRight_NbodyContCount_of_Width = None,

    #Middle vtc nbodycontact
_Middle_NbodyContCount_of_Width = None,

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

            ## ################################################################################################################### Gen Res_n : right side
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(B05_routing._routing._ParametersForDesignCalculation)
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

        _Caculation_Parameters['_Left_NbodyContCount_of_Width'] 				= _LeftRight_NbodyContCount_of_Width

        _Caculation_Parameters['_Right_NbodyContCount_of_Width'] 				= _Middle_NbodyContCount_of_Width

            # Generate Sref
        self._DesignParameter['_Res_n'] = self._SrefElementDeclaration(_DesignObj=B05_routing._routing(_DesignParameter=None, _Name='{}:_Res_n'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Res_n']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Res_n']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Res_n']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Res_n']['_XYCoordinates'] = [[0,0]]

            ## ################################################################################################################### Gen Res_p : left side
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(B05_routing._routing._ParametersForDesignCalculation)
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

        _Caculation_Parameters['_Left_NbodyContCount_of_Width'] 				= _LeftRight_NbodyContCount_of_Width

        _Caculation_Parameters['_Right_NbodyContCount_of_Width'] 				= _Middle_NbodyContCount_of_Width

            # Generate Sref
        self._DesignParameter['_Res_p'] = self._SrefElementDeclaration(_DesignObj=B05_routing._routing(_DesignParameter=None, _Name='{}:_Res_p'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Res_p']['_Reflect'] = [1, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Res_p']['_Angle'] = 180

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Res_p']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Res_p']['_XYCoordinates'] = [[0,0]]

        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Res_p']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Res_n','_Array_with_ring','_Left_nbodycontact','_Met1Layer')  		
        target_coord = tmp1[0][0][0][0][0]['_XY_cent']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Res_p','_Array_with_ring','_Left_nbodycontact','_Met1Layer')  
        approaching_coord = tmp2[0][0][0][0][0]['_XY_cent']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Res_p') 
        Scoord = tmp3[0][0]['_XY_cent']  
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Res_p']['_XYCoordinates'] = tmpXY
        

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_B_building_block'
    cellname = 'B06_pos_neg_95'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

#polyres
_Array_Polyres_R_X_width  = [500, 1500, 1000, 800,1100,],
_Array_Polyres_R_Y_length = [600, 800, 850, 1000,700,],
_Array_Polyres_CoXNum     = [None,None,None,None,None,],
_Array_Polyres_CoYNum     = [None,None,None,None,None,],
_Array_Polyres_Dummy      = False,
_Array_Polyres_N_Parallel = [3,1,1,1,1],

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
    LayoutObj = _pos_neg(_DesignParameter=None, _Name=cellname)
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
