import os, sys
dir_check = os.getcwd()
# if 'auto_encrypted_test' not in dir_check:
#     os.chdir('./auto_encrypted_test')
import block_layer

class NMOS(block_layer.GDS_API):
    def __init__(self, cell_name = 'NMOS'):
        super(NMOS, self).__init__(cell_name)
        self._DesignParameter = dict()

    def calculate_design(self, user_variable=dict(_NMOSChannellength=60, _NMOSChannelWidth=700, _NMOSNumberofGate =30, _NMOSDummy=True)):

        _XYCoordinateOfNMOS = [[0, 0]]

        self._DesignParameter['_POLayer'] = self.boundary_declaration('METAL3')
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
        print(
        _LengthNMOSBtwPO = self.get_drc('DRCPolygateMinSpace',dict(_TmpLengthBtwPolyEdge=
                                                                   self.get_drc('_CoMinWidth') +
                                                                   2 * self.get_drc('_PolygateMinSpace2Co')
                                                                   + self._DesignParameter['_POLayer']['_XWidth']))


        self._DesignParameter['_ODLayer'] = self.boundary_declaration('METAL2')
        self._DesignParameter['_ODLayer']['_XYCoordinates'] = _XYCoordinateOfNMOS
        self._DesignParameter['_ODLayer']['_XWidth'] = _LengthNMOSBtwPO * user_variable['_NMOSNumberofGate'] +\
                                                       self.get_drc('_CoMinWidth') + 2 * self.get_drc('_CoMinEnclosureByOD')
        self._DesignParameter['_ODLayer']['_YWidth'] = user_variable['_NMOSChannelWidth']
        if user_variable['_NMOSDummy'] == True:
            self._DesignParameter['_PODummyLayer'] = self.boundary_declaration('METAL5')
            self._DesignParameter['_PODummyLayer']['_XWidth'] = user_variable['_NMOSChannellength']
            self._DesignParameter['_PODummyLayer']['_YWidth'] = user_variable['_NMOSChannelWidth'] + 2 * self.get_drc('_PolygateMinExtensionOnOD')
            _LengthNMOSBtwPO = self.get_drc('DRCPolygateMinSpace', dict(_TmpLengthBtwPolyEdge=
                                                                        self.get_drc('_CoMinWidth') +
                                                                        2 * self.get_drc('_PolygateMinSpace2Co')
                                                                        + self._DesignParameter['_POLayer']['_XWidth']))

        self.calculate_done()
            # if (user_variable['_NMOSNumberofGate'] % 2) == 0:
            #     _xycoordinatetmp = [
            #         [_XYCoordinateOfNMOS[0][0] - (
            #                     user_variable['_NMOSNumberofGate'] / 2 - 0.5) * _LengthNMOSBtwPO + 0 * _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(
            #             _DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) - (
            #                      float(self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2 + float(
            #                  self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2), _XYCoordinateOfNMOS[0][1]],
            #         [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] / 2 - 0.5) * _LengthNMOSBtwPO + (
            #                     user_variable['_NMOSNumberofGate'] - 1) * _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(
            #             _DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) + float(
            #             self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2 + float(
            #             self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2, _XYCoordinateOfNMOS[0][1]],
            #     ]
        #     elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
        #         _xycoordinatetmp = [
        #             [_XYCoordinateOfNMOS[0][0] - (
        #                         user_variable['_NMOSNumberofGate'] - 1) / 2 * _LengthNMOSBtwPO + 0 * _LengthNMOSBtwPO - _DRCObj.DRCPolygateMinSpace(
        #                 _DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) - (
        #                          float(self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2 + float(
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2), _XYCoordinateOfNMOS[0][1]],
        #             [_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] - 1) / 2 * _LengthNMOSBtwPO + (
        #                         user_variable['_NMOSNumberofGate'] - 1) * _LengthNMOSBtwPO + _DRCObj.DRCPolygateMinSpace(
        #                 _DRCObj._CoMinWidth + _DRCObj._PolygateMinSpace2Co + _DRCObj._CoMinEnclosureByOD + _DRCObj._PolygateMinSpace2OD) + (
        #                          float(self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2 + float(
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']) / 2), _XYCoordinateOfNMOS[0][1]],
        #         ]
        #
        #     # _xycoordinatetmp = [
        #     #                     [self._DesignParameter['_ODLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'][0][0] - float(self._DesignParameter['_ODLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'])/2 - _DRCObj._PolygateMinSpace2OD - float(self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'])/2,  _XYCoordinateOfNMOS[0][1]],
        #     #                     [self._DesignParameter['_ODLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'][0][0] + float(self._DesignParameter['_ODLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'])/2 + _DRCObj._PolygateMinSpace2OD + float(self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'])/2,  _XYCoordinateOfNMOS[0][1]],
        #     #                     # [_XYCoordinateOfNMOS[0][0] - ( user_variable['_NMOSNumberofGate'] / 2 - 0.5) *  _LengthNMOSBtwPO + 0 *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]],
        #     #                     # [_XYCoordinateOfNMOS[0][0] - ( user_variable['_NMOSNumberofGate'] / 2 - 0.5) *  _LengthNMOSBtwPO + (user_variable['_NMOSNumberofGate'] -1) *  _LengthNMOSBtwPO,  _XYCoordinateOfNMOS[0][1]],
        #     #                     ]
        #
        #     self._DesignParameter['_PODummyLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = _xycoordinatetmp
        # else:
        #     self._DesignParameter['_PODummyLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = []
        #
        # print(
        #     '#############################     METAL1 Layer Calcuation    ##############################################')
        # self._DesignParameter['_Met1Layer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] = _DRCObj._CoMinWidth + 2 * _DRCObj._Metal1MinEnclosureCO
        # self._DesignParameter['_Met1Layer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] = self._DesignParameter['_ODLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb']
        # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        #
        # tmp = []
        #
        # for i in range(0, user_variable['_NMOSNumberofGate'] + 1):
        #     if (user_variable['_NMOSNumberofGate'] % 2) == 0:
        #         _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 * \
        #                             _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]
        #     elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
        #         _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
        #                             * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]]
        #
        #     tmp.append(_xycoordinatetmp)
        #
        # self._DesignParameter['_Met1Layer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = tmp
        #
        # print(
        #     '#############################     CONT Layer Calculation    ##############################################')
        # _XNumberOfCOInNMOS = user_variable['_NMOSNumberofGate'] + 1
        # _YNumberOfCOInNMOS = int(float(self._DesignParameter['_ODLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] - 2 * max(
        #     [_DRCObj._CoMinEnclosureByODAtLeastTwoSide, _DRCObj._Metal1MinEnclosureCO2]) + _DRCObj._CoMinSpace) / (
        #                                      _DRCObj._CoMinSpace + _DRCObj._CoMinWidth))
        # self._DesignParameter['_COLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] = _DRCObj._CoMinWidth
        # self._DesignParameter['_COLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] = _DRCObj._CoMinWidth
        #
        # _LengthNMOSBtwCO = _DRCObj._CoMinSpace + self._DesignParameter['_COLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb']
        # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        #
        # tmp = []
        # ###############################################Check the number of CO On NMOS TR##############################################################################################
        # if _XNumberOfCOInNMOS == 0 or _YNumberOfCOInNMOS == 0:
        #     print(
        #         '************************* Error occured in {} Design Parameter Calculation******************************'.format(
        #             self._DesignParameter['_Name']['_Name']))
        #     if DesignParameters._DebugMode == 0:
        #         return 0
        # ###############################################################################################################################################################################
        # for i in range(0, _XNumberOfCOInNMOS):
        #     for j in range(0, _YNumberOfCOInNMOS):
        #
        #         if (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 0:
        #             _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
        #                         _XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
        #                                 _XYCoordinateOfNMOS[0][1] - (
        #                                             _YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
        #
        #         elif (_XNumberOfCOInNMOS % 2) == 1 and (_YNumberOfCOInNMOS % 2) == 1:
        #             _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
        #                         _XNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
        #                                 _XYCoordinateOfNMOS[0][1] - (
        #                                             _YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
        #
        #         elif (_XNumberOfCOInNMOS % 2) == 0 and (_YNumberOfCOInNMOS % 2) == 0:
        #             _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
        #                         _XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
        #                                 _XYCoordinateOfNMOS[0][1] - (
        #                                             _YNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
        #
        #         elif (_XNumberOfCOInNMOS % 2) == 0 and (_YNumberOfCOInNMOS % 2) == 1:
        #             _xycoordinatetmp = [_XYCoordinateOfNMOS[0][0] - (
        #                         _XNumberOfCOInNMOS / 2 - 0.5) * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1,
        #                                 _XYCoordinateOfNMOS[0][1] - (
        #                                             _YNumberOfCOInNMOS - 1) / 2 * _LengthNMOSBtwCO + j * _LengthNMOSBtwCO]
        #         tmp.append(_xycoordinatetmp)
        #
        # self._DesignParameter['_COLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = tmp
        # print('#############################     NIMP Layer Calculation    ####################')
        # self._DesignParameter['_NPLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = _XYCoordinateOfNMOS
        # self._DesignParameter['_NPLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] = self._DesignParameter['_ODLayer'][
        #                                                    '_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] + 2 * _DRCObj._NpMinExtensiononNactive if user_variable['_NMOSDummy'] == False else \
        #     self._DesignParameter['_PODummyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] + abs(
        #         self._DesignParameter['_PODummyLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'][0][0] -
        #         self._DesignParameter['_PODummyLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'][1][0]) + 2 * _DRCObj._NpMinEnclosureOfPo
        # self._DesignParameter['_NPLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] = self._DesignParameter['_POLayer'][
        #                                                    'b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] + 2 * _DRCObj._NpMinEnclosureOfPo
        #
        # if DesignParameters._Technology == '180nm':
        #     print(
        #         '#############################     WELLBODY Layer Calculation    #########################################')
        #     self._DesignParameter['_WELLBodyLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = _XYCoordinateOfNMOS
        #     self._DesignParameter['_WELLBodyLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] = self._DesignParameter['_ODLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        #     self._DesignParameter['_WELLBodyLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] = self._DesignParameter['_ODLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb']
        #
        # if DesignParameters._Technology == '065nm':
        #     print(
        #         '################################     PDK Layer Calculation    ############################################')
        #     self._DesignParameter['_PDKLayer']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = _XYCoordinateOfNMOS
        #     self._DesignParameter['_PDKLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647'] = self._DesignParameter['_NPLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        #     self._DesignParameter['_PDKLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb'] = self._DesignParameter['_NPLayer']['b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb']
        #
        # print(
        #     '#########################     Supply Routing Coordinates Calculation   ##################################')
        # tmp = []
        # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        # if (user_variable['_NMOSNumberofGate'] % 2) == 0:
        #     for i in range(0, user_variable['_NMOSNumberofGate'] // 2 + 1):
        #         # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 \
        #                     * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        # elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
        #     for i in range(0, (user_variable['_NMOSNumberofGate'] - 1) // 2 + 1):
        #         # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
        #                     * _LengthNMOSBtwMet1 + i * 2 * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        #
        # self._DesignParameter['_XYCoordinateNMOSSupplyRouting']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = tmp
        #
        # print(
        #     '#########################     Output Routing Coordinates Calculation    ##################################')
        # tmp = []
        # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        # if (user_variable['_NMOSNumberofGate'] % 2) == 0:
        #     for i in range(0, user_variable['_NMOSNumberofGate'] // 2):
        #         # _XYCenter=[self._XYCoordinateNMOS[0] -  self._NumberOfNMOSGate / 2 * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - user_variable['_NMOSNumberofGate'] / 2 \
        #                     * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        # elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
        #     for i in range(0, (user_variable['_NMOSNumberofGate'] - 1) // 2 + 1):
        #         # _XYCenter=[self._XYCoordinateNMOS[0] - (  (self._NumberOfNMOSGate + 1) / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]]
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - ((user_variable['_NMOSNumberofGate'] + 1) / 2 - 0.5) \
        #                     * _LengthNMOSBtwMet1 + (i * 2 + 1) * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        # self._DesignParameter['_XYCoordinateNMOSOutputRouting']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = tmp
        #
        # print('#########################     Gate Routing Coordinates Calculation   ##################################')
        # tmp = []
        # _LengthNMOSBtwMet1 = _DRCObj.DRCPolygateMinSpace(_DRCObj._CoMinWidth + 2 * _DRCObj._PolygateMinSpace2Co) + \
        #                      self._DesignParameter['_POLayer']['_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647']
        # for i in range(0, user_variable['_NMOSNumberofGate']):
        #     if (user_variable['_NMOSNumberofGate'] % 2) == 0:
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] / 2 - 0.5) \
        #                     * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        #         # _xycoordinatetmp = self.CenterCoordinateAndWidth2XYCoordinate(_XYCenter=[self._XYCoordinateNMOS[0] - (self._NumberOfNMOSGate / 2 - 0.5) * self._LengthBtwMet1 + i * self._LengthBtwMet1, self._XYCoordinateNMOS[1]], _WidthX=self._LengthNMOSPO, _WidthY=self._WidthNMOSPO)
        #     elif (user_variable['_NMOSNumberofGate'] % 2) == 1:
        #         tmp.append([_XYCoordinateOfNMOS[0][0] - (user_variable['_NMOSNumberofGate'] - 1) / 2 \
        #                     * _LengthNMOSBtwMet1 + i * _LengthNMOSBtwMet1, _XYCoordinateOfNMOS[0][1]])
        #
        # self._DesignParameter['_XYCoordinateNMOSGateRouting']['_77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8'] = tmp



if __name__ == '__main__':
    mos_gen = NMOS()
    mos_gen.calculate_design()
    mos_gen.create_gds('nmos_test')