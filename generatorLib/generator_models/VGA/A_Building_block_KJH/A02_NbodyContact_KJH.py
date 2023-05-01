from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

## ########################################################################################################################################################## Class_HEADER
class _NbodyContact_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_NumberOfNbodyCOX	= None,
_NumberOfNbodyCOY	= None,

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

_NumberOfNbodyCOX	= None,
_NumberOfNbodyCOY	= None,

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

            ## ################################################################################################################### Pre-define Parameters
        _XYCoordinateOfNbodyContact = [[0,0]]

            ## ################################################################################################################### DIFF(OD/RX)_Dummy_Layer
        #Define Boundary_element
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Calculate _LengthNbodyBtwCO for Ywidth and Xwidth
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfNbodyCOX,NumOfCOY=_NumberOfNbodyCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOY - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define Boundary_element _XWidth
        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfNbodyCOX - 1) * _LengthNbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define XYcoord.
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNbodyContact

            ## ################################################################################################################### METAL1_Layer
        #Define Boundary_element
        self._DesignParameter['_Met1Layer'] = self._BoundaryElementDeclaration(
                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                _XWidth=None,
                                                                                _YWidth=None,
                                                                                _XYCoordinates=[ ],
                                                                               )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']

        #Define Boundary_element _XWidth
        self._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']

        #Define XYcoord.
        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

            ## ################################################################################################################### CONT_Layer
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

        #Define XYcoord.
            #Define Distance between CONT
        _LengthNbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfNbodyCOX,NumOfCOY=_NumberOfNbodyCOY )

            #Cal Coord.
        tmp=[]

        for i in range(0, _NumberOfNbodyCOX):
            for j in range(0, _NumberOfNbodyCOY):

                if (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]
                elif (_NumberOfNbodyCOX % 2) == 0 and (_NumberOfNbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX / 2 - 0.5) * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY-1)/2*_LengthNbodyBtwCO +j*_LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 1 and (_NumberOfNbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX -1) / 2  * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY / 2 - 0.5) * _LengthNbodyBtwCO + j * _LengthNbodyBtwCO]

                elif (_NumberOfNbodyCOX % 2) == 1 and (_NumberOfNbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfNbodyContact[0][0] - (_NumberOfNbodyCOX -1) / 2  * _LengthNbodyBtwCO + i * _LengthNbodyBtwCO,
                                        _XYCoordinateOfNbodyContact[0][1] - (_NumberOfNbodyCOY-1)/2*_LengthNbodyBtwCO +j*_LengthNbodyBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

            ## ################################################################################################################### Nwell_Layer
        #Define NWELL of _NbodyContact
        self._DesignParameter['_Nwell'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                          )

        #Define NWELL Xwidth
        self._DesignParameter['_Nwell']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + _DRCObj._PpMinExtensiononPactive*2

        #Define NWELL Ywidth
        self._DesignParameter['_Nwell']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + _DRCObj._PpMinExtensiononPactive*2

        #Define NWELL Coordinates
        self._DesignParameter['_Nwell']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']


        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A02_NbodyContact_KJH_97'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_NumberOfNbodyCOX=15,
_NumberOfNbodyCOY=8,

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
    LayoutObj = _NbodyContact_KJH(_DesignParameter=None, _Name=cellname)
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




