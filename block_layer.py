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
        __MAX_STRUCTURE_LEN = 10
        dp['_Name'] = StickDiagram._StickDiagram._NameDeclaration(None,name)
        dp['_GDSFile'] = StickDiagram._StickDiagram._GDSObjDeclaration(None)
        __gds_structure = StickDiagram._StickDiagram()._UpdateDesignParameter2GDSStructure(dp)
        __gds_stream = StickDiagram._StickDiagram._CreateGDSStream(None,__gds_structure[:__MAX_STRUCTURE_LEN])
        output_file = open(f'{name}.gds','wb')
        __gds_stream.write_binary_gds_stream(output_file)
        output_file.close()
        del __gds_structure, __gds_stream, output_file

    def get_drc(self, rule_name, rule_arg=dict()):
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
        return dict(_DesignParametertype=3, _DesignObj=designobj, _XYCoordinates=[[]], _Reflect=None,
                    _Angle=None, _Ignore=None, _ElementName=None)

    def __var_name_tf(self,name):
        pass


    # def test_flow(self):
    #     self.__stick_diagram._DesignParameter = dict(
    #         test_routing=self.__stick_diagram._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
    #                                                                       _Datatype=DesignParameters._LayerMapping['POLY'][1],
    #                                                                       _XYCoordinates=[[0,0]], _XWidth=100, _YWidth=100),
    #         _Name=self.__stick_diagram._NameDeclaration(_Name='test'),
    #         _GDSFile=self.__stick_diagram._GDSObjDeclaration(_GDSFile=None)
    #     )
    #
    # def run_flow(self):
    #     self.__update_dp_to_gds_structure(self.__stick_diagram._DesignParameter)
    #
    # # def __UpdateDesignParameter(self,dp):
    #
    # def __update_dp_to_gds_structure(self,dp,file=None):
    #     __MAX_STRUCTURE_LEN=10
    #     self.__stick_diagram._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=dp)
    #     __gds_stream = self.__stick_diagram._CreateGDSStream(self.__stick_diagram._DesignParameter['_GDSFile']['_GDSFile'][:__MAX_STRUCTURE_LEN])
    #     file_name = file if file is not None else './out.gds'
    #     output_file = open(f'{file_name}','wb')
    #     __gds_stream.write_binary_gds_stream(output_file)
    #     output_file.close()


if __name__ == '__main__':
    a = GDS_API()
