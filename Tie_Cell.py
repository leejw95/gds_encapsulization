import StickDiagram
import DesignParameters
import copy
import math
import DRC
import PMOSWithDummy
import ViaPoly2Met1
import SupplyRails
import NMOSWithDummy

class Tie_Cell(StickDiagram._StickDiagram):
    def __init__(self, _DesignParameter=None, _Name='TIEH_2X_STD_v1'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter_tiehigh_v1(self,vss2nmos=None,vdd2pmos=None,sd_width=66,gate_spacing=110,vdd2vss_height=1800,nmos_width=200,pmos_width=400,length=40,nmos_gate=1,pmos_gate=1,XVT='RVT'):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssIn{}'.format(_Name)))[0]
        self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['vss']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddIn{}'.format(_Name)))[0]
        self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['vdd']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vdd2vss_height]]
        self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))

        if vss2nmos == None :
            vss2nmos=max(self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3, self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+drc._OdMinSpace2Pp)

        self._DesignParameter['nmos']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (self._DesignParameter['vss']['_XYCoordinates'][0][1] + vss2nmos)]]
        self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
        self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))

        if vdd2pmos == None :
            vdd2pmos=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3

        self._DesignParameter['pmos']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (self._DesignParameter['vdd']['_XYCoordinates'][0][1] - vdd2pmos)]]
        self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
        self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
        self._DesignParameter['gate_input']['_XYCoordinates'] = [[min((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['poly_gate_nmos_xy'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][0] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['pmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['pmos_supply_routing']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['vss']['_XYCoordinates'][0][0] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['nmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['nmos_supply_routing']['_XYCoordinates'] = path_list
        self._DesignParameter['RVT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], _YWidth=((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])))
        self._DesignParameter['RVT_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['gate_input_routing_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=drc._PolygateMinWidth*5/3)
        self._DesignParameter['gate_input_routing_1']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))], [(self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['poly_gate_nmos_xy']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]]
        self._DesignParameter['nwell_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (6 * drc._NwMinEnclosurePactive2)), _YWidth=(((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - self._DesignParameter['gate_input']['_XYCoordinates'][0][1]))
        self._DesignParameter['nwell_layer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['gate_input']['_XYCoordinates'][0][1]) / 2)]]
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['m1_pmos_drain_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'] = path_list
        self._DesignParameter['m1_pmos_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'])
        self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])], [(self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
        self._DesignParameter['m1_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
        self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['gate_input']['_XYCoordinates'][0][0] - (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)], [((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)]]]
        path_list = []
        if (len(self._DesignParameter['gate_input']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] == self._DesignParameter['gate_input']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] == self._DesignParameter['gate_input']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1])
            for i in range(len(self._DesignParameter['gate_input']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], [self._DesignParameter['gate_input']['_XYCoordinates'][i][0], self._DesignParameter['gate_input']['_XYCoordinates'][i][1]+self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][0])
            for i in range(len(self._DesignParameter['gate_input']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([0, 0], self._DesignParameter['gate_input']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['m1_drain_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['m1_drain_gate']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['gate_input_pmos'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['gate_input_pmos']['_XYCoordinates'] = path_list
        self._DesignParameter['gate_input_routing_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=drc._PolygateMinWidth*5/3)
        self._DesignParameter['gate_input_routing_2']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))], [(self._DesignParameter['gate_input_pmos']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['gate_input_pmos']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]]

        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_TIEHpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='TIEH')

        self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vdd']['_XYCoordinates']
        self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']
        self._DesignParameter['_TIEHpin']['_XYCoordinates']=[[(self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][0]+self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][-1][0])/2, self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][1]]]

        if self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
            self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2

        if self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
            self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2

        self._DesignParameter['_AdditionalPPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=None, _YWidth=None)
        self._DesignParameter['_AdditionalPPLayer']['_XWidth']=self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']+2*drc._PpMinWidth
        self._DesignParameter['_AdditionalPPLayer']['_YWidth']=self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
        self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']


    # def _CalculateDesignParameter_tiehigh_v2(self,sd_width=66,gate_spacing=110,vdd2vss_height=1800,nmos_width=200,pmos_width=400,length=40,nmos_gate=4,pmos_gate=4,XVT='RVT'):
    #
    # 	drc = DRC.DRC()
    # 	_Name = self._DesignParameter['_Name']['_Name']
    #
    # 	self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
    # 	self._DesignParameter['vss']['_XYCoordinates'] = [[0.0, 0.0]]
    # 	self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
    # 	self._DesignParameter['vdd']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vdd2vss_height]]
    # 	self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
    # 	self._DesignParameter['nmos']['_XYCoordinates'] = [[0.0, 300.0]]
    # 	self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
    # 	self._DesignParameter['pmos']['_XYCoordinates'] = [[0.0, 1300.0]]
    # 	self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
    # 	self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][0] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['pmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['pmos_supply_routing']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['vss']['_XYCoordinates'][0][0] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['nmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['nmos_supply_routing']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['RVT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], _YWidth=((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])))
    # 	self._DesignParameter['RVT_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])) / 2)]]
    # 	self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(2, max(1, (1 + int((((max((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']), (((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'])) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
    # 	self._DesignParameter['gate_input']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] / 2))
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['m1_drain_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['m1_drain_gate_routing_y']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['nmos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
    # 	self._DesignParameter['nmos_gate_routing']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['pmos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
    # 	self._DesignParameter['pmos_gate_routing']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['m1_pmos_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
    # 	self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_pmos_drain_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)], [((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_pmos_drain_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)]]]
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (0 + self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (0 + self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['mos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
    # 	self._DesignParameter['mos_gate_routing']['_XYCoordinates'] = [[[min(((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), self._DesignParameter['gate_input']['_XYCoordinates'][0][1]], [max(((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2))), self._DesignParameter['gate_input']['_XYCoordinates'][0][1]]]]
    # 	self._DesignParameter['m1_gate_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
    # 	self._DesignParameter['m1_gate_drain_routing_x']['_XYCoordinates'] = [[[min((self._DesignParameter['m1_drain_gate_routing_y']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_drain_gate_routing_y']['_Width'] / 2)), self._DesignParameter['gate_input']['_XYCoordinates'][0][0]), self._DesignParameter['gate_input']['_XYCoordinates'][0][1]], [max((self._DesignParameter['m1_drain_gate_routing_y']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_drain_gate_routing_y']['_Width'] / 2)), self._DesignParameter['gate_input']['_XYCoordinates'][0][0]), self._DesignParameter['gate_input']['_XYCoordinates'][0][1]]]]
    # 	self._DesignParameter['nw_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (drc._NwMinEnclosurePactive2 * 6)), _YWidth=(((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - self._DesignParameter['gate_input']['_XYCoordinates'][0][1]))
    # 	self._DesignParameter['nw_layer']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['gate_input']['_XYCoordinates'][0][1]) / 2)]]
    #
    # 	self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
    # 	self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
    # 	self._DesignParameter['_TIEHpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='TIEH')
    #
    # 	self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vdd']['_XYCoordinates']
    # 	self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']
    # 	self._DesignParameter['_TIEHpin']['_XYCoordinates']=[[(self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][0]+self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][-1][0])/2, self._DesignParameter['m1_pmos_drain_routing_x']['_XYCoordinates'][0][0][1]]]


    def _CalculateDesignParameter_tielow_v1(self,vss2nmos=None,vdd2pmos=None,sd_width=66,gate_spacing=110,vdd2vss_height=1800,nmos_width=200,pmos_width=400,length=40,nmos_gate=1,pmos_gate=1,XVT='RVT'):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssIn{}'.format(_Name)))[0]
        self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['vss']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
        self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))

        if vss2nmos == None :
            vss2nmos=max(self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3,self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']/2+self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth']/2+drc._OdMinSpace2Pp)

        self._DesignParameter['nmos']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (self._DesignParameter['vss']['_XYCoordinates'][0][1] + vss2nmos)]]
        self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddIn{}'.format(_Name)))[0]
        self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['vdd']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vdd2vss_height]]
        self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
        self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))

        if vdd2pmos == None :
            vdd2pmos=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2+drc._Metal1MinSpace3


        self._DesignParameter['pmos']['_XYCoordinates'] = [[self._DesignParameter['vdd']['_XYCoordinates'][0][0], (self._DesignParameter['vdd']['_XYCoordinates'][0][1] - vdd2pmos)]]
        self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
        self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
        self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
        self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameterMinimumEnclosureX(**dict(_ViaPoly2Met1NumberOfCOX=1, _ViaPoly2Met1NumberOfCOY=2))
        self._DesignParameter['gate_input']['_XYCoordinates'] = [[min((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0]), (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0])), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['poly_gate_nmos_xy'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = ((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) + (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2))
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
                xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['gate_input_pmos'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
        self._DesignParameter['gate_input_pmos']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][0] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['pmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['pmos_supply_routing']['_XYCoordinates'] = path_list
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (self._DesignParameter['vss']['_XYCoordinates'][0][0] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['nmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['nmos_supply_routing']['_XYCoordinates'] = path_list
        self._DesignParameter['RVT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], _YWidth=((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])))
        self._DesignParameter['RVT_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])) / 2)]]
        self._DesignParameter['gate_input_routing_2'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=drc._PolygateMinWidth*5/3)
        self._DesignParameter['gate_input_routing_2']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]+self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)))], [(self._DesignParameter['gate_input_pmos']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['gate_input_pmos']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]+self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth']/2)))]]]
        self._DesignParameter['gate_input_routing_1'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=drc._PolygateMinWidth*5/3)
        self._DesignParameter['gate_input_routing_1']['_XYCoordinates'] = [[[((self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))], [(self._DesignParameter['poly_gate_nmos_xy']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['poly_gate_nmos_xy']['_Width'] / 2)), (((self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1]) - (self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'] / 2)))]]]
        self._DesignParameter['nwell_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (6 * drc._NwMinEnclosurePactive2)), _YWidth=(((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - self._DesignParameter['gate_input']['_XYCoordinates'][0][1]))
        self._DesignParameter['nwell_layer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['gate_input']['_XYCoordinates'][0][1]) / 2)]]
        self._DesignParameter['m1_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
        self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['gate_input']['_XYCoordinates'][0][0] - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)], [((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_XYCoordinatePMOSSupplyRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) - (self._DesignParameter['m1_drain_routing_x']['_Width'] / 2)) - drc._Metal1MinSpace2)]]]
        path_list = []
        if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][0])
            for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 0):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['m1_pmos_drain_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['m1_pmos_drain_gate_routing_x']['_XYCoordinates'] = path_list
        self._DesignParameter['m1_nmos_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
        self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])], [((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
        path_list = []
        if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
            mode = 'horizontal'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
            mode = 'vertical'
            _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
        else:
            print('Invalid Target Input')
        if (mode == 'vertical'):
            xy_with_offset = []
            target_y_value = (0 + self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][1])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
        elif (mode == 'horizontal'):
            xy_with_offset = []
            target_x_value = (0 + self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][0])
            for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
                if ((i % 2) == 1):
                    xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
            for i in range(len(xy_with_offset)):
                path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
        self._DesignParameter['m1_drain_gate'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
        self._DesignParameter['m1_drain_gate']['_XYCoordinates'] = path_list
        self._DesignParameter['m1_gate_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['m1_pmos_drain_gate_routing_x']['_Width'])
        self._DesignParameter['m1_gate_drain_routing_y']['_XYCoordinates'] = [[[(+ self._DesignParameter['gate_input']['_XYCoordinates'][0][0]), (+ self._DesignParameter['gate_input']['_XYCoordinates'][0][1])-self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth']/2], [self._DesignParameter['gate_input']['_XYCoordinates'][0][0], self._DesignParameter['m1_drain_routing_x']['_XYCoordinates'][0][0][1]]]]

        self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
        self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
        self._DesignParameter['_TIELpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='TIEL')

        self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vdd']['_XYCoordinates']
        self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']
        self._DesignParameter['_TIELpin']['_XYCoordinates']=[[(self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][0]+self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][-1][0])/2, self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][1]]]

        if self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
            self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2

        if self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']*self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth'] < drc._PODummyMinArea :
            self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_YWidth']=drc._PODummyMinArea//self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth']+2

        self._DesignParameter['_AdditionalPPLayer']=self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=None, _YWidth=None)
        self._DesignParameter['_AdditionalPPLayer']['_XWidth']=self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth']+2*drc._PpMinWidth
        self._DesignParameter['_AdditionalPPLayer']['_YWidth']=self._DesignParameter['vss']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth']
        self._DesignParameter['_AdditionalPPLayer']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']


    # def _CalculateDesignParameter_tielow_v2(self,vss2nmos=None,vdd2pmos=None,sd_width=66,gate_spacing=110,vdd2vss_height=1800,nmos_width=200,pmos_width=400,length=40,nmos_gate=3,pmos_gate=3,XVT='RVT'):
    #
    # 	drc = DRC.DRC()
    # 	_Name = self._DesignParameter['_Name']['_Name']
    #
    # 	self._DesignParameter['vss'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vssIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
    # 	self._DesignParameter['vss']['_XYCoordinates'] = [[0.0, 0.0]]
    # 	self._DesignParameter['vdd'] = self._SrefElementDeclaration(_DesignObj=SupplyRails.SupplyRail(_Name='vddIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=2, UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
    # 	self._DesignParameter['vdd']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], vdd2vss_height]]
    # 	self._DesignParameter['nmos'] = self._SrefElementDeclaration(_DesignObj=NMOSWithDummy._NMOS(_Name='nmosIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['nmos']['_DesignObj']._CalculateNMOSDesignParameter(**dict(_NMOSNumberofGate=nmos_gate, _NMOSChannelWidth=nmos_width, _NMOSChannellength=length, _NMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
    # 	self._DesignParameter['nmos']['_XYCoordinates'] = [[0.0, 300.0]]
    # 	self._DesignParameter['pmos'] = self._SrefElementDeclaration(_DesignObj=PMOSWithDummy._PMOS(_Name='pmosIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['pmos']['_DesignObj']._CalculatePMOSDesignParameter(**dict(_PMOSNumberofGate=pmos_gate, _PMOSChannelWidth=pmos_width, _PMOSChannellength=length, _PMOSDummy=True, _GateSpacing=gate_spacing, _SDWidth=sd_width, _XVT=XVT))
    # 	self._DesignParameter['pmos']['_XYCoordinates'] = [[0.0, 1300.0]]
    # 	self._DesignParameter['vss']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=True))
    # 	self._DesignParameter['vdd']['_DesignObj']._CalculateDesignParameter(**dict(NumPitch=max(1, (1 + int(((((((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2)) - ((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_PODummyLayer']['_XWidth'] / 2))) - drc._VIAxMinSpace) - (2 * drc._VIAxMinEnclosureByMetx)) / (drc._VIAxMinWidth + drc._VIAxMinSpace))))), UnitPitch=130, Met1YWidth=80, Met2YWidth=300, PpNpYWidth=180, isPbody=False))
    # 	self._DesignParameter['gate_input'] = self._SrefElementDeclaration(_DesignObj=ViaPoly2Met1._ViaPoly2Met1(_Name='gate_inputIn{}'.format(_Name)))[0]
    # 	self._DesignParameter['gate_input']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=max(2, max(1, (1 + int((((max((((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']), (((self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]) - (self._DesignParameter['pmos']['_XYCoordinates'][0][0] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])) + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth'])) - drc._CoMinSpace) - (2 * drc._CoMinEnclosureByPO)) / (drc._CoMinWidth + drc._CoMinSpace)))))), _ViaPoly2Met1NumberOfCOY=1))
    # 	self._DesignParameter['gate_input']['_XYCoordinates'] = [[self._DesignParameter['nmos']['_XYCoordinates'][0][0], ((((self._DesignParameter['pmos']['_XYCoordinates'][0][1] + self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) - (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + ((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2))) / 2)]]
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['vdd']['_XYCoordinates'][0][0] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['pmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['pmos_supply_routing']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['vss']['_XYCoordinates'][0][0] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['nmos_supply_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['nmos_supply_routing']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['RVT_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['RVT'][0], _Datatype=DesignParameters._LayerMapping['RVT'][1], _XWidth=self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XWidth'], _YWidth=((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) - (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])))
    # 	self._DesignParameter['RVT_boundary_0']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], (((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vss']['_XYCoordinates'][0][1] + self._DesignParameter['vss']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1])) / 2)]]
    # 	self._DesignParameter['nwell_layer'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['NWELL'][0], _Datatype=DesignParameters._LayerMapping['NWELL'][1], _XWidth=(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] + (6 * drc._NwMinEnclosurePactive2)), _YWidth=(((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) - self._DesignParameter['gate_input']['_XYCoordinates'][0][1]))
    # 	self._DesignParameter['nwell_layer']['_XYCoordinates'] = [[self._DesignParameter['vss']['_XYCoordinates'][0][0], ((((self._DesignParameter['vdd']['_XYCoordinates'][0][1] + self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_XYCoordinates'][0][1]) + (self._DesignParameter['vdd']['_DesignObj']._DesignParameter['_Met2Layer']['_YWidth'] / 2)) + self._DesignParameter['gate_input']['_XYCoordinates'][0][1]) / 2)]]
    # 	self._DesignParameter['m1_nmos_drain_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'])
    # 	self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'] = [[[((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][0][0]) - (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_nmos_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)], [((self._DesignParameter['nmos']['_XYCoordinates'][0][0] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_XYCoordinateNMOSOutputRouting']['_XYCoordinates'][(- 1)][0]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth'] / 2)), ((((self._DesignParameter['nmos']['_XYCoordinates'][0][1] + self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1]) + (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_YWidth'] / 2)) + (self._DesignParameter['m1_nmos_drain_routing_x']['_Width'] / 2)) + drc._Metal1MinSpace2)]]]
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (0 + self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][1])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (0 + self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 1):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['m1_drain_gate_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['m1_drain_gate_routing_y']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'])):
    # 	        if ((i % 2) == 0):
    # 	            xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_METAL1PINDrawing']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['m1_drain_routing_y'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=_width)
    # 	self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'] = path_list
    # 	path_list = []
    # 	if (len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['nmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['nmos']['_XYCoordinates'][0][1])], self._DesignParameter['nmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['nmos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
    # 	self._DesignParameter['nmos_gate_routing']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['mos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_YWidth'])
    # 	self._DesignParameter['mos_gate_routing']['_XYCoordinates'] = [[[(self._DesignParameter['nmos_gate_routing']['_XYCoordinates'][0][0][0] - (self._DesignParameter['nmos_gate_routing']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])], [(self._DesignParameter['nmos_gate_routing']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['nmos_gate_routing']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])]]]
    # 	path_list = []
    # 	if (len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates']) == 1):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][0]):
    # 	    mode = 'horizontal'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	elif (self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1] == self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][(- 1)][1]):
    # 	    mode = 'vertical'
    # 	    _width = self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XWidth']
    # 	else:
    # 	    print('Invalid Target Input')
    # 	if (mode == 'vertical'):
    # 	    xy_with_offset = []
    # 	    target_y_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][1])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [xy_with_offset[i][0], target_y_value]])
    # 	elif (mode == 'horizontal'):
    # 	    xy_with_offset = []
    # 	    target_x_value = (self._DesignParameter['gate_input']['_XYCoordinates'][0][0] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][0][0])
    # 	    for i in range(len(self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'])):
    # 	        xy_with_offset.append([(x + y) for (x, y) in zip([(0 + self._DesignParameter['pmos']['_XYCoordinates'][0][0]), (0 + self._DesignParameter['pmos']['_XYCoordinates'][0][1])], self._DesignParameter['pmos']['_DesignObj']._DesignParameter['_POLayer']['_XYCoordinates'][i])])
    # 	    for i in range(len(xy_with_offset)):
    # 	        path_list.append([xy_with_offset[i], [target_x_value, xy_with_offset[i][1]]])
    # 	self._DesignParameter['pmos_gate_routing'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _Width=_width)
    # 	self._DesignParameter['pmos_gate_routing']['_XYCoordinates'] = path_list
    # 	self._DesignParameter['m1_gate_routing_x'] = self._PathElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1'][0], _Datatype=DesignParameters._LayerMapping['METAL1'][1], _Width=self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'])
    # 	self._DesignParameter['m1_gate_routing_x']['_XYCoordinates'] = [[[(self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][0][0][0] - (self._DesignParameter['m1_drain_routing_y']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])], [(self._DesignParameter['m1_drain_routing_y']['_XYCoordinates'][(- 1)][0][0] + (self._DesignParameter['m1_drain_routing_y']['_Width'] / 2)), (self._DesignParameter['gate_input']['_XYCoordinates'][0][1] + self._DesignParameter['gate_input']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'][0][1])]]]
    #
    # 	self._DesignParameter['_VDDpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VDD')
    # 	self._DesignParameter['_VSSpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL2PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL2PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0], _XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='VSS')
    # 	self._DesignParameter['_TIELpin'] = self._TextElementDeclaration(_Layer=DesignParameters._LayerMapping['METAL1PIN'][0], _Datatype=DesignParameters._LayerMapping['METAL1PIN'][1], _Presentation=[0, 1, 2], _Reflect=[0, 0, 0],_XYCoordinates=[[0, 0]], _Mag=0.05, _Angle=0, _TEXT='TIEL')
    #
    # 	self._DesignParameter['_VDDpin']['_XYCoordinates']=self._DesignParameter['vdd']['_XYCoordinates']
    # 	self._DesignParameter['_VSSpin']['_XYCoordinates']=self._DesignParameter['vss']['_XYCoordinates']
    # 	self._DesignParameter['_TIELpin']['_XYCoordinates']=[[(self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][0]+self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][-1][0])/2, self._DesignParameter['m1_nmos_drain_routing_x']['_XYCoordinates'][0][0][1]]]

