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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.E_Building_block import E00_ncap_nbias

## ########################################################################################################################################################## Class_HEADER
class _guardring(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

#Ncap
_XWidth		=None, 		## Poly Xwidthh
_YWidth		=None,		## OD Ywidht
_NumofGates	=None,			## Column
_NumofOD	=None,			## Row

#M1 Routing: Connecting gates
_Routing_flag = None,

#Nbias_hrz_length
_Nbias_hrz_legnth = None,

# PbodyRing
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeft		= None,
_NumContRight		= None,
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

#Ncap
_XWidth		=None, 		## Poly Xwidthh
_YWidth		=None,		## OD Ywidht
_NumofGates	=None,			## Column
_NumofOD	=None,			## Row

#M1 Routing: Connecting gates
_Routing_flag = None,

#Nbias_hrz_length
_Nbias_hrz_legnth = None,

# PbodyRing
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeft		= None,
_NumContRight		= None,
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

            ## ################################################################################################################### Gen ncap
            # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(E00_ncap_nbias._ncap_nbias._ParametersForDesignCalculation)
        _Caculation_Parameters['_XWidth'] 		            = _XWidth
        _Caculation_Parameters['_YWidth'] 		            = _YWidth
        _Caculation_Parameters['_NumofGates'] 	            = _NumofGates
        _Caculation_Parameters['_NumofOD'] 			        = _NumofOD
        
        _Caculation_Parameters['_Routing_flag'] 			= _Routing_flag
        
        _Caculation_Parameters['_Nbias_hrz_legnth'] 		= _Nbias_hrz_legnth

            # Generate Sref
        self._DesignParameter['_Nbias'] = self._SrefElementDeclaration(_DesignObj=E00_ncap_nbias._ncap_nbias(_DesignParameter=None, _Name='{}:_Nbias'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Nbias']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Nbias']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Nbias']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Nbias']['_XYCoordinates'] = [[0,0]]

            ## ################################################################################################################### Pbody Guardring
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A07_PbodyRing_KJH._PbodyRing_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] 		= None
        _Caculation_Parameters['_YlengthIntn'] 		= None
        _Caculation_Parameters['_NumContTop'] 		= _NumContTop
        _Caculation_Parameters['_NumContBottom'] 	= _NumContBottom
        _Caculation_Parameters['_NumContLeft'] 		= _NumContLeft
        _Caculation_Parameters['_NumContRight'] 	= _NumContRight

        #Find Outter boundary
        tmp = self.get_outter_KJH('_Nbias')

        # Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] 		= abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0] ) + _right_margin + _left_margin

        # Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] 		= abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0] ) + _up_margin + _down_margin

        # Generate Sref
        self._DesignParameter['_Pbodyring'] = self._SrefElementDeclaration(_DesignObj=A07_PbodyRing_KJH._PbodyRing_KJH(_DesignParameter=None, _Name='{}:_Pbodyring'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Pbodyring']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Pbodyring']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Pbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Pbodyring']['_XYCoordinates'] = [[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Pbodyring']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord 		
        target_coord = [ tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0] ]  
                #Approaching_coord
                    #x
        tmp2_1 = self.get_param_KJH3('_Pbodyring','_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')  
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                    #y
        tmp2_2 = self.get_param_KJH3('_Pbodyring','_PbodyBottom','_PbodyContactPhyLen','_Met1Layer')  
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1] 

        approaching_coord = [approaching_coordx,approaching_coordy]
                #Sref coord
        tmp3 = self.get_param_KJH3('_Pbodyring')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Pbodyring']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Port2-Guardirng M1 connection
        # Define Boundary_element
        self._DesignParameter['_Port2_m1_conn'] = self._BoundaryElementDeclaration(
            _Layer=DesignParameters._LayerMapping['METAL1'][0],
            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
            _XWidth=None,
            _YWidth=None,
            _XYCoordinates=[],
        )

        # Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH3('_Nbias','_Ncap','_M1RailPort2')
        tmp2 = self.get_param_KJH3('_Pbodyring','_ExtenMet1Layer_Right','_BoundaryElement')
        self._DesignParameter['_Port2_m1_conn']['_XWidth'] = abs( tmp2[0][0][0][0]['_XY_left'][0] - tmp1[0][0][0][0]['_XY_right'][0] )

        # Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH3('_Nbias','_Ncap','_M1RailPort2')
        self._DesignParameter['_Port2_m1_conn']['_YWidth'] = tmp3[0][0][0][0]['_Ywidth']

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Port2_m1_conn']['_XYCoordinates'] = [[0,0]]

            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Nbias','_Ncap','_M1RailPort2')
        target_coord = tmp1[0][0][0][0]['_XY_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Port2_m1_conn')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Port2_m1_conn')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)

            #Define
        self._DesignParameter['_Port2_m1_conn']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_E_building_block'
    cellname = 'E01_guardring_70'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
    
#Ncap
_XWidth		=2500, 		## Poly Xwidthh
_YWidth		=2500,		## OD Ywidht
_NumofGates	=3,			## Column
_NumofOD	=2,			## Row

#M1 Routing: Connecting gates
_Routing_flag = True,

#Nbias_hrz_length
_Nbias_hrz_legnth = 20000,

# PbodyRing
_NumContTop			= 3,
_NumContBottom		= 3,
_NumContLeft		= 3,
_NumContRight		= 3,
_right_margin 		= 154,
_left_margin 		= 143,
_up_margin 			= 132,
_down_margin 		= 121,

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
