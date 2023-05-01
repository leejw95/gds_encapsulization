

############################################################################################################################################################ BASIC Modules
from KJH91_Projects."Project_name".Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects."Project_name".Library_and_Engine import DesignParameters
from KJH91_Projects."Project_name".Library_and_Engine import DRC

import copy
import math
import numpy as np
from SthPack import CoordCalc

from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A00_NMOSWithDummy_v3
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A01_NSubRing
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A02_PMOSWithDummy
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A03_PSubRing
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A04_NbodyContact
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A05_PbodyContact
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A06_ViaStack
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A07_ViaPoly2Met1
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A08_ViaMet12Met2_v2
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A09_ViaMet22Met3
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A10_ViaMet32Met4
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A11_ViaMet42Met5
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A12_ViaMet52Met6
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A13_ViaMet62Met7
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A14_ViaMet72Met8
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block import A16_UNITR

#KJH91 Basic building blocks
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A00_NmosWithDummy_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A01_PmosWithDummy_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A02_NbodyContact_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A03_PbodyContact_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A04_NbodyContactPhyLen_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A05_PbodyContactPhyLen_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A06_NbodyRing_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A07_PbodyRing_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A08_PolyRes_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A09_Ncap_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A10_ViaM0toM1_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A11_ViaM1toM2_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A12_ViaM2toM3_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A13_ViaM3toM4_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A14_ViaM4toM5_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A15_ViaM5toM6_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A16_ViaM6toM7_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A17_ViaM7toM8_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A18_ViaStack_KJH
from KJH91_Projects."Project_name".Layoutgen_code.A_Building_block_KJH import A19_Boundary_element_KJH



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

        #Define Boundary_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
		self._DesignParameter['AAAAAAA'] = self._BoundaryElementDeclaration(
                                                                            _Layer=DesignParameters._LayerMapping['BBBBBB'][0],    
                                                                            _Datatype=DesignParameters._LayerMapping['BBBBBB'][1], 
                                                                            _XWidth=None,
                                                                            _YWidth=None,
                                                                            _XYCoordinates=[ ],
                                                                           )

		#Define Boundary_element _YWidth
		self._DesignParameter['AAAAAAA']['_YWidth'] = '?'

		#Define Boundary_element _XWidth
		self._DesignParameter['AAAAAAA']['_XWidth'] = '?'

		#Define Boundary_element _XYCoordinates
		self._DesignParameter['AAAAAAA']['_XYCoordinates'] = [[0,0]]
		
			#Calculate Sref XYcoord
        tmpXY=[]
				#initialized Sref coordinate
		self._DesignParameter['____elementname_MovingSref']['_XYCoordinates'] = [[0,0]]
				#Calculate
					#Target_coord
        tmp1 = self.get_param_KJH3('____elementname_Target')  		
        target_coord = tmp1[?][?][0]['_XY_type1']  
					#Approaching_coord
        tmp2 = self.get_param_KJH3('____elementname_Approaching')  
        approaching_coord = tmp2[?][?][0]['_XY_type2']   
					#Sref coord
		tmp3 = self.get_param_KJH3('____elementname_MovingSref') 
		Scoord = tmp3[?][0]['_XY_cent']  
					#Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
				#Define
		self._DesignParameter['____elementname_MovingSref']['_XYCoordinates'] = tmpXY
		

############################################################################################################################################################ Path_element Generation: 
		print('##     Path_element Generation:     ##')

        #Define Path_element ex)METAL1 / DIFF (_ODLayer) / POLY / PIMP (_PPLayer) / NWELL / SLVT LVT RVT HVT / OP(OPpress) / CONT (CA) / PCCRIT
        self._DesignParameter['pathelementname'] = self._PathElementDeclaration(          
                                                                                    _Layer=DesignParameters._LayerMapping['BBBBBB'][0],
                                                                                    _Datatype=DesignParameters._LayerMapping['BBBBBB'][1],
                                                                                    _XYCoordinates=[],
                                                                                    _Width=None,
                                                                                )

        #P1--P2 Width
        self._DesignParameter['pathelementname']['_Width'] = '-----'
        
        tmpXY = []
        #P1--P2 coordiantes
			#P1 calculation
		P1 = '?'
			#P2 calculation
		P2 = '?'
			#P1_P2
		P1_P2 = [P1,P2]
		tmpXY.append(P1_P2)
            #Cal tmpXY
        self._DesignParameter['pathelementname']['_XYCoordinates'] = tmpXY


