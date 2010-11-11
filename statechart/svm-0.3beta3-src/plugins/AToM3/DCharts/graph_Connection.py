from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Connection(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 160, 41
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([14.0, 15.0, 22.0, 23.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        h = drawing.create_oval(self.translate([113.0, 14.0, 121.0, 22.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)
        h = drawing.create_line(self.translate([23.0, 19.0, 113.0, 19.0]), tags = self.tag, stipple= '', width= '2.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'black')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)
        if self.semanticObject: drawText = self.semanticObject.port.toString(25,5)
        else: drawText = "<port>"
        h = drawing.create_text(self.translate([18.0, 34.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["port"] = h
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        if self.semanticObject: drawText = self.semanticObject.server_port.toString(25,5)
        else: drawText = "<server_port>"
        h = drawing.create_text(self.translate([120.0, 34.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["server_port"] = h
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([70.0, 7.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["name"] = h
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Connection
