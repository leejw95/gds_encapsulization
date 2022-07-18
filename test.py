from generatorLib import StickDiagram
from generatorLib import DRC
from generatorLib.generator_models import PMOSWithDummy


class EasyDebugModule(StickDiagram._StickDiagram):
	def __init__(self, _DesignParameter=None, _Name='EasyDebugModule'):
		if _DesignParameter != None:
			self._DesignParameter = _DesignParameter
		else:
			self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
		self._DesignParameter['_Name']['Name'] = _Name

	def _CalculateDesignParameter(self,finger=2,width=1500,length=100,dummy=True,xvt='LVT',pccrit=False,guardring_co_right=3,guardring_co_left=3,guardring_co_top=4,guardring_co_bottom=2,guardring_width=None,guardring_height=None):
	
		drc = DRC.DRC()
		_Name = self._DesignParameter['_Name']['_Name']
		
		self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
		print ('sdfsdf')