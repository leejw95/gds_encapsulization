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
class _unit(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
                                            
                                            #poly res
                                            _Polyres_R_X_width  = 2500,
                                            _Polyres_R_Y_length = 1500,
                                            _Polyres_CoXNum     = None,
                                            _Polyres_CoYNum     = None,
                                            _Polyres_N_Parallel = 2,
                                            _Polyres_Dummy      = False,
                                            _Poly_up_connect 	= True,
                                            
                                            #nmos sw
                                            _NMOSNumberofGate=20,
                                            _NMOSChannelWidth=1000,
                                            _NMOSChannellength=30,
                                            _NMOSDummy=True,
                                            _GateSpacing=None,
                                            _SDWidth=None,
                                            _XVT='SLVT',
                                            _PCCrit=None,
                                            
                                            #num pbody contact btw res and sw
                                            _Array_vtc_btw_res_sw_PbodyContCount_of_Width = 3,

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

                                        #poly res
                                        _Polyres_R_X_width  = 2500,
                                        _Polyres_R_Y_length = 1500,
                                        _Polyres_CoXNum     = None,
                                        _Polyres_CoYNum     = None,
                                        _Polyres_N_Parallel = 2,
                                        _Polyres_Dummy      = False,
                                        _Poly_up_connect 	= True,
                                        
                                        #nmos sw
                                        _NMOSNumberofGate=20,
                                        _NMOSChannelWidth=1000,
                                        _NMOSChannellength=30,
                                        _NMOSDummy=True,
                                        _GateSpacing=None,
                                        _SDWidth=None,
                                        _XVT='SLVT',
                                        _PCCrit=None,
                                        
                                        #num pbody contact btw res and sw
                                        _Array_vtc_btw_res_sw_PbodyContCount_of_Width = 3,
                                        
                                        
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
        
        if _NMOSNumberofGate != 0:
        
            ##################################################################################################################### Gen_nmos_sw
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C01_nmos_sw._nmos_sw._ParametersForDesignCalculation)
            _Caculation_Parameters['_NMOSNumberofGate']  	= _NMOSNumberofGate
            _Caculation_Parameters['_NMOSChannelWidth']  	= _NMOSChannelWidth
            _Caculation_Parameters['_NMOSChannellength'] 	= _NMOSChannellength
            _Caculation_Parameters['_NMOSDummy']  			= _NMOSDummy
            _Caculation_Parameters['_GateSpacing']  		= _GateSpacing
            _Caculation_Parameters['_SDWidth']  			= _SDWidth
            _Caculation_Parameters['_XVT']  				= _XVT
            _Caculation_Parameters['_PCCrit']  				= _PCCrit

            #Generate Sref
            self._DesignParameter['_Nmos_sw'] = self._SrefElementDeclaration(_DesignObj=C01_nmos_sw._nmos_sw( _DesignParameter=None, _Name='{}:_Nmos'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Nmos_sw']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Nmos_sw']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Nmos_sw']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Nmos_sw']['_XYCoordinates']=[[0, 0]]    
            
            ##################################################################################################################### Gen_res_for_cal
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C00_polyseriesstripe._polyseriesstripe._ParametersForDesignCalculation)
            _Caculation_Parameters['_Polyres_R_X_width']  	= _Polyres_R_X_width
            _Caculation_Parameters['_Polyres_R_Y_length']  	= _Polyres_R_Y_length
            _Caculation_Parameters['_Polyres_CoXNum'] 	    = _Polyres_CoXNum
            _Caculation_Parameters['_Polyres_CoYNum']  		= _Polyres_CoYNum
            _Caculation_Parameters['_Polyres_N_Parallel']  	= _Polyres_N_Parallel
            _Caculation_Parameters['_Polyres_Dummy']  		= _Polyres_Dummy
            _Caculation_Parameters['_Poly_up_connect']  	= _Poly_up_connect

            #Generate Sref
            self._DesignParameter['_Res_for_cal'] = self._SrefElementDeclaration(_DesignObj=C00_polyseriesstripe._polyseriesstripe( _DesignParameter=None, _Name='{}:_Res_for_cal'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Res_for_cal']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Res_for_cal']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Res_for_cal']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Res_for_cal']['_XYCoordinates']=[[0, 0]]
            
            ##################################################################################################################### Gen_left_pbody
            #pre-define
            xdistance = 250
                
            #_Array_vtc_btw_res_sw_PbodyCont_Length
            tmp1 = self.get_param_KJH2('_Res_for_cal','_Polyres','PRES_boundary_0')
                    
            tmp2 = self.get_param_KJH2('_Nmos_sw','_Nmos_drain_m2_hrz')
            tmp3 = self.get_param_KJH2('_Nmos_sw','_Nmos_hrz_poly')
            
            tmp4 = tmp1[0]['_Ywidth']
            tmp5 = abs ( tmp2[0]['_XY_up'][1] - tmp3[0]['_XY_down'][1] )
                
            if tmp4>tmp5:
                _Array_vtc_btw_res_sw_PbodyCont_Length = tmp4
            else:
                _Array_vtc_btw_res_sw_PbodyCont_Length = tmp5
            
            #delete _Res_for_cal
            del self._DesignParameter['_Res_for_cal']
            
            #If Vert                
            _PbodyContact_NumberOfPbodyCOX = _Array_vtc_btw_res_sw_PbodyContCount_of_Width
            _PbodyContact_NumberOfPbodyCOY = (int(((_Array_vtc_btw_res_sw_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Array_vtc_btw_res_sw_PbodyContCount_of_Width) + 0
            _PbodyContact_Met1XWidth       = None
            _PbodyContact_Met1YWidth       = None
            
            #Define _PbodyContact input parameter
            _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
            _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
            _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
            _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
            _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

            #Define _PbodyContact Sref
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Vtc_btw_res_sw_PbodyContact'.format(_Name)))[0] 

            #Define Sref Relection
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_Reflect'] = [0, 0, 0] 
            
            #Define Sref Angle
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_Angle'] = 0 

            #Define NMOS_DEFAULT layer
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            tmp1_1 = self.get_param_KJH2('_Nmos_sw','_Nmos_drain_m2_hrz')
            tmp1_2 = self.get_param_KJH2('_Nmos_sw','_Nmos_hrz_poly')
            target_coordy = 0.5*( tmp1_1[0]['_XY_up'][1] + tmp1_2[0]['_XY_down'][1] ) 
            
            tmp1_3 = self.get_param_KJH2('_Nmos_sw','_Nmos','_PODummyLayer')
            target_coordx = tmp1_3[0]['_XY_left'][0]
            
            target_coord = [target_coordx,target_coordy]
            
                    #Approaching_coord
            tmp2 = self.get_param_KJH2('_Vtc_btw_res_sw_PbodyContact','_ODLayer')  
            approaching_coord = tmp2[0]['_XY_right']  
            
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Vtc_btw_res_sw_PbodyContact')
            Scoord = tmp3[0]['_XY_cent']
            
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0]- xdistance
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Vtc_btw_res_sw_PbodyContact']['_XYCoordinates'] = tmpXY
            
            ##################################################################################################################### Gen_right_pbody
            #_Array_vtc_btw_res_sw_PbodyCont_Length
            _Array_vtc_btw_res_sw_PbodyCont_Length = _Array_vtc_btw_res_sw_PbodyCont_Length
            
            #If Vert                
            _PbodyContact_NumberOfPbodyCOX = _Array_vtc_btw_res_sw_PbodyContCount_of_Width
            _PbodyContact_NumberOfPbodyCOY = (int(((_Array_vtc_btw_res_sw_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Array_vtc_btw_res_sw_PbodyContCount_of_Width) + 0
            _PbodyContact_Met1XWidth       = None
            _PbodyContact_Met1YWidth       = None
            
            #Define _PbodyContact input parameter
            _Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
            _Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
            _Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
            _Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
            _Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

            #Define _PbodyContact Sref
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_Vtc_btw_sw_res_PbodyContact'.format(_Name)))[0] 

            #Define Sref Relection
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_Reflect'] = [0, 0, 0] 
            
            #Define Sref Angle
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_Angle'] = 0 

            #Define NMOS_DEFAULT layer
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) 

            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            tmp1_1 = self.get_param_KJH2('_Nmos_sw','_Nmos_drain_m2_hrz')
            tmp1_2 = self.get_param_KJH2('_Nmos_sw','_Nmos_hrz_poly')
            target_coordy = 0.5*( tmp1_1[0]['_XY_up'][1] + tmp1_2[0]['_XY_down'][1] ) 
            
            tmp1_3 = self.get_param_KJH2('_Nmos_sw','_Nmos','_PODummyLayer')
            target_coordx = tmp1_3[-1]['_XY_right'][0]
            
            target_coord = [target_coordx,target_coordy]
            
                    #Approaching_coord
            tmp2 = self.get_param_KJH2('_Vtc_btw_sw_res_PbodyContact','_ODLayer')  
            approaching_coord = tmp2[0]['_XY_left']  
            
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Vtc_btw_sw_res_PbodyContact')
            Scoord = tmp3[0]['_XY_cent']
            
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] + xdistance
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Vtc_btw_sw_res_PbodyContact']['_XYCoordinates'] = tmpXY
           
            ##################################################################################################################### Gen_left_res
            #pre-defined    
            xdistance2 = 250
           
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C00_polyseriesstripe._polyseriesstripe._ParametersForDesignCalculation)
            _Caculation_Parameters['_Polyres_R_X_width']  	= _Polyres_R_X_width
            _Caculation_Parameters['_Polyres_R_Y_length']  	= _Polyres_R_Y_length
            _Caculation_Parameters['_Polyres_CoXNum'] 	    = _Polyres_CoXNum
            _Caculation_Parameters['_Polyres_CoYNum']  		= _Polyres_CoYNum
            _Caculation_Parameters['_Polyres_N_Parallel']  	= _Polyres_N_Parallel
            _Caculation_Parameters['_Polyres_Dummy']  		= _Polyres_Dummy
            _Caculation_Parameters['_Poly_up_connect']      = _Poly_up_connect
            

            #Generate Sref
            self._DesignParameter['_Left_res'] = self._SrefElementDeclaration(_DesignObj=C00_polyseriesstripe._polyseriesstripe( _DesignParameter=None, _Name='{}:_Left_res'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Left_res']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Left_res']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Left_res']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Left_res']['_XYCoordinates']=[[0, 0]]
            
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Left_res']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH2('_Vtc_btw_res_sw_PbodyContact','_ODLayer')
            target_coord = tmp1[0]['_XY_left']
            
                    #Approaching_coord
            if _Polyres_Dummy == True:
                tmp2 = self.get_param_KJH2('_Left_res','_Polyres_dummy','PRES_boundary_0')  
                approaching_coord = tmp2[-1]['_XY_right'] 
            else:
                tmp2 = self.get_param_KJH2('_Left_res','_Polyres','PRES_boundary_0')  
                approaching_coord = tmp2[-1]['_XY_right']  
            
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Left_res')
            Scoord = tmp3[0]['_XY_cent']
            
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] - xdistance2
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Left_res']['_XYCoordinates'] = tmpXY

            ##################################################################################################################### Gen_right_res
            #pre-defined    
            xdistance3 = 250
           
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C00_polyseriesstripe._polyseriesstripe._ParametersForDesignCalculation)
            _Caculation_Parameters['_Polyres_R_X_width']  	= _Polyres_R_X_width
            _Caculation_Parameters['_Polyres_R_Y_length']  	= _Polyres_R_Y_length
            _Caculation_Parameters['_Polyres_CoXNum'] 	    = _Polyres_CoXNum
            _Caculation_Parameters['_Polyres_CoYNum']  		= _Polyres_CoYNum
            _Caculation_Parameters['_Polyres_N_Parallel']  	= _Polyres_N_Parallel
            _Caculation_Parameters['_Polyres_Dummy']  		= _Polyres_Dummy
            _Caculation_Parameters['_Poly_up_connect']  	= _Poly_up_connect

            #Generate Sref
            self._DesignParameter['_Right_res'] = self._SrefElementDeclaration(_DesignObj=C00_polyseriesstripe._polyseriesstripe( _DesignParameter=None, _Name='{}:_Right_res'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Right_res']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Right_res']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Right_res']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Right_res']['_XYCoordinates']=[[0, 0]]
            
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Right_res']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH2('_Vtc_btw_sw_res_PbodyContact','_ODLayer')
            target_coord = tmp1[0]['_XY_right']
            
                    #Approaching_coord
            if _Polyres_Dummy == True:
                tmp2 = self.get_param_KJH2('_Right_res','_Polyres_dummy','PRES_boundary_0')  
                approaching_coord = tmp2[0]['_XY_left'] 
            else:
                tmp2 = self.get_param_KJH2('_Right_res','_Polyres','PRES_boundary_0')  
                approaching_coord = tmp2[0]['_XY_left']  
            
                    #Sref coord
            tmp3 = self.get_param_KJH2('_Right_res')
            Scoord = tmp3[0]['_XY_cent']
            
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0] + xdistance3
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Right_res']['_XYCoordinates'] = tmpXY
        
        else:
        
            ##################################################################################################################### Gen_cent_res
           
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy(C00_polyseriesstripe._polyseriesstripe._ParametersForDesignCalculation)
            _Caculation_Parameters['_Polyres_R_X_width']  	= _Polyres_R_X_width
            _Caculation_Parameters['_Polyres_R_Y_length']  	= _Polyres_R_Y_length
            _Caculation_Parameters['_Polyres_CoXNum'] 	    = _Polyres_CoXNum
            _Caculation_Parameters['_Polyres_CoYNum']  		= _Polyres_CoYNum
            _Caculation_Parameters['_Polyres_N_Parallel']  	= _Polyres_N_Parallel
            _Caculation_Parameters['_Polyres_Dummy']  		= _Polyres_Dummy
            _Caculation_Parameters['_Poly_up_connect']  	= _Poly_up_connect

            #Generate Sref
            self._DesignParameter['_Cent_res'] = self._SrefElementDeclaration(_DesignObj=C00_polyseriesstripe._polyseriesstripe( _DesignParameter=None, _Name='{}:_Cent_res'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_Cent_res']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_Cent_res']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_Cent_res']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_Cent_res']['_XYCoordinates']=[[0, 0]]
            
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_Cent_res']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
            target_coord = [0,0]
 
                    #Approaching_coord
            if _Polyres_Dummy == True:
                tmp2_1 = self.get_param_KJH2('_Cent_res','_Polyres_dummy','PRES_boundary_0')
                
                approaching_coordx = 0.5 * ( tmp2_1[-1]['_XY_right'][0] + tmp2_1[0]['_XY_left'][0] ) 
                approaching_coordy = 0.5 * ( tmp2_1[0]['_XY_up'][1] + tmp2_1[0]['_XY_down'][1] ) 
                
                approaching_coord = [approaching_coordx,approaching_coordy]
            else:
                tmp2 = self.get_param_KJH2('_Cent_res','_Polyres','PRES_boundary_0')

                approaching_coordx = 0.5 * ( tmp2[-1]['_XY_right'][0] + tmp2[0]['_XY_left'][0] ) 
                approaching_coordy = 0.5 * ( tmp2[0]['_XY_up'][1] + tmp2[0]['_XY_down'][1] ) 
                
                approaching_coord = [approaching_coordx,approaching_coordy]                

                    #Sref coord
            tmp3 = self.get_param_KJH2('_Cent_res')
            Scoord = tmp3[0]['_XY_cent']
            
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord[0] = New_Scoord[0]
            tmpXY.append(New_Scoord)
                #Define
            self._DesignParameter['_Cent_res']['_XYCoordinates'] = tmpXY

        ################################################################################################################################### Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_C_building_block'
    cellname = 'C02_unit_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

                            #poly res
                            _Polyres_R_X_width  = 2500,
                            _Polyres_R_Y_length = 1500,
                            _Polyres_CoXNum     = None,
                            _Polyres_CoYNum     = None,
                            _Polyres_N_Parallel = 3,
                            _Polyres_Dummy      = False,
                            _Poly_up_connect 	= True,
                            
                            #nmos sw
                            _NMOSNumberofGate=5,
                            _NMOSChannelWidth=1000,
                            _NMOSChannellength=30,
                            _NMOSDummy=True,
                            _GateSpacing=None,
                            _SDWidth=None,
                            _XVT='SLVT',
                            _PCCrit=None,
                            
                            #num pbody contact btw res and sw
                            _Array_vtc_btw_res_sw_PbodyContCount_of_Width = 3,
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
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
