from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math
#from SthPack import CoordCalc

## ########################################################################################################################################################## Class_HEADER
class _ViaM4toM5_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_ViaMet42Met5NumberOfCOX=None,
_ViaMet42Met5NumberOfCOY=None,

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

_ViaMet42Met5NumberOfCOX=None,
_ViaMet42Met5NumberOfCOY=None,

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
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### Metal5 Layer
        #Define Boundary_element
        self._DesignParameter['_Met5Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met5Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met5Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met5Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### Metal4 Layer
        #Define Boundary_element
        self._DesignParameter['_Met4Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['VIA45'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['VIA45'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')












    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXmin(self,

_ViaMet42Met5NumberOfCOX=None,
_ViaMet42Met5NumberOfCOY=None

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
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### Metal5 Layer
        #Define Boundary_element
        self._DesignParameter['_Met5Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met5Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met5Layer']['_XWidth'] = _DRCObj._VIAxMinWidth+ (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met5Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### Metal4 Layer
        #Define Boundary_element
        self._DesignParameter['_Met4Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['VIA45'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['VIA45'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')












    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterYmin(self,

_ViaMet42Met5NumberOfCOX=None,
_ViaMet42Met5NumberOfCOY=None

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
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet42Met5NumberOfCOX ==0 or _ViaMet42Met5NumberOfCOY==0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### Metal5 Layer
        #Define Boundary_element
        self._DesignParameter['_Met5Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met5Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met5Layer']['_XWidth'] = _DRCObj._VIAxMinWidth+ (_ViaMet42Met5NumberOfCOX - 1)* _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met5Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### Metal4 Layer
        #Define Boundary_element
        self._DesignParameter['_Met4Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia1,_DRCObj._MetalxMinEnclosureCO])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1)*  _LengthViaMet42Met5BtwCO+ 2 * max([_DRCObj._Metal1MinEnclosureVia12,_DRCObj._MetalxMinEnclosureCO2])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['VIA45'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['VIA45'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY )

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):

                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]

                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates']=tmp

        del _DRCObj

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')










    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameterXYsame(self,

_ViaMet42Met5NumberOfCOX=None,
_ViaMet42Met5NumberOfCOY=None,

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
        _XYCoordinateOfViaMet42Met5 = [[0,0]]


            ## ################################################################################################################### NotImplemented condition
        if _ViaMet42Met5NumberOfCOX == 0 or _ViaMet42Met5NumberOfCOY == 0:
            print(('************************* Error occured in {} Design Parameter Calculation******************************'.format(self._DesignParameter['_Name']['_Name'])))
            if DesignParameters._DebugMode == 0:
                return 0

            ## ################################################################################################################### Metal5 Layer
        #Define Boundary_element
        self._DesignParameter['_Met5Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL5'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL5'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met5Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met5Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met5Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### Metal4 Layer
        #Define Boundary_element
        self._DesignParameter['_Met4Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL4'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL4'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                             )
        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met4Layer']['_YWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOY - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met4Layer']['_XWidth'] = _DRCObj._VIAxMinWidth + (_ViaMet42Met5NumberOfCOX - 1) * _LengthViaMet42Met5BtwCO + 2 * max([_DRCObj._Metal1MinEnclosureVia3,_DRCObj._MetalxMinEnclosureVia3])

        #Define Boundary_element Coordinates
        self._DesignParameter['_Met4Layer']['_XYCoordinates'] = _XYCoordinateOfViaMet42Met5

            ## ################################################################################################################### CONT Layer
        #Define Boundary_element
        self._DesignParameter['_COLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['VIA45'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['VIA45'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_COLayer']['_YWidth'] = _DRCObj._VIAxMinWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_COLayer']['_XWidth'] = _DRCObj._VIAxMinWidth

        #Define _LengthViaPoly2Met1BtwCO
        _LengthViaMet42Met5BtwCO = _DRCObj._VIAxMinWidth + _DRCObj.DRCVIAxMinSpace(NumOfVIAxX=_ViaMet42Met5NumberOfCOX,NumOfVIAxY=_ViaMet42Met5NumberOfCOY)

        #Define Boundary_element Coordinates
            #Calculate coordinates
        tmp=[]
        for i in range(0, _ViaMet42Met5NumberOfCOX):
            for j in range(0, _ViaMet42Met5NumberOfCOY):
                if (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 0 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX / 2 - 0.5) * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2  * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY / 2 - 0.5 )*_LengthViaMet42Met5BtwCO + j*_LengthViaMet42Met5BtwCO]
                elif (_ViaMet42Met5NumberOfCOX % 2) == 1 and (_ViaMet42Met5NumberOfCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfViaMet42Met5[0][0] - (_ViaMet42Met5NumberOfCOX -1) / 2 * _LengthViaMet42Met5BtwCO + i * _LengthViaMet42Met5BtwCO,
                                        _XYCoordinateOfViaMet42Met5[0][1] - (_ViaMet42Met5NumberOfCOY-1)/2 * _LengthViaMet42Met5BtwCO +j*_LengthViaMet42Met5BtwCO]
                tmp.append(_xycoordinatetmp)

            #Define coordinates
        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

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
    cellname = 'A14_ViaM4toM5_KJH_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_ViaMet42Met5NumberOfCOX = 2 ,
_ViaMet42Met5NumberOfCOY = 4 ,

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
    LayoutObj = _ViaM4toM5_KJH(_DesignParameter=None, _Name=cellname)
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




