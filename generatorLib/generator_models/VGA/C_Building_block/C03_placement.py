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
class _placement(StickDiagram_KJH0._StickDiagram_KJH):

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
        
            ##################################################################################################################### Gen_unit
        for i in range(0,len(_Array_NMOSNumberofGate)):
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C02_unit._unit._ParametersForDesignCalculation)
            _Caculation_Parameters['_Polyres_R_X_width']  	= _Array_Polyres_R_X_width[i]
            _Caculation_Parameters['_Polyres_R_Y_length']  	= _Array_Polyres_R_Y_length[i]
            _Caculation_Parameters['_Polyres_CoXNum'] 	    = _Array_Polyres_CoXNum[i]
            _Caculation_Parameters['_Polyres_CoYNum']  		= _Array_Polyres_CoYNum[i]
            _Caculation_Parameters['_Polyres_N_Parallel']  	= _Array_Polyres_N_Parallel[i]
            _Caculation_Parameters['_Polyres_Dummy']  		= _Array_Polyres_Dummy[i]
            _Caculation_Parameters['_Poly_up_connect']  	= _Array_Poly_up_connect[i]

            _Caculation_Parameters['_NMOSNumberofGate']  	= _Array_NMOSNumberofGate[i]
            _Caculation_Parameters['_NMOSChannelWidth']  	= _Array_NMOSChannelWidth[i]
            _Caculation_Parameters['_NMOSChannellength'] 	= _Array_NMOSChannellength[i]
            _Caculation_Parameters['_NMOSDummy']  			= _Array_NMOSDummy[i]
            _Caculation_Parameters['_GateSpacing']  		= _Array_GateSpacing[i]
            _Caculation_Parameters['_SDWidth']  			= _Array_SDWidth[i]
            _Caculation_Parameters['_XVT']  				= _Array_XVT[i]
            _Caculation_Parameters['_PCCrit']  				= _Array_PCCrit[i]
            
            _Caculation_Parameters['_Array_vtc_btw_res_sw_PbodyContCount_of_Width'] = _Array_vtc_btw_res_sw_PbodyContCount_of_Width[i]

            #Generate Sref
            self._DesignParameter['_Unit_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=C02_unit._unit( _DesignParameter=None, _Name='{}:_Unit_{}'.format(_Name,i)))[0]

            #Define Sref Relection
            self._DesignParameter['_Unit_{}'.format(i)]['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Unit_{}'.format(i)]['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates']=[[0, 0]]    
        
            #################################################################################################################### Cal_Max_unit_xlength
        
        unit_xlength=[]
        for i in range(0,len(_Array_NMOSNumberofGate)):
        
            #res only
            if _Array_NMOSNumberofGate[i] == 0:
            
                if _Array_Polyres_Dummy[i] == True:
                    tmp = self.get_param_KJH2('_Unit_{}'.format(i),'_Cent_res','_Polyres_dummy','PRES_boundary_0')
                    tmp_length = abs( tmp[-1]['_XY_right'][0] - tmp[0]['_XY_left'][0])
                    unit_xlength.append(tmp_length)
                else:
                    tmp = self.get_param_KJH2('_Unit_{}'.format(i),'_Cent_res','_Polyres','PRES_boundary_0')
                    tmp_length = abs( tmp[-1]['_XY_right'][0] - tmp[0]['_XY_left'][0])
                    unit_xlength.append(tmp_length)
            
            #nomal unit
            else:

                if _Array_Polyres_Dummy[i] == True:
                    tmp1 = self.get_param_KJH2('_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','PRES_boundary_0')
                    tmp2 = self.get_param_KJH2('_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','PRES_boundary_0')
                    
                    tmp_length = abs( tmp2[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0])
                    unit_xlength.append(tmp_length)
                    
                else:
                    tmp1 = self.get_param_KJH2('_Unit_{}'.format(i),'_Left_res','_Polyres','PRES_boundary_0')
                    tmp2 = self.get_param_KJH2('_Unit_{}'.format(i),'_Right_res','_Polyres','PRES_boundary_0')
                    
                    tmp_length = abs( tmp2[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0])
                    unit_xlength.append(tmp_length)
            
            #################################################################################################################### Ycoord_Placement
            for i in range(0,len(_Array_hrz_btw_units_PbodyContCount_of_Width)):
            
                # last pbody:do not create unit--------------------------------------------------------------------------------------------------------------------------------
                ###################################################################################################### Ycoord_Placement:Gen_Pbody
                if i == len(_Array_hrz_btw_units_PbodyContCount_of_Width)-1:
                    #pre-defined
                    ydistance2 = 250
                    
                    #res Xwidth
                    _Hrz_btw_unit_PbodyCont_Length = max(unit_xlength)
                    
                    #If Hrz
                    _PbodyContact_NumberOfPbodyCOX = (int(((_Hrz_btw_unit_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Array_hrz_btw_units_PbodyContCount_of_Width[i]) + 0
                    _PbodyContact_NumberOfPbodyCOY = _Array_hrz_btw_units_PbodyContCount_of_Width[i]
                    _PbodyContact_Met1XWidth       = None
                    _PbodyContact_Met1YWidth       = None

                    #Define _PbodyContact input parameter
                    _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
                    _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
                    _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
                    _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
                    _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

                    #Define _PbodyContact Sref
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Hrz_btw_unit_PbodyContact_{}'.format(_Name,i)))[0] 

                    #Define Sref Relection
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_Reflect'] = [0, 0, 0] 
                    
                    #Define Sref Angle
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_Angle'] = 0 

                    #Define NMOS_DEFAULT layer
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 
                    
                    #Calculate Sref XYcoord 
                    tmpXY=[]
                        #initialized Sref coordinate
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                        #Calculate
                            #Target_coord
                    if _Array_NMOSNumberofGate[i-1] == 0:
                        tmp1_3 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Cent_res','_Polyres','PRES_boundary_0')
                        target_coord = tmp1_3[0]['_XY_down'][1]
                    else:
                        tmp1_1 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Left_res','_Polyres','PRES_boundary_0')
                        tmp1_2 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Nmos_sw','_Nmos_hrz_poly')
                        
                        if tmp1_1[0]['_XY_down'][1] < tmp1_2[0]['_XY_down'][1]:
                            target_coord = tmp1_1[0]['_XY_down']
                        else:
                            target_coord = tmp1_2[0]['_XY_down']
                        
                            #Approaching_coord
                    tmp2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')  
                    approaching_coord = tmp2[0]['_XY_up']  
                    
                            #Sref coord
                    tmp3 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(i))
                    Scoord = tmp3[0]['_XY_cent']
                    
                            #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord[1] = New_Scoord[1] - ydistance2
                    tmpXY.append(New_Scoord)
                        #Define
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_XYCoordinates'][0][1] = New_Scoord[1]
                    
                # first ~ (last-1):create pbody and unit
                else:
                ###################################################################################################### Ycoord_Placement:Gen_Pbody
                    #pre-defined
                    ydistance3 = 250
                    
                    #res Xwidth
                    _Hrz_btw_unit_PbodyCont_Length = max(unit_xlength)
                    
                    #If Hrz
                    _PbodyContact_NumberOfPbodyCOX = (int(((_Hrz_btw_unit_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Array_hrz_btw_units_PbodyContCount_of_Width[i]) + 0
                    _PbodyContact_NumberOfPbodyCOY = _Array_hrz_btw_units_PbodyContCount_of_Width[i]
                    _PbodyContact_Met1XWidth       = None
                    _PbodyContact_Met1YWidth       = None

                    #Define _PbodyContact input parameter
                    _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
                    _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
                    _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
                    _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
                    _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

                    #Define _PbodyContact Sref
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Hrz_btw_unit_PbodyContact_{}'.format(_Name,i)))[0] 

                    #Define Sref Relection
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_Reflect'] = [0, 0, 0] 
                    
                    #Define Sref Angle
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_Angle'] = 0 

                    #Define NMOS_DEFAULT layer
                    self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 

                    #Define NMOS_DEFAULT coordinate
                        
                    if i == 0:
                        #initialized Sref coordinate
                        self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_XYCoordinates']=[[0, 0]]
                    else:
                        #Calculate Sref XYcoord 
                        tmpXY=[]
                            #initialized Sref coordinate
                        self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                            #Calculate
                                #Target_coord
                        if _Array_NMOSNumberofGate[i-1] == 0:
                            tmp1_3 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Cent_res','_Polyres','PRES_boundary_0')
                            target_coord = tmp1_3[0]['_XY_down'][1]
                        else:
                            tmp1_1 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Left_res','_Polyres','PRES_boundary_0')
                            tmp1_2 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Nmos_sw','_Nmos_hrz_poly')
                            
                            if tmp1_1[0]['_XY_down'][1] < tmp1_2[0]['_XY_down'][1]:
                                target_coord = tmp1_1[0]['_XY_down']
                            else:
                                target_coord = tmp1_2[0]['_XY_down']
                            
                                #Approaching_coord
                        tmp2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')  
                        approaching_coord = tmp2[0]['_XY_up']  
                        
                                #Sref coord
                        tmp3 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(i))
                        Scoord = tmp3[0]['_XY_cent']
                        
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord[1] = New_Scoord[1] - ydistance3
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_Hrz_btw_unit_PbodyContact_{}'.format(i)]['_XYCoordinates'][0][1] = New_Scoord[1]

                ###################################################################################################### Ycoord_Placement:place_unit
                    #pre-defined
                    ydistance = 250
                
                    #Calculate Sref XYcoord ---------------------------------------------------------------------------------------------------------------------------------------------
                    tmpXY=[]
                        #initialized Sref coordinate
                    self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                        #Calculate
                            #Target_coord
                    tmp1 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(i),'_ODLayer')
                    target_coord = tmp1[0]['_XY_down']
                    
                            #Approaching_coord: most upper one
                    if _Array_NMOSNumberofGate[i] == 0:
                        tmp2_3 = self.get_param_KJH2('_Unit_{}'.format(i),'_Cent_res','_Polyres','PRES_boundary_0')
                        approaching_coord = tmp2_3[0]['_XY_up']
                    else:
                        tmp2_1 = self.get_param_KJH2('_Unit_{}'.format(i),'_Left_res','_Polyres','PRES_boundary_0')
                        tmp2_2 = self.get_param_KJH2('_Unit_{}'.format(i),'_Nmos_sw','_Nmos_drain_m2_hrz')
                    
                        if tmp2_1[0]['_XY_up'][1] > tmp2_2[0]['_XY_up'][1]:
                            approaching_coord = tmp2_1[0]['_XY_up']
                        else:
                            approaching_coord = tmp2_2[0]['_XY_up']  
                    
                            #Sref coord
                    tmp3 = self.get_param_KJH2('_Unit_{}'.format(i))
                    Scoord = tmp3[0]['_XY_cent']
                    
                            #Cal
                    New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                    New_Scoord[1] = New_Scoord[1] - ydistance
                    tmpXY.append(New_Scoord)
                        #Define
                    self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates'][0][1] = New_Scoord[1]
                    
            ##################################################################################################################### Gen_Vtc_left_pbody
        #pre-define
        xdistance1 = 250
            
        #_Array_vtc_btw_res_sw_PbodyCont_Length
        tmp1 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_hrz_btw_units_PbodyContCount_of_Width)-1),'_ODLayer')
        _Array_vtc_left_PbodyCont_Length = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1] )

        #If Vert                
        _PbodyContact_NumberOfPbodyCOX = _Vtc_left_PbodyContCount_of_Width
        _PbodyContact_NumberOfPbodyCOY = (int(((_Array_vtc_left_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Vtc_left_PbodyContCount_of_Width) + 0
        _PbodyContact_Met1XWidth       = None
        _PbodyContact_Met1YWidth       = None
        
        #Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

        #Define _PbodyContact Sref
        self._DesignParameter['_Vtc_left_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Vtc_left_PbodyContact'.format(_Name)))[0] 

        #Define Sref Relection
        self._DesignParameter['_Vtc_left_PbodyContact']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_Vtc_left_PbodyContact']['_Angle'] = 0 

        #Define NMOS_DEFAULT layer
        self._DesignParameter['_Vtc_left_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Vtc_left_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coordx
        tmp = max(unit_xlength)
        tmp_index = unit_xlength.index(tmp)
        
                    #res only
        if _Array_NMOSNumberofGate[tmp_index] == 0:
        
            if _Array_Polyres_Dummy[tmp_index] == True:
                tmp = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Cent_res','_Polyres_dummy','PRES_boundary_0')
                target_coordx = tmp[0]['_XY_left'][0]
            else:
                tmp = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Cent_res','_Polyres','PRES_boundary_0')
                target_coordx = tmp[0]['_XY_left'][0]
        
                    #nomal unit
        else:

            if _Array_Polyres_Dummy[tmp_index] == True:
                tmp1 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Left_res','_Polyres_dummy','PRES_boundary_0')
                tmp2 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Right_res','_Polyres_dummy','PRES_boundary_0')
                
                target_coordx = tmp1[0]['_XY_left'][0]
                
            else:
                tmp1 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Left_res','_Polyres','PRES_boundary_0')
                tmp2 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Right_res','_Polyres','PRES_boundary_0')
                
                target_coordx = tmp1[0]['_XY_left'][0]
                
                #Target_coordy
        tmp1_1 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp1_2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_hrz_btw_units_PbodyContCount_of_Width)-1),'_ODLayer')
        target_coordy = 0.5 * ( tmp1_1[0]['_XY_up'][1] + tmp1_2[0]['_XY_down'][1] )
                
        target_coord = [target_coordx,target_coordy] 
        
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Vtc_left_PbodyContact','_ODLayer')  
        approaching_coord = tmp2[0]['_XY_right']  
        
                #Sref coord
        tmp3 = self.get_param_KJH2('_Vtc_left_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
        
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord[0] = New_Scoord[0] - xdistance1
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Vtc_left_PbodyContact']['_XYCoordinates'] = tmpXY
        
            ##################################################################################################################### Gen_Vtc_right_pbody
        #pre-define
        xdistance2 = 250
            
        #_Array_vtc_btw_res_sw_PbodyCont_Length
        tmp1 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_hrz_btw_units_PbodyContCount_of_Width)-1),'_ODLayer')
        _Array_vtc_right_PbodyCont_Length = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1] )

        #If Vert                
        _PbodyContact_NumberOfPbodyCOX = _Vtc_right_PbodyContCount_of_Width
        _PbodyContact_NumberOfPbodyCOY = (int(((_Array_vtc_right_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Vtc_right_PbodyContCount_of_Width) + 0
        _PbodyContact_Met1XWidth       = None
        _PbodyContact_Met1YWidth       = None
        
        #Define _PbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

        #Define _PbodyContact Sref
        self._DesignParameter['_Vtc_right_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Vtc_right_PbodyContact'.format(_Name)))[0] 

        #Define Sref Relection
        self._DesignParameter['_Vtc_right_PbodyContact']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_Vtc_right_PbodyContact']['_Angle'] = 0 

        #Define NMOS_DEFAULT layer
        self._DesignParameter['_Vtc_right_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Vtc_right_PbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coordx
        tmp = max(unit_xlength)
        tmp_index = unit_xlength.index(tmp)
        
                    #res only
        if _Array_NMOSNumberofGate[tmp_index] == 0:
        
            if _Array_Polyres_Dummy[tmp_index] == True:
                tmp = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Cent_res','_Polyres_dummy','PRES_boundary_0')
                target_coordx = tmp[-1]['_XY_right'][0]
            else:
                tmp = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Cent_res','_Polyres','PRES_boundary_0')
                target_coordx = tmp[-1]['_XY_right'][0]
        
                    #nomal unit
        else:

            if _Array_Polyres_Dummy[tmp_index] == True:
                tmp1 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Left_res','_Polyres_dummy','PRES_boundary_0')
                tmp2 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Right_res','_Polyres_dummy','PRES_boundary_0')
                
                target_coordx = tmp2[-1]['_XY_right'][0]
                
            else:
                tmp1 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Left_res','_Polyres','PRES_boundary_0')
                tmp2 = self.get_param_KJH2('_Unit_{}'.format(tmp_index),'_Right_res','_Polyres','PRES_boundary_0')
                
                target_coordx = tmp2[-1]['_XY_right'][0]
                
                #Target_coordy
        tmp1_1 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_0','_ODLayer')
        tmp1_2 = self.get_param_KJH2('_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_hrz_btw_units_PbodyContCount_of_Width)-1),'_ODLayer')
        target_coordy = 0.5 * ( tmp1_1[0]['_XY_up'][1] + tmp1_2[0]['_XY_down'][1] )
                
        target_coord = [target_coordx,target_coordy] 
        
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Vtc_right_PbodyContact','_ODLayer')  
        approaching_coord = tmp2[0]['_XY_left']  
        
                #Sref coord
        tmp3 = self.get_param_KJH2('_Vtc_right_PbodyContact')
        Scoord = tmp3[0]['_XY_cent']
        
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord[0] = New_Scoord[0] + xdistance2
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Vtc_right_PbodyContact']['_XYCoordinates'] = tmpXY        
                
        ################################################################################################################################### Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_C_building_block'
    cellname = 'C03_placement_99'
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
    LayoutObj = _placement(_DesignParameter=None, _Name=cellname)
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
