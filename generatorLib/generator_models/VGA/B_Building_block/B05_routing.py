'''


'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A00_NMOSWithDummy_v2
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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B00_polyresparallel
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B01_pmos_sw
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B02_res_and_sw_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B03_ycoord_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B04_xcoord_placement

############################################################################################################################################################ Class_HEADER
class _routing(StickDiagram_KJH1._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                            #polyres
                                            _Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
                                            _Array_Polyres_R_Y_length = [600,800,850,500],
                                            _Array_Polyres_CoXNum     = [None,None,None,None],
                                            _Array_Polyres_CoYNum     = [None,None,None,None],
                                            _Array_Polyres_Dummy      = True,
                                            _Array_Polyres_N_Parallel = [2,2,1,4],

                                            #pmos_sw
                                            _Array_PMOSNumberofGate     = [0, 3, 1, 1],
                                            _Array_PMOSChannelWidth     = [500, 700, 600, 300],
                                            _Array_PMOSChannellength    = [30,30,30,30],
                                            _Array_PMOSDummy            = [True,True,True,True],
                                            _Array_GateSpacing          = [None,None,None,None],
                                            _Array_SDWidth              = [None,None,None,None],
                                            _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
                                            _Array_PCCrit               = [None,None,None,None],

                                            #vtc nbodycontact
                                            _Array_vtc_btw_res_sw_NbodyContCount_of_Width = [5,3,8,2],

                                            #hrz nbodycontact
                                            _Array_hrz_NbodyContCount_of_Width_upper_unit = [4,2,2,3,5],

                                            #left vtc nbodycontact
                                            _Left_NbodyContCount_of_Width = 3,

                                            #left vtc nbodycontact
                                            _Right_NbodyContCount_of_Width = 7,

                                           )

    #Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                        )

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    def _CalculateDesignParameter(self,

                                        #polyres
                                        _Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
                                        _Array_Polyres_R_Y_length = [600,800,850,500],
                                        _Array_Polyres_CoXNum     = [None,None,None,None],
                                        _Array_Polyres_CoYNum     = [None,None,None,None],
                                        _Array_Polyres_Dummy      = True,
                                        _Array_Polyres_N_Parallel = [2,2,1,4],

                                        #pmos_sw
                                        _Array_PMOSNumberofGate     = [0, 3, 1, 1],
                                        _Array_PMOSChannelWidth     = [500, 700, 600, 300],
                                        _Array_PMOSChannellength    = [30,30,30,30],
                                        _Array_PMOSDummy            = [True,True,True,True],
                                        _Array_GateSpacing          = [None,None,None,None],
                                        _Array_SDWidth              = [None,None,None,None],
                                        _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
                                        _Array_PCCrit               = [None,None,None,None],

                                        #vtc nbodycontact
                                        _Array_vtc_btw_res_sw_NbodyContCount_of_Width = [5,3,8,2],

                                        #hrz nbodycontact
                                        _Array_hrz_NbodyContCount_of_Width_upper_unit = [4,2,2,3,5],

                                        #left vtc nbodycontact
                                        _Left_NbodyContCount_of_Width = 3,

                                        #left vtc nbodycontact
                                        _Right_NbodyContCount_of_Width = 7,

                                 ):

################################################################################################################################################## Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        #Load DRC library
        _DRCobj = DRC.DRC()

        #Define _name
        _Name = self._DesignParameter['_Name']['_Name']

############################################################################################################################################################ CALCULATION START
        print ('#########################################################################################################')
        print ('                                      Calculation Start                                                  ')
        print ('#########################################################################################################')

        ################################################################################################################################### _Array_with_ring
        print('##     _Array_with_ring   ##')

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( B04_xcoord_placement._xcoord_placement._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Polyres_R_X_width']                        = _Array_Polyres_R_X_width
        _Caculation_Parameters['_Array_Polyres_R_Y_length']                       = _Array_Polyres_R_Y_length
        _Caculation_Parameters['_Array_Polyres_CoXNum']                           = _Array_Polyres_CoXNum
        _Caculation_Parameters['_Array_Polyres_CoYNum']                           = _Array_Polyres_CoYNum
        _Caculation_Parameters['_Array_Polyres_Dummy']                            = _Array_Polyres_Dummy
        _Caculation_Parameters['_Array_Polyres_N_Parallel']                       = _Array_Polyres_N_Parallel
        _Caculation_Parameters['_Array_PMOSNumberofGate']                         = _Array_PMOSNumberofGate
        _Caculation_Parameters['_Array_PMOSChannelWidth']                         = _Array_PMOSChannelWidth
        _Caculation_Parameters['_Array_PMOSChannellength']                        = _Array_PMOSChannellength
        _Caculation_Parameters['_Array_PMOSDummy']                                = _Array_PMOSDummy
        _Caculation_Parameters['_Array_GateSpacing']                              = _Array_GateSpacing
        _Caculation_Parameters['_Array_SDWidth']                                  = _Array_SDWidth
        _Caculation_Parameters['_Array_XVT']                                      = _Array_XVT
        _Caculation_Parameters['_Array_PCCrit']                                   = _Array_PCCrit
        _Caculation_Parameters['_Array_vtc_btw_res_sw_NbodyContCount_of_Width']   = _Array_vtc_btw_res_sw_NbodyContCount_of_Width
        _Caculation_Parameters['_Array_hrz_NbodyContCount_of_Width_upper_unit']   = _Array_hrz_NbodyContCount_of_Width_upper_unit
        _Caculation_Parameters['_Left_NbodyContCount_of_Width']                   = _Left_NbodyContCount_of_Width
        _Caculation_Parameters['_Right_NbodyContCount_of_Width']                  = _Right_NbodyContCount_of_Width

        #Generate Sref
        self._DesignParameter['_Array_with_ring'] = self._SrefElementDeclaration(_DesignObj=B04_xcoord_placement._xcoord_placement( _DesignParameter=None, _Name='{}:_Array_with_ring'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Array_with_ring']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Array_with_ring']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Array_with_ring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Array_with_ring']['_XYCoordinates']=[[0, 0]]

        ################################################################################################################################### connect res and sw
        print('##     connect res and sw   ##')

        for i in range(0,len(_Array_PMOSNumberofGate)):
            if _Array_PMOSNumberofGate[i] == 0:
                pass
            else:
                #Define Boundary_element
                self._DesignParameter['_M3_conn_res_sw_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                           )

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Polyres','_Polyres_Via2_M2M3','_Met3Layer')
                tmp2 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos_drain_Via2_M2M3','_Met3Layer')

                    #up coord
                if tmp1[-1]['_XY_up'][1] > tmp2[0]['_XY_up'][1]:
                    up_tmp = tmp1[-1]['_XY_up'][1]
                else:
                    up_tmp = tmp2[0]['_XY_up'][1]

                    #down coord
                if tmp1[-1]['_XY_down'][1] > tmp2[0]['_XY_down'][1]:
                    down_tmp = tmp2[0]['_XY_down'][1]
                else:
                    down_tmp = tmp1[-1]['_XY_down'][1]

                self._DesignParameter['_M3_conn_res_sw_{}'.format(i)]['_YWidth'] = up_tmp - down_tmp

                #Define Boundary_element _XWidth
                self._DesignParameter['_M3_conn_res_sw_{}'.format(i)]['_XWidth'] = abs( tmp1[-1]['_XY_left'][0] - tmp2[-1]['_XY_right'][0] )

                #Define Boundary_element _XYCoordinates
                    #initialization
                self._DesignParameter['_M3_conn_res_sw_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                    #Calculate Boundary_element XYcoord
                    #up coord
                if tmp1[0]['_XY_up'][1] > tmp2[0]['_XY_up'][1]:
                    tmp3 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Polyres','_Polyres_Via2_M2M3','_Met3Layer')
                    target_coord = tmp3[-1]['_XY_up_left']
                    approaching_type = '_XY_up_left'
                else:
                    tmp3 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos_drain_Via2_M2M3','_Met3Layer')
                    target_coord = tmp3[-1]['_XY_up_right']
                    approaching_type = '_XY_up_right'

                B_XWidth = self.getXWidth('_M3_conn_res_sw_{}'.format(i))
                B_YWidth = self.getYWidth('_M3_conn_res_sw_{}'.format(i))

                New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

                self._DesignParameter['_M3_conn_res_sw_{}'.format(i)]['_XYCoordinates'] = [New_Bcoord]

        ################################################################################################################################### connect resistors
        print('##     connect resistors   ##')

        #Pre-defined
        _M3_conn_res_res_xwidth = 200

        #Define Boundary_element
        self._DesignParameter['_M3_conn_res_res'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL3'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL3'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_0','_Polyres','_Polyres_Via2_M2M3','_Met3Layer')
        tmp2 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(len(_Array_PMOSNumberofGate)-1),'_Polyres','_Polyres_Via2_M2M3','_Met3Layer')

        self._DesignParameter['_M3_conn_res_res']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Define Boundary_element _XWidth
        self._DesignParameter['_M3_conn_res_res']['_XWidth'] = _M3_conn_res_res_xwidth

        #Calculate Boundary_element XYcoord
        tmp3 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_0','_Polyres','_Polyres_Via2_M2M3','_Met3Layer')

        target_coord = tmp3[0]['_XY_up_right']
        approaching_type = '_XY_up_right'
        B_XWidth = self.getXWidth('_M3_conn_res_res')
        B_YWidth = self.getYWidth('_M3_conn_res_res')

        New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

        self._DesignParameter['_M3_conn_res_res']['_XYCoordinates'] = [New_Bcoord]

        ################################################################################################################################### Pmos sw source(or resis only) VDD connection(Ring)
        print('##     Pmos sw source power connection   ##')
        for i in range(0,len(_Array_PMOSNumberofGate)):
            # Resistor only
            if _Array_PMOSNumberofGate[i] == 0:
                #Define Boundary_element
                self._DesignParameter['_M1_conn_resonly_power_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )
                
                #Define Boundary_element _XWidth
                tmp = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','_Met1Layer')
                self._DesignParameter['_M1_conn_resonly_power_{}'.format(i)]['_XWidth'] = tmp[0]['_Ywidth']
                
                #Define Boundary_element _YWidth
                tmp2 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','_Met1Layer')
                tmp3 = self.get_param_KJH2('_Array_with_ring','_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
                self._DesignParameter['_M1_conn_resonly_power_{}'.format(i)]['_YWidth'] = abs ( tmp3[0]['_XY_cent'][1] - tmp2[0]['_XY_cent'][1] )

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_M1_conn_resonly_power_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','_Met1Layer')  		
                target_coord = tmp1[-1]['_XY_cent']  
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_M1_conn_resonly_power_{}'.format(i))  
                approaching_coord = tmp2[0]['_XY_down']   
                        #Sref coord
                tmp3 = self.get_param_KJH2('_M1_conn_resonly_power_{}'.format(i)) 
                Scoord = tmp3[0]['_XY_cent']  
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_M1_conn_resonly_power_{}'.format(i)]['_XYCoordinates'] = tmpXY
                
            else:
                #Define Boundary_element
                self._DesignParameter['_M1_conn_pmos_power_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

                #Define Boundary_element _XWidth
                tmp = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_Met1Layer')
                self._DesignParameter['_M1_conn_pmos_power_{}'.format(i)]['_XWidth'] = tmp[0]['_Xwidth']

                #Define Boundary_element _YWidth
                tmp2 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_Met1Layer')
                tmp3 = self.get_param_KJH2('_Array_with_ring','_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
                self._DesignParameter['_M1_conn_pmos_power_{}'.format(i)]['_YWidth'] = abs ( tmp3[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Cal M1 coord: Source & Drain Zigzag placing
                    #Define flag
                flag = 1

                tmpXY = []
                for j in range(0,len(tmp2)):
                    #Source
                    if flag == 1:
                        #Calculate Boundary_element XYcoord
                        tmp1 = self.get_param_KJH2('_Array_with_ring','_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_Met1Layer')

                        target_coord = tmp1[j]['_XY_down']
                        approaching_type = '_XY_down'
                        B_XWidth = self.getXWidth('_M1_conn_pmos_power_{}'.format(i))
                        B_YWidth = self.getYWidth('_M1_conn_pmos_power_{}'.format(i))

                        New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)
                        tmpXY.append(New_Bcoord)

                        flag = -1
                    #Drain
                    else:
                        #tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                        #tmpXY.append(tmp3)
                        flag = +1

                self._DesignParameter['_M1_conn_pmos_power_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Resistor connection M5
        #Define Boundary_element
        self._DesignParameter['_M5_conn_res_res'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_M5_conn_res_res']['_YWidth'] = self._DesignParameter['_M3_conn_res_res']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_M5_conn_res_res']['_XWidth'] = self._DesignParameter['_M3_conn_res_res']['_XWidth']

        #Calculate Boundary_element XYcoord
        self._DesignParameter['_M5_conn_res_res']['_XYCoordinates'] = self._DesignParameter['_M3_conn_res_res']['_XYCoordinates']

            ## ################################################################################################################### Resistor connection _ViaM3M5
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 3
        _Caculation_Parameters['_Layer2'] 	= 5
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_ViaM3M5'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_ViaM3M5'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_ViaM3M5']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_ViaM3M5']['_Angle'] = 0

        #Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH3('_M3_conn_res_res')
        tmp2 = self.get_param_KJH3('_M5_conn_res_res')
        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0],tmp2[0][0])

        #Calcuate _COX and _COY
        _COX, _COY= self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'],Ovlpcoord[0]['_Ywidth'],None)  ## None or 'MinEnclosureX' or 'MinEnclosureY'

        #Define _COX and _COY
        _Caculation_Parameters['_COX'] 		= _COX
        _Caculation_Parameters['_COY'] 		= _COY

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_ViaM3M5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ViaM3M5']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_M5_conn_res_res') 
        target_coord = tmp1[0][0]['_XY_cent']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ViaM3M5','_ViaM4M5','_Met5Layer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ViaM3M5')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ViaM3M5']['_XYCoordinates'] = tmpXY

        print('###############      For Debugging      ##################')


        #Delete
        #del self._DesignParameter['_Polyres_for_coordcal']


############################################################################################################################################################ CALCULATION END
        print ('#########################################################################################################')
        print ('                                      Calculation   END                                                  ')
        print ('#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_B_building_block'
    cellname = 'B05_routing_91'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
                            
                            #polyres
                            # _Array_Polyres_R_X_width  = [500, 1500, 1000, 800,],
                            # _Array_Polyres_R_Y_length = [600, 800, 850, 1000,],
                            # _Array_Polyres_CoXNum     = [None,None,None,None],
                            # _Array_Polyres_CoYNum     = [None,None,None,None],
                            # _Array_Polyres_Dummy      = False,
                            # _Array_Polyres_N_Parallel = [1,1,1,1],

                            #pmos_sw
                            # _Array_PMOSNumberofGate     = [0, 3, 6, 2],
                            # _Array_PMOSChannelWidth     = [500, 700, 600, 400],
                            # _Array_PMOSChannellength    = [30,30,30,80],
                            # _Array_PMOSDummy            = [True,True,True,True],
                            # _Array_GateSpacing          = [None,None,None,None],
                            # _Array_SDWidth              = [None,None,None,None],
                            # _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
                            # _Array_PCCrit               = [None,None,None,None],

                            #vtc nbodycontact
                            # _Array_vtc_btw_res_sw_NbodyContCount_of_Width = [4,4,4,4],

                            #hrz nbodycontact
                            # _Array_hrz_NbodyContCount_of_Width_upper_unit = [3,3,3,3,3],

                            #left vtc nbodycontact
                            # _Left_NbodyContCount_of_Width = 3,

                            #left vtc nbodycontact
                            # _Right_NbodyContCount_of_Width = 3,
                            
                            #polyres
                            _Array_Polyres_R_X_width  = [500, 1500, 1000, 800,1100,],
                            _Array_Polyres_R_Y_length = [600, 800, 850, 1000,700,],
                            _Array_Polyres_CoXNum     = [None,None,None,None,None,],
                            _Array_Polyres_CoYNum     = [None,None,None,None,None,],
                            _Array_Polyres_Dummy      = False,
                            _Array_Polyres_N_Parallel = [2,1,1,1,1],

                            #pmos_sw
                            _Array_PMOSNumberofGate     = [0, 3, 6, 2, 8,],
                            _Array_PMOSChannelWidth     = [500, 700, 600, 400, 580],
                            _Array_PMOSChannellength    = [30,30,30,80,30,],
                            _Array_PMOSDummy            = [True,True,True,True,True],
                            _Array_GateSpacing          = [None,None,None,None,None],
                            _Array_SDWidth              = [None,None,None,None,None],
                            _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT','SLVT'],
                            _Array_PCCrit               = [None,None,None,None,None],

                            #vtc nbodycontact
                            _Array_vtc_btw_res_sw_NbodyContCount_of_Width = [4,4,4,4,2],

                            #hrz nbodycontact
                            _Array_hrz_NbodyContCount_of_Width_upper_unit = [3,3,3,3,3,4],

                            #left vtc nbodycontact
                            _Left_NbodyContCount_of_Width = 3,

                            #left vtc nbodycontact
                            _Right_NbodyContCount_of_Width = 3,
                            
                            #polyres
                            # _Array_Polyres_R_X_width  = [500, 1500, 1000,  ],
                            # _Array_Polyres_R_Y_length = [600, 800, 850, ],
                            # _Array_Polyres_CoXNum     = [None,None,None,],
                            # _Array_Polyres_CoYNum     = [None,None,None,],
                            # _Array_Polyres_Dummy      = False,
                            # _Array_Polyres_N_Parallel = [1,1,1,],

                            #pmos_sw
                            # _Array_PMOSNumberofGate     = [0, 3, 6, ],
                            # _Array_PMOSChannelWidth     = [500, 700, 600, ],
                            # _Array_PMOSChannellength    = [30,30,30,],
                            # _Array_PMOSDummy            = [True,True,True,],
                            # _Array_GateSpacing          = [None,None,None,],
                            # _Array_SDWidth              = [None,None,None,],
                            # _Array_XVT                  = ['SLVT','SLVT','SLVT',],
                            # _Array_PCCrit               = [None,None,None,],

                            #vtc nbodycontact
                            # _Array_vtc_btw_res_sw_NbodyContCount_of_Width = [4,4,4,4],

                            #hrz nbodycontact
                            # _Array_hrz_NbodyContCount_of_Width_upper_unit = [3,3,3,3,3],

                            #left vtc nbodycontact
                            # _Left_NbodyContCount_of_Width = 3,

                            #left vtc nbodycontact
                            # _Right_NbodyContCount_of_Width = 3,
                        )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck =1

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
    #Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
