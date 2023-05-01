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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C00_polyseriesstripe
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C01_nmos_sw
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C03_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C04_routing_guardring


############################################################################################################################################################ Class_HEADER
class _routing_guardring(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
                                            
                                            #polyres
                                            _Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
                                            _Array_Polyres_R_Y_length = [600,800,850,500],
                                            _Array_Polyres_CoXNum     = [None,None,None,None],
                                            _Array_Polyres_CoYNum     = [None,None,None,None],
                                            _Array_Polyres_N_Parallel = [5,4,2,1],
                                            _Array_Polyres_Dummy      = [True,True,True,True],
                                            _Array_Poly_up_connect    = [True,True,True,True],
                                           
                                            #nmos_sw
                                            _Array_NMOSNumberofGate     = [0, 3, 1, 0],
                                            _Array_NMOSChannelWidth     = [500, 700, 600, 300],
                                            _Array_NMOSChannellength    = [30,30,30,30],
                                            _Array_NMOSDummy            = [True,True,True,True],
                                            _Array_GateSpacing          = [None,None,None,None],
                                            _Array_SDWidth              = [None,None,None,None],
                                            _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
                                            _Array_PCCrit               = [None,None,None,None],
                                            
                                            #vtc pbodycontact btw res and sw
                                            _Array_vtc_btw_res_sw_PbodyContCount_of_Width = [2,3,8,4],
                                            
                                            #hrz pbodycontact btw unit
                                            _Array_hrz_btw_units_PbodyContCount_of_Width = [4,3,2,2,5],
                                            
                                            #vtc left pbodycontact
                                            _Vtc_left_PbodyContCount_of_Width = 3, 
                                            
                                            #vtc right pbodycontact
                                            _Vtc_right_PbodyContCount_of_Width = 6, 

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

    ################################################################################################################################################## _CalculateDesignParameter
    def _CalculateDesignParameter(self,

                                        #polyres
                                        _Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
                                        _Array_Polyres_R_Y_length = [600,800,850,500],
                                        _Array_Polyres_CoXNum     = [None,None,None,None],
                                        _Array_Polyres_CoYNum     = [None,None,None,None],
                                        _Array_Polyres_N_Parallel = [5,4,2,1],
                                        _Array_Polyres_Dummy      = [True,True,True,True],
                                        _Array_Poly_up_connect    = [True,True,True,True],
                                       
                                        #nmos_sw
                                        _Array_NMOSNumberofGate     = [0, 3, 1, 0],
                                        _Array_NMOSChannelWidth     = [500, 700, 600, 300],
                                        _Array_NMOSChannellength    = [30,30,30,30],
                                        _Array_NMOSDummy            = [True,True,True,True],
                                        _Array_GateSpacing          = [None,None,None,None],
                                        _Array_SDWidth              = [None,None,None,None],
                                        _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
                                        _Array_PCCrit               = [None,None,None,None],
                                        
                                        #vtc pbodycontact btw res and sw
                                        _Array_vtc_btw_res_sw_PbodyContCount_of_Width = [2,3,8,4],
                                        
                                        #hrz pbodycontact btw unit
                                        _Array_hrz_btw_units_PbodyContCount_of_Width = [4,3,2,2,5],
                                        
                                        #vtc left pbodycontact
                                        _Vtc_left_PbodyContCount_of_Width = 3, 
                                        
                                        #vtc right pbodycontact
                                        _Vtc_right_PbodyContCount_of_Width = 6, 
                                 ):

        #################################################################################################################################### Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        #Load DRC library
        _DRCobj = DRC.DRC()

        #Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ################################################################################################################################### Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')
        

            ##################################################################################################################### Gen_C03_placement
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(C03_placement._placement._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Polyres_R_X_width']  	= _Array_Polyres_R_X_width
        _Caculation_Parameters['_Array_Polyres_R_Y_length']  	= _Array_Polyres_R_Y_length
        _Caculation_Parameters['_Array_Polyres_CoXNum'] 	    = _Array_Polyres_CoXNum
        _Caculation_Parameters['_Array_Polyres_CoYNum']  		= _Array_Polyres_CoYNum
        _Caculation_Parameters['_Array_Polyres_N_Parallel']  	= _Array_Polyres_N_Parallel
        _Caculation_Parameters['_Array_Polyres_Dummy']  		= _Array_Polyres_Dummy
        _Caculation_Parameters['_Array_Poly_up_connect']  		= _Array_Poly_up_connect

        _Caculation_Parameters['_Array_NMOSNumberofGate']  	= _Array_NMOSNumberofGate
        _Caculation_Parameters['_Array_NMOSChannelWidth']  	= _Array_NMOSChannelWidth
        _Caculation_Parameters['_Array_NMOSChannellength'] 	= _Array_NMOSChannellength
        _Caculation_Parameters['_Array_NMOSDummy']  		= _Array_NMOSDummy
        _Caculation_Parameters['_Array_GateSpacing']  		= _Array_GateSpacing
        _Caculation_Parameters['_Array_SDWidth']  			= _Array_SDWidth
        _Caculation_Parameters['_Array_XVT']  				= _Array_XVT
        _Caculation_Parameters['_Array_PCCrit']  			= _Array_PCCrit

        _Caculation_Parameters['_Array_vtc_btw_res_sw_PbodyContCount_of_Width'] = _Array_vtc_btw_res_sw_PbodyContCount_of_Width

        _Caculation_Parameters['_Array_hrz_btw_units_PbodyContCount_of_Width'] 	= _Array_hrz_btw_units_PbodyContCount_of_Width

        _Caculation_Parameters['_Vtc_left_PbodyContCount_of_Width'] 			= _Vtc_left_PbodyContCount_of_Width

        _Caculation_Parameters['_Vtc_right_PbodyContCount_of_Width'] 			= _Vtc_right_PbodyContCount_of_Width

        #Generate Sref
        self._DesignParameter['_Placement'] = self._SrefElementDeclaration(_DesignObj=C03_placement._placement( _DesignParameter=None, _Name='{}:_Placement'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Placement']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Placement']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Placement']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Placement']['_XYCoordinates']=[[0, 0]]

            ##################################################################################################################### extension _Hzr_btw_unit_Pbodycontact_{}
                ####################################################################################################### extension _Hzr_btw_unit_Pbodycontact_{}: _ODLayer
        for i in range(0,len(_Array_hrz_btw_units_PbodyContCount_of_Width)):
            #Define Boundary_element
            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                            _XWidth=None,
                                                                                                                            _YWidth=None,
                                                                                                                            _XYCoordinates=[ ],
                                                                                                                           )

            #Define Boundary_element _YWidth
            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_YWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']

            #Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_ODLayer')
            tmp2 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_ODLayer')

            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

            #Initialize coordinate
            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
                        #Target_coordx
            tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_ODLayer')
            target_coordx = tmp1_1[0]['_XY_left'][0]
                        #Target_coordy
            tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
            target_coordy = tmp1_2[0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                    #Approaching_coord
            tmp2 = self.get_param_KJH2('_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i),)
            approaching_coord = tmp2[0]['_XY_up_left']
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i))
            Scoord = tmp3[0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Extension_ODLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Hzr_btw_unit_Pbodycontact_{}: _PPLayer
        for i in range(0,len(_Array_hrz_btw_units_PbodyContCount_of_Width)):
            #Define Boundary_element
            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                            _XWidth=None,
                                                                                                                            _YWidth=None,
                                                                                                                            _XYCoordinates=[ ],
                                                                                                                           )

            #Define Boundary_element _YWidth
            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_YWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']

            #Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_PPLayer')
            tmp2 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_PPLayer')

            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

            #Initialize coordinate
            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
                        #Target_coordx
            tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_PPLayer')
            target_coordx = tmp1_1[0]['_XY_left'][0]
                        #Target_coordy
            tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_PPLayer')
            target_coordy = tmp1_2[0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                    #Approaching_coord
            tmp2 = self.get_param_KJH2('_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i),)
            approaching_coord = tmp2[0]['_XY_up_left']
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i))
            Scoord = tmp3[0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Extension_PPLayer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Hzr_btw_unit_Pbodycontact_{}: _M1Layer
        for i in range(0,len(_Array_hrz_btw_units_PbodyContCount_of_Width)):
            #Define Boundary_element
            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                            _XWidth=None,
                                                                                                                            _YWidth=None,
                                                                                                                            _XYCoordinates=[ ],
                                                                                                                           )

            #Define Boundary_element _YWidth
            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_YWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            #Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_Met1Layer')
            tmp2 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_Met1Layer')

            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XWidth'] = abs( tmp2[0]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

            #Initialize coordinate
            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
                        #Target_coordx
            tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_Met1Layer')
            target_coordx = tmp1_1[0]['_XY_left'][0]
                        #Target_coordy
            tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_Met1Layer')
            target_coordy = tmp1_2[0]['_XY_up'][1]

            target_coord = [target_coordx,target_coordy]
                    #Approaching_coord
            tmp2 = self.get_param_KJH2('_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i),)
            approaching_coord = tmp2[0]['_XY_up_left']
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i))
            Scoord = tmp3[0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Extension_Met1Layer_Hrz_btw_unit_Pbodycontact_{}'.format(i)]['_XYCoordinates'] = tmpXY


            ##################################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact
                ####################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact: _ODLayer
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_ODLayer')

                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_res_sw_PbodyContact','_ODLayer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact: _PPLayer
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_PPLayer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_PPLayer')

                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_res_sw_PbodyContact','_PPLayer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_PPLayer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact: _M1Layer _Met1Layer METAL1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_Met1Layer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_Met1Layer')

                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_res_sw_PbodyContact','_Met1Layer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_Met1Layer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_res_sw_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY


            ##################################################################################################################### extension _Unit_{} _Vtc_btw_sw_res_PbodyContact
                ####################################################################################################### extension _Unit_{} _Vtc_btw_sw_res_PbodyContact: _ODLayer
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_ODLayer')

                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_sw_res_PbodyContact','_ODLayer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_ODLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact: _PPLayer
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_PPLayer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_PPLayer')

                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_sw_res_PbodyContact','_PPLayer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_PPLayer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_PPLayer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Unit_{} _Vtc_btw_res_sw_PbodyContact: _M1Layer _Met1Layer METAL1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            if _Array_NMOSNumberofGate[i] != 0:
                #Define Boundary_element
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                                        _XWidth=None,
                                                                                                                                        _YWidth=None,
                                                                                                                                        _XYCoordinates=[ ],
                                                                                                                                       )

                #Define Boundary_element _XWidth
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

                #Define Boundary_element _YWidth
                tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_Met1Layer')
                tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i+1),'_Met1Layer')

                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

                #Initialize coordinate
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                    #Calculate
                        #Target_coord
                            #Target_coordx
                tmp1_1 = self.get_param_KJH2('_Placement','_Unit_{}'.format(i),'_Vtc_btw_sw_res_PbodyContact','_Met1Layer')
                target_coordx = tmp1_1[0]['_XY_left'][0]
                            #Target_coordy
                tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(i),'_Met1Layer')
                target_coordy = tmp1_2[0]['_XY_up'][1]

                target_coord = [target_coordx,target_coordy]
                        #Approaching_coord
                tmp2 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i),)
                approaching_coord = tmp2[0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i))
                Scoord = tmp3[0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                tmpXY.append(New_Scoord)
                    #Define
                self._DesignParameter['_Extension_Met1Layer_Vtc_btw_sw_res_PbodyContact_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ##################################################################################################################### extension _Vtc_left_PbodyContact
                ####################################################################################################### extension _Vtc_left_PbodyContact:Metal1
        #Define Boundary_element
        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_left_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_Met1Layer')

        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_Met1Layer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_Met1Layer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_left_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_left_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_Met1Layer_Vtc_left_PbodyContact']['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Vtc_left_PbodyContact:PIMP
        #Define Boundary_element
        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_left_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_PPLayer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_PPLayer')

        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_PPLayer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_PPLayer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_PPLayer_Vtc_left_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_PPLayer_Vtc_left_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_PPLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Vtc_left_PbodyContact:ODLyaer
        #Define Boundary_element
        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_left_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_ODLayer')

        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_left_PbodyContact','_ODLayer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_ODLayer_Vtc_left_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_ODLayer_Vtc_left_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_ODLayer_Vtc_left_PbodyContact']['_XYCoordinates'] = tmpXY

            ##################################################################################################################### extension _Vtc_right_PbodyContact
                ####################################################################################################### extension _Vtc_left_PbodyContact:Metal1
        #Define Boundary_element
        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_right_PbodyContact']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_Met1Layer')

        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_Met1Layer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_Met1Layer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_right_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_Met1Layer_Vtc_right_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_Met1Layer_Vtc_right_PbodyContact']['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Vtc_right_PbodyContact:PIMP
        #Define Boundary_element
        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_right_PbodyContact']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_PPLayer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_PPLayer')

        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_PPLayer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_PPLayer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_PPLayer_Vtc_right_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_PPLayer_Vtc_right_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_PPLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = tmpXY

                ####################################################################################################### extension _Vtc_right_PbodyContact:ODLyaer
        #Define Boundary_element
        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact'] = self._BoundaryElementDeclaration(
                                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                                _XWidth=None,
                                                                                                                _YWidth=None,
                                                                                                                _XYCoordinates=[ ],
                                                                                                               )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact']['_XWidth'] = self._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Vtc_right_PbodyContact']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_ODLayer')

        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

        #Initialize coordinate
        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Target_coordx
        tmp1_1 = self.get_param_KJH2('_Placement','_Vtc_right_PbodyContact','_ODLayer')
        target_coordx = tmp1_1[0]['_XY_left'][0]
                    #Target_coordy
        tmp1_2 = self.get_param_KJH2('_Placement','_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        target_coordy = tmp1_2[0]['_XY_up'][1]

        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Extension_ODLayer_Vtc_right_PbodyContact')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Extension_ODLayer_Vtc_right_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Extension_ODLayer_Vtc_right_PbodyContact']['_XYCoordinates'] = tmpXY
                
        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_C_building_block'
    cellname = 'C04_routing_guardring_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

                            #polyres
                            _Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000, 1800, 2300],
                            _Array_Polyres_R_Y_length = [600,800,850,500,700,500],
                            _Array_Polyres_CoXNum     = [None,None,None,None,None,None],
                            _Array_Polyres_CoYNum     = [None,None,None,None,None,None],
                            _Array_Polyres_N_Parallel = [3,2,2,1,1,1],
                            _Array_Polyres_Dummy      = [True,True,True,True,True,True],
                            _Array_Poly_up_connect    = [True,True,True,True,True,True],
                           
                            #nmos_sw
                            _Array_NMOSNumberofGate     = [2, 3, 1, 0, 10, 1],
                            _Array_NMOSChannelWidth     = [500, 700, 600, 300, 800, 1000],
                            _Array_NMOSChannellength    = [30,30,30,30,150,80],
                            _Array_NMOSDummy            = [True,True,True,True,True,True],
                            _Array_GateSpacing          = [None,None,None,None,None,None],
                            _Array_SDWidth              = [None,None,None,None,None,None],
                            _Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT','SLVT','SLVT'],
                            _Array_PCCrit               = [None,None,None,None,None,None],
                            
                            #vtc pbodycontact btw res and sw
                            _Array_vtc_btw_res_sw_PbodyContCount_of_Width = [3,3,3,3,3,5],
                            
                            #hrz pbodycontact btw unit
                            _Array_hrz_btw_units_PbodyContCount_of_Width = [2,2,2,2,2,2,2],
                            
                            #vtc left pbodycontact
                            _Vtc_left_PbodyContCount_of_Width = 8, 
                            
                            #vtc right pbodycontact
                            _Vtc_right_PbodyContCount_of_Width = 10, 
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
    LayoutObj = _routing_guardring(_DesignParameter=None, _Name=cellname)
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
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
