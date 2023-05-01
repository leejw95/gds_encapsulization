from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A04_NbodyContact


import numpy as np
import copy
import math


############################################################################################################################################################ Class_HEADER
class _Nsubring(StickDiagram_KJH0._StickDiagram_KJH):

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    #Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                                _Xwidth = 600,
                                                _Ywidth = 2320,

                                                _Guardring_left_NbodyContCount_of_Width = 2,
                                                _Guardring_right_NbodyContCount_of_Width = 2,
                                                _Guardring_up_NbodyContCount_of_Width = 2,
                                                _Guardring_down_NbodyContCount_of_Width = 2,
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

                                            _Xwidth = 600,
                                            _Ywidth = 2320,

                                            _Guardring_left_NbodyContCount_of_Width = 2,
                                            _Guardring_right_NbodyContCount_of_Width = 2,
                                            _Guardring_up_NbodyContCount_of_Width = 2,
                                            _Guardring_down_NbodyContCount_of_Width = 2,

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

############################################################################################################################################################ Guardring(Nbody_contact)
        print('##     Guardring(Nbody_contact)    ##')

        #Pre-defined
        _M1_to_PP = 100


################################################################################################################################################## Guardring(Nbody_contact):left
        print('##     Guardring(Nbody_contact):left    ##')

        _Guardring_left_NbodyCont_Length = _Ywidth

        #Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
        #Vertical
        _NbodyContact_NumberOfNbodyCOX = _Guardring_left_NbodyContCount_of_Width
        _NbodyContact_NumberOfNbodyCOY = (int(((_Guardring_left_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Guardring_left_NbodyContCount_of_Width) + 0
        _NbodyContact_Met1XWidth       = None
        _NbodyContact_Met1YWidth       = None

        #Define _NbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
        _Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

        #Define _NbodyContact Sref
        self._DesignParameter['_Guardring_left_NbodyContact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Guardring_left_NbodyContact'.format(_Name) ))[0]

        #Define _NbodyContact Sref Relection
        self._DesignParameter['_Guardring_left_NbodyContact']['_Reflect'] = [0, 0, 0]

        #Define _NbodyContact Sref Angle
        self._DesignParameter['_Guardring_left_NbodyContact']['_Angle'] = 0

        #Define _NbodyContact layer
        self._DesignParameter['_Guardring_left_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

        #Define _NbodyContact coordinate
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_left_NbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Pmos_SW','_PPLayer')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Guardring_left_NbodyContact')

        target_coord        = tmp1[0]['_XY_left']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            #Distancing
        New_Scoord[0] = New_Scoord[0] - _M1_to_PP
        self._DesignParameter['_Guardring_left_NbodyContact']['_XYCoordinates'] = [New_Scoord]


        #Define NWELL of _NbodyContact
        self._DesignParameter['_Guardring_left_NbodyContact_Nwell'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                          )

        #Define NWELL Xwidth
        self._DesignParameter['_Guardring_left_NbodyContact_Nwell']['_XWidth'] = self.getXWidth('_Guardring_left_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Ywidth
        self._DesignParameter['_Guardring_left_NbodyContact_Nwell']['_YWidth'] = self.getYWidth('_Guardring_left_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Coordinates
        self._DesignParameter['_Guardring_left_NbodyContact_Nwell']['_XYCoordinates'] =  self.getXY('_Guardring_left_NbodyContact')

################################################################################################################################################## Guardring(Nbody_contact):right
        print('##     Guardring(Nbody_contact):right    ##')

        _Guardring_right_NbodyCont_Length = _Ywidth

        #Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
        #Vertical
        _NbodyContact_NumberOfNbodyCOX = _Guardring_right_NbodyContCount_of_Width
        _NbodyContact_NumberOfNbodyCOY = (int(((_Guardring_right_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Guardring_right_NbodyContCount_of_Width) + 0
        _NbodyContact_Met1XWidth       = None
        _NbodyContact_Met1YWidth       = None

        #Define _NbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
        _Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

        #Define _NbodyContact Sref
        self._DesignParameter['_Guardring_right_NbodyContact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Guardring_right_NbodyContact'.format(_Name) ))[0]

        #Define _NbodyContact Sref Relection
        self._DesignParameter['_Guardring_right_NbodyContact']['_Reflect'] = [0, 0, 0]

        #Define _NbodyContact Sref Angle
        self._DesignParameter['_Guardring_right_NbodyContact']['_Angle'] = 0

        #Define _NbodyContact layer
        self._DesignParameter['_Guardring_right_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

        #Define _NbodyContact coordinate
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_right_NbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Pmos_SW','_PPLayer')
        tmp2 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Guardring_right_NbodyContact')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            #Distancing
        New_Scoord[0] = New_Scoord[0] + _M1_to_PP
        self._DesignParameter['_Guardring_right_NbodyContact']['_XYCoordinates'] = [New_Scoord]


        #Define NWELL of _NbodyContact
        self._DesignParameter['_Guardring_right_NbodyContact_Nwell'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                          )

        #Define NWELL Xwidth
        self._DesignParameter['_Guardring_right_NbodyContact_Nwell']['_XWidth'] = self.getXWidth('_Guardring_right_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Ywidth
        self._DesignParameter['_Guardring_right_NbodyContact_Nwell']['_YWidth'] = self.getYWidth('_Guardring_right_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Coordinates
        self._DesignParameter['_Guardring_right_NbodyContact_Nwell']['_XYCoordinates'] =  self.getXY('_Guardring_right_NbodyContact')

################################################################################################################################################## Guardring(Nbody_contact):up
        print('##     Guardring(Nbody_contact):up    ##')

        _Guardring_up_NbodyCont_Length = _Xwidth

        #Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
        #Vertical
        _NbodyContact_NumberOfNbodyCOY = _Guardring_up_NbodyContCount_of_Width
        _NbodyContact_NumberOfNbodyCOX = (int(((_Guardring_up_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Guardring_up_NbodyContCount_of_Width) + 0
        _NbodyContact_Met1XWidth       = None
        _NbodyContact_Met1YWidth       = None

        #Define _NbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
        _Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

        #Define _NbodyContact Sref
        self._DesignParameter['_Guardring_up_NbodyContact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Guardring_up_NbodyContact'.format(_Name) ))[0]

        #Define _NbodyContact Sref Relection
        self._DesignParameter['_Guardring_up_NbodyContact']['_Reflect'] = [0, 0, 0]

        #Define _NbodyContact Sref Angle
        self._DesignParameter['_Guardring_up_NbodyContact']['_Angle'] = 0

        #Define _NbodyContact layer
        self._DesignParameter['_Guardring_up_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

        #Define _NbodyContact coordinate
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_up_NbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Pmos_SW','_PPLayer')
        tmp2 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Guardring_up_NbodyContact')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_down']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            #Distancing
        New_Scoord[1] = New_Scoord[1] + _M1_to_PP
        self._DesignParameter['_Guardring_up_NbodyContact']['_XYCoordinates'] = [New_Scoord]


        #Define NWELL of _NbodyContact
        self._DesignParameter['_Guardring_up_NbodyContact_Nwell'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                          )

        #Define NWELL Xwidth
        self._DesignParameter['_Guardring_up_NbodyContact_Nwell']['_XWidth'] = self.getXWidth('_Guardring_up_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Ywidth
        self._DesignParameter['_Guardring_up_NbodyContact_Nwell']['_YWidth'] = self.getYWidth('_Guardring_up_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Coordinates
        self._DesignParameter['_Guardring_up_NbodyContact_Nwell']['_XYCoordinates'] =  self.getXY('_Guardring_up_NbodyContact')

################################################################################################################################################## Guardring(Nbody_contact):down
        print('##     Guardring(Nbody_contact):up    ##')

        _Guardring_down_NbodyCont_Length = _Xwidth

        #Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
        #Vertical
        _NbodyContact_NumberOfNbodyCOY = _Guardring_down_NbodyContCount_of_Width
        _NbodyContact_NumberOfNbodyCOX = (int(((_Guardring_down_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Guardring_down_NbodyContCount_of_Width) + 0
        _NbodyContact_Met1XWidth       = None
        _NbodyContact_Met1YWidth       = None

        #Define _NbodyContact input parameter
        _Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
        _Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
        _Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
        _Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

        #Define _NbodyContact Sref
        self._DesignParameter['_Guardring_down_NbodyContact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Guardring_down_NbodyContact'.format(_Name) ))[0]

        #Define _NbodyContact Sref Relection
        self._DesignParameter['_Guardring_down_NbodyContact']['_Reflect'] = [0, 0, 0]

        #Define _NbodyContact Sref Angle
        self._DesignParameter['_Guardring_down_NbodyContact']['_Angle'] = 0

        #Define _NbodyContact layer
        self._DesignParameter['_Guardring_down_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

        #Define _NbodyContact coordinate
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_down_NbodyContact']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Pmos_SW','_PPLayer')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact','_Met1Layer')
        tmp3 = self.get_param_KJH2('_Guardring_down_NbodyContact')

        target_coord        = tmp1[0]['_XY_down']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

            #Distancing
        New_Scoord[1] = New_Scoord[1] - _M1_to_PP
        self._DesignParameter['_Guardring_down_NbodyContact']['_XYCoordinates'] = [New_Scoord]


        #Define NWELL of _NbodyContact
        self._DesignParameter['_Guardring_down_NbodyContact_Nwell'] = self._BoundaryElementDeclaration(
                                                                                                            _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                            _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                            _XWidth=None,
                                                                                                            _YWidth=None,
                                                                                                            _XYCoordinates=[ ],
                                                                                                          )

        #Define NWELL Xwidth
        self._DesignParameter['_Guardring_down_NbodyContact_Nwell']['_XWidth'] = self.getXWidth('_Guardring_down_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Ywidth
        self._DesignParameter['_Guardring_down_NbodyContact_Nwell']['_YWidth'] = self.getYWidth('_Guardring_down_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

        #Define NWELL Coordinates
        self._DesignParameter['_Guardring_down_NbodyContact_Nwell']['_XYCoordinates'] =  self.getXY('_Guardring_down_NbodyContact')

################################################################################################################################################## Guardring(Nbody_contact):OD_covering
        print('##     Guardring(Nbody_contact):OD_covering    ##')
######################################################################################################################################## Guardring(Nbody_contact):OD_covering:left
        print('##     Guardring(Nbody_contact):OD_covering:left    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_OD_covering_left'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact','_ODLayer')

        self._DesignParameter['_Guardring_OD_covering_left']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_left_NbodyContact','_ODLayer')
        self._DesignParameter['_Guardring_OD_covering_left']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_OD_covering_left']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_left')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_left_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_left')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_OD_covering_left']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):OD_covering:right
        print('##     Guardring(Nbody_contact):OD_covering:right    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_OD_covering_right'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact','_ODLayer')

        self._DesignParameter['_Guardring_OD_covering_right']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        self._DesignParameter['_Guardring_OD_covering_right']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_OD_covering_right']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_right')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_right')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_OD_covering_right']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]


######################################################################################################################################## Guardring(Nbody_contact):OD_covering:up
        print('##     Guardring(Nbody_contact):OD_covering:up    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_OD_covering_up'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact','_ODLayer')

        self._DesignParameter['_Guardring_OD_covering_up']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        self._DesignParameter['_Guardring_OD_covering_up']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_OD_covering_up']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_up')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_up')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_OD_covering_up']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):OD_covering:down
        print('##     Guardring(Nbody_contact):OD_covering:down    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_OD_covering_down'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact','_ODLayer')

        self._DesignParameter['_Guardring_OD_covering_down']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_down_NbodyContact','_ODLayer')
        self._DesignParameter['_Guardring_OD_covering_down']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_OD_covering_down']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_down_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_down')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_ODLayer')
        tmp2 = self.get_param_KJH2('_Guardring_OD_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_OD_covering_down')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_OD_covering_down']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



################################################################################################################################################## Guardring(Nbody_contact):M1Covering
        print('##     Guardring(Nbody_contact):M1Covering    ##')
######################################################################################################################################## Guardring(Nbody_contact):M1Covering:left
        print('##     Guardring(Nbody_contact):M1Covering:left    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_M1_covering_left'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact','_Met1Layer')

        self._DesignParameter['_Guardring_M1_covering_left']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_left_NbodyContact','_Met1Layer')
        self._DesignParameter['_Guardring_M1_covering_left']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_M1_covering_left']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_left')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_left_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_left')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_M1_covering_left']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):M1_covering:right
        print('##     Guardring(Nbody_contact):M1_covering:right    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_M1_covering_right'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact','_Met1Layer')

        self._DesignParameter['_Guardring_M1_covering_right']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        self._DesignParameter['_Guardring_M1_covering_right']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_M1_covering_right']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_right')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_right')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_M1_covering_right']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]


######################################################################################################################################## Guardring(Nbody_contact):M1_covering:up
        print('##     Guardring(Nbody_contact):M1_covering:up    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_M1_covering_up'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact','_Met1Layer')

        self._DesignParameter['_Guardring_M1_covering_up']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        self._DesignParameter['_Guardring_M1_covering_up']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_M1_covering_up']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_up')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_up')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_M1_covering_up']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):M1_covering:down
        print('##     Guardring(Nbody_contact):M1_covering:down    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_M1_covering_down'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact','_Met1Layer')

        self._DesignParameter['_Guardring_M1_covering_down']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_down_NbodyContact','_Met1Layer')
        self._DesignParameter['_Guardring_M1_covering_down']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_M1_covering_down']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_down_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_down')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Guardring_M1_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_M1_covering_down')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_M1_covering_down']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]


################################################################################################################################################## Guardring(Nbody_contact):NWELLCovering
        print('##     Guardring(Nbody_contact):NWELLCovering    ##')
######################################################################################################################################## Guardring(Nbody_contact):NWELLCovering:left
        print('##     Guardring(Nbody_contact):NWELLCovering:left    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_NWELL_covering_left'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact_Nwell')

        self._DesignParameter['_Guardring_NWELL_covering_left']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_left_NbodyContact_Nwell')
        self._DesignParameter['_Guardring_NWELL_covering_left']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_NWELL_covering_left']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_left')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_left_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_left')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_left')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_NWELL_covering_left']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):M1_covering:right
        print('##     Guardring(Nbody_contact):M1_covering:right    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_NWELL_covering_right'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_down_NbodyContact_Nwell')

        self._DesignParameter['_Guardring_NWELL_covering_right']['_YWidth'] = abs(tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1])

        #Define Boundary_element _XWidth
        tmp3 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        self._DesignParameter['_Guardring_NWELL_covering_right']['_XWidth'] = tmp3[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_NWELL_covering_right']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_right')

        target_coord        = tmp1[0]['_XY_up']
        approaching_coord   = tmp2[0]['_XY_up']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_right')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_right')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_NWELL_covering_right']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]


######################################################################################################################################## Guardring(Nbody_contact):M1_covering:up
        print('##     Guardring(Nbody_contact):M1_covering:up    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_NWELL_covering_up'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact_Nwell')

        self._DesignParameter['_Guardring_NWELL_covering_up']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        self._DesignParameter['_Guardring_NWELL_covering_up']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_NWELL_covering_up']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_up_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_up')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_up')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_up')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_NWELL_covering_up']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]



