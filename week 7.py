class Tracking:
    def __init__(self, tid):
        self.tid = tid
        self.history = []

    def update(self, location):
        self.history.append(location)

    def show(self):
        for h in self.history:
            print(h)