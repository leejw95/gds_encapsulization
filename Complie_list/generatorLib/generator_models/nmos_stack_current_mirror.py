from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import PSubRing
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaStack
from generatorLib.generator_models import ViaPoly2Met1

class _nmos_stack_current_mirror(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='nmos_stack_current_mirror'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,nmos1_width=2000,nmos1_length=500,nmos1_gate=1,nmos1_dummy=False,nmos1_xvt='RVT',nmos1_pccrit=False,nmos2_width=2000,nmos2_length=30,nmos2_gate=1,nmos2_dummy=False,nmos2_xvt='RVT',nmos2_pccrit=False,guardring_bot=2,guardring_top=2,guardring_left=2,guardring_right=2,guardring_width=None,guardring_height=None,diode_connect=None):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing

		self._DesignParameter['nmos1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos1In{}'.format(_Name)))[0]
		self._DesignParameter['nmos1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos1_gate, _NMOSChannelWidth=nmos1_width, _NMOSChannellength=nmos1_length, _NMOSDummy=nmos1_dummy, _GateSpacing=None, _SDWidth=None, _XVT=nmos1_xvt, _PCCrit=nmos1_pccrit))
		self._DesignParameter['nmos1']['_XYCoordinates'] = [[0, (- 25.0)]]
		self._DesignParameter['nmos2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos2In{}'.format(_Name)))[0]
		self._DesignParameter['nmos2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos2_gate, _NMOSChannelWidth=nmos2_width, _NMOSChannellength=nmos2_length, _NMOSDummy=nmos2_dummy, _GateSpacing=None, _SDWidth=None, _XVT=nmos2_xvt, _PCCrit=nmos2_pccrit))
		self._DesignParameter['nmos2']['_XYCoordinates'] = [[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]+self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2) - self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]+self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2+2*drc._PolygateMinSpace2OD), (((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]
		del self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)]
		del self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0]
		del self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][int((len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']) / 2)):len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'])]
		del self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0:int((len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']) / 2))]
		num_cont1 = max(max(1, (1 + int(((((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1)
		num_cont2 = max(max(1, (1 + int(((((((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1)
		self._DesignParameter['gate_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_1In{}'.format(_Name)))[0]
		self._DesignParameter['gate_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=num_cont1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['gate_1']['_XYCoordinates'] = [[self._DesignParameter['nmos1']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2)]]

		self._DesignParameter['M1_diode_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['M1_diode_connect_x']['_Width']=self.getYWidth('gate_1','_Met1Layer')
		self._DesignParameter['M1_diode_connect_x']['_XYCoordinates']=[[self.getXY('gate_1')[0], [self.getXY('nmos2','_Met1Layer')[0][0], self.getXY('gate_1')[0][1]]]]

		self._DesignParameter['M1_diode_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['M1_diode_connect_y']['_Width']=self.getXWidth('nmos2','_Met1Layer')
		self._DesignParameter['M1_diode_connect_y']['_XYCoordinates']=[[[self.getXY('nmos2','_Met1Layer')[0][0], self.getXY('gate_1')[0][1]+self.getYWidth('gate_1','_Met1Layer')/2], self.getXY('nmos2','_Met1Layer')[0]]]

		self._DesignParameter['gate_2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_2In{}'.format(_Name)))[0]
		self._DesignParameter['gate_2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=num_cont2, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['gate_2']['_XYCoordinates'] = [[(self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + ((self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] - self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)), self._DesignParameter['M1_diode_connect_x']['_XYCoordinates'][0][0][1]+self._DesignParameter['M1_diode_connect_x']['_Width']/2+self.getYWidth('gate_2','_Met1Layer')/2+drc._Metal1MinSpace2]]

		if diode_connect == False :
			self._DesignParameter['M1_diode_connect_x']['_XYCoordinates']=[]
			self._DesignParameter['M1_diode_connect_y']['_XYCoordinates']=[]

		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ (self._DesignParameter['gate_1']['_XYCoordinates'][0][0] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_1']['_XYCoordinates'][0][1] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
			for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ (self._DesignParameter['gate_1']['_XYCoordinates'][0][0] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_1']['_XYCoordinates'][0][1] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
			for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_gate1_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_gate1_y']['_XYCoordinates'] = path_list
		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ (self._DesignParameter['gate_2']['_XYCoordinates'][0][0] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_2']['_XYCoordinates'][0][1] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
			for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ (self._DesignParameter['gate_2']['_XYCoordinates'][0][0] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_2']['_XYCoordinates'][0][1] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
			for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_gate2_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_gate2_x']['_XYCoordinates'] = path_list
		# self._DesignParameter['poly_gate_left_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		# self._DesignParameter['poly_gate_left_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_1']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_1']['_XYCoordinates'][0][1]]]]
		# self._DesignParameter['poly_gate_right_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		# self._DesignParameter['poly_gate_right_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_2']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_2']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['via_m1_m2_nmos2'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_nmos2In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'] = [[self._DesignParameter['gate_2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2-self.getXWidth('gate_2','_Met1Layer')/2, self.getXY('gate_2')[0][1]+self.getYWidth('gate_2','_Met1Layer')/2-self.getYWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2]]
		self._DesignParameter['guardring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='guardringIn{}'.format(_Name)))[0]
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[(- 88.0), 11.0]]
		if (guardring_width == None):
			guardring_xwidth = self.CeilMinSnapSpacing((max(self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2+self.getXWidth('guardring','right','_Met1Layer')/2+drc._Metal1MinSpace3, (((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3) - ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3)), 2*MinSnapSpacing)
		if (guardring_width != None):
			guardring_xwidth = guardring_width
		if (guardring_height == None):
			guardring_yheight = self.CeilMinSnapSpacing(max(self._DesignParameter['gate_1']['_XYCoordinates'][0][1]+self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3)-min(self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD), 2*MinSnapSpacing)
		if (guardring_height != None):
			guardring_yheight = guardring_height
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_yheight, width=guardring_xwidth, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[self.CeilMinSnapSpacing((max(self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2+self.getXWidth('guardring','right','_Met1Layer')/2+drc._Metal1MinSpace3, (((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3) + ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3))/2, 2*MinSnapSpacing),self.CeilMinSnapSpacing((max(self._DesignParameter['gate_1']['_XYCoordinates'][0][1]+self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3)+min(self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD))/2, MinSnapSpacing)]]

		self._DesignParameter['m1_vss'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._Metal1MinWidth * 3))
		self._DesignParameter['m1_vss']['_XYCoordinates'] = [[[(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + ((drc._Metal1MinWidth * 3) / 2)), ((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))], [(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + ((drc._Metal1MinWidth * 3) / 2)), (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1])]]]

		num_via_x=2#max(1, int(self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		num_via_y=1
		self._DesignParameter['via_m1_m3_nmos1_gate']=self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_nmos1_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=num_via_x, COY=num_via_y, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates']=[[self._DesignParameter['gate_1']['_XYCoordinates'][0][0]-self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+self._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter['gate_1']['_XYCoordinates'][0][1]]]

		self._DesignParameter['_AdditionalM1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['_AdditionalM1']['_Width']=self.getYWidth('gate_1','_Met1Layer')
		self._DesignParameter['_AdditionalM1']['_XYCoordinates']=[[[self.getXY('gate_1')[0][0], self.getXY('gate_1')[0][1]], [self.getXY('via_m1_m3_nmos1_gate')[0][0]+self.getXWidth('via_m1_m3_nmos1_gate','ViaMet12Met2','_Met1Layer')/2, self.getXY('gate_1')[0][1]]]]



		if nmos1_gate != 1 or nmos2_gate != 1 :
			raise NotImplementedError


	def _CalculateDesignParameter_single(self,nmos1_width=2000,nmos1_length=500,nmos1_gate=1,nmos1_dummy=False,nmos1_xvt='RVT',nmos1_pccrit=False,nmos2_width=2000,nmos2_length=30,nmos2_gate=1,nmos2_dummy=False,nmos2_xvt='RVT',nmos2_pccrit=False,guardring_bot=2,guardring_top=2,guardring_left=2,guardring_right=2,guardring_width=None,guardring_height=None, diode_connect=None):

		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		MinSnapSpacing=drc._MinSnapSpacing

		if diode_connect != False :
			diode_connect = False
		self._DesignParameter['nmos1'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos1In{}'.format(_Name)))[0]
		self._DesignParameter['nmos1']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos1_gate, _NMOSChannelWidth=nmos1_width, _NMOSChannellength=nmos1_length, _NMOSDummy=nmos1_dummy, _GateSpacing=None, _SDWidth=None, _XVT=nmos1_xvt, _PCCrit=nmos1_pccrit))
		self._DesignParameter['nmos1']['_XYCoordinates'] = [[0, (- 25.0)]]
		self._DesignParameter['nmos2'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmos2In{}'.format(_Name)))[0]
		self._DesignParameter['nmos2']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos2_gate, _NMOSChannelWidth=nmos2_width, _NMOSChannellength=nmos2_length, _NMOSDummy=nmos2_dummy, _GateSpacing=None, _SDWidth=None, _XVT=nmos2_xvt, _PCCrit=nmos2_pccrit))
		self._DesignParameter['nmos2']['_XYCoordinates'] = [[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][0]+self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth']/2) - self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]+self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']/2+2*drc._PolygateMinSpace2OD), (((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2)) - (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] / 2))]]
		#del self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][(- 1)]
		del self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0]
		#del self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][int((len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']) / 2)):len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'])]
		del self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][0:int((len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates']) / 2))]
		num_cont1 = max(max(1, (1 + int(((((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1)
		num_cont2 = max(max(1, (1 + int(((((((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))))), 1)
		self._DesignParameter['gate_1'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_1In{}'.format(_Name)))[0]
		self._DesignParameter['gate_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=num_cont1, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['gate_1']['_XYCoordinates'] = [[self._DesignParameter['nmos1']['_XYCoordinates'][0][0], ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace2)]]

		self._DesignParameter['M1_diode_connect_x']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['M1_diode_connect_x']['_Width']=self.getYWidth('gate_1','_Met1Layer')
		self._DesignParameter['M1_diode_connect_x']['_XYCoordinates']=[[self.getXY('gate_1')[0], [self.getXY('nmos2','_Met1Layer')[0][0], self.getXY('gate_1')[0][1]]]]

		self._DesignParameter['M1_diode_connect_y']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['M1_diode_connect_y']['_Width']=self.getXWidth('nmos2','_Met1Layer')
		self._DesignParameter['M1_diode_connect_y']['_XYCoordinates']=[[[self.getXY('nmos2','_Met1Layer')[0][0], self.getXY('gate_1')[0][1]+self.getYWidth('gate_1','_Met1Layer')/2], self.getXY('nmos2','_Met1Layer')[0]]]

		self._DesignParameter['gate_2'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_2In{}'.format(_Name)))[0]
		self._DesignParameter['gate_2']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=num_cont2, _ViaPoly2Met1NumberOfCOY=1))
		self._DesignParameter['gate_2']['_XYCoordinates'] = [[(self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + ((self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] - self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']) / 2)), self._DesignParameter['M1_diode_connect_x']['_XYCoordinates'][0][0][1]+self._DesignParameter['M1_diode_connect_x']['_Width']/2+self.getYWidth('gate_2','_Met1Layer')/2+drc._Metal1MinSpace2]]

		if diode_connect == False :
			self._DesignParameter['M1_diode_connect_x']['_XYCoordinates']=[]
			self._DesignParameter['M1_diode_connect_y']['_XYCoordinates']=[]

		path_list = []
		xy_offset = [0, 0]
		if (len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
			mode = 'vertical'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
			mode = 'horizontal'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		elif (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
			mode = 'vertical'
			_width = self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		else:
			print('Invalid Target Input')
		if (mode == 'vertical'):
			xy_with_offset = []
			target_y_value = [[(+ (self._DesignParameter['gate_1']['_XYCoordinates'][0][0] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_1']['_XYCoordinates'][0][1] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
			for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		elif (mode == 'horizontal'):
			xy_with_offset = []
			target_x_value = [[(+ (self._DesignParameter['gate_1']['_XYCoordinates'][0][0] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_1']['_XYCoordinates'][0][1] + self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
			for i in range(len(self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
				xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos1']['_XYCoordinates'][0][1])], self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
			for i in range(len(xy_with_offset)):
				path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		for i in range(len(path_list)):
			path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		self._DesignParameter['poly_gate1_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		self._DesignParameter['poly_gate1_y']['_XYCoordinates'] = path_list
		# path_list = []
		# xy_offset = [0, 0]
		# if (len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
		# 	mode = 'vertical'
		# 	_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
		# 	mode = 'horizontal'
		# 	_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# elif (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
		# 	mode = 'vertical'
		# 	_width = self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
		# else:
		# 	print('Invalid Target Input')
		# if (mode == 'vertical'):
		# 	xy_with_offset = []
		# 	target_y_value = [[(+ (self._DesignParameter['gate_2']['_XYCoordinates'][0][0] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_2']['_XYCoordinates'][0][1] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][1]
		# 	for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		# 		xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		# 	for i in range(len(xy_with_offset)):
		# 		path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
		# elif (mode == 'horizontal'):
		# 	xy_with_offset = []
		# 	target_x_value = [[(+ (self._DesignParameter['gate_2']['_XYCoordinates'][0][0] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['gate_2']['_XYCoordinates'][0][1] + self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]][0][0]
		# 	for i in range(len(self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
		# 		xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos2']['_XYCoordinates'][0][1])], self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
		# 	for i in range(len(xy_with_offset)):
		# 		path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
		# for i in range(len(path_list)):
		# 	path_list[i][0] = [(xy + offset) for (xy, offset) in zip(path_list[i][0], xy_offset)]
		# self._DesignParameter['poly_gate2_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
		# self._DesignParameter['poly_gate2_x']['_XYCoordinates'] = path_list
		# self._DesignParameter['poly_gate_left_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		# self._DesignParameter['poly_gate_left_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_1']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_1']['_XYCoordinates'][0][1]]]]
		# self._DesignParameter['poly_gate_right_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_2']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
		# self._DesignParameter['poly_gate_right_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_2']['_XYCoordinates'][0][1]], [((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), self._DesignParameter['gate_2']['_XYCoordinates'][0][1]]]]
		self._DesignParameter['via_m1_m2_nmos2'] = self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m2_nmos2In{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=2, COY=1, start_layer=1, end_layer=4))
		self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'] = [[self._DesignParameter['gate_2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2-self.getXWidth('gate_2','_Met1Layer')/2, self.getXY('gate_2')[0][1]+self.getYWidth('gate_2','_Met1Layer')/2-self.getYWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2]]
		self._DesignParameter['guardring'] = self._SrefElementDeclaration(_DesignObj=PSubRing.PSubRing(_Name='guardringIn{}'.format(_Name)))[0]
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=5000, width=3000, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[(- 88.0), 11.0]]
		if (guardring_width == None):
			guardring_xwidth = self.CeilMinSnapSpacing((max(self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2+self.getXWidth('guardring','right','_Met1Layer')/2+drc._Metal1MinSpace3, (((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3) - ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3)), 2*MinSnapSpacing)
		if (guardring_width != None):
			guardring_xwidth = guardring_width
		if (guardring_height == None):
			guardring_yheight = self.CeilMinSnapSpacing(max(self._DesignParameter['gate_1']['_XYCoordinates'][0][1]+self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3)-min(self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD), 2*MinSnapSpacing)
		if (guardring_height != None):
			guardring_yheight = guardring_height
		self._DesignParameter['guardring']['_DesignObj']._CalculateDesignParameter(**dict(height=guardring_yheight, width=guardring_xwidth, contact_bottom=guardring_bot, contact_top=guardring_top, contact_left=guardring_left, contact_right=guardring_right))
		self._DesignParameter['guardring']['_XYCoordinates'] = [[self.CeilMinSnapSpacing((max(self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][0]+self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')/2+self.getXWidth('guardring','right','_Met1Layer')/2+drc._Metal1MinSpace3, (((self._DesignParameter['nmos2']['_XYCoordinates'][0][0] + self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos2']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['right']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) + drc._Metal1MinSpace3) + ((((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) - (self._DesignParameter['guardring']['_DesignObj']._DesignParameter['left']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / 2)) - drc._Metal1MinSpace3))/2, 2*MinSnapSpacing),self.CeilMinSnapSpacing((max(self._DesignParameter['gate_1']['_XYCoordinates'][0][1]+self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3, self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates'][0][1]+self._DesignParameter['via_m1_m2_nmos2']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self.getYWidth('guardring','top','_Met1Layer')/2+drc._Metal1MinSpace3)+min(self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_Met1Layer')/2-self.getYWidth('guardring','bot','_Met1Layer')/2-drc._Metal1MinSpace3, self._DesignParameter['nmos1']['_XYCoordinates'][0][1]-self.getYWidth('nmos1','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD, self._DesignParameter['nmos2']['_XYCoordinates'][0][1]-self.getYWidth('nmos2','_POLayer')/2-self.getYWidth('guardring','bot','_ODLayer')/2-drc._PolygateMinSpace2OD))/2, MinSnapSpacing)]]

		self._DesignParameter['m1_vss'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=(drc._Metal1MinWidth * 3))
		self._DesignParameter['m1_vss']['_XYCoordinates'] = [[[(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + ((drc._Metal1MinWidth * 3) / 2)), ((self._DesignParameter['nmos1']['_XYCoordinates'][0][1] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))], [(((self._DesignParameter['nmos1']['_XYCoordinates'][0][0] + self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos1']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)) + ((drc._Metal1MinWidth * 3) / 2)), (self._DesignParameter['guardring']['_XYCoordinates'][0][1] + self._DesignParameter['guardring']['_DesignObj']._DesignParameter['bot']['_XYCoordinates'][0][1])]]]

		num_via_x=2#max(1, int(self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] / (drc._VIAxMinWidth + drc._VIAxMinSpace)))
		num_via_y=1
		self._DesignParameter['via_m1_m3_nmos1_gate']=self._SrefElementDeclaration(_DesignObj=ViaStack._ViaStack(_Name='via_m1_m3_nmos1_gateIn{}'.format(_Name)))[0]
		self._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._CalculateStackSameEnclosure(**dict(COX=num_via_x, COY=num_via_y, start_layer=1, end_layer=3))
		self._DesignParameter['via_m1_m3_nmos1_gate']['_XYCoordinates']=[[self._DesignParameter['gate_1']['_XYCoordinates'][0][0]-self._DesignParameter['gate_1']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2+self._DesignParameter['via_m1_m3_nmos1_gate']['_DesignObj']._DesignParameter['ViaMet12Met2']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth']/2, self._DesignParameter['gate_1']['_XYCoordinates'][0][1]]]

		self._DesignParameter['_AdditionalM1']=self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=None)
		self._DesignParameter['_AdditionalM1']['_Width']=self.getYWidth('gate_1','_Met1Layer')
		self._DesignParameter['_AdditionalM1']['_XYCoordinates']=[[[self.getXY('gate_1')[0][0], self.getXY('gate_1')[0][1]], [self.getXY('via_m1_m3_nmos1_gate')[0][0]+self.getXWidth('via_m1_m3_nmos1_gate','ViaMet12Met2','_Met1Layer')/2, self.getXY('gate_1')[0][1]]]]

		if nmos1_gate != 1 or nmos2_gate != 1 :
			raise NotImplementedError

		self._DesignParameter['via_temp_m1']=dict(_DesignParametertype=7, _XYCoordinates=[], _XWidth=None, _YWidth=None)
		self._DesignParameter['via_temp_m1']['_XYCoordinates']=self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates']
		self._DesignParameter['via_temp_m1']['_XWidth']=self.getXWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')
		self._DesignParameter['via_temp_m1']['_YWidth']=self.getYWidth('via_m1_m2_nmos2','ViaMet12Met2','_Met1Layer')

		#### To make same guardring width and height with stacked nmos ####
		self._DesignParameter['via_m1_m2_nmos2']['_XYCoordinates']=[]
		self._DesignParameter['gate_2']['_XYCoordinates']=[]
		self._DesignParameter['nmos2']['_XYCoordinates']=[]