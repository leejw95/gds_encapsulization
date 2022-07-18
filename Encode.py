import ast
import astunparse
import hashlib
import keyword
import inspect, math, copy
import glob, sys, os, user_setup, platform, pickle, gzip

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

        expired_date = ['Jul 2022', 'Sep 2022', 'Oct 2022']
        
        exception_list = ['self', 'print', 'range', 're', 'math', 'datetime', 'MINYEAR', 'MAXYEAR', 'copy', 'open', 'readlines', 'readline', 'format', 'now', 'sha256', 'types', 'tuple', 'staticmethod', 'classmethod', 'NotImplemented', 'NotImplementedError', 'enumerate', 'type', 'bytes',
                        'Exception','and','exec','not','assert','finally','or','break','for','pass','class','from','print', 'seek', 'close', 'items', 'random', 'input', 'center','getmembers','isclass',
                        'continue','global','raise','def','if','return','del','import','try','elif','in','while','else','is', 'split', 'update', 'isdigit', 'eval', 'isinstance', 'sorted', 'inspect', '__import__','filter',
                        'with','except','lambda','yield','True','False','None','self','struct', '__init__', 'locals', '__dict__', 'new', 'hexdigest', 'pickle', 'gzip', 'traceback', 'print_exc', 'parameters', 'values', 'name',
                        '__del__','__add__','__repr__','__len__','__file__','__all__','sys','os','dict','str','int','float','round','len','getcwd', '_', 'getattr',
                        'append','deepcopy','globals','doctest','testmod','warnings','warn','pop','getenv','platform','win32','linux2','match', 'encode',
                        '>', 's', 'excess64_8byte_encode', 'unpack', 'divmod', 'min', 'max', 'abs','list','set', 'sum', 'zip', 'list', 'set', 'nonlocal',
                        'pack', 'calcsize', 'write', 'year', 'month', 'day', 'hour', 'minute', 'second', '__name__','__main__', 'items', 'hashlib','/tsmcN65.layermap',
                        'Demo version supports maximum 20 elements per structure.', 'Demo version does not support lower layer','Demo version supports maximum 20 structure.',
                        'urllib', 'request','urlopen','headers','http://www.kriss.re.kr','Date',
                        'Connect to Internet', 'License Expired', 'urllib.request', 'urllib.error', '/cmos28lp_tech.layermap',
                        'wb', 'rb']
        
        exception_list.extend(dir(inspect))
        exception_list.extend(dir(math))
        exception_list.extend(dir(copy))
        exception_list.extend(expired_date)

        for field, old_value in ast.iter_fields(node):
            if type(old_value) == str:
                if old_value[:1] == '>':
                    pass
                if old_value[:2] in ['>h', '>H', '^\\', '>Q', '>d']:
                    pass
                elif old_value[:5] in ['exces']:
                    pass
                elif '{' in old_value or '%' in old_value:
                    pass
                elif old_value not in exception_list:
                    sha = hashlib.new('sha256')
                    sha.update(old_value.encode())
                    hash_str = sha.hexdigest()
                    if hash_str[0].isdigit():
                        hash_str = '_' + hash_str
                    node.__dict__[field] = hash_str
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, ast.keyword) :
                        if value.arg == '_TEXT' :
                            # print (value.arg)
                            # print (value.value.value)
                            sha = hashlib.new('sha256')
                            sha.update(value.arg.encode())
                            hash_str = sha.hexdigest()
                            if hash_str[0].isdigit():
                                hash_str = '_' + hash_str
                            value.arg = hash_str
                            new_values.append(value)
                            continue
                        pass
                    if isinstance(value, ast.AST):
                        # if isinstance(value, ast.Attribute):
                        #     continue
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif not isinstance(value, ast.AST):
                            new_values.extend(value)
                            continue
                    elif type(value) == str:
                        sha = hashlib.new('sha256')
                        sha.update(value.encode())
                        hash_str = sha.hexdigest()
                        if hash_str[0].isdigit():
                            hash_str = '_' + hash_str
                        value = hash_str
                    new_values.append(value)
                old_value[:] = new_values
            
            elif isinstance(old_value, ast.AST):
                if isinstance(old_value, ast.Attribute) and old_value.attr == 'format' and isinstance(old_value.value, ast.Constant):
                    continue
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
                if isinstance(old_value, ast.Name):
                    if old_value.id == 'print' :
                        node = ast.Pass()
                        
        if isinstance(node, ast.ImportFrom):
            if node.module in ['datetime'] : ## The import class not in the local directory
                pass
            else :
                # print (node.module)
                tmp_node = ast.Import()
                tmp_node.names = node.names
                return tmp_node

        # if isinstance(node, ast.keyword) :
        #     if node.arg :
        #         print(node.arg)
        
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
    # test = ast.parse(open('./test.py').read())
    # # print (astunparse.dump(test))
    # # if isinstance(test, ast.Assign):
    # #     print (1)
    
    
    # test_1 = name_change()
    # test_out = test_1.visit(test)
    # f_name = ('test') +'.py'
    # test_w = open('./auto_encrypted_test/'+f_name,'w')
    # test_w.write(astunparse.unparse(test_out))


    En_list = []
    dir_check=os.getcwd()
    if 'generator_model_path' in user_setup.__dict__ and user_setup.generator_model_path:
        generator_model_path = user_setup.generator_model_path
    else:
        generator_model_path = './generatorLib/generator_models'
    for generator in glob.iglob(f'{generator_model_path}/*.py') :
        if platform.system() in ['Linux', 'Darwin'] :
            generator_class_name = generator.split('/')[-1][:-3]
        else :
            generator_class_name = generator.split('\\')[1][:-3]
        En_list.append(generator_class_name)

    for gen in En_list :
        A = ast.parse(open('./generatorLib/generator_models/'+gen+'.py').read())
        A_1 = name_change()
        A_out = A_1.visit(A)
        f_name = hashing(gen) + '.py'
        f_w = open('./auto_encrypted_test/'+f_name, 'w')
        f_w.write(astunparse.unparse(A_out))
    
    test = ast.parse(open('./Encode_list/Trans.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = hashing('Trans') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    test = ast.parse(open('./Encode_list/CoordinateCalc.py').read())
    test_1 = name_change()
    test_out = test_1.visit(test)
    f_name = hashing('CoordinateCalc') +'.py'
    test_w = open('./auto_encrypted_test/'+f_name,'w')
    test_w.write(astunparse.unparse(test_out))

    US = ast.parse(open('./Encode_list/user_setup.py').read())
    US_1 = name_change()
    US_out = US_1.visit(US)
    f_name = hashing('user_setup') +'.py'
    US_w = open('./auto_encrypted_test/'+f_name,'w')
    US_w.write(astunparse.unparse(US_out))

    DP = ast.parse(open('./Encode_list/DesignParameters.py').read())
    DP_1 = name_change()
    DP_out = DP_1.visit(DP)
    f_name = hashing('DesignParameters') +'.py'
    DP_w = open('./auto_encrypted_test/'+f_name,'w')
    DP_w.write(astunparse.unparse(DP_out))

    DRC = ast.parse(open('./Encode_list/DRC.py').read())
    DRC_1 = name_change()
    DRC_out = DRC_1.visit(DRC)
    f_name = hashing('DRC') + '.py'
    DRC_w = open('./auto_encrypted_test/'+f_name,'w')
    DRC_w.write(astunparse.unparse(DRC_out))

    Stick = ast.parse(open('./Encode_list/StickDiagram.py').read())
    Stick_1 = name_change()
    Stick_out = Stick_1.visit(Stick)
    f_name = hashing('StickDiagram') + '.py'
    Stick_w = open('./auto_encrypted_test/'+f_name,'w')
    Stick_w.write(astunparse.unparse(Stick_out))

    GDS_EL = ast.parse(open('./Encode_list/gds_elements.py').read())
    GDS_EL_1 = name_change()
    GDS_EL_out = GDS_EL_1.visit(GDS_EL)
    f_name = hashing('gds_elements') + '.py'
    GDS_EL_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_EL_w.write(astunparse.unparse(GDS_EL_out))

    GDS_R = ast.parse(open('./Encode_list/gds_record.py').read())
    GDS_R_1 = name_change()
    GDS_R_out = GDS_R_1.visit(GDS_R)
    f_name = hashing('gds_record') + '.py'
    GDS_R_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_R_w.write(astunparse.unparse(GDS_R_out))

    GDS_STREAM = ast.parse(open('./Encode_list/gds_stream.py').read())
    GDS_STREAM_1 = name_change()
    GDS_STREAM_out = GDS_STREAM_1.visit(GDS_STREAM)
    f_name = hashing('gds_stream') + '.py'
    GDS_STREAM_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_STREAM_w.write(astunparse.unparse(GDS_STREAM_out))

    GDS_structure = ast.parse(open('./Encode_list/gds_structures.py').read())
    GDS_structure_1 = name_change()
    GDS_structure_out = GDS_structure_1.visit(GDS_structure)
    f_name = hashing('gds_structures') + '.py'
    GDS_structure_w = open('./auto_encrypted_test/'+f_name,'w')
    GDS_structure_w.write(astunparse.unparse(GDS_structure_out))

    gds_tags = ast.parse(open('./Encode_list/gds_tags.py').read())
    gds_tags_1 = name_change()
    gds_tags_out = gds_tags_1.visit(gds_tags)
    f_name = hashing('gds_tags') + '.py'
    gds_tags_w = open('./auto_encrypted_test/'+f_name,'w')
    gds_tags_w.write(astunparse.unparse(gds_tags_out))

    user_d = ast.parse(open('./Encode_list/user_define_exceptions.py').read())
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

def method_list() : 
    dir_check=os.getcwd()
    if 'generator_model_path' in user_setup.__dict__ and user_setup.generator_model_path:
        generator_model_path = user_setup.generator_model_path
    else:
        generator_model_path = './generatorLib/generator_models'

    if 'generatorLib' in dir_check or 'PyQTInterface' in dir_check:
        os.chdir('..')
    # sys.path.append('./generatorLib/generator_models')
    sys.path.append(generator_model_path)
    generator_list = []
    class_dict = dict()
    class_name_dict = dict()
    class_function_dict = dict()
    libraries = dict()
    for generator in glob.iglob(f'{generator_model_path}/*.py'):
        if platform.system() in ['Linux', 'Darwin']:
            generator_class_name = generator.split('/')[-1][:-3]
        else:
            generator_class_name = generator.split('\\')[1][:-3]
        generator_list.append(generator_class_name)
        tmp = __import__(generator_class_name)
        for name,obj in inspect.getmembers(tmp):
            if inspect.isclass(obj):
                # class_dict[generator_class_name] = dict(name=name,object=obj)
                class_dict[generator_class_name] = obj
                class_name_dict[generator_class_name] = name
                libraries[generator_class_name] = tmp
                fcn_list = [[fcn_name, fcn_obj] for fcn_name, fcn_obj in inspect.getmembers(obj) if "Calculate" in fcn_name]
                class_function_dict[generator_class_name] = dict()
                for fcn_name, fcn_obj in fcn_list:
                    args = list(inspect.signature(fcn_obj).parameters.values())[1:]
                    # args = str(args).split('=')[0]
                    class_function_dict[generator_class_name][fcn_name] = args
    
    # print (class_function_dict)
    # print ('//')
    # print (class_dict)
    class_lst = dict()
    for i in class_dict.keys() :
        class_lst[i] = str(class_dict[i])[6:-2].split('.')[-1]
    # print (class_lst)
    # print ((class_lst['TristateInverter']))

    with gzip.open ("./Gen_list.pickle", "wb") as f :
        pickle.dump([class_function_dict, class_lst], f)


# method_list() ## for obtaining generator functions
main_1()
