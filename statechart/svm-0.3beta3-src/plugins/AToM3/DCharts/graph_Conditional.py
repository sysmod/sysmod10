from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Conditional(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 41, 43
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 1
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"Conditional_Visual_EDIT","self.semanticObject.", [], [])
        constObj.setValue(('Conditional_Visual_EDIT', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Conditional_Visual_EDIT(self)\n'))
        self.constraintList.append(constObj)

        constObj = ATOM3Constraint(atribs,"Conditional_Visual_CREATE","self.semanticObject.", [], [])
        constObj.setValue(('Conditional_Visual_CREATE', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'import DCharts_utils\nDCharts_utils.Conditional_Visual_CREATE(self)\n'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([3.0, 3.0, 38.0, 40.0]), tags = self.tag, stipple= '', width= '2.0', outline= 'darkblue', fill= 'lightblue')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_text(self.translate([21.0, 23.0]), tags = self.tag, stipple= '', width= '0', fill= 'black', text= 'C', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_oval(self.translate([21.0, 3.0, 21.0, 3.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([21.0, 40.0, 21.0, 40.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([38.0, 22.0, 38.0, 22.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 22.0, 3.0, 22.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)

    def Conditional_Visual_EDIT(self,params):
       import DCharts_utils
       DCharts_utils.Conditional_Visual_EDIT(self)
       
    def Conditional_Visual_CREATE(self,params):
       import DCharts_utils
       DCharts_utils.Conditional_Visual_CREATE(self)
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT:
         res = self.Conditional_Visual_EDIT(params)
         if res: return res
       if actionID ==  self.CREATE:
         res = self.Conditional_Visual_CREATE(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Conditional
