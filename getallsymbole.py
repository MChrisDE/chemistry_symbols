class Element:
    def __init__(self, *args):
        self.n = args[0].replace("\t", "")  # number (of protons)
        self.short = args[1]  # symbol
        self.name = args[2]  # is obvious
        self.color = args[3]  # bg color

    def __str__(self):
        return 'element n°: {self.n}, name: {self.name} ({self.short}), color: {self.color}'.format(self=self)


class ElementList(dict):
    def __init__(self, *args):
        self.master = None
        for arg in args:
            self[arg.short] = arg

    def __str__(self):
        return '\n'.join([str(self[element]) for element in self])

    def __getitem__(self, item):
        buffer=[]
        for i in range(len(self),0):



    def get_el(self, el) -> Element:
        return self[el]

    def getallsymbole(self) -> list:
        return [self.get_el(el).short for el in self]

    def getallnames(self) -> list:
        return [self.get_el(el).name for el in self]

    def getallns(self) -> list:
        return [self.get_el(el).n for el in self]

    def set_master(self, master):
        self.master = master

    def create_text(self, master, **kwargs):
        if master is None:
            master = self.master
        if master is None:
            print('Could not create text ({}) with master: None'
                  ''.format(', '.join(['{kw}: {arg}'.format(kw=kw, arg=arg) for kw, arg in kwargs])))
            # create text with kwargs: showNumbers, showFullNames


def get_all() -> ElementList:
    with open("db.csv") as f:  # db.csv for 8-bit colors, db2.csv for 12-bit colors
        lines = f.read().splitlines()
    return ElementList(*[Element(*line.split(',')) for line in lines])
