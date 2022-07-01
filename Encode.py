import ast
import astunparse
import hashlib

class name_change(ast.NodeTransformer) :
    # def visit_Name (self, node) :
    #     if node.id in ['print', 'self'] :
    #         node.id = node.id
    #     else :
    #         node.id = hashlib.sha256(node.id.encode()).hexdigest()
    #         if ord(node.id[0]) in range (48,58) :
    #             node.id = '_' + node.id 
    #         self.generic_visit(node)
    #     return node
    #     # node.attr = hashlib.sha256(node.attr.encode()).hexdigest()
    #     # if ord(node.attr[0]) in range (48,58) :
    #     #     node.attr = '_' + node.attr 
    #     # self.generic_visit(node)
    #     # return node
    # def visit_Attribute (self, node) :
    #     node.attr = hashlib.sha256(node.attr.encode()).hexdigest()
    #     if ord(node.attr[0]) in range (48,58) :
    #         node.attr = '_' + node.attr 
    #     self.generic_visit(node)
    #     return node
    def generic_visit(self, node):
        for field, old_value in ast.iter_fields(node):
            if type(old_value) == str:
                if old_value[:1] == '>':
                    pass
                if old_value[:2] in ['>h', '>H', '^\\', '>Q', '>d']:
                    pass
                elif old_value[:5] in ['exces']:
                    pass
                elif old_value not in ['self', 'print', 'range', 're', 'math', 'datetime', 'MINYEAR', 'copy', 'open', 'readlines', 'readline', 'format', 'now', 'sha256', 'types', 'tuple', 'staticmethod', 'NotImplemented', 'NotImplementedError', 'enumerate', 'type', 'bytes',
                                     'Exception','and','exec','not','assert','finally','or','break','for','pass','class','from','print', 'seek', 'close', 'items', 'random',
                                     'continue','global','raise','def','if','return','del','import','try','elif','in','while','else','is', 'split', 'update', 'isdigit',
                                     'with','except','lambda','yield','True','False','None','self','struct', '__init__', 'locals', '__dict__', 'new', 'hexdigest',
                                     '__del__','__add__','__repr__','__len__','__file__','__all__','sys','os','dict','str','int','float','round','len','getcwd', '_',
                                     'append','deepcopy','globals','doctest','testmod','warnings','warn','pop','getenv','platform','win32','linux2','match', 'encode',
                                     '>', 's', 'excess64_8byte_encode', 'unpack', 'divmod', 'min', 'max', 'abs','list','set', 'sum', 'zip', 'list', 'set', 'nonlocal',
                                     'pack', 'calcsize', 'write', 'year', 'month', 'day', 'hour', 'minute', 'second', '__name__','__main__', 'items', 'hashlib','/tsmcN65.layermap',
                                       'Demo version supports maximum 20 elements per structure.', 'Demo version does not support lower layer','Demo version supports maximum 20 structure.',
                                       "Connect to Internet", 'urllib', 'request','urlopen','headers','http://www.kriss.re.kr','Date','Jun 2022','Jul 2022', 'Sep 2022', 'Oct 2022',
                                       'Connect to Internet', 'License Expired', 'urllib.request', 'urllib.error', '/cmos28lp_tech.layermap',
                                       'Tie_Cell', 'NMOSWithDummy', 'PMOSWithDummy', 'SupplyRails', 'ViaPoly2Met1', 'CoordinateCalc']:
                    sha = hashlib.new('sha256')
                    sha.update(old_value.encode())
                    hash_str = sha.hexdigest()
                    if hash_str[0].isdigit():
                        hash_str = '_' + hash_str
                    node.__dict__[field] = hash_str
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, ast.AST):
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif not isinstance(value, ast.AST):
                            new_values.extend(value)
                            continue
                    new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, ast.AST):
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
        return node
    # def visit_Call(self, node) :
    #     for field, old_value in ast.iter_fields(node):
    #         if field != 'func' :
    #             if isinstance(old_value, list):
    #                 new_values = []
    #                 for value in old_value:
    #                     if isinstance(value, ast.AST):
    #                         value = self.visit(value)
    #                         if value is None:
    #                             continue
    #                         elif not isinstance(value, ast.AST):
    #                             new_values.extend(value)
    #                             continue
    #                     new_values.append(value)
    #                 old_value[:] = new_values
    #             elif isinstance(old_value, ast.AST):
    #                 new_node = self.visit(old_value)
    #                 if new_node is None:
    #                     delattr(node, field)
    #                 else:
    #                     setattr(node, field, new_node)
    #     return node
def hashing(key:str):
    sha = hashlib.new('sha256')
    sha.update(key.encode())
    hash_str = sha.hexdigest()
    if hash_str[0].isdigit():
        hash_str = '_' + hash_str
    return hash_str


