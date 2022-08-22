
import _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f
import struct
import _43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f
import ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8
import _6d423e1f15dd9480c4c0e66185d073ba511a802de60979d6a6d9c66f079ee2a7
'_HEADER=None\n_BGNLIB=None\n_LIBDIRSIZE=None\n_SRFNAME=None\n_LIBSECUR=None\n_LIBNAME=None\n_REFLIBS=None\n_FONTS=None\n_ATTRTABLE=None\n_GENERATIONS=None\n_FORMATTYPE=None\n_UNITS=None\n_STRUCTURES=None\n_ENDLIB=None'

class _6260d5abcc1879784e8235784c1c9196cda4b96c91f0fed1b40fbee5cf9486f7():

    def __init__(self):
        self._169c9c7ef42055b9a7f7822ebb3706c395a2919d3dcae3e1800f2bfa0022bc02 = None
        self._938a02ecd63e1f99df26ef88d274cd2cbcba13c1ec8d7f8e61b1d3a0de09b6d1 = None
        self.f15a7644ea20c55b10bb3d5ccd14ac90ad687f85d0f7782b90339d43f59a763a = None
        self._64517aee96c72df8db8bb77f12fd3021cdd944cf889c423b3b95ae836c75d4df = None
        self._56ee007d805e0fe03d3ef875723c5bdac46c726a1570cd1325e13049ff3e7e48 = None
        self.f92927f8e33f3f57fad46d9ebfc8c443483f4070e5e9c6f064ea03a369c712ea = None
        self._455b204635aba4ce85e0b95ef8d401c6a3ea744f8059703ef668e058e45217e3 = None
        self._6ed2a9e302afe040ec5838531bb7e3c9e377c91612e65c6e784d1e63d9c26c4c = None
        self._97109b901764a84a61596012754805c8948aa66cc25187b22688baef9f8c612d = None
        self._45857d0ee1011b95fe96e75903963533255cbc580cad64bcb8b40aa048006f69 = None
        self._994e43f15738075b473e1353859f7bc74e9473ddf03674bf5e56d6ffcb23e82d = None
        self._40828697495067ca827dd12b97b7c06e058ae456e03c7c490a7c30a594bf6cfd = None
        self.b140b79dccf6fb516fbc3d1e407a50a607c87c1e661ca1631035a073dc1cc928 = []
        self._50f1b5d8cf890dc787a6cf930158c0bcc23d1256e00c2559e625362bde9c95ce = None
    '\n    \n    read binary record data --> classify the binary data  \n    \n    record\n    [record header:[record length, record type,data type], data]\n    \n    '

    def aa97351453393a73fc23886a504055503bce46018c698fab356007d91a7d88f4(self, _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3):
        _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3._3316348dbadfb7b11c7c2ea235949419e23f9fa898ad2c198f999617912a9925(4)
        if ((not _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a) or (len(_7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a) < 4)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.EndofFileError
        (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82) = struct.unpack('>HH', _7a1e1c43019770eb93d326b841ce9ae93c2aed14491a2604e7d09fdf411c654a)
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb < 4):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectRecordSize('record size is too small')
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb % 2):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.IncorrectRecordSize('incorrect record size')
        ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb -= 4
        _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596 = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3._3316348dbadfb7b11c7c2ea235949419e23f9fa898ad2c198f999617912a9925(ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb)
        if (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb != len(_96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)):
            raise _2e86fe448da492e98618fe1f648e2258950495056bc1f001083a37713411cb5f.EndofFileError
        _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51 = (c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82 & 255)
        _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a = ((c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82 >> 8) & 255)
        _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.seek((- (ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4)), 1)
        _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c = _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3._3316348dbadfb7b11c7c2ea235949419e23f9fa898ad2c198f999617912a9925((ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4))
        ' return record size, record tag, record type, record data type, record data, record binary stream'
        return [(ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb + 4), c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c]

    def _4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(self, _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3):
        self._169c9c7ef42055b9a7f7822ebb3706c395a2919d3dcae3e1800f2bfa0022bc02._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        self._938a02ecd63e1f99df26ef88d274cd2cbcba13c1ec8d7f8e61b1d3a0de09b6d1._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self.f15a7644ea20c55b10bb3d5ccd14ac90ad687f85d0f7782b90339d43f59a763a != None):
            self.f15a7644ea20c55b10bb3d5ccd14ac90ad687f85d0f7782b90339d43f59a763a._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._64517aee96c72df8db8bb77f12fd3021cdd944cf889c423b3b95ae836c75d4df != None):
            self._64517aee96c72df8db8bb77f12fd3021cdd944cf889c423b3b95ae836c75d4df._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._56ee007d805e0fe03d3ef875723c5bdac46c726a1570cd1325e13049ff3e7e48 != None):
            self._56ee007d805e0fe03d3ef875723c5bdac46c726a1570cd1325e13049ff3e7e48._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        self.f92927f8e33f3f57fad46d9ebfc8c443483f4070e5e9c6f064ea03a369c712ea._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._455b204635aba4ce85e0b95ef8d401c6a3ea744f8059703ef668e058e45217e3 != None):
            self._455b204635aba4ce85e0b95ef8d401c6a3ea744f8059703ef668e058e45217e3._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._6ed2a9e302afe040ec5838531bb7e3c9e377c91612e65c6e784d1e63d9c26c4c != None):
            self._6ed2a9e302afe040ec5838531bb7e3c9e377c91612e65c6e784d1e63d9c26c4c._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._97109b901764a84a61596012754805c8948aa66cc25187b22688baef9f8c612d != None):
            self._97109b901764a84a61596012754805c8948aa66cc25187b22688baef9f8c612d._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._45857d0ee1011b95fe96e75903963533255cbc580cad64bcb8b40aa048006f69 != None):
            self._45857d0ee1011b95fe96e75903963533255cbc580cad64bcb8b40aa048006f69._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self._994e43f15738075b473e1353859f7bc74e9473ddf03674bf5e56d6ffcb23e82d != None):
            self._994e43f15738075b473e1353859f7bc74e9473ddf03674bf5e56d6ffcb23e82d._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        self._40828697495067ca827dd12b97b7c06e058ae456e03c7c490a7c30a594bf6cfd._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        if (self.b140b79dccf6fb516fbc3d1e407a50a607c87c1e661ca1631035a073dc1cc928 != []):
            _917990d25f10533d7cf33f0c4491ea3b0aad2f9a2724c5be3d479b956b81506e = len(self.b140b79dccf6fb516fbc3d1e407a50a607c87c1e661ca1631035a073dc1cc928)
            for de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7 in range(0, _917990d25f10533d7cf33f0c4491ea3b0aad2f9a2724c5be3d479b956b81506e):
                self.b140b79dccf6fb516fbc3d1e407a50a607c87c1e661ca1631035a073dc1cc928[de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7]._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
        self._50f1b5d8cf890dc787a6cf930158c0bcc23d1256e00c2559e625362bde9c95ce._4b846fdde38fad3afc3a740a590ff2a6e775507515836c10129e02f95e93e578(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)

    def _4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(self, _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3):
        '\n        read record binary stream separately\n        '
        while True:
            'extract binary gds data until units'
            [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = self.aa97351453393a73fc23886a504055503bce46018c698fab356007d91a7d88f4(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
            if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['HEADER'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._169c9c7ef42055b9a7f7822ebb3706c395a2919d3dcae3e1800f2bfa0022bc02 = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._7e2c688c964598c5c6da61d18a7bb617665e2b4f26261d93f900ae6ad63128bf()
                self._169c9c7ef42055b9a7f7822ebb3706c395a2919d3dcae3e1800f2bfa0022bc02._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['BGNLIB'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._938a02ecd63e1f99df26ef88d274cd2cbcba13c1ec8d7f8e61b1d3a0de09b6d1 = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.dcca0dc143b28ef4bdc0b6a645d8c37eda5eaf9ee1132233ec62ba531f98bf5c()
                self._938a02ecd63e1f99df26ef88d274cd2cbcba13c1ec8d7f8e61b1d3a0de09b6d1._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['LIBDIRSIZE'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self.f15a7644ea20c55b10bb3d5ccd14ac90ad687f85d0f7782b90339d43f59a763a = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._4c8e68ed0295a3431d7493cf02fa3123b5719a28de593caeb9b8f47572051977()
                self.f15a7644ea20c55b10bb3d5ccd14ac90ad687f85d0f7782b90339d43f59a763a._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['SRFNAME'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._64517aee96c72df8db8bb77f12fd3021cdd944cf889c423b3b95ae836c75d4df = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.cc6c5311c170836b26b8fdd7f861122bbdc771c29b7999a2933c923dd41ea207()
                self._64517aee96c72df8db8bb77f12fd3021cdd944cf889c423b3b95ae836c75d4df._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['LIBSECUR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._56ee007d805e0fe03d3ef875723c5bdac46c726a1570cd1325e13049ff3e7e48 = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.d989964d6995eceb7cd3c35e2bfd216b0f37d1c72fc66f919ecc348c4b8d7944()
                self._56ee007d805e0fe03d3ef875723c5bdac46c726a1570cd1325e13049ff3e7e48._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['LIBNAME'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self.f92927f8e33f3f57fad46d9ebfc8c443483f4070e5e9c6f064ea03a369c712ea = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._82d7f265d5c531bacba4c3ebb674e3e30a65400dda2de51157d36446e27b629f()
                self.f92927f8e33f3f57fad46d9ebfc8c443483f4070e5e9c6f064ea03a369c712ea._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['REFLIBS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._455b204635aba4ce85e0b95ef8d401c6a3ea744f8059703ef668e058e45217e3 = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._52a694127d3171a903362aad2891b42aeb20a8a0373a607078ae7f5a7435114b()
                self._455b204635aba4ce85e0b95ef8d401c6a3ea744f8059703ef668e058e45217e3._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['FONTS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._6ed2a9e302afe040ec5838531bb7e3c9e377c91612e65c6e784d1e63d9c26c4c = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._0034cfca3071c7fb04d015b459e0416a80e0af05726b0d0c840098fffbf8c737()
                self._6ed2a9e302afe040ec5838531bb7e3c9e377c91612e65c6e784d1e63d9c26c4c._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['ATTRTABLE'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._97109b901764a84a61596012754805c8948aa66cc25187b22688baef9f8c612d = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._06729e9adb96a235071d9e18c251976017fcfd11932da30b87ede1575ad637dc()
                self._97109b901764a84a61596012754805c8948aa66cc25187b22688baef9f8c612d._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['GENERATIONS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._45857d0ee1011b95fe96e75903963533255cbc580cad64bcb8b40aa048006f69 = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._8cc9798ba42a71c5d05fe90b443e4a1e760fa1e0259b309707cf8ec3881c11dc()
                self._45857d0ee1011b95fe96e75903963533255cbc580cad64bcb8b40aa048006f69._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['FORMAT'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                'extract FORMATTYPE binary data'
                while True:
                    [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = self.aa97351453393a73fc23886a504055503bce46018c698fab356007d91a7d88f4(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
                    if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['UNITS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                        self._994e43f15738075b473e1353859f7bc74e9473ddf03674bf5e56d6ffcb23e82d = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.c8c97e0332a9bbcbd4d00d84abffbc253421029402ae401eff00fad20c3c935c()
                        self._994e43f15738075b473e1353859f7bc74e9473ddf03674bf5e56d6ffcb23e82d._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
                        del a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5
                        _8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3.seek((- ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb), 1)
                        break
                    else:
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['UNITS'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._40828697495067ca827dd12b97b7c06e058ae456e03c7c490a7c30a594bf6cfd = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8._16c3a6a8023a94fd720e8d55c3f61483c16210c557fc871efdae80eddccf9782()
                self._40828697495067ca827dd12b97b7c06e058ae456e03c7c490a7c30a594bf6cfd._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596)
                break
            "    \n            elif gds_tags.DICT['FORMAT']==record_tag:\n                self._FORMATTYPE.append(record_binary_stream)\n            "
            "\n                while True: \n                    [record_size, record_tag, record_type, record_datatype, record_data, record_binary_stream] = self.read_record(gds_file=gds_file)\n                    if gds_tags.DICT['MASK']==record_tag:\n                        self._FORMATTYPE.append(record_binary_stream)\n                    elif gds_tags.DICT['ENDMASKS']:\n                        self._FORMATTYPE.append(record_binary_stream)\n                        break\n                    elif gds_tags.DICT['UNITS']==record_tag:\n            "
            '\n                        gds_file.seek(-record_size,1)\n                        break\n            '
        'extract structures & endlib'
        while True:
            a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5 = []
            a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = None
            [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = self.aa97351453393a73fc23886a504055503bce46018c698fab356007d91a7d88f4(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
            if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['BGNSTR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                'extract each binary structure data'
                a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                while True:
                    [ea4107daa323d2623187ec02cfa51a2dfa3f2842fc34daf69619b93a2ced92cb, c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _5569902e06c7813199cc22b0a6bf803bfd5b5425d3fb48ac355838b7c15a138a, _654db26802d6bd2247d005995c51922421c97e52bc63e319957994d5a0bf1f51, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596, _9cd99d5810fa1e6e9467f167eb4a3bbf06151fcdb73eb484d3e6b4e9d4a4943c] = self.aa97351453393a73fc23886a504055503bce46018c698fab356007d91a7d88f4(_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3=_8ba8e7ffca657c2f8ca7b7adbabcf539bc196634176c32e608f8dc1ce8ad45e3)
                    if (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['ENDSTR'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = _6d423e1f15dd9480c4c0e66185d073ba511a802de60979d6a6d9c66f079ee2a7._4ae93eb6332f0e1295bc8dc12eef5ad7be1a99a47430446a84dce7ccb3a2f5ee()
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5._4afdb9d0303b7f5509262bbf35b94e5f2b18911a890ceac879b35f028b276487(a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5)
                        self.b140b79dccf6fb516fbc3d1e407a50a607c87c1e661ca1631035a073dc1cc928.append(a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5)
                        a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5 = None
                        del a73669ac4c247ae26d08a82bd71f629e74ea852b0b0aa36f907812f10608c5b5
                        break
                    else:
                        a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5.append([c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82, _96ce26fc2d37fda2fea23ac6fb64d0782f63d5719237553992a0ccdc91a3e596])
            elif (_43a2bcb21cf6aacdcc29ba7a4bc1ccc5ecac7875ee77dd67879c52c9d6148f4f._8a2e3259a824bf554a53deba37b276b7aaac1f3a6c7ae85b791a80b0f57b182a['ENDLIB'] == c198793c3f1056fd913d0775029254f02ca91560e3e5ed9ea3d7d3cbc1f9dc82):
                self._50f1b5d8cf890dc787a6cf930158c0bcc23d1256e00c2559e625362bde9c95ce = ad2f856b5678f98d4316b4f3428fc9e0b32bf1917c40b8202e28e1aadee285d8.c3eb2aae8da55cc3f1ac6783ef2b5139b446b462fcca57d7eb83a4e1f6f954a4()
                del a6864eb339b0e1f6e00d75293a8840abf069a2c0fe82e6e53af6ac099793c1d5
                'delete temp=[] in the while loop'
                break
    '\n    _HEADER=None\n    _BGNLIB=None\n    _LIBDIRSIZE=None\n    _SRFNAME=None\n    _LIBSECUR=None\n    _LIBNAME=None\n    _REFLIBS=None\n    _FONTS=None\n    _ATTRTABLE=None\n    _GENERATIONS=None\n    _FORMATTYPE=None\n    _UNITS=None\n    _STRUCTURES=None\n    _ENDLIB=None\n    '
    '\n    _gds_stream=(_HEADER, _BGNLIB, _LIBDIRSIZE,_SRFNAME,_LIBSECUR, _LIBNAME,                 _REFLIBS, _FONTS, _ATTRTABLE,_GENERATIONS,_FORMATTYPE,_UNITS,                _STRUCTURES,_ENDLIB)\n                '
    '\n    GDS stream format:\n        .. productionlist::\n            library: HEADER\n                   : BGNLIB\n                   : [LIBDIRSIZE]\n                   : [SRFNAME]\n                   : [LIBSECUR]\n                   : LIBNAME\n                   : [REFLIBS]\n                   : [FONTS]\n                   : [ATTRTABLE]\n                   : [GENERATIONS]\n                   : [`format`]\n                   : UNITS\n                   : {`structure`}*\n                   : ENDLIB\n            format: FORMAT\n                  : [MASK+ ENDMASKS]\n    '
