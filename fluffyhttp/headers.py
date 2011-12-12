from date import Date
import re


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

    @property
    def content_type(self):
        return self.get('Content-Type')

    @property
    def content_is_text(self):
        if self.content_type is None:
            return False
        if re.search(r'^text/', self.content_type):
            return True
        return False

    @property
    def last_modified(self):
        return self.date_header('Last-Modified')

    @property
    def date(self):
        return self.date_header('Date')

    @property
    def expires(self):
        return self.date_header('Expires')

    @property
    def if_modified_since(self):
        return self.date_header('If-Modified-Since')

    @property
    def if_unmodified_since(self):
        return self.date_header('If-Unmodified-Since')

    def date_header(self, key):
        value = self.get(key)
        if value is None:
            return None
        return Date.str2time(value)
