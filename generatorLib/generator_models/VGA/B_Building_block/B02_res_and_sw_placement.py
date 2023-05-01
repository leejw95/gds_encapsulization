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

############################################################################################################################################################ Class_HEADER
class _res_and_sw_placement(StickDiagram_KJH0._StickDiagram_KJH):

	##########################################################################################################################^^^^^^^^^^^^^^^^^^^^^
	#Define input_parameters for Design calculation 
	_ParametersForDesignCalculation = dict(	
											_Polyres_R_X_width  = 2500,
											_Polyres_R_Y_length = 1500,
											_Polyres_CoXNum     = None,
											_Polyres_CoYNum     = None,
											_Polyres_Dummy      = True,
											_Polyres_N_Parallel = None,

											_PMOSNumberofGate=20,
											_PMOSChannelWidth=1000,
											_PMOSChannellength=30,
											_PMOSDummy=True,
											_GateSpacing=None,
											_SDWidth=None,
											_XVT='SLVT',
											_PCCrit=None,

											_vtc_btw_res_sw_NbodyContCount_of_Width = 2,

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
										_Polyres_R_X_width  = 2500,
										_Polyres_R_Y_length = 1500,
										_Polyres_CoXNum     = None,
										_Polyres_CoYNum     = None,
										_Polyres_Dummy      = True,
										_Polyres_N_Parallel = None,
										
										_PMOSNumberofGate=20,
										_PMOSChannelWidth=1000,
										_PMOSChannellength=30,
										_PMOSDummy=True,
										_GateSpacing=None,
										_SDWidth=None,
										_XVT='SLVT',
										_PCCrit=None,

										_vtc_btw_res_sw_NbodyContCount_of_Width = 2,
								
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

	############################################################################################################################################## SREF_Generation:resistor
		print('##     SREF_Generation:resistor    ##')

		#Define Calculation_Parameters
		_Caculation_Parameters = copy.deepcopy( B00_polyresparallel._polyresparallel._ParametersForDesignCalculation)
		_Caculation_Parameters['_Polyres_R_X_width']    =  _Polyres_R_X_width
		_Caculation_Parameters['_Polyres_R_Y_length']   =  _Polyres_R_Y_length
		_Caculation_Parameters['_Polyres_CoXNum']       =  _Polyres_CoXNum
		_Caculation_Parameters['_Polyres_CoYNum']       =  _Polyres_CoYNum
		_Caculation_Parameters['_Polyres_Dummy']        =  _Polyres_Dummy
		_Caculation_Parameters['_Polyres_N_Parallel']   =  _Polyres_N_Parallel

		#Generate Sref
		self._DesignParameter['_Polyres'] = self._SrefElementDeclaration(_DesignObj=B00_polyresparallel._polyresparallel( _DesignParameter=None, _Name='{}:_polyres'.format(_Name)))[0]
																			  
		#Define Sref Relection
		self._DesignParameter['_Polyres']['_Reflect'] = [0, 0, 0]

		#Define Sref Angle
		self._DesignParameter['_Polyres']['_Angle'] = 0

		#Calculate Sref Layer by using Calculation_Parameter
		self._DesignParameter['_Polyres']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

		#Define Sref _XYcoordinate
		self._DesignParameter['_Polyres']['_XYCoordinates']=[[0, 0]]

	############################################################################################################################################## _Vtc_nbodycontact_btw_res_sw
		print('##     _Vtc_nbodycontact_btw_res_sw    ##')
		################################################################################################################################ _Vtc_nbodycontact_btw_res_sw:if resistor only
		if _PMOSNumberofGate == 0:
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor only    ##')
		################################################################################################################################ _Vtc_nbodycontact_btw_res_sw:if resistor with sw
		else:
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor with sw    ##')

			################################################################################################################## _Vtc_nbodycontact_btw_res_sw:if resistor with sw: length calculation
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor with sw: length calculation   ##')

				#################################################################################################### _Vtc_nbodycontact_btw_res_sw:if resistor with sw: length calculation:gen sw for len cal
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor with sw: length calculation:gen sw for len cal   ##')

			#Define Calculation_Parameters
			_Caculation_Parameters = copy.deepcopy(B01_pmos_sw._pmos_sw._ParametersForDesignCalculation)
			_Caculation_Parameters['_PMOSNumberofGate']  	= _PMOSNumberofGate
			_Caculation_Parameters['_PMOSChannelWidth']  	= _PMOSChannelWidth
			_Caculation_Parameters['_PMOSChannellength'] 	= _PMOSChannellength
			_Caculation_Parameters['_PMOSDummy']  			= _PMOSDummy
			_Caculation_Parameters['_GateSpacing']  		= _GateSpacing
			_Caculation_Parameters['_SDWidth']  			= _SDWidth
			_Caculation_Parameters['_XVT']  				= _XVT
			_Caculation_Parameters['_PCCrit']  				= _PCCrit

			#Generate Sref
			self._DesignParameter['_Pmos_sw_test'] = self._SrefElementDeclaration(_DesignObj=B01_pmos_sw._pmos_sw( _DesignParameter=None, _Name='{}:_Pmos_sw_test'.format(_Name)))[0]

			#Define Sref Relection
			self._DesignParameter['_Pmos_sw_test']['_Reflect'] = [0, 0, 0]

			#Define Sref Angle
			self._DesignParameter['_Pmos_sw_test']['_Angle'] = 0

			#Calculate Sref Layer by using Calculation_Parameter
			self._DesignParameter['_Pmos_sw_test']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

			#Define Sref _XYcoordinate
			self._DesignParameter['_Pmos_sw_test']['_XYCoordinates']=[[0, 0]]

				#################################################################################################### _Vtc_nbodycontact_btw_res_sw:if resistor with sw: cal nbody length
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor with sw: cal nbody length   ##')

			#Calcuate Ywidth of cell
				#Ywidht of polyres
			tmp1 = self.get_param_KJH2('_Polyres','_Polyres','PRES_boundary_0')
			len_of_polyres = tmp1[0]['_Xwidth'] #becuase 90 degree

				#Ywidht of Pmos_sw
			tmp2 = self.get_param_KJH2('_Pmos_sw_test','_Pmos','_POLayer')
			tmp3 = self.get_param_KJH2('_Pmos_sw_test','_Pmos_hrz_poly')
			len_of_sw = abs( tmp2[0]['_XY_up'][1] - tmp3[0]['_XY_down'][1] )

			len_of_Nbody = max(len_of_polyres,len_of_sw)
			_vtc_nbodycont_btw_res_sw_Length = len_of_Nbody

			#Delete
			del self._DesignParameter['_Pmos_sw_test']

			################################################################################################################## _Vtc_nbodycontact_btw_res_sw:if resistor with sw: gen Nbodycontact
			print('##     _Vtc_nbodycontact_btw_res_sw:if resistor with sw: gen Nbodycontact   ##')

			#Pre_defined
			Xdistance_btw_polyres_and_nbodycontact = 250

			#Calculate _NbodyContact input parameter: input as _NbodyContCount_of_Width and _NbodyCont_Length and _NbodyContact_Vert
			#If vertical
			_NbodyContact_NumberOfNbodyCOX = _vtc_btw_res_sw_NbodyContCount_of_Width
			_NbodyContact_NumberOfNbodyCOY = (int(((_vtc_nbodycont_btw_res_sw_Length - (2 * _DRCobj._CoMinEnclosureByOD)) / (_DRCobj._CoMinWidth + _DRCobj._CoMinSpace2))) - _vtc_btw_res_sw_NbodyContCount_of_Width) + 0
			_NbodyContact_Met1XWidth       = None
			_NbodyContact_Met1YWidth       = None

			#Define _NbodyContact input parameter
			_Caculation_Parameters = copy.deepcopy(A04_NbodyContact._NbodyContact._ParametersForDesignCalculation)
			_Caculation_Parameters['_NumberOfNbodyCOX']     = _NbodyContact_NumberOfNbodyCOX
			_Caculation_Parameters['_NumberOfNbodyCOY']     = _NbodyContact_NumberOfNbodyCOY
			_Caculation_Parameters['_Met1XWidth']           = _NbodyContact_Met1XWidth
			_Caculation_Parameters['_Met1YWidth']           = _NbodyContact_Met1YWidth

			#Define _NbodyContact Sref
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw'] = self._SrefElementDeclaration(_DesignObj=A04_NbodyContact._NbodyContact( _DesignParameter=None, _Name='{}:_Vtc_nbodycontact_btw_res_sw'.format(_Name) ))[0]

			#Define _NbodyContact Sref Relection
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw']['_Reflect'] = [0, 0, 0]

			#Define _NbodyContact Sref Angle
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw']['_Angle'] = 0

			#Define _NbodyContact layer
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw']['_DesignObj']._CalculateNbodyContactDesignParameter(**_Caculation_Parameters)

			#Define _NbodyContact coordinate

				#Calculate Sref XYcoord
					#initialized Sref coordinate
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw']['_XYCoordinates'] = [[0,0]]
					#Calculation
			tmp1 = self.get_param_KJH2('_Polyres','_Polyres','PRES_boundary_0')
			tmp2 = self.get_param_KJH2('_Vtc_nbodycontact_btw_res_sw','_Met1Layer')
			tmp3 = self.get_param_KJH2('_Vtc_nbodycontact_btw_res_sw')

			target_coord        = tmp1[-1]['_XY_down']
			approaching_coord   = tmp2[0]['_XY_left']
			Scoord              = tmp3[0]['_XY_cent']

			New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

					#Xdistance
			New_Scoord[0] = New_Scoord[0] + Xdistance_btw_polyres_and_nbodycontact

			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw']['_XYCoordinates'] = [New_Scoord]


			#Define NWELL of _NbodyContact
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw_nwell'] = self._BoundaryElementDeclaration(
																												_Layer=DesignParameters._LayerMapping['NWELL'][0],
																												_Datatype=DesignParameters._LayerMapping['NWELL'][1],
																												_XWidth=None,
																												_YWidth=None,
																												_XYCoordinates=[ ],
																											  )

			#Define NWELL Xwidth
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw_nwell']['_XWidth'] = self.getXWidth('_Vtc_nbodycontact_btw_res_sw','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

			#Define NWELL Ywidth
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw_nwell']['_YWidth'] = self.getYWidth('_Vtc_nbodycontact_btw_res_sw','_ODLayer') + _DRCobj._PpMinExtensiononPactive*2

			#Define NWELL Coordinates
			self._DesignParameter['_Vtc_nbodycontact_btw_res_sw_nwell']['_XYCoordinates'] =  self.getXY('_Vtc_nbodycontact_btw_res_sw')

	############################################################################################################################################## Pmos_sw
			print('##     Pmos_sw    ##')
		################################################################################################################################ Pmos_sw: gen
			print('##     Pmos_sw: gen    ##')

			#pre-defined
			xdistance_btw_vtcnobodycontact_pmossw = 100

			#Define Calculation_Parameters
			_Caculation_Parameters = copy.deepcopy(B01_pmos_sw._pmos_sw._ParametersForDesignCalculation)
			_Caculation_Parameters['_PMOSNumberofGate']  	= _PMOSNumberofGate
			_Caculation_Parameters['_PMOSChannelWidth']  	= _PMOSChannelWidth
			_Caculation_Parameters['_PMOSChannellength'] 	= _PMOSChannellength
			_Caculation_Parameters['_PMOSDummy']  			= _PMOSDummy
			_Caculation_Parameters['_GateSpacing']  		= _GateSpacing
			_Caculation_Parameters['_SDWidth']  			= _SDWidth
			_Caculation_Parameters['_XVT']  				= _XVT
			_Caculation_Parameters['_PCCrit']  				= _PCCrit

			#Generate Sref
			self._DesignParameter['_Pmos_sw'] = self._SrefElementDeclaration(_DesignObj=B01_pmos_sw._pmos_sw( _DesignParameter=None, _Name='{}:_Pmos_sw'.format(_Name)))[0]

			#Define Sref Relection
			self._DesignParameter['_Pmos_sw']['_Reflect'] = [0, 0, 0]

			#Define Sref Angle
			self._DesignParameter['_Pmos_sw']['_Angle'] = 0

			#Calculate Sref Layer by using Calculation_Parameter
			self._DesignParameter['_Pmos_sw']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

			#Define Sref _XYcoordinate
				#Calculate Sref XYcoord
						#initialized Sref coordinate
			self._DesignParameter['_Pmos_sw']['_XYCoordinates'] = [[0,0]]
						#Calculation
			tmp1 = self.get_param_KJH2('_Vtc_nbodycontact_btw_res_sw','_Met1Layer')
			tmp2 = self.get_param_KJH2('_Pmos_sw','_Pmos','_PODummyLayer')
			tmp3 = self.get_param_KJH2('_Pmos_sw')

			target_coord        = tmp1[0]['_XY_right']
			approaching_coord   = tmp2[0]['_XY_left']
			Scoord              = tmp3[0]['_XY_cent']

			New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)

						#Xdistance
			New_Scoord[0] = New_Scoord[0] + xdistance_btw_vtcnobodycontact_pmossw

			self._DesignParameter['_Pmos_sw']['_XYCoordinates'] = [New_Scoord]





		print('###############      For Debugging      ##################')



############################################################################################################################################################ CALCULATION END
		print ('#########################################################################################################')
		print ('                                      Calculation   END                                                  ')
		print ('#########################################################################################################')

############################################################################################################################################################ START MAIN
if __name__ == '__main__':

	from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
	from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

	libname = 'Proj_VGA_B_building_block'
	cellname = 'B02_res_and_sw_placement_99'
	_fileName = cellname + '.gds'

	''' Input Parameters for Layout Object '''
	InputParams = dict(
							#polyres
							_Polyres_R_X_width  = 1000,
							_Polyres_R_Y_length = 600,
							_Polyres_CoXNum     = None,
							_Polyres_CoYNum     = None,
							_Polyres_Dummy      = True,
							_Polyres_N_Parallel = 2,

							#pmos_sw
							_PMOSNumberofGate=3,
							_PMOSChannelWidth=500,
							_PMOSChannellength=30,
							_PMOSDummy=True,
							_GateSpacing=None,
							_SDWidth=None,
							_XVT='SLVT',
							_PCCrit=None,

							#vtc nbodycontact
							_vtc_btw_res_sw_NbodyContCount_of_Width = 5,

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
	LayoutObj = _res_and_sw_placement(_DesignParameter=None, _Name=cellname)
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
