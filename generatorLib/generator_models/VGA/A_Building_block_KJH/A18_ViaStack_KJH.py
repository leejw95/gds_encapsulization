from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A10_ViaM0toM1_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A11_ViaM1toM2_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A12_ViaM2toM3_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A13_ViaM3toM4_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A14_ViaM4toM5_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A15_ViaM5toM6_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A16_ViaM6toM7_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A17_ViaM7toM8_KJH


## ########################################################################################################################################################## Class_HEADER
class _ViaStack_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
    
_Layer1 = None, #Bottom metal layer
_Layer2 = None, #Top metal layer
_COX=None,
_COY=None,

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

_Layer1 = None,
_Layer2 = None,
_COX=None,
_COY=None,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A10_ViaM0toM1_KJH._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A10_ViaM0toM1_KJH._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM0M1']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM0M1']['_XYCoordinates']=[[0, 0]]

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A11_ViaM1toM2_KJH._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A11_ViaM1toM2_KJH._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM1M2']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM1M2']['_XYCoordinates']=[[0, 0]]

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A12_ViaM2toM3_KJH._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A12_ViaM2toM3_KJH._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM2M3']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM2M3']['_XYCoordinates']=[[0, 0]]

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A13_ViaM3toM4_KJH._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A13_ViaM3toM4_KJH._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM3M4']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM3M4']['_XYCoordinates']=[[0, 0]]

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A14_ViaM4toM5_KJH._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A14_ViaM4toM5_KJH._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM4M5']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM4M5']['_XYCoordinates']=[[0, 0]]

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A15_ViaM5toM6_KJH._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A15_ViaM5toM6_KJH._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM5M6']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM5M6']['_XYCoordinates']=[[0, 0]]

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A16_ViaM6toM7_KJH._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A16_ViaM6toM7_KJH._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM6M7']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM6M7']['_XYCoordinates']=[[0, 0]]

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A17_ViaM7toM8_KJH._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A17_ViaM7toM8_KJH._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM7M8']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM7M8']['_XYCoordinates']=[[0, 0]]
            
            

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXmin(self,

_Layer1 = None,
_Layer2 = None,
_COX=None,
_COY=None,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A10_ViaM0toM1_KJH._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A10_ViaM0toM1_KJH._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM0M1']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM0M1']['_XYCoordinates']=[[0, 0]]

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A11_ViaM1toM2_KJH._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A11_ViaM1toM2_KJH._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM1M2']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM1M2']['_XYCoordinates']=[[0, 0]]

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A12_ViaM2toM3_KJH._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A12_ViaM2toM3_KJH._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM2M3']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM2M3']['_XYCoordinates']=[[0, 0]]

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A13_ViaM3toM4_KJH._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A13_ViaM3toM4_KJH._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM3M4']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM3M4']['_XYCoordinates']=[[0, 0]]

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A14_ViaM4toM5_KJH._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A14_ViaM4toM5_KJH._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM4M5']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM4M5']['_XYCoordinates']=[[0, 0]]

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A15_ViaM5toM6_KJH._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A15_ViaM5toM6_KJH._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM5M6']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM5M6']['_XYCoordinates']=[[0, 0]]

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A16_ViaM6toM7_KJH._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A16_ViaM6toM7_KJH._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM6M7']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM6M7']['_XYCoordinates']=[[0, 0]]

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A17_ViaM7toM8_KJH._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A17_ViaM7toM8_KJH._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM7M8']['_DesignObj']._CalculateDesignParameterXmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM7M8']['_XYCoordinates']=[[0, 0]]
            
            
            
    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterYmin(self,

_Layer1 = None,
_Layer2 = None,
_COX=None,
_COY=None,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Not implemented condition
        if 0 > _Layer1 or 8 < _Layer2 :
            raise NotImplementedError

        if 0 >= _Layer1 and 0 < _Layer2 :
            ## ################################################################################################################### Gen ViaM0M1
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A10_ViaM0toM1_KJH._ViaM0toM1_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet02Met1NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM0M1'] = self._SrefElementDeclaration(_DesignObj=A10_ViaM0toM1_KJH._ViaM0toM1_KJH( _DesignParameter=None, _Name='{}:_ViaM0M1'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM0M1']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM0M1']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM0M1']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM0M1']['_XYCoordinates']=[[0, 0]]

        if 1 >= _Layer1 and 1 < _Layer2 :
            ## ################################################################################################################### Gen ViaM1M2
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A11_ViaM1toM2_KJH._ViaM1toM2_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet12Met2NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM1M2'] = self._SrefElementDeclaration(_DesignObj=A11_ViaM1toM2_KJH._ViaM1toM2_KJH( _DesignParameter=None, _Name='{}:_ViaM1M2'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM1M2']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM1M2']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM1M2']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM1M2']['_XYCoordinates']=[[0, 0]]

        if 2 >= _Layer1 and 2 < _Layer2 :
            ## ################################################################################################################### Gen ViaM2M3
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A12_ViaM2toM3_KJH._ViaM2toM3_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet22Met3NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM2M3'] = self._SrefElementDeclaration(_DesignObj=A12_ViaM2toM3_KJH._ViaM2toM3_KJH( _DesignParameter=None, _Name='{}:_ViaM2M3'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM2M3']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM2M3']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM2M3']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM2M3']['_XYCoordinates']=[[0, 0]]

        if 3 >= _Layer1 and 3 < _Layer2 :
            ## ################################################################################################################### Gen ViaM3M4
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A13_ViaM3toM4_KJH._ViaM3toM4_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet32Met4NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM3M4'] = self._SrefElementDeclaration(_DesignObj=A13_ViaM3toM4_KJH._ViaM3toM4_KJH( _DesignParameter=None, _Name='{}:_ViaM3M4'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM3M4']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM3M4']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM3M4']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM3M4']['_XYCoordinates']=[[0, 0]]

        if 4 >= _Layer1 and 4 < _Layer2 :
            ## ################################################################################################################### Gen ViaM4M5
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A14_ViaM4toM5_KJH._ViaM4toM5_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet42Met5NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM4M5'] = self._SrefElementDeclaration(_DesignObj=A14_ViaM4toM5_KJH._ViaM4toM5_KJH( _DesignParameter=None, _Name='{}:_ViaM4M5'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM4M5']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM4M5']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM4M5']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM4M5']['_XYCoordinates']=[[0, 0]]

        if 5 >= _Layer1 and 5 < _Layer2 :
            ## ################################################################################################################### Gen ViaM5M6
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A15_ViaM5toM6_KJH._ViaM5toM6_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet52Met6NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM5M6'] = self._SrefElementDeclaration(_DesignObj=A15_ViaM5toM6_KJH._ViaM5toM6_KJH( _DesignParameter=None, _Name='{}:_ViaM5M6'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM5M6']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM5M6']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM5M6']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM5M6']['_XYCoordinates']=[[0, 0]]

        if 6 >= _Layer1 and 6 < _Layer2 :
            ## ################################################################################################################### Gen ViaM6M7
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A16_ViaM6toM7_KJH._ViaM6toM7_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet62Met7NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM6M7'] = self._SrefElementDeclaration(_DesignObj=A16_ViaM6toM7_KJH._ViaM6toM7_KJH( _DesignParameter=None, _Name='{}:_ViaM6M7'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM6M7']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM6M7']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM6M7']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM6M7']['_XYCoordinates']=[[0, 0]]

        if 7 >= _Layer1 and 7 < _Layer2 :
            ## ################################################################################################################### Gen ViaM7M8
            #Define Calculation_Parameters
            _Caculation_Parameters = copy.deepcopy( A17_ViaM7toM8_KJH._ViaM7toM8_KJH._ParametersForDesignCalculation)
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOX']  = _COX
            _Caculation_Parameters['_ViaMet72Met8NumberOfCOY']  = _COY

            #Generate Sref
            self._DesignParameter['_ViaM7M8'] = self._SrefElementDeclaration(_DesignObj=A17_ViaM7toM8_KJH._ViaM7toM8_KJH( _DesignParameter=None, _Name='{}:_ViaM7M8'.format(_Name)))[0]

            #Define Sref Relection
            self._DesignParameter['_ViaM7M8']['_Reflect'] = [0, 0, 0]

            #Define Sref Angle
            self._DesignParameter['_ViaM7M8']['_Angle'] = 0

            #Calculate Sref Layer by using Calculation_Parameter
            self._DesignParameter['_ViaM7M8']['_DesignObj']._CalculateDesignParameterYmin(**_Caculation_Parameters)

            #Define Sref _XYcoordinate
            self._DesignParameter['_ViaM7M8']['_XYCoordinates']=[[0, 0]]
                        
            
## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A18_ViaStack_KJH_96'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_Layer1 = 0,
_Layer2 = 8,
_COX    = 4,
_COY    = 4,

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
    LayoutObj = _ViaStack_KJH(_DesignParameter=None, _Name=cellname)
    
    #LayoutObj._CalculateDesignParameter(**InputParams)
    #LayoutObj._CalculateDesignParameterXmin(**InputParams)
    LayoutObj._CalculateDesignParameterYmin(**InputParams)

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




