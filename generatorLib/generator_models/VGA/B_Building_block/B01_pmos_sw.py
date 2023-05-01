'''


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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B00_polyresparallel

############################################################################################################################################################ Class_HEADER
class _pmos_sw(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                            _PMOSNumberofGate=20,
                                            _PMOSChannelWidth=1000,
                                            _PMOSChannellength=30,
                                            _PMOSDummy=True,
                                            _GateSpacing=None,
                                            _SDWidth=None,
                                            _XVT='SLVT',
                                            _PCCrit=None,

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

                                        _PMOSNumberofGate=20,
                                        _PMOSChannelWidth=1000,
                                        _PMOSChannellength=30,
                                        _PMOSDummy=True,
                                        _GateSpacing=None,
                                        _SDWidth=None,
                                        _XVT='SLVT',
                                        _PCCrit=None,
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

    ############################################################################################################################################## SREF Generation:PMOS
        print('##     SREF Generation:PMOS    ##')

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A02_PMOSWithDummy._PMOS._ParametersForDesignCalculation)
        _Caculation_Parameters['_PMOSNumberofGate']  	= _PMOSNumberofGate
        _Caculation_Parameters['_PMOSChannelWidth']  	= _PMOSChannelWidth
        _Caculation_Parameters['_PMOSChannellength'] 	= _PMOSChannellength
        _Caculation_Parameters['_PMOSDummy']  			= _PMOSDummy
        _Caculation_Parameters['_GateSpacing']  		= _GateSpacing
        _Caculation_Parameters['_SDWidth']  			= _SDWidth
        _Caculation_Parameters['_XVT']  				= _XVT
        _Caculation_Parameters['_PCCrit']  				= _PCCrit

        #Generate Sref
        self._DesignParameter['_Pmos'] = self._SrefElementDeclaration(_DesignObj=A02_PMOSWithDummy._PMOS( _DesignParameter=None, _Name='{}:_Pmos'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Pmos']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Pmos']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Pmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Pmos']['_XYCoordinates']=[[0, 0]]

    ############################################################################################################################################## Polygate_connect
        print('##     Polygate_connect    ##')

        ################################################################################################################################ Polygate_connect:Vtc_poly
        print('##     Polygate_connect:Vtc_poly    ##')

        #Pre-defined
        Vtc_poly_ydistance = 100

        #Define Boundary_element
        self._DesignParameter['_Pmos_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Pmos_vtc_poly']['_YWidth'] = Vtc_poly_ydistance

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Pmos','_POLayer')
        self._DesignParameter['_Pmos_vtc_poly']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Pmos','_POLayer')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Pmos_vtc_poly']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Pmos','_POLayer')
            tmp2 = self.get_param_KJH2('_Pmos_vtc_poly')
            tmp3 = self.get_param_KJH2('_Pmos_vtc_poly')

            target_coord        = tmp1[i]['_XY_down_left']
            approaching_coord   = tmp2[0]['_XY_up_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['_Pmos_vtc_poly']['_XYCoordinates'] = tmpXY


        ################################################################################################################################ Polygate_connect:Hrz_poly
        print('##     Polygate_connect:Hrz_poly    ##')

        #Pre-defined
        Horz_poly_ywidth = 50

        #Define Boundary_element
        self._DesignParameter['_Pmos_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Pmos_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Pmos','_POLayer')
        self._DesignParameter['_Pmos_hrz_poly']['_XWidth'] = abs( tmp[-1]['_XY_right'][0] - tmp[0]['_XY_left'][0] )

        #Define Boundary_element _XYCoordinates
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Pmos_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Pmos_vtc_poly')
        tmp2 = self.get_param_KJH2('_Pmos_hrz_poly')
        tmp3 = self.get_param_KJH2('_Pmos_hrz_poly')

        target_coord        = tmp1[0]['_XY_down_left']
        approaching_coord   = tmp2[0]['_XY_up_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Pmos_hrz_poly']['_XYCoordinates'] = [New_Scoord]

        ################################################################################################################################ PMOS drain V1(M1-M2)
        print('##     PMOS drain V1(M1-M2)    ##')

        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Pmos_drain_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Pmos_drain_Via1_M1M2'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Pmos_drain_Via1_M1M2']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Pmos_drain_Via1_M1M2']['_Angle'] = 0

        #Define Cox
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

        #Define Coy
            #Calculate Number of V1
        M1_ywidth   = self.getYWidth('_Pmos','_Met1Layer')
        Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

            #Define Num of V1
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

        #M1, M2 and V1 layer XY_width are calculated
        self._DesignParameter['_Pmos_drain_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V1 coord: Source & Drain Zigzag placing
            #initialize coord
        self._DesignParameter['_Pmos_drain_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Define flag
        flag = 1

            #For num of M1 in Pmos
        tmp1 = self.get_param_KJH2('_Pmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Pmos_drain_Via1_M1M2','_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                #tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] ]
                #tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Pmos_drain_Via1_M1M2']['_XYCoordinates'] = tmpXY

        ################################################################################################################################ PMOS drain V2(M2-M3)
        print('##     PMOS drain V2(M2-M3)    ##')

        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Pmos_drain_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:_Pmos_drain_Via2_M2M3'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Pmos_drain_Via2_M2M3']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_Pmos_drain_Via2_M2M3']['_Angle'] = 0

        #Define Cox
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 1

        #Define Coy
        Num_V2 = Num_V1
        if Num_V2 < 4:
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 4
        else:
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = Num_V2

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Pmos_drain_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V2 coord:
        self._DesignParameter['_Pmos_drain_Via2_M2M3']['_XYCoordinates'] = self._DesignParameter['_Pmos_drain_Via1_M1M2']['_XYCoordinates']

        print('###############      For Debugging      ##################')



############################################################################################################################################################ CALCULATION END
        print ('#########################################################################################################')
        print ('                                      Calculation   END                                                  ')
        print ('#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_B_building_block'
    cellname = 'B01_pmos_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

                            _PMOSNumberofGate=3,
                            _PMOSChannelWidth=500,
                            _PMOSChannellength=30,
                            _PMOSDummy=True,
                            _GateSpacing=None,
                            _SDWidth=None,
                            _XVT='SLVT',
                            _PCCrit=None,

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
    LayoutObj = _pmos_sw(_DesignParameter=None, _Name=cellname)
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
