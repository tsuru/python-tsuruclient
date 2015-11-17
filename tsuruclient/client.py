from tsuruclient import apps, nodes, templates


class Client(object):
    def __init__(self, target):
        self.apps = apps.AppManager(target)
        self.nodes = nodes.NodeManager(target)
        self.templates = templates.TemplateManager(target)
