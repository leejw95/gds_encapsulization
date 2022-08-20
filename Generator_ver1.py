import gzip
import pickle
import inspect
import os


class Generator:
    def __init__(self, client_name, lib_name, method_idx, args_dict):
        with gzip.open('./Gen_list.pickle', 'rb') as f:
            self.picked = pickle.load(f)
        
        self.libraries = self.picked[0]

        self.client_name = client_name
        self.lib_name = lib_name
        self.method_idx = method_idx
        self.arg_dict = args_dict
        self.methods_name_list = list(self.libraries[lib_name].keys())
        print("Generator Initialized!")

    def __create_dir_if_not_exists(self):
        if not os.path.exists('/home/Clients/' + self.client_name):
            os.makedirs('/home/Clients/' + self.client_name)


    def __encrypt_arg_dict(self, args):
        new_args = dict()
        for i in args.keys():
            if type(args[i]) != dict:
                new_args[i] = args[i]

            else:
                new_args[i] = dict()
                self.__encrypt_arg_dict(new_args[i])

        return (new_args)

    def run(self):
        print(self.arg_dict)
        self.arg_dict = self.__encrypt_arg_dict(self.arg_dict)
        imp = self.lib_name
        lib = __import__(imp)
        func = self.methods_name_list[self.method_idx]
        for name, cla in inspect.getmembers(lib):
            if inspect.isclass(cla):
                obj = cla(_DesignParameter=None, _Name=self.lib_name)
                abc = getattr(obj, func)
                abc(**self.arg_dict) 
                obj._UpdateDesignParameter2GDSStructure(_DesignParameterInDictionary=obj._DesignParameter)
                self.__create_dir_if_not_exists()
                gds = open('/home/Clients/' + self.client_name + '/' + self.lib_name + '.gds', 'wb')
                tmp = obj._CreateGDSStream(obj._DesignParameter['_GDSFile']['_GDSFile'])
                tmp.write_binary_gds_stream(gds)
                gds.close()
