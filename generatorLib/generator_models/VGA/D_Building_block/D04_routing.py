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
class _routing(StickDiagram_KJH0._StickDiagram_KJH):
    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

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

            # Dummy_indication
         _Array_dummy_indication = [ [0,1,0,1],[0,0,1,0], ],
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

            # Dummy_indication
        _Array_dummy_indication = [ [0,1,0,1],[0,0,1,0], ],

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

        ######################################################################################################################### Gen_Placement
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(D03_placement._placement._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Cs_NMOSNumberofGate']    = _Array_Cs_NMOSNumberofGate
        _Caculation_Parameters['_Array_Cs_NMOSChannelWidth']    = _Array_Cs_NMOSChannelWidth
        _Caculation_Parameters['_Array_Cs_NMOSChannellength']   = _Array_Cs_NMOSChannellength
        _Caculation_Parameters['_Array_Cs_NMOSDummy']           = _Array_Cs_NMOSDummy
        _Caculation_Parameters['_Array_Cs_GateSpacing']         = _Array_Cs_GateSpacing
        _Caculation_Parameters['_Array_Cs_SDWidth']             = _Array_Cs_SDWidth
        _Caculation_Parameters['_Array_Cs_XVT']                 = _Array_Cs_XVT
        _Caculation_Parameters['_Array_Cs_PCCrit']              = _Array_Cs_PCCrit

        _Caculation_Parameters['_Array_Sw_NMOSNumberofGate']    = _Array_Sw_NMOSNumberofGate
        _Caculation_Parameters['_Array_Sw_NMOSChannelWidth']    = _Array_Sw_NMOSChannelWidth
        _Caculation_Parameters['_Array_Sw_NMOSChannellength']   = _Array_Sw_NMOSChannellength
        _Caculation_Parameters['_Array_Sw_NMOSDummy']           = _Array_Sw_NMOSDummy
        _Caculation_Parameters['_Array_Sw_GateSpacing']         = _Array_Sw_GateSpacing
        _Caculation_Parameters['_Array_Sw_SDWidth']             = _Array_Sw_SDWidth
        _Caculation_Parameters['_Array_Sw_XVT']                 = _Array_Sw_XVT
        _Caculation_Parameters['_Array_Sw_PCCrit']              = _Array_Sw_PCCrit

        _Caculation_Parameters['_Vtc_PbodyContCount_of_Width']  = _Vtc_PbodyContCount_of_Width
        _Caculation_Parameters['_Hrz_PbodyContCount_of_Width']  = _Hrz_PbodyContCount_of_Width

        # Generate Sref
        self._DesignParameter['_Placement'] = self._SrefElementDeclaration(_DesignObj=D03_placement._placement(_DesignParameter=None,_Name='{}:_Placement'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Placement']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Placement']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Placement']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Placement']['_XYCoordinates'] = [[0, 0]]

        ######################################################################################################################### CS_source_VSS_connection   
        # Row
        for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            # Column
            for j in range(0, len(_Array_Cs_NMOSNumberofGate[i])):
                tmpXY=[]

                #Define Boundary_element
                self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)] = self._BoundaryElementDeclaration(
                                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                    _XWidth=None,
                                                                                                    _YWidth=None,
                                                                                                    _XYCoordinates=[ ],
                                                                                                   )

                #Define Boundary_element _XWidth
                tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos','_Met1Layer')
                self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)]['_XWidth'] = tmp[0]['_Xwidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos','_Met1Layer')
                tmp2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Guardring','_Unit_Hrz_Pbody_upper','_Met1Layer')

                self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)]['_YWidth'] = abs( tmp2[0]['_XY_down'][1] - tmp1[0]['_XY_up'][1] )

                #Initialize coordinate
                self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_source_M1')


                for k in range(0,len(tmp)):
                        #initialized Sref coordinate
                    self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]
                        #Calculate
                            #Target_coord
                    tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_source_M1')
                    target_coord = tmp1[k]['_XY_up_left']
                            #Approaching_coord
                    tmp2 = self.get_param_KJH2('_Cs_source_vss_M1_conn_{}_{}'.format(i,j))
                    approaching_coord = tmp2[0]['_XY_down_left']
                            #Sref coord
                    tmp3 = self.get_param_KJH2('_Cs_source_vss_M1_conn_{}_{}'.format(i,j))
                    Scoord = tmp3[0]['_XY_cent']
                            #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord = np.round(New_Scoord,2)
                    tmpXY.append(New_Scoord)
                        #Define
                    self._DesignParameter['_Cs_source_vss_M1_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = tmpXY
        
        ######################################################################################################################### CS_gate_connection_M3
            ########################################################################################################### CS_gate_connection_M3:Hrz_lenthen_M3
                ############################################################################################# CS_gate_connection_M3:Hrz_lenthen_M3:Find_most_far_coord
        tmp_max_coord = []
        # Column
        for j in range(0, len(_Array_Cs_NMOSNumberofGate[0])):
            tmp_log = []
            # Row
            for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                max_coord = tmp1[0]['_XY_left'][0]
                        
                #Index finder
                if (i==0):
                    max_coord_i_index = 0
                    max_coord_j_index = j
                elif max_coord < min(tmp_log):
                    max_coord_i_index = i
                    max_coord_j_index = j
                else :  
                    max_coord_i_index = max_coord_i_index
                    max_coord_j_index = max_coord_j_index
                    
                #tmp_log
                tmp_log.append(max_coord)
                
            #tmp_max_coord
            max_coord_index = [ max_coord_i_index,max_coord_j_index ]
            tmp_max_coord.append(max_coord_index)

                ############################################################################################# CS_gate_connection_M3:Hrz_lenthen_M3:Gen_M3
        # Row
        for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            # Column
            for j in range(0, len(_Array_Cs_NMOSNumberofGate[i])):

                #Define Boundary_element
                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)] = self._BoundaryElementDeclaration(
                                                                                                                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                                    _XWidth=None,
                                                                                                                    _YWidth=None,
                                                                                                                    _XYCoordinates=[ ],
                                                                                                                   )

                #Define Boundary_element _YWidth
                tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)]['_YWidth'] = tmp[0]['_Ywidth']

                #Define Boundary_element _XWidth
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')

                max_coordindate = tmp_max_coord[j]
                tmp2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(max_coordindate[0],max_coordindate[1]),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')

                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)]['_XWidth'] = abs( tmp2[0]['_XY_left'][0] - tmp1_1[0]['_XY_left'][0] )

                #Initialize coordinate
                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                target_coord = tmp1[0]['_XY_left']
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Cs_gate_M3_lengthen_{}_{}'.format(i,j))
                approaching_coord = tmp2[0]['_XY_right']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Cs_gate_M3_lengthen_{}_{}'.format(i,j))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Cs_gate_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = tmpXY


            ########################################################################################################### CS_gate_connection_M3:Vtc_M3
        #Pre-define
        vtc_M3_width = 150

        for j in range(0, len(_Array_Cs_NMOSNumberofGate[0])):

                #Define Boundary_element
                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                        )

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Unit_0_{}'.format(j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                tmp2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(len(_Array_Cs_NMOSNumberofGate)-1,j),'_Guardring','_Unit_Hrz_Pbody_lower','_Met1Layer')

                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)]['_XWidth'] = vtc_M3_width

                #Initialize coordinate
                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)]['_XYCoordinates'] = [[0,0]]		

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #xcoord
                max_coordindate = tmp_max_coord[j]
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(max_coordindate[0],max_coordindate[1]),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #ycoord
                tmp1_2 = self.get_param_KJH2('_Placement','_Unit_0_{}'.format(j),'_Nmos_sw_cs','_Cs_nmos_gate_Via2_M2M3','_Met3Layer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Cs_gate_M3_vtc_{}'.format(j))
                approaching_coord = tmp2[0]['_XY_up_right']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Cs_gate_M3_vtc_{}'.format(j))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Cs_gate_M3_vtc_{}'.format(j)]['_XYCoordinates'] = tmpXY


        

        ######################################################################################################################### SW_gate_connection_M3
            ########################################################################################################### SW_gate_connection_M3:Hrz_lenthen_M3
                ############################################################################################# SW_gate_connection_M3:Hrz_lenthen_M3:Find_most_far_coord
        tmp_max_coord1 = []
        # Column
        for j in range(0, len(_Array_Cs_NMOSNumberofGate[0])):
            tmp_log = []
            # Row
            for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                max_coord = tmp1[0]['_XY_left'][0]
                        
                #Index finder
                if (i==0):
                    max_coord_i_index = 0
                    max_coord_j_index = j
                elif max_coord > max(tmp_log):
                    max_coord_i_index = i
                    max_coord_j_index = j
                else :  
                    max_coord_i_index = max_coord_i_index
                    max_coord_j_index = max_coord_j_index
                    
                #tmp_log
                tmp_log.append(max_coord)
                
            #tmp_max_coord
            max_coord_index = [ max_coord_i_index,max_coord_j_index ]
            tmp_max_coord1.append(max_coord_index)

                ############################################################################################# SW_gate_connection_M3:_Hrz_lenthen_M3:_Gen_Hrz_M3
        # Row
        for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            # Column
            for j in range(0, len(_Array_Cs_NMOSNumberofGate[i])):

                #Define Boundary_element
                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)] = self._BoundaryElementDeclaration(
                                                                                                                    _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                                    _XWidth=None,
                                                                                                                    _YWidth=None,
                                                                                                                    _XYCoordinates=[ ],
                                                                                                                   )

                #Define Boundary_element _YWidth
                tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)]['_YWidth'] = tmp[0]['_Ywidth']

                #Define Boundary_element _XWidth
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')

                max_coordindate = tmp_max_coord1[j]
                tmp2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(max_coordindate[0],max_coordindate[1]),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')

                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)]['_XWidth'] = abs( tmp2[0]['_XY_left'][0] - tmp1_1[0]['_XY_left'][0] )

                #Initialize coordinate
                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                target_coord = tmp1[0]['_XY_right']
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Sw_drain_M3_lengthen_{}_{}'.format(i,j))
                approaching_coord = tmp2[0]['_XY_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Sw_drain_M3_lengthen_{}_{}'.format(i,j))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Sw_drain_M3_lengthen_{}_{}'.format(i,j)]['_XYCoordinates'] = tmpXY

            ########################################################################################################### SW_gate_connection_M3:_Vtc_M3
        #Pre-define
        vtc_M3_width2 = 150

        for j in range(0, len(_Array_Cs_NMOSNumberofGate[0])):

                #Define Boundary_element
                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                        )

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(len(_Array_Cs_NMOSNumberofGate)-1,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                tmp2 = self.get_param_KJH2('_Placement','_Unit_0_{}'.format(j),'_Guardring','_Unit_Hrz_Pbody_upper','_Met1Layer')

                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)]['_YWidth'] = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1] )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)]['_XWidth'] = vtc_M3_width2

                #Initialize coordinate
                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)]['_XYCoordinates'] = [[0,0]]		

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #xcoord
                max_coordindate = tmp_max_coord1[j]
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(max_coordindate[0],max_coordindate[1]),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                target_coordx = tmp1_1[0]['_XY_right'][0]
                            #ycoord
                tmp1_2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(len(_Array_Cs_NMOSNumberofGate)-1,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via2_M2M3','_Met3Layer')
                target_coordy = tmp1_2[0]['_XY_down'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Sw_drain_M3_vtc_{}'.format(j))
                approaching_coord = tmp2[0]['_XY_down_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Sw_drain_M3_vtc_{}'.format(j))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Sw_drain_M3_vtc_{}'.format(j)]['_XYCoordinates'] = tmpXY
        
        ######################################################################################################################### SW_gate_connection_M3M4
            ########################################################################################################### SW_gate_connection_M3M4:gen M4
        
        #Pre-defined
        M4_width = 150

        #Define Boundary_element
        self._DesignParameter['_Sw_drain_M4_hrz'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                    )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Sw_drain_M4_hrz']['_YWidth'] = M4_width

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Sw_drain_M3_vtc_0')
        tmp2 = self.get_param_KJH2('_Sw_drain_M3_vtc_{}'.format(len(_Array_Cs_NMOSNumberofGate[0])-1))

        self._DesignParameter['_Sw_drain_M4_hrz']['_XWidth'] = abs(tmp1[0]['_XY_left'][0] - tmp2[0]['_XY_right'][0])

        #Initialize coordinate
        self._DesignParameter['_Sw_drain_M4_hrz']['_XYCoordinates'] = [[0,0]]

        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_drain_M4_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_drain_M3_vtc_0') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_drain_M4_hrz')
        approaching_coord = tmp2[0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_drain_M4_hrz')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_drain_M4_hrz']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### SW_gate_connection_M3M4:gen M3
        
        #Pre-defined
        M3_width = 150

        #Define Boundary_element
        self._DesignParameter['_Sw_drain_M3_hrz'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                    )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Sw_drain_M3_hrz']['_YWidth'] = M3_width

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Sw_drain_M4_hrz')
        self._DesignParameter['_Sw_drain_M3_hrz']['_XWidth'] = tmp1[0]['_Xwidth']

        #Initialize coordinate
        self._DesignParameter['_Sw_drain_M3_hrz']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_drain_M3_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_drain_M4_hrz') 
        target_coord = tmp1[0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_drain_M3_hrz')  
        approaching_coord = tmp2[0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_drain_M3_hrz')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_drain_M3_hrz']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### SW_gate_connection_M3M4:gen Via3
        
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A10_ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4'] = self._SrefElementDeclaration(_DesignObj=A10_ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:_Sw_drain_hrz_Via3_M3M4'.format(_Name)))[0]

		#Define Sref Relection
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4']['_Angle'] = 0

        #Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH2('_Sw_drain_M3_hrz')
        tmp2 = self.get_param_KJH2('_Sw_drain_M4_hrz')

        Ovlpcoord = self.get_ovlp_coord_KJH(tmp1[0],tmp2[0])

        #Calcuate _ViaMet32Met4NumberOfCOX
        Xwidth = Ovlpcoord[0]['_Xwidth']
        Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
            #If Via is less than 2, Num_Via = 2
        if Num_Via_Xwidth < 2:
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = 2
        else:
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = Num_Via_Xwidth

        #Calcuate _ViaMet22Met3NumberOfCOY
        Ywidth = Ovlpcoord[0]['_Ywidth']
        Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
            #If Via is less than 2, Num_Via = 2
        if Num_Via_Ywidth < 2:
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = 2
        else:
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = Num_Via_Ywidth

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_drain_M3_hrz') 
        target_coord = tmp1[0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_drain_hrz_Via3_M3M4','_Met3Layer')  
        approaching_coord = tmp2[0]['_XY_down_right'] 
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_drain_hrz_Via3_M3M4')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_drain_hrz_Via3_M3M4']['_XYCoordinates'] = tmpXY
        
        ######################################################################################################################### Dummy_Process(SW_drain_M1_vss_connection)
            ########################################################################################################### Dummy_Process(SW_drain_M1_vss_connection):drain_M1_connection
        # Row
        for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            # Column
            for j in range(0, len(_Array_Cs_NMOSNumberofGate[i])):
                tmpXY=[]
                
                #If indicator == 1
                if _Array_dummy_indication[i][j] != 0:

                    #Define Boundary_element
                    self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)] = self._BoundaryElementDeclaration(
                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                        _XWidth=None,
                                                                                                        _YWidth=None,
                                                                                                        _XYCoordinates=[ ],
                                                                                                       )

                    #Define Boundary_element _XWidth
                    tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos','_Met1Layer')
                    self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)]['_XWidth'] = tmp[0]['_Xwidth']

                    #Define Boundary_element _YWidth
                    tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_M1')
                    tmp2 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Guardring','_Unit_Hrz_Pbody_upper','_Met1Layer')

                    self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)]['_YWidth'] = abs( tmp2[0]['_XY_down'][1] - tmp1[0]['_XY_up'][1] )

                    #Initialize coordinate
                    self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]

                    #Calculate Sref XYcoord
                    tmp = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_Via1_M1M2','_Met1Layer')


                    for k in range(0,len(tmp)):
                            #initialized Sref coordinate
                        self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = [[0,0]]
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH2('_Placement','_Unit_{}_{}'.format(i,j),'_Nmos_sw_cs','_Sw_nmos_drain_M1')
                        target_coord = tmp1[k]['_XY_up_left']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH2('_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j))
                        approaching_coord = tmp2[0]['_XY_down_left']
                                #Sref coord
                        tmp3 = self.get_param_KJH2('_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j))
                        Scoord = tmp3[0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord = np.round(New_Scoord,2)
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_Sw_dummy_M1_vss_conn_{}_{}'.format(i,j)]['_XYCoordinates'] = tmpXY

            ########################################################################################################### Dummy_Process(SW_drain_M1_vss_connection):delete_drain_via3
        # Row
        for i in range(0, len(_Array_Cs_NMOSNumberofGate)):
            # Column
            for j in range(0, len(_Array_Cs_NMOSNumberofGate[i])):
                tmpXY=[]
                
                #If indicator == 1
                if _Array_dummy_indication[i][j] != 0:
                    
                    del self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}_{}'.format(i,j)]['_DesignObj']._DesignParameter['_Nmos_sw_cs']['_DesignObj']._DesignParameter['_Sw_nmos_drain_Via2_M2M3']


        
        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_D_building_block'
    cellname = 'D03_routing_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

        # ## Guardring_gen
            # Current source nmos
        # _Array_Cs_NMOSNumberofGate    =[ [2,2,2,2,4, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2],[2,2,2,2,2, 2,2,2,2,2, 2,2,2,2,2] ], 
        # _Array_Cs_NMOSChannelWidth    =[ [1000,1300,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        # _Array_Cs_NMOSChannellength   =[ [200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200],[200,200,200,200,200, 200,200,200,200,200, 200,200,200,200,200] ] ,
        # _Array_Cs_NMOSDummy           =True, 
        # _Array_Cs_GateSpacing         =None, 
        # _Array_Cs_SDWidth             =None,
        # _Array_Cs_XVT                 ='SLVT',
        # _Array_Cs_PCCrit              =None, 

            # SW nmos
        # _Array_Sw_NMOSNumberofGate    =[ [1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1],[1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1] ] ,
        # _Array_Sw_NMOSChannelWidth    =[ [1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000],[1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000, 1000,1000,1000,1000,1000] ] ,
        # _Array_Sw_NMOSChannellength   =[ [30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30],[30,30,30,30,30, 30,30,30,30,30, 30,30,30,30,30] ] ,
        # _Array_Sw_NMOSDummy           =True, 
        # _Array_Sw_GateSpacing         =None,
        # _Array_Sw_SDWidth             =None, 
        # _Array_Sw_XVT                 ='SLVT',
        # _Array_Sw_PCCrit              =None,

            # Vtc_pbodycontact
        # _Vtc_PbodyContCount_of_Width = 2,

            # Hrz_pbodycontact
        # _Hrz_PbodyContCount_of_Width = 4,


        # ## Guardring_gen
            # Current source nmos
         _Array_Cs_NMOSNumberofGate    =[ [2,2,2,4],[2,2,2,2], ], 
         _Array_Cs_NMOSChannelWidth    =[ [1000,1300,1000,1000,],[1000,1000,1000,1000,],] ,
         _Array_Cs_NMOSChannellength   =[ [200,200,200,200,],[200,200,200,200,], ] ,
         _Array_Cs_NMOSDummy           =True, 
         _Array_Cs_GateSpacing         =None, 
         _Array_Cs_SDWidth             =None,
         _Array_Cs_XVT                 ='SLVT',
         _Array_Cs_PCCrit              =None, 

            # SW nmos
         _Array_Sw_NMOSNumberofGate    =[ [1,1,1,2,],[1,3,3,1,], ] ,
         _Array_Sw_NMOSChannelWidth    =[ [1000,1000,1000,1000,],[1000,1000,1000,1000,],] ,
         _Array_Sw_NMOSChannellength   =[ [30,30,80,30,],[30,30,100,30,],] ,
         _Array_Sw_NMOSDummy           =True, 
         _Array_Sw_GateSpacing         =None,
         _Array_Sw_SDWidth             =None, 
         _Array_Sw_XVT                 ='SLVT',
         _Array_Sw_PCCrit              =None,

            # Vtc_pbodycontact
         _Vtc_PbodyContCount_of_Width = 3,

            # Hrz_pbodycontact
         _Hrz_PbodyContCount_of_Width = 3,

            # Dummy_indication
         _Array_dummy_indication = [ [0,1,0,1],[0,0,1,0], ],

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
    LayoutObj = _routing(_DesignParameter=None, _Name=cellname)
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
