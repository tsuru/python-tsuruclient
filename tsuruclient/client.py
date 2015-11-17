from tsuruclient import apps, nodes, templates


class Client(object):
    def __init__(self, target):
        self.apps = apps.Manager(target)
        self.nodes = nodes.Manager(target)
        self.templates = templates.Manager(target)
