from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Server(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 106, 79
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_polygon(self.translate([81.0, 39.0, 97.0, 49.0, 31.0, 49.0, 49.0, 39.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', outline= 'black', smooth= 0, fill= '')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        h = drawing.create_rectangle(self.translate([31.0, 49.0, 97.0, 53.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)
        h = drawing.create_rectangle(self.translate([40.0, 1.0, 88.0, 37.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf17 = GraphicalForm(drawing, h, "gf17")
        self.graphForms.append(self.gf17)
        h = drawing.create_rectangle(self.translate([42.0, 5.0, 86.0, 33.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= 'black')
        self.gf21 = GraphicalForm(drawing, h, "gf21")
        self.graphForms.append(self.gf21)
        h = drawing.create_line(self.translate([46.0, 10.0, 48.0, 10.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'gray')
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)
        h = drawing.create_line(self.translate([56.0, 10.0, 58.0, 10.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'gray')
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)
        h = drawing.create_line(self.translate([51.0, 10.0, 53.0, 10.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'gray')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)
        h = drawing.create_line(self.translate([50.0, 42.0, 80.0, 42.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'black')
        self.gf9 = GraphicalForm(drawing, h, "gf9")
        self.graphForms.append(self.gf9)
        h = drawing.create_line(self.translate([46.0, 44.0, 84.0, 44.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'black')
        self.gf10 = GraphicalForm(drawing, h, "gf10")
        self.graphForms.append(self.gf10)
        h = drawing.create_line(self.translate([43.0, 46.0, 87.0, 46.0]), tags = self.tag, stipple= '', width= '1.0', splinesteps= '12', arrowshape= '8 10 3', arrow= 'none', capstyle= 'butt', smooth= 0, joinstyle= 'round', fill= 'black')
        self.gf11 = GraphicalForm(drawing, h, "gf11")
        self.graphForms.append(self.gf11)
        h = drawing.create_rectangle(self.translate([9.0, 6.0, 28.0, 53.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf12 = GraphicalForm(drawing, h, "gf12")
        self.graphForms.append(self.gf12)
        h = drawing.create_rectangle(self.translate([12.0, 9.0, 25.0, 53.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf19 = GraphicalForm(drawing, h, "gf19")
        self.graphForms.append(self.gf19)
        h = drawing.create_rectangle(self.translate([12.0, 16.0, 25.0, 23.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= '')
        self.gf20 = GraphicalForm(drawing, h, "gf20")
        self.graphForms.append(self.gf20)
        h = drawing.create_oval(self.translate([28.0, 53.0, 28.0, 53.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 35.0, 9.0, 35.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([19.0, 53.0, 19.0, 53.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 53.0, 9.0, 53.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 44.0, 9.0, 44.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([19.0, 5.0, 19.0, 5.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 25.0, 9.0, 25.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 5.0, 9.0, 5.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([28.0, 5.0, 28.0, 5.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([9.0, 15.0, 9.0, 15.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([28.0, 15.0, 28.0, 15.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([28.0, 44.0, 28.0, 44.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([28.0, 25.0, 28.0, 25.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([28.0, 35.0, 28.0, 35.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.id.toString(25,5)
        else: drawText = "<id>"
        h = drawing.create_text(self.translate([92.0, 65.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'blue', font= 'Helvetica -12', anchor= 'center', justify= 'left')
        self.attr_display["id"] = h
        self.gf10 = GraphicalForm(drawing, h, "gf10")
        self.graphForms.append(self.gf10)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Server
