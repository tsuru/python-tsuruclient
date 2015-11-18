from tsuruclient import apps, nodes, templates


class Client(object):
    def __init__(self, target, token):
        self.apps = apps.Manager(target, token)
        self.nodes = nodes.Manager(target, token)
        self.templates = templates.Manager(target, token)
