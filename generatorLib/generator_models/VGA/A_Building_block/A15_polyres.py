from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH0
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import copy

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block import A07_ViaPoly2Met1

class PolyResWithOD(StickDiagram_KJH0._StickDiagram_KJH):
    def __init__(self, _DesignParameter=None, _Name='poly_res_od'):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(_Name=self._NameDeclaration(_Name=_Name), _GDSFile=self._GDSObjDeclaration(_GDSFile=None))
        self._DesignParameter['_Name']['Name'] = _Name

    def _CalculateDesignParameter(self,res_length=800,res_width=400,contact_y=2):

        drc = DRC.DRC()
        _Name = self._DesignParameter['_Name']['_Name']

        self._DesignParameter['OP_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['OP'][0], _Datatype=DesignParameters._LayerMapping['OP'][1], _XWidth=(((drc._OPlayeroverPoly * 2) + res_width) + 0), _YWidth=res_length)
        self._DesignParameter['OP_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['POLY_boundary_48'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['POLY'][0], _Datatype=DesignParameters._LayerMapping['POLY'][1], _XWidth=res_width, _YWidth=((0 + self._DesignParameter['OP_boundary_0']['_YWidth']) + (2 * drc._PolyoverOPlayer)))
        self._DesignParameter['POLY_boundary_48']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['PRES_boundary_0'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PRES'][0], _Datatype=DesignParameters._LayerMapping['PRES'][1], _XWidth=(((drc._PRESlayeroverPoly * 2) + self._DesignParameter['POLY_boundary_48']['_XWidth']) + 0), _YWidth=((0 + (drc._PRESlayeroverPoly * 2)) + self._DesignParameter['POLY_boundary_48']['_YWidth']))
        self._DesignParameter['PRES_boundary_0']['_XYCoordinates'] = [[0.0, 0.0]]
        self._DesignParameter['rectarray_CDNS_6330718089180_1'] = self._SrefElementDeclaration(_DesignObj=A07_ViaPoly2Met1._ViaPoly2Met1(_Name='rectarray_CDNS_6330718089180_1In{}'.format(_Name)))[0]
        self._DesignParameter['rectarray_CDNS_6330718089180_1']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=(int((((res_width + drc._CoMinSpace2) - (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) / (drc._CoMinWidth + drc._CoMinSpace2))) + 0), _ViaPoly2Met1NumberOfCOY=contact_y))
        self._DesignParameter['rectarray_CDNS_6330718089180_1']['_XYCoordinates'] = [[(0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0]), (((((0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1]) + (((- (drc._CoMinSpace2 + drc._CoMinWidth)) / 2) * (contact_y - 1))) + (- drc._CoMinSpace2OP)) + ((- drc._CoMinWidth) / 2)) + ((- self._DesignParameter['OP_boundary_0']['_YWidth']) / 2))]]
        self._DesignParameter['rectarray_CDNS_6330718089180_0'] = self._SrefElementDeclaration(_DesignObj=A07_ViaPoly2Met1._ViaPoly2Met1(_Name='rectarray_CDNS_6330718089180_0In{}'.format(_Name)))[0]
        self._DesignParameter['rectarray_CDNS_6330718089180_0']['_DesignObj']._CalculateViaPoly2Met1DesignParameter(**dict(_ViaPoly2Met1NumberOfCOX=(int((((res_width + drc._CoMinSpace2) - (2 * drc._CoMinEnclosureByPOAtLeastTwoSide)) / (drc._CoMinWidth + drc._CoMinSpace2))) + 0), _ViaPoly2Met1NumberOfCOY=contact_y))
        self._DesignParameter['rectarray_CDNS_6330718089180_0']['_XYCoordinates'] = [[(0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][0]), (((((0 + self._DesignParameter['OP_boundary_0']['_XYCoordinates'][0][1]) + drc._CoMinSpace2OP) + (drc._CoMinWidth / 2)) + (self._DesignParameter['OP_boundary_0']['_YWidth'] / 2)) + (((drc._CoMinSpace + drc._CoMinWidth) / 2) * (contact_y - 1)))]]
        self._DesignParameter['PIMP_boundary_5'] = self._BoundaryElementDeclaration(_Layer=DesignParameters._LayerMapping['PIMP'][0], _Datatype=DesignParameters._LayerMapping['PIMP'][1], _XWidth=(self._DesignParameter['PRES_boundary_0']['_XWidth'] + 0), _YWidth=(0 + self._DesignParameter['PRES_boundary_0']['_YWidth']))
        self._DesignParameter['PIMP_boundary_5']['_XYCoordinates'] = [[0.0, 0.0]]

        print('###############      For Debugging      ##################')


############################################################################################################################################################ START MAIN
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block'
    cellname = 'A15_polyres_99'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(
        res_length=1000,
        res_width=800,
        contact_y=5,
                        )

    '''Mode_DRCCHECK '''
    Mode_DRCCheck = False
    Num_DRCCheck =1

    for ii in range(0, Num_DRCCheck if Mode_DRCCheck else 1):
        if Mode_DRCCheck:
            ''' Input Parameters for Layout Object '''
        else:
            pass

    ''' Generate Layout Object '''
    LayoutObj = PolyResWithOD(_DesignParameter=None, _Name=cellname)
    LayoutObj._CalculateDesignParameter(**InputParams)
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
    #Checker.lib_deletion()
    Checker.cell_deletion()
    Checker.Upload2FTP()
    Checker.StreamIn(tech=DesignParameters._Technology)
    #Checker_KJH0.DRCchecker()

    print ('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------
