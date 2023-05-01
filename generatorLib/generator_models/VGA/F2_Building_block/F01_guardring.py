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
 


## ########################################################################################################################################################## Class_HEADER
class _guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= None,
_Cs_PMOSChannelWidth	= None,
_Cs_PMOSChannellength	= None,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= None,
_Cs_PCCrit				= None,

        #IF PMOS Dummy == True
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= None,
_Sw_PMOSChannelWidth	= None,
_Sw_PMOSChannellength	= None,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= None,
_Sw_PCCrit				= None,

        #IF PMOS Dummy == True
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,

# NbodyRing
_NumCont			= None,
_right_margin 		= None,
_left_margin 		= None,
_up_margin 			= None,
_down_margin 		= None,

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

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= None,
_Cs_PMOSChannelWidth	= None,
_Cs_PMOSChannellength	= None,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= None,
_Cs_PCCrit				= None,

        #IF PMOS Dummy == True
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= None,
_Sw_PMOSChannelWidth	= None,
_Sw_PMOSChannellength	= None,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= None,
_Sw_PCCrit				= None,

        #IF PMOS Dummy == True
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,

# NbodyRing
_NumCont			= None,
_right_margin 		= None,
_left_margin 		= None,
_up_margin 			= None,
_down_margin 		= None,

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
        
            ## ################################################################################################################### Gen Pmos Current source
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(F00_pmos_sw_and_pmos_cs._pmos_sw_and_pmos_cs._ParametersForDesignCalculation)
        _Caculation_Parameters['_Cs_PMOSNumberofGate'] 		= _Cs_PMOSNumberofGate
        _Caculation_Parameters['_Cs_PMOSChannelWidth'] 		= _Cs_PMOSChannelWidth
        _Caculation_Parameters['_Cs_PMOSChannellength'] 	= _Cs_PMOSChannellength
        _Caculation_Parameters['_Cs_GateSpacing'] 			= _Cs_GateSpacing
        _Caculation_Parameters['_Cs_SDWidth'] 				= _Cs_SDWidth
        _Caculation_Parameters['_Cs_XVT'] 					= _Cs_XVT
        _Caculation_Parameters['_Cs_PCCrit'] 				= _Cs_PCCrit
        _Caculation_Parameters['_Cs_Source_Via_TF'] 		= False
        _Caculation_Parameters['_Cs_Drain_Via_TF'] 			= True
        _Caculation_Parameters['_Cs_PMOSDummy'] 			= True
        _Caculation_Parameters['_Cs_PMOSDummy_length'] 		= _Cs_PMOSDummy_length
        _Caculation_Parameters['_Cs_PMOSDummy_placement'] 	= _Cs_PMOSDummy_placement

        _Caculation_Parameters['_Sw_PMOSNumberofGate'] 		= _Sw_PMOSNumberofGate
        _Caculation_Parameters['_Sw_PMOSChannelWidth'] 		= _Sw_PMOSChannelWidth
        _Caculation_Parameters['_Sw_PMOSChannellength'] 	= _Sw_PMOSChannellength
        _Caculation_Parameters['_Sw_GateSpacing'] 			= _Sw_GateSpacing
        _Caculation_Parameters['_Sw_SDWidth'] 				= _Sw_SDWidth
        _Caculation_Parameters['_Sw_XVT'] 					= _Sw_XVT
        _Caculation_Parameters['_Sw_PCCrit'] 				= _Sw_PCCrit
        _Caculation_Parameters['_Sw_Source_Via_TF'] 		= True
        _Caculation_Parameters['_Sw_Drain_Via_TF'] 			= True
        _Caculation_Parameters['_Sw_PMOSDummy'] 			= True
        _Caculation_Parameters['_Sw_PMOSDummy_length'] 		= _Sw_PMOSDummy_length
        _Caculation_Parameters['_Sw_PMOSDummy_placement'] 	= _Sw_PMOSDummy_placement


        # Generate Sref
        self._DesignParameter['_Pmos_cs_sw'] = self._SrefElementDeclaration(_DesignObj=F00_pmos_sw_and_pmos_cs._pmos_sw_and_pmos_cs(_DesignParameter=None, _Name='{}:_Pmos_cs_sw'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Pmos_cs_sw']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Pmos_cs_sw']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Pmos_cs_sw']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Pmos_cs_sw']['_XYCoordinates'] = [[0, 0]]

            ## ################################################################################################################### Nbodyring
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A06_NbodyRing_KJH._NbodyRing_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] 		= None
        _Caculation_Parameters['_YlengthIntn'] 		= None
        _Caculation_Parameters['_NumContTop'] 		= _NumCont
        _Caculation_Parameters['_NumContBottom'] 	= _NumCont
        _Caculation_Parameters['_NumContLeft'] 		= _NumCont
        _Caculation_Parameters['_NumContRight'] 	= _NumCont

        #Find Outter boundary
        tmp = self.get_outter_KJH('_Pmos_cs_sw')

        # Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] 		= abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0] ) + _right_margin + _left_margin

        # Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] 		= abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0] ) + _up_margin + _down_margin

        # Generate Sref
        self._DesignParameter['_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A06_NbodyRing_KJH._NbodyRing_KJH(_DesignParameter=None, _Name='{}:_Nbodyring'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Nbodyring']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Nbodyring']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = [[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord 		
        target_coord = [ tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0] ]  
                #Approaching_coord
                    #x
        tmp2_1 = self.get_param_KJH3('_Nbodyring','_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')  
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                    #y
        tmp2_2 = self.get_param_KJH3('_Nbodyring','_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')  
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1] 

        approaching_coord = [approaching_coordx,approaching_coordy]
                #Sref coord
        tmp3 = self.get_param_KJH3('_Nbodyring')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _Cs_source guardring M1 connection
        # Define Boundary_element
        self._DesignParameter['_Cs_and_nbody_m1_connect'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[],
                                                                                            )

        # Define Boundary_element _XWidth
        tmp = self.get_param_KJH3('_Pmos_cs_sw','_Cs_pmos','_Met1Layer_Source')
        self._DesignParameter['_Cs_and_nbody_m1_connect']['_XWidth'] = tmp[0][0][0][0]['_Xwidth']

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Pmos_cs_sw','_Cs_pmos','_Met1Layer_Source')
        tmp2 = self.get_param_KJH3('_Nbodyring','_NbodyTop','_NbodyContactPhyLen','_Met1Layer')

        self._DesignParameter['_Cs_and_nbody_m1_connect']['_YWidth'] = abs( tmp2[0][0][0][0][0]['_XY_down'][1] - tmp1[0][0][0][0]['_XY_up'][1] )

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_and_nbody_m1_connect']['_XYCoordinates'] = [[0,0]]

        tmp = self.get_param_KJH3('_Pmos_cs_sw','_Cs_pmos','_Met1Layer_Source')
        for i in range(0,len(tmp[0][0])):
                #Calculate
                    #Target_coord
            tmp1 = self.get_param_KJH3('_Pmos_cs_sw','_Cs_pmos','_Met1Layer_Source')
            target_coord = tmp1[0][0][i][0]['_XY_up']
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_Cs_and_nbody_m1_connect')
            approaching_coord = tmp2[0][0]['_XY_down']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_Cs_and_nbody_m1_connect')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Cs_and_nbody_m1_connect']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### _Nwell_cover-up
        # Define Boundary_element
        self._DesignParameter['_Nwell_covering'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[],
                                                                                    )

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_Nbodyring','_ExtenNwell_Left')
        tmp2 = self.get_param_KJH3('_Nbodyring','_ExtenNwell_Right')
        self._DesignParameter['_Nwell_covering']['_XWidth'] = abs ( tmp2[0][0][0]['_XY_right'][0] - tmp1[0][0][0]['_XY_left'][0] )

        # Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_Nbodyring','_ExtenNwell_Top')
        tmp2 = self.get_param_KJH3('_Nbodyring','_ExtenNwell_Bottom')

        self._DesignParameter['_Nwell_covering']['_YWidth'] = abs( tmp1[0][0][0]['_XY_up'][1] - tmp2[0][0][0]['_XY_down'][1] )

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Nwell_covering']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Nbodyring','_ExtenNwell_Bottom')
        target_coord = tmp1[0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Nwell_covering')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Nwell_covering')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Nwell_covering']['_XYCoordinates'] = tmpXY		


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_F2_building_block'
    cellname = 'F00_guardring_93'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

# Current source pmos
    #PMOS
_Cs_PMOSNumberofGate	= 2,
_Cs_PMOSChannelWidth	= 1600,
_Cs_PMOSChannellength	= 300,
_Cs_GateSpacing			= None,
_Cs_SDWidth				= None,
_Cs_XVT					= 'SLVT', 
_Cs_PCCrit				= None,

    #Pmos dummy option
_Cs_PMOSDummy_length	= None,
_Cs_PMOSDummy_placement = None,

# PMOS Switch
    #PMOS
_Sw_PMOSNumberofGate	= 2,
_Sw_PMOSChannelWidth	= 1600,
_Sw_PMOSChannellength	= 30,
_Sw_GateSpacing			= None,
_Sw_SDWidth				= None,
_Sw_XVT					= 'SLVT',
_Sw_PCCrit				= None,

    #Pmos dummy option
_Sw_PMOSDummy_length	= None,
_Sw_PMOSDummy_placement = None,

# NbodyRing
_NumCont			= 2,
_right_margin 		= 150,
_left_margin 		= 150,
_up_margin 			= 150,
_down_margin 		= 150,


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
    LayoutObj = _guardring(_DesignParameter=None, _Name=cellname)
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
