class Headers(dict):

    @property
    def _normalize_keys(self):
        if not hasattr(self, '_normalized_keys') or not self._normalized_keys:
            self._normalized_keys = dict(
                    (k.lower(), k) for k in self.iterkeys())
        return self._normalized_keys

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        if hasattr(self, '_normalized_keys'):
            self._normalized_keys.clear()

    def __delitem__(self, key):
        dict.__delitem__(self, key)
        self._normalized_keys.clear()

    def __contains__(self, key):
        return key.lower() in self._normalize_keys

    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, self._normalize_keys[key.lower()])

    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default
