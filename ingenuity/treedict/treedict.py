class TreeDict(object):

    def __init__(self, dict: dict):

        self.dict = dict

    def __getitem__(self, keys):

        return self._getdefault(keys)

    def _setDictValue(self, d, key, value):
        if type(d[key]) is dict:
            raise Exception('is dict')
        d[key] = value

    def __setitem__(self, keys, value):

        d = self.dict

        if len(keys) == 1:

            a = keys[0]
            self._setDictValue(d, a, value)

        elif len(keys) == 2:
            
            a = keys[0]
            d = d[a]

            b = keys[1]
            self._setDictValue(d, b, value)

    def getdefault(self, *keys, default=None):

        return self._getdefault(keys, default)

    def _getdefault(self, keys, default=None):

        d = self.dict

        for key in list(keys):

            if type(d) is not dict:
                break

            d = d.setdefault(key, default)

        return d




