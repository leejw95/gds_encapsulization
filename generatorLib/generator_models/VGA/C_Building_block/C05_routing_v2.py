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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C00_polyseriesstripe
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C01_nmos_sw
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C03_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C04_routing_guardring


############################################################################################################################################################ Class_HEADER
class _routing(StickDiagram_KJH1._StickDiagram_KJH):
    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                                # polyres
                                                _Array_Polyres_R_X_width=[1000, 1000, 1500, 2000, ],
                                                _Array_Polyres_R_Y_length=[600, 800, 850, 500],
                                                _Array_Polyres_CoXNum=[None, None, None, None],
                                                _Array_Polyres_CoYNum=[None, None, None, None],
                                                _Array_Polyres_N_Parallel=[5, 4, 2, 1],
                                                _Array_Polyres_Dummy=[True, True, True, True],
                                                _Array_Poly_up_connect=[True, True, True, True],

                                                # nmos_sw
                                                _Array_NMOSNumberofGate=[0, 3, 1, 0],
                                                _Array_NMOSChannelWidth=[500, 700, 600, 300],
                                                _Array_NMOSChannellength=[30, 30, 30, 30],
                                                _Array_NMOSDummy=[True, True, True, True],
                                                _Array_GateSpacing=[None, None, None, None],
                                                _Array_SDWidth=[None, None, None, None],
                                                _Array_XVT=['SLVT', 'SLVT', 'SLVT', 'SLVT'],
                                                _Array_PCCrit=[None, None, None, None],

                                                # vtc pbodycontact btw res and sw
                                                _Array_vtc_btw_res_sw_PbodyContCount_of_Width=[2, 3, 8, 4],

                                                # hrz pbodycontact btw unit
                                                _Array_hrz_btw_units_PbodyContCount_of_Width=[4, 3, 2, 2, 5],

                                                # vtc left pbodycontact
                                                _Vtc_left_PbodyContCount_of_Width=3,

                                                # vtc right pbodycontact
                                                _Vtc_right_PbodyContCount_of_Width=6,

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

                                  # polyres
                                  _Array_Polyres_R_X_width=[1000, 1000, 1500, 2000, ],
                                  _Array_Polyres_R_Y_length=[600, 800, 850, 500],
                                  _Array_Polyres_CoXNum=[None, None, None, None],
                                  _Array_Polyres_CoYNum=[None, None, None, None],
                                  _Array_Polyres_N_Parallel=[5, 4, 2, 1],
                                  _Array_Polyres_Dummy=[True, True, True, True],
                                  _Array_Poly_up_connect=[True, True, True, True],

                                  # nmos_sw
                                  _Array_NMOSNumberofGate=[0, 3, 1, 0],
                                  _Array_NMOSChannelWidth=[500, 700, 600, 300],
                                  _Array_NMOSChannellength=[30, 30, 30, 30],
                                  _Array_NMOSDummy=[True, True, True, True],
                                  _Array_GateSpacing=[None, None, None, None],
                                  _Array_SDWidth=[None, None, None, None],
                                  _Array_XVT=['SLVT', 'SLVT', 'SLVT', 'SLVT'],
                                  _Array_PCCrit=[None, None, None, None],

                                  # vtc pbodycontact btw res and sw
                                  _Array_vtc_btw_res_sw_PbodyContCount_of_Width=[2, 3, 8, 4],

                                  # hrz pbodycontact btw unit
                                  _Array_hrz_btw_units_PbodyContCount_of_Width=[4, 3, 2, 2, 5],

                                  # vtc left pbodycontact
                                  _Vtc_left_PbodyContCount_of_Width=3,

                                  # vtc right pbodycontact
                                  _Vtc_right_PbodyContCount_of_Width=6,
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

        ##################################################################################################################### Gen_C03_placement
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(C04_routing_guardring._routing_guardring._ParametersForDesignCalculation)
        _Caculation_Parameters['_Array_Polyres_R_X_width'] = _Array_Polyres_R_X_width
        _Caculation_Parameters['_Array_Polyres_R_Y_length'] = _Array_Polyres_R_Y_length
        _Caculation_Parameters['_Array_Polyres_CoXNum'] = _Array_Polyres_CoXNum
        _Caculation_Parameters['_Array_Polyres_CoYNum'] = _Array_Polyres_CoYNum
        _Caculation_Parameters['_Array_Polyres_N_Parallel'] = _Array_Polyres_N_Parallel
        _Caculation_Parameters['_Array_Polyres_Dummy'] = _Array_Polyres_Dummy
        _Caculation_Parameters['_Array_Poly_up_connect'] = _Array_Poly_up_connect

        _Caculation_Parameters['_Array_NMOSNumberofGate'] = _Array_NMOSNumberofGate
        _Caculation_Parameters['_Array_NMOSChannelWidth'] = _Array_NMOSChannelWidth
        _Caculation_Parameters['_Array_NMOSChannellength'] = _Array_NMOSChannellength
        _Caculation_Parameters['_Array_NMOSDummy'] = _Array_NMOSDummy
        _Caculation_Parameters['_Array_GateSpacing'] = _Array_GateSpacing
        _Caculation_Parameters['_Array_SDWidth'] = _Array_SDWidth
        _Caculation_Parameters['_Array_XVT'] = _Array_XVT
        _Caculation_Parameters['_Array_PCCrit'] = _Array_PCCrit

        _Caculation_Parameters['_Array_vtc_btw_res_sw_PbodyContCount_of_Width'] = _Array_vtc_btw_res_sw_PbodyContCount_of_Width

        _Caculation_Parameters['_Array_hrz_btw_units_PbodyContCount_of_Width'] = _Array_hrz_btw_units_PbodyContCount_of_Width

        _Caculation_Parameters['_Vtc_left_PbodyContCount_of_Width'] = _Vtc_left_PbodyContCount_of_Width

        _Caculation_Parameters['_Vtc_right_PbodyContCount_of_Width'] = _Vtc_right_PbodyContCount_of_Width

        # Generate Sref
        self._DesignParameter['_Routing_guardring'] = self._SrefElementDeclaration(_DesignObj=C04_routing_guardring._routing_guardring(_DesignParameter=None, _Name='{}:_routing_guardring'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Routing_guardring']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Routing_guardring']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Routing_guardring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Routing_guardring']['_XYCoordinates'] = [[0, 0]]
        
        ##################################################################################################################### RES_and_SW_M2_connection   
            ####################################################################################################### RES_and_SW_M2_connection :invert even parallized res
        for i in range(0,len(_Array_NMOSNumberofGate)):
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if resistor is even parallized
                if _Array_Polyres_N_Parallel[i]%2 == 0:
                    self._DesignParameter['_Routing_guardring']['_DesignObj']._DesignParameter['_Placement']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._DesignParameter['_Left_res']['_Reflect'] = [1,0,0]                
            
            ####################################################################################################### RES_and_SW_M2_connection : M2 on res
        for i in range(0,len(_Array_NMOSNumberofGate)):
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :    
                #Define Boundary_element
                self._DesignParameter['_Left_res_M2_on_sw_port_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL2'][1], 
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

                #Define Boundary_element _YWidth
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')  
                self._DesignParameter['_Left_res_M2_on_sw_port_{}'.format(i)]['_YWidth'] = tmp[-1]['_Ywidth']

                #Define Boundary_element _XWidth
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')  
                self._DesignParameter['_Left_res_M2_on_sw_port_{}'.format(i)]['_XWidth'] = tmp[-1]['_Xwidth']

                #Define Boundary_element _XYCoordinates
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')
                
                if _Array_Polyres_N_Parallel[i]%2 == 0:
                    tmpXY =[tmp[-2]['_XY_cent']]
                else:
                    tmpXY =[tmp[-1]['_XY_cent']]
                    
                self._DesignParameter['_Left_res_M2_on_sw_port_{}'.format(i)]['_XYCoordinates'] = tmpXY
                
            ####################################################################################################### RES_and_SW_M2_connection: M2_Path
        
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :        
                #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                    _Layer=DesignParameters._LayerMapping['METAL2'][0], 
                                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                                    _XYCoordinates=[],
                                                                                                                    _Width=None,
                                                                                                                )

                #P1--P2 Width
                    #Cal width
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Nmos_sw','_Nmos_source_m2_hrz')    
                   
                self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']
                
                #P1--P2 coordiantes
                #tmpXY = []
                    #Cal tmpXY
                        #Cal tmpXY1
                tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Nmos_sw','_Nmos_source_m2_hrz')   
                tmp2 = self.get_param_KJH2('_Left_res_M2_on_sw_port_{}'.format(i))  
                
                p1 = tmp1[0]['_XY_left']
                p2y = tmp1[0]['_XY_left'][1]
                p2x = tmp2[-1]['_XY_right'][0]
                p2  = [p2x,p2y]
                
                p1_p2 = [p1,p2]
                
                tmpXY.append(p1_p2)
                
                        #Cal tmpXY2
                tmp3 = self.get_param_KJH2('_Left_res_M2_on_sw_port_{}'.format(i))                
                if p2y < tmp3[0]['_XY_cent'][1]:
                    a = np.array( [ -self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_Width'],-self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_Width'] ] )
                    p3 = p2 + 0.5*a
                    p4y = tmp3[0]['_XY_down'][1]
                    p4x = p3[0]
                    p4 = [p4x,p4y]
                else:
                    a = np.array( [ -self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_Width'],self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_Width'] ] )
                    p3 = p2 + 0.5*a
                    p4y = tmp3[0]['_XY_up'][1]
                    p4x = p3[0]
                    p4 = [p4x,p4y]
                
                p3_p4 = [p3,p4]
                tmpXY.append(p3_p4)
                
                self._DesignParameter['_Left_res_sw_M2_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ####################################################################################################### RES_and_SW_M2_connection: Via1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :   
                #Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
                _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
                _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

                #Sref ViaX declaration
                self._DesignParameter['_Left_res_sw_Via1_M1M2_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Left_res_sw_Via1_M1M2_{}'.format(_Name,i)))[0]

                #Calcuate _ViaMet22Met3NumberOfCOX
                tmp = self.get_param_KJH2('_Left_res_M2_on_sw_port_{}'.format(i))
                
                Xwidth = tmp[0]['_Xwidth']
                Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
                    #If Via is less than 2, Num_Via = 2
                if Num_Via_Xwidth < 2:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 2
                else:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = Num_Via_Xwidth

                #Calcuate _ViaMet22Met3NumberOfCOY
                Ywidth = tmp[0]['_Ywidth']
                Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
                    #If Via is less than 2, Num_Via = 2
                if Num_Via_Ywidth < 2:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1
                else:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1

                #Generate Metal(x), Metal(x+1) and C0(Viax) layer
                self._DesignParameter['_Left_res_sw_Via1_M1M2_{}'.format(i)]['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

                #Calcualte XYcoordinates by using get_Scoord_KJH
                    #Calculate Sref XYcoord
                        #initialized Sref coordinate
                self._DesignParameter['_Left_res_sw_Via1_M1M2_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                        #Calculation
                tmp1 = self.get_param_KJH2('_Left_res_M2_on_sw_port_{}'.format(i))
                tmp2 = self.get_param_KJH2('_Left_res_sw_Via1_M1M2_{}'.format(i),'_Met2Layer')
                tmp3 = self.get_param_KJH2('_Left_res_sw_Via1_M1M2_{}'.format(i))

                target_coord        = tmp1[0]['_XY_down_right']
                approaching_coord   = tmp2[0]['_XY_down_right']
                Scoord              = tmp3[0]['_XY_cent']

                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

                self._DesignParameter['_Left_res_sw_Via1_M1M2_{}'.format(i)]['_XYCoordinates'] = [New_Scoord]

        ##################################################################################################################### SW_and_RES_M2_connection   
            ####################################################################################################### SW_and_RES_M2_connection : M2 on res
        for i in range(0,len(_Array_NMOSNumberofGate)):
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :    
                #Define Boundary_element
                self._DesignParameter['_Right_res_M2_on_sw_port_{}'.format(i)] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL2'][1], 
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

                #Define Boundary_element _YWidth
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres','_Met1Layer')  
                self._DesignParameter['_Right_res_M2_on_sw_port_{}'.format(i)]['_YWidth'] = tmp[0]['_Ywidth']

                #Define Boundary_element _XWidth
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres','_Met1Layer')  
                self._DesignParameter['_Right_res_M2_on_sw_port_{}'.format(i)]['_XWidth'] = tmp[0]['_Xwidth']

                #Define Boundary_element _XYCoordinates
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres','_Met1Layer')
                
                if _Array_Polyres_N_Parallel[i]%2 == 0:
                    tmpXY =[tmp[0]['_XY_cent']]
                else:
                    tmpXY =[tmp[0]['_XY_cent']]
                    
                self._DesignParameter['_Right_res_M2_on_sw_port_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ####################################################################################################### SW_and_RES_M2_connection : M2 path
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :        
                #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                    _Layer=DesignParameters._LayerMapping['METAL2'][0], 
                                                                                                                    _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                                    _XYCoordinates=[],
                                                                                                                    _Width=None,
                                                                                                                )

                #P1--P2 Width
                    #Cal width
                tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Nmos_sw','_Nmos_drain_m2_hrz')    
                   
                self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']
                
                #P1--P2 coordiantes
                #tmpXY = []
                    #Cal tmpXY
                        #Cal tmpXY1
                tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Nmos_sw','_Nmos_drain_m2_hrz')   
                tmp2 = self.get_param_KJH2('_Right_res_M2_on_sw_port_{}'.format(i))  
                
                p1 = tmp1[0]['_XY_right']
                p2y = tmp1[0]['_XY_right'][1]
                p2x = tmp2[0]['_XY_left'][0]
                p2  = [p2x,p2y]
                
                p1_p2 = [p1,p2]
                
                tmpXY.append(p1_p2)
                
                        #Cal tmpXY2
                tmp3 = self.get_param_KJH2('_Right_res_M2_on_sw_port_{}'.format(i))                
                if p2y < tmp3[0]['_XY_cent'][1]:
                    a = np.array( [ self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_Width'],-self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_Width'] ] )
                    p3 = p2 + 0.5*a
                    p4y = tmp3[0]['_XY_down'][1]
                    p4x = p3[0]
                    p4 = [p4x,p4y]
                else:
                    a = np.array( [ self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_Width'],self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_Width'] ] )
                    p3 = p2 + 0.5*a
                    p4y = tmp3[0]['_XY_up'][1]
                    p4x = p3[0]
                    p4 = [p4x,p4y]
                
                p3_p4 = [p3,p4]
                tmpXY.append(p3_p4)
                
                self._DesignParameter['_Right_res_sw_M2_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ####################################################################################################### SW_and_RES_M2_connection : Via1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :   
                #Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
                _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
                _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

                #Sref ViaX declaration
                self._DesignParameter['_Right_res_sw_Via1_M1M2_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Right_res_sw_Via1_M1M2_{}'.format(_Name,i)))[0]

                #Calcuate _ViaMet22Met3NumberOfCOX
                tmp = self.get_param_KJH2('_Right_res_M2_on_sw_port_{}'.format(i))
                
                Xwidth = tmp[0]['_Xwidth']
                Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
                    #If Via is less than 2, Num_Via = 2
                if Num_Via_Xwidth < 2:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 2
                else:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = Num_Via_Xwidth

                #Calcuate _ViaMet22Met3NumberOfCOY
                Ywidth = tmp[0]['_Ywidth']
                Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
                    #If Via is less than 2, Num_Via = 2
                if Num_Via_Ywidth < 2:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1
                else:
                    _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1

                #Generate Metal(x), Metal(x+1) and C0(Viax) layer
                self._DesignParameter['_Right_res_sw_Via1_M1M2_{}'.format(i)]['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

                #Calcualte XYcoordinates by using get_Scoord_KJH
                    #Calculate Sref XYcoord
                        #initialized Sref coordinate
                self._DesignParameter['_Right_res_sw_Via1_M1M2_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                        #Calculation
                tmp1 = self.get_param_KJH2('_Right_res_M2_on_sw_port_{}'.format(i))
                tmp2 = self.get_param_KJH2('_Right_res_sw_Via1_M1M2_{}'.format(i),'_Met2Layer')
                tmp3 = self.get_param_KJH2('_Right_res_sw_Via1_M1M2_{}'.format(i))

                target_coord        = tmp1[0]['_XY_down_left']
                approaching_coord   = tmp2[0]['_XY_down_left']
                Scoord              = tmp3[0]['_XY_cent']

                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

                self._DesignParameter['_Right_res_sw_Via1_M1M2_{}'.format(i)]['_XYCoordinates'] = [New_Scoord]

        ##################################################################################################################### Left_res_dummy_connection M1
            ####################################################################################################### Left_res_dummy_connection M1:dummy inout connection M1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
            
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Left_dummy_inout_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Left_dummy_inout_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[0]['_XY_cent']
                        #P2 calculation
                    P2 = tmp1[1]['_XY_cent']
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[2]['_XY_cent']
                        #P2 calculation
                    P4 = tmp1[3]['_XY_cent']
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Left_dummy_inout_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ####################################################################################################### Left_res_dummy_connection M1: dummy1-_vtc-left_pbodycontact
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
                
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Left_dummy1_vtc_left_pbody_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Left_dummy1_vtc_left_pbody_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                    tmp2 = self.get_param_KJH2('_Routing_guardring','_Placement','_Vtc_left_PbodyContact','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[0]['_XY_cent']
                        #P2 calculation
                    P2x = tmp2[0]['_XY_cent'][0]
                    P2y = P1[1]
                    P2 = [P2x,P2y]
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[1]['_XY_cent']
                        #P2 calculation
                    P4x = tmp2[0]['_XY_cent'][0]
                    P4y = P3[1]
                    P4 = [P4x,P4y]
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Left_dummy1_vtc_left_pbody_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY                                                                                                                        

            ####################################################################################################### Left_res_dummy_connection M1: dummy1-_vtc_btw_res_sw_PbodyContact
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
                
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Left_dummy1_vtc_btw_res_sw_pbody_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Left_dummy1_vtc_btw_res_sw_pbody_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres_dummy','_Met1Layer')
                    tmp2 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Vtc_btw_res_sw_PbodyContact','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[2]['_XY_cent']
                        #P2 calculation
                    P2x = tmp2[0]['_XY_cent'][0]
                    P2y = P1[1]
                    P2 = [P2x,P2y]
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[3]['_XY_cent']
                        #P2 calculation
                    P4x = tmp2[0]['_XY_cent'][0]
                    P4y = P3[1]
                    P4 = [P4x,P4y]
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Left_dummy1_vtc_btw_res_sw_pbody_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY     



























        ##################################################################################################################### Left_res_dummy_connection M1
            ####################################################################################################### Left_res_dummy_connection M1:dummy inout connection M1
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
            
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Right_dummy_inout_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Right_dummy_inout_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[0]['_XY_cent']
                        #P2 calculation
                    P2 = tmp1[1]['_XY_cent']
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[2]['_XY_cent']
                        #P2 calculation
                    P4 = tmp1[3]['_XY_cent']
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Right_dummy_inout_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY

            ####################################################################################################### Left_res_dummy_connection M1: dummy2-_vtc-right_pbodycontact
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
                
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Right_dummy1_vtc_right_pbody_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Right_dummy1_vtc_right_pbody_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                    tmp2 = self.get_param_KJH2('_Routing_guardring','_Placement','_Vtc_right_PbodyContact','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[2]['_XY_cent']
                        #P2 calculation
                    P2x = tmp2[0]['_XY_cent'][0]
                    P2y = P1[1]
                    P2 = [P2x,P2y]
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[3]['_XY_cent']
                        #P2 calculation
                    P4x = tmp2[0]['_XY_cent'][0]
                    P4y = P3[1]
                    P4 = [P4x,P4y]
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Right_dummy1_vtc_right_pbody_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY                                                                                                                        

            ####################################################################################################### Left_res_dummy_connection M1: dummy1-_vtc_btw_res_sw_PbodyContact
        for i in range(0,len(_Array_NMOSNumberofGate)):
            tmpXY=[]
            # if res-sw-res structure
            if _Array_NMOSNumberofGate[i] != 0 :
                # if dummy exist
                if _Array_Polyres_Dummy[i] == True:
                
                    #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                    self._DesignParameter['_Right_dummy1_vtc_btw_sw_res_pbody_M1_connection_{}'.format(i)] = self._PathElementDeclaration(          
                                                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0], 
                                                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                                        _XYCoordinates=[],
                                                                                                                        _Width=None,
                                                                                                                        )

                    #P1--P2 Width
                        #Cal width
                    tmp = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                       
                    self._DesignParameter['_Right_dummy1_vtc_btw_sw_res_pbody_M1_connection_{}'.format(i)]['_Width'] = tmp[0]['_Ywidth']

                    #P1--P2 coordiantes
                    tmp1 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres_dummy','_Met1Layer')
                    tmp2 = self.get_param_KJH2('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Vtc_btw_sw_res_PbodyContact','_Met1Layer')
                        #P1 calculation
                    P1 = tmp1[0]['_XY_cent']
                        #P2 calculation
                    P2x = tmp2[0]['_XY_cent'][0]
                    P2y = P1[1]
                    P2 = [P2x,P2y]
                        #P1_P2
                    P1_P2 = [P1,P2]
                    tmpXY.append(P1_P2)
                    
                    #P3--P4 coordiantes
                        #P1 calculation
                    P3 = tmp1[1]['_XY_cent']
                        #P2 calculation
                    P4x = tmp2[0]['_XY_cent'][0]
                    P4y = P3[1]
                    P4 = [P4x,P4y]
                        #P1_P2
                    P3_P4 = [P3,P4]
                    
                    tmpXY.append(P3_P4)
                    self._DesignParameter['_Right_dummy1_vtc_btw_sw_res_pbody_M1_connection_{}'.format(i)]['_XYCoordinates'] = tmpXY     


                ## ##################################################################################################### resis connection: M5 connection vtc
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_res_M5conn_vtc'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL5'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL5'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(0),'_Met1Layer')
        tmp2 = self.get_param_KJH3('_Routing_guardring','_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(len(_Array_NMOSNumberofGate)),'_Met1Layer')

        self._DesignParameter['_res_M5conn_vtc']['_YWidth'] = abs( tmp1[0][0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_right_PbodyContact','_Met1Layer')
        tmp4 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_left_PbodyContact','_Met1Layer')
        
        self._DesignParameter['_res_M5conn_vtc']['_XWidth'] = np.ceil(abs( tmp3[0][0][0][0][0]['_XY_right'][0] - tmp4[0][0][0][0][0]['_XY_left'][0] ) / 8)

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_res_M5conn_vtc']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):
            #Pside
            if i ==0:
        
                        #Calculate
                            #Target_coord
                                #x
                tmp1_1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_right_PbodyContact','_Met1Layer')
                tmp1_2 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_left_PbodyContact','_Met1Layer')
                target_coordx = ( (1*tmp1_1[0][0][0][0][0]['_XY_right'][0]) + (3*tmp1_2[0][0][0][0][0]['_XY_left'][0] ) ) / (1+3)
                                #y
                tmp1_3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(0),'_Met1Layer')
                target_coordy = tmp1_3[0][0][0][0][0]['_XY_up'][1]
                
                target_coord = [target_coordx,target_coordy]
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_res_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_res_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
            #Nside
            else:
                        #Calculate
                            #Target_coord
                                #x
                tmp1_1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_right_PbodyContact','_Met1Layer')
                tmp1_2 = self.get_param_KJH3('_Routing_guardring','_Placement','_Vtc_left_PbodyContact','_Met1Layer')
                target_coordx = ( (3*tmp1_1[0][0][0][0][0]['_XY_right'][0]) + (1*tmp1_2[0][0][0][0][0]['_XY_left'][0] ) ) / (1+3)
                                #y
                tmp1_3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Hrz_btw_unit_PbodyContact_{}'.format(0),'_Met1Layer')
                target_coordy = tmp1_3[0][0][0][0][0]['_XY_up'][1]
                
                target_coord = [target_coordx,target_coordy]
                            #Approaching_coord
                tmp2 = self.get_param_KJH3('_res_M5conn_vtc')  
                approaching_coord = tmp2[0][0]['_XY_up']   
                            #Sref coord
                tmp3 = self.get_param_KJH3('_res_M5conn_vtc')
                Scoord = tmp3[0][0]['_XY_cent']
                            #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)
            
                #Define
        self._DesignParameter['_res_M5conn_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### resis connection: M5 connection hrz
        for i in range(0,len(_Array_NMOSNumberofGate)):

            #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
            self._DesignParameter['_res_M5conn_hrz_{}'.format(i)] = self._PathElementDeclaration(          
                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                _XYCoordinates=[],
                _Width=None,
            )
                                                                                    
            # Res and SW
            if _Array_NMOSNumberofGate[i] != 0 :

                #P1--P2 Width
                tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')
                self._DesignParameter['_res_M5conn_hrz_{}'.format(i)]['_Width'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']
                
                tmpXY = []
                #P1--P2 coordiantes
                    #P1 calculation
                tmp3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')
                P1 = tmp3[0][0][0][0][0][0][0]['_XY_cent']
                    #P2 calculation
                        #x
                tmp4 = self.get_param_KJH3('_res_M5conn_vtc')
                P2x = tmp4[0][0]['_XY_cent'][0]
                        #y
                P2y = P1[1] 
                
                P2 = [P2x,P2y]
                    #P1_P2
                P1_P2 = [P1,P2]
                tmpXY.append(P1_P2)

                #P3--P4 coordiantes
                    #P3 calculation
                tmp3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres','_Met1Layer')
                if _Array_Polyres_N_Parallel[i]%2 == 0:
                    P3 = tmp3[0][0][0][0][-1][0][0]['_XY_cent']
                else:
                    P3 = tmp3[0][0][0][0][-1][-1][0]['_XY_cent']
                    #P2 calculation
                        #x
                tmp4 = self.get_param_KJH3('_res_M5conn_vtc')
                P4x = tmp4[-1][0]['_XY_cent'][0]
                        #y
                P4y = P3[1]
                
                P4 = [P4x,P4y]
                    #P1_P2
                P3_P4 = [P3,P4]
                tmpXY.append(P3_P4)
                
                
                    #Cal tmpXY
                self._DesignParameter['_res_M5conn_hrz_{}'.format(i)]['_XYCoordinates'] = tmpXY
            
            #Res only
            else:

                #P1--P2 Width
                tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                self._DesignParameter['_res_M5conn_hrz_{}'.format(i)]['_Width'] = tmp1[0][0][0][0][0][0][0]['_Ywidth']
                
                tmpXY = []
                #P1--P2 coordiantes
                    #P1 calculation
                tmp3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                P1 = tmp3[0][0][0][0][0][0][0]['_XY_cent']
                    #P2 calculation
                        #x
                tmp4 = self.get_param_KJH3('_res_M5conn_vtc')
                P2x = tmp4[0][0]['_XY_cent'][0]
                        #y
                P2y = P1[1] 
                
                P2 = [P2x,P2y]
                    #P1_P2
                P1_P2 = [P1,P2]
                tmpXY.append(P1_P2)

                #P3--P4 coordiantes
                    #P1 calculation
                tmp3 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                if _Array_Polyres_N_Parallel[i]%2 == 0:
                    P3 = tmp3[0][0][0][0][-1][0][0]['_XY_cent']
                else:
                    P3 = tmp3[0][0][0][0][-1][-1][0]['_XY_cent']
                    #P2 calculation
                        #x
                tmp4 = self.get_param_KJH3('_res_M5conn_vtc')
                P4x = tmp4[-1][0]['_XY_cent'][0]
                        #y
                P4y = P3[1]
                
                P4 = [P4x,P4y]
                    #P1_P2
                P3_P4 = [P3,P4]
                tmpXY.append(P3_P4)
                
                
                    #Cal tmpXY
                self._DesignParameter['_res_M5conn_hrz_{}'.format(i)]['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### resis connection: ViaM1M5
        for i in range(0,len(_Array_NMOSNumberofGate)):
            # Res and SW
            if _Array_NMOSNumberofGate[i] != 0 :

                #Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] 	= 1
                _Caculation_Parameters['_Layer2'] 	= 5
                _Caculation_Parameters['_COX'] 		= None
                _Caculation_Parameters['_COY'] 		= None

                #Sref ViaX declaration
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_res_M5conn_ViaM1M5_{}'.format(_Name,i)))[0]

                #Define Sref Relection
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_Reflect'] = [0, 0, 0]
                
                #Define Sref Angle
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_Angle'] = 0

                #Calcuate Overlapped XYcoord
                tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')
                tmp2 = self.get_param_KJH3('_res_M5conn_hrz_{}'.format(i))
                Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0][0][0],tmp2[0][0])

                #Calcuate _COX and _COY
                _COX, _COY= self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'],Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')  ## None or 'MinEnclosureX' or 'MinEnclosureY'
                
                #Define _COX and _COY
                if _COX < 4:
                    _COX = 4
                if _COY < 1:
                    _COY = 2
                _Caculation_Parameters['_COX'] 		= _COX
                _Caculation_Parameters['_COY'] 		= _COY

                #Generate Metal(x), Metal(x+1) and C0(Viax) layer
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
                
                for j in range(0,2):
                    #pside
                    if j == 0:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Left_res','_Polyres','_Met1Layer')
                        tmp2 = self.get_param_KJH3('_res_M5conn_hrz_{}'.format(i))
                        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0][0][0],tmp2[0][0])
                        
                        target_coord = Ovlpcoord[0]['_XY_cent']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))  
                        approaching_coord = tmp2[0][0]['_XY_cent']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord = np.round(New_Scoord,2)
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = tmpXY 
                    #Nside
                    else:                    
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Right_res','_Polyres','_Met1Layer')
                        tmp2 = self.get_param_KJH3('_res_M5conn_hrz_{}'.format(i))
                        if _Array_Polyres_N_Parallel[i]%2 == 0:
                            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][-1][0][0],tmp2[-1][0])
                        else:
                            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][-1][-1][0],tmp2[-1][0])
                            
                        target_coord = Ovlpcoord[0]['_XY_cent']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))  
                        approaching_coord = tmp2[0][0]['_XY_cent']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord = np.round(New_Scoord,2)
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = tmpXY 
                        
            #Res only
            else:
                #Define ViaX Parameter
                _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
                _Caculation_Parameters['_Layer1'] 	= 1
                _Caculation_Parameters['_Layer2'] 	= 5
                _Caculation_Parameters['_COX'] 		= None
                _Caculation_Parameters['_COY'] 		= None

                #Sref ViaX declaration
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_res_M5conn_ViaM1M5_{}'.format(_Name,i)))[0]

                #Define Sref Relection
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_Reflect'] = [0, 0, 0]
                
                #Define Sref Angle
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_Angle'] = 0

                #Calcuate Overlapped XYcoord
                tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                tmp2 = self.get_param_KJH3('_res_M5conn_vtc')
                Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0][0][0],tmp2[0][0])

                #Calcuate _COX and _COY
                _COX, _COY= self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'],Ovlpcoord[0]['_Ywidth'],'MinEnclosureY')  ## None or 'MinEnclosureX' or 'MinEnclosureY'

                #Define _COX and _COY
                if _COX < 4:
                    _COX = 4
                if _COY < 1:
                    _COY = 2
                _Caculation_Parameters['_COX'] 		= _COX
                _Caculation_Parameters['_COY'] 		= _COY

                #Generate Metal(x), Metal(x+1) and C0(Viax) layer
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

                #Calculate Sref XYcoord
                tmpXY=[]
                    #initialized Sref coordinate
                self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

                for j in range(0,2):
                    #pside
                    if j == 0:
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                        tmp2 = self.get_param_KJH3('_res_M5conn_hrz_{}'.format(i))
                        Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][0][0][0],tmp2[0][0])
                        
                        target_coord = Ovlpcoord[0]['_XY_cent']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))  
                        approaching_coord = tmp2[0][0]['_XY_cent']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord = np.round(New_Scoord,2)
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = tmpXY 
                    #Nside
                    else:                    
                            #Calculate
                                #Target_coord
                        tmp1 = self.get_param_KJH3('_Routing_guardring','_Placement','_Unit_{}'.format(i),'_Cent_res','_Polyres','_Met1Layer')
                        tmp2 = self.get_param_KJH3('_res_M5conn_hrz_{}'.format(i))
                        if _Array_Polyres_N_Parallel[i]%2 == 0:
                            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][-1][0][0],tmp2[-1][0])
                        else:
                            Ovlpcoord = self.get_ovlp_KJH2(tmp1[0][0][0][0][-1][-1][0],tmp2[-1][0])
                            
                        target_coord = Ovlpcoord[0]['_XY_cent']
                                #Approaching_coord
                        tmp2 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))  
                        approaching_coord = tmp2[0][0]['_XY_cent']
                                #Sref coord
                        tmp3 = self.get_param_KJH3('_res_M5conn_ViaM1M5_{}'.format(i))
                        Scoord = tmp3[0][0]['_XY_cent']
                                #Cal
                        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                        New_Scoord = np.round(New_Scoord,2)
                        tmpXY.append(New_Scoord)
                            #Define
                        self._DesignParameter['_res_M5conn_ViaM1M5_{}'.format(i)]['_XYCoordinates'] = tmpXY 



        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_C_building_block'
    cellname = 'C05_routing_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

                            # polyres
                            _Array_Polyres_R_X_width=[ 1500, 2000, 1500, 2000, 1500, 2000, 1800, 1000],
                            _Array_Polyres_R_Y_length=[ 850, 500,850, 500,850, 500, 700, 500],
                            _Array_Polyres_CoXNum=[ None, None,None, None,None, None, None, None],
                            _Array_Polyres_CoYNum=[ None, None,None, None,None, None, None, None],
                            _Array_Polyres_N_Parallel=[ 2,2,2,2,2, 1, 2, 8],
                            _Array_Polyres_Dummy=[ True, True,True, True,True, True, True, True],
                            _Array_Poly_up_connect=[ True, True,True, True,True, True, True, True],

                            # nmos_sw
                            _Array_NMOSNumberofGate=[8,7,10,3,1, 5, 8, 0],
                            _Array_NMOSChannelWidth=[ 1500,1000,400,500,600, 400, 800, 1000],
                            _Array_NMOSChannellength=[30, 30, 30, 30,30, 30, 30, 30],
                            _Array_NMOSDummy=[True, True, True, True,True, True, True, True],
                            _Array_GateSpacing=[None, None, None, None,None, None, None, None],
                            _Array_SDWidth=[None, None, None, None,None, None, None, None],
                            _Array_XVT=['SLVT', 'SLVT', 'SLVT', 'SLVT','SLVT', 'SLVT', 'SLVT', 'SLVT'],
                            _Array_PCCrit=[None, None, None, None,None, None, None, None],

                            # vtc pbodycontact btw res and sw
                            _Array_vtc_btw_res_sw_PbodyContCount_of_Width=[5, 5, 5, 5, 5, 5, 5, 5],

                            # hrz pbodycontact btw unit
                            _Array_hrz_btw_units_PbodyContCount_of_Width=[ 5, 5, 5, 5, 5, 5, 5, 5, 5],

                            # vtc left pbodycontact
                            _Vtc_left_PbodyContCount_of_Width=5,

                            # vtc right pbodycontact
                            _Vtc_right_PbodyContCount_of_Width=5,
                            
    
                            # polyres
                            # _Array_Polyres_R_X_width=[1000, 1000, 1500, 2000, 1800, 1000],
                            # _Array_Polyres_R_Y_length=[600, 800, 850, 500, 700, 500],
                            # _Array_Polyres_CoXNum=[None, None, None, None, None, None],
                            # _Array_Polyres_CoYNum=[None, None, None, None, None, None],
                            # _Array_Polyres_N_Parallel=[3, 2, 2, 1, 2, 5],
                            # _Array_Polyres_Dummy=[True, True, True, True, True, True],
                            # _Array_Poly_up_connect=[True, True, True, True, True, True],

                            # nmos_sw
                            # _Array_NMOSNumberofGate=[2, 3, 1, 5, 8, 0],
                            # _Array_NMOSChannelWidth=[500, 700, 600, 300, 800, 1000],
                            # _Array_NMOSChannellength=[30, 30, 30, 30, 30, 30],
                            # _Array_NMOSDummy=[True, True, True, True, True, True],
                            # _Array_GateSpacing=[None, None, None, None, None, None],
                            # _Array_SDWidth=[None, None, None, None, None, None],
                            # _Array_XVT=['SLVT', 'SLVT', 'SLVT', 'SLVT', 'SLVT', 'SLVT'],
                            # _Array_PCCrit=[None, None, None, None, None, None],

                            # vtc pbodycontact btw res and sw
                            # _Array_vtc_btw_res_sw_PbodyContCount_of_Width=[3, 3, 3, 3, 3, 5],

                            # hrz pbodycontact btw unit
                            # _Array_hrz_btw_units_PbodyContCount_of_Width=[2, 2, 2, 2, 2, 2, 2],

                            # vtc left pbodycontact
                            # _Vtc_left_PbodyContCount_of_Width=8,

                            # vtc right pbodycontact
                            # _Vtc_right_PbodyContCount_of_Width=10,

   
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
