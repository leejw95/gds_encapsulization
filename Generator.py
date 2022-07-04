import Arg_name_to_object

libname = ['Tie_Cell (1)', 'NMOSWithDummy (2)', 'PMOSWithDummy (3)', 'SupplyRails (4)']

print ("Select Generator list {}: ".format(libname))

arg = Arg_name_to_object

exec(open('Tie_Cell' + '.py').read())