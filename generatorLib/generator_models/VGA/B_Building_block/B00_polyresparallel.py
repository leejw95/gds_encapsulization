'''
1. connection between poly res by M1 metal may cause DRC in future...

'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
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

############################################################################################################################################################ Class_HEADER
class _polyresparallel(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
                                            _Polyres_R_X_width  = 2500,
                                            _Polyres_R_Y_length = 1500,
                                            _Polyres_CoXNum     = None,
                                            _Polyres_CoYNum     = None,
                                            _Polyres_Dummy      = True,
                                            _Polyres_N_Parallel = None,




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
                                        _Polyres_R_X_width  = 2500,
                                        _Polyres_R_Y_length = 1500,
                                        _Polyres_CoXNum     = None,
                                        _Polyres_CoYNum     = None,
                                        _Polyres_Dummy      = True,
                                        _Polyres_N_Parallel = None,


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

############################################################################################################################################################ Polyres_SREF_Generation
        print('##     Polyres_SREF_Generation    ##')

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A16_UNITR.UNITR._ParametersForDesignCalculation)
        _Caculation_Parameters['R_X_width']     = _Polyres_R_X_width
        _Caculation_Parameters['R_Y_length']    = _Polyres_R_Y_length
        _Caculation_Parameters['_CoXNum'] 	    = _Polyres_CoXNum
        _Caculation_Parameters['_CoYNum']  	    = _Polyres_CoYNum

        #Generate Sref
        self._DesignParameter['_Polyres'] = self._SrefElementDeclaration(_DesignObj=A16_UNITR.UNITR( _DesignParameter=None, _Name='{}:_Polyres'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Polyres']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Polyres']['_Angle'] = 90

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Polyres']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Polyres']['_XYCoordinates']=[[0, 0]]

############################################################################################################################################################ Polyres_SREF_Generation_for_coordcal
        print('##     Polyres_SREF_Generation_for_coordcal    ##')

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A16_UNITR.UNITR._ParametersForDesignCalculation)
        _Caculation_Parameters['R_X_width']     = _Polyres_R_X_width
        _Caculation_Parameters['R_Y_length']    = _Polyres_R_Y_length
        _Caculation_Parameters['_CoXNum'] 	    = _Polyres_CoXNum
        _Caculation_Parameters['_CoYNum']  	    = _Polyres_CoYNum

        #Generate Sref
        self._DesignParameter['_Polyres_for_coordcal'] = self._SrefElementDeclaration(_DesignObj=A16_UNITR.UNITR( _DesignParameter=None, _Name='{}:_Polyres_for_coorcal'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Polyres_for_coordcal']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Polyres_for_coordcal']['_Angle'] = 90

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Polyres_for_coordcal']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Polyres_for_coordcal']['_XYCoordinates']=[[0, 0]]

############################################################################################################################################################ Polyres_SREF_Generation_coord_cal
        print('##     Polyres_SREF_Generation_coord_cal    ##')

        #n_of_polyres
        if _Polyres_Dummy == True:
            n_of_polyres = _Polyres_N_Parallel + 2
        else:
            n_of_polyres = _Polyres_N_Parallel


        XY_coord = [[0,0]]
        for i in range(0,n_of_polyres-1):

            #Calculate Sref XYcoord
                #initialized Sref coordinate
            self._DesignParameter['_Polyres_for_coordcal']['_XYCoordinates'] = [[0,0]]
                #Calculation
            tmp1 = self.get_param_KJH2('_Polyres','PRES_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_for_coordcal','PRES_boundary_0')
            tmp3 = self.get_param_KJH2('_Polyres_for_coordcal')

            tmp = int('{}'.format(i))
            target_coord        = tmp1[tmp]['_XY_down']
            approaching_coord   = tmp2[0]['_XY_up']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres']['_XYCoordinates'] = XY_coord


############################################################################################################################################################ Connect_Polyres:M1
        print('##     Connect_Polyres:M1    ##')

        #check the number of real practical poly
        N = len(self.get_param_KJH2('_Polyres'))
        if _Polyres_Dummy == True:
            N = N - 2
        else:
            N = N

        #If only one resistor, then connection is not needed
        if N>=2:

            #Define Boundary_element
            self._DesignParameter['_Polyres_m1_connect'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )
            #Define Boundary_element _YWidth
            self._DesignParameter['_Polyres_m1_connect']['_YWidth'] = self._DesignParameter['_Polyres']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']


            #Define Boundary_element _XWidth
            tmp = self.get_param_KJH2('_Polyres','_Met1Layer')
            self._DesignParameter['_Polyres_m1_connect']['_XWidth'] = tmp[1]['_XY_up'][0] - tmp[2]['_XY_down'][0]

            # Define Boundary_element _XYCoordinates
            if _Polyres_Dummy == True:

                tmp_xy = []
                for i in range(0, N-1):
                    # Calculate Boundary_element XYcoord
                    tmp1 = self.get_param_KJH2('_Polyres', '_Met1Layer')

                    target_coord = tmp1[int('{}'.format( 2*i + 3))]['_XY_up']
                    approaching_type = '_XY_right'
                    B_XWidth = self.getXWidth('_Polyres_m1_connect')
                    B_YWidth = self.getYWidth('_Polyres_m1_connect')

                    New_Bcoord = self.get_Bcoord_KJH(target_coord, approaching_type, B_XWidth, B_YWidth)

                    tmp_xy.append(New_Bcoord)

                self._DesignParameter['_Polyres_m1_connect']['_XYCoordinates'] = tmp_xy

            else:

                tmp_xy = []
                for i in range(0, N-1):
                    # Calculate Boundary_element XYcoord
                    tmp1 = self.get_param_KJH2('_Polyres', '_Met1Layer')

                    target_coord = tmp1[int('{}'.format( 2*i + 1))]['_XY_up']
                    approaching_type = '_XY_right'
                    B_XWidth = self.getXWidth('_Polyres_m1_connect')
                    B_YWidth = self.getYWidth('_Polyres_m1_connect')

                    New_Bcoord = self.get_Bcoord_KJH(target_coord, approaching_type, B_XWidth, B_YWidth)

                    tmp_xy.append(New_Bcoord)

                self._DesignParameter['_Polyres_m1_connect']['_XYCoordinates'] = tmp_xy

        ################################################################################################################################ PMOS drain V1(M1-M2)
        print('##     PMOS drain V1(M1-M2)    ##')

        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Polyres_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Polyres_Via1_M1M2'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Polyres_Via1_M1M2']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Polyres_Via1_M1M2']['_Angle'] = 0

        #Define Cox
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

        #Define Coy
            #Calculate Number of V1
        tmp = self.get_param_KJH2('_Polyres','_Met1Layer')
        M1_ywidth   = int(tmp[0]['_Xwidth'])
        Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

            #Define Num of V1
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

        #M1, M2 and V1 layer XY_width are calculated
        self._DesignParameter['_Polyres_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V1 coord
            #initialize coord
        self._DesignParameter['_Polyres_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
  
            #Calculate Sref XYcoord
                #Calculation1:for sw connection
        tmp1 = self.get_param_KJH2('_Polyres','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Polyres_Via1_M1M2','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Polyres_Via1_M1M2')

        target_coord        = tmp1[-1]['_XY_left']
        approaching_coord   = tmp2[0]['_XY_down']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                #Calculation1:resistor connection
        tmp1 = self.get_param_KJH2('_Polyres','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Polyres_Via1_M1M2','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Polyres_Via1_M1M2')

        target_coord        = tmp1[0]['_XY_left']
        approaching_coord   = tmp2[0]['_XY_down']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Polyres_Via1_M1M2']['_XYCoordinates'] = [New_Scoord2,New_Scoord1]

        ################################################################################################################################ PMOS drain V2(M2-M3)
        print('##     PMOS drain V2(M2-M3)    ##')

        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Polyres_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:_Polyres_Via2_M2M3'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Polyres_Via2_M2M3']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Polyres_Via2_M2M3']['_Angle'] = 0


        #Define Cox
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 1

        #Define Coy
        Num_V2 = Num_V1
        if Num_V2 < 4:
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 4
        else:
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = Num_V2

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Polyres_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V2 coord:
        self._DesignParameter['_Polyres_Via2_M2M3']['_XYCoordinates'] = self._DesignParameter['_Polyres_Via1_M1M2']['_XYCoordinates']

        print('###############      For Debugging      ##################')


        #Delete
        del self._DesignParameter['_Polyres_for_coordcal']


############################################################################################################################################################ CALCULATION END
        print ('#########################################################################################################')
        print ('                                      Calculation   END                                                  ')
        print ('#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_B_building_block'
    cellname = 'B00_polyresparallel_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
                            _Polyres_R_X_width  = 2500,
                            _Polyres_R_Y_length = 1500,
                            _Polyres_CoXNum     = None,
                            _Polyres_CoYNum     = None,
                            _Polyres_Dummy      = False,
                            _Polyres_N_Parallel = 5,

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
    LayoutObj = _polyresparallel(_DesignParameter=None, _Name=cellname)
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
