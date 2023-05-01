'''


'''

from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A00_NMOSWithDummy_v2
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

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B00_polyresparallel
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B01_pmos_sw
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B02_res_and_sw_placement
from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.B_Building_block import B03_ycoord_placement

############################################################################################################################################################ Class_HEADER
class _xcoord_placement(StickDiagram_KJH0._StickDiagram_KJH):

	##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
	#Define input_parameters for Design calculation 
	_ParametersForDesignCalculation = dict(	
											
											#polyres
											_Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
											_Array_Polyres_R_Y_length = [600,800,850,500],
											_Array_Polyres_CoXNum     = [None,None,None,None],
											_Array_Polyres_CoYNum     = [None,None,None,None],
											_Array_Polyres_Dummy      = True,
											_Array_Polyres_N_Parallel = [2,2,1,4],

											#pmos_sw
											_Array_PMOSNumberofGate     = [0, 3, 1, 1],
											_Array_PMOSChannelWidth     = [500, 700, 600, 300],
											_Array_PMOSChannellength    = [30,30,30,30],
											_Array_PMOSDummy            = [True,True,True,True],
											_Array_GateSpacing          = [None,None,None,None],
											_Array_SDWidth              = [None,None,None,None],
											_Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
											_Array_PCCrit               = [None,None,None,None],

											#vtc nbodycontact
											_Array_vtc_btw_res_sw_NbodyContCount_of_Width = [5,3,8,2],

											#hrz nbodycontact
											_Array_hrz_NbodyContCount_of_Width_upper_unit = [4,2,2,3,5],

											#left vtc nbodycontact
											_Left_NbodyContCount_of_Width = 3,

											#left vtc nbodycontact
											_Right_NbodyContCount_of_Width = 7,

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

										#polyres
										_Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
										_Array_Polyres_R_Y_length = [600,800,850,500],
										_Array_Polyres_CoXNum     = [None,None,None,None],
										_Array_Polyres_CoYNum     = [None,None,None,None],
										_Array_Polyres_Dummy      = True,
										_Array_Polyres_N_Parallel = [2,2,1,4],

										#pmos_sw
										_Array_PMOSNumberofGate     = [0, 3, 1, 1],
										_Array_PMOSChannelWidth     = [500, 700, 600, 300],
										_Array_PMOSChannellength    = [30,30,30,30],
										_Array_PMOSDummy            = [True,True,True,True],
										_Array_GateSpacing          = [None,None,None,None],
										_Array_SDWidth              = [None,None,None,None],
										_Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
										_Array_PCCrit               = [None,None,None,None],

										#vtc nbodycontact
										_Array_vtc_btw_res_sw_NbodyContCount_of_Width = [5,3,8,2],

										#hrz nbodycontact
										_Array_hrz_NbodyContCount_of_Width_upper_unit = [4,2,2,3,5],

										#left vtc nbodycontact
										_Left_NbodyContCount_of_Width = 3,

										#left vtc nbodycontact
										_Right_NbodyContCount_of_Width = 7,


									
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



		################################################################################################################################### Array gen
		print('##     Array gen   ##')

		#Define Calculation_Parameters
		_Caculation_Parameters = copy.deepcopy( B03_ycoord_placement._ycoord_placement._ParametersForDesignCalculation)
		_Caculation_Parameters['_Array_Polyres_R_X_width']                        = _Array_Polyres_R_X_width
		_Caculation_Parameters['_Array_Polyres_R_Y_length']                       = _Array_Polyres_R_Y_length
		_Caculation_Parameters['_Array_Polyres_CoXNum']                           = _Array_Polyres_CoXNum
		_Caculation_Parameters['_Array_Polyres_CoYNum']                           = _Array_Polyres_CoYNum
		_Caculation_Parameters['_Array_Polyres_Dummy']                            = _Array_Polyres_Dummy
		_Caculation_Parameters['_Array_Polyres_N_Parallel']                       = _Array_Polyres_N_Parallel
		_Caculation_Parameters['_Array_PMOSNumberofGate']                         = _Array_PMOSNumberofGate
		_Caculation_Parameters['_Array_PMOSChannelWidth']                         = _Array_PMOSChannelWidth
		_Caculation_Parameters['_Array_PMOSChannellength']                        = _Array_PMOSChannellength
		_Caculation_Parameters['_Array_PMOSDummy']                                = _Array_PMOSDummy
		_Caculation_Parameters['_Array_GateSpacing']                              = _Array_GateSpacing
		_Caculation_Parameters['_Array_SDWidth']                                  = _Array_SDWidth
		_Caculation_Parameters['_Array_XVT']                                      = _Array_XVT
		_Caculation_Parameters['_Array_PCCrit']                                   = _Array_PCCrit
		_Caculation_Parameters['_Array_vtc_btw_res_sw_NbodyContCount_of_Width']   = _Array_vtc_btw_res_sw_NbodyContCount_of_Width
		_Caculation_Parameters['_Array_hrz_NbodyContCount_of_Width_upper_unit']   = _Array_hrz_NbodyContCount_of_Width_upper_unit

		#Generate Sref
		self._DesignParameter['_Array'] = self._SrefElementDeclaration(_DesignObj=B03_ycoord_placement._ycoord_placement( _DesignParameter=None, _Name='{}:_Array'.format(_Name)))[0]

		#Define Sref Relection
		self._DesignParameter['_Array']['_Reflect'] = [0, 0, 0]

		#Define Sref Angle
		self._DesignParameter['_Array']['_Angle'] = 0

		#Calculate Sref Layer by using Calculation_Parameter
		self._DesignParameter['_Array']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

		#Define Sref _XYcoordinate
		self._DesignParameter['_Array']['_XYCoordinates']=[[0, 0]]

		################################################################################################################################### gen left nbodycontact column
		print('##     gen left nbodycontact column   ##')
			##################################################################################################################### gen left nbodycontact column:cal ylength
		print('##     gen left nbodycontact column:cal ylength   ##')

		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_Met1Layer')

		ylength = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1])

			##################################################################################################################### gen left nbodycontact column:gen Nbodycontact
		print('##     gen left nbodycontact column:gen Nbodycontact   ##')

		left_NbodyCont_Length = ylength
		#If vertical
		_NbodyContact_NumberOfNbodyCOX = _Left_NbodyContCount_of_Width
		_NbodyContact_NumberOfNbodyCOY = (int(((left_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Left_NbodyContCount_of_Width) + 0
		_NbodyContact_Met1XWidth       = None
		_NbodyContact_Met1YWidth       = None
		
		#Define _NbodyContact input parameter
		_Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
		_Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
		_Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
		_Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
		_Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

		#Define _NbodyContact Sref
		self._DesignParameter['_Left_nbodycontact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Left_nbodycontact'.format(_Name) ))[0] 

		#Define _NbodyContact Sref Relection
		self._DesignParameter['_Left_nbodycontact']['_Reflect'] = [0, 0, 0]

		#Define _NbodyContact Sref Angle
		self._DesignParameter['_Left_nbodycontact']['_Angle'] = 0

		#Define _NbodyContact layer
		self._DesignParameter['_Left_nbodycontact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters) 

		#Define _NbodyContact coordinate
			#place _Nbodycontact ycoord between ...
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_Met1Layer')

		ycoord_tmp = 0.5 *  ( tmp1[0]['_XY_cent'][1] + tmp2[0]['_XY_cent'][1] )

		#Calculate Sref XYcoord
			#initialized Sref coordinate
		self._DesignParameter['_Left_nbodycontact']['_XYCoordinates'] = [[0,0]]  
			#Calculation
		tmp2 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')  
		tmp3 = self.get_param_KJH2('_Left_nbodycontact') 

		target_coord        = ycoord_tmp
		approaching_coord   = tmp2[0]['_XY_cent'] 
		Scoord              = tmp3[0]['_XY_cent'] 

		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

		self._DesignParameter['_Left_nbodycontact']['_XYCoordinates'] = [New_Scoord] 

		#Define NWELL of _NbodyContact
		self._DesignParameter['_Left_nbodycontact_Nwell'] = self._BoundaryElementDeclaration( 
																											_Layer=DesignParameters._LayerMapping['NWELL'][0],
																											_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																											_XWidth=None,
																											_YWidth=None,
																											_XYCoordinates=[ ],
																										  ) 
		
		#Define NWELL Xwidth
		self._DesignParameter['_Left_nbodycontact_Nwell']['_XWidth'] = self.getXWidth('_Left_nbodycontact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 

		#Define NWELL Ywidth
		self._DesignParameter['_Left_nbodycontact_Nwell']['_YWidth'] = self.getYWidth('_Left_nbodycontact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 
		
		#Define NWELL Coordinates
		self._DesignParameter['_Left_nbodycontact_Nwell']['_XYCoordinates'] =  self.getXY('_Left_nbodycontact') 

		################################################################################################################################### Cal xcoord of Hrz_nobodycontact of Array
		print('##     Cal Hrz_nobodycontact of Array   ##')

		#Pre-defined
		xdistance = 300

		#+1 for up Nbodycontact
		for i in range(0,len(_Array_PMOSNumberofGate)+1):
			#Calculate Sref XYcoord
				#Calculation
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')
			tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
			tmp3 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i))

			target_coord        = tmp1[0]['_XY_right']
			approaching_coord   = tmp2[0]['_XY_left']
			Scoord              = tmp3[0]['_XY_cent']

			New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
			New_Scoord[0] =  New_Scoord[0] + xdistance

			self._DesignParameter['_Array']['_DesignObj']._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_XYCoordinates'][0][0] = New_Scoord[0]

		################################################################################################################################### Cal xcoord of _Unit of _Array
		print('##     Cal xcoord of _Unit of _Array   ##')

		#Pre-defined
		xdistance_unit = 250

		for i in range(0,len(_Array_PMOSNumberofGate)):
			#Calculate Sref XYcoord
				#Calculation
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')
			tmp2 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')
			tmp3 = self.get_param_KJH2('_Array','_Unit_{}'.format(i))

			target_coord        = tmp1[0]['_XY_right']
			approaching_coord   = tmp2[0]['_XY_up']
			Scoord              = tmp3[0]['_XY_cent']

			New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
			New_Scoord[0] =  New_Scoord[0] + xdistance_unit

			self._DesignParameter['_Array']['_DesignObj']._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates'][0][0] = New_Scoord[0]

		################################################################################################################################### gen right nbodycontact column:gen Nbodycontact
		print('##     gen right nbodycontact column:gen Nbodycontact   ##')

		#pre-defined
		xdistance_tmp = 200

		right_NbodyCont_Length = ylength
		#If vertical
		_NbodyContact_NumberOfNbodyCOX = _Right_NbodyContCount_of_Width
		_NbodyContact_NumberOfNbodyCOY = (int(((right_NbodyCont_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Right_NbodyContCount_of_Width) + 0
		_NbodyContact_Met1XWidth       = None
		_NbodyContact_Met1YWidth       = None
		
		#Define _NbodyContact input parameter
		_Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
		_Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
		_Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
		_Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
		_Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

		#Define _NbodyContact Sref
		self._DesignParameter['_Right_nbodycontact'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Right_nbodycontact'.format(_Name) ))[0] 

		#Define _NbodyContact Sref Relection
		self._DesignParameter['_Right_nbodycontact']['_Reflect'] = [0, 0, 0]

		#Define _NbodyContact Sref Angle
		self._DesignParameter['_Right_nbodycontact']['_Angle'] = 0

		#Define _NbodyContact layer
		self._DesignParameter['_Right_nbodycontact']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters) 

		#Define _NbodyContact coordinate
			#Cal ycoord
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_Met1Layer')

		ycoord_tmp = 0.5 *  ( tmp1[0]['_XY_cent'][1] + tmp2[0]['_XY_cent'][1] )
				#Calculate Sref XYcoord
					#initialized Sref coordinate
		self._DesignParameter['_Right_nbodycontact']['_XYCoordinates'] = [[0,0]]  
					#Calculation
		tmp2 = self.get_param_KJH2('_Right_nbodycontact','_Met1Layer')  
		tmp3 = self.get_param_KJH2('_Right_nbodycontact') 

		target_coord        = ycoord_tmp
		approaching_coord   = tmp2[0]['_XY_cent'] 
		Scoord              = tmp3[0]['_XY_cent'] 

		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

		self._DesignParameter['_Right_nbodycontact']['_XYCoordinates'] = [New_Scoord] 
			#Cal xcoord
				#Find the right most coordinates
		for i in range(0,len(_Array_PMOSNumberofGate)):
					#Polyres only
			if _Array_PMOSNumberofGate[i] == 0:
				tmp = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')

					#if no resistor parallelized
				if len(tmp) == 1:
					_Unit_xlength = abs( tmp[0]['_XY_up'][0] - tmp[0]['_XY_down'][0] )

				else:
					_Unit_xlength = abs( tmp[0]['_XY_up'][0] - tmp[-1]['_XY_down'][0] )

					#Polyres-Nbody-sw
			else:
				tmp1 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')
				tmp2 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_PODummyLayer')

				_Unit_xlength = abs ( tmp1[0]['_XY_up'][0] - tmp2[-1]['_XY_right'][0] )

				################################################################################################################### Define Xlength
			print('##     Define Xlength   ##')

			if i == 0:
				longest_unit = 0
				Xlength = _Unit_xlength
			else:

				if Xlength > _Unit_xlength:
					Xlength = Xlength
					longest_unit = longest_unit
				else:
					Xlength = _Unit_xlength
					longest_unit = i

				#Calculate Sref XYcoord
					#Calculation
						#Target coord
		if _Array_PMOSNumberofGate[longest_unit] == 0:
			tmp1 = self.get_param_KJH2('_Array','_Unit_{}'.format(longest_unit),'_Polyres','_Polyres','PRES_boundary_0')
			target_coord = tmp1[-1]['_XY_down']
		else:
			tmp1 = self.get_param_KJH2('_Array','_Unit_{}'.format(longest_unit),'_Pmos_sw','_Pmos','_PODummyLayer')
			target_coord = tmp1[-1]['_XY_right']

		tmp2 = self.get_param_KJH2('_Right_nbodycontact','_Met1Layer')  
		tmp3 = self.get_param_KJH2('_Right_nbodycontact') 

		approaching_coord   = tmp2[0]['_XY_left'] 
		Scoord              = tmp3[0]['_XY_cent'] 

		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
		New_Scoord[0] = New_Scoord[0] + xdistance_tmp

		self._DesignParameter['_Right_nbodycontact']['_XYCoordinates'][0][0] = New_Scoord[0]


		#Define NWELL of _NbodyContact
		self._DesignParameter['_Right_nbodycontact_Nwell'] = self._BoundaryElementDeclaration( 
																											_Layer=DesignParameters._LayerMapping['NWELL'][0],
																											_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																											_XWidth=None,
																											_YWidth=None,
																											_XYCoordinates=[ ],
																										  ) 
		
		#Define NWELL Xwidth
		self._DesignParameter['_Right_nbodycontact_Nwell']['_XWidth'] = self.getXWidth('_Right_nbodycontact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 

		#Define NWELL Ywidth
		self._DesignParameter['_Right_nbodycontact_Nwell']['_YWidth'] = self.getYWidth('_Right_nbodycontact','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2 
		
		#Define NWELL Coordinates
		self._DesignParameter['_Right_nbodycontact_Nwell']['_XYCoordinates'] =  self.getXY('_Right_nbodycontact') 



		################################################################################################################################### make ring by extending Nbody
		print('##     make ring by extending Nbody   ##')
			##################################################################################################################### make ring by extending Nbody:outer ring
		print('##     make ring by extending Nbody:outer ring  ##')
				####################################################################################################### make ring by extending Nbody:outer ring:left
		print('##     make ring by extending Nbody:outer ring:left up  ##')

		#Define DIFF
		self._DesignParameter['_Left_diff'] = self._BoundaryElementDeclaration(
																			_Layer=DesignParameters._LayerMapping['DIFF'][0],
																			_Datatype=DesignParameters._LayerMapping['DIFF'][1],
																			_XWidth=None,
																			_YWidth=None,
																			_XYCoordinates=[ ],
																		   )

			#Define Boundary_element _YWidth
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_ODLayer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_ODLayer')
		self._DesignParameter['_Left_diff']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

			#Define Boundary_element _XWidth
		tmp3 = self.get_param_KJH2('_Left_nbodycontact','_ODLayer')
		self._DesignParameter['_Left_diff']['_XWidth'] = tmp3[0]['_Xwidth']

			#Define Boundary_element _XYCoordinates
				#Calculate Xcoord
		tmp4 = self.get_param_KJH2('_Left_nbodycontact','_ODLayer')
		self._DesignParameter['_Left_diff']['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

				#Calculate Ycoord
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_ODLayer')

		target_coord = tmp1[0]['_XY_up']
		approaching_type = '_XY_up'    
		B_XWidth = self.getXWidth('_Left_diff')
		B_YWidth = self.getYWidth('_Left_diff')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Left_diff']['_XYCoordinates'][0][1] = New_Bcoord[1]

		#Define METAL1
		self._DesignParameter['_Left_metal1'] = self._BoundaryElementDeclaration(
																			_Layer=DesignParameters._LayerMapping['METAL1'][0],
																			_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																			_XWidth=None,
																			_YWidth=None,
																			_XYCoordinates=[ ],
																		   )

			#Define Boundary_element _YWidth
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_Met1Layer')
		self._DesignParameter['_Left_metal1']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

			#Define Boundary_element _XWidth
		tmp3 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')
		self._DesignParameter['_Left_metal1']['_XWidth'] = tmp3[0]['_Xwidth']

			#Define Boundary_element _XYCoordinates
				#Calculate Xcoord
		tmp4 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')
		self._DesignParameter['_Left_metal1']['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

				#Calculate Ycoord
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')

		target_coord = tmp1[0]['_XY_up']
		approaching_type = '_XY_up'    
		B_XWidth = self.getXWidth('_Left_metal1')
		B_YWidth = self.getYWidth('_Left_metal1')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Left_metal1']['_XYCoordinates'][0][1] = New_Bcoord[1]


				####################################################################################################### make ring by extending Nbody:outer ring:right
		print('##     make ring by extending Nbody:outer ring:right up ##')

		#Define DIFF
		self._DesignParameter['_Right_diff'] = self._BoundaryElementDeclaration(
																			_Layer=DesignParameters._LayerMapping['DIFF'][0],
																			_Datatype=DesignParameters._LayerMapping['DIFF'][1],
																			_XWidth=None,
																			_YWidth=None,
																			_XYCoordinates=[ ],
																		   )

			#Define Boundary_element _YWidth
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_ODLayer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_ODLayer')
		self._DesignParameter['_Right_diff']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

			#Define Boundary_element _XWidth
		tmp3 = self.get_param_KJH2('_Right_nbodycontact','_ODLayer')
		self._DesignParameter['_Right_diff']['_XWidth'] = tmp3[0]['_Xwidth']

			#Define Boundary_element _XYCoordinates
				#Calculate Xcoord
		tmp4 = self.get_param_KJH2('_Right_nbodycontact','_ODLayer')
		self._DesignParameter['_Right_diff']['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

				#Calculate Ycoord
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_ODLayer')

		target_coord = tmp1[0]['_XY_up']
		approaching_type = '_XY_up'    
		B_XWidth = self.getXWidth('_Right_diff')
		B_YWidth = self.getYWidth('_Right_diff')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Right_diff']['_XYCoordinates'][0][1] = New_Bcoord[1]

		#Define METAL1
		self._DesignParameter['_Right_metal1'] = self._BoundaryElementDeclaration(
																			_Layer=DesignParameters._LayerMapping['METAL1'][0],
																			_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																			_XWidth=None,
																			_YWidth=None,
																			_XYCoordinates=[ ],
																		   )

			#Define Boundary_element _YWidth
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(len(_Array_PMOSNumberofGate)),'_Met1Layer')
		self._DesignParameter['_Right_metal1']['_YWidth'] = abs( tmp1[0]['_XY_up'][1] - tmp2[0]['_XY_down'][1] )

			#Define Boundary_element _XWidth
		tmp3 = self.get_param_KJH2('_Right_nbodycontact','_Met1Layer')
		self._DesignParameter['_Right_metal1']['_XWidth'] = tmp3[0]['_Xwidth']

			#Define Boundary_element _XYCoordinates
				#Calculate Xcoord
		tmp4 = self.get_param_KJH2('_Right_nbodycontact','_Met1Layer')
		self._DesignParameter['_Right_metal1']['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

				#Calculate Ycoord
		tmp1 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0','_Met1Layer')

		target_coord = tmp1[0]['_XY_up']
		approaching_type = '_XY_up'    
		B_XWidth = self.getXWidth('_Right_metal1')
		B_YWidth = self.getYWidth('_Right_metal1')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Right_metal1']['_XYCoordinates'][0][1] = New_Bcoord[1]

				####################################################################################################### make ring by extending Nbody: inner hrz
		print('##     make ring by extending Nbody:outer ring:right down  ##')

		for i in range(0,len(_Array_PMOSNumberofGate)+1):
			#Define DIFF
			self._DesignParameter['_Up_diff_{}'.format(i)] = self._BoundaryElementDeclaration(
																				_Layer=DesignParameters._LayerMapping['DIFF'][0],
																				_Datatype=DesignParameters._LayerMapping['DIFF'][1],
																				_XWidth=None,
																				_YWidth=None,
																				_XYCoordinates=[ ],
																			   )

				#Define Boundary_element _YWidth
			tmp3 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_ODLayer')
			self._DesignParameter['_Up_diff_{}'.format(i)]['_YWidth'] = tmp3[0]['_Ywidth']

				#Define Boundary_element _XWidth
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_ODLayer')
			tmp2 = self.get_param_KJH2('_Right_nbodycontact','_ODLayer')
			self._DesignParameter['_Up_diff_{}'.format(i)]['_XWidth'] = abs( tmp1[0]['_XY_left'][0] - tmp2[0]['_XY_right'][0] )

				#Define Boundary_element _XYCoordinates
					#Calculate Ycoord
			tmp4 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_ODLayer')
			self._DesignParameter['_Up_diff_{}'.format(i)]['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

					#Calculate Xcoord
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_ODLayer')

			target_coord = tmp1[0]['_XY_left']
			approaching_type = '_XY_left'
			B_XWidth = self.getXWidth('_Up_diff_{}'.format(i))
			B_YWidth = self.getYWidth('_Up_diff_{}'.format(i))

			New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

			self._DesignParameter['_Up_diff_{}'.format(i)]['_XYCoordinates'][0][0] = New_Bcoord[0]

			#Define METAL1
			self._DesignParameter['_Up_metal1_{}'.format(i)] = self._BoundaryElementDeclaration(
																				_Layer=DesignParameters._LayerMapping['METAL1'][0],
																				_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																				_XWidth=None,
																				_YWidth=None,
																				_XYCoordinates=[ ],
																			   )

				#Define Boundary_element _YWidth
			tmp3 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
			self._DesignParameter['_Up_metal1_{}'.format(i)]['_YWidth'] = tmp3[0]['_Ywidth']

				#Define Boundary_element _XWidth
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')
			tmp2 = self.get_param_KJH2('_Right_nbodycontact','_Met1Layer')
			self._DesignParameter['_Up_metal1_{}'.format(i)]['_XWidth'] = abs( tmp1[0]['_XY_left'][0] - tmp2[0]['_XY_right'][0] )

				#Define Boundary_element _XYCoordinates
					#Calculate Ycoord
			tmp4 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
			self._DesignParameter['_Up_metal1_{}'.format(i)]['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

					#Calculate Xcoord
			tmp1 = self.get_param_KJH2('_Left_nbodycontact','_Met1Layer')

			target_coord = tmp1[0]['_XY_left']
			approaching_type = '_XY_left'
			B_XWidth = self.getXWidth('_Up_metal1_{}'.format(i))
			B_YWidth = self.getYWidth('_Up_metal1_{}'.format(i))

			New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

			self._DesignParameter['_Up_metal1_{}'.format(i)]['_XYCoordinates'][0][0] = New_Bcoord[0]

			##################################################################################################################### make ring by extending Nbody:inner vtc
		print('##     make ring by extending Nbody:inner vtc   ##')

		for i in range(0,len(_Array_PMOSNumberofGate)):

			#resistor only
			if _Array_PMOSNumberofGate[i]==0:
				pass

			#resistor with switch
			else:


				#Define DIFF
				self._DesignParameter['_Vtc_diff_{}'.format(i)] = self._BoundaryElementDeclaration(
																					_Layer=DesignParameters._LayerMapping['DIFF'][0],
																					_Datatype=DesignParameters._LayerMapping['DIFF'][1],
																					_XWidth=None,
																					_YWidth=None,
																					_XYCoordinates=[ ],
																				   )

					#Define Boundary_element _XWidth
				tmp3 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Vtc_nbodycontact_btw_res_sw','_ODLayer')
				self._DesignParameter['_Vtc_diff_{}'.format(i)]['_XWidth'] = tmp3[0]['_Xwidth']

					#Define Boundary_element _YWidth
				tmp1 = self.get_param_KJH2('_Up_diff_{}'.format(i))
				tmp2 = self.get_param_KJH2('_Up_diff_{}'.format(i+1))
				self._DesignParameter['_Vtc_diff_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1] )

					#Define Boundary_element _XYCoordinates
						#Calculate Xcoord
				tmp4 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Vtc_nbodycontact_btw_res_sw','_ODLayer')
				self._DesignParameter['_Vtc_diff_{}'.format(i)]['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

						#Calculate Ycoord
				tmp1 = self.get_param_KJH2('_Up_diff_{}'.format(i))

				target_coord = tmp1[0]['_XY_down']
				approaching_type = '_XY_up'
				B_XWidth = self.getXWidth('_Vtc_diff_{}'.format(i))
				B_YWidth = self.getYWidth('_Vtc_diff_{}'.format(i))

				New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

				self._DesignParameter['_Vtc_diff_{}'.format(i)]['_XYCoordinates'][0][1] = New_Bcoord[1]

				#Define Metal1
				self._DesignParameter['_Vtc_metal1_{}'.format(i)] = self._BoundaryElementDeclaration(
																					_Layer=DesignParameters._LayerMapping['METAL1'][0],
																					_Datatype=DesignParameters._LayerMapping['METAL1'][1],
																					_XWidth=None,
																					_YWidth=None,
																					_XYCoordinates=[ ],
																				   )

					#Define Boundary_element _XWidth
				tmp3 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Vtc_nbodycontact_btw_res_sw','_Met1Layer')
				self._DesignParameter['_Vtc_metal1_{}'.format(i)]['_XWidth'] = tmp3[0]['_Xwidth']

					#Define Boundary_element _YWidth
				tmp1 = self.get_param_KJH2('_Up_metal1_{}'.format(i))
				tmp2 = self.get_param_KJH2('_Up_metal1_{}'.format(i+1))
				self._DesignParameter['_Vtc_metal1_{}'.format(i)]['_YWidth'] = abs( tmp1[0]['_XY_down'][1] - tmp2[0]['_XY_up'][1] )

					#Define Boundary_element _XYCoordinates
						#Calculate Xcoord
				tmp4 = self.get_param_KJH2('_Array','_Unit_{}'.format(i),'_Vtc_nbodycontact_btw_res_sw','_Met1Layer')
				self._DesignParameter['_Vtc_metal1_{}'.format(i)]['_XYCoordinates'] = [ tmp4[0]['_XY_cent']]

						#Calculate Ycoord
				tmp1 = self.get_param_KJH2('_Up_metal1_{}'.format(i))

				target_coord = tmp1[0]['_XY_down']
				approaching_type = '_XY_up'
				B_XWidth = self.getXWidth('_Vtc_metal1_{}'.format(i))
				B_YWidth = self.getYWidth('_Vtc_metal1_{}'.format(i))

				New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

				self._DesignParameter['_Vtc_metal1_{}'.format(i)]['_XYCoordinates'][0][1] = New_Bcoord[1]

		################################################################################################################################### Nwell covering
		print('##     Nwell covering  ##')

		#Define NWELL
		self._DesignParameter['_Nwell_covering'] = self._BoundaryElementDeclaration(
																							_Layer=DesignParameters._LayerMapping['NWELL'][0],
																							_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																							_XWidth=None,
																							_YWidth=None,
																							_XYCoordinates=[ ],
																					)

		#Define Xwidth
		tmp1 = self.get_param_KJH2('_Left_nbodycontact_Nwell')
		tmp2 = self.get_param_KJH2('_Right_nbodycontact_Nwell')
		self._DesignParameter['_Nwell_covering']['_XWidth'] = abs(tmp1[0]['_XY_left'][0] - tmp2[0]['_XY_right'][0])

		#Define Ywidth
		zzzz = len(_Array_PMOSNumberofGate)
		tmp3 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0_nwell')
		tmp4 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_{}_nwell'.format(len(_Array_PMOSNumberofGate)))
		self._DesignParameter['_Nwell_covering']['_YWidth'] = abs(tmp3[0]['_XY_up'][1] - tmp4[0]['_XY_down'][1])

		#Define Coordinates
			#initialization
		self._DesignParameter['_Nwell_covering']['_XYCoordinates'] = [[0,0]]
			#Calculate Xcoord
		tmp1 = self.get_param_KJH2('_Left_nbodycontact_Nwell')

		target_coord = tmp1[0]['_XY_left']
		approaching_type = '_XY_left'
		B_XWidth = self.getXWidth('_Nwell_covering')
		B_YWidth = self.getYWidth('_Nwell_covering')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Nwell_covering']['_XYCoordinates'][0][0] = New_Bcoord[0]

			#Calculate Ycoord
		tmp2 = self.get_param_KJH2('_Array','_Hrz_nbodycontact_upper_unit_0_nwell')

		target_coord = tmp2[0]['_XY_up']
		approaching_type = '_XY_up'
		B_XWidth = self.getXWidth('_Nwell_covering')
		B_YWidth = self.getYWidth('_Nwell_covering')

		New_Bcoord = self.get_Bcoord_KJH(target_coord,approaching_type,B_XWidth,B_YWidth)

		self._DesignParameter['_Nwell_covering']['_XYCoordinates'][0][1] = New_Bcoord[1]


		print('###############      For Debugging      ##################')


		#Delete
		#del self._DesignParameter['_Polyres_for_coordcal']


############################################################################################################################################################ CALCULATION END
		print ('#########################################################################################################')
		print ('                                      Calculation   END                                                  ')
		print ('#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

	from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
	from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

	libname = 'Proj_VGA_B_building_block'
	cellname = 'B04_xcoord_placement_99'
	_fileName = cellname + '.gds'

	''' Input Parameters for Layout Object '''
	InputParams = dict(
							#polyres
							_Array_Polyres_R_X_width  = [1000, 1000, 1500, 2000,],
							_Array_Polyres_R_Y_length = [600,800,850,500],
							_Array_Polyres_CoXNum     = [None,None,None,None],
							_Array_Polyres_CoYNum     = [None,None,None,None],
							_Array_Polyres_Dummy      = True,
							_Array_Polyres_N_Parallel = [2,2,1,4],

							#pmos_sw
							_Array_PMOSNumberofGate     = [0, 3, 0, 1],
							_Array_PMOSChannelWidth     = [500, 700, 600, 400],
							_Array_PMOSChannellength    = [30,30,30,80],
							_Array_PMOSDummy            = [True,True,True,True],
							_Array_GateSpacing          = [None,None,None,None],
							_Array_SDWidth              = [None,None,None,None],
							_Array_XVT                  = ['SLVT','SLVT','SLVT','SLVT'],
							_Array_PCCrit               = [None,None,None,None],

							#vtc nbodycontact
							_Array_vtc_btw_res_sw_NbodyContCount_of_Width = [5,3,8,2],

							#hrz nbodycontact
							_Array_hrz_NbodyContCount_of_Width_upper_unit = [4,2,2,3,5],

							#left vtc nbodycontact
							_Left_NbodyContCount_of_Width = 3,

							#left vtc nbodycontact
							_Right_NbodyContCount_of_Width = 7,
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
	LayoutObj = _xcoord_placement(_DesignParameter=None, _Name=cellname)
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
	#Checker_KJH0.DRCchecker()

	print ('#############################      Finished      ################################')
	# end of 'main():' ---------------------------------------------------------------------------------------------
