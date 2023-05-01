from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

## ########################################################################################################################################################## Class_HEADER
class _ViaM0toM1_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_ViaMet02Met1NumberOfCOX=None,
_ViaMet02Met1NumberOfCOY=None,

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

_ViaMet02Met1NumberOfCOX=None,
_ViaMet02Met1NumberOfCOY=None,

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

            ## ################################################################################################################### Pre-defined: Coordination
        _XYCoordinateOfViaPoly2Met1 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet02Met1NumberOfCOX ==0 or _ViaMet02Met1NumberOfCOY==0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,NumOfCOY=_ViaMet02Met1NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1)*_LengthViaPoly2Met1BtwCO + 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1)*_LengthViaPoly2Met1BtwCO + 2*_DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        #Define Boundary_element Coordinates
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### Metal1 Layer
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,NumOfCOY=_ViaMet02Met1NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1)* _LengthViaPoly2Met1BtwCO+ 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX,NumOfCOY=_ViaMet02Met1NumberOfCOY )

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet02Met1NumberOfCOX):
            for j in range(0, _ViaMet02Met1NumberOfCOY):

                if (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5 )*_LengthViaPoly2Met1BtwCO + j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY-1)/2  * _LengthViaPoly2Met1BtwCO +j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2)==0:
                    _xycoordinatetmp =[_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX -1) / 2  * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                       _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5 ) *_LengthViaPoly2Met1BtwCO + j*_LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX -1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY-1)/2 * _LengthViaPoly2Met1BtwCO +j*_LengthViaPoly2Met1BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')











    ## ################################################################################################################################################ _CalculateDesignParameterXmin
    def _CalculateDesignParameterXmin(self,

_ViaMet02Met1NumberOfCOX=None,
_ViaMet02Met1NumberOfCOY=None,

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

            ## ################################################################################################################### Pre-defined: Coordination
        _XYCoordinateOfViaPoly2Met1 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet02Met1NumberOfCOX ==0 or _ViaMet02Met1NumberOfCOY==0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)		

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * 4

        #Define Boundary_element Coordinates
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### Metal1 Layer
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)		

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet02Met1NumberOfCOX):
            for j in range(0, _ViaMet02Met1NumberOfCOY):

                if (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY - 1) / 2 * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX - 1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX - 1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY - 1) / 2 * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')















    ## ################################################################################################################################################ _CalculateDesignParameterYmin
    def _CalculateDesignParameterYmin(self,

_ViaMet02Met1NumberOfCOX=None,
_ViaMet02Met1NumberOfCOY=None,

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

            ## ################################################################################################################### Pre-defined: Coordination
        _XYCoordinateOfViaPoly2Met1 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet02Met1NumberOfCOX ==0 or _ViaMet02Met1NumberOfCOY==0:
            print(('**** Error occured in {} Design Parameter Calculation****'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)		
        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * 4

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide

        #Define Boundary_element Coordinates
        self._DesignParameter['_POLayer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### Metal1 Layer
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)		

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOY - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer']['_XWidth'] = _DRCObj._CoMinWidth + (_ViaMet02Met1NumberOfCOX - 1) * _LengthViaPoly2Met1BtwCO + 2 * _DRCObj._Metal1MinEnclosureCO2

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = _XYCoordinateOfViaPoly2Met1

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['CONT'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['CONT'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._CoMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._CoMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaPoly2Met1BtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_ViaMet02Met1NumberOfCOX, NumOfCOY=_ViaMet02Met1NumberOfCOY)

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet02Met1NumberOfCOX):
            for j in range(0, _ViaMet02Met1NumberOfCOY):

                if (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 0 and (_ViaMet02Met1NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY - 1) / 2 * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX - 1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY / 2 - 0.5) * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]

                elif (_ViaMet02Met1NumberOfCOX % 2) == 1 and (_ViaMet02Met1NumberOfCOY % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfViaPoly2Met1[0][0] - (_ViaMet02Met1NumberOfCOX - 1) / 2 * _LengthViaPoly2Met1BtwCO + i * _LengthViaPoly2Met1BtwCO,
                                        _XYCoordinateOfViaPoly2Met1[0][1] - (_ViaMet02Met1NumberOfCOY - 1) / 2 * _LengthViaPoly2Met1BtwCO + j * _LengthViaPoly2Met1BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A10_ViaM0toM1_KJH_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_ViaMet02Met1NumberOfCOX=2,
_ViaMet02Met1NumberOfCOY=2,

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
    LayoutObj = _ViaM0toM1_KJH(_DesignParameter=None, _Name=cellname)
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




