from tsuruclient import apps, nodes


class Client(object):
    def __init__(self, target):
        self.apps = apps.AppManager(target)
        self.nodes = nodes.NodeManager(target)
