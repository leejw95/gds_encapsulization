from generatorLib import StickDiagram
from generatorLib import DesignParameters
import copy
import math
from generatorLib import DRC
from generatorLib.generator_models import ViaPoly2Met1
from generatorLib.generator_models import NbodyContact
from generatorLib.generator_models import PMOSWithDummy
from generatorLib.generator_models import NMOSWithDummy
from generatorLib.generator_models import ViaMet12Met2
from generatorLib.generator_models import PbodyContact

class INVERTER_800n_2016_MK(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='INVERTER_800n_2016_MK'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,COX=12,COY=2,finger1=6,width1=200,SLVT=None,VDD2VSSHeight=1800,finger2=8,width2=400):
    
        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']
        
        self._DesignParameter['extStackedContact_CDNS_641779186725_0'] = self._SrefElementDeclaration(_DesignObj=PbodyContact._PbodyContact(_Name='extStackedContact_CDNS_641779186725_0In{}'.format(_Name)))[0]
        self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_DesignObj']._CalculatePbodyContactDesignParameter(**dict(_NumberOfPbodyCOX=COX, _NumberOfPbodyCOY=COY, _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['slvtnfet_b_CDNS_641779186720_0'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='slvtnfet_b_CDNS_641779186720_0In{}'.format(_Name)))[0]
        self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=finger1, _NMOSChannelWidth=width1, _NMOSChannellength=30, _NMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
        self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'] = [[self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_XYCoordinates'][0][0], (((self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_XYCoordinates'][0][1] + (self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + drc._Metal1MinSpace3) + (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))]]
        path_list = []
        if (len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_XYCoordinates'][0][1] + self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_XYCoordinates'][0][0] + self._DesignParameter['extStackedContact_CDNS_641779186725_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['M1_NMOS_SRC'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['M1_NMOS_SRC']['_XYCoordinates'] = path_list
        XYList = []
        xy_offset = [0, 0]
        for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
            if ((i % 2) == 1):
                XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['VIA1_Drain_NMOS'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='VIA1_Drain_NMOSIn{}'.format(_Name)))[0]
        self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=2))
        self._DesignParameter['VIA1_Drain_NMOS']['_XYCoordinates'] = XYList
        self._DesignParameter['testtt'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='testttIn{}'.format(_Name)))[0]
        self._DesignParameter['testtt']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (int(((((((self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))) + 1)), _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['testtt']['_XYCoordinates'] = [[self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0], (((((self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + drc._Metal1MinSpace2) + drc._Metal1MinEnclosureCO2) + (drc._CoMinWidth / 2))]]
        path_list = []
        if (len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['testtt']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['testtt']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtnfet_b_CDNS_641779186720_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['cont_nmos'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['PCCRIT'][0], _Datatype=DesignParameters._LayerMapping['PCCRIT'][1], _Width=_width)
        self._DesignParameter['cont_nmos']['_XYCoordinates'] = path_list
        self._DesignParameter['ngate_poly'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['testtt']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['ngate_poly']['_XYCoordinates'] = [[[(self._DesignParameter['cont_nmos']['_XYCoordinates'][0][0][0] - (self._DesignParameter['cont_nmos']['_Width'] / 2)), self._DesignParameter['cont_nmos']['_XYCoordinates'][0][1][1]], [(self._DesignParameter['cont_nmos']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['cont_nmos']['_Width'] / 2)), self._DesignParameter['cont_nmos']['_XYCoordinates'][(- 1)][1][1]]]]
        self._DesignParameter['METAL2_path_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
        self._DesignParameter['METAL2_path_1']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['VIA1_Drain_NMOS']['_XYCoordinates'][0][0] + self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), (+ ((self._DesignParameter['VIA1_Drain_NMOS']['_XYCoordinates'][0][1] + self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(+ ((self._DesignParameter['VIA1_Drain_NMOS']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), (+ ((self._DesignParameter['VIA1_Drain_NMOS']['_XYCoordinates'][(- 1)][1] + self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['VIA1_Drain_NMOS']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))]]]
        self._DesignParameter['extStackedContact_CDNS_641779186721_0'] = self._SrefElementDeclaration(_DesignObj=NbodyContact._NbodyContact(_Name='extStackedContact_CDNS_641779186721_0In{}'.format(_Name)))[0]
        self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._CalculateNbodyContactDesignParameter(**dict(_NumberOfNbodyCOX=COX, _NumberOfNbodyCOY=COY, _Met1XWidth=None, _Met1YWidth=None))
        self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'] = [[0, VDD2VSSHeight]]
        self._DesignParameter['slvtpfet_b_CDNS_641779186723_0'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='slvtpfet_b_CDNS_641779186723_0In{}'.format(_Name)))[0]
        self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=finger2, _PMOSChannelWidth=width2, _PMOSChannellength=30, _PMOSDummy=True, _GateSpacing=None, _XVT='SLVT'))
        self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'] = [[self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'][0][0], (((self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'][0][1] - (self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace3) - (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))]]
        path_list = []
        if (len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'][0][1] + self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'][0][0] + self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['PMOS_source'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['PMOS_source']['_XYCoordinates'] = path_list
        via_num_pdrain = (max(1, int((((self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace)))) + 2)
        XYList = []
        xy_offset = [0, 0]
        for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
            if ((i % 2) == 1):
                XYList.append([((x + y) + z) for (x, y, z) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i], xy_offset)])
        self._DesignParameter['pmos_drain_array'] = self._SrefElementDeclaration(_DesignObj=ViaMet12Met2._ViaMet12Met2(_Name='pmos_drain_arrayIn{}'.format(_Name)))[0]
        self._DesignParameter['pmos_drain_array']['_DesignObj']._CalculateViaMet12Met2DesignParameterMinimumEnclosureX(**dict(_ViaMet12Met2NumberOfCOX=1, _ViaMet12Met2NumberOfCOY=via_num_pdrain))
        self._DesignParameter['pmos_drain_array']['_XYCoordinates'] = XYList
        self._DesignParameter['pmos_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='pmos_inputIn{}'.format(_Name)))[0]
        self._DesignParameter['pmos_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(1, (int(((((((self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)) - ((self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0] + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace))) + 1)), _ViaPoly2Met1NumberOfCOY=1))
        self._DesignParameter['pmos_input']['_XYCoordinates'] = [[self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos_drain_array']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - drc._Metal1MinSpace2) - (self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))]]
        path_list = []
        if (len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['pmos_input']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['pmos_input']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1])], self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['pmos_gate_ex_array'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['pmos_gate_ex_array']['_XYCoordinates'] = path_list
        self._DesignParameter['cont_poly_ext'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['pmos_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
        self._DesignParameter['cont_poly_ext']['_XYCoordinates'] = [[[(self._DesignParameter['pmos_gate_ex_array']['_XYCoordinates'][0][0][0] - (self._DesignParameter['pmos_gate_ex_array']['_Width'] / 2)), self._DesignParameter['pmos_gate_ex_array']['_XYCoordinates'][0][1][1]], [(self._DesignParameter['pmos_gate_ex_array']['_XYCoordinates'][(- 1)][1][0] + (self._DesignParameter['pmos_gate_ex_array']['_Width'] / 2)), self._DesignParameter['pmos_gate_ex_array']['_XYCoordinates'][(- 1)][(- 1)][1]]]]
        self._DesignParameter['METAL2_path_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
        self._DesignParameter['METAL2_path_2']['_XYCoordinates'] = [[[(+ ((self._DesignParameter['pmos_drain_array']['_XYCoordinates'][0][0] + self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), (+ ((self._DesignParameter['pmos_drain_array']['_XYCoordinates'][0][1] + self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))], [(+ ((self._DesignParameter['pmos_drain_array']['_XYCoordinates'][(- 1)][0] + self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][0]) + (self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'] / 2))), (+ ((self._DesignParameter['pmos_drain_array']['_XYCoordinates'][(- 1)][1] + self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos_drain_array']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)))]]]
        self._DesignParameter['METAL1_path_3'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=50)
        self._DesignParameter['METAL1_path_3']['_XYCoordinates'] = [[[(+ self._DesignParameter['pmos_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['pmos_input']['_XYCoordinates'][0][1])], [(+ self._DesignParameter['testtt']['_XYCoordinates'][0][0]), (+ self._DesignParameter['testtt']['_XYCoordinates'][0][1])]]]
        self._DesignParameter['METAL2_path_0'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2'][0], _Datatype=DesignParameters._LayerMapping['METAL2'][1], _Width=50)
        self._DesignParameter['METAL2_path_0']['_XYCoordinates'] = [[[(min(self._DesignParameter['METAL2_path_1']['_XYCoordinates'][0][1][0], self._DesignParameter['METAL2_path_2']['_XYCoordinates'][0][1][0]) - (self._DesignParameter['METAL2_path_2']['_Width'] / 2)), self._DesignParameter['METAL2_path_1']['_XYCoordinates'][0][0][1]], [(min(self._DesignParameter['METAL2_path_1']['_XYCoordinates'][0][1][0], self._DesignParameter['METAL2_path_2']['_XYCoordinates'][0][1][0]) - (self._DesignParameter['METAL2_path_2']['_Width'] / 2)), self._DesignParameter['METAL2_path_2']['_XYCoordinates'][0][0][1]]]]
        self._DesignParameter['NWELL_boundary_2'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] + (drc._NwMinEnclosurePactive * 2)), _YWidth=((((self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_XYCoordinates'][0][1] + self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['extStackedContact_CDNS_641779186721_0']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) - ((self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2))) + (drc._NwMinEnclosurePactive * 2)))
        self._DesignParameter['NWELL_boundary_2']['_XYCoordinates'] = [[self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][0], (((self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_XYCoordinates'][0][1] + self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['slvtpfet_b_CDNS_641779186723_0']['_DesignObj']._DesignParameter['_SLVTLayer']['_YWidth'] / 2)) + (self._DesignParameter['NWELL_boundary_2']['_YWidth'] / 2))]]
        