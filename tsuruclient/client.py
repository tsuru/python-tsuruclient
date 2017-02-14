from tsuruclient import apps, nodes, templates, pools
from tsuruclient import machines, containers, events


class Client(object):
    def __init__(self, target, token):
        self.apps = apps.Manager(target, token)
        self.nodes = nodes.Manager(target, token)
        self.templates = templates.Manager(target, token)
        self.pools = pools.Manager(target, token)
        self.machines = machines.Manager(target, token)
        self.containers = containers.Manager(target, token)
        self.events = events.Manager(target, token)
