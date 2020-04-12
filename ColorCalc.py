#Destiny G. Nunn Color Calculator for Houdini
#you need to load this into houdini for it to work
#Example of what input the user needs to put into the text editor of houdini is ColorSwatch("A", .23, .45, .88)

import math

class ColorSwatch:
    """Color Calculator"""
    #topNode
    topNode = hou.node("/obj")
    count = 0 #to follow iterations on how many times its been called
    #color Container node
    container = None
    #mergeSOP
    mergeSOP = None
    
    def __init__(self, name="default", red = 0.0, green = 0.0, blue = 0.0): #constructor
        self.colorName = name #name of the color
        self.rVal = red #red color value
        self.gVal = green #green color value
        self.bVal = blue #blue color value
        
        if ColorSwatch.count == 0:
            self.initialize()
            
        self.createSwatchNodes() #will create the node tree for the swatches
        
    def initialize(self):
        """where I initiallize container and merge node"""
#        print "initializing"
        ColorSwatch.container = ColorSwatch.topNode.createNode("geo","Container")
        #merge node
        ColorSwatch.mergeSOP = ColorSwatch.container.createNode("merge", "mergeSOP")
                             
    def __setattr__(self, name, value):
        """SETATTR override function, BEWARE!!!"""        
        max = 1               
        min = 0
                        
        if name == 'rVal' or name =='gVal' or name == 'bVal':
            if value > max:
                value = max
            if value < min:
                value = min
            self.__dict__[name] = value 
                
        if name =='colorName':
            self.__dict__[name] = value
            #creates a color dictionary called value
                                      
                                              
    def __str__(self):
        """string override method to print out colors with strings"""
        return "color: {} ({}, {}, {})".format(self.colorName, self.rVal, self.gVal, self.bVal)
        
    def createSwatchNodes(self):
        """This is where the nodes are created and connected"""
        #mergeNode for each individualSwatch
        mergeColors = ColorSwatch.container.createNode("merge", "colorCalMerge")
       
        #creates swatch
        swatch = ColorSwatch.container.createNode("grid","swatch")
        #making grid a 1x1 square
        swatch.parm('sizex').set('1')
        swatch.parm('sizey').set('1')
        #make orientation of grid XY
        swatch.parm('orient').set(0)
        #make rows and columns 2x2
        swatch.parm('rows').set('2')
        swatch.parm('cols').set('2')
        
        #swatchColorNode to swatch
        swatchColor = ColorSwatch.container.createNode('color','SwatchColor')
        myColor = hou.Color((0.0,0.0,0.0)) #makes myColor connect to houColor node
        myColor.setRGB((self.rVal,self.gVal,self.bVal))
        swatchColor.parmTuple('color').set(myColor.rgb()) #connect myColor and colorNode together
        swatchColor.setInput(0, swatch) #connects color to swatch node
        mergeColors.setInput(0,swatchColor) #connects color node to mergeColors
        
        #fontNode#
        font = ColorSwatch.container.createNode('font','FONT')
        buff = "{}({}, {}, {})".format(self.colorName, self.rVal, self.gVal, self.bVal)
        font.parm('text').set(buff) #sets the text in relation to the colorname, and rgb colors
        font.parm('fontsize').set(0.1) #font Size
        font.parm('ty').set('-0.75') #font Transformation
        #fontColorNode
        fontColor = ColorSwatch.container.createNode('color', 'FontColor')
        fontColor.parmTuple('color').set((0,0,0)) #makes font color black
        fontColor.setInput(0, font) #connects fontColor to font node
        mergeColors.setInput(1, fontColor) #connects fontColor to mergeColors into second input
        
        #transform the swatch and fonts
        swatchGrpTrans = ColorSwatch.container.createNode('xform')
        y = ColorSwatch.count/5 * -1.5
        x = ColorSwatch.count % 5 * 1.5
        swatchGrpTrans.parm('ty').set(y)
        swatchGrpTrans.parm('tx').set(x)
        swatchGrpTrans.setInput(0, mergeColors) #connects mergeColors to swatchGrpTrans
        
        #connect the transform nodes to the mergeSOP 
        ColorSwatch.mergeSOP.setInput(ColorSwatch.count,swatchGrpTrans)
        ColorSwatch.count += 1 #adds a count number each iteration
        #layout node editor
        ColorSwatch.container.layoutChildren()
        
    #####OVERRIDES#####
    
    def __add__(self, other):
        """adds two colors together and returns the sum of the new one"""
        newName = "{} + {}".format(self.colorName, other.colorName)
        return ColorSwatch(newName, (self.rVal + other.rVal),(self.gVal + other.gVal), (self.bVal + other.bVal)) 
        
    def __sub__(self, other):
        """subtracts two colors together and returns the sum of the new one"""
        newName = "{} - {}".format(self.colorName, other.colorName)
        return ColorSwatch(newName, (self.rVal - other.rVal), (self.gVal - other.gVal), (self.bVal - other.bVal))
        
    def __mul__(self, other):
        """Multiply two colors together"""
        newName = "{} * {}".format(self.colorName, other.colorName)
        return ColorSwatch(newName, self.rVal*other.rVal, self.gVal*other.gVal, self.bVal * other.bVal)
    def __invert__(self):
        """inversion of colors"""
        newName = "~{}".format(self.colorName)
        return ColorSwatch(newName, ( 1 - self.rVal), (1- self.gVal), (1 - self.bVal))
