from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Port(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 46, 51
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([3.0, 10.0, 8.0, 28.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_polygon(self.translate([8.0, 10.0, 16.0, 2.0, 16.0, 36.0, 8.0, 28.0, 8.0, 28.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', outline= 'black', smooth= 0, fill= '')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)
        h = drawing.create_oval(self.translate([16.0, 3.0, 16.0, 3.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([16.0, 36.0, 16.0, 36.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([16.0, 11.0, 16.0, 11.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([16.0, 20.0, 16.0, 20.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([16.0, 28.0, 16.0, 28.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([23.0, 44.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["name"] = h
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Port
