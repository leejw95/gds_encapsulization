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
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A19_Boundary_element_KJH


import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G00_nmos_input
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G01_nmos_parallel
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G02_nmos_dummy
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.G_Building_block import G03_guardring



## ########################################################################################################################################################## Class_HEADER
class _Boundary_element_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_Layermapping = None,
_XWidth = None,
_YWidth = None,

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

_Layermapping = None,
_XWidth = None,
_YWidth = None,

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


        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['_BoundaryElement'] = self._BoundaryElementDeclaration(
        _Layer=DesignParameters._LayerMapping[_Layermapping][0],    
        _Datatype=DesignParameters._LayerMapping[_Layermapping][1], 
        _XWidth=None,
        _YWidth=None,
        _XYCoordinates=[ ],
       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_BoundaryElement']['_YWidth'] = _YWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_BoundaryElement']['_XWidth'] = _XWidth

        #Define Boundary_element _XYCoordinates
        self._DesignParameter['_BoundaryElement']['_XYCoordinates'] = [[_XWidth,_YWidth]]


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


## ########################################################################################################################################################## START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A19_Boundary_element_KJH_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
    
    _Layermapping = 'METAL1',
    _XWidth = 2121,
    _YWidth = 211,
    
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
    LayoutObj = _Boundary_element_KJH(_DesignParameter=None, _Name=cellname)
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

    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker_KJH0.DRCchecker()

    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
