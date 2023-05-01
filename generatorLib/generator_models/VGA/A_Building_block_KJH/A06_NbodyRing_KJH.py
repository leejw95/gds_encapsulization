from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A04_NbodyContactPhyLen_KJH

## ########################################################################################################################################################## Class_HEADER
class _NbodyRing_KJH(StickDiagram_KJH1._StickDiagram_KJH):

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

            ## ################################################################################################################### Nbody:Top
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContTop
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['_NbodyTop'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_NbodyTop'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_NbodyTop']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_NbodyTop']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_NbodyTop']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_NbodyTop']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Nbody:Bottom
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _XlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContBottom
        _Caculation_Parameters['_Vtc_flag']  	=  False

        #Generate Sref
        self._DesignParameter['_NbodyBottom'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_NbodyBottom'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_NbodyBottom']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_NbodyBottom']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_NbodyBottom']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_NbodyBottom']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_NbodyBottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up']
                #Sref coord
        tmp3 = self.get_param_KJH3('_NbodyBottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[1] = New_Scoord[1] - _YlengthIntn
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_NbodyBottom']['_XYCoordinates'] = tmpXY

        
            ## ################################################################################################################### Nbody:Left
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContLeft
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['_NbodyLeft'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_NbodyLeft'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_NbodyLeft']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_NbodyLeft']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_NbodyLeft']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_NbodyLeft']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_NbodyLeft']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_NbodyLeft')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_NbodyLeft']['_XYCoordinates'] = tmpXY

            ## ################################################################################################################### Nbody:Right
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy( A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_Length']  		=  _YlengthIntn
        _Caculation_Parameters['_NumCont']  	=  _NumContRight
        _Caculation_Parameters['_Vtc_flag']  	=  True

        #Generate Sref
        self._DesignParameter['_NbodyRight'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContactPhyLen_KJH._NbodyContactPhyLen_KJH( _DesignParameter=None, _Name='{}:_NbodyRight'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_NbodyRight']['_Reflect'] = [0, 0, 0] 
        
        #Define Sref Angle
        self._DesignParameter['_NbodyRight']['_Angle'] = 0 

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_NbodyRight']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_NbodyRight']['_XYCoordinates']=[[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_NbodyRight']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Met1Layer')
        approaching_coord = tmp2[0][0][0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_NbodyRight')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_NbodyRight']['_XYCoordinates'] = tmpXY
        
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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_ODLayer')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Top')
        approaching_coord = tmp2[0][0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Top']['_XYCoordinates'] = tmpXY
                ## ##################################################################################################### Extension:Top:NW
        #Define Boundary_element
        self._DesignParameter['_ExtenNwell_Top'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Top']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Top']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenNwell_Top']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenNwell_Top']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenNwell_Top')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenNwell_Top')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmp4 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Nwell')
        New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenNwell_Top']['_XYCoordinates'] = tmpXY
        
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
        tmp1 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_ODLayer')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

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
        tmp1 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Bottom')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Bottom']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Bottom:NW
        #Define Boundary_element
        self._DesignParameter['_ExtenNwell_Bottom'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Bottom']['_YWidth'] = tmp1[0][0][0][0]['_Ywidth']

        #Define Boundary_element _XWidth
        tmp2 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Bottom']['_XWidth'] = abs( tmp3[0][0][0][0]['_XY_right'][0] - tmp2[0][0][0][0]['_XY_left'][0] ) 

        #Define XYcoord.
        self._DesignParameter['_ExtenNwell_Bottom']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenNwell_Bottom']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        target_coord = tmp1_1[0][0][0][0]['_XY_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenNwell_Bottom')
        approaching_coord = tmp2[0][0]['_XY_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenNwell_Bottom')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmp4 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Nwell')
        New_Scoord[1] = tmp4[0][0][0][0]['_XY_cent'][1]
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenNwell_Bottom']['_XYCoordinates'] = tmpXY
        
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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_ODLayer')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Left')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Left']['_XYCoordinates'] = tmpXY

                ## ##################################################################################################### Extension:Left:NW
        #Define Boundary_element
        self._DesignParameter['_ExtenNwell_Left'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Nwell')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Left']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Left']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenNwell_Left']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenNwell_Left']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_ExtenNwell_Top')
        target_coord = tmp1_1[0][0]['_XY_up_left']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenNwell_Left')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenNwell_Left')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenNwell_Left']['_XYCoordinates'] = tmpXY
        
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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_ODLayer')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_ODLayer')
        self._DesignParameter['_ExtenODLayer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenODLayer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenODLayer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenODLayer_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

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
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyRight','_NbodyContactPhyLen','_Met1Layer')
        self._DesignParameter['_ExtenMet1Layer_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Met1Layer')
        target_coord = tmp1[0][0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenMet1Layer_Right')
        approaching_coord = tmp2[0][0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenMet1Layer_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenMet1Layer_Right']['_XYCoordinates'] = tmpXY
                ## ##################################################################################################### Extension:Right:NW
        #Define Boundary_element
        self._DesignParameter['_ExtenNwell_Right'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH3('_NbodyTop','_NbodyContactPhyLen','_Nwell')
        tmp2 = self.get_param_KJH3('_NbodyBottom','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Right']['_YWidth'] = abs( tmp1[0][0][0][0]['_XY_up'][1] - tmp2[0][0][0][0]['_XY_down'][1] ) 

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH3('_NbodyLeft','_NbodyContactPhyLen','_Nwell')
        self._DesignParameter['_ExtenNwell_Right']['_XWidth'] = tmp3[0][0][0][0]['_Xwidth']

        #Define XYcoord.
        self._DesignParameter['_ExtenNwell_Right']['_XYCoordinates'] = [[0,0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ExtenNwell_Right']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH3('_ExtenNwell_Top')
        target_coord = tmp1_1[0][0]['_XY_up_right']

                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ExtenNwell_Right')
        approaching_coord = tmp2[0][0]['_XY_up_right']
                #Sref coord
        tmp3 = self.get_param_KJH3('_ExtenNwell_Right')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ExtenNwell_Right']['_XYCoordinates'] = tmpXY
        
        
        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')



## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A06_NbodyRing_KJH_89'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_XlengthIntn		= 4534,
_YlengthIntn		= 2119,
_NumContTop			= 2,
_NumContBottom		= 2,
_NumContLeft		= 2,
_NumContRight		= 2,


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
    LayoutObj = _NbodyRing_KJH(_DesignParameter=None, _Name=cellname)
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




