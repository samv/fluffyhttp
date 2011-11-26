class Handlers(object):

    _phases = ['request_prepare', 'request_send' ]
    _handlers = {
        'request_send': []
    }

    def __init__(self):
        pass

    def handlers(self, phase):
        if phase in self._phases:
            return self._handlers.get(phase, list())
        else:
            print "no phase %s" % phase
            raise

    def append(self, phase, cb):
        if phase in self._phases:
            self._handlers[phase].append(cb)
        else:
            print "no phase %s" % phase
            raise

    def dispatch(self, phase, request):
        for handler in self.handlers(phase):
            if phase == 'request_send':
                res = self._dispatch_request_send(handler, request)
                if res is not None:
                    return res

    def _dispatch_request_send(self, cb, request):
        return cb.__call__(request)
