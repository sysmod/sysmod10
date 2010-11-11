from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_visual_settings(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 104, 53
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([1.0, 1.0, 94.0, 52.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_text(self.translate([48.0, 27.0]), tags = self.tag, stipple= '', width= '0', fill= 'black', text= 'Visual Settings', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_visual_settings
