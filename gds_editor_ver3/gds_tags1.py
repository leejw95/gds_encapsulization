
_8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a = {'HEADER': 2, 'BGNLIB': 258, 'LIBNAME': 518, 'UNITS': 773, 'ENDLIB': 1024, 'BGNSTR': 1282, 'STRNAME': 1542, 'ENDSTR': 1792, 'BOUNDARY': 2048, 'PATH': 2304, 'SREF': 2560, 'AREF': 2816, 'TEXT': 3072, 'LAYER': 3330, 'DATATYPE': 3586, 'WIDTH': 3843, 'XY': 4099, 'ENDEL': 4352, 'SNAME': 4614, 'COLROW': 4866, 'TEXTNODE': 5120, 'NODE': 5376, 'TEXTTYPE': 5634, 'PRESENTATION': 5889, 'STRING': 6406, 'STRANS': 6657, 'MAG': 6917, 'ANGLE': 7173, 'REFLIBS': 7942, 'FONTS': 8198, 'PATHTYPE': 8450, 'GENERATIONS': 8706, 'ATTRTABLE': 8966, 'STYPTABLE': 9222, 'STRTYPE': 9474, 'ELFLAGS': 9729, 'ELKEY': 9987, 'NODETYPE': 10754, 'PROPATTR': 11010, 'PROPVALUE': 11270, 'BOX': 11520, 'BOXTYPE': 11778, 'PLEX': 12035, 'BGNEXTN': 12291, 'ENDEXTN': 12547, 'TAPENUM': 12802, 'TAPECODE': 13058, 'STRCLASS': 13313, 'FORMAT': 13826, 'MASK': 14086, 'ENDMASKS': 14336, 'LIBDIRSIZE': 14594, 'SRFNAME': 14854, 'LIBSECUR': 15106, 'BORDER': 15360, 'SOFTFENCE': 15616, 'HARDFENCE': 15872, 'SOFTWIRE': 16128, 'HARDWIRE': 16384, 'PATHPORT': 16640, 'NODEPORT': 16896, 'USERCONSTRAINT': 17152, 'SPACERERROR': 17408, 'CONTACT': 17664}
_8dad69d6d41a7203e06c7feb1bc0a5413b7271ef270b08cdc827dde339ab0449 = {}
for (_2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683, cd42404d52ad55ccfa9aca4adc828aa5800ad9d385a0671fbcbf724118320619) in _8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a.items():
    _274f2e9a4b40fb846cba14b3ed16cf9eed4822b124add2c907c05769848b26ba()[_2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683] = cd42404d52ad55ccfa9aca4adc828aa5800ad9d385a0671fbcbf724118320619
    _8dad69d6d41a7203e06c7feb1bc0a5413b7271ef270b08cdc827dde339ab0449[cd42404d52ad55ccfa9aca4adc828aa5800ad9d385a0671fbcbf724118320619] = _2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683
del _2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683, cd42404d52ad55ccfa9aca4adc828aa5800ad9d385a0671fbcbf724118320619

def type_of_tag(tag):
    '\n    Returns type of a tag.\n\n    :param tag: tag ID\n    :type tag: int\n    :rtype: int\n\n    Examples:\n\n        >>> type_of_tag(HEADER)\n        2\n        >>> type_of_tag(MASK)\n        6\n\n    '
    return (_2a1073a6e67f0e5f09a5957c659503c690efe7272be8313df872556a9a684d8c & 255)
if (_222cd5ba71945d24cf1a45f333298bd376b1ea4dff1128d09ec095be6d2b3076 == '__main__'):
    import doctest
    ec4cce69ecd087eb67e0debbf03215b83fb42a496026851bead2c63cd18ec858.testmod()
