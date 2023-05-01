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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G00_nmos_input
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G01_nmos_parallel



## ########################################################################################################################################################## Class_HEADER
class _nmos_dummy(StickDiagram_KJH1._StickDiagram_KJH):

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

# NMOS Parallel
_Num_NMOS				= None,

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

# NMOS Parallel
_Num_NMOS				= None,

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
        _Caculation_Parameters = copy.deepcopy(G01_nmos_parallel._nmos_parallel._ParametersForDesignCalculation)
        _Caculation_Parameters['_In_NMOSNumberofGate'] 		= _In_NMOSNumberofGate
        _Caculation_Parameters['_In_NMOSChannelWidth'] 		= _In_NMOSChannelWidth
        _Caculation_Parameters['_In_NMOSChannellength'] 	= _In_NMOSChannellength
        _Caculation_Parameters['_In_GateSpacing'] 			= _In_GateSpacing
        _Caculation_Parameters['_In_SDWidth'] 				= _In_SDWidth
        _Caculation_Parameters['_In_XVT'] 					= _In_XVT
        _Caculation_Parameters['_In_PCCrit'] 				= _In_PCCrit

        _Caculation_Parameters['_In_Source_Via_TF'] 		= _In_Source_Via_TF
        _Caculation_Parameters['_In_Drain_Via_TF'] 			= _In_Drain_Via_TF

        _Caculation_Parameters['_In_NMOSDummy'] 			= _In_NMOSDummy
        _Caculation_Parameters['_In_NMOSDummy_length'] 		= _In_NMOSDummy_length
        _Caculation_Parameters['_In_NMOSDummy_placement'] 	= _In_NMOSDummy_placement

        _Caculation_Parameters['_Num_NMOS'] 				= _Num_NMOS

            # Generate Sref
        self._DesignParameter['_Tr_parallel'] = self._SrefElementDeclaration(_DesignObj=G01_nmos_parallel._nmos_parallel(_DesignParameter=None, _Name='{}:_Tr_parallel'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Tr_parallel']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Tr_parallel']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Tr_parallel']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Tr_parallel']['_XYCoordinates'] = [[0,0]]

            ## ################################################################################################################### Gen nmos dummy
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A00_NmosWithDummy_KJH._NmosWithDummy_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_NMOSNumberofGate'] 	= _In_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth'] 	= _In_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] 	= _In_NMOSChannellength
        _Caculation_Parameters['_GateSpacing'] 			= _In_GateSpacing
        _Caculation_Parameters['_SDWidth'] 				= _In_SDWidth
        _Caculation_Parameters['_XVT'] 					= _In_XVT
        _Caculation_Parameters['_PCCrit'] 				= _In_PCCrit

        _Caculation_Parameters['_Source_Via_TF'] 		= False
        _Caculation_Parameters['_Drain_Via_TF'] 		= False

        _Caculation_Parameters['_NMOSDummy'] 			= _In_NMOSDummy
        _Caculation_Parameters['_NMOSDummy_length'] 	= _In_NMOSDummy_length
        _Caculation_Parameters['_NMOSDummy_placement'] 	= _In_NMOSDummy_placement

            # Generate Sref
        self._DesignParameter['_Input_dummy_tr'] = self._SrefElementDeclaration(_DesignObj=A00_NmosWithDummy_KJH._NmosWithDummy_KJH(_DesignParameter=None, _Name='{}:_Input_dummy_tr'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Input_dummy_tr']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Input_dummy_tr']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Input_dummy_tr']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Input_dummy_tr']['_XYCoordinates'] = [[0,0]] 

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_dummy_tr']['_XYCoordinates'] = [[0,0]]
        
        for i in range(0,2):

            if i ==0:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_Tr_parallel','_Unit_tr','_Input_tr','_PODummyLayer')
                target_coord = tmp1[0][0][0][0][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_Input_dummy_tr','_PODummyLayer')
                approaching_coord = tmp2[0][-1][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_Input_dummy_tr')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

            else:
                        #Target_coord
                tmp1 = self.get_param_KJH3('_Tr_parallel','_Unit_tr','_Input_tr','_PODummyLayer')
                target_coord = tmp1[0][-1][0][-1][0]['_XY_cent']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_Input_dummy_tr','_PODummyLayer')
                approaching_coord = tmp2[0][0][0]['_XY_cent']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_Input_dummy_tr')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Input_dummy_tr']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Input_Tr_PolyConnection
                ## ##################################################################################################### Input_Tr_PolyConnection: Poly Vtc
        # pre-defined values
        Vtc_poly_ydistance = 250

        # Define Boundary_element
        self._DesignParameter['_Input_dummy_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_dummy_tr', '_POLayer')
        self._DesignParameter['_Input_dummy_vtc_poly']['_XWidth'] = tmp[0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        self._DesignParameter['_Input_dummy_vtc_poly']['_YWidth'] =  Vtc_poly_ydistance

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_dummy_vtc_poly']['_XYCoordinates'] = [[0,0]]

        tmp11 = self.get_param_KJH3('_Input_dummy_tr')
        for i in range(0,len(tmp11)):

            tmp = self.get_param_KJH3('_Input_dummy_tr', '_POLayer')
            for j in range(0,len(tmp[i])):
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_Input_dummy_tr', '_POLayer')
                target_coord = tmp1[i][j][0]['_XY_up']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_Input_dummy_vtc_poly')
                approaching_coord = tmp2[0][0]['_XY_down']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_Input_dummy_vtc_poly')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Input_dummy_vtc_poly']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Input_Tr_PolyConnection: Poly Hrz
        # Pre-defined
        Horz_poly_ywidth = 50

        # Define Boundary_element
        self._DesignParameter['_Input_dummy_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )
        
        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Input_dummy_vtc_poly')
        self._DesignParameter['_Input_dummy_hrz_poly']['_XWidth'] = abs( tmp[_In_NMOSNumberofGate-1][0]['_XY_right'][0] - tmp[0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        self._DesignParameter['_Input_dummy_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_dummy_hrz_poly']['_XYCoordinates'] = [[0,0]]


        tmp11 = self.get_param_KJH3('_Input_dummy_tr')
        for i in range(0,len(tmp11)):
            if i == 0:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_Input_dummy_vtc_poly')
                target_coord = tmp1[0][0]['_XY_up_left']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_Input_dummy_hrz_poly')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_Input_dummy_hrz_poly')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

            else:
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_Input_dummy_vtc_poly')
                target_coord = tmp1[_In_NMOSNumberofGate][0]['_XY_up_left']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_Input_dummy_hrz_poly')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_Input_dummy_hrz_poly')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)


            #Define
        self._DesignParameter['_Input_dummy_hrz_poly']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _Input_dummy_tr XVT cover-up
        # Define Boundary_element
        self._DesignParameter['_Input_dummy_tr_xvt_coverup'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['{}'.format(_In_XVT)][0],
            _Datatype=DesignParameters._LayerMapping['{}'.format(_In_XVT)][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_Input_dummy_tr','_{}Layer'.format(_In_XVT))
        self._DesignParameter['_Input_dummy_tr_xvt_coverup']['_XWidth'] = abs( tmp1[-1][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        tmp2 = self.get_param_KJH3('_Input_dummy_tr','_{}Layer'.format(_In_XVT))
        self._DesignParameter['_Input_dummy_tr_xvt_coverup']['_YWidth'] = tmp2[0][0][0]['_Ywidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Input_dummy_tr_xvt_coverup']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Input_dummy_tr','_{}Layer'.format(_In_XVT))
        target_coord = tmp1[0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Input_dummy_tr_xvt_coverup')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Input_dummy_tr_xvt_coverup')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Input_dummy_tr_xvt_coverup']['_XYCoordinates'] = tmpXY		



        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_G_building_block'
    cellname = 'G02_nmos_dummy_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# NMOS INPUT UNIT TR
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

# NMOS Parallel
_Num_NMOS				= 7,

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
    LayoutObj = _nmos_dummy(_DesignParameter=None, _Name=cellname)
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
