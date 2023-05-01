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

############################################################################################################################################################ Class_HEADER
class _ycoord_placement(StickDiagram_KJH0._StickDiagram_KJH):

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


		#################################################################################################################################################### Calculate Xlength(ring hrz nbody length)
		for i in range(0,len(_Array_PMOSNumberofGate)):

			################################################################################################################################### Unit Generation for cal
			print('##     Unit Generation   ##')

			#Define Calculation_Parameters
			_Caculation_Parameters = copy.deepcopy( B02_res_and_sw_placement._res_and_sw_placement._ParametersForDesignCalculation)
			_Caculation_Parameters['_Polyres_R_X_width']                        = _Array_Polyres_R_X_width[i]
			_Caculation_Parameters['_Polyres_R_Y_length']                       = _Array_Polyres_R_Y_length[i]
			_Caculation_Parameters['_Polyres_CoXNum']                           = _Array_Polyres_CoXNum[i]
			_Caculation_Parameters['_Polyres_CoYNum']                           = _Array_Polyres_CoYNum[i]
			_Caculation_Parameters['_Polyres_Dummy']                            = _Array_Polyres_Dummy
			_Caculation_Parameters['_Polyres_N_Parallel']                       = _Array_Polyres_N_Parallel[i]
			_Caculation_Parameters['_PMOSNumberofGate']                         = _Array_PMOSNumberofGate[i]
			_Caculation_Parameters['_PMOSChannelWidth']                         = _Array_PMOSChannelWidth[i]
			_Caculation_Parameters['_PMOSChannellength']                        = _Array_PMOSChannellength[i]
			_Caculation_Parameters['_PMOSDummy']                                = _Array_PMOSDummy[i]
			_Caculation_Parameters['_GateSpacing']                              = _Array_GateSpacing[i]
			_Caculation_Parameters['_SDWidth']                                  = _Array_SDWidth[i]
			_Caculation_Parameters['_XVT']                                      = _Array_XVT[i]
			_Caculation_Parameters['_PCCrit']                                   = _Array_PCCrit[i]
			_Caculation_Parameters['_vtc_btw_res_sw_NbodyContCount_of_Width']   = _Array_vtc_btw_res_sw_NbodyContCount_of_Width[i]

			#Generate Sref
			self._DesignParameter['_Unit_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=B02_res_and_sw_placement._res_and_sw_placement( _DesignParameter=None, _Name='{}:_Unit_{}'.format(_Name,i)))[0]

			#Define Sref Relection
			self._DesignParameter['_Unit_{}'.format(i)]['_Reflect'] = [0, 0, 0]

			#Define Sref Angle
			self._DesignParameter['_Unit_{}'.format(i)]['_Angle'] = 0

			#Calculate Sref Layer by using Calculation_Parameter
			self._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

			#Define Sref _XYcoordinate
			self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates']=[[0, 0]]

			################################################################################################################################### Cal Unit length and define Xlength
			print('##     Cal Unit length   ##')
				################################################################################################################### Cal Unit length
			print('##     Cal Unit length   ##')

			#Polyres only
			if _Array_PMOSNumberofGate[i] == 0:
				tmp = self.get_param_KJH2('_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')

				#if no resistor parallelized
				if len(tmp) == 1:
					_Unit_xlength = abs( tmp[0]['_XY_up'][0] - tmp[0]['_XY_down'][0] )

				else:
					_Unit_xlength = abs( tmp[0]['_XY_up'][0] - tmp[-1]['_XY_down'][0] )

			#Polyres-Nbody-sw
			else:
				tmp1 = self.get_param_KJH2('_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')
				tmp2 = self.get_param_KJH2('_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_PODummyLayer')

				_Unit_xlength = abs ( tmp1[0]['_XY_up'][0] - tmp2[-1]['_XY_right'][0] )

				################################################################################################################### Define Xlength
			print('##     Define Xlength   ##')

			if i == 0:
				Xlength = _Unit_xlength
			else:

				if Xlength > _Unit_xlength:
					Xlength = Xlength
				else:
					Xlength = _Unit_xlength

			#Delete
			del self._DesignParameter['_Unit_{}'.format(i)]



		#################################################################################################################################################### Ycoord placement
		print('##     Define Xlength   ##')

		#Pre-defined
		Ydistance = 300

		#+1 for up Nbodycontact
		for i in range(0,len(_Array_PMOSNumberofGate)+1):

			################################################################################################################################### Nbodygeneration
			#Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
			_Hrz_nbodycont_length_upper_unit_ = Xlength
			#If horizontal
			_NbodyContact_NumberOfNbodyCOX = (int(((_Hrz_nbodycont_length_upper_unit_ - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _Array_hrz_NbodyContCount_of_Width_upper_unit[i]) + 0
			_NbodyContact_NumberOfNbodyCOY = _Array_hrz_NbodyContCount_of_Width_upper_unit[i]
			_NbodyContact_Met1XWidth       = None
			_NbodyContact_Met1YWidth       = None

			#Define _NbodyContact input parameter
			_Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
			_Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
			_Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
			_Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
			_Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

			#Define _NbodyContact Sref
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Hrz_nbodycontact_upper_unit_{}'.format(_Name,i) ))[0]

			#Define _NbodyContact Sref Relection
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_Reflect'] = [0, 0, 0]

			#Define _NbodyContact Sref Angle
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_Angle'] = 0

			#Define _NbodyContact layer
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

			#Define _NbodyContact XYcoordinates
				#first
			if i==0:
				self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
				#
			else:
				#target_coord
				if _Array_PMOSNumberofGate[i-1] == 0:
					tmp1 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Polyres','_Polyres','PRES_boundary_0')
					target_coord = tmp1[0]['_XY_left']
					#resistor with sw
				else:
					tmp2 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Polyres','_Polyres','PRES_boundary_0')
					tmp3 = self.get_param_KJH2('_Unit_{}'.format(i-1),'_Pmos_sw','_Pmos','_PODummyLayer')

					#check which one is lower
					if tmp2[0]['_XY_left'][1] > tmp3[0]['_XY_down'][1]:
						target_coord = tmp3[0]['_XY_down']
					else:
						target_coord = tmp2[0]['_XY_left']

				#Initialization
				self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_XYCoordinates'] = [[0,0]]

				#Approaching_coord
				tmp4 = self.get_param_KJH2('_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer',)
				approaching_coord = tmp4[0]['_XY_up']

				#Scoord
				tmp5 = self.get_param_KJH2('_Hrz_nbodycontact_upper_unit_{}'.format(i))
				Scoord = tmp5[0]['_XY_cent']

				New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

				#Ydistance
				New_Scoord[1] = New_Scoord[1] - Ydistance

				self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}'.format(i)]['_XYCoordinates'] = [New_Scoord]

			#Define NWELL of _NbodyContact
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}_nwell'.format(i)] = self._BoundaryElementDeclaration(
																												_Layer=DesignParameters._LayerMapping['NWELL'][0],
																												_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																												_XWidth=None,
																												_YWidth=None,
																												_XYCoordinates=[ ],
																											  )

			#Define NWELL Xwidth
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}_nwell'.format(i)]['_XWidth'] = self.getXWidth('_Hrz_nbodycontact_upper_unit_{}'.format(i),'_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

			#Define NWELL Ywidth
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}_nwell'.format(i)]['_YWidth'] = self.getYWidth('_Hrz_nbodycontact_upper_unit_{}'.format(i),'_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

			#Define NWELL Coordinates
			self._DesignParameter['_Hrz_nbodycontact_upper_unit_{}_nwell'.format(i)]['_XYCoordinates'] =  self.getXY('_Hrz_nbodycontact_upper_unit_{}'.format(i))

			################################################################################################################################### Unit Generation
			print('##     Unit Generation   ##')    
			if i == len(_Array_PMOSNumberofGate):
				pass
			else:

				#Define Calculation_Parameters
				_Caculation_Parameters = copy.deepcopy( B02_res_and_sw_placement._res_and_sw_placement._ParametersForDesignCalculation)
				_Caculation_Parameters['_Polyres_R_X_width']                        = _Array_Polyres_R_X_width[i]
				_Caculation_Parameters['_Polyres_R_Y_length']                       = _Array_Polyres_R_Y_length[i]
				_Caculation_Parameters['_Polyres_CoXNum']                           = _Array_Polyres_CoXNum[i]
				_Caculation_Parameters['_Polyres_CoYNum']                           = _Array_Polyres_CoYNum[i]
				_Caculation_Parameters['_Polyres_Dummy']                            = _Array_Polyres_Dummy
				_Caculation_Parameters['_Polyres_N_Parallel']                       = _Array_Polyres_N_Parallel[i]
				_Caculation_Parameters['_PMOSNumberofGate']                         = _Array_PMOSNumberofGate[i]
				_Caculation_Parameters['_PMOSChannelWidth']                         = _Array_PMOSChannelWidth[i]
				_Caculation_Parameters['_PMOSChannellength']                        = _Array_PMOSChannellength[i]
				_Caculation_Parameters['_PMOSDummy']                                = _Array_PMOSDummy[i]
				_Caculation_Parameters['_GateSpacing']                              = _Array_GateSpacing[i]
				_Caculation_Parameters['_SDWidth']                                  = _Array_SDWidth[i]
				_Caculation_Parameters['_XVT']                                      = _Array_XVT[i]
				_Caculation_Parameters['_PCCrit']                                   = _Array_PCCrit[i]
				_Caculation_Parameters['_vtc_btw_res_sw_NbodyContCount_of_Width']   = _Array_vtc_btw_res_sw_NbodyContCount_of_Width[i]

				#Generate Sref
				self._DesignParameter['_Unit_{}'.format(i)] = self._SrefElementDeclaration(_DesignObj=B02_res_and_sw_placement._res_and_sw_placement( _DesignParameter=None, _Name='{}:_Unit_{}'.format(_Name,i)))[0]

				#Define Sref Relection
				self._DesignParameter['_Unit_{}'.format(i)]['_Reflect'] = [0, 0, 0]

				#Define Sref Angle
				self._DesignParameter['_Unit_{}'.format(i)]['_Angle'] = 0

				#Calculate Sref Layer by using Calculation_Parameter
				self._DesignParameter['_Unit_{}'.format(i)]['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

				#Define Sref _XYcoordinate
					#Initialization
				self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates'] = [[0,0]]
					#target_coord
				tmp = self.get_param_KJH2('_Hrz_nbodycontact_upper_unit_{}'.format(i),'_Met1Layer')
				target_coord = tmp[0]['_XY_down']
					#approaching coord
						#if only resistor
				if _Array_PMOSNumberofGate[i] == 0:
					tmp1 = self.get_param_KJH2('_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')
					approaching_coord = tmp1[0]['_XY_right']
						#resistor with sw
				else:
					tmp2 = self.get_param_KJH2('_Unit_{}'.format(i),'_Polyres','_Polyres','PRES_boundary_0')
					tmp3 = self.get_param_KJH2('_Unit_{}'.format(i),'_Pmos_sw','_Pmos','_PODummyLayer')

					#check which one is higher
					if tmp2[0]['_XY_right'][1] > tmp3[0]['_XY_up'][1]:
						approaching_coord = tmp2[0]['_XY_right']
					else:
						approaching_coord = tmp3[0]['_XY_up']

					#Scoord
				tmp4 = self.get_param_KJH2('_Unit_{}'.format(i))
				Scoord = tmp4[0]['_XY_cent']

				New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

					#Ydistance
				New_Scoord[1] = New_Scoord[1] - Ydistance

				self._DesignParameter['_Unit_{}'.format(i)]['_XYCoordinates'] = [New_Scoord]
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
	cellname = 'B03_ycoord_placement_99'
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
	LayoutObj = _ycoord_placement(_DesignParameter=None, _Name=cellname)
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