def main_1():
    test = ast.parse(open('./Tie_Cell.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('Tie_Cell') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./NMOSWithDummy.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('NMOSWithDummy') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./PMOSWithDummy.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('PMOSWithDummy') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./SupplyRails.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('SupplyRails') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./ViaPoly2Met1.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('ViaPoly2Met1') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./CoordinateCalc.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = ('CoordinateCalc') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    US = ast.parse(open('./user_setup.py').read())
    US_1 = name_change()
    US_out = US_1.visit(US)
    f_name = hashing('user_setup') +'.py'
    US_w = open('./auto_encrypted_test/'+f_name,'w')
    US_w.write(astunparse.unparse(US_out))

    DP = ast.parse(open('./generatorLib/DesignParameters.py').read())
    DP_1 = name_change()
    DP_out = DP_1.visit(DP)
    f_name = hashing('DesignParameters') +'.py'
    DP_w = open('./auto_encrypted_test/'+f_name,'w')
    DP_w.write(astunparse.unparse(DP_out))

    DRC = ast.parse(open('./generatorLib/DRC.py').read())
    DRC_1 = name_change()
    DRC_out = DRC_1.visit(DRC)
    f_name = hashing('DRC') + '.py'
    DRC_w = open('./auto_encrypted_test/'+f_name,'w')
    DRC_w.write(astunparse.unparse(DRC_out))

    Stick = ast.parse(open('./generatorLib/StickDiagram.py').read())
    Stick_1 = name_change()
    Stick_out = Stick_1.visit(Stick)
    f_name = hashing('StickDiagram') + '.py'
    Stick_w = open('./auto_encrypted_test/'+f_name,'w')
    Stick_w.write(astunparse.unparse(Stick_out))

    GDS_EL = ast.parse(open('./gds_editor_ver3/gds_elements.py').read())
    GDS_EL_1 = name_change()
    GDS_EL_out = GDS_EL_1.visit(GDS_EL)
    f_name = hashing('gds_elements') + '.py'
    GDS_EL_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_EL_w.write(astunparse.unparse(GDS_EL_out))

    GDS_R = ast.parse(open('./gds_editor_ver3/gds_record.py').read())
    GDS_R_1 = name_change()
    GDS_R_out = GDS_R_1.visit(GDS_R)
    f_name = hashing('gds_record') + '.py'
    GDS_R_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_R_w.write(astunparse.unparse(GDS_R_out))

    GDS_STREAM = ast.parse(open('./gds_editor_ver3/gds_stream.py').read())
    GDS_STREAM_1 = name_change()
    GDS_STREAM_out = GDS_STREAM_1.visit(GDS_STREAM)
    f_name = hashing('gds_stream') + '.py'
    GDS_STREAM_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_STREAM_w.write(astunparse.unparse(GDS_STREAM_out))

    GDS_structure = ast.parse(open('./gds_editor_ver3/gds_structures.py').read())
    GDS_structure_1 = name_change()
    GDS_structure_out = GDS_structure_1.visit(GDS_structure)
    f_name = hashing('gds_structures') + '.py'
    GDS_structure_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_structure_w.write(astunparse.unparse(GDS_structure_out))

    gds_tags = ast.parse(open('./gds_editor_ver3/gds_tags.py').read())
    gds_tags_1 = name_change()
    gds_tags_out = gds_tags_1.visit(gds_tags)
    f_name = hashing('gds_tags') + '.py'
    gds_tags_w = open('./auto_encrypted_test/'+f_name,'w')
    gds_tags_w.write(astunparse.unparse(gds_tags_out))

    user_d = ast.parse(open('./gds_editor_ver3/user_define_exceptions.py').read())
    user_d_1 = name_change()
    user_d_out = user_d_1.visit(user_d)
    f_name = hashing('user_define_exceptions') + '.py'
    user_d_w = open('./auto_encrypted_test/'+f_name,'w')
    user_d_w.write(astunparse.unparse(user_d_out))

def main_2():
    def hashing(key:str):
        sha = hashlib.new('sha256')
        sha.update(key.encode())
        hash_str = sha.hexdigest()
        if hash_str[0].isdigit():
            hash_str = '_' + hash_str
        return hash_str

    def lineup(str_line:list):
        strFormat = '%-15s%-15s%-21s%-16s\n'
        return strFormat % (str_line[0], str_line[1], str_line[2], str_line[3])


    file_ = open('tsmcN65.layermap').readlines()
    for i, line in enumerate(file_):
        if i< 4:
            continue


        a = line.split()
        a[0] = hashing(a[0])
        a[1] = hashing(a[1])
        print(lineup(a))


main_1()