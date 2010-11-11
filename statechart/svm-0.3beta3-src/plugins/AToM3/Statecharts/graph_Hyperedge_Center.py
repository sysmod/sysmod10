from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Hyperedge_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 56, 14
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        if self.semanticObject: drawText = self.semanticObject.display.toString(25,5)
        else: drawText = "<display>"
        h = drawing.create_text(self.translate([28.0, 7.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["display"] = h
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Hyperedge_Center
