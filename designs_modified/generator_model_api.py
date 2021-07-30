import glob, os, sys
import sys, inspect
import urllib
import urllib.request
import urllib.error
import sys

sys.tracebacklimit = 0

try :
    urllib.request.urlopen('http://www.kriss.re.kr').headers['Date']
except Exception:
    raise Exception("Connect to Internet")

date = urllib.request.urlopen('http://www.kriss.re.kr').headers['Date']


if date[8:16] not in ['Jul 2021','Aug 2021', 'Sep 2021', 'Oct 2021']:
    raise Exception("License Expired")

sys.path.append('./generatorLib/generator_models')
print("*********************Generator Library Loading Start")

generator_list = []
class_dict = dict()
for generator in glob.iglob('./generatorLib/generator_models/*.py'):
    generator_class_name = generator.split('\\')[1][:-3]
    generator_list.append(generator_class_name)
    tmp = __import__(generator_class_name)
    for name,obj in inspect.getmembers(tmp):
        if inspect.isclass(obj):
            # class_dict[generator_class_name] = dict(name=name,object=obj)
            class_dict[generator_class_name] = obj

print("************************Generator Library Loading Complete")
