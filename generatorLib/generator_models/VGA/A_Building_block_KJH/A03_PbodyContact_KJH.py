from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

## ########################################################################################################################################################## Class_HEADER
class _PbodyContact_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_NumberOfPbodyCOX	= None,
_NumberOfPbodyCOY	= None,

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

_NumberOfPbodyCOX	= None,
_NumberOfPbodyCOY	= None,

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
        _XYCoordinateOfPbodyContact = [[0,0]]

            ## ################################################################################################################### DIFF(OD/RX)_Layer
        #Define Boundary_element
        self._DesignParameter['_ODLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Calculate _LengthNbodyBtwCO for Ywidth and Xwidth
        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX,NumOfCOY=_NumberOfPbodyCOY )

        #Define Boundary_element _YWidth
        self._DesignParameter['_ODLayer']['_YWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOY - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define Boundary_element _XWidth
        self._DesignParameter['_ODLayer']['_XWidth'] = _DRCObj._CoMinWidth + (_NumberOfPbodyCOX - 1) * _LengthPbodyBtwCO + 2 * _DRCObj._CoMinEnclosureByODAtLeastTwoSide

        #Define XYcoord.
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfPbodyContact

            ## ################################################################################################################### PIMP_Layer
        #Define Boundary_element
        self._DesignParameter['_PPLayer'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth		
        self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

        if self._DesignParameter['_PPLayer']['_YWidth'] < 170:
            self._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
        
        #Define Boundary_element _XWidth
        self._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2

        #Define XYcoord.
        self._DesignParameter['_PPLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer']['_XYCoordinates']

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
        _LengthPbodyBtwCO = _DRCObj._CoMinWidth + _DRCObj.DRCCOMinSpace(NumOfCOX=_NumberOfPbodyCOX,NumOfCOY=_NumberOfPbodyCOY )

            #Cal Coord.
        tmp=[]

        for i in range(0, _NumberOfPbodyCOX):
            for j in range(0, _NumberOfPbodyCOY):

                if (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX // 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY // 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]
                elif (_NumberOfPbodyCOX % 2) == 0 and (_NumberOfPbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX // 2 - 0.5) * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY-1)//2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 1 and (_NumberOfPbodyCOY % 2)==0:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX -1) // 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY // 2 - 0.5) * _LengthPbodyBtwCO + j * _LengthPbodyBtwCO]

                elif (_NumberOfPbodyCOX % 2) == 1 and (_NumberOfPbodyCOY % 2)==1:
                    _xycoordinatetmp = [_XYCoordinateOfPbodyContact[0][0] - (_NumberOfPbodyCOX -1) // 2  * _LengthPbodyBtwCO + i * _LengthPbodyBtwCO,
                                        _XYCoordinateOfPbodyContact[0][1] - (_NumberOfPbodyCOY-1)//2*_LengthPbodyBtwCO +j*_LengthPbodyBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp







        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A03_PbodyContact_KJH_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_NumberOfPbodyCOX=30,
_NumberOfPbodyCOY=2,


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
    LayoutObj = _PbodyContact_KJH(_DesignParameter=None, _Name=cellname)
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




