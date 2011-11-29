class Handlers(object):

    _phases = [
        'request_prepare',
        'request_send',
        'response_done',
        'response_redirect',
    ]

    def __init__(self):
        self._handlers = {}

    def handlers(self, phase):
        self._check_phase(phase)
        return self._handlers.get(phase, None)

    def add_handler(self, phase, cb):
        self._check_phase(phase)
        self._handlers[phase] = cb

    def remove_handler(self, phase):
        self._check_phase(phase)
        self._handlers[phase] = None

    def dispatch(self, phase, input_object):
        self._check_phase(phase)
        cb = self.handlers(phase)

        if cb is None:
            return input_object

        res = cb.__call__(input_object)
        if res is not None:
            return res
        return input_object

    def _check_phase(self, phase):
        if phase not in self._phases:
            raise Exception("phase %s does not exists" % phase)
