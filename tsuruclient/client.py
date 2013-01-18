from tsuruclient  import apps


class Client(object):
    def __init__(self):
        self.apps = apps.AppManager()
