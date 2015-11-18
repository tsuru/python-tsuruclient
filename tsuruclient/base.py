class Manager(object):
    def __init__(self, target, token):
        self.target = target
        self.token = token

    @property
    def headers(self):
        return {"authorization": "bearer {}".format(self.token)}