######################################################################################################################################## Sref generation: ViaX
		print('##     Sref generation: ViaX    ##')

		#Define ViaX Parameter
		_Caculation_Parameters = copy.deepcopy(A18_ViaStack_KJH._ViaStack_KJH._ParametersForDesignCalculation)
		_Caculation_Parameters['_Layer1'] 	= None
		_Caculation_Parameters['_Layer2'] 	= None
		_Caculation_Parameters['_COX'] 		= None
		_Caculation_Parameters['_COY'] 		= None

		#Sref ViaX declaration
		self._DesignParameter['_____Vianame'] = self._SrefElementDeclaration(_DesignObj=A18_ViaStack_KJH._ViaStack_KJH(_DesignParameter=None, _Name='{}:_____Vianame'.format(_Name)))[0]

		#Define Sref Relection
        self._DesignParameter['_____Vianame']['_Reflect'] = [0, 0, 0]
        
        #Define Sref Angle
        self._DesignParameter['_____Vianame']['_Angle'] = 0

		#Calcuate Overlapped XYcoord
		tmp1 = self.get_param_KJH3('_____Metalx') 
		tmp2 = self.get_param_KJH3('_____Metaly')
		Ovlpcoord = self.get_ovlp_KJH2(tmp1[?][?],tmp2[?][?])

		#Calcuate _COX and _COY
		_COX, _COY= self._CalculateNumViaByXYWidth(Ovlpcoord[0]['_Xwidth'],Ovlpcoord[0]['_Ywidth'],None)  ## None or 'MinEnclosureX' or 'MinEnclosureY'
		
		#Define _COX and _COY
		_Caculation_Parameters['_COX'] 		= _COX
		_Caculation_Parameters['_COY'] 		= _COY

		#Generate Metal(x), Metal(x+1) and C0(Viax) layer
		self._DesignParameter['_____Vianame']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters) ## Option: Xmin, Ymin

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['_____Vianame']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_____elementname_Target') 
        target_coord = tmp1[?][?]['_____XYtype1']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_____elementname_Approaching')  
        approaching_coord = tmp2[?][?]['_____XYtype2']
                #Sref coord
		tmp3 = self.get_param_KJH3('_____Vianame')
		Scoord = tmp3[?][?]['_XY_cent']
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
		New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['_____Vianame']['_XYCoordinates'] = tmpXY 

