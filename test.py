from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import Three2TwentyEight_MUX
from generatorLib.generator_models import RArray
from generatorLib.generator_models import ViaMet22Met3


for i in range (0,Num_of_Vref) :

	name1 = 'Vref_%d_via_1'%i
	name1_1 = 'Vref_%d_via_1in{}'%i
	name2 = 'Vref_%d_via_2'%i
	name2_1 = 'Vref_%d_via_2in{}'%i

	pathname1 = 'Vref_%d_m2_1'%i
	pathname2 = 'Vref_%d_m3_1'%i
	module_num = i%7
	muxname = 'mux_module_%d'%module_num

	Eightmux_num = i // 7
	muxname2 = 'EightMUX_%d'%Eightmux_num

	self._DesignParameter[name1] = self._SrefElementDeclaration(_DesignObj=ViaMet22Met3._ViaMet22Met3(_Name=name1_1.format(_Name)))[0]
	self._DesignParameter[name1]['_XYCoordinates'] = [[(+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][0] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][0])), (+ (self._DesignParameter['R_ladder']['_XYCoordinates'][0][1] + self._DesignParameter['R_ladder']['_DesignObj']._DesignParameter['_M3_vertical']['_XYCoordinates'][i+1][1][1]))]]

	self._DesignParameter['via_m1_m2_drain'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='via_m1_m2_drainIn{}'.format(_Name)))[0]