from Tkinter         import *
from ATOM3Type       import *
from ATOM3Exceptions import *
from types           import *
from string          import replace

class DChartsEvent(ATOM3Type):

    def __init__(self, valInitial=""):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )
       self.strValue = str(valInitial)			# Attribute to store the value
       self.params = {}
       self.strEntry = None				# widget to be create when show is called

    def isNone (self):
       "check if the type value is none"
       if self.strValue == '' or self.strValue == None: return 1
       return 0

    def setNone (self):
       "sets to None the attribute value"
       self.strValue = ''

    def setValue(self, value):
       "Sets the actual attribute value"
       # check that we have the correct type (a string)
       if type(value) != StringType and type(value) != NoneType:
          raise ATOM3BadAssignmentValue, "in setValue(), a string was expected"
       self.strValue = value
       if self.strEntry:
         self.strEntry.delete(0, END)			# delete from graphical field
         if value:
            self.strEntry.insert(0, value)		# insert into graphical field

    def getParam(self, name):
        try:
            value = self.params[name]
        except KeyError:
            value = None
        return value

    def setParam(self, name, value):
        self.params[name] = value

    def getValue(self):
       "Gets the actual attribute value"
       if self.strEntry:
          self.strValue = self.strEntry.get()
       return self.strValue

    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if self.strEntry:
          self.strValue = self.strEntry.get()
       if self.strValue:
          if type(self.strValue) == StringType:
             if maxWide: return self.strValue[0:maxWide]
             elif self.strValue: return str(self.strValue)
          else: return str(self.strValue)
       else: return ""

    def show(self, parent, parentTopWindow = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentTopWindow )

       self.strEntry = Entry(parent)
       self.strEntry.insert(0, self.strValue)
       return self.strEntry

    def destroy(self):
       "Stores the widget value into the variable"
       if self.strEntry:
          self.strValue = self.strEntry.get()
          self.strEntry = None

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3String()
       cloneObject.parent   = self.parent
       cloneObject.mode     = self.mode
       cloneObject.strValue = self.strValue
       cloneObject.strEntry = self.strEntry
       cloneObject.params   = self.params.copy()
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.strValue = other.strValue
       self.strEntry = other.strEntry

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       replacedStr = self.toString()                                        # Added 27/July/2002 by JL
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')                 # Added 27/July/2002 by JL
       replacedStr = replace( replacedStr, "'", "\\'")                      # Added 27/July/2002 by JL    
       replacedStr = replace( replacedStr, '\n', '\\n')                     # Added 27/July/2002 by JL
       file.write(indent+objName+"=ATOM3String('"+replacedStr+"')\n")       # Modified 27/July/2002 by JL

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       replacedStr = self.toString()                                        # Added 27/July/2002 by JL
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')                 # Added 27/July/2002 by JL
       replacedStr = replace( replacedStr, "'", "\\'")                      # Added 27/July/2002 by JL    
       replacedStr = replace( replacedStr, '\n', '\\n')                     # Added 27/July/2002 by JL       
       file.write(indent+objName+".setValue('"+replacedStr+"')\n")          # Modified 27/July/2002 by JL
