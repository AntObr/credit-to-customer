import json

class Manager:

    data = None
    file = None

    def __init__(this, file):
        this.file = file

    def load(self):
        with open(self.file, 'r') as d:
            self.data = json.load(d)

    def save(self):
        with open(self.file, 'w') as d:
            json.dump(self.data, d, indent=4)

    def add(self, d):
        self.data.append(d)
        # self.save()

    def getData(self):
        return self.data

    def getDataDumps(self, i=0):
        return json.dumps(self.data, indent=i)

    # def search(self, content):
    #     out = []
    #     for x in self.data:
    #         if x[1] == content:
    #             out.append(x[0])
    #     return json.dumps(out)
