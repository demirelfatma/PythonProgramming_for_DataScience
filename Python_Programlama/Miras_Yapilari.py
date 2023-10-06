# Miras Yapilari(inheritance)

class Employees():
    def __init__(self, FirstName, LastName, Address):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

ali = Employees("FirstName", "LastName", "Address")
ali.FirstName

class DataScience():
    def __init__(self):
        self.Programming = ""
        
veribilimci1 = DataScience()
veribilimci1.Programming

class Marketing():
    def __init__(self):
        self.StoryTelling = ""
        
mar1 = Marketing()
mar1.StoryTelling