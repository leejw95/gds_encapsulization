import os, sys
dir_check = os.getcwd()
if 'auto_encrypted_test' not in dir_check:
    os.chdir('./auto_encrypted_test')

import inspect
import warnings
import hashlib
import ast
import _9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4, b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81, ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092

class GDS_API:
    def __init__(self):
        pass

    def create_gds(self, name=None):
        if '_DesignParameter' in self.__dict__:
            self.feed_design(dp=self._DesignParameter, name=name)
        else:
            warnings.warn('There is no layout design.')

    def feed_design(self, dp, name=None):
        __MAX_STRUCTURE_LEN = 20
        dp['_7563a16a547855ae85f461c6ade6e8a9d7d7a2aca7f877614e0d0459fb25d1e6'] =  _9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4.c668a73a36c4334132f1a4bf1956febacd22ea8e8a1b4b25ccf19f6b1f522f52._4cc7762d387f12c54f12d265f78fdc495bdfb3e0909acdf27ea1234d755e7ba0(None,name)
        dp['_13864ddbaab63577bb07db6dcc11d8a2f724a0784933aedad515ce4a6fd2e256'] =  _9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4.c668a73a36c4334132f1a4bf1956febacd22ea8e8a1b4b25ccf19f6b1f522f52._680b2521950f6cd6aa109e161a71b2f62707b13172b69c9736ea85d4b5068631(None)
        self.transform_design_parm_name()
        __gds_structure =  _9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4.c668a73a36c4334132f1a4bf1956febacd22ea8e8a1b4b25ccf19f6b1f522f52()._4690f053371816ceb54e58b693a58de7ef1a84383309889b3d0cb7a5ebb2436a(dp)
        if len(__gds_structure) > 20:
            warnings.warn('Demo version supports maximum 20 elements per structure.')
        __gds_stream =  _9d836f0eb91c3bf41dab33e6971f76eae91446199aa6508651e6d8ab502df2c4.c668a73a36c4334132f1a4bf1956febacd22ea8e8a1b4b25ccf19f6b1f522f52.cf39d1afa2d28ca3922bf136b6bb0cb031c5bc297c4c5eaca5f4277e99813980(None,__gds_structure[:__MAX_STRUCTURE_LEN])
        output_file = open(f'{name}.gds','wb')
        __gds_stream._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(output_file)
        output_file.close()
        del __gds_structure, __gds_stream, output_file

    def get_drc(self, rule_name, rule_arg=dict()):
        rule_name = self.__var_name_tf(rule_name)
        for key in list(rule_arg.keys()):
            hash_key = self.__var_name_tf(key)
            rule_arg[hash_key] = rule_arg.pop(key)
        if rule_name in ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092.ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092().__dict__:
            return ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092.ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092().__dict__[rule_name]
        elif rule_name in [obj_info[0] for obj_info in inspect.getmembers(ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092.ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092, inspect.isfunction)]:
            method = getattr(ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092.ef9d0d0c16b2fcf734c4dbeba6625f1f343b6c49a102dd7d4c165a375226a092(), rule_name)
            return method(**rule_arg)
        else:
            raise Exception("Not valid design rule name.")

    def boundary_declaration(self, layer_name):
        layer_name = self.__var_name_tf(layer_name)

        return dict(d60147ba44dc08572d2187aedc77df7f7ea74256f1cfdd93a35b3185e766cabf=1,
                    efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd=b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._4608926bff46b2e77f7f302526d2da7d0089c506eac72659862872d39d2dd0f6[layer_name][0],
                    _170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4=b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._4608926bff46b2e77f7f302526d2da7d0089c506eac72659862872d39d2dd0f6[layer_name][1],
                    _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8=[],_63d072897e53c01dbc2afd4bb14e07585fcd2d7f3fd3589a4eeb97f7124cd647=None, b9bc3a98a024872315b2ee55bd0514e0e11cf35c1812171f26cef7200e8fdbbb=None,
                    _6a54638af456958e028f9ab99dfa3bb3d220b4930ee0c9bcab240939f7c85340=None, _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16=None)

    def path_declaration(self, layer_name):
        layer_name = self.__var_name_tf(layer_name)

        return dict(d60147ba44dc08572d2187aedc77df7f7ea74256f1cfdd93a35b3185e766cabf=2,
                    efbe9fd8a41381213cd7b8246d5cce6da16955369b27f32c81bfbedb8e0a27fd=b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._4608926bff46b2e77f7f302526d2da7d0089c506eac72659862872d39d2dd0f6[layer_name][0],
                    _170ab5383233af8774a135f7ebb81c414f6ba07b57399c768d7f05f54ce962b4=b4b34939031b9cf1201098d07c14d8203e733e1faaa6917451caf5e83b779a81._4608926bff46b2e77f7f302526d2da7d0089c506eac72659862872d39d2dd0f6[layer_name][1],
                    _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8=[],e8c887f783a924712bb26df18fc7d83c9797355259822634c84c3c9ace5a6d1f=None,  _6a54638af456958e028f9ab99dfa3bb3d220b4930ee0c9bcab240939f7c85340=None, _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16=None)

    def sref_declaration(self, designobj=None):

        return dict(d60147ba44dc08572d2187aedc77df7f7ea74256f1cfdd93a35b3185e766cabf=3, _0e50a8d405c4a9f0a50295b7dafbf67ca3b9c3edfe787d90dbe71dd37433df6e=designobj, _77e27fdc078c5b69aec8f4a15d1a68039f481fd1fa7466f19b5cc2324d794fb8=[],
                    _4a13cef9863384a78b3289eb281f164b99d8062fd4de18b2d95c095f3d43abf0=None,
                    _5f5278fd16a2bb911853ce64c7d0e5441ea1f5a067dc5c269310cc2e3a42607c=None, _6a54638af456958e028f9ab99dfa3bb3d220b4930ee0c9bcab240939f7c85340=None, _93e3e02b26da11e7f623d5c2fa8b976254b1dc1e336e9a23026386b4ecaa2d16=None)

    def transform_design_parm_name(self):
        for _, dp in self._DesignParameter.items():
            for key in list(dp.keys()):
                if key in ['_XWidth', '_YWidth', '_Width', '_XYCoordinates']:
                    hashed_name = self.__var_name_tf(key)
                    dp[hashed_name] = dp.pop(key)


    def __var_name_tf(self, name):
        sha = hashlib.new('sha256')
        sha.update(name.encode())
        hash_str = sha.hexdigest()
        if hash_str[0].isdigit():
            hash_str = '_' + hash_str
        return hash_str

if __name__ == '__main__':
    a = GDS_API()