######################################################################################################################################## Guardring
        # Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A06_NbodyRing_KJH._NbodyRing_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_XlengthIntn'] 		= None
        _Caculation_Parameters['_YlengthIntn'] 		= None
        _Caculation_Parameters['_NumContTop'] 		= _NumCont
        _Caculation_Parameters['_NumContBottom'] 	= _NumCont
        _Caculation_Parameters['_NumContLeft'] 		= _NumCont
        _Caculation_Parameters['_NumContRight'] 	= _NumCont

        #Find Outter boundary
        tmp = self.get_outter_KJH('_Pmos_cs_sw')

        # Define _XlengthIntn
        _Caculation_Parameters['_XlengthIntn'] 		= abs( tmp['_Mostright']['coord'][0] - tmp['_Mostleft']['coord'][0] ) + _right_margin + _left_margin

        # Define _YlengthIntn
        _Caculation_Parameters['_YlengthIntn'] 		= abs( tmp['_Mostup']['coord'][0] - tmp['_Mostdown']['coord'][0] ) + _up_margin + _down_margin

        # Generate Sref
        self._DesignParameter['_Nbodyring'] = self._SrefElementDeclaration(_DesignObj=A06_NbodyRing_KJH._NbodyRing_KJH(_DesignParameter=None, _Name='{}:_Nbodyring'.format(_Name)))[0]

        # Define Sref Relection
        self._DesignParameter['_Nbodyring']['_Reflect'] = [0, 0, 0]

        # Define Sref Angle
        self._DesignParameter['_Nbodyring']['_Angle'] = 0

        # Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_Nbodyring']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        # Define Sref _XYcoordinate
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = [[0, 0]]

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord 		
        target_coord = [ tmp['_Mostleft']['coord'][0], tmp['_Mostdown']['coord'][0] ]  
                #Approaching_coord
                    #x
        tmp2_1 = self.get_param_KJH3('_Nbodyring','_NbodyLeft','_NbodyContactPhyLen','_Met1Layer')  
        approaching_coordx = tmp2_1[0][0][0][0][0]['_XY_right'][0]
                    #y
        tmp2_2 = self.get_param_KJH3('_Nbodyring','_NbodyBottom','_NbodyContactPhyLen','_Met1Layer')  
        approaching_coordy = tmp2_2[0][0][0][0][0]['_XY_up'][1] 

        approaching_coord = [approaching_coordx,approaching_coordy]
                #Sref coord
        tmp3 = self.get_param_KJH3('_Nbodyring')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        New_Scoord[0] = New_Scoord[0] - _left_margin
        New_Scoord[1] = New_Scoord[1] - _down_margin
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_Nbodyring']['_XYCoordinates'] = tmpXY

		
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

		Ovlpcoord = self.get_ovlp_coord_KJH(tmp1['____number1'],tmp2['____number2']) ##########2^^^^^^^^^^^^^^^^^^^^^ number: choose num from multiple_object
		
############################################################################################################################################################ Get_Scoord_v3.

        #Calculate Sref XYcoord
        tmpXY=[]
			#initialized Sref coordinate
		self._DesignParameter['____elementname_MovingSref']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('____elementname_Target')  		
        target_coord = tmp1[?][?][0]['_XY_type1']  
                #Approaching_coord
        tmp2 = self.get_param_KJH3('____elementname_Approaching')  
        approaching_coord = tmp2[?][?][0]['_XY_type2']   
                #Sref coord
		tmp3 = self.get_param_KJH3('____elementname_MovingSref') 
		Scoord = tmp3[?][0]['_XY_cent']  
                #Cal
		New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
		self._DesignParameter['____elementname_MovingSref']['_XYCoordinates'] = tmpXY



############################################################################################################################################################ Delete

#Delete
del self._DesignParameter['_Unit_{}'.format(i)]

## temp

        #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_G_input_tr']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1_1 = self.get_outter_KJH('_B_load_res')
                    #x
        target_coordx = 0.5 * ( tmp1_1['_Mostright']['coord'][0] + tmp1_1['_Mostleft']['coord'][0] )
                    #y
        target_coordy = 0.5 * ( tmp1_1['_Mostup']['coord'][0] + tmp1_1['_Mostdown']['coord'][0] )
                    
        target_coord = [target_coordx,target_coordy]
                #Approaching_coord
        tmp2 = self.get_outter_KJH('_G_input_tr')  		
                    #x
        approaching_coordx = 0.5 * ( tmp2['_Mostright']['coord'][0] + tmp2['_Mostleft']['coord'][0] )
                    #y
        approaching_coordy = 0.5 * ( tmp2['_Mostup']['coord'][0] + tmp2['_Mostdown']['coord'][0] )

        approaching_coord = [approaching_coordx,approaching_coordy]
                #Sref coord
        tmp3 = self.get_param_KJH3('_G_input_tr')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_G_input_tr']['_XYCoordinates'] = tmpXY








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
