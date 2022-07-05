# import Arg_name_to_object
import gzip, pickle
from auto_encrypted_test import *
import Trans
from os.path import dirname, basename, isfile, join
import glob


# modules = glob.glob(join('./auto_encrypted_test/', "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
# print (__all__)

# from . import *

with gzip.open('./Gen_list.pickle', 'rb') as f :
    picked = pickle.load(f)

gen = picked[0]
# print (picked[0])
# print ('//')
# print (picked[1])

Gen_list = list(gen.keys())
print (Gen_list)

sel1 = input()

Func_list = list(gen[sel1].keys())
print (Func_list)

sel2 = int(input())

a = gen[sel1][Func_list[sel2]]
args_wt_value = list()
for i in a :
    args_wt_value.append(str(i))
print (args_wt_value)

args = {}
for i in args_wt_value :
    tmp = i.split('=')
    args[tmp[0]] = tmp[1]
print (args)

for i in args.keys() :
    print (i)
    val = input()
    try :
        int(val)
        args[i] = int(val)
    except :
        if val == 'None' or val == 'none' :
            args[i] = None
        else :
            args[i] = val

print (args)

transfer = [sel1, Func_list[sel2], args]
print (transfer)

swap = Trans.Transfer()
print([swap.change(transfer[0])])

imp = swap.change(transfer[0])
cla = swap.change(picked[1][transfer[0]])
# print (picked[1][transfer[0]])
print (imp + '.' + cla)
tmp = __import__(imp)
