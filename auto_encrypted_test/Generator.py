# import Arg_name_to_object
import gzip, pickle
#from auto_encrypted_test import *
import _180cb85a13ff2d6630e43553dccac8fb8d45f89e4ab3f70c47c78a551b0120ff
from os.path import dirname, basename, isfile, join
import glob
import inspect


# modules = glob.glob(join('./auto_encrypted_test/', "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
# print (__all__)

# from . import *
sw = _180cb85a13ff2d6630e43553dccac8fb8d45f89e4ab3f70c47c78a551b0120ff.dde8bef78cbb720683fa1fe76bfb900592099ed4346ed995bcbc514e9aa67256()

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
            args[i] = sw._12ea12eace7d655f471ce55e34f89b1b77a3d9d05a445ca82877dd2235beaa51(val)

# print (args)

transfer = [sel1, Func_list[sel2], args]

# print (transfer)

# print([swap.change(transfer[0])])

# add1 = dict()
new_args = dict()
for i in args.keys() :
    new_args[sw._12ea12eace7d655f471ce55e34f89b1b77a3d9d05a445ca82877dd2235beaa51(i)] = args[i]
imp = sw._12ea12eace7d655f471ce55e34f89b1b77a3d9d05a445ca82877dd2235beaa51(transfer[0])
# cla = swap.change(picked[1][transfer[0]])
func = sw._12ea12eace7d655f471ce55e34f89b1b77a3d9d05a445ca82877dd2235beaa51(Func_list[sel2])
# print (picked[1][transfer[0]])
# print (imp + '.' + cla)
lib = __import__(imp)
for name, cla in inspect.getmembers(lib) :
    if inspect.isclass(cla) :
        # print (cla)
        obj = cla(_9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435 = None, _7563a16a547855ae85f461c6ade6e8a9d7d7a2aca7f877614e0d0459fb25d1e6 = sel1)
        abc = getattr(obj, func)
        # print (i for i in list(args.values()))
        abc(**new_args)
        obj._4690f053371816ceb54e58b693a58de7ef1a84383309889b3d0cb7a5ebb2436a(_98a63f876c8ce2884780fb17a1a6ae56c346beac00402ec8bdf6b914c1fd4920 = obj._9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435)
        gds = open('./'+sel1+'.gds', 'wb')
        tmp = obj.cf39d1afa2d28ca3922bf136b6bb0cb031c5bc297c4c5eaca5f4277e99813980(obj._9ef134b74cc6307bd3aef4c632f1a51085c4c203bd66c7b6b3403aa7d9261435['_13864ddbaab63577bb07db6dcc11d8a2f724a0784933aedad515ce4a6fd2e256']['_13864ddbaab63577bb07db6dcc11d8a2f724a0784933aedad515ce4a6fd2e256'])
        tmp._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(gds)
        gds.close()
