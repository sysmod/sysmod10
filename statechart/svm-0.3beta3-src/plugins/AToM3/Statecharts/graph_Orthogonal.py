from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Orthogonal(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 65, 75
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 1
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([34.0, 72.0, 34.0, 72.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([5.0, 43.0, 5.0, 43.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([62.0, 44.0, 62.0, 44.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([32.0, 16.0, 32.0, 16.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_rectangle(self.translate([5.0, 16.0, 62.0, 72.0]), tags = self.tag, stipple= '', width= '2.0', outline= 'DARKGRAY', fill= '')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([23.0, 7.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'black', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["name"] = h
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Orthogonal
