from designs import StickDiagram, DesignParameters

class GDS_API:
    def __init__(self):
        self.__stick_diagram = StickDiagram._StickDiagram()
        self.test_flow()
        self.run_flow()

    def test_flow(self):
        self.__stick_diagram._DesignParameter = dict(
            test_routing=self.__stick_diagram._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0],
                                                                          _Datatype=DesignParameters._LayerMapping['POLY'][1],
                                                                          _XYCoordinates=[[0,0]], _XWidth=100, _YWidth=100),
            _Name=self.__stick_diagram._NameDeclaration(_Name='test'),
            _GDSFile=self.__stick_diagram._GDSObjDeclaration(_GDSFile=None)
        )

    def run_flow(self):
        self.__update_dp_to_gds_structure(self.__stick_diagram._DesignParameter)

    def __update_dp_to_gds_structure(self,dp,file=None):
        self.__stick_diagram._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=dp)
        __gds_stream = self.__stick_diagram._CreateGDSStream(self.__stick_diagram._DesignParameter['_GDSFile']['_GDSFile'])
        file_name = file if file is not None else './out.gds'
        output_file = open(f'{file_name}','wb')
        __gds_stream.write_binary_gds_stream(output_file)
        output_file.close()


if __name__ == '__main__':
    a = GDS_API()
