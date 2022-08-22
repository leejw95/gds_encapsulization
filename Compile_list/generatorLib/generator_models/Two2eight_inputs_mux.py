from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import MUX_module

class _2to8inputs_mux(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='_2to8inputs_mux'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,_INV_nmos_width=180, _INV_finger=1, _VDD2PMOS=410, _gate_length=30, _gate_spacing=100, _XVT='RVT', _NMOS_y=375, _Cell_height=1800, _TG_pmos_width=600, _TG_nmos_width=300, _TG_poly_y=760, _NANDIN_y=860, Num_of_MUX_modules=8):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']

		final_module_name = ''

		for i in range(0,Num_of_MUX_modules) :
			name = 'mux_module_%d'%i
			name2 = 'mux_module_%d{}'%i
			self._DesignParameter[name] = self._SrefElementDeclaration(_DesignObj=MUX_module.EasyDebugModule(_Name=name2.format(_Name)))[0]
			self._DesignParameter[name]['_DesignObj']._CalculateDesignParameter(**dict(INV_nmos_width=_INV_nmos_width, INV_finger=_INV_finger, VDD2PMOS=_VDD2PMOS, gate_length=_gate_length, gate_spacing=_gate_spacing, XVT=_XVT, NMOS_y=_NMOS_y,
																					   Cell_height=_Cell_height, TG_pmos_width=_TG_pmos_width, TG_nmos_width=_TG_nmos_width, TG_poly_y=_TG_poly_y, NANDIN_y=_NANDIN_y, MUX_module_num=i))
			if i == 0:
				self._DesignParameter[name]['_XYCoordinates'] = [[0, 0]]
			else:
				module_distance = ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][1][0]) - (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][0][0]))\
									+ _gate_spacing + _gate_length
				self._DesignParameter[name]['_XYCoordinates'] = [[i*module_distance, 0]]

			final_module_name = 'mux_module_%d'%i

		self._DesignParameter['INVb_0_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVb_0_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INb_m1_4']['_XYCoordinates'][0][1][1])], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INb_m1_4']['_XYCoordinates'][0][0][0]), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INb_m1_4']['_XYCoordinates'][0][1][1])]]]
		self._DesignParameter['INVb_1_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVb_1_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INb_m1_3']['_XYCoordinates'][0][0][1])], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INb_m1_4']['_XYCoordinates'][0][0][0]), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INb_m1_3']['_XYCoordinates'][0][0][1])]]]
		self._DesignParameter['INVa_0_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVa_0_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1])], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][0]), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1])]]]
		self._DesignParameter['INVa_1_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVa_1_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), ((((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1]) - drc._VIAxMinWidth) - (2 * drc._Metal1MinEnclosureVia3)) - drc._MetalxMinSpace2)], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][0]), ((((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1]) - drc._VIAxMinWidth) - (2 * drc._Metal1MinEnclosureVia3)) - drc._MetalxMinSpace2)]]]
		self._DesignParameter['INVc_0_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVc_0_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), ((((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1]) - (2 * drc._VIAxMinWidth)) - (4 * drc._Metal1MinEnclosureVia3)) - (2 * drc._MetalxMinSpace2))], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INc_m1']['_XYCoordinates'][0][0][0]), ((((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INVa_m1']['_XYCoordinates'][0][0][1]) - (2 * drc._VIAxMinWidth)) - (4 * drc._Metal1MinEnclosureVia3)) - (2 * drc._MetalxMinSpace2))]]]
		self._DesignParameter['INVc_1_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=(drc._VIAxMinWidth + (2 * drc._Metal1MinEnclosureVia3)))
		self._DesignParameter['INVc_1_line']['_XYCoordinates'] = [[[(((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XYCoordinates'][0][0]) - (self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_pmos']['_XWidth'] / 2)), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INc_m1']['_XYCoordinates'][0][0][1])], [(self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['INc_m1']['_XYCoordinates'][0][0][0]), (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INc_m1']['_XYCoordinates'][0][0][1])]]]
		self._DesignParameter['OUT_line'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['OUTvia']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['OUT_line']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['OUTvia']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['OUTvia']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['OUTvia']['_XYCoordinates'][0][1]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['OUTvia']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['OUTvia']['_XYCoordinates'][0][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['OUTvia']['_XYCoordinates'][0][1]))]]]

		self._DesignParameter['RVT_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['XVT_Around']['_Width'])
		self._DesignParameter['RVT_all']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][1][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['XVT_Around']['_XYCoordinates'][0][1][1]))]]]
		self._DesignParameter['VSS_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INV']['_DesignObj']._DesignParameter['PbodyContact']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['VSS_all']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['VSS_M2']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['VSS_M2']['_XYCoordinates'][0][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['VSS_M2']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['VSS_M2']['_XYCoordinates'][0][0][1]))]]]
		self._DesignParameter['VDD_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['INV']['_DesignObj']._DesignParameter['NbodyContact']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'])
		self._DesignParameter['VDD_all']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['VDD_M2']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['VDD_M2']['_XYCoordinates'][0][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['VDD_M2']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['VDD_M2']['_XYCoordinates'][0][0][1]))]]]
		self._DesignParameter['VSS_pimp_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_vss']['_YWidth'])
		self._DesignParameter['VSS_pimp_all']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_vss']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_vss']['_XYCoordinates'][0][1]))],
																	[(+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_vss']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['pp_vss']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['PIMP_pmos_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['pmos_all_pimp']['_Width'])
		self._DesignParameter['PIMP_pmos_all']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['pmos_all_pimp']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['pmos_all_pimp']['_XYCoordinates'][0][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['pmos_all_pimp']['_XYCoordinates'][0][1][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['pmos_all_pimp']['_XYCoordinates'][0][1][1]))]]]
		self._DesignParameter['vdd_diff_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_YWidth'])
		self._DesignParameter['vdd_diff_all']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][1][0])), (+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][1][1]))],
																	[(+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][1][0])), (+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][1][1]))]]]
		self._DesignParameter['vss_diff_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['DIFF'][0], _Datatype=DesignParameters._LayerMapping['DIFF'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_YWidth'])
		self._DesignParameter['vss_diff_all']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][0][1]))],
																	[(+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][0]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][0][0])), (+ ((self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_XYCoordinates'][0][1]) + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NAND']['_DesignObj']._DesignParameter['supply_od']['_XYCoordinates'][0][1]))]]]
		self._DesignParameter['NW_all'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _Width=self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NW_all']['_Width'])
		self._DesignParameter['NW_all']['_XYCoordinates'] = [[[(+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][0] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NW_all']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter['mux_module_0']['_XYCoordinates'][0][1] + self._DesignParameter['mux_module_0']['_DesignObj']._DesignParameter['NW_all']['_XYCoordinates'][0][0][1]))], [(+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][0] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NW_all']['_XYCoordinates'][0][0][0])), (+ (self._DesignParameter[final_module_name]['_XYCoordinates'][0][1] + self._DesignParameter[final_module_name]['_DesignObj']._DesignParameter['NW_all']['_XYCoordinates'][0][0][1]))]]]