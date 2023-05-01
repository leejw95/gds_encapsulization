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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.F2_Building_block import F00_pmos_sw_and_pmos_cs
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.F2_Building_block import F01_guardring
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.F2_Building_block import F02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.F2_Building_block import F03_placement



## ########################################################################################################################################################## Class_HEADER
class _nmos_input(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

# NMOS INPUT TR
    #NMOS
_In_NMOSNumberofGate 	= None,
_In_NMOSChannelWidth 	= None,
_In_NMOSChannellength 	= None,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= None,
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= None,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= None,
    #POLY dummy setting
_In_NMOSDummy 			= None, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/

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

# NMOS INPUT TR
    #NMOS
_In_NMOSNumberofGate 	= None,
_In_NMOSChannelWidth 	= None,
_In_NMOSChannellength 	= None,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= None,
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= None,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= None,
    #POLY dummy setting
_In_NMOSDummy 			= None, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/

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

            ## ################################################################################################################### Gen nmos input Tr
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A00_NmosWithDummy_KJH._NmosWithDummy_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_NMOSNumberofGate'] 	= _In_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] 	= _In_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] 	= _In_NMOSChannellength
        _Caculation_Parameters['_GateSpacing'] 			= _In_GateSpacing
        _Caculation_Parameters['_SDWidth'] 				= _In_SDWidth
        _Caculation_Parameters['_XVT'] 					= _In_XVT
        _Caculation_Parameters['_PCCrit'] 				= _In_PCCrit

        _Caculation_Parameters['_Source_Via_TF'] 		= _In_Source_Via_TF
        _Caculation_Parameters['_Drain_Via_TF'] 		= _In_Drain_Via_TF

        _Caculation_Parameters['_NMOSDummy'] 			= _In_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length'] 	= _In_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] 	= _In_NMOSDummy_placement

            # Generate Sref
        self._DesignParameter['_Input_tr'] = self._SrefElementDeclaration(_DesignObj=A00_NmosWithDummy_KJH._NmosWithDummy_KJH(_DesignParameter=None, _Name='{}:_Input_tr'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Input_tr']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Input_tr']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Input_tr']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Input_tr']['_XYCoordinates'] = [[0,0]]        
        
            ## ################################################################################################################### Input_Tr_Source_M2_connection
                ## ##################################################################################################### Input_Tr_Source_M2_connection : Vtc_M2
        # pre-defined values
        y_distance = 150

        # Define Boundary_element
        self._DesignParameter['_Input_tr_source_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')
        self._DesignParameter['_Input_tr_source_m2_vtc']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Input_tr', '_Met1Layer_Source')
        tmp2 = self.get_param_KJH3('_Input_tr','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')

        self._DesignParameter['_Input_tr_source_m2_vtc']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0][0][0]['_XY_up'][1]) + y_distance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_source_m2_vtc']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Input_tr', '_Met1Layer_Source')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Input_tr','_Source_ViaM1M2','_ViaM1M2','_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_up']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Input_tr_source_m2_vtc')
            approaching_coord = tmp2[0][0]['_XY_down']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Input_tr_source_m2_vtc')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Input_tr_source_m2_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Input_Tr_Source_M2_connection : Hrz_M2
        # Define Boundary_element
        self._DesignParameter['_Input_tr_source_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr_source_m2_vtc')
        self._DesignParameter['_Input_tr_source_m2_hrz']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )																						

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Input_tr_source_m2_vtc')
        self._DesignParameter['_Input_tr_source_m2_hrz']['_YWidth'] = tmp1[0][0]['_Xwidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_source_m2_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Input_tr_source_m2_vtc')  		
        target_coord = tmp1[0][0]['_XY_up_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Input_tr_source_m2_hrz')  
        approaching_coord = tmp2[0][0]['_XY_down_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Input_tr_source_m2_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Input_tr_source_m2_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Input_Tr_Drain_M2_connection
                ## ##################################################################################################### Input_Tr_Drain_M2_connection : Vtc_M2
        # pre-defined values
        y_distance = 100

        # Define Boundary_element
        self._DesignParameter['_Input_tr_drain_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
        self._DesignParameter['_Input_tr_drain_m2_vtc']['_XWidth'] = tmp[0][0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Input_tr', '_Met1Layer_Drain')
        tmp2 = self.get_param_KJH3('_Input_tr','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')

        self._DesignParameter['_Input_tr_drain_m2_vtc']['_YWidth'] = -abs( tmp1[0][0][0]['_XY_down'][1] - tmp2[0][0][0][0][0]['_XY_down'][1]) + y_distance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Input_tr', '_Met1Layer_Drain')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Input_tr','_Drain_ViaM1M2','_ViaM1M2','_Met2Layer')
            target_coord = tmp1[0][i][0][0][0]['_XY_down']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Input_tr_drain_m2_vtc')
            approaching_coord = tmp2[0][0]['_XY_up']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Input_tr_drain_m2_vtc')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Input_tr_drain_m2_vtc']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Input_Tr_Drain_M2_connection : Hrz_M2
        # Define Boundary_element
        self._DesignParameter['_Input_tr_drain_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr_drain_m2_vtc')
        self._DesignParameter['_Input_tr_drain_m2_hrz']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )																						

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Input_tr_drain_m2_vtc')
        self._DesignParameter['_Input_tr_drain_m2_hrz']['_YWidth'] = tmp1[0][0]['_Xwidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Input_tr_drain_m2_vtc')  		
        target_coord = tmp1[0][0]['_XY_down_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Input_tr_drain_m2_hrz')  
        approaching_coord = tmp2[0][0]['_XY_up_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Input_tr_drain_m2_hrz')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Input_tr_drain_m2_hrz']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Input_Tr_PolyConnection
                ## ##################################################################################################### Input_Tr_PolyConnection: Poly Vtc
        # pre-defined values
        Vtc_poly_ydistance = 250

        # Define Boundary_element
        self._DesignParameter['_Input_tr_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr', '_POLayer')
        self._DesignParameter['_Input_tr_vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        self._DesignParameter['_Input_tr_vtc_poly']['_YWidth'] =  Vtc_poly_ydistance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_vtc_poly']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Input_tr', '_POLayer')
        for i in range(0,len(tmp[0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Input_tr', '_POLayer')
            target_coord = tmp1[0][i][0]['_XY_up']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Input_tr_vtc_poly')
            approaching_coord = tmp2[0][0]['_XY_down']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Input_tr_vtc_poly')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Input_tr_vtc_poly']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Input_Tr_PolyConnection: Poly Hrz
        # Pre-defined
        Horz_poly_ywidth = 50

        # Define Boundary_element
        self._DesignParameter['_Input_tr_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )
        
        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_tr_vtc_poly')
        self._DesignParameter['_Input_tr_hrz_poly']['_XWidth'] = abs( tmp[-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        self._DesignParameter['_Input_tr_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Input_tr_vtc_poly')  		
        target_coord = tmp1[0][0]['_XY_up_left']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Input_tr_hrz_poly')  
        approaching_coord = tmp2[0][0]['_XY_up_left']   
                #Sref coord
        tmp3 = self.get_param_KJH3('_Input_tr_hrz_poly')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Input_tr_hrz_poly']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Input_Tr_gate_ViaM0M3
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 0
        _Caculation_Parameters['_Layer2'] 	= 3
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Input_tr_ViaM0M3'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Input_tr_ViaM0M3'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Input_tr_ViaM0M3']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Input_tr_ViaM0M3']['_Angle'] = 0

        #Calcuate _COX
        _Caculation_Parameters['_COX'] = 1

        #Calcuate _COY
        _Caculation_Parameters['_COY'] = 2

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Input_tr_ViaM0M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_tr_ViaM0M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Input_tr_hrz_poly') 
        target_coord = tmp1[0][0]['_XY_up']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Input_tr_ViaM0M3','_ViaM0M1','_POLayer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_down']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Input_tr_ViaM0M3')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Input_tr_ViaM0M3']['_XYCoordinates'] = tmpXY
		
		
        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_G_building_block'
    cellname = 'G00_nmos_input_98'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# NMOS INPUT TR
    #NMOS
_In_NMOSNumberofGate 	= 5,
_In_NMOSChannelWidth 	= 625,
_In_NMOSChannellength 	= 40,
_In_GateSpacing 		= None,
_In_SDWidth 			= None,
_In_XVT 				= 'RVT',
_In_PCCrit 				= None,
    #Source_node_ViaM1M2
_In_Source_Via_TF 		= True,
    #Drain_node_ViaM1M2
_In_Drain_Via_TF 		= True,
    #POLY dummy setting
_In_NMOSDummy 			= True, #TF
        #if _PMOSDummy == True
_In_NMOSDummy_length 	= None, #None/Value
_In_NMOSDummy_placement = None, #None/'Up'/'Dn'/


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
    LayoutObj = _nmos_input(_DesignParameter=None, _Name=cellname)
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
