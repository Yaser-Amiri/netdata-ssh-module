from re import search
from bases.FrameworkServices.LogService import LogService

update_every = 5
retries = 3


ORDER = ['failed_authentications']

CHARTS = {
    'failed_authentications': {
        'options': [None, 'Failed Authentications', 'count', 'Authentication',
                    'ssh.failed_auth', 'line'],
        'lines': [
            ["count", "failed-count", 'absolute', 1, 1]
        ]},
}


class Service(LogService):
    def __init__(self, configuration=None, name=None):
        LogService.__init__(self, configuration=configuration, name=name)
        self.log_path = self.configuration.get('path', '/var/log/auth.log')
        self.order = ORDER
        self.definitions = CHARTS

    def _get_data(self):
        try:
            count = 0
            for line in self._get_raw_data():
                if search(r'Failed password for invalid.+ssh', line):
                    count += 1
            return {"count": count}
        except (ValueError, AttributeError):
            return None
