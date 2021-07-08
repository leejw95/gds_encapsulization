import inspect
import warnings

from designs import StickDiagram, DesignParameters, DRC

class GDS_API:
    def __init__(self):
        # self.__drc_obj = DRC.DRC()
        pass

    def create_gds(self, name=None):
        if '_DesignParameter' in self.__dict__:
            self.feed_design(dp=self._DesignParameter, name=name)
        else:
            warnings.warn('There is no layout design.')

    def feed_design(self, dp, name=None):
        __MAX_STRUCTURE_LEN = 20
        dp['_Name'] = StickDiagram._StickDiagram._NameDeclaration(None,name)
        dp['_GDSFile'] = StickDiagram._StickDiagram._GDSObjDeclaration(None)
        __gds_structure = StickDiagram._StickDiagram()._UpdateDesignParameter2GDSStructure(dp)
        if len(__gds_structure) > 20:
            warnings.warn('Demo version supports maximum 20 elements per structure.')
        __gds_stream = StickDiagram._StickDiagram._CreateGDSStream(None,__gds_structure[:__MAX_STRUCTURE_LEN])
        output_file = open(f'{name}.gds','wb')
        __gds_stream.write_binary_gds_stream(output_file)
        output_file.close()
        del __gds_structure, __gds_stream, output_file

    def get_drc(self, rule_name, rule_arg=dict()):
        rule_name = self.__var_name_tf(rule_name)
        if rule_name in DRC.DRC().__dict__:
            return DRC.DRC().__dict__[rule_name]
        elif rule_name in [obj_info[0] for obj_info in inspect.getmembers(DRC.DRC, inspect.isfunction)]:
            method = getattr(DRC.DRC(), rule_name)
            return method(**rule_arg)
        else:
            raise Exception("Not valid design rule name.")


    def boundary_declaration(self, layer_name):
        return dict(_DesignParametertype=1,
                    _Layer=DesignParameters._LayerMapping[layer_name][0],
                    _Datatype=DesignParameters._LayerMapping[layer_name][1],
                    _XYCoordinates=[],_XWidth=None, _YWidth=None, _Ignore=None, _ElementName=None)

    def path_declaration(self, layer_name):
        return dict(_DesignParametertype=2,
                    _Layer=DesignParameters._LayerMapping[layer_name][0],
                    _Datatype=DesignParameters._LayerMapping[layer_name][1],
                    _XYCoordinates=[],_Width=None,  _Ignore=None, _ElementName=None)

    def sref_declaration(self, designobj=None):
        return dict(_DesignParametertype=3, _DesignObj=designobj, _XYCoordinates=[], _Reflect=None,
                    _Angle=None, _Ignore=None, _ElementName=None)

    def __var_name_tf(self, name):


        return name



if __name__ == '__main__':
    a = GDS_API()
