import ntplib
from time import ctime
#
# if datetime (server) >day and datetime <day (1month):
#     asf= open(ss.lic,'w')
#     if asf.readlines() == '8cXSRdf215SDF':
#         pass
#     else:
#         raise Exception("License expired or invalid")

import os, sys
dir_check = os.getcwd()
# if 'auto_encrypted_test' not in dir_check:
#     os.chdir('./auto_encrypted_test')
import block_layer

class NMOS(block_layer.GDS_API):
    def __init__(self, cell_name = 'NMOS'):
        super(NMOS, self).__init__(cell_name)
        self._DesignParameter = dict()

    def calculate_design(self, user_variable=dict(_NMOSChannellength=60, _NMOSChannelWidth=700, _NMOSNumberofGate =4, _NMOSDummy=True)):

        _XYCoordinateOfNMOS = [[0, 0]]

        self._DesignParameter['_POLayer'] = self.boundary_declaration('POLY')
        self._DesignParameter['_POLayer']['_XWidth'] = user_variable['_NMOSChannellength']
        self._DesignParameter['_POLayer']['_YWidth'] = user_variable['_NMOSChannelWidth'] + 2 * self.get_drc('_PolygateMinExtensionOnOD')
        _LengthNMOSBtwPO = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=
                                                                   self.get_drc('_CoMinWidth') +
                                                                   2 * self.get_drc('_PolygateMinSpace2Co')
                                                                   + self._DesignParameter['_POLayer']['_XWidth']))
        tmp = []
        for i in range(0, user_variable['_NMOSNumberofGate']):
            if (user_variable['_NMOSNumberofGate'] % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] / 2 - 0.5) \
                                    * _LengthNMOSBtwPO + i * _LengthNMOSBtwPO, _XYCoordinateOfNMOS[0][1]]
            elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] - 1) / 2 \
                                    * _LengthNMOSBtwPO + i * _LengthNMOSBtwPO, _XYCoordinateOfNMOS[0][1]]
            tmp.append(_xycoordinatetmp)
        self._DesignParameter['_POLayer']['_XYCoordinates'] = tmp
        _LengthNMOSBtwPO = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=
                                                                   self.get_drc('_CoMinWidth') +
                                                                   2 * self.get_drc('_PolygateMinSpace2Co')
                                                                   + self._DesignParameter['_POLayer']['_XWidth']))


        self._DesignParameter['_ODLayer'] = self.boundary_declaration('DIFF')
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        self._DesignParameter['_ODLayer']['_XWidth'] = _LengthNMOSBtwPO * user_variable['_NMOSNumberofGate'] +\
                                                       self.get_drc('_CoMinWidth') + 2 * self.get_drc('_CoMinEnclosureByOD')
        self._DesignParameter['_ODLayer']['_YWidth'] = user_variable['_NMOSChannelWidth']
        if user_variable['_NMOSDummy'] == True:
            self._DesignParameter['_PODummyLayer'] = self.boundary_declaration('POLY')
            self._DesignParameter['_PODummyLayer']['_XWidth'] = user_variable['_NMOSChannellength']
            self._DesignParameter['_PODummyLayer']['_YWidth'] = user_variable['_NMOSChannelWidth'] + 2 * self.get_drc('_PolygateMinExtensionOnOD')
            _LengthNMOSBtwPO = self.get_drc('DRCPolygateMinSpace', dict(_TmpLengthBtwPolyEdge=
                                                                        self.get_drc('_CoMinWidth') +
                                                                        2 * self.get_drc('_PolygateMinSpace2Co')
                                                                        + self._DesignParameter['_POLayer']['_XWidth']))

        # self.calculate_done()
        if (user_variable['_NMOSNumberofGate'] % 2) == 0:
            _xycoordinatetmp = [
                [_XYCoordinateOfNMOS[0][0] - (
                user_variable['_NMOSNumberofGate'] / 2 - 0.5) * _LengthNMOSBtwPO + 0 * _LengthNMOSBtwPO -
                self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + self.get_drc('_PolygateMinSpace2Co') + self.get_drc('_CoMinEnclosureByOD') + self.get_drc('_PolygateMinSpace2OD')))
                             - (float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 +
                                float(self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfNMOS[0][1]],
                [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] / 2 - 0.5) * _LengthNMOSBtwPO + (
                            user_variable['_NMOSNumberofGate'] - 1) * _LengthNMOSBtwPO + self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=
                    self.get_drc('_CoMinWidth') + self.get_drc('_PolygateMinSpace2Co') + self.get_drc('_CoMinEnclosureByOD') + self.get_drc('_PolygateMinSpace2OD'))) + float(
                    self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(
                    self._DesignParameter['_POLayer']['_XWidth']) / 2, _XYCoordinateOfNMOS[0][1]],
            ]
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp
        elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
            _xycoordinatetmp = [
                [_XYCoordinateOfNMOS[0][0] - (
                            user_variable['_NMOSNumberofGate'] - 1) / 2 * _LengthNMOSBtwPO + 0 * _LengthNMOSBtwPO - self.get_drc('DRCPolygateMinSpace',(
                    self.get_drc('_CoMinWidth') + self.get_drc('_PolygateMinSpace2Co') + self.get_drc('_CoMinEnclosureByOD') + self.get_drc('_PolygateMinSpace2OD'))) - (
                             float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(
                         self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfNMOS[0][1]],
                [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] - 1) / 2 * _LengthNMOSBtwPO + (
                            user_variable['_NMOSNumberofGate'] - 1) * _LengthNMOSBtwPO + self.get_drc('DRCPolygateMinSpace',
                    self.get_drc('_CoMinWidth') + self.get_drc('_PolygateMinSpace2Co') + self.get_drc('_CoMinEnclosureByOD') + self.get_drc('_PolygateMinSpace2OD')) + (
                             float(self._DesignParameter['_PODummyLayer']['_XWidth']) / 2 + float(
                         self._DesignParameter['_POLayer']['_XWidth']) / 2), _XYCoordinateOfNMOS[0][1]],
            ]

            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = _xycoordinatetmp
        else:
            self._DesignParameter['_PODummyLayer']['_XYCoordinates'] = []

        # print(
        #     '#############################     METAL1 Layer Calcuation    ##############################################')
        self._DesignParameter['_Met1Layer'] = self.boundary_declaration('METAL1')
        self._DesignParameter['_Met1Layer']['_XWidth'] = self.get_drc('_CoMinWidth') + 2 * self.get_drc('_Metal1MinEnclosureCO')
        self._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        _LengthNMOSBtwMet1 = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + 2 * self.get_drc('_PolygateMinSpace2Co'))) + \
                             self._DesignParameter['_POLayer']['_XWidth']

        tmp = []

        for i in range(0, user_variable['_NMOSNumberofGate'] + 1):
            if (user_variable['_NMOSNumberofGate'] % 2) == 0:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 * \
                                    _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]
            elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
                _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
                                    * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]

            tmp.append(_xycoordinatetmp)

        self._DesignParameter['_Met1Layer']['_XYCoordinates'] = tmp

        _XNumberOfCOInNMOS = user_variable['_NMOSNumberofGate'] + 1
        _YNumberOfCOInNMOS = int(float(self._DesignParameter['_ODLayer']['_YWidth'] - 2 * max(
            [self.get_drc('_CoMinEnclosureByODAtLeastTwoSide'), self.get_drc('_Metal1MinEnclosureCO2')]) + self.get_drc('_CoMinSpace') / (
                                             self.get_drc('_CoMinSpace') + self.get_drc('_CoMinWidth'))))
        self._DesignParameter['_COLayer'] = self.boundary_declaration('CONT')
        self._DesignParameter['_COLayer']['_YWidth'] = self.get_drc('_CoMinWidth')
        self._DesignParameter['_COLayer']['_XWidth'] = self.get_drc('_CoMinWidth')

        _LengthNMOSBtwCO = self.get_drc('_CoMinSpace') + self._DesignParameter['_COLayer']['_YWidth']
        _LengthNMOSBtwMet1 = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + 2 * self.get_drc('_PolygateMinSpace2Co'))) + \
                             self._DesignParameter['_POLayer']['_XWidth']

        tmp = []
        for i in range(0, _XNumberOfCOInNMOS):
            for j in range(0, _YNumberOfCOInNMOS):
                if (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
                                _XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (
                                                    _YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
                                _XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (
                                                    _YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 0 and (_YNumberOfCOInNMOS % 2) == 0:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
                                _XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (
                                                    _YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]

                elif (_XNumberOfCOInNMOS % 2) == 0 and (_YNumberOfCOInNMOS % 2) == 1:
                    _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
                                _XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
                                        _XYCoordinateOfNMOS[0][1] - (
                                                    _YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
                tmp.append(_xycoordinatetmp)

        self._DesignParameter['_COLayer']['_XYCoordinates'] = tmp

        self._DesignParameter['_NPLayer'] = self.boundary_declaration('NIMP')
        self._DesignParameter['_NPLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        self._DesignParameter['_NPLayer']['_XWidth'] = self._DesignParameter['_ODLayer'][
                                                           '_XWidth'] + 2 * self.get_drc('_NpMinExtensiononNactive') if user_variable['_NMOSDummy'] == False else \
            self._DesignParameter['_PODummyLayer']['_XWidth'] + abs(
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'][0][0] -
                self._DesignParameter['_PODummyLayer']['_XYCoordinates'][1][0]) + 2 * self.get_drc('_NpMinEnclosureOfPo')
        self._DesignParameter['_NPLayer']['_YWidth'] = self._DesignParameter['_POLayer']['_YWidth'] + 2 * self.get_drc('_NpMinEnclosureOfPo')
        #
        # if DesignParameters._Technology == '180nm':
        #     print(
        #         '#############################     WELLBODY Layer Calculation    #########################################')
        #     self._DesignParameter['_WELLBodyLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        #     self._DesignParameter['_WELLBodyLayer']['_XWidth'] = self._DesignParameter['_ODLayer']['_XWidth']
        #     self._DesignParameter['_WELLBodyLayer']['_YWidth'] = self._DesignParameter['_ODLayer']['_YWidth']
        #
        self._DesignParameter['_PDKLayer'] = self.boundary_declaration('PDK')
        self._DesignParameter['_PDKLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        self._DesignParameter['_PDKLayer']['_XWidth'] = self._DesignParameter['_NPLayer']['_XWidth']
        self._DesignParameter['_PDKLayer']['_YWidth'] = self._DesignParameter['_NPLayer']['_YWidth']
        #
        # print(
        #     '#########################     Supply Routing Coordinates Calculation   ##################################')
        tmp = []
        _LengthNMOSBtwMet1 = self.get_drc('DRCPolygateMinSpace', dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + 2 * self.get_drc('_PolygateMinSpace2Co'))) + \
                             self._DesignParameter['_POLayer']['_XWidth']
        if (user_variable['_NMOSNumberofGate'] % 2) == 0:
            for i in range(0, user_variable['_NMOSNumberofGate'] // 2 + 1):
                # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 \
                            * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
            for i in range(0, (user_variable['_NMOSNumberofGate'] - 1) // 2 + 1):
                # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
                            * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])

        tmp = []
        _LengthNMOSBtwMet1 = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + 2 * self.get_drc('_PolygateMinSpace2Co'))) + \
                             self._DesignParameter['_POLayer']['_XWidth']
        if (user_variable['_NMOSNumberofGate'] % 2) == 0:
            for i in range(0, user_variable['_NMOSNumberofGate'] // 2):
                # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 \
                            * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
            for i in range(0, (user_variable['_NMOSNumberofGate'] - 1) // 2 + 1):
                # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
                tmp.append([_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
                            * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        tmp = []
        _LengthNMOSBtwMet1 = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=self.get_drc('_CoMinWidth') + 2 * self.get_drc('_PolygateMinSpace2Co'))) + \
                             self._DesignParameter['_POLayer']['_XWidth']
        for i in range(0, user_variable['_NMOSNumberofGate']):
            if (user_variable['_NMOSNumberofGate'] % 2) == 0:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] / 2 - 0.5) \
                            * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
            elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
                tmp.append([_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] - 1) / 2 \
                            * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])

        self.calculate_done()

if __name__ == '__main__':
    mos_gen = NMOS()
    mos_gen.calculate_design()
    mos_gen.create_gds('nmos_test')