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


## ########################################################################################################################################################## Class_HEADER
class _ncap_nbias(StickDiagram_KJH1._StickDiagram_KJH):

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
        _Caculation_Parameters = copy.deepcopy(A09_Ncap_KJH._Ncap_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XWidth'] 		            = _XWidth
        _Caculation_Parameters['_YWidth'] 		            = _YWidth
        _Caculation_Parameters['_NumofGates'] 	            = _NumofGates
        _Caculation_Parameters['_NumofOD'] 			        = _NumofOD
        
        _Caculation_Parameters['_Routing_flag'] 			= _Routing_flag
        
        _Caculation_Parameters['NumOfCOX'] 					= None ##Fix
        _Caculation_Parameters['NumOfCOY'] 				    = None ##Fix
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] 	= None ##Fix
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] 	= 1    ##Fix

            # Generate Sref
        self._DesignParameter['_Ncap'] = self._SrefElementDeclaration(_DesignObj=A09_Ncap_KJH._Ncap_KJH(_DesignParameter=None, _Name='{}:_Ncap'.format(_Name)))[0]

            # Define Sref Relection
        self._DesignParameter['_Ncap']['_Reflect'] = [0, 0, 0]

            # Define Sref Angle
        self._DesignParameter['_Ncap']['_Angle'] = 0

            # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Ncap']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            # Define Sref _XYcoordinate
        self._DesignParameter['_Ncap']['_XYCoordinates'] = [[0,0]]

            ## ################################################################################################################### Port1 _ViaM1M4
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 1
        _Caculation_Parameters['_Layer2'] 	= 4
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Port1_ViaM1M4'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Port1_ViaM1M4'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Port1_ViaM1M4']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Port1_ViaM1M4']['_Angle'] = 0

        #Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH3('_Ncap','_M1RailPort1')

        #Calcuate _COX and _COY
        _COX, _COY= self._CalculateNumViaByXYWidth(tmp1[0][0][0]['_Xwidth'],tmp1[0][0][0]['_Ywidth'],None)  ## None or 'MinEnclosureX' or 'MinEnclosureY'

        #Define _COX and _COY
        _Caculation_Parameters['_COX'] 		= _COX
        _Caculation_Parameters['_COY'] 		= _COY

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Port1_ViaM1M4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Port1_ViaM1M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Ncap','_M1RailPort1') 
        target_coord = tmp1[0][0][0]['_XY_cent']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Port1_ViaM1M4','_ViaM1M2','_Met1Layer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_cent']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Port1_ViaM1M4')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Port1_ViaM1M4']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Nbias M3
        #Pre-define
        m3_width = 500
            
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_Nbias_m3'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['METAL3'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['METAL3'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Nbias_m3']['_YWidth'] = m3_width

        #Define Boundary_element _XWidth
        tmp = self.get_outter_KJH('_Ncap')
        sref_xlen = ( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0] )

        if _Nbias_hrz_legnth > sref_xlen:
            self._DesignParameter['_Nbias_m3']['_XWidth'] = _Nbias_hrz_legnth
        else:
            self._DesignParameter['_Nbias_m3']['_XWidth'] = sref_xlen

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_Nbias_m3']['_XYCoordinates'] = [[0,0]]

            #Calculate Sref XYcoord
        tmpXY=[]
                #initialized Sref coordinate
        self._DesignParameter['_Nbias_m3']['_XYCoordinates'] = [[0,0]]
                #Calculate
                    #Target_coord
                        #x
        tmp1_1 = self.get_outter_KJH('_Ncap')	
        target_coordx = 0.5 * ( tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0] )
                        #y
        tmp1_2 = self.get_param_KJH3('_Port1_ViaM1M4','_ViaM3M4','_Met3Layer')
        target_coordy = tmp1_2[0][0][0][0]['_XY_up'][1]
        
        target_coord = [target_coordx, target_coordy]
                    #Approaching_coord
        tmp2 = self.get_param_KJH3('_Nbias_m3')  
        approaching_coord = tmp2[0][0]['_XY_up']   
                    #Sref coord
        tmp3 = self.get_param_KJH3('_Nbias_m3')
        Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
                #Define
        self._DesignParameter['_Nbias_m3']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Nbias M4
        #Pre-define
        m3_width = 500
            
        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_Nbias_m4'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping['METAL4'][0],
        _Datatype=DesignParameters._LayerMapping['METAL4'][1],
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[ ],
        )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Nbias_m4']['_YWidth'] = self._DesignParameter['_Nbias_m3']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_Nbias_m4']['_XWidth'] = self._DesignParameter['_Nbias_m3']['_XWidth']

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_Nbias_m4']['_XYCoordinates'] = self._DesignParameter['_Nbias_m3']['_XYCoordinates']


        ''' 보류
            ## ################################################################################################################### Nbias hrz viam3m4
                ## ##################################################################################################### Nbias hrz viam3m4:left
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 3
        _Caculation_Parameters['_Layer2'] 	= 4
        _Caculation_Parameters['_COX'] 		= None
        _Caculation_Parameters['_COY'] 		= None

        #Sref ViaX declaration
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_Nbias_hrz_left_ViaM3M4'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4']['_Angle'] = 0

        #Calcuate Overlapped XYcoord
        tmp1 = self.get_param_KJH3('_Nbias_m3')
        tmp2 = self.get_param_KJH3('_Ncap','_M1RailPort1')

        #X/Ywidthh
        xwidth = abs ( tmp1[0][0]['_XY_left'][0] - tmp2[0][0][0]['_XY_left'][0] ) - 300
        ywidht = tmp1[0][0]['_Ywidth']

        #Calcuate _COX and _COY
        _COX, _COY= self._CalculateNumViaByXYWidth(xwidth,ywidht,'MinEnclosureY')  ## None or 'MinEnclosureX' or 'MinEnclosureY'

        #Define _COX and _COY
        _Caculation_Parameters['_COX'] 		= _COX
        _Caculation_Parameters['_COY'] 		= _COY

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_Nbias_m3') 
        target_coord = tmp1[0][0]['_XY_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_Nbias_hrz_left_ViaM3M4','_ViaM3M4','_Met3Layer')  
        approaching_coord = tmp2[0][0][0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_Nbias_hrz_left_ViaM3M4')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Nbias_hrz_left_ViaM3M4']['_XYCoordinates'] = tmpXY
                ## ##################################################################################################### Nbias hrz viam3m4:right

        '''






        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_E_building_block'
    cellname = 'E00_ncap_nbias_89'
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
    LayoutObj = _ncap_nbias(_DesignParameter=None, _Name=cellname)
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
