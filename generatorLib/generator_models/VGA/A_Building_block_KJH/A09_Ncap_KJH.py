from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A18_ViaStack_KJH
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A03_PSubRing

## ########################################################################################################################################################## Class_HEADER
class _Ncap_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_XWidth=None,
_YWidth=None,
_NumofGates=None,
NumOfCOX=None,
NumOfCOY=None,

#M1 Routing: Connecting gates
_Routing_flag = None,

_NumofOD=None,
_ViaPoly2Met1NumberOfCOX=None,
_ViaPoly2Met1NumberOfCOY=None,

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

_XWidth=None,
_YWidth=None,
_NumofGates=None,
NumOfCOX=None,
NumOfCOY=None,

#M1 Routing: Connecting gates
_Routing_flag = None,

_NumofOD=None,
_ViaPoly2Met1NumberOfCOX=None,
_ViaPoly2Met1NumberOfCOY=None,
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

            ## ################################################################################################################### POLY Layer
        #Define Boundary_element
        self._DesignParameter['_POLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Not implemented condition
            #Min Xwidth = 30nm
        if DesignParameters == '028nm':
            if _XWidth < _DRCObj._PolygateMinWidth:
                raise NotImplementedError("Xwidth should be longer than 30nm")
            #Min Area condition
        _DRCgatemaxarea = _DRCObj._PolygateMaxArea
        if DesignParameters == '028nm':
            if _XWidth * _YWidth > _DRCgatemaxarea:
                raise NotImplementedError("poly max area should be less than 38.661um2")

        #Define ODExtensionOnPO
        ODExtensionOnPO = (_DRCObj._OdMinSpace + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2 # (80 + 40 + 20) * 2

        #Define Boundary_element _YWidth
        self._DesignParameter['_POLayer']['_YWidth'] = _YWidth + ODExtensionOnPO

        #Define Boundary_element _XWidth
        self._DesignParameter['_POLayer']['_XWidth'] = _XWidth

        #Define Boundary_element _XYCoordinates
            #Define Origin Coordinates
        MinSnapSpacing = _DRCObj._MinSnapSpacing
        if _XWidth % 2 == 0 and _YWidth % 2 == 0 :
            _XYCoordinatesofNcap = [[0,0]]
        elif _XWidth % 2 == 0 and _YWidth % 2 == 1 :
            _XYCoordinatesofNcap = [[0, MinSnapSpacing/2.0]]
        elif _XWidth % 2 == 1 and _YWidth % 2 == 0 :
            _XYCoordinatesofNcap = [[MinSnapSpacing/2.0,0]]
        elif _XWidth % 2 == 1 and _YWidth % 2 == 1 :
            _XYCoordinatesofNcap = [[MinSnapSpacing/2.0,MinSnapSpacing/2.0]]
            #Calculate Coordinates
        tmp = []
        if _NumofGates % 2 == 0 and _NumofOD % 2 == 0:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - ((_NumofGates - 1) // 2 + 0.5) * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - ((_NumofOD - 1) // 2 + 0.5) * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 0 and _NumofOD % 2 == 1:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - ((_NumofGates - 1) // 2 + 0.5) * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - (_NumofOD - 1) // 2 * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 1 and _NumofOD % 2 == 0:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - (_NumofGates - 1) // 2 * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - ((_NumofOD - 1) // 2 + 0.5) * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])
        if _NumofGates % 2 == 1 and _NumofOD % 2 == 1:
            for j in range(_NumofOD):
                for i in range(_NumofGates):
                    tmp.append([_XYCoordinatesofNcap[0][0] - (_NumofGates - 1) // 2 * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD) + i * (self._DesignParameter['_POLayer']['_XWidth'] + ODExtensionOnPO // 2 + _DRCObj._PolygateMinSpace2OD),
                                _XYCoordinatesofNcap[0][1] - (_NumofOD - 1) // 2 * (_YWidth + _DRCObj._OdSpace_ncap) + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmp
        del tmp

            ## ################################################################################################################### DIFF(OD/RX) Layer
        #Define Boundary_element
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Not implemented condition
            #Min Xwidth = 30nm
        if DesignParameters._Technology == '028nm':
            if _YWidth < _DRCObj._OdMinWidth:
                raise NotImplementedError("Ywidth should be longer than 80nm")

        #Calculate ODExtensionOnPO for Ywidth and Xwidth
        ODExtensionOnPO = (_DRCObj._OdMinSpace + _DRCObj._CoMinWidth + 2 * _DRCObj._CoMinEnclosureByPOAtLeastTwoSide) * 2 # (80 + 40 + 20) * 2

        #Define Boundary_element _YWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _YWidth

        #Define Boundary_element _XWidth
        self._DesignParameter['_ODLayer']['_XWidth'] = _XWidth + ODExtensionOnPO

        #Define XYcoord.
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = self._DesignParameter['_POLayer']['_XYCoordinates']

            ## ################################################################################################################### ViaM0M1_Hrz
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 0
        _Caculation_Parameters['_Layer2'] 	= 1
        _Caculation_Parameters['_COX'] 		= max(1, int(_DRCObj.DRCCOFillAtPoly2Met1(XWidth=_XWidth, YWidth=ODExtensionOnPO, NumOfCOX=NumOfCOX, NumOfCOY=NumOfCOY)[0]))
        _Caculation_Parameters['_COY'] 		= _ViaPoly2Met1NumberOfCOY

        #Sref ViaX declaration
        self._DesignParameter['_ViaM0M1_Hrz'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_ViaM0M1_Hrz'.format(_Name)))[0]
        
        #Define Sref Relection
        self._DesignParameter['_ViaM0M1_Hrz']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_ViaM0M1_Hrz']['_Angle'] = 0
        
        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_ViaM0M1_Hrz']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #change Value
        self._DesignParameter['_ViaM0M1_Hrz']['_DesignObj']._DesignParameter['_ViaM0M1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] = _DRCObj._Metal1MinWidth
        self._DesignParameter['_ViaM0M1_Hrz']['_DesignObj']._DesignParameter['_ViaM0M1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = _DRCObj._Metal1MinWidth

        #Calculate Sref XYcoord
        tmp_m1poly = []
        for j in range(_NumofOD):
            for i in range(_NumofGates):
                if _XWidth % 2 == 0 and _YWidth % 2 == 0:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 0 and _YWidth % 2 == 1:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0],
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 0:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 1:
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_YWidth'] // 2 + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       + 0.5 * _DRCObj._CoMinWidth + (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1poly.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0,
                                       self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_YWidth'] // 2 - _DRCObj._CoMinEnclosureByPOAtLeastTwoSide
                                       - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2) // 2 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        self._DesignParameter['_ViaM0M1_Hrz']['_XYCoordinates'] = tmp_m1poly
        del tmp_m1poly

            ## ################################################################################################################### ViaM0M1_Vtc
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Layer1'] 	= 0
        _Caculation_Parameters['_Layer2'] 	= 1
        _Caculation_Parameters['_COX'] 		= _ViaPoly2Met1NumberOfCOY
        _Caculation_Parameters['_COY'] 		= max(1, int(_DRCObj.DRCCOFillAtOD2Met1(XWidth = ODExtensionOnPO,  YWidth = _YWidth, NumOfCOX = NumOfCOX, NumOfCOY=NumOfCOY)[1]))

        #Sref ViaX declaration
        self._DesignParameter['_ViaM0M1_Vtc'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_ViaM0M1_Vtc'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_ViaM0M1_Vtc']['_Reflect'] = [1, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_ViaM0M1_Vtc']['_Angle'] = 0

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_ViaM0M1_Vtc']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #change Value
        self._DesignParameter['_ViaM0M1_Vtc']['_DesignObj']._DesignParameter['_ViaM0M1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] = 0
        self._DesignParameter['_ViaM0M1_Vtc']['_DesignObj']._DesignParameter['_ViaM0M1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] = 0

        #Calculate Sref XYcoord
        tmp_m1od = []
        for j in range(_NumofOD):
            for i in range(_NumofGates):
                if _XWidth % 2 == 0 and _YWidth % 2 == 0:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 0 and _YWidth % 2 == 1:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 0:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + j * (_YWidth + _DRCObj._OdSpace_ncap)])

                if _XWidth % 2 == 1 and _YWidth % 2 == 1:
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] - MinSnapSpacing/2.0 - self._DesignParameter['_POLayer']['_XWidth'] // 2 - _DRCObj._CoMinSpace
                                     - 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])
                    tmp_m1od.append([self._DesignParameter['_POLayer']['_XYCoordinates'][i][0] + MinSnapSpacing/2.0 + self._DesignParameter['_POLayer']['_XWidth'] // 2 + _DRCObj._CoMinSpace
                                     + 0.5 * _DRCObj._CoMinWidth - (_ViaPoly2Met1NumberOfCOY - 1) * (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace) // 2,
                                     self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] - MinSnapSpacing/2.0 + j * (_YWidth + _DRCObj._OdSpace_ncap)])

        self._DesignParameter['_ViaM0M1_Vtc']['_XYCoordinates'] = tmp_m1od
        del tmp_m1od

            ## ################################################################################################################### LVS Layer
        #Define Boundary_element
        self._DesignParameter['_LVSLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['LVS_dr4'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['LVS_dr4'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                              )

        #Define Boundary_element _YWidth
        self._DesignParameter['_LVSLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_POLayer']['_YWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2

        #Define Boundary_element _XWidth
        self._DesignParameter['_LVSLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_ODLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._CoMinEnclosureByPOAtLeastTwoSide * 2

        #Define XYcoord.
        self._DesignParameter['_LVSLayer']['_XYCoordinates'] = _XYCoordinatesofNcap

            ## ################################################################################################################### Nwell Layer
        #Define Boundary_element
        self._DesignParameter['_Nwell'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                              )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Nwell']['_YWidth'] = self._DesignParameter['_POLayer']['_XYCoordinates'][-1][1] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][1] + self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap

        #Define Boundary_element _XWidth
        self._DesignParameter['_Nwell']['_XWidth'] = self._DesignParameter['_POLayer']['_XYCoordinates'][-1][0] - self._DesignParameter['_POLayer']['_XYCoordinates'][0][0] + self._DesignParameter['_POLayer']['_XWidth'] + 2 * _DRCObj._PolygateMinEnclosureByNcap

        #Define XYcoord.
        self._DesignParameter['_Nwell']['_XYCoordinates'] = self._DesignParameter['_LVSLayer']['_XYCoordinates']

            ## ################################################################################################################### NCap Layer
        #Define Boundary_element
        self._DesignParameter['_NcapLayer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['NCAP'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['NCAP'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                              )

        #Define Boundary_element _YWidth
        self._DesignParameter['_NcapLayer']['_YWidth'] = self._DesignParameter['_Nwell']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_NcapLayer']['_XWidth'] = self._DesignParameter['_Nwell']['_XWidth']

        #Define XYcoord.
        self._DesignParameter['_NcapLayer']['_XYCoordinates'] = self._DesignParameter['_LVSLayer']['_XYCoordinates']




            ## ################################################################################################################### M1 Routing
        if _Routing_flag == True:
            #Define Boundary_element
            self._DesignParameter['_M1Routing'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                  )

            #Define Boundary_element _YWidth
            self._DesignParameter['_M1Routing']['_YWidth'] = 0.5 * _YWidth

            #Define Boundary_element _XWidth
            tmp = self.get_param_KJH3('_ViaM0M1_Vtc','_ViaM0M1','_Met1Layer')
            self._DesignParameter['_M1Routing']['_XWidth'] = abs( tmp[0][0][0][0]['_XY_left'][0] - tmp[2*_NumofGates-1][0][0][0]['_XY_right'][0] )

            #Define XYcoord.
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_M1Routing']['_XYCoordinates'] = [[0,0]]

            for i in range(0,_NumofOD):
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_ViaM0M1_Vtc','_ViaM0M1','_Met1Layer')
                target_coord = tmp1[0 + 2*_NumofGates*i ][0][0][0]['_XY_left']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_M1Routing')
                approaching_coord = tmp2[0][0]['_XY_left']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_M1Routing')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

                #Define
            self._DesignParameter['_M1Routing']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### M1 Rail Port1(Left)
                ## ##################################################################################################### M1 Rail Port1(Left):Gen Port1
            #Define Boundary_element
            self._DesignParameter['_M1RailPort1'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                  )

            #Define Boundary_element _YWidth
            tmp = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
            self._DesignParameter['_M1RailPort1']['_YWidth'] = abs( tmp[0][0][0][0]['_XY_down'][1] - tmp[-1][0][0][0]['_XY_up'][1] )

            #Define Boundary_element _XWidth
            self._DesignParameter['_M1RailPort1']['_XWidth'] = 1000

            #Define XYcoord.
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_M1RailPort1']['_XYCoordinates'] = [[0,0]]

                #Calculate
                    #Target_coord
                        #Target_coordx
                            #metalx distance DRC
            if self._DesignParameter['_M1RailPort1']['_YWidth'] > 3000:
                distance = 500
            elif self._DesignParameter['_M1RailPort1']['_YWidth'] > 1500 and self._DesignParameter['_M1RailPort1']['_YWidth'] < 3000:
                distance = 280
            else:
                distance = 210

            tmp1_1 = self.get_param_KJH3('_ViaM0M1_Vtc','_ViaM0M1','_Met1Layer')
            Target_coordx = tmp1_1[0][0][0][0]['_XY_left'][0] - distance
                        #Target_coordy
            tmp1_2 = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
            Target_coordy = tmp1_2[-1][0][0][0]['_XY_up'][1]

            target_coord = [Target_coordx,Target_coordy]
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_M1RailPort1')
            approaching_coord = tmp2[0][0]['_XY_up_right']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_M1RailPort1')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

                #Define
            self._DesignParameter['_M1RailPort1']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### M1 Rail Port1(Left):Connect Port1
            #Define Boundary_element
            self._DesignParameter['_M1ConnectPort1'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                          )

            #Define Boundary_element _YWidth
            tmp = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
            self._DesignParameter['_M1ConnectPort1']['_YWidth'] = tmp[0][0][0][0]['_Ywidth']

            #Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
            tmp2 = self.get_param_KJH3('_M1RailPort1')
            self._DesignParameter['_M1ConnectPort1']['_XWidth'] = abs( tmp1[(_NumofGates-1) * 2 + 1 ][0][0][0]['_XY_right'][0] - tmp2[0][0]['_XY_right'][0] )

            #Define XYcoord.
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_M1ConnectPort1']['_XYCoordinates'] = [[0,0]]

            for i in range(0,_NumofOD):
                    #Calculate 1
                        #Target_coord
                tmp1 = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
                target_coord = tmp1[ (_NumofGates*2)*i + (_NumofGates-1)*2  ][0][0][0]['_XY_up_right']

                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_M1ConnectPort1')
                approaching_coord = tmp2[0][0]['_XY_up_right']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_M1ConnectPort1')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

                    #Calculate 2
                        #Target_coord
                tmp1 = self.get_param_KJH3('_ViaM0M1_Hrz','_ViaM0M1','_Met1Layer')
                target_coord = tmp1[ (_NumofGates*2)*i + (_NumofGates-1)*2 + 1 ][0][0][0]['_XY_up_right']

                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_M1ConnectPort1')
                approaching_coord = tmp2[0][0]['_XY_up_right']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_M1ConnectPort1')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

                #Define
            self._DesignParameter['_M1ConnectPort1']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### M1 Rail Port2(Right)
                ## ##################################################################################################### M1 Rail Port2(Right):Gen Port2
            #Define Boundary_element
            self._DesignParameter['_M1RailPort2'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                  )

            #Define Boundary_element _YWidth
            tmp1 = self.get_param_KJH3('_M1Routing')
            self._DesignParameter['_M1RailPort2']['_YWidth'] = abs( tmp1[-1][0]['_XY_up'][1] - tmp1[0][0]['_XY_down'][1] )

            #Define Boundary_element _XWidth
            self._DesignParameter['_M1RailPort2']['_XWidth'] = 1000

            #Define XYcoord.
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_M1RailPort2']['_XYCoordinates'] = [[0,0]]

                #Calculate
                    #Target_coord
                        #Target_coordx
                            #Metalx distance DRC
            if self._DesignParameter['_M1RailPort2']['_YWidth'] > 3000:
                distance = 500
            elif self._DesignParameter['_M1RailPort2']['_YWidth'] > 1500 and self._DesignParameter['_M1RailPort2']['_YWidth'] < 3000:
                distance = 280
            else:
                distance = 210

            tmp1_1 = self.get_param_KJH3('_ViaM0M1_Vtc','_ViaM0M1','_Met1Layer')
            Target_coordx = tmp1_1[ _NumofGates * 2 - 1 ][0][0][0]['_XY_right'][0] + distance
                        #Target_coordy
            tmp1_2 = self.get_param_KJH3('_M1Routing')
            Target_coordy = tmp1_2[-1][0]['_XY_up'][1]

            target_coord = [Target_coordx,Target_coordy]
                    #Approaching_coord
            tmp2 = self.get_param_KJH3('_M1RailPort2')
            approaching_coord = tmp2[0][0]['_XY_up_left']
                    #Sref coord
            tmp3 = self.get_param_KJH3('_M1RailPort2')
            Scoord = tmp3[0][0]['_XY_cent']
                    #Cal
            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord)

                #Define
            self._DesignParameter['_M1RailPort2']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### M1 Rail Port2(Right):Connect Port2
            #Define Boundary_element
            self._DesignParameter['_M1ConnectPort2'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                          )

            #Define Boundary_element _YWidth
            tmp = self.get_param_KJH3('_M1Routing')
            self._DesignParameter['_M1ConnectPort2']['_YWidth'] = tmp[0][0]['_Ywidth']

            #Define Boundary_element _XWidth
            tmp1 = self.get_param_KJH3('_M1Routing')
            tmp2 = self.get_param_KJH3('_M1RailPort2')
            self._DesignParameter['_M1ConnectPort2']['_XWidth'] = abs( tmp2[0][0]['_XY_left'][0] - tmp1[0][0]['_XY_right'][0] )

            #Define XYcoord.
            #Calculate Sref XYcoord
            tmpXY=[]
                #initialized Sref coordinate
            self._DesignParameter['_M1ConnectPort2']['_XYCoordinates'] = [[0,0]]

            for i in range(0,_NumofOD):
                    #Calculate
                        #Target_coord
                tmp1 = self.get_param_KJH3('_M1Routing')
                target_coord = tmp1[i][0]['_XY_up_right']
                        #Approaching_coord
                tmp2 = self.get_param_KJH3('_M1ConnectPort2')
                approaching_coord = tmp2[0][0]['_XY_up_left']
                        #Sref coord
                tmp3 = self.get_param_KJH3('_M1ConnectPort2')
                Scoord = tmp3[0][0]['_XY_cent']
                        #Cal
                New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
                New_Scoord = np.round(New_Scoord,2)
                tmpXY.append(New_Scoord)

                #Define
            self._DesignParameter['_M1ConnectPort2']['_XYCoordinates'] = tmpXY


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A09_Ncap_KJH_85'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

#Ncap
_XWidth		=2000, 		## Poly Xwidthh
_YWidth		=1000,		## OD Ywidht
_NumofGates	=3,			## Column
_NumofOD	=10,			## Row

#M1 Routing: Connecting gates
_Routing_flag = True,

# Fixed Value
NumOfCOX=None,
NumOfCOY=None,
_ViaPoly2Met1NumberOfCOX=None,
_ViaPoly2Met1NumberOfCOY=1,

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
    LayoutObj = _Ncap_KJH(_DesignParameter=None, _Name=cellname)
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
