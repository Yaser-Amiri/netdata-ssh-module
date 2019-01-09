from re import search
import platform
from bases.FrameworkServices.LogService import LogService

UPDATE_EVERY = 5
RETRIES = 3


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
        if 'Red Hat' in platform.linux_distribution()[0]:
            log_path = '/var/log/secure'
        else:
            log_path = '/var/log/auth.log'
        self.log_path = self.configuration.get('path', log_path)
        self.order = ORDER
        self.definitions = CHARTS

    def _get_data(self):
        try:
            count = 0
            if 'Red Hat' in platform.linux_distribution()[0]:
                search_string = 'Failed password for.+ssh'
            else:
                search_string = 'Failed password for invalid.+ssh'
            for line in self._get_raw_data():
                if search(search_string, line):
                    count += 1
            return {"count": count}
        except (ValueError, AttributeError):
            return None
