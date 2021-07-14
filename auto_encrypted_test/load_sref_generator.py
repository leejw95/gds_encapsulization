import block_layer
import test_generator

class SREFTEST(block_layer.GDS_API):
    def __init__(self,cell_name='SREFTEST'):
        super(SREFTEST, self).__init__(cell_name)
        self._DesignParameter = dict()

    def calculate_design(self, user_variable=dict(num_of_sref=2, sub_block_v=dict(_NMOSChannellength=60, _NMOSChannelWidth=700, _NMOSNumberofGate =2, _NMOSDummy=True))):
        self._DesignParameter['path_test'] = self.path_declaration('METAL1')
        self._DesignParameter['path_test']['_XYCoordinates'] = [[[0,0],[1000,0]]]
        self._DesignParameter['path_test']['_Width'] = 300
        for i in range(0,user_variable['num_of_sref']):
            name = f'testSref{i}'
            self._DesignParameter[name] = self.sref_declaration(designobj=test_generator.NMOS(f'nmos{i}'))
            self._DesignParameter[name]['_DesignObj'].calculate_design(user_variable['sub_block_v'])
            self._DesignParameter[name]['_XYCoordinates'] = [[0,i*1000]]


        self.calculate_done()


if __name__ == '__main__':
    srefgen = SREFTEST()
    srefgen.calculate_design()
    srefgen.create_gds('sreftest')