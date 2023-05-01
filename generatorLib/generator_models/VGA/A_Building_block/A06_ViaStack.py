from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import importlib
import os

import inspect

class _ViaStack(StickDiagram_KJH0._StickDiagram_KJH):
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter!=None:
            self._DesignParameter=_DesignParameter
        else :
            self._DesignParameter = dict(
                                                    _Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None)
                                                   )



        if _Name != None:
            self._DesignParameter['_Name']['_Name']=_Name


    def _CalculateStack(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'ViaPoly2Met1'
            else:
                lib_name = f'ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'Enclosure' not in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

    def _CalculateStackMinimumEnclosureX(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'A07_ViaPoly2Met1'
            else:
                lib_name = f'A{layer+7}_ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'EnclosureX' in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

    def _CalculateStackMinimumEnclosureY(self, COX=None, COY=None, start_layer=None, end_layer=None ):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0 :
                lib_name = 'ViaPoly2Met1'
            else:
                lib_name = f'ViaMet{layer}2Met{layer+1}'
            lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'EnclosureY' in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(_DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox : COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0,0]]

    def _CalculateStackSameEnclosure(self, COX=None, COY=None, start_layer=None, end_layer=None):
        layer_list = range(start_layer, end_layer)
        for layer in layer_list:
            if layer == 0:
                lib_name = 'A07_ViaPoly2Met1'
            elif layer== 1:
                lib_name = 'A08_ViaMet12Met2'
            elif layer == 2:
                lib_name = 'A09_ViaMet22Met3'
            elif layer == 3:
                lib_name = 'A10_ViaMet32Met4'
            elif layer == 4:
                lib_name = 'A11_ViaMet42Met5'
            elif layer == 5:
                lib_name = 'A12_ViaMet52Met6'
            elif layer == 6:
                lib_name = 'A13_ViaMet62Met7'
            elif layer == 7:
                lib_name = 'A14_ViaMet72Met8'
            else:
                pass

            lib = importlib.import_module('KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block.{}'.format(lib_name))
            #lib = __import__(lib_name)
            for name, obj in inspect.getmembers(lib):
                if inspect.isclass(obj):
                    class_obj = obj
                    fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if
                                "Calculate" in fcn_name]
                    fcn_list2 = list(
                        filter(lambda fcn: 'SameEnclosure' in fcn[0] and 'DesignParameter' in fcn[0], fcn_list))
                    fcn_obj = fcn_list2[0][1]
                    fcn_name = fcn_list2[0][0]
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    args_name = [arg.name for arg in args]
                    break
            self._DesignParameter[lib_name] = self._SrefElementDeclaration(
                _DesignObj=class_obj(_Name=f"{lib_name}in{self._DesignParameter['_Name']['_Name']}"))[0]
            calculate_fcn = getattr(self._DesignParameter[lib_name]['_DesignObj'], fcn_name)
            cox = list(filter(lambda arg: 'COX' in arg, args_name))[0]
            coy = list(filter(lambda arg: 'COY' in arg, args_name))[0]
            parameters = {cox: COX, coy: COY}
            calculate_fcn(**parameters)
            self._DesignParameter[lib_name]['_XYCoordinates'] = [[0, 0]]




##################################################### MAIN #############################################################
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A06_ViaStack_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
                            COX = 3,
                            COY = 10,
                            start_layer = 0,
                            end_layer = 0,

    )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck = 1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = _ViaStack(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateStackSameEnclosure(**InputParams)
    LayoutObj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=LayoutObj._DesignParameter)
    testStreamFile = open('./{}'.format(_fileName), 'wb')
    tmp = LayoutObj._CreateGDSStream(LayoutObj._DesignParameter['_GDSFile']['_GDSFile'])
    tmp.write_binary_gds_stream(testStreamFile)
    testStreamFile.close()

    print('###############      Sending to FTP Server...      ##################')
    My = MyInfo.USER(DesignParameters._Technology)
    Checker = DRCchecker_KJH0.DRCchecker_KJH0(
        username=My.ID,
        password=My.PW,
        WorkDir=My.Dir_Work,
        DRCrunDir=My.Dir_DRCrun,
        libname=libname,
        cellname=cellname,
        GDSDir=My.Dir_GDS
    )
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    # Checker.DRCchecker()

    print('#############################      Finished      ################################')
# end of 'main():' ---------------------------------------------------------------------------------------------