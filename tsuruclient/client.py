from tsuruclient  import apps


class Client(object):
    def __init__(self, target):
        self.apps = apps.AppManager(target)
