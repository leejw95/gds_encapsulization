from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A05_PbodyContactPhyLen_KJH

## ########################################################################################################################################################## Class_HEADER
class _PbodyRing_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(
_XlengthIntn		= None,
_YlengthIntn		= None,
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeft		= None,
_NumContRight		= None,

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
_XlengthIntn		= None,
_YlengthIntn		= None,
_NumContTop			= None,
_NumContBottom		= None,
_NumContLeft		= None,
_NumContRight		= None,
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

            ## ################################################################################################################### Pbody:Top
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContTop
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['_PbodyTop'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_PbodyTop'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_PbodyTop']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_PbodyTop']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_PbodyTop']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_PbodyTop']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Pbody:Bottom
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContBottom
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['_PbodyBottom'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_PbodyBottom'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_PbodyBottom']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_PbodyBottom']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_PbodyBottom']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_PbodyBottom']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_PbodyBottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                #Sref coord
        tmp3 = self.get_param_KJH3('_PbodyBottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord[1] = New_Scoord[1] - _YlengthIntn
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_PbodyBottom']['_XYCoordinates'] = tmpXY


            ## ################################################################################################################### Pbody:Left
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContLeft
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['_PbodyLeft'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_PbodyLeft'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_PbodyLeft']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_PbodyLeft']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_PbodyLeft']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_PbodyLeft']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_PbodyLeft']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_PbodyLeft')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_PbodyLeft']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Pbody:Right
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContRight
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['_PbodyRight'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContactPhyLen_KJH._PbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_PbodyRight'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_PbodyRight']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_PbodyRight']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_PbodyRight']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_PbodyRight']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_PbodyRight']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_PbodyRight')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_PbodyRight']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Extension:Top
                ## ##################################################################################################### Extension:Top:OD
        #Define Boundary_element
        self._DesignParameter['_ExtenODLayer_Top'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_ODLayer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenODLayer_Top']['_XYCoordinates'] = tmpXY


                ## ##################################################################################################### Extension:Top:M1
        #Define Boundary_element
        self._DesignParameter['_ExtenMet1Layer_Top'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Top:PP
        #Define Boundary_element
        self._DesignParameter['_ExtenPPLayer_Top'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenPPLayer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenPPLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenPPLayer_Top')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenPPLayer_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmp4 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_PPLayer')
        New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenPPLayer_Top']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Extension:Bottom
                ## ##################################################################################################### Extension:Bottom:OD
        #Define Boundary_element
        self._DesignParameter['_ExtenODLayer_Bottom'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                            _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_ODLayer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenODLayer_Bottom']['_XYCoordinates'] = tmpXY
                ## ##################################################################################################### Extension:Bottom:M1
        #Define Boundary_element
        self._DesignParameter['_ExtenMet1Layer_Bottom'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Bottom:PP
        #Define Boundary_element
        self._DesignParameter['_ExtenPPLayer_Bottom'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenPPLayer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenPPLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenPPLayer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenPPLayer_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmp4 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_PPLayer')
        New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenPPLayer_Bottom']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Extension:Left
                ## ##################################################################################################### Extension:Left:OD
        #Define Boundary_element
        self._DesignParameter['_ExtenODLayer_Left'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_ODLayer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenODLayer_Left']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Left:M1
        #Define Boundary_element
        self._DesignParameter['_ExtenMet1Layer_Left'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Left:PP
        #Define Boundary_element
        self._DesignParameter['_ExtenPPLayer_Left'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_PPLayer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenPPLayer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenPPLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_ExtenPPLayer_Top')
        target_coord = tmp1_1[0][0]['_XY_up_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenPPLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenPPLayer_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenPPLayer_Left']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Extension:Right
                ## ##################################################################################################### Extension:Right:OD
        #Define Boundary_element
        self._DesignParameter['_ExtenODLayer_Right'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_ODLayer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenODLayer_Right']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Right:M1
        #Define Boundary_element
        self._DesignParameter['_ExtenMet1Layer_Right'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyRight','_PbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = tmpXY
                ## ##################################################################################################### Extension:Right:PP
        #Define Boundary_element
        self._DesignParameter['_ExtenPPLayer_Right'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['PIMP'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['PIMP'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_PbodyTop','_PbodyContactPhyLen','_PPLayer')
        tmp2 = self.get_param_KJH3('_PbodyBottom','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_PbodyLeft','_PbodyContactPhyLen','_PPLayer')
        self._DesignParameter['_ExtenPPLayer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenPPLayer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenPPLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_ExtenPPLayer_Top')
        target_coord = tmp1_1[0][0]['_XY_up_right']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenPPLayer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenPPLayer_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenPPLayer_Right']['_XYCoordinates'] = tmpXY

        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A07_PbodyRing_KJH_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_XlengthIntn		= 4500,
_YlengthIntn		= 8000,
_NumContTop			= 2,
_NumContBottom		= 3,
_NumContLeft		= 4,
_NumContRight		= 5,


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
    LayoutObj = _PbodyRing_KJH(_DesignParameter=None, _Name=cellname)
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