if __name__ == '__main__':
    for i in range(0,1):
        #finger=random.randint(1,8)
        #npratio=round(2+random.random())
        print ("sd_width? : ")
        sd_width = int(input())
        print ("gate_spacing? : ")
        gate_spacing = int(input())
        print ("vdd2vss_height? : ")
        vdd2vss_height = int(input())
        print ("nmos_width? : ")
        nmos_width = int(input())
        print ("pmos_width? : ")
        pmos_width = int(input())
        print ("length? : ")
        length = int(input())
        print ("finger? : ")
        finger = int(input())
        
        input_params={'vss2nmos':None,
                    'vdd2pmos':None,
                    'sd_width': sd_width,#66,
                    'gate_spacing':gate_spacing,#96,
                    'vdd2vss_height':vdd2vss_height,#1800,
                    'nmos_width':nmos_width, #random.randrange(200,500,2),
                    'pmos_width':pmos_width, #random.randrange(200,500,2),
                    'length':length ,#random.randrange(36,48,2),
                    'nmos_gate':finger,
                    'pmos_gate':finger,
                    'XVT':'SLVT'}

    #### length 는 46까지, width는 200~400까지

        #DesignParameters._Technology = '028nm'
        _Name = 'TIEL_2X_STD_v1'

        Tie_CellObj = Tie_Cell(_DesignParameter=None, _Name='TIEL_2X_STD_v1')

        Tie_CellObj._CalculateDesignParameter_tielow_v1(**input_params)

        Tie_CellObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=Tie_CellObj._DesignParameter)
        _fileName = 'TIEL_2X_STD_v1.gds'
        testStreamFile = open('./{}'.format(_fileName), 'wb')

        tmp = Tie_CellObj._CreateGDSStream(Tie_CellObj._DesignParameter['_GDSFile']['_GDSFile'])

        tmp.write_binary_gds_stream(testStreamFile)

        testStreamFile.close()