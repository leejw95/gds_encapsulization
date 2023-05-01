

############################################################################################################################################################ BASIC Modules
import StickDiagram_KJH0
import DesignParameters
import DRC

import copy
import math
import numpy as np

import A00_NMOSWithDummy_v2
import A01_NSubRing
import A02_PMOSWithDummy
import A03_PSubRing
import A04_NbodyContact
import A05_PbodyContact
import A06_ViaStack
import A07_ViaPoly2Met1
import A08_ViaMet12Met2
import A09_ViaMet22Met3
import A10_ViaMet32Met4
import A11_ViaMet42Met5
import A12_ViaMet52Met6
import A13_ViaMet62Met7
import A14_ViaMet72Met8
import A16_UNITR


from SthPack import CoordCalc

from generatorLib.generator_models.KJH91_Project.Library_and_Engine import DesignParameters
from generatorLib.generator_models.KJH91_Project.Library_and_Engine import StickDiagram_KJH0
from generatorLib.generator_models.KJH91_Project.Library_and_Engine import DRC












############################################################################################################################################################ Class_HEADER
class _DRIVER(StickDiagram_KJH0._StickDiagram_KJH): ##########################################################################^^^^^^^^^^^^^^^^^^^^^

    ##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
	#Define input_parameters for Design calculation 
	_ParametersForDesignCalculation = dict(	
											
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

############################################################################################################################################################ SREF Generation
		print('##     SREF Generation    ##')

		#Define Calculation_Parameters
		_Caculation_Parameters = copy.deepcopy( 'filename------' .'classname------'._ParametersForDesignCalculation) ##########^^^^^^^^^^^^^^^^^^^^^ex)copy.deepcopy(B16_nmos_power_v2._NMOS_POWER._ParametersForDesignCalculation)
		_Caculation_Parameters[' internally_define_parameter_list----- ']  = ' ----- ' #################^^^^^^^^^^^^^^^^^^^^^ex)_Caculation_Parameters['_NMOSPOWER_PbodyContact_1_Length']  = _NMOSPOWER_PbodyContact_1_Length

		#Generate Sref
		self._DesignParameter[' elementname----- '] = self._SrefElementDeclaration(_DesignObj='-----'.'-----'( _DesignParameter=None, _Name='{}:-----'.format(_Name)))[0] ##########^^^^^^^^^^^^^^^^^^^^^ex)self._DesignParameter['_NMOS_POWER'] = self._SrefElementDeclaration(_DesignObj=B16_nmos_power_v2._NMOS_POWER( _DesignParameter=None, _Name='{}:NMOS_POWER'.format(_Name)))[0]
																			  
        #Define Sref Relection
        self._DesignParameter[' elementname-----']['_Reflect'] = [0, 0, 0] ##########^^^^^^^^^^^^^^^^^^^^^ex)self._DesignParameter['_NMOS_POWER']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['elemenetname------']['_Angle'] = 0 ##########^^^^^^^^^^^^^^^^^^^^^ex)'_NMOS_POWER'

		#Calculate Sref Layer by using Calculation_Parameter
		self._DesignParameter['elementname-----']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^ex)'_NMOS_POWER'  

		#Define Sref _XYcoordinate
		self._DesignParameter['elementname-----']['_XYCoordinates']=[[0, 0]] ##########^^^^^^^^^^^^^^^^^^^^^ex)'_NMOS_POWER'  


