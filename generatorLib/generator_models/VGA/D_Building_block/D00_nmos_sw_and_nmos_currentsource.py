'''


'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
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

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D00_nmos_sw_and_nmos_currentsource
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D01_guardring_gen_v2
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D02_unit
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D03_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.D_Building_block import D04_routing

############################################################################################################################################################ Class_HEADER
class _nmos_sw_and_nmos_currentsource(StickDiagram_KJH0._StickDiagram_KJH):
    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
    # Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

                                            #Current source nmos
                                            _Cs_NMOSNumberofGate=20,
                                            _Cs_NMOSChannelWidth=1000,
                                            _Cs_NMOSChannellength=30,
                                            _Cs_NMOSDummy=True,
                                            _Cs_GateSpacing=None,
                                            _Cs_SDWidth=None,
                                            _Cs_XVT='SLVT',
                                            _Cs_PCCrit=None,


                                            #SW nmos
                                            _Sw_NMOSNumberofGate=20,
                                            _Sw_NMOSChannelWidth=1000,
                                            _Sw_NMOSChannellength=30,
                                            _Sw_NMOSDummy=True,
                                            _Sw_GateSpacing=None,
                                            _Sw_SDWidth=None,
                                            _Sw_XVT='SLVT',
                                            _Sw_PCCrit=None,


                                            )

    # Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                _Name=self._NameDeclaration(_Name=_Name),
                _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
            )

    ################################################################################################################################################## _CalculateDesignParameter
    def _CalculateDesignParameter(self,

                                            #Current source nmos
                                            _Cs_NMOSNumberofGate=20,
                                            _Cs_NMOSChannelWidth=1000,
                                            _Cs_NMOSChannellength=30,
                                            _Cs_NMOSDummy=True,
                                            _Cs_GateSpacing=None,
                                            _Cs_SDWidth=None,
                                            _Cs_XVT='SLVT',
                                            _Cs_PCCrit=None,


                                            #SW nmos
                                            _Sw_NMOSNumberofGate=20,
                                            _Sw_NMOSChannelWidth=1000,
                                            _Sw_NMOSChannellength=30,
                                            _Sw_NMOSDummy=True,
                                            _Sw_GateSpacing=None,
                                            _Sw_SDWidth=None,
                                            _Sw_XVT='SLVT',
                                            _Sw_PCCrit=None,

                                  ):

        #################################################################################################################################### Class_HEADER: Pre Defined Parameter Before Calculation
        print('##     Pre Defined Parameter Before Calculation    ##')
        # Load DRC library
        _DRCobj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']

        ################################################################################################################################### Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

        ######################################################################################################################### NMOS_Currnet_source:Sref gen
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A00_NMOSWithDummy_v3._NMOS._ParametersForDesignCalculation)
        _Caculation_Parameters['_NMOSNumberofGate']  	= _Cs_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']  	= _Cs_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] 	= _Cs_NMOSChannellength
        _Caculation_Parameters['_NMOSDummy']  			= _Cs_NMOSDummy
        _Caculation_Parameters['_GateSpacing']  		= _Cs_GateSpacing
        _Caculation_Parameters['_SDWidth']  			= _Cs_SDWidth
        _Caculation_Parameters['_XVT']  				= _Cs_XVT
        _Caculation_Parameters['_PCCrit']  				= _Cs_PCCrit

        #Generate Sref
        self._DesignParameter['_Cs_nmos'] = self._SrefElementDeclaration(_DesignObj=A00_NMOSWithDummy_v3._NMOS( _DesignParameter=None, _Name='{}:_Cs_nmos'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Cs_nmos']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Cs_nmos']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Cs_nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Cs_nmos']['_XYCoordinates']=[[0, 0]]

        ######################################################################################################################### NMOS_Currnet_source:source_M1_for_later_calculation
        #Define Boundary_element
        self._DesignParameter['_Cs_nmos_source_M1'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )
        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Cs_nmos','_Met1Layer')
        self._DesignParameter['_Cs_nmos_source_M1']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Cs_nmos','_Met1Layer')
        self._DesignParameter['_Cs_nmos_source_M1']['_YWidth'] = tmp1[0]['_Ywidth']

        #For num of M1 in Nmos
        tmp1 = self.get_param_KJH2('_Cs_nmos','_Met1Layer')
        
        #Define coord.
            #Define flag
        flag = 1
        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] ]
                tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                #tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                #tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Cs_nmos_source_M1']['_XYCoordinates'] = tmpXY 

        ######################################################################################################################### NMOS_Currnet_source:Drain via(V1 M1-M2)
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Cs_nmos_drain_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Cs_nmos_drain_Via1_M1M2'.format(_Name)))[0]

        #Define Cox
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

        #Define Coy
            #Calculate Number of V1
        M1_ywidth   = self.getYWidth('_Cs_nmos','_Met1Layer')
        Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

            #Define Num of V1
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

        #M1, M2 and V1 layer XY_width are calculated
        self._DesignParameter['_Cs_nmos_drain_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V1 coord: Source & Drain Zigzag placing
            #initialize coord
        self._DesignParameter['_Cs_nmos_drain_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Define flag
        flag = 1

            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH2('_Cs_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Cs_nmos_drain_Via1_M1M2','_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                #tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] ]
                #tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Cs_nmos_drain_Via1_M1M2']['_XYCoordinates'] = tmpXY        

        ######################################################################################################################### NMOS_Currnet_source:Drain M2 connection
        #pre-defined values
        y_distance = 100
            ########################################################################################################### NMOS_Currnet_source:Drain M2 connection:Vtc_M2        
        #Define Boundary_element
        self._DesignParameter['_Cs_nmos_drain_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_XWidth'] = self._DesignParameter['_Cs_nmos_drain_Via1_M1M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Cs_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Cs_nmos_drain_Via1_M1M2','_Met2Layer')
        
        self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_up'][1] ) + y_distance

        #Initialize coordinate
        self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Cs_nmos_drain_Via1_M1M2')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Cs_nmos_drain_Via1_M1M2','_Met2Layer')
            tmp2 = self.get_param_KJH2('_Cs_nmos_drain_m2_vtc')
            tmp3 = self.get_param_KJH2('_Cs_nmos_drain_m2_vtc')

            target_coord        = tmp1[i]['_XY_up_left']
            approaching_coord   = tmp2[0]['_XY_down_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### NMOS_Currnet_source:Drain M2 connectionHrz_M2
        #Define Boundary_element
        self._DesignParameter['_Cs_nmos_drain_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Cs_nmos_drain_m2_vtc')
        self._DesignParameter['_Cs_nmos_drain_m2_hrz']['_XWidth'] = abs( tmp1[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Define Boundary_element _YWidth        
        self._DesignParameter['_Cs_nmos_drain_m2_hrz']['_YWidth'] = self._DesignParameter['_Cs_nmos_drain_m2_vtc']['_XWidth']

        #Initialize coordinate
        self._DesignParameter['_Cs_nmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        tmp1 = self.get_param_KJH2('_Cs_nmos_drain_m2_vtc')
        tmp2 = self.get_param_KJH2('_Cs_nmos_drain_m2_hrz')
        tmp3 = self.get_param_KJH2('_Cs_nmos_drain_m2_hrz')

        target_coord        = tmp1[0]['_XY_up_left']
        approaching_coord   = tmp2[0]['_XY_down_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['_Cs_nmos_drain_m2_hrz']['_XYCoordinates'] = tmpXY        

        ######################################################################################################################### NMOS_Currnet_source:Polygate_connect
            ########################################################################################################### NMOS_Currnet_source:Polygate_connect:Vtc
        #Pre-defined
        Vtc_poly_ydistance = 80

        #Define Boundary_element
        self._DesignParameter['_Cs_nmos_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Cs_nmos_vtc_poly']['_YWidth'] = Vtc_poly_ydistance

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Cs_nmos','_POLayer')
        self._DesignParameter['_Cs_nmos_vtc_poly']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Cs_nmos','_POLayer')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_vtc_poly']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Cs_nmos','_POLayer')
            tmp2 = self.get_param_KJH2('_Cs_nmos_vtc_poly')
            tmp3 = self.get_param_KJH2('_Cs_nmos_vtc_poly')

            target_coord        = tmp1[i]['_XY_down']
            approaching_coord   = tmp2[0]['_XY_up']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord.tolist())

        self._DesignParameter['_Cs_nmos_vtc_poly']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### NMOS_Currnet_source:Polygate_connect:Hrz        
        #Pre-defined
        Horz_poly_ywidth = 50

        #Define Boundary_element
        self._DesignParameter['_Cs_nmos_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Cs_nmos_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Cs_nmos','_POLayer')
        self._DesignParameter['_Cs_nmos_hrz_poly']['_XWidth'] = abs( tmp[-1]['_XY_right'][0] - tmp[0]['_XY_left'][0] )

        #Define Boundary_element _XYCoordinates
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Cs_nmos_vtc_poly')
        tmp2 = self.get_param_KJH2('_Cs_nmos_hrz_poly')
        tmp3 = self.get_param_KJH2('_Cs_nmos_hrz_poly')

        target_coord        = tmp1[0]['_XY_down_left']
        approaching_coord   = tmp2[0]['_XY_up_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        
        self._DesignParameter['_Cs_nmos_hrz_poly']['_XYCoordinates'] = [New_Scoord]        
        










        ######################################################################################################################### NMOS_SW:Sref gen
        #Pre-defined
        poly_to_xvt_distance = 150
        
        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A00_NMOSWithDummy_v3._NMOS._ParametersForDesignCalculation)
        _Caculation_Parameters['_NMOSNumberofGate']  	= _Sw_NMOSNumberofGate
        _Caculation_Parameters['_NMOSChannelWidth']  	= _Sw_NMOSChannelWidth
        _Caculation_Parameters['_NMOSChannellength'] 	= _Sw_NMOSChannellength
        _Caculation_Parameters['_NMOSDummy']  			= _Sw_NMOSDummy
        _Caculation_Parameters['_GateSpacing']  		= _Sw_GateSpacing
        _Caculation_Parameters['_SDWidth']  			= _Sw_SDWidth
        _Caculation_Parameters['_XVT']  				= _Sw_XVT
        _Caculation_Parameters['_PCCrit']  				= _Sw_PCCrit

        #Generate Sref
        self._DesignParameter['_Sw_nmos'] = self._SrefElementDeclaration(_DesignObj=A00_NMOSWithDummy_v3._NMOS( _DesignParameter=None, _Name='{}:_Sw_nmos'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_Sw_nmos']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_Sw_nmos']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Sw_nmos']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_Sw_nmos']['_XYCoordinates']=[[0, 0]]        

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
                    #Xcoord
        tmp1_1 = self.get_param_KJH2('_Cs_nmos','_PODummyLayer')
        target_coordx = tmp1_1[-1]['_XY_right'][0]
                    #Ycoord
        tmp1_2 = self.get_param_KJH2('_Cs_nmos','_{}Layer'.format(_Cs_XVT))
        target_coordy = tmp1_2[0]['_XY_down'][1]

        target_coord = [target_coordx,target_coordy]

                #Approaching_coord
                    #Xcoord
        tmp2_1 = self.get_param_KJH2('_Sw_nmos','_PODummyLayer')
        approaching_coordx = tmp2_1[0]['_XY_left'][0]
                    #Ycoord
        tmp2_2 = self.get_param_KJH2('_Sw_nmos','_{}Layer'.format(_Sw_XVT))
        approaching_coordy = tmp2_2[0]['_XY_down'][1]

        approaching_coord = [ approaching_coordx,approaching_coordy ]

                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos') 
        Scoord = tmp3[0]['_XY_cent'] 
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] + poly_to_xvt_distance
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos']['_XYCoordinates'] = tmpXY

        ######################################################################################################################### NMOS_Currnet_source:source_M1_for_later_calculation
        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_drain_M1'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL1'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL1'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )
        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        self._DesignParameter['_Sw_nmos_drain_M1']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        self._DesignParameter['_Sw_nmos_drain_M1']['_YWidth'] = tmp1[0]['_Ywidth']

        #For num of M1 in Nmos
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        
        #Define coord.
            #Define flag
        flag = 1
        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                #tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] ]
                #tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] ]
                tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Sw_nmos_drain_M1']['_XYCoordinates'] = tmpXY 

        ######################################################################################################################### NMOS_SW:Source via(V1 M1-M2)
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_source_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Sw_nmos_source_Via1_M1M2'.format(_Name)))[0]

        #Define Cox
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

        #Define Coy
            #Calculate Number of V1
        M1_ywidth   = self.getYWidth('_Sw_nmos','_Met1Layer')
        Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

            #Define Num of V1
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

        #M1, M2 and V1 layer XY_width are calculated
        self._DesignParameter['_Sw_nmos_source_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V1 coord: Source & Drain Zigzag placing
            #initialize coord
        self._DesignParameter['_Sw_nmos_source_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Define flag
        flag = 1

            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Sw_nmos_source_Via1_M1M2','_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] ]
                tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                # tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                # tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Sw_nmos_source_Via1_M1M2']['_XYCoordinates'] = tmpXY              
        
        ######################################################################################################################### NMOS_SW:Drain via(V1 M1-M2)
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_drain_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Sw_nmos_drain_Via1_M1M2'.format(_Name)))[0]

        #Define Cox
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

        #Define Coy
            #Calculate Number of V1
        M1_ywidth   = self.getYWidth('_Sw_nmos','_Met1Layer')
        Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

            #Define Num of V1
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

        #M1, M2 and V1 layer XY_width are calculated
        self._DesignParameter['_Sw_nmos_drain_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Cal V1 coord: Source & Drain Zigzag placing
            #initialize coord
        self._DesignParameter['_Sw_nmos_drain_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Define flag
        flag = 1

            #For num of M1 in Nmos
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Sw_nmos_drain_Via1_M1M2','_Met1Layer')

        tmpXY = []
        for i in range(0,len(tmp1)):

            #Source
            if flag == 1:
                # tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] ]
                # tmpXY.append(tmp3)
                flag = -1
            #Drain
            else:
                tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
                tmpXY.append(tmp3)
                flag = +1

        self._DesignParameter['_Sw_nmos_drain_Via1_M1M2']['_XYCoordinates'] = tmpXY        

        ######################################################################################################################### NMOS_SW:Source M2 connection
        #pre-defined values
        y_distance1 = 100
            ########################################################################################################### NMOS_SW:Source M2 connection:Vtc_M2        
        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_source_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Sw_nmos_source_m2_vtc']['_XWidth'] = self._DesignParameter['_Sw_nmos_source_Via1_M1M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Sw_nmos_source_Via1_M1M2','_Met2Layer')
        
        self._DesignParameter['_Sw_nmos_source_m2_vtc']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_up'][1] ) + y_distance1

        #Initialize coordinate
        self._DesignParameter['_Sw_nmos_source_m2_vtc']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Sw_nmos_source_Via1_M1M2')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_source_m2_vtc']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Sw_nmos_source_Via1_M1M2','_Met2Layer')
            tmp2 = self.get_param_KJH2('_Sw_nmos_source_m2_vtc')
            tmp3 = self.get_param_KJH2('_Sw_nmos_source_m2_vtc')

            target_coord        = tmp1[i]['_XY_up_left']
            approaching_coord   = tmp2[0]['_XY_down_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['_Sw_nmos_source_m2_vtc']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### NMOS_SW:Source M2 connectionHrz_M2
        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_source_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Sw_nmos_source_m2_vtc')
        self._DesignParameter['_Sw_nmos_source_m2_hrz']['_XWidth'] = abs( tmp1[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Define Boundary_element _YWidth        
        self._DesignParameter['_Sw_nmos_source_m2_hrz']['_YWidth'] = self._DesignParameter['_Sw_nmos_source_m2_vtc']['_XWidth']

        #Initialize coordinate
        self._DesignParameter['_Sw_nmos_source_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_source_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        tmp1 = self.get_param_KJH2('_Sw_nmos_source_m2_vtc')
        tmp2 = self.get_param_KJH2('_Sw_nmos_source_m2_hrz')
        tmp3 = self.get_param_KJH2('_Sw_nmos_source_m2_hrz')

        target_coord        = tmp1[0]['_XY_up_left']
        approaching_coord   = tmp2[0]['_XY_down_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['_Sw_nmos_source_m2_hrz']['_XYCoordinates'] = tmpXY   

        ######################################################################################################################### NMOS_SW:Drain M2 connection
        #pre-defined values
        y_distance2 = 100
            ########################################################################################################### NMOS_SW:Drain M2 connection:Vtc_M2        
        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_drain_m2_vtc'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_XWidth'] = self._DesignParameter['_Sw_nmos_drain_Via1_M1M2']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth']

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Sw_nmos','_Met1Layer')
        tmp2 = self.get_param_KJH2('_Sw_nmos_drain_Via1_M1M2','_Met2Layer')
        
        self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_up'][1] ) + y_distance2

        #Initialize coordinate
        self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Sw_nmos_drain_Via1_M1M2')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Sw_nmos_drain_Via1_M1M2','_Met2Layer')
            tmp2 = self.get_param_KJH2('_Sw_nmos_drain_m2_vtc')
            tmp3 = self.get_param_KJH2('_Sw_nmos_drain_m2_vtc')

            target_coord        = tmp1[i]['_XY_down_left']
            approaching_coord   = tmp2[0]['_XY_up_left']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            tmpXY.append(New_Scoord)

        self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### NMOS_SW:Drain M2 connectionHrz_M2
        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_drain_m2_hrz'] = self._BoundaryElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XWidth=None,
                                                                                            _YWidth=None,
                                                                                            _XYCoordinates=[ ],
                                                                                           )

        #Define Boundary_element _XWidth
        tmp1 = self.get_param_KJH2('_Sw_nmos_drain_m2_vtc')
        self._DesignParameter['_Sw_nmos_drain_m2_hrz']['_XWidth'] = abs( tmp1[-1]['_XY_right'][0] - tmp1[0]['_XY_left'][0] )

        #Define Boundary_element _YWidth        
        self._DesignParameter['_Sw_nmos_drain_m2_hrz']['_YWidth'] = self._DesignParameter['_Sw_nmos_drain_m2_vtc']['_XWidth']

        #Initialize coordinate
        self._DesignParameter['_Sw_nmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        #Define Boundary_element _XYCoordinates
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_drain_m2_hrz']['_XYCoordinates'] = [[0,0]]
        
        tmp1 = self.get_param_KJH2('_Sw_nmos_drain_m2_vtc')
        tmp2 = self.get_param_KJH2('_Sw_nmos_drain_m2_hrz')
        tmp3 = self.get_param_KJH2('_Sw_nmos_drain_m2_hrz')

        target_coord        = tmp1[0]['_XY_down_left']
        approaching_coord   = tmp2[0]['_XY_up_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        tmpXY.append(New_Scoord)

        self._DesignParameter['_Sw_nmos_drain_m2_hrz']['_XYCoordinates'] = tmpXY   

        ######################################################################################################################### NMOS_SW:Polygate_connect
            ########################################################################################################### NMOS_SW:Polygate_connect:Vtc
        #Pre-defined
        Vtc_poly_ydistance = 80

        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_vtc_poly'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        tmp1 = self.get_param_KJH2('_Cs_nmos_hrz_poly')
        tmp2 = self.get_param_KJH2('_Sw_nmos','_POLayer')

        self._DesignParameter['_Sw_nmos_vtc_poly']['_YWidth'] = abs(tmp2[0]['_XY_down'][1] - tmp1[0]['_XY_down'][1]) + Vtc_poly_ydistance

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Sw_nmos','_POLayer')
        self._DesignParameter['_Sw_nmos_vtc_poly']['_XWidth'] = tmp[0]['_Xwidth']

        #Define Boundary_element _XYCoordinates
        tmp = self.get_param_KJH2('_Sw_nmos','_POLayer')
        tmpXY = []
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_vtc_poly']['_XYCoordinates'] = [[0,0]]
        for i in range(0,len(tmp)):
            tmp1 = self.get_param_KJH2('_Sw_nmos','_POLayer')
            tmp2 = self.get_param_KJH2('_Sw_nmos_vtc_poly')
            tmp3 = self.get_param_KJH2('_Sw_nmos_vtc_poly')

            target_coord        = tmp1[i]['_XY_down']
            approaching_coord   = tmp2[0]['_XY_up']
            Scoord              = tmp3[0]['_XY_cent']

            New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
            New_Scoord = np.round(New_Scoord,2)
            tmpXY.append(New_Scoord.tolist())

        self._DesignParameter['_Sw_nmos_vtc_poly']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### NMOS_SW:Polygate_connect:Hrz        
        #Pre-defined
        Horz_poly_ywidth = 50

        #Define Boundary_element
        self._DesignParameter['_Sw_nmos_hrz_poly'] = self._BoundaryElementDeclaration(
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XWidth=None,
                                                                                    _YWidth=None,
                                                                                    _XYCoordinates=[ ],
                                                                                   )

        #Define Boundary_element _YWidth
        self._DesignParameter['_Sw_nmos_hrz_poly']['_YWidth'] = Horz_poly_ywidth

        #Define Boundary_element _XWidth
        tmp = self.get_param_KJH2('_Sw_nmos','_POLayer')
        self._DesignParameter['_Sw_nmos_hrz_poly']['_XWidth'] = abs( tmp[-1]['_XY_right'][0] - tmp[0]['_XY_left'][0] )

        #Define Boundary_element _XYCoordinates
        #Calculate Sref XYcoord
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_hrz_poly']['_XYCoordinates'] = [[0,0]]
            #Calculation
        tmp1 = self.get_param_KJH2('_Sw_nmos_vtc_poly')
        tmp2 = self.get_param_KJH2('_Sw_nmos_hrz_poly')
        tmp3 = self.get_param_KJH2('_Sw_nmos_hrz_poly')

        target_coord        = tmp1[0]['_XY_down_left']
        approaching_coord   = tmp2[0]['_XY_up_left']
        Scoord              = tmp3[0]['_XY_cent']

        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        
        self._DesignParameter['_Sw_nmos_hrz_poly']['_XYCoordinates'] = [New_Scoord] 











        ######################################################################################################################### Nmos_sw_and_cs_connection_M2

        #Check which one is lower than the other
        tmp1 = self.get_param_KJH2('_Cs_nmos_drain_m2_hrz')
        tmp2 = self.get_param_KJH2('_Sw_nmos_source_m2_hrz')

        #If Current source height is smaller
        if tmp1[0]['_XY_up'][1] < tmp2[0]['_XY_up'][1] :
            #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
            self._DesignParameter['_sw_and_cs_connect_M2'] = self._PathElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XYCoordinates=[],
                                                                                            _Width=None,
                                                                                        )

            #P1--P2 Width
            tmp = self.get_param_KJH2('_Cs_nmos_drain_m2_hrz')
            self._DesignParameter['_sw_and_cs_connect_M2']['_Width'] = tmp[0]['_Ywidth']

            #P1--P2 coordiantes
            tmpXY = []
                #P1 calculation
            tmp3 = self.get_param_KJH2('_Cs_nmos_drain_m2_hrz')
            P1 = tmp3[0]['_XY_right']
                #P2 calculation
                    #P2x
            tmp4 = self.get_param_KJH2('_Sw_nmos_source_m2_vtc')
            p2x = tmp4[0]['_XY_left'][0]
                    #P2y
            p2y = P1[1]
            P2 = [p2x,p2y]
                #P1_P2
            P1_P2 = [P1,P2]
            tmpXY.append(P1_P2)
                #Cal tmpXY
            self._DesignParameter['_sw_and_cs_connect_M2']['_XYCoordinates'] = tmpXY

        #SW is smaller than the other
        else:
            #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
            self._DesignParameter['_sw_and_cs_connect_M2'] = self._PathElementDeclaration(
                                                                                            _Layer=DesignParameters._LayerMapping['METAL2'][0],
                                                                                            _Datatype=DesignParameters._LayerMapping['METAL2'][1],
                                                                                            _XYCoordinates=[],
                                                                                            _Width=None,
                                                                                        )

            #P1--P2 Width
            tmp = self.get_param_KJH2('_Sw_nmos_source_m2_hrz')
            self._DesignParameter['_sw_and_cs_connect_M2']['_Width'] = tmp[0]['_Ywidth']

            #P1--P2 coordiantes
            tmpXY = []
                #P1 calculation
            tmp3 = self.get_param_KJH2('_Sw_nmos_source_m2_hrz')
            P1 = tmp3[0]['_XY_left']
                #P2 calculation
                    #P2x
            tmp4 = self.get_param_KJH2('_Cs_nmos_drain_m2_vtc')
            p2x = tmp4[0]['_XY_right'][0]
                    #P2y
            p2y = P1[1]
            P2 = [p2x,p2y]
                #P1_P2
            P1_P2 = [P1,P2]
            tmpXY.append(P1_P2)
                #Cal tmpXY
            self._DesignParameter['_sw_and_cs_connect_M2']['_XYCoordinates'] = tmpXY


        ######################################################################################################################### Nmos_cs_via1_and_via2(poly -- M3)
            ########################################################################################################### Nmos_cs_via1_and_via2(poly -- M3):CA        
        #Define CA Parameter
        _Caculation_Parameters = copy.deepcopy(A07_ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = None
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = None
        
        #Calcuate _ViaPoly2Met1NumberOfCOX
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = 1
        
        #CA Sref declaration
        self._DesignParameter['_Cs_nmos_gate_CA_PolyM1'] = self._SrefElementDeclaration(_DesignObj=A07_ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='{}:_Cs_nmos_gate_CA_PolyM1'.format(_Name)))[0]
        
        #M1, M2 and CA layer XY_width are calculated
        self._DesignParameter['_Cs_nmos_gate_CA_PolyM1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**_Caculation_Parameters)
        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_gate_CA_PolyM1']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Cs_nmos_hrz_poly') 
        target_coord = tmp1[0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Cs_nmos_gate_CA_PolyM1','_POLayer')
        approaching_coord = tmp2[0]['_XY_down_right']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Cs_nmos_gate_CA_PolyM1')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_nmos_gate_CA_PolyM1']['_XYCoordinates'] = tmpXY
        
            ########################################################################################################### Nmos_cs_via1_and_via2(poly -- M3):via1        
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Cs_nmos_gate_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Cs_nmos_gate_Via1_M1M2'.format(_Name)))[0]

        #Calcuate _ViaMet22Met3NumberOfCOX
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Cs_nmos_gate_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_gate_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Cs_nmos_gate_CA_PolyM1','_Met1Layer') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Cs_nmos_gate_Via1_M1M2','_Met1Layer')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Cs_nmos_gate_Via1_M1M2')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_nmos_gate_Via1_M1M2']['_XYCoordinates'] = tmpXY

            ########################################################################################################### Nmos_cs_via1_and_via2(poly -- M3):via2        
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Cs_nmos_gate_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:_Cs_nmos_gate_Via2_M2M3'.format(_Name)))[0]

        #Calcuate _ViaMet22Met3NumberOfCOX
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Cs_nmos_gate_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Cs_nmos_gate_Via2_M2M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Cs_nmos_gate_Via1_M1M2','_Met2Layer') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Cs_nmos_gate_Via2_M2M3','_Met2Layer')  
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Cs_nmos_gate_Via2_M2M3')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Cs_nmos_gate_Via2_M2M3']['_XYCoordinates'] = tmpXY

        






        ######################################################################################################################### Nmos_sw_CA_via1_and_via2_and_via3(poly -- M4)
            ########################################################################################################### Nmos_sw_CA_via1_and_via2_and_via3(poly -- M4):CA
        #Define CA Parameter
        _Caculation_Parameters = copy.deepcopy(A07_ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = None
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = None
        
        #Calcuate _ViaPoly2Met1NumberOfCOX
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = 1
        
        #CA Sref declaration
        self._DesignParameter['_Sw_nmos_gate_CA_PolyM1'] = self._SrefElementDeclaration(_DesignObj=A07_ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='{}:_Sw_nmos_gate_CA_PolyM1'.format(_Name)))[0]
        
        #M1, M2 and CA layer XY_width are calculated
        self._DesignParameter['_Sw_nmos_gate_CA_PolyM1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**_Caculation_Parameters)
        
        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_gate_CA_PolyM1']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_nmos_hrz_poly') 
        target_coord = tmp1[0]['_XY_down_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_nmos_gate_CA_PolyM1','_POLayer')
        approaching_coord = tmp2[0]['_XY_down_right']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos_gate_CA_PolyM1')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos_gate_CA_PolyM1']['_XYCoordinates'] = tmpXY            
            ########################################################################################################### Nmos_sw_CA_via1_and_via2_and_via3(poly -- M4):via1
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_gate_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Sw_nmos_gate_Via1_M1M2'.format(_Name)))[0]

        #Calcuate _ViaMet22Met3NumberOfCOX
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_nmos_gate_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_gate_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_nmos_gate_CA_PolyM1','_Met1Layer') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_nmos_gate_Via1_M1M2','_Met1Layer')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos_gate_Via1_M1M2')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos_gate_Via1_M1M2']['_XYCoordinates'] = tmpXY            
            ########################################################################################################### Nmos_sw_CA_via1_and_via2_and_via3(poly -- M4):via2
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_gate_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:_Sw_nmos_gate_Via2_M2M3'.format(_Name)))[0]

        #Calcuate _ViaMet22Met3NumberOfCOX
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_nmos_gate_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_gate_Via2_M2M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_nmos_gate_Via1_M1M2','_Met2Layer') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_nmos_gate_Via2_M2M3','_Met2Layer')  
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos_gate_Via2_M2M3')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos_gate_Via2_M2M3']['_XYCoordinates'] = tmpXY
            ########################################################################################################### Nmos_sw_CA_via1_and_via2_and_via3(poly -- M4):via3 
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A10_ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_gate_Via3_M3M4'] = self._SrefElementDeclaration(_DesignObj=A10_ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:_Sw_nmos_gate_Via3_M3M4'.format(_Name)))[0]

        #Calcuate _ViaMet32Met4NumberOfCOX
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_nmos_gate_Via3_M3M4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_gate_Via3_M3M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_nmos_gate_Via2_M2M3','_Met3Layer') 
        target_coord = tmp1[0]['_XY_up_left']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_nmos_gate_Via3_M3M4','_Met3Layer')
        approaching_coord = tmp2[0]['_XY_up_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos_gate_Via3_M3M4')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos_gate_Via3_M3M4']['_XYCoordinates'] = tmpXY


        ######################################################################################################################### Nmos_Sw_drain_via2(M2 -- M3)
        #Define ViaX Parameter
        _Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

        #Sref ViaX declaration
        self._DesignParameter['_Sw_nmos_drain_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:_Sw_nmos_drain_Via2_M2M3'.format(_Name)))[0]

        #Calcuate _ViaMet22Met3NumberOfCOX
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 2

        #Calcuate _ViaMet22Met3NumberOfCOY
        _Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 1

        #Generate Metal(x), Metal(x+1) and C0(Viax) layer
        self._DesignParameter['_Sw_nmos_drain_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Sw_nmos_drain_Via2_M2M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('_Sw_nmos_drain_m2_hrz') 
        target_coord = tmp1[0]['_XY_down_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH2('_Sw_nmos_drain_Via2_M2M3','_Met2Layer')  
        approaching_coord = tmp2[0]['_XY_down_left']
                #Sref coord
        tmp3 = self.get_param_KJH2('_Sw_nmos_drain_Via2_M2M3')
        Scoord = tmp3[0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Sw_nmos_drain_Via2_M2M3']['_XYCoordinates'] = tmpXY
            
        ################################################################################################################################### Calculation_End
        print('##############################')
        print('##     Calculation_End    ##')
        print('##############################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_D_building_block'
    cellname = 'D00_nmos_sw_and_nmos_currentsource_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
    

                                            #Current source nmos
                                            _Cs_NMOSNumberofGate=3,
                                            _Cs_NMOSChannelWidth=1000,
                                            _Cs_NMOSChannellength=200,
                                            _Cs_NMOSDummy=True,
                                            _Cs_GateSpacing=None,
                                            _Cs_SDWidth=None,
                                            _Cs_XVT='SLVT',
                                            _Cs_PCCrit=None,


                                            #SW nmos
                                            _Sw_NMOSNumberofGate=4,
                                            _Sw_NMOSChannelWidth=1000,
                                            _Sw_NMOSChannellength=30,
                                            _Sw_NMOSDummy=True,
                                            _Sw_GateSpacing=None,
                                            _Sw_SDWidth=None,
                                            _Sw_XVT='SLVT',
                                            _Sw_PCCrit=None,


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
    LayoutObj = _nmos_sw_and_nmos_currentsource(_DesignParameter=None, _Name=cellname)
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
