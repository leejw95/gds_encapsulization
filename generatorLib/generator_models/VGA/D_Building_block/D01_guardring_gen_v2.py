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
class _guardring_gen(StickDiagram_KJH0._StickDiagram_KJH):
    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

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

        ######################################################################################################################### Gen_unit
        #Row
        for i in range(0,len(_Array_Cs_NMOSNumberofGate)):
            #Column
            for j in range(0,len(_Array_Cs_NMOSNumberofGate[i])):
            
                # Define Calculation_Parameters
                _Caculation_Parameters = copy.deepcopy(D00_nmos_sw_and_nmos_currentsource._nmos_sw_and_nmos_currentsource._ParametersForDesignCalculation)
                _Caculation_Parameters['_Cs_NMOSNumberofGate']  = _Array_Cs_NMOSNumberofGate[i][j]
                _Caculation_Parameters['_Cs_NMOSChannelWidth']  = _Array_Cs_NMOSChannelWidth[i][j]
                _Caculation_Parameters['_Cs_NMOSChannellength'] = _Array_Cs_NMOSChannellength[i][j]
                _Caculation_Parameters['_Cs_NMOSDummy']         = _Array_Cs_NMOSDummy
                _Caculation_Parameters['_Cs_GateSpacing']       = _Array_Cs_GateSpacing
                _Caculation_Parameters['_Cs_SDWidth']           = _Array_Cs_SDWidth
                _Caculation_Parameters['_Cs_XVT']               = _Array_Cs_XVT
                _Caculation_Parameters['_Cs_PCCrit']            = _Array_Cs_PCCrit

                _Caculation_Parameters['_Sw_NMOSNumberofGate']  = _Array_Sw_NMOSNumberofGate[i][j]
                _Caculation_Parameters['_Sw_NMOSChannelWidth']  = _Array_Sw_NMOSChannelWidth[i][j]
                _Caculation_Parameters['_Sw_NMOSChannellength'] = _Array_Sw_NMOSChannellength[i][j]
                _Caculation_Parameters['_Sw_NMOSDummy']         = _Array_Sw_NMOSDummy
                _Caculation_Parameters['_Sw_GateSpacing']       = _Array_Sw_GateSpacing
                _Caculation_Parameters['_Sw_SDWidth']           = _Array_Sw_SDWidth
                _Caculation_Parameters['_Sw_XVT']               = _Array_Sw_XVT
                _Caculation_Parameters['_Sw_PCCrit']            = _Array_Sw_PCCrit
                
                # Generate Sref
                self._DesignParameter['_Unit_{}_{}'.format(i,j)] = self._SrefElementDeclaration(_DesignObj=D00_nmos_sw_and_nmos_currentsource._nmos_sw_and_nmos_currentsource(_DesignParameter=None, _Name='{}:_Unit_{}_{}'.format(_Name,i,j)))[0]

                # Define Sref Relection
                self._DesignParameter['_Unit_{}_{}'.format(i,j)]['_Reflect'] = [0, 0, 0]

                # Define Sref Angle
                self._DesignParameter['_Unit_{}_{}'.format(i,j)]['_Angle'] = 0

                # Calculate Sref Layer by using Calculation_Parameter
                self._DesignParameter['_Unit_{}_{}'.format(i,j)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

                # Define Sref _XYcoordinate
                self._DesignParameter['_Unit_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0, 0]]

            ########################################################################################################### Calculate unit_guardring_size:find the biggest size
                ############################################################################################# Calculate unit_guardring_size:find the biggest size:xwidth
        tmp_xwidth = []
        #Row
        for i in range(0,len(_Array_Cs_NMOSNumberofGate)):
            #Column
            for j in range(0,len(_Array_Cs_NMOSNumberofGate[i])):        
        
                #set most outter boundary as nmos polydummy.(## it is not always true..)
                    #left most boundary
                tmp1 = self.get_param_KJH2('_Unit_{}_{}'.format(i,j),'_Cs_nmos','_PODummyLayer')
                    #right most boundary
                tmp2 = self.get_param_KJH2('_Unit_{}_{}'.format(i,j),'_Sw_nmos','_PODummyLayer')
                
                #Cal xwidth
                xwidth = abs(tmp2[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0])
                    
                #Index
                if (i ==0 and j==0):
                    max_xwidth_i_index = 0
                    max_xwidth_j_index = 0
                elif xwidth > max(tmp_xwidth):
                    max_xwidth_i_index = i
                    max_xwidth_j_index = j
                else :  
                    max_xwidth_i_index = max_xwidth_i_index
                    max_xwidth_j_index = max_xwidth_j_index
                    
                #tmp_xwidth
                tmp_xwidth.append(xwidth)
        
                ############################################################################################# Calculate unit_guardring_size:find the biggest size:ywidth
        tmp_ywidth = []
        #Row
        for i in range(0,len(_Array_Cs_NMOSNumberofGate)):
            #Column
            for j in range(0,len(_Array_Cs_NMOSNumberofGate[i])):        
        
                #set most outter upper boundary as M2 Hrz connection, and lower boundary as nmos_sw_via_m4
                    #upper most boundary
                tmp1_1 = self.get_param_KJH2('_Unit_{}_{}'.format(i,j),'_Cs_nmos_drain_m2_hrz')
                tmp1_2 = self.get_param_KJH2('_Unit_{}_{}'.format(i,j),'_Sw_nmos_source_m2_hrz')
                if tmp1_1[0]['_XY_up'][1] > tmp1_2[0]['_XY_up'][1]:
                    tmp1 = tmp1_1
                else:
                    tmp1 = tmp1_2
                    #lower most boundary
                tmp2 = self.get_param_KJH2('_Unit_{}_{}'.format(i,j),'_Sw_nmos_gate_Via3_M3M4','_Met4Layer')
                
                #Cal ywidth
                ywidth = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])
                
                #Index
                if (i ==0 and j==0):
                    max_ywidth_i_index = 0
                    max_ywidth_j_index = 0
                elif ywidth > max(tmp_ywidth):
                    max_ywidth_i_index = i
                    max_ywidth_j_index = j
                else :  
                    max_ywidth_i_index = max_ywidth_i_index
                    max_ywidth_j_index = max_ywidth_j_index
                
                #tmp_ywidth
                tmp_ywidth.append(ywidth) 

        ######################################################################################################################### Gen_Hrz_Pbody_upper
        # pre-defined
        ydistance1 = 250
        
        #_Unit_xwidth
        _Unit_xwidth = max(tmp_xwidth)

        # If Hrz
        _PbodyContact_NumberOfPbodyCOX = (int(((_Unit_xwidth - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Hrz_PbodyContCount_of_Width) + 0
        _PbodyContact_NumberOfPbodyCOY = _Hrz_PbodyContCount_of_Width
        _PbodyContact_Met1XWidth = None
        _PbodyContact_Met1YWidth = None

        # Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX'] = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY'] = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth'] = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth'] = _PbodyContact_Met1YWidth

        # Define _PbodyContact Sref
        self._DesignParameter['_Unit_Hrz_Pbody_upper'] = self._SrefElementDeclaration( _DesignObj=A05_PbodyContact._PbodyContact(_DesignParameter=None, _Name='{}:_Unit_Hrz_Pbody_upper'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Unit_Hrz_Pbody_upper']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Unit_Hrz_Pbody_upper']['_Angle'] = 0

        # Define NMOS_DEFAULT layer
        self._DesignParameter['_Unit_Hrz_Pbody_upper']['_DesignObj']._CalculatePbodyContactDesignParameter(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['_Unit_Hrz_Pbody_upper']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        # Xcoord
        tmp1_1 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Cs_nmos', '_PODummyLayer')
        tmp1_2 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Sw_nmos', '_PODummyLayer')
        target_coordx = 0.5 * (tmp1_2[-1]['_XY_right'][0] + tmp1_1[0]['_XY_left'][0])
        # Ycoord
        tmp1_3 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Cs_nmos_drain_m2_hrz')
        tmp1_4 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_source_m2_hrz')
        
        if tmp1_3[0]['_XY_up'][1] > tmp1_4[0]['_XY_up'][1]:
            target_coordy = tmp1_3[0]['_XY_up'][1] + ydistance1
        else:
            target_coordy = tmp1_4[0]['_XY_up'][1] + ydistance1

        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper', '_Met1Layer')
        approaching_coord = tmp2[0]['_XY_down']
        # Sref coord
        tmp3 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper')
        Scoord = tmp3[0]['_XY_cent']
        # Cal
        New_Scoord = self.get_Scoord_KJH(target_coord, approaching_coord, Scoord)
        New_Scoord = np.round(New_Scoord, 2)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_Unit_Hrz_Pbody_upper']['_XYCoordinates'] = tmpXY

        ######################################################################################################################### Gen_Hrz_Pbody_lower
        # pre-defined
        ydistance2 = 250
        
        #_Unit_xwidth
        _Unit_xwidth = max(tmp_xwidth)
        
        # If Hrz
        _PbodyContact_NumberOfPbodyCOX = (int(((_Unit_xwidth - (2 * _DRCobj._CoMinEnclosureByOD)) / ( _DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Hrz_PbodyContCount_of_Width) + 0
        _PbodyContact_NumberOfPbodyCOY = _Hrz_PbodyContCount_of_Width
        _PbodyContact_Met1XWidth = None
        _PbodyContact_Met1YWidth = None

        # Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX'] = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY'] = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth'] = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth'] = _PbodyContact_Met1YWidth

        # Define _PbodyContact Sref
        self._DesignParameter['_Unit_Hrz_Pbody_lower'] = self._SrefElementDeclaration(
            _DesignObj=A05_PbodyContact._PbodyContact(_DesignParameter=None,
                                                      _Name='{}:_Unit_Hrz_Pbody_lower'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Unit_Hrz_Pbody_lower']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Unit_Hrz_Pbody_lower']['_Angle'] = 0

        # Define NMOS_DEFAULT layer
        self._DesignParameter['_Unit_Hrz_Pbody_lower']['_DesignObj']._CalculatePbodyContactDesignParameter(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['_Unit_Hrz_Pbody_lower']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        # Xcoord
        tmp1_1 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Cs_nmos', '_PODummyLayer')
        tmp1_2 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Sw_nmos', '_PODummyLayer')
        target_coordx = 0.5 * (tmp1_2[-1]['_XY_right'][0] + tmp1_1[0]['_XY_left'][0])
        # Ycoord
        # tmp1_3 = self.get_param_KJH2('_Unit','_sw_and_cs_connect_M2')
        tmp1_4 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_gate_Via3_M3M4', '_Met4Layer')
        target_coordy = tmp1_4[0]['_XY_down'][1] - ydistance2

        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower', '_Met1Layer')
        approaching_coord = tmp2[0]['_XY_up']
        # Sref coord
        tmp3 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower')
        Scoord = tmp3[0]['_XY_cent']
        # Cal
        New_Scoord = self.get_Scoord_KJH(target_coord, approaching_coord, Scoord)
        New_Scoord = np.round(New_Scoord, 2)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_Unit_Hrz_Pbody_lower']['_XYCoordinates'] = tmpXY

        ######################################################################################################################### Gen_Vtc_Pbody_left
        # pre-defined
        xdistance1 = 250

        #_Unit_ywidth
        _Unit_ywidth = max(tmp_ywidth)

        # If Hrz
        _PbodyContact_NumberOfPbodyCOX = _Vtc_PbodyContCount_of_Width
        _PbodyContact_NumberOfPbodyCOY = (int(((_Unit_ywidth - (2 * _DRCobj._CoMinEnclosureByOD)) / ( _DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Vtc_PbodyContCount_of_Width) + 0
        _PbodyContact_Met1XWidth = None
        _PbodyContact_Met1YWidth = None

        # Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX'] = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY'] = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth'] = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth'] = _PbodyContact_Met1YWidth

        # Define _PbodyContact Sref
        self._DesignParameter['_Unit_Vtc_Pbody_left'] = self._SrefElementDeclaration(
            _DesignObj=A05_PbodyContact._PbodyContact(_DesignParameter=None,
                                                      _Name='{}:_Unit_Vtc_Pbody_left'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Unit_Vtc_Pbody_left']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Unit_Vtc_Pbody_left']['_Angle'] = 0

        # Define NMOS_DEFAULT layer
        self._DesignParameter['_Unit_Vtc_Pbody_left']['_DesignObj']._CalculatePbodyContactDesignParameter(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['_Unit_Vtc_Pbody_left']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        # xcoord
        tmp1_1 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Cs_nmos', '_PODummyLayer')       
        
        target_coordx = tmp1_1[0]['_XY_left'][0] - xdistance1
        # ycoord
        tmp1_3 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Cs_nmos_drain_m2_hrz')
        tmp1_4 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_source_m2_hrz')
        
        if tmp1_3[0]['_XY_up'][1] > tmp1_4[0]['_XY_up'][1]:
            tmp1_5 = tmp1_3
        else:
            tmp1_5 = tmp1_4
            
        tmp1_6 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_gate_Via3_M3M4', '_Met4Layer')    
            
        target_coordy = 0.5 * (tmp1_5[0]['_XY_up'][1] + tmp1_6[0]['_XY_down'][1])

        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_left', '_Met1Layer')
        approaching_coord = tmp2[0]['_XY_right']
        # Sref coord
        tmp3 = self.get_param_KJH2('_Unit_Vtc_Pbody_left')
        Scoord = tmp3[0]['_XY_cent']
        # Cal
        New_Scoord = self.get_Scoord_KJH(target_coord, approaching_coord, Scoord)
        New_Scoord = np.round(New_Scoord, 2)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_Unit_Vtc_Pbody_left']['_XYCoordinates'] = tmpXY

        ######################################################################################################################### Gen_Vtc_Pbody_right
        # pre-defined
        xdistance2 = 250

        #_Unit_ywidth
        _Unit_ywidth = max(tmp_ywidth)

        # If Hrz
        _PbodyContact_NumberOfPbodyCOX = _Vtc_PbodyContCount_of_Width
        _PbodyContact_NumberOfPbodyCOY = (int(((_Unit_ywidth - (2 * _DRCobj._CoMinEnclosureByOD)) / ( _DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Vtc_PbodyContCount_of_Width) + 0
        _PbodyContact_Met1XWidth = None
        _PbodyContact_Met1YWidth = None

        # Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX'] = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY'] = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth'] = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth'] = _PbodyContact_Met1YWidth

        # Define _PbodyContact Sref
        self._DesignParameter['_Unit_Vtc_Pbody_right'] = self._SrefElementDeclaration(
            _DesignObj=A05_PbodyContact._PbodyContact(_DesignParameter=None,
                                                      _Name='{}:_Unit_Vtc_Pbody_right'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Unit_Vtc_Pbody_right']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Unit_Vtc_Pbody_right']['_Angle'] = 0

        # Define NMOS_DEFAULT layer
        self._DesignParameter['_Unit_Vtc_Pbody_right']['_DesignObj']._CalculatePbodyContactDesignParameter(
            **_Caculation_Parameters)

        # Calculate Sref XYcoord
        tmpXY = []
        # initialized Sref coordinate
        self._DesignParameter['_Unit_Vtc_Pbody_right']['_XYCoordinates'] = [[0, 0]]
        # Calculate
        # Target_coord
        # xcoord
        tmp1_1 = self.get_param_KJH2('_Unit_{}_{}'.format(max_xwidth_i_index,max_xwidth_j_index), '_Sw_nmos', '_PODummyLayer')       
        
        target_coordx = tmp1_1[-1]['_XY_right'][0] + xdistance2
        # ycoord
        tmp1_3 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Cs_nmos_drain_m2_hrz')
        tmp1_4 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_source_m2_hrz')
        
        if tmp1_3[0]['_XY_up'][1] > tmp1_4[0]['_XY_up'][1]:
            tmp1_5 = tmp1_3
        else:
            tmp1_5 = tmp1_4
            
        tmp1_6 = self.get_param_KJH2('_Unit_{}_{}'.format(max_ywidth_i_index,max_ywidth_j_index), '_Sw_nmos_gate_Via3_M3M4', '_Met4Layer')    
            
        target_coordy = 0.5 * (tmp1_5[0]['_XY_up'][1] + tmp1_6[0]['_XY_down'][1])

        target_coord = [target_coordx, target_coordy]
        # Approaching_coord
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right', '_Met1Layer')
        approaching_coord = tmp2[0]['_XY_left']
        # Sref coord
        tmp3 = self.get_param_KJH2('_Unit_Vtc_Pbody_right')
        Scoord = tmp3[0]['_XY_cent']
        # Cal
        New_Scoord = self.get_Scoord_KJH(target_coord, approaching_coord, Scoord)
        New_Scoord = np.round(New_Scoord, 2)
        tmpXY.append(New_Scoord)
        # Define
        self._DesignParameter['_Unit_Vtc_Pbody_right']['_XYCoordinates'] = tmpXY
        
        ######################################################################################################################### _Unit delete
        #Row
        for i in range(0,len(_Array_Cs_NMOSNumberofGate)):
            #Column
            for j in range(0,len(_Array_Cs_NMOSNumberofGate[i])):
                del self._DesignParameter['_Unit_{}_{}'.format(i,j)]


        ######################################################################################################################### _Upper_pbody_extenstion
            ########################################################################################################### _Upper_pbody_extenstion:_ODLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_ODLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_ODLayer')
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_ODLayer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_ODLayer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_ODLayer')

        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_ODLayer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_ODLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_upper']['_XYCoordinates']


            ########################################################################################################### _Upper_pbody_extenstion:_PPLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_PPLayer')
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_PPLayer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_PPLayer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_PPLayer')

        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_PPLayer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_PPLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_upper']['_XYCoordinates']
            ########################################################################################################### _Upper_pbody_extenstion:_Met1Layer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_Me1Layer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_Met1Layer')
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_Me1Layer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_Met1Layer')

        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_Me1Layer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_upper_extension_Me1Layer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_upper']['_XYCoordinates']
        
        

        ######################################################################################################################### _Lower_pbody_extenstion
            ########################################################################################################### _Lower_pbody_extenstion:_ODLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_ODLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_ODLayer')
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_ODLayer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_ODLayer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_ODLayer')

        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_ODLayer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_ODLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_lower']['_XYCoordinates']
            ########################################################################################################### _Lower_pbody_extenstion:_PPLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_PPLayer')
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_PPLayer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_PPLayer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_PPLayer')

        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_PPLayer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_PPLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_lower']['_XYCoordinates']
            ########################################################################################################### _Lower_pbody_extenstion:_Met1Layer
        #Define Boundary_element
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_Me1Layer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_Met1Layer')
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_Me1Layer']['_YWidth'] = tmp[0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_Met1Layer')

        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_Me1Layer']['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Hrz_pbody_lower_extension_Me1Layer']['_XYCoordinates'] = self._DesignParameter['_Unit_Hrz_Pbody_lower']['_XYCoordinates']



        ######################################################################################################################### _Left_pbody_extenstion
            ########################################################################################################### _Left_pbody_extenstion:_ODLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_ODLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_ODLayer')
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_ODLayer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_ODLayer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_ODLayer')

        self._DesignParameter['_Unit_Vtc_pbody_left_extension_ODLayer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_ODLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_left']['_XYCoordinates']
            ########################################################################################################### _Left_pbody_extenstion:_PPLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_PPLayer')
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_PPLayer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_PPLayer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_PPLayer')

        self._DesignParameter['_Unit_Vtc_pbody_left_extension_PPLayer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_PPLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_left']['_XYCoordinates']
            ########################################################################################################### _Left_pbody_extenstion:_Met1Layer
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_left','_Met1Layer')
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_Met1Layer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_Met1Layer')

        self._DesignParameter['_Unit_Vtc_pbody_left_extension_Met1Layer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_left_extension_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_left']['_XYCoordinates']

        ######################################################################################################################### _Right_pbody_extenstion
            ########################################################################################################### _Right_pbody_extenstion:_ODLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_ODLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_ODLayer')
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_ODLayer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_ODLayer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_ODLayer')

        self._DesignParameter['_Unit_Vtc_pbody_right_extension_ODLayer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_ODLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_right']['_XYCoordinates']
            ########################################################################################################### _Right_pbody_extenstion:_PPLayer
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_PPLayer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_PPLayer')
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_PPLayer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_PPLayer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_PPLayer')

        self._DesignParameter['_Unit_Vtc_pbody_right_extension_PPLayer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_PPLayer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_right']['_XYCoordinates']
            ########################################################################################################### _Right_pbody_extenstion:_Met1Layer    
        #Define Boundary_element
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _YWidth
        tmp = self.get_param_KJH2('_Unit_Vtc_Pbody_right','_Met1Layer')
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_Met1Layer']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Unit_Hrz_Pbody_lower','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Unit_Hrz_Pbody_upper','_Met1Layer')

        self._DesignParameter['_Unit_Vtc_pbody_right_extension_Met1Layer']['_YWidth'] = abs( tmp2[0]['_XY_up'][1] - tmp1[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Unit_Vtc_pbody_right_extension_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_Unit_Vtc_Pbody_right']['_XYCoordinates']            
        

        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_D_building_block'
    cellname = 'D01_guardring_gen_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # Current source nmos
        _Array_Cs_NMOSNumberofGate    =[ [2,2,5,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 5,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,7,2] ] ,
        _Array_Cs_NMOSChannelWidth    =[ [1000,1200,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
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
    LayoutObj = _guardring_gen(_DesignParameter=None, _Name=cellname)
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
