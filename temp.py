class Classy():
    
    def __init__(self):
        self.items = []
    def addItem(s):
        self.items.append(s)
    def getClassiness():
        score = 0
        for i in self.items:
            if i == "tophat":
                score+=2
            elif i == "bowtie":
                score+=4
            elif i == "monocle":
                score+=5
            else:
                score+=0
        return score
# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())