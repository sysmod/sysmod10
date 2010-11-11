from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Composite(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 68, 70
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 1
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"Composite_Visual_CREATE","self.semanticObject.", [], [])
        constObj.setValue(('Composite_Visual_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Composite_Visual_CREATE(self)\n'))
        self.constraintList.append(constObj)

        constObj = ATOM3Constraint(atribs,"Composite_Visual_EDIT","self.semanticObject.", [], [])
        constObj.setValue(('Composite_Visual_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Composite_Visual_EDIT(self)\n'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([39.0, 67.0, 39.0, 67.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([65.0, 41.0, 65.0, 41.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([39.0, 16.0, 39.0, 16.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([13.0, 41.0, 13.0, 41.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_rectangle(self.translate([13.0, 16.0, 65.0, 67.0]), tags = self.tag, stipple= '', width= '2.0', outline= 'darkblue', fill= '')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([23.0, 7.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'black', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["name"] = h
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)

    def Composite_Visual_CREATE(self,params):
       import DCharts_utils
       DCharts_utils.Composite_Visual_CREATE(self)
       
    def Composite_Visual_EDIT(self,params):
       import DCharts_utils
       DCharts_utils.Composite_Visual_EDIT(self)
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.CREATE:
         res = self.Composite_Visual_CREATE(params)
         if res: return res
       if actionID ==  self.EDIT:
         res = self.Composite_Visual_EDIT(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Composite
