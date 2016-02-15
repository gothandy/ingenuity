class TreeDict(object):

    def __init__(self, dict: dict):

        self.dict = dict

    def __getitem__(self, keys):

        return self._getdefault(keys)

    def _getParentDictAndKey(self, keys):

        d = self.dict

        if len(keys) > 1:
            
            parentKeys = keys[0:len(keys) - 1]

            for key in parentKeys:
                d = d[key]

        return d, keys[len(keys) - 1]

    def __setitem__(self, keys, value):

        d, key = self._getParentDictAndKey(keys)

        if key in d and type(d[key]) is dict:
            raise Exception('is dict')

        d[key] = value

    def getdefault(self, *keys, default=None):

        return self._getdefault(keys, default)

    def _getdefault(self, keys, default=None):

        d, key = self._getParentDictAndKey(keys)

        return d.setdefault(key, default)




