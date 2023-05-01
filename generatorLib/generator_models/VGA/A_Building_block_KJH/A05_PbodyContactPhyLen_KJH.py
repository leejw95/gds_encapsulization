from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import StickDiagram_KJH1
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DesignParameters
from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRC

import numpy as np
import copy
import math

from KJH91_Projects.Project_IORX_VGA_UNIT1.Layoutgen_code.A_Building_block_KJH import A03_PbodyContact_KJH

## ########################################################################################################################################################## Class_HEADER
class _PbodyContactPhyLen_KJH(StickDiagram_KJH1._StickDiagram_KJH):

    ## Define input_parameters for Design calculation
    _ParametersForDesignCalculation = dict(

_Length		= None,
_NumCont	= None,
_Vtc_flag	= None,

                                        )

    ## Initially Defined design_parameter
    def __init__(self, _DesignParameter=None, _Name=None):
        if _DesignParameter != None:
            self._DesignParameter = _DesignParameter
        else:
            self._DesignParameter = dict(
                                            _Name=self._NameDeclaration(_Name=_Name),
                                            _GDSFile=self._GDSObjDeclaration(_GDSFile=None),
                                        )

    ## ################################################################################################################################################ _CalculateDesignParameter
    def _CalculateDesignParameter(self,

_Length		= None,
_NumCont	= None,
_Vtc_flag	= None,

                                  ):

        ## ################################################################################################################################# Class_HEADER: Pre Defined Parameter Before Calculation
        # Load DRC library
        _DRCObj = DRC.DRC()

        # Define _name
        _Name = self._DesignParameter['_Name']['_Name']


        ## ################################################################################################################################# Calculation_Start
        print('##############################')
        print('##     Calculation_Start    ##')
        print('##############################')

            ## ################################################################################################################### Pre-define Parameters
        #Calculation_Parameters
            #VTC
        if _Vtc_flag == True:
            _NumberOfPbodyCOX = _NumCont
            _NumberOfPbodyCOY = ((int(((_Length - (2 * _DRCObj._CoMinEnclosureByOD)) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))) ) + 0) #maximum number of contact

            #Hrz
        else:
            _NumberOfPbodyCOX = ((int(((_Length - (2 * _DRCObj._CoMinEnclosureByOD)) / (_DRCObj._CoMinWidth + _DRCObj._CoMinSpace2))) ) + 0) #maximum number of contact
            _NumberOfPbodyCOY = _NumCont

        #Define Calculation_Parameters
        _Caculation_Parameters = copy.deepcopy(A03_PbodyContact_KJH._PbodyContact_KJH._ParametersForDesignCalculation)
        _Caculation_Parameters['_NumberOfPbodyCOX']  	= _NumberOfPbodyCOX
        _Caculation_Parameters['_NumberOfPbodyCOY']  	= _NumberOfPbodyCOY

        #Generate Sref
        self._DesignParameter['_PbodyContactPhyLen'] = self._SrefElementDeclaration(_DesignObj=A03_PbodyContact_KJH._PbodyContact_KJH( _DesignParameter=None, _Name='{}:_PbodyContactPhyLen'.format(_Name)))[0]

        #Define Sref Relection
        self._DesignParameter['_PbodyContactPhyLen']['_Reflect'] = [0, 0, 0]

        #Define Sref Angle
        self._DesignParameter['_PbodyContactPhyLen']['_Angle'] = 0

        #Calculate Sref Layer by using Calculation_Parameter
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._CalculateDesignParameter(**_Caculation_Parameters)

        #Define Sref _XYcoordinate
        self._DesignParameter['_PbodyContactPhyLen']['_XYCoordinates']=[[0, 0]]


            ## ################################################################################################################### Re-Caculate (OD/RX) Layer
                ## ##################################################################################################### Re-Caculate (OD/RX) Layer: Dummy OD Layer just for Cal
        #Define Boundary_element
        self._DesignParameter['_ODLayer_JustCal'] = self._BoundaryElementDeclaration(
                                                                                        _Layer=DesignParameters._LayerMapping['DIFF'][0],
                                                                                        _Datatype=DesignParameters._LayerMapping['DIFF'][1],
                                                                                        _XWidth=None,
                                                                                        _YWidth=None,
                                                                                        _XYCoordinates=[ ],
                                                                                       )

        #Define Boundary_element _YWidth
        if _Vtc_flag == True:
            self._DesignParameter['_ODLayer_JustCal']['_YWidth'] = _Length
        else:
            tmp = self.get_param_KJH3('_PbodyContactPhyLen','_ODLayer')
            self._DesignParameter['_ODLayer_JustCal']['_YWidth'] = tmp[0][0][0]['_Ywidth']

            
        #Define Boundary_element _XWidth
        if _Vtc_flag == True:
            tmp = self.get_param_KJH3('_PbodyContactPhyLen','_ODLayer')
            self._DesignParameter['_ODLayer_JustCal']['_XWidth'] = tmp[0][0][0]['_Xwidth']
        else:
            self._DesignParameter['_ODLayer_JustCal']['_XWidth'] = _Length
            
        #Define XYcoord.
                #Calculate Sref XYcoord
        tmpXY=[]
            #initialized Sref coordinate
        self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates'] = [[0,0]]
            #Calculate
                #Target_coord
        tmp1 = self.get_param_KJH3('_PbodyContactPhyLen','_ODLayer')
        target_coord = tmp1[0][0][0]['_XY_up_right']
                #Approaching_coord
        tmp2 = self.get_param_KJH3('_ODLayer_JustCal')
        approaching_coord = tmp2[0][0]['_XY_down_left'] ##
                #Sref coord
        tmp3 = self.get_param_KJH3('_ODLayer_JustCal')
        Scoord = tmp3[0][0]['_XY_cent']
                #Cal
        New_Scoord = self.get_Scoord_KJH(target_coord,approaching_coord,Scoord)
        New_Scoord = np.round(New_Scoord,2)
        tmpXY.append(New_Scoord)
            #Define
        self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates'] = tmpXY
        
                ## ##################################################################################################### Re-Caculate (OD/RX) Layer: Substitute to real ODLayer
        #Define Boundary_element _XWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_ODLayer']['_XWidth'] = self._DesignParameter['_ODLayer_JustCal']['_XWidth']
        #Define Boundary_element _YWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_ODLayer']['_YWidth'] = self._DesignParameter['_ODLayer_JustCal']['_YWidth']
        #Define XYcoord.
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_ODLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates']

            ## ################################################################################################################### Re-Caculate Metal1 Layer
        #Define Boundary_element _XWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_Met1Layer']['_XWidth'] = self._DesignParameter['_ODLayer_JustCal']['_XWidth']
        #Define Boundary_element _YWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_Met1Layer']['_YWidth'] = self._DesignParameter['_ODLayer_JustCal']['_YWidth']
        #Define XYcoord.
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_Met1Layer']['_XYCoordinates'] = self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates']

            ## ################################################################################################################### Re-Caculate Nwell Layer
        #Define Boundary_element _XWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_PPLayer']['_XWidth'] = self._DesignParameter['_ODLayer_JustCal']['_XWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
        #Define Boundary_element _YWidth
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer_JustCal']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2
        if self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] < 170:
            self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_PPLayer']['_YWidth'] = self._DesignParameter['_ODLayer_JustCal']['_YWidth'] + 2 * _DRCObj._PpMinExtensiononPactive2 + 28
        #Define XYcoord.
        self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_PPLayer']['_XYCoordinates'] = self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates']

            ## ################################################################################################################### Re-Caculate CONT
        tmp = self.get_param_KJH3('_PbodyContactPhyLen','_COLayer')
        #Defien XY coord
        tmpXY = []
        for i in range(0,len(tmp[0])):
            self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][i] = self._DesignParameter['_PbodyContactPhyLen']['_DesignObj']._DesignParameter['_COLayer']['_XYCoordinates'][i] + self._DesignParameter['_ODLayer_JustCal']['_XYCoordinates'][0]

                ## ##################################################################################################### Delete
        del self._DesignParameter['_ODLayer_JustCal']



        ## ################################################################################################################################# Calculation_End
        print('##############################')
        print('##     Calculation_End      ##')
        print('##############################')

## ########################################################################################################################################################## Start_Main
if __name__ == '__main__':

    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine.Private import MyInfo
    from KJH91_Projects.Project_IORX_VGA_UNIT1.Library_and_Engine import DRCchecker_KJH0

    libname = 'Proj_VGA_A_building_block_KJH'
    cellname = 'A05_PbodyContactPhyLen_KJH_97'
    _fileName = cellname + '.gds'

    ''' Input Parameters for Layout Object '''
    InputParams = dict(

_Length		= 2123,
_NumCont	= 5,
_Vtc_flag	= False,

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
    LayoutObj = _PbodyContactPhyLen_KJH(_DesignParameter=None, _Name=cellname)
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
    # Checker_KJH0.DRCchecker()
    print('#############################      Finished      ################################')
    # end of 'main():' ---------------------------------------------------------------------------------------------