############################################################################################################################################################ Boundary_element Generation: 
		print('##     Boundary_element Generation:     ##')

        #Define Boundary_element
		self._DesignParameter['A-----'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['B-----'][0],    ##########^^^^^^^^^^^^^^^^^^^^^ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
                                                                            _Datatype=DesignParameters._LayerMapping['B-----'][1], ##########^^^^^^^^^^^^^^^^^^^^^ex)METAL1
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

		#Define Boundary_element _YWidth
		self._DesignParameter['A-----']['_YWidth'] = '-----'

		#Define Boundary_element _XWidth
		self._DesignParameter['A-----']['_XWidth'] = '-----'

		#Define Boundary_element _XYCoordinates
		self._DesignParameter['A-----']['_XYCoordinates'] = [[0,0]]

############################################################################################################################################################ Path_element Generation: 
		print('##     Path_element Generation:     ##')

        #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) /
        self._DesignParameter['pathelementname'] = self._PathElementDeclaration(          
                                                                                    _Layer=DesignParameters._LayerMapping['POLY'][0], ##########^^^^^^^^^^^^^^^^^^^^
                                                                                    _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                                    _XYCoordinates=[],
                                                                                    _Width=None,
                                                                                )

        #P1--P2 Width
        self._DesignParameter['pathelementname']['_Width'] = '-----' ##########^^^^^^^^^^^^^^^^^^^^^
        
        #P1--P2 coordiantes
        tmpXY = []
			#P1 calculation
		P1 = '?'
			#P2 calculation
		P2 = '?'
			#P1_P2
		P1_P2 = [P1,P2]
		tmpXY.append(P1_P2)
            #Cal tmpXY
        self._DesignParameter['pathelementname']['_XYCoordinates'] = tmpXY






################################################################################################################################################## Sref generation: _PbodyContact
		print('##     Sref generation: _PbodyContact    ##')

		#Calculate _PbodyContact input parameter: input as _PbodyContCount_of_Width and _PbodyCont_Length and _PbodyContact_Vert
			#If Vert==1
		if 'elementname-----'_PbodyContact_Vert == 1: ##########^^^^^^^^^^^^^^^^^^^^^
			_PbodyContact_NumberOfPbodyCOX = 'elementname-----'_PbodyContCount_of_Width ##########^^^^^^^^^^^^^^^^^^^^^
			_PbodyContact_NumberOfPbodyCOY = (int((('elementname-----'_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - 'elementname-----'_PbodyContCount_of_Width) + 0 ##########2^^^^^^^^^^^^^^^^^^^^^
			_PbodyContact_Met1XWidth       = None
			_PbodyContact_Met1YWidth       = None
			
		else:
			_PbodyContact_NumberOfPbodyCOX = (int((('elementname-----'_PbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - 'elementname-----'_PbodyContCount_of_Width) + 0 ##########2^^^^^^^^^^^^^^^^^^^^^
			_PbodyContact_NumberOfPbodyCOY = 'elementname-----'_PbodyContCount_of_Width
			_PbodyContact_Met1XWidth       = None
			_PbodyContact_Met1YWidth       = None
		
		#Define _PbodyContact input parameter
		_Caculation_Parameters = copy.deepcopy(A05_PbodyContact._PbodyContact._ParametersForDesignCalculation)
		_Caculation_Parameters['_NumberOfPbodyCOX']     = _PbodyContact_NumberOfPbodyCOX
		_Caculation_Parameters['_NumberOfPbodyCOY']     = _PbodyContact_NumberOfPbodyCOY
		_Caculation_Parameters['_Met1XWidth']           = _PbodyContact_Met1XWidth
		_Caculation_Parameters['_Met1YWidth']           = _PbodyContact_Met1YWidth

		#Define _PbodyContact Sref
		self._DesignParameter['elementname-----_PbodyContact'] = self._SrefElementDeclaration(_DesignObj=A05_PbodyContact._PbodyContact( _DesignParameter=None, _Name='{}:_elementname-----_PbodyContact'.format(_Name)))[0]  ##########2^^^^^^^^^^^^^^^^^^^^^

		#Define Sref Relection
        self._DesignParameter['elementname-----_PbodyContact']['_Reflect'] = [0, 0, 0] ##########^^^^^^^^^^^^^^^^^^^^^
        
        #Define Sref Angle
        self._DesignParameter['elementname-----_PbodyContact']['_Angle'] = 0 ##########^^^^^^^^^^^^^^^^^^^^^

		#Define NMOS_DEFAULT layer
		self._DesignParameter['elementname-----_PbodyContact']['_DesignObj']._CalculatePbodyContactDesignParameter(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^

		#Define NMOS_DEFAULT coordinate
		self._DesignParameter['elementname-----_PbodyContact']['_XYCoordinates']=[[0, 0]] ##########^^^^^^^^^^^^^^^^^^^^^

################################################################################################################################################## Sref generation: _NbodyContact
		print('##     Sref generation: _NbodyContact    ##')

		#Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
			#If vertical
		if 'element-----'_NbodyContact_Vert == 1: ##########^^^^^^^^^^^^^^^^^^^^^
			_NbodyContact_NumberOfNbodyCOX = 'element-----'_NbodyContCount_of_Width ##########^^^^^^^^^^^^^^^^^^^^^
			_NbodyContact_NumberOfNbodyCOY = (int((('element-----'_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - 'element-----'_NbodyContCount_of_Width) + 0 ##########2^^^^^^^^^^^^^^^^^^^^^
			_NbodyContact_Met1XWidth       = None
			_NbodyContact_Met1YWidth       = None			
		else:
			_NbodyContact_NumberOfNbodyCOX = (int((('element-----'_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - 'element-----'_NbodyContCount_of_Width) + 0 ##########2^^^^^^^^^^^^^^^^^^^^^
			_NbodyContact_NumberOfNbodyCOY = 'element-----'_NbodyContCount_of_Width ##########^^^^^^^^^^^^^^^^^^^^^
			_NbodyContact_Met1XWidth       = None
			_NbodyContact_Met1YWidth       = None
		
		#Define _NbodyContact input parameter
		_Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
		_Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
		_Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
		_Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
		_Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

		#Define _NbodyContact Sref
		self._DesignParameter['elementname-----_NbodyContact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:elementname-----_NbodyContact'.format(_Name) ))[0] ##########2^^^^^^^^^^^^^^^^^^^^^

		#Define _NbodyContact Sref Relection
        self._DesignParameter['elementname-----_NbodyContact']['_Reflect'] = [0, 0, 0] ##########^^^^^^^^^^^^^^^^^^^^^
        
        #Define _NbodyContact Sref Angle
        self._DesignParameter['elementname-----_NbodyContact']['_Angle'] = 0 		   ##########^^^^^^^^^^^^^^^^^^^^^

		#Define _NbodyContact layer
		self._DesignParameter['elementname-----_NbodyContact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^

		#Define _NbodyContact coordinate
		self._DesignParameter['elementname-----_NbodyContact']['_XYCoordinates']=[[0, 0]] ##########^^^^^^^^^^^^^^^^^^^^^

		#Define NWELL of _NbodyContact
		self._DesignParameter['elementname-----_NbodyContact_Nwell'] = self._BoundaryElementDeclaration( 
																											_Layer=DesignParameters._LayerMapping['NWELL'][0],
																											_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																											_XWidth=None,
																											_YWidth=None,
																											_XYCoordinates=[ ],
																										  ) ##########^^^^^^^^^^^^^^^^^^^^^
		
		#Define NWELL Xwidth
		self._DesignParameter['elementname-----_NbodyContact_Nwell']['_XWidth'] = self.getXWidth('elementname-----_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 ##########2^^^^^^^^^^^^^^^^^^^^^

		#Define NWELL Ywidth
		self._DesignParameter['elementname-----_NbodyContact_Nwell']['_YWidth'] = self.getYWidth('elementname-----_NbodyContact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 ##########2^^^^^^^^^^^^^^^^^^^^^
		
		#Define NWELL Coordinates
		self._DesignParameter['elementname-----_NbodyContact_Nwell']['_XYCoordinates'] =  self.getXY('elementname-----_NbodyContact') ##########2^^^^^^^^^^^^^^^^^^^^^


######################################################################################################################################## Sref generation: NWELL
		print('##     Sref generation: NWELL    ##')

		#Define NWELL
		self._DesignParameter['elementname-----Nwell'] = self._BoundaryElementDeclaration(
																							_Layer=DesignParameters._LayerMapping['NWELL'][0],
																							_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																							_XWidth=None,
																							_YWidth=None,
																							_XYCoordinates=[ ],
																						  ) ##########^^^^^^^^^^^^^^^^^^^^^

		#Define Xwidth
		self._DesignParameter['elementname-----Nwell']['_XWidth'] = ##########^^^^^^^^^^^^^^^^^^^^^

		#Define Ywidth
		self._DesignParameter['elementname-----Nwell']['_YWidth'] = ##########^^^^^^^^^^^^^^^^^^^^^

		#Define Coordinates
		self._DesignParameter['elementname-----Nwell']['_XYCoordinates'] = [ [0,0] ] ##########^^^^^^^^^^^^^^^^^^^^^


######################################################################################################################################## Sref generation: CA(Poly-M1)

        #Define CA Parameter
        _Caculation_Parameters = copy.deepcopy(A07_ViaPoly2Met1._ViaPoly2Met1._ParametersForDesignCalculation)
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = None
        _Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = None
        
        #Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH2('elementname_A-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal1
		tmp2 = self.get_param_KJH2('elementname_B-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal2

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['number1----'],tmp2['number2----']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object
        
		#Calcuate _ViaPoly2Met1NumberOfCOX
        Xwidth = Ovlpcoord[0]['_Xwidth']
		Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Xwidth < 2:
			_Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = 2
		else:
			_Caculation_Parameters['_ViaPoly2Met1NumberOfCOX'] = Num_Via_Xwidth

		#Calcuate _ViaMet22Met3NumberOfCOY
        Ywidth = Ovlpcoord[0]['_Ywidth']
		Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Ywidth < 2:
			_Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = 2
		else:
			_Caculation_Parameters['_ViaPoly2Met1NumberOfCOY'] = Num_Via_Ywidth
        
        #CA Sref declaration
        self._DesignParameter['elementname_CA_PolyM1'] = self._SrefElementDeclaration(_DesignObj=A07_ViaPoly2Met1._ViaPoly2Met1(_DesignParameter=None, _Name='{}:elementname_CA_PolyM1'.format(_Name)))[0]
        
        #M1, M2 and CA layer XY_width are calculated
        self._DesignParameter['elementname_CA_PolyM1']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**_Caculation_Parameters)
        
        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['elementname_CA_PolyM1']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
        target_coord = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Approaching_coord
        tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        approaching_coord = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Sref coord
		tmp3 = self.get_param_KJH2('elementname_CA_PolyM1') ##########^^^^^^^^^^^^^^^^^^^^^
		Scoord = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['elementname_CA_PolyM1']['_XYCoordinates'] = tmpXY  ##########^^^^^^^^^^^^^^^^^^^^^


######################################################################################################################################## Sref generation: Via1(M1-M2)
		print('##     Sref generation: Via1(M1-M2)    ##')

		#Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

		#Sref ViaX declaration
		self._DesignParameter['elementname-----_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:elementname-----_Via1_M1M2'.format(_Name)))[0] ##########2^^^^^^^^^^^^^^^^^^^^^

		#Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH2('elementname_A-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal1
		tmp2 = self.get_param_KJH2('elementname_B-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal2

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['number1----'],tmp2['number2----']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object

		#Calcuate _ViaMet22Met3NumberOfCOX
		Xwidth = Ovlpcoord[0]['_Xwidth']
		Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Xwidth < 2:
			_Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 2
		else:
			_Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = Num_Via_Xwidth

		#Calcuate _ViaMet22Met3NumberOfCOY
		Ywidth = Ovlpcoord[0]['_Ywidth']
		Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Ywidth < 2:
			_Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = 2
		else:
			_Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_Via_Ywidth

		#Generate Metal(x), Metal(x+1) and C0(Viax) layer
		self._DesignParameter['elementname-----_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['elementname-----_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
        target_coord = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Approaching_coord
        tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        approaching_coord = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Sref coord
		tmp3 = self.get_param_KJH2('elementname-----_Via1_M1M2') ##########^^^^^^^^^^^^^^^^^^^^^
		Scoord = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['elementname-----_Via1_M1M2']['_XYCoordinates'] = tmpXY  ##########^^^^^^^^^^^^^^^^^^^^^


######################################################################################################################################## Sref generation: Via2(M2-M3)
		print('##     Sref generation: Via3(M2-M3)    ##')

		#Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A09_ViaMet22Met3._ViaMet22Met3._ParametersForDesignCalculation)
		_Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = None
		_Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = None

		#Sref ViaX declaration
		self._DesignParameter['elementname-----_Via2_M2M3'] = self._SrefElementDeclaration(_DesignObj=A09_ViaMet22Met3._ViaMet22Met3(_DesignParameter=None, _Name='{}:elementname-----_Via2_M2M3'.format(_Name)))[0] ##########2^^^^^^^^^^^^^^^^^^^^^

		#Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH2('elementname_A-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal2
		tmp2 = self.get_param_KJH2('elementname_B-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal3

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['number1----'],tmp2['number2----']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object

		#Calcuate _ViaMet22Met3NumberOfCOX
		Xwidth = Ovlpcoord[0]['_Xwidth']
		Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Xwidth < 2:
			_Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = 2
		else:
			_Caculation_Parameters['_ViaMet22Met3NumberOfCOX'] = Num_Via_Xwidth

		#Calcuate _ViaMet22Met3NumberOfCOY
		Ywidth = Ovlpcoord[0]['_Ywidth']
		Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Ywidth < 2:
			_Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = 2
		else:
			_Caculation_Parameters['_ViaMet22Met3NumberOfCOY'] = Num_Via_Ywidth

		#Generate Metal(x), Metal(x+1) and C0(Viax) layer
		self._DesignParameter['elementname-----_Via2_M2M3']['_DesignObj']._CalculateViaMet22Met3DesignParameterMinimumEnclosureX(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['elementname-----_Via2_M2M3']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
        target_coord = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Approaching_coord
        tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        approaching_coord = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Sref coord
		tmp3 = self.get_param_KJH2('elementname-----_Via2_M2M3') ##########^^^^^^^^^^^^^^^^^^^^^
		Scoord = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['elementname-----_Via2_M2M3']['_XYCoordinates'] = tmpXY  ##########^^^^^^^^^^^^^^^^^^^^^



######################################################################################################################################## Sref generation: Via3(M3-M4)
		print('##     Sref generation: Via3(M3-M4)    ##')

		#Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A10_ViaMet32Met4._ViaMet32Met4._ParametersForDesignCalculation)
		_Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = None
		_Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = None

		#Sref ViaX declaration
		self._DesignParameter['elementname-----_Via3_M3M4'] = self._SrefElementDeclaration(_DesignObj=A10_ViaMet32Met4._ViaMet32Met4(_DesignParameter=None, _Name='{}:elementname-----_Via3_M3M4'.format(_Name)))[0] ##########2^^^^^^^^^^^^^^^^^^^^^

		#Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH2('elementname_A-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal3
		tmp2 = self.get_param_KJH2('elementname_B-----') ##########^^^^^^^^^^^^^^^^^^^^^Metal4

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['number1----'],tmp2['number2----']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object

		#Calcuate _ViaMet32Met4NumberOfCOX
		Xwidth = Ovlpcoord[0]['_Xwidth']
		Num_Via_Xwidth = int( ( Xwidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Xwidth < 2:
			_Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = 2
		else:
			_Caculation_Parameters['_ViaMet32Met4NumberOfCOX'] = Num_Via_Xwidth

		#Calcuate _ViaMet22Met3NumberOfCOY
		Ywidth = Ovlpcoord[0]['_Ywidth']
		Num_Via_Ywidth = int( ( Ywidth - 2 * _DRCobj._MetalxMinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0
			#If Via is less than 2, Num_Via = 2
		if Num_Via_Ywidth < 2:
			_Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = 2
		else:
			_Caculation_Parameters['_ViaMet32Met4NumberOfCOY'] = Num_Via_Ywidth

		#Generate Metal(x), Metal(x+1) and C0(Viax) layer
		self._DesignParameter['elementname-----_Via3_M3M4']['_DesignObj']._CalculateViaMet32Met4DesignParameterMinimumEnclosureX(**_Caculation_Parameters) ##########^^^^^^^^^^^^^^^^^^^^^

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['elementname-----_Via3_M3M4']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
        target_coord = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Approaching_coord
        tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        approaching_coord = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Sref coord
		tmp3 = self.get_param_KJH2('elementname-----_Via3_M3M4') ##########^^^^^^^^^^^^^^^^^^^^^
		Scoord = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['elementname-----_Via3_M3M4']['_XYCoordinates'] = tmpXY  ##########^^^^^^^^^^^^^^^^^^^^^





######################################################################################################################################## Sref generation: Mosfet Via1(M1-M2)
		print('##     Sref generation: Mosfet Via1(M1-M2)    ##')

		#Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A08_ViaMet12Met2_v2._ViaMet12Met2._ParametersForDesignCalculation)
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = None
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = None

		#Sref ViaX declaration
		self._DesignParameter['_Pmos_drain_Via1_M1M2'] = self._SrefElementDeclaration(_DesignObj=A08_ViaMet12Met2_v2._ViaMet12Met2(_DesignParameter=None, _Name='{}:_Pmos_drain_Via1_M1M2'.format(_Name)))[0]

		#Define Cox
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOX'] = 1

		#Define Coy
			#Calculate Number of V1
		M1_ywidth   = self.getYWidth('_Pmos','_Met1Layer')
		Num_V1      = int( ( M1_ywidth - 2 * _DRCobj._Metal1MinEnclosureVia3) / (_DRCobj._VIAxMinWidth + _DRCobj._VIAxMinSpace) ) + 0

			#Define Num of V1
		_Caculation_Parameters['_ViaMet12Met2NumberOfCOY'] = Num_V1

		#M1, M2 and V1 layer XY_width are calculated
		self._DesignParameter['_Pmos_drain_Via1_M1M2']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**_Caculation_Parameters)

		#Cal V1 coord: Source & Drain Zigzag placing
			#initialize coord
		self._DesignParameter['_Pmos_drain_Via1_M1M2']['_XYCoordinates'] = [[0,0]]
			#Define flag
		flag = 1

			#For num of M1 in Pmos
		tmp1 = self.get_param_KJH2('_Pmos','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Pmos_drain_Via1_M1M2','_Met1Layer')

		tmpXY = []
		for i in range(0,len(tmp1)):

			#Source
			if flag == 1:
				tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] ]
				tmpXY.append(tmp3)
				flag = -1
			#Drain
			else:
				tmp3 = [ tmp1[i]['_XY_cent'][0] , tmp1[i]['_XY_cent'][1] + 0.5 * tmp1[0]['_Ywidth'] - 0.5 * tmp2[0]['_Ywidth'] - 64 ]
				tmpXY.append(tmp3)
				flag = +1

		self._DesignParameter['_Pmos_drain_Via1_M1M2']['_XYCoordinates'] = tmpXY
		
		
############################################################################################################################################################ Get_Scoord.

        #Calculate Sref XYcoord
			#initialized Sref coordinate
		self._DesignParameter[' elementname_MovingSref------- ']['_XYCoordinates'] = [[0,0]]  ##########^^^^^^^^^^^^^^^^^^^^^
			#Calculation
		tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
		tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
		tmp3 = self.get_param_KJH2('elementname_MovingSref-------') ##########^^^^^^^^^^^^^^^^^^^^^

		target_coord        = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
		approaching_coord   = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
		Scoord              = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object

		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)

		self._DesignParameter['elementname_MovingSref------']['_XYCoordinates'] = [New_Scoord]  ##########^^^^^^^^^^^^^^^^^^^^^


############################################################################################################################################################ Get_Bcoord.

        #Calculate Boundary_element XYcoord
		tmp1 = self.get_param_KJH2('elementname_Target-----') ##########^^^^^^^^^^^^^^^^^^^^^

		target_coord = tmp1[0]['_XYtype1-----'] ##########^^^^^^^^^^^^^^^^^^^^^_XYtype: _XY_cent,_XY_up_right...
		approaching_type = '_XYtype2-----'      ##########^^^^^^^^^^^^^^^^^^^^^_XYtype: _XY_cent,_XY_up_right...
		B_XWidth = self.getXWidth('elementname_Approaching-----') ##########^^^^^^^^^^^^^^^^^^^^^
		B_YWidth = self.getYWidth('elementname_Approaching-----') ##########^^^^^^^^^^^^^^^^^^^^^

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['elementname_Approaching-----']['_XYCoordinates'] = [New_Bcoord] ##########^^^^^^^^^^^^^^^^^^^^^



############################################################################################################################################################ Get_ovlp_coord.

		#Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH2('elementname_A-----') ##########^^^^^^^^^^^^^^^^^^^^^
		tmp2 = self.get_param_KJH2('elementname_B-----') ##########^^^^^^^^^^^^^^^^^^^^^

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['number1----'],tmp2['number2----']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object



############################################################################################################################################################ Get_Scoord_v2.

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['elementname_MovingSref']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH2('elementname_Target-----')  		##########^^^^^^^^^^^^^^^^^^^^^
        target_coord = tmp1['number1-----']['_XYtype1-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Approaching_coord
        tmp2 = self.get_param_KJH2('elementname_Approaching-----')  ##########^^^^^^^^^^^^^^^^^^^^^
        approaching_coord = tmp2['number2-----']['_XYtype2-----']  ##########2^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object, _XYtype: _XY_cent,_XY_up_right...
                #Sref coord
		tmp3 = self.get_param_KJH2('elementname_MovingSref-------') ##########^^^^^^^^^^^^^^^^^^^^^
		Scoord = tmp3['number3-----']['_XY_cent']  ##########^^^^^^^^^^^^^^^^^^^^^ex) number: choose num from multiple_object
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['elementname_MovingSref------']['_XYCoordinates'] = tmpXY  ##########^^^^^^^^^^^^^^^^^^^^^






############################################################################################################################################################ Get_Scoord_v2.

#Delete
del self._DesignParameter['_Unit_{}'.format(i)]























############################################################################################################################################################ START MAIN
if __name__ == '__main__':

	from Private import MyInfo
	import DRCchecker_KJH0

	libname = ' ----- '  ##########################################################################^^^^^^^^^^^^^^^^^^^^^ex)C_my_building_block
	cellname = ' ----- ' ##########################################################################^^^^^^^^^^^^^^^^^^^^^ex)C01_cap_array_v2_84
	_fileName = cellname + '.gds'

	''' Input Parameters for Layout Object ''' ############################################################### ^^^^^^^^^^^^^^^^^^^^^
	InputParams = dict(


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
	LayoutObj = ' ----- '(_DesignParameter=None, _Name=cellname)  ##########################################^^^^^^^^^^^^^^^^^^^^^^
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
	#Checker.cell_deletion()
	Checker.Upload2FTP()
	Checker.StreamIn(tech=DesignParameters._Technology)
	#Checker_KJH0.DRCchecker()

	print ('#############################      Finished      ################################')
	# end of 'main():' ---------------------------------------------------------------------------------------------
