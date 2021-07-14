import block_layer
import test_generator

class SREFTEST(block_layer.GDS_API):
    def __init__(self):
        super(SREFTEST, self).__init__()
        self._DesignParameter = dict()

    def calculate_design(self, user_variable=dict(num_of_sref=1, sub_block_v=dict(_NMOSChannellength=60, _NMOSChannelWidth=700, _NMOSNumberofGate =30, _NMOSDummy=True))):
        for i in range(0,user_variable['num_of_sref']):
            name = f'testSref{i}'
            self._DesignParameter[name] = self.sref_declaration(designobj=test_generator.NMOS())
            self._DesignParameter[name]['_DesignObj'].calculate_design(user_variable['sub_block_v'])
            self._DesignParameter[name]['_XYCoordinates'] = [i*1000,0]



if __name__ == '__main__':
    srefgen = SREFTEST()
    srefgen.calculate_design()
    srefgen.create_gds('sreftest')