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
        ct = self.content_type
        if ct is None:
            return False
        if re.search(r'^text/', ct):
            return True
        return False

    @property
    def content_is_xhtml(self):
        ct = self.content_type
        if ct is None:
            return False
        if ct == 'application/xhtml+xml':
            return True
        if ct == 'application/vnd.wap.xhtml+xml':
            return True
        return False

    @property
    def content_is_xml(self):
        ct = self.content_type
        if ct is None:
            return False
        if ct == 'text/xml':
            return True
        if ct == 'application/xml':
            return True
        if re.search(r'\+xml$', ct):
            return True
        return False

    def last_modified(self, date=None):
        return self.date_header('Last-Modified', date)

    def date(self, date=None):
        return self.date_header('Date', date)

    def expires(self, date=None):
        return self.date_header('Expires', date)

    def if_modified_since(self, date=None):
        return self.date_header('If-Modified-Since', date)

    def if_unmodified_since(self, date):
        return self.date_header('If-Unmodified-Since')

    def date_header(self, key, date=None):
        if date:
            date = Date.time2str(date)
            self[key] = date
        else:
            value = self.get(key)
            if value is None:
                raise Exception(value)
                return None
            return Date.str2time(value)
