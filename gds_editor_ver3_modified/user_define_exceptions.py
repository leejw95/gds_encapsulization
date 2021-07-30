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
# import exceptions
#####exceptions are defined

__all__=('FormatError','EndofFileError','IncorrectRecordSize','IncorrectDataSize')

class FormatError(Exception):
    """base class for all gds exceptions""" 
class EndofFileError(FormatError):
    """raised on unexpected end of file"""
    
class IncorrectRecordSize(FormatError):
    """raised if record size is not correct"""
    

class IncorrectDataSize(FormatError):
    """raised if data size is not correct"""
class IncorrectDataValue(FormatError):
    """data has incorrect value"""
class IncorrecElementName(FormatError):
    """element name is incorrect"""

class IncorrectInputError(FormatError):
    """Input is incorrect""" 