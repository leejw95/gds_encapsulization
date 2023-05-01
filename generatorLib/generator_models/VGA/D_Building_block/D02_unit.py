'''


'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
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

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D00_nmos_sw_and_nmos_currentsource
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D01_guardring_gen_v2
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D03_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D04_routing


############################################################################################################################################################ Class_HEADER
class _unit(StickDiagram_KJH0._StickDiagram_KJH):
    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

        # ## Guardring_gen
            # Current source nmos
        _Array_Cs_NMOSNumberofGate    =[ [2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2] ], 
        _Array_Cs_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Cs_NMOSChannellength   =[ [200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200] ] ,
        _Array_Cs_NMOSDummy           =True, 
        _Array_Cs_GateSpacing         =None, 
        _Array_Cs_SDWidth             =None,
        _Array_Cs_XVT                 ='SLVT',
        _Array_Cs_PCCrit              =None, 

            # SW nmos
        _Array_Sw_NMOSNumberofGate    =[ [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1] ] ,
        _Array_Sw_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Sw_NMOSChannellength   =[ [30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30] ] ,
        _Array_Sw_NMOSDummy           =True, 
        _Array_Sw_GateSpacing         =None,
        _Array_Sw_SDWidth             =None, 
        _Array_Sw_XVT                 ='SLVT',
        _Array_Sw_PCCrit              =None,

            # Vtc_pbodycontact
        _Vtc_PbodyContCount_of_Width = 2,

            # Hrz_pbodycontact
        _Hrz_PbodyContCount_of_Width = 4,

        # ## Nmos_sw_and_cs
            #Current source nmos
        _Cs_NMOSNumberofGate=2,
        _Cs_NMOSChannelWidth=1200,
        _Cs_NMOSChannellength=200,
        _Cs_NMOSDummy=True,
        _Cs_GateSpacing=None,
        _Cs_SDWidth=None,
        _Cs_XVT='SLVT',
        _Cs_PCCrit=None,


            #SW nmos
        _Sw_NMOSNumberofGate=4,
        _Sw_NMOSChannelWidth=1000,
        _Sw_NMOSChannellength=30,
        _Sw_NMOSDummy=True,
        _Sw_GateSpacing=None,
        _Sw_SDWidth=None,
        _Sw_XVT='SLVT',
        _Sw_PCCrit=None,

    )

    # Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ################################################################################################################################################## _CalculateDesignParameter
    def _CalculateDesignParameter(self,

        # ## Guardring_gen
            # Current source nmos
        _Array_Cs_NMOSNumberofGate    =[ [2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2] ], 
        _Array_Cs_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Cs_NMOSChannellength   =[ [200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200] ] ,
        _Array_Cs_NMOSDummy           =True, 
        _Array_Cs_GateSpacing         =None, 
        _Array_Cs_SDWidth             =None,
        _Array_Cs_XVT                 ='SLVT',
        _Array_Cs_PCCrit              =None, 

            # SW nmos
        _Array_Sw_NMOSNumberofGate    =[ [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1] ] ,
        _Array_Sw_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Sw_NMOSChannellength   =[ [30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30] ] ,
        _Array_Sw_NMOSDummy           =True, 
        _Array_Sw_GateSpacing         =None,
        _Array_Sw_SDWidth             =None, 
        _Array_Sw_XVT                 ='SLVT',
        _Array_Sw_PCCrit              =None,

            # Vtc_pbodycontact
        _Vtc_PbodyContCount_of_Width = 2,

            # Hrz_pbodycontact
        _Hrz_PbodyContCount_of_Width = 4,

        # ## Nmos_sw_and_cs
            #Current source nmos
        _Cs_NMOSNumberofGate=2,
        _Cs_NMOSChannelWidth=1200,
        _Cs_NMOSChannellength=200,
        _Cs_NMOSDummy=True,
        _Cs_GateSpacing=None,
        _Cs_SDWidth=None,
        _Cs_XVT='SLVT',
        _Cs_PCCrit=None,


            #SW nmos
        _Sw_NMOSNumberofGate=4,
        _Sw_NMOSChannelWidth=1000,
        _Sw_NMOSChannellength=30,
        _Sw_NMOSDummy=True,
        _Sw_GateSpacing=None,
        _Sw_SDWidth=None,
        _Sw_XVT='SLVT',
        _Sw_PCCrit=None,


                                  ):

        #################################################################################################################################### Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ################################################################################################################################### Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ######################################################################################################################### Gen_guardring
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(D01_guardring_gen_v2._guardring_gen._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Cs_NMOSNumberofGate']  = _Array_Cs_NMOSNumberofGate
        _Caculation_Parameters['_Array_Cs_NMOSChannelWidth']  = _Array_Cs_NMOSChannelWidth
        _Caculation_Parameters['_Array_Cs_NMOSChannellength'] = _Array_Cs_NMOSChannellength
        _Caculation_Parameters['_Array_Cs_NMOSDummy']         = _Array_Cs_NMOSDummy
        _Caculation_Parameters['_Array_Cs_GateSpacing']       = _Array_Cs_GateSpacing
        _Caculation_Parameters['_Array_Cs_SDWidth']           = _Array_Cs_SDWidth
        _Caculation_Parameters['_Array_Cs_XVT']               = _Array_Cs_XVT
        _Caculation_Parameters['_Array_Cs_PCCrit']            = _Array_Cs_PCCrit

        _Caculation_Parameters['_Array_Sw_NMOSNumberofGate']  = _Array_Sw_NMOSNumberofGate
        _Caculation_Parameters['_Array_Sw_NMOSChannelWidth']  = _Array_Sw_NMOSChannelWidth
        _Caculation_Parameters['_Array_Sw_NMOSChannellength'] = _Array_Sw_NMOSChannellength
        _Caculation_Parameters['_Array_Sw_NMOSDummy']         = _Array_Sw_NMOSDummy
        _Caculation_Parameters['_Array_Sw_GateSpacing']       = _Array_Sw_GateSpacing
        _Caculation_Parameters['_Array_Sw_SDWidth']           = _Array_Sw_SDWidth
        _Caculation_Parameters['_Array_Sw_XVT']               = _Array_Sw_XVT
        _Caculation_Parameters['_Array_Sw_PCCrit']            = _Array_Sw_PCCrit
    
        _Caculation_Parameters['_Vtc_PbodyContCount_of_Width']  = _Vtc_PbodyContCount_of_Width
        _Caculation_Parameters['_Hrz_PbodyContCount_of_Width']  = _Hrz_PbodyContCount_of_Width
    
        # Generate Sref
        self._DesignParameter['_Guardring'] = self._SrefElementDeclaration(_DesignObj=D01_guardring_gen_v2._guardring_gen(_DesignParameter=None, _Name='{}:_Guardring'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Guardring']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Guardring']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Guardring']['_XYCoordinates'] = [[0, 0]]
        
        ######################################################################################################################### Gen_Nmos_sw_and_cs
        #pre-defined
        xdistance = 250
        
        
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(D00_nmos_sw_and_nmos_currentsource._nmos_sw_and_nmos_currentsource._ParametersForDesignCalculation)
        _Caculation_Parameters['_Cs_NMOSNumberofGate']  = _Cs_NMOSNumberofGate
        _Caculation_Parameters['_Cs_NMOSChannelWidth']  = _Cs_NMOSChannelWidth
        _Caculation_Parameters['_Cs_NMOSChannellength'] = _Cs_NMOSChannellength
        _Caculation_Parameters['_Cs_NMOSDummy']         = _Cs_NMOSDummy
        _Caculation_Parameters['_Cs_GateSpacing']       = _Cs_GateSpacing
        _Caculation_Parameters['_Cs_SDWidth']           = _Cs_SDWidth
        _Caculation_Parameters['_Cs_XVT']               = _Cs_XVT
        _Caculation_Parameters['_Cs_PCCrit']            = _Cs_PCCrit

        _Caculation_Parameters['_Sw_NMOSNumberofGate']  = _Sw_NMOSNumberofGate
        _Caculation_Parameters['_Sw_NMOSChannelWidth']  = _Sw_NMOSChannelWidth
        _Caculation_Parameters['_Sw_NMOSChannellength'] = _Sw_NMOSChannellength
        _Caculation_Parameters['_Sw_NMOSDummy']         = _Sw_NMOSDummy
        _Caculation_Parameters['_Sw_GateSpacing']       = _Sw_GateSpacing
        _Caculation_Parameters['_Sw_SDWidth']           = _Sw_SDWidth
        _Caculation_Parameters['_Sw_XVT']               = _Sw_XVT
        _Caculation_Parameters['_Sw_PCCrit']            = _Sw_PCCrit
        
        # Generate Sref
        self._DesignParameter['_Nmos_sw_cs'] = self._SrefElementDeclaration(_DesignObj=D00_nmos_sw_and_nmos_currentsource._nmos_sw_and_nmos_currentsource(_DesignParameter=None, _Name='{}:_Nmos_sw_cs'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Nmos_sw_cs']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Nmos_sw_cs']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Nmos_sw_cs']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Nmos_sw_cs']['_XYCoordinates'] = [[0, 0]]
        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Nmos_sw_cs']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #xcoord
        tmp1_1 = self.get_param_KJH2('_Nmos_sw_cs','_Sw_nmos','_PODummyLayer')
        approaching_coordx = tmp1_1[-1]['_XY_right'][0]
                    #ycoord
        tmp1_2 = self.get_param_KJH2('_Nmos_sw_cs','_Cs_nmos_drain_m2_hrz')
        tmp1_3 = self.get_param_KJH2('_Nmos_sw_cs','_Sw_nmos_source_m2_hrz')
        
        if tmp1_2[0]['_XY_up'][1] > tmp1_3[0]['_XY_up'][1]:
            tmp1_4 = tmp1_2
        else:
            tmp1_4 = tmp1_3
            
        tmp1_5 = self.get_param_KJH2('_Nmos_sw_cs','_Sw_nmos_gate_Via3_M3M4','_Met4Layer')
        
        approaching_coordy = 0.5 * ( tmp1_4[0]['_XY_up'][1] + tmp1_5[0]['_XY_down'][1] )

        approaching_coord = [approaching_coordx,approaching_coordy]
        
                #Target_coord
        tmp2 = self.get_param_KJH2('_Guardring','_Unit_Vtc_Pbody_right','_Met1Layer')  
        target_coord = tmp2[0]['_XY_left'] 
                #Sref coord
        tmp3 = self.get_param_KJH2('_Nmos_sw_cs')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] - xdistance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Nmos_sw_cs']['_XYCoordinates'] = tmpXY

        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_D_building_block'
    cellname = 'D02_unit_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # ## Guardring_gen
            # Current source nmos
        _Array_Cs_NMOSNumberofGate    =[ [2,2,2,2,4, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2] ], 
        _Array_Cs_NMOSChannelWidth    =[ [1000,1300,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Cs_NMOSChannellength   =[ [200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200] ] ,
        _Array_Cs_NMOSDummy           =True, 
        _Array_Cs_GateSpacing         =None, 
        _Array_Cs_SDWidth             =None,
        _Array_Cs_XVT                 ='SLVT',
        _Array_Cs_PCCrit              =None, 

            # SW nmos
        _Array_Sw_NMOSNumberofGate    =[ [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1] ] ,
        _Array_Sw_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        _Array_Sw_NMOSChannellength   =[ [30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30] ] ,
        _Array_Sw_NMOSDummy           =True, 
        _Array_Sw_GateSpacing         =None,
        _Array_Sw_SDWidth             =None, 
        _Array_Sw_XVT                 ='SLVT',
        _Array_Sw_PCCrit              =None,

            # Vtc_pbodycontact
        _Vtc_PbodyContCount_of_Width = 2,

            # Hrz_pbodycontact
        _Hrz_PbodyContCount_of_Width = 4,

        # ## Nmos_sw_and_cs
            #Current source nmos
        _Cs_NMOSNumberofGate=2,
        _Cs_NMOSChannelWidth=1000,
        _Cs_NMOSChannellength=200,
        _Cs_NMOSDummy=True,
        _Cs_GateSpacing=None,
        _Cs_SDWidth=None,
        _Cs_XVT='SLVT',
        _Cs_PCCrit=None,


            #SW nmos
        _Sw_NMOSNumberofGate=1,
        _Sw_NMOSChannelWidth=1000,
        _Sw_NMOSChannellength=30,
        _Sw_NMOSDummy=True,
        _Sw_GateSpacing=None,
        _Sw_SDWidth=None,
        _Sw_XVT='SLVT',
        _Sw_PCCrit=None,

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
    LayoutObj = _unit(_DesignParameter=None, _Name=cellname)
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
