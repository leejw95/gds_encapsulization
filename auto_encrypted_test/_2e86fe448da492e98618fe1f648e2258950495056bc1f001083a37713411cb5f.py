
__all__ = ('FormatError', 'EndofFileError', 'IncorrectRecordSize', 'IncorrectDataSize')

class FormatError(Exception):
    'base class for all gds exceptions'

class EndofFileError(FormatError):
    'raised on unexpected end of file'

class IncorrectRecordSize(FormatError):
    'raised if record size is not correct'

class IncorrectDataSize(FormatError):
    'raised if data size is not correct'

class _9cc51fa952354132fe746824e92f14b9b9a0a2c55b8b77d865bde01762769514(FormatError):
    'data has incorrect value'

class c21d162cbb2ea03e45dd8e84fa7146b473afc3906fe0ba78c5369a967875ff38(FormatError):
    'element name is incorrect'
