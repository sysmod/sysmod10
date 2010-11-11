from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_History(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 46, 54
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 1
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"default","self.semanticObject.", [], [])
        constObj.setValue(('default', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import statechart_utils\nstatechart_utils.History_Visual_EDIT_CREATE(self)\n'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([4.0, 3.0, 40.0, 38.0]), tags = self.tag, stipple= '', width= '2.0', outline= 'darkblue', fill= 'lightblue')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_text(self.translate([21.0, 22.0]), tags = self.tag, stipple= '', width= '0', fill= 'black', text= 'H', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_oval(self.translate([22.0, 3.0, 22.0, 3.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([39.0, 21.0, 39.0, 21.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([22.0, 38.0, 22.0, 38.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([4.0, 22.0, 4.0, 22.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_text(self.translate([29.0, 22.0]), tags = self.tag, stipple= '', width= '0', fill= 'black', text= '*', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([23.0, 47.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["name"] = h
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

    def default(self,params):
       import statechart_utils
       statechart_utils.History_Visual_EDIT_CREATE(self)
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT or actionID == self.CREATE:
         res = self.default(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_History
