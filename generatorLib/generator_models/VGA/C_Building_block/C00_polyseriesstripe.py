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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C00_polyseriesstripe
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C01_nmos_sw
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C03_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.C_Building_block import C04_routing_guardring


############################################################################################################################################################ Class_HEADER
class _polyseriesstripe(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
                                            _Polyres_R_X_width  = 2500,
                                            _Polyres_R_Y_length = 1500,
                                            _Polyres_CoXNum     = None,
                                            _Polyres_CoYNum     = None,
                                            _Polyres_N_Parallel = None,
                                            _Polyres_Dummy      = False,
                                            _Poly_up_connect 	= True,

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
                                        _Polyres_N_Parallel = None,
                                        _Polyres_Dummy      = False,
                                        _Poly_up_connect 	= True,

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
        self._DesignParameter['_Polyres']['_Angle'] = 0

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
        self._DesignParameter['_Polyres_for_coordcal']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Polyres_for_coordcal']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Polyres_for_coordcal']['_XYCoordinates']=[[0, 0]]

        ############################################################################################################################################################ Polyres_SREF_Generation_placing_cal
        print('##     Polyres_SREF_Generation_placing_cal    ##')

        XY_coord = [[0,0]]
        for i in range(0,_Polyres_N_Parallel-1):

            #Calculate Sref XYcoord
                #initialized Sref coordinate
            self._DesignParameter['_Polyres_for_coordcal']['_XYCoordinates'] = [[0,0]]
                #Calculation
            tmp1 = self.get_param_KJH2('_Polyres','PRES_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_for_coordcal','PRES_boundary_0')
            tmp3 = self.get_param_KJH2('_Polyres_for_coordcal')

            tmp = int('{}'.format(i))
            target_coord        = tmp1[tmp]['_XY_down_right']
            approaching_coord   = tmp2[0]['_XY_down_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres']['_XYCoordinates'] = XY_coord

        ############################################################################################################################################################ Polyres_dummy_SREF_Generation
        print('##     Polyres_dummy_SREF_Generation    ##')

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A16_UNITR.UNITR._ParametersForDesignCalculation)
        _Caculation_Parameters['R_X_width']     = _Polyres_R_X_width
        _Caculation_Parameters['R_Y_length']    = _Polyres_R_Y_length
        _Caculation_Parameters['_CoXNum'] 	    = _Polyres_CoXNum
        _Caculation_Parameters['_CoYNum']  	    = _Polyres_CoYNum

        #Generate Sref
        self._DesignParameter['_Polyres_dummy'] = self._SrefElementDeclaration(_DesignObj=A16_UNITR.UNITR( _DesignParameter=None, _Name='{}:_Polyres_dummy'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Polyres_dummy']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Polyres_dummy']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Polyres_dummy']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Polyres_dummy']['_XYCoordinates']=[[0, 0]]

        ############################################################################################################################################################ Polyres_dummy_placement_cal
        print('##     Polyres_dummy_placement_cal    ##')

        if _Polyres_Dummy == True:

            XY_coord = []

                ############################################################################################################################################## Polyres_dummy_placement_cal:left poly
            print('##     Polyres_dummy_placement_cal:left poly    ##')

            #Calculate Sref XYcoord
                #initialized Sref coordinate
            self._DesignParameter['_Polyres_dummy']['_XYCoordinates'] = [[0,0]]
                #Calculation
            tmp1 = self.get_param_KJH2('_Polyres','PRES_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_dummy','PRES_boundary_0')
            tmp3 = self.get_param_KJH2('_Polyres_dummy')

            target_coord        = tmp1[0]['_XY_down_left']
            approaching_coord   = tmp2[0]['_XY_down_right']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres_dummy']['_XYCoordinates'] = XY_coord

                ############################################################################################################################################## Polyres_dummy_placement_cal:right poly
            print('##     Polyres_dummy_placement_cal:right poly    ##')

            #Calculate Sref XYcoord
                #initialized Sref coordinate
            self._DesignParameter['_Polyres_dummy']['_XYCoordinates'] = [[0,0]]
                #Calculation
            tmp1 = self.get_param_KJH2('_Polyres','PRES_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_dummy','PRES_boundary_0')
            tmp3 = self.get_param_KJH2('_Polyres_dummy')

            target_coord        = tmp1[-1]['_XY_down_right']
            approaching_coord   = tmp2[0]['_XY_down_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres_dummy']['_XYCoordinates'] = XY_coord

        else:
            pass

        ############################################################################################################################################################ M1_connection
        print('##     M1_connection    ##')

        #check the number of real practical poly
        N = len(self.get_param_KJH2('_Polyres'))

        #If only one resistor, then connection is not needed
        if N>=2:
            ############################################################################################################################################## M1_connection:genM1
            print('##     M1_connection:genM1    ##')

            #Define Boundary_element
            self._DesignParameter['_Polyres_m1_connect'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

            #Define Boundary_element _YWidth
            self._DesignParameter['_Polyres_m1_connect']['_YWidth'] = self._DesignParameter['_Polyres']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']

            #Define Boundary_element _XWidth
            tmp = self.get_param_KJH2('_Polyres','_Met1Layer')
            self._DesignParameter['_Polyres_m1_connect']['_XWidth'] = tmp[0]['_XY_left'][0] - tmp[2]['_XY_right'][0]

            #Initialize coordinate
            self._DesignParameter['_Polyres_m1_connect']['_XYCoordinates'] = [[0,0]]

            ############################################################################################################################################## M1_connection:placement
            print('##     M1_connection:placement    ##')

            tmp_xy = []

            # if up_connect
            if _Poly_up_connect == True:

                #Initial value
                j = 1

                for i in range(_Polyres_N_Parallel-1):

                # Calculate Boundary_element XYcoord
                    tmp1 = self.get_param_KJH2('_Polyres', '_Met1Layer')

                    if i ==0:
                        j = j
                    elif i%2 == 0:
                        j = j + 3
                    else:
                        j = j + 1

                    target_coord = tmp1[int('{}'.format(j))]['_XY_down_left']
                    approaching_type = '_XY_down_right'
                    B_XWidth = self.getXWidth('_Polyres_m1_connect')
                    B_YWidth = self.getYWidth('_Polyres_m1_connect')

                    New_Bcoord = self.get_Bcoord_KJH(target_coord, approaching_type, B_XWidth, B_YWidth)

                    tmp_xy.append(New_Bcoord)

            # if down_connect
            else:

                #Flag
                j = 0

                for i in range(_Polyres_N_Parallel-1):

                # Calculate Boundary_element XYcoord
                    tmp1 = self.get_param_KJH2('_Polyres', '_Met1Layer')

                    if i ==0:
                        j = j
                    elif i%2 == 0:
                        j = j + 1
                    else:
                        j = j + 3

                    target_coord = tmp1[int('{}'.format( j ))]['_XY_down_left']
                    approaching_type = '_XY_down_right'
                    B_XWidth = self.getXWidth('_Polyres_m1_connect')
                    B_YWidth = self.getYWidth('_Polyres_m1_connect')

                    New_Bcoord = self.get_Bcoord_KJH(target_coord, approaching_type, B_XWidth, B_YWidth)

                    tmp_xy.append(New_Bcoord)

            self._DesignParameter['_Polyres_m1_connect']['_XYCoordinates'] = tmp_xy

        ############################################################################################################################################################ OP_covering
        print('##     OP_covering    ##')

        if _Polyres_Dummy == True:
            ############################################################################################################################################## OP_covering:if dummy
            print('##     OP_covering:if dummy    ##')
            
            #Define Boundary_element
            self._DesignParameter['_Polyres_opcovering'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['OP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['OP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

            #Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH2('_Polyres_dummy','OP_boundary_0')
            self._DesignParameter['_Polyres_opcovering']['_YWidth'] = tmp1[0]['_Ywidth']

            #Define Boundary_element _XWidth
            tmp2 = self.get_param_KJH2('_Polyres_dummy','OP_boundary_0')
            self._DesignParameter['_Polyres_opcovering']['_XWidth'] = tmp2[-1]['_XY_right'][0] - tmp2[0]['_XY_left'][0]

            #Define Boundary_element _XYCoordinates
                #Calculate Sref XYcoord
                    #initialized Sref coordinate
            self._DesignParameter['_Polyres_opcovering']['_XYCoordinates'] = [[0,0]]
                    #Calculation
            tmp1 = self.get_param_KJH2('_Polyres_dummy','OP_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_opcovering')
            tmp3 = self.get_param_KJH2('_Polyres_opcovering')

            target_coord        = tmp1[0]['_XY_left']
            approaching_coord   = tmp2[0]['_XY_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord=[]
            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres_opcovering']['_XYCoordinates'] = XY_coord
            
        else:   
            ############################################################################################################################################## OP_covering:if not dummy
            print('##     OP_covering:if not dummy    ##')  
            
            #Define Boundary_element
            self._DesignParameter['_Polyres_opcovering'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['OP'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['OP'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

            #Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH2('_Polyres','OP_boundary_0')
            self._DesignParameter['_Polyres_opcovering']['_YWidth'] = tmp1[0]['_Ywidth']

            #Define Boundary_element _XWidth
            tmp2 = self.get_param_KJH2('_Polyres','OP_boundary_0')
            self._DesignParameter['_Polyres_opcovering']['_XWidth'] = tmp2[-1]['_XY_right'][0] - tmp2[0]['_XY_left'][0]

            #Define Boundary_element _XYCoordinates
                #Calculate Sref XYcoord
                    #initialized Sref coordinate
            self._DesignParameter['_Polyres_opcovering']['_XYCoordinates'] = [[0,0]]
                    #Calculation
            tmp1 = self.get_param_KJH2('_Polyres','OP_boundary_0')
            tmp2 = self.get_param_KJH2('_Polyres_opcovering')
            tmp3 = self.get_param_KJH2('_Polyres_opcovering')

            target_coord        = tmp1[0]['_XY_left']
            approaching_coord   = tmp2[0]['_XY_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            XY_coord=[]
            XY_coord.append(New_Scoord.tolist())
            self._DesignParameter['_Polyres_opcovering']['_XYCoordinates'] = XY_coord
        

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

    libname = 'Proj_VGA_C_building_block'
    cellname = '_polyseriesstripe_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
                            _Polyres_R_X_width  = 2500,
                            _Polyres_R_Y_length = 1500,
                            _Polyres_CoXNum     = None,
                            _Polyres_CoYNum     = None,
                            _Polyres_N_Parallel = 5,
                            _Polyres_Dummy      = True,
                            _Poly_up_connect 	= True,

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
    LayoutObj = _polyseriesstripe(_DesignParameter=None, _Name=cellname)
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