######################################################################################################################################## Guardring(Nbody_contact):M1_covering:down
        print('##     Guardring(Nbody_contact):M1_covering:down    ##')

        #Define Boundary_element
        self._DesignParameter['_Guardring_NWELL_covering_down'] = self._BoundaryElementDeclaration(
                                                                                                _Layer=DesignParameters._LayerMapping['NWELL'][0],
                                                                                                _Datatype=DesignParameters._LayerMapping['NWELL'][1],
                                                                                                _XWidth=None,
                                                                                                _YWidth=None,
                                                                                                _XYCoordinates=[ ],
                                                                                               )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_left_NbodyContact_Nwell')

        self._DesignParameter['_Guardring_NWELL_covering_down']['_XWidth'] = abs(tmp1[0]['_XY_right'][0] - tmp2[0]['_XY_left'][0])

        #Define Boundary_element _YWidth
        tmp3 = self.get_param_KJH2('_Guardring_down_NbodyContact_Nwell')
        self._DesignParameter['_Guardring_NWELL_covering_down']['_YWidth'] = tmp3[0]['_Ywidth']

        #Define Boundary_element _XYCoordinates
        #Calculate Sref Ycoord
            #initialized Sref coordinate
        self._DesignParameter['_Guardring_NWELL_covering_down']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_down_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_down')

        target_coord        = tmp1[0]['_XY_cent']
        approaching_coord   = tmp2[0]['_XY_cent']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord1 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        #Calculate Sref Xcoord
            #Calculation
        tmp1 = self.get_param_KJH2('_Guardring_right_NbodyContact_Nwell')
        tmp2 = self.get_param_KJH2('_Guardring_NWELL_covering_down')
        tmp3 = self.get_param_KJH2('_Guardring_NWELL_covering_down')

        target_coord        = tmp1[0]['_XY_right']
        approaching_coord   = tmp2[0]['_XY_right']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord2 = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

        self._DesignParameter['_Guardring_NWELL_covering_down']['_XYCoordinates'] = [[New_Scoord2[0],New_Scoord1[1]]]









############################################################################################################################################################ CALCULATION END
        print ('#########################################################################################################')
        print ('                                      Calculation   END                                                  ')
        print ('#########################################################################################################')











############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A01_NSubRing_v2_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

                            _Xwidth = 600,
                            _Ywidth = 2320,


                            _Guardring_left_NbodyContCount_of_Width = 3,
                            _Guardring_right_NbodyContCount_of_Width = 4,
                            _Guardring_up_NbodyContCount_of_Width = 5,
                            _Guardring_down_NbodyContCount_of_Width = 2,

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
    LayoutObj = _Nsubring(_DesignParameter=None, _Name=cellname)
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
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------






















