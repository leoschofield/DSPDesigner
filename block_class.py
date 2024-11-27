import random
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from line_class import MyLine
from config import *


class Block(Widget):
    def __init__(self,name,nameID,numInputs, numOutputs,numParams, **kwargs):
        super(Block, self).__init__(**kwargs)     
        self.name = name
        self.ID = nameID
        self.xPos = random.randrange(0, WIDGET_MAX_WIDTH-BLOCK_WIDTH*2)
        self.yPos = random.randrange(0, WIDGET_MAX_HEIGHT-BLOCK_WIDTH*2)
        self.selected = RELEASED
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.numParams = numParams
        self.lines = []
        self.inputs = []
        self.outputs = []
        self.params = []
        
        with self.canvas:     
            Color(0.0,0.0,0.0,OPAQUE, mode="rgba")
            self.border = Rectangle(pos=(self.xPos,self.yPos), size=(BLOCK_WIDTH,BLOCK_HEIGHT))
            Color(1.0,1.0,1.0,OPAQUE, mode="rgba")
            self.fill = Rectangle(pos=(self.xPos+BLOCK_BORDER/2,self.yPos+BLOCK_BORDER/2), size=(BLOCK_WIDTH-BLOCK_BORDER, BLOCK_HEIGHT-BLOCK_BORDER))
            self.label = Label(pos=(self.xPos+BLOCK_BORDER, self.yPos+BLOCK_HEIGHT/2),text=self.name,color=(0,0,0,OPAQUE))

            Color(0.0,0.0,1.0,OPAQUE, mode="rgba")
            if self.numInputs == 1:
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numInputs == 2:
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/3), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/3*2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            
            Color(0.0,0.0,1.0,OPAQUE, mode="rgba")
            if self.numOutputs == 1:
                self.outputs.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH-CONNECTOR_WIDTH,self.yPos+BLOCK_HEIGHT), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numOutputs == 2:
                self.outputs.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH-CONNECTOR_WIDTH,self.yPos+BLOCK_HEIGHT/3), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.outputs.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH-CONNECTOR_WIDTH,self.yPos+BLOCK_HEIGHT/3*2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            
            Color(0.5,0.0,0.5,OPAQUE, mode="rgba")
            if self.numParams == 1:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numParams == 2:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/3-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/3*2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numParams == 3:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/4-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/4*3-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numParams == 4:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/5-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/5*2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/5*3-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/5*4-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numParams == 5:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/6-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/6*2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/6*3-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/6*4-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/6*5-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numParams == 6:
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7*2-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7*3-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7*4-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7*5-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.params.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH/7*6-CONNECTOR_WIDTH/2,self.yPos), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))

    def get_connector_name(self,connector):
        if connector == OUTPUT:
            return 'Input'

        if connector == INPUT:
            return 'Output'
    
    def remove_block(self):
        with self.canvas:
            self.canvas.remove(self.background)
            self.canvas.remove(self.fill)
            self.canvas.remove(self.label)
            # if self.inputConnector:
            #     self.canvas.remove(self.input)
            # if self.outputConnector: 
            #     self.canvas.remove(self.output)                
            # if self.nParams == 6:
            #     self.canvas.remove(self.param6Con)
            # if self.nParams >= 5:
            #     self.canvas.remove(self.param5Con)
            # if self.nParams >= 4:                
            #     self.canvas.remove(self.param4Con)
            # if self.nParams >= 3:
            #     self.canvas.remove(self.param3Con)
            # if self.nParams >= 2:
            #     self.canvas.remove(self.param2Con)
            # if self.nParams >= 1:
            #     self.canvas.remove(self.param1Con)   
            self.canvas.ask_update()

    def move_block(self,touch):
        if self.selected == SELECTED:
            if touch.pos[X] > 20:
                if touch.pos[X] + self.border.size[X] < WIDGET_MAX_WIDTH:
                    if touch.pos[Y] > 20:
                        if touch.pos[Y] + self.border.size[Y] < WIDGET_MAX_HEIGHT:
                            if len(blocks) == 1:#if only this block is in the list - move block                    
                                self.border.pos = touch.pos
                                self.fill.pos = (touch.pos[X]+BLOCK_BORDER/2,touch.pos[Y]+BLOCK_BORDER/2)
                                self.label.pos = (touch.pos[X]+BLOCK_BORDER, touch.pos[Y] - (self.border.size[Y]/2))
                                self.move_connectors(touch,True,True)
                                
                            else:  # check for block-block collisions  
                                for secondBlock in blocks:
                                    print (secondBlock.name)              
                                    if self.name != secondBlock.name: # dont compare a block with itself
                                        if self.is_collision(secondBlock):
                                            print("collision")
                                            moveUp = 1
                                            moveDown = 1
                                            moveLeft = 1
                                            moveRight = 1
                                            allowX = 0
                                            allowY = 0
                                            # restrict movement based on relative position of colliding blocks
                                            if self.border.pos[X] + BLOCK_WIDTH > secondBlock.border.pos[X] + BLOCK_WIDTH + THRESH:
                                                moveLeft = 0
                                            if self.border.pos[X] < secondBlock.border.pos[X] - THRESH:
                                                moveRight = 0
                                            if self.border.pos[Y] + BLOCK_HEIGHT > secondBlock.border.pos[Y] + BLOCK_HEIGHT + THRESH:
                                                moveDown = 0
                                            if self.border.pos[Y] < secondBlock.border.pos[Y] - THRESH:
                                                moveUp = 0
                                            # check movement and movement restrictions    
                                            if touch.pos[X] < self.border.pos[X]: # left movement
                                                if moveLeft:
                                                    allowX = 1
                                            else: # right movement
                                                if moveRight:
                                                    allowX = 1
                                            if touch.pos[Y] > self.border.pos[Y]: # up movement
                                                if moveUp:
                                                    allowY = 1
                                            else: # down movement
                                                if moveDown:
                                                    allowY = 1   
                                            # move the block if allowed
                                            temp = list(self.border.pos)
                                            if allowX:
                                                temp[X] = touch.pos[0]
                                                self.label.pos[X] = touch.pos[X]
                                            if allowY:
                                                temp[Y] = touch.pos[1]
                                            self.border.pos = tuple(temp)
                                            self.fill.pos = (tuple(temp)[X]+BLOCK_BORDER/2,tuple(temp)[Y]+BLOCK_BORDER/2)
                                            if allowX or allowY:
                                                self.border.pos = touch.pos
                                                self.fill.pos = (touch.pos[X]+BLOCK_BORDER/2,touch.pos[Y]+BLOCK_BORDER/2)
                                                self.label.pos = (touch.pos[X]+BLOCK_BORDER, touch.pos[Y] - (self.border.size[Y]/2))
                                                self.move_connectors(touch,allowX,allowY)                                            
                                            return
                                else: # no collisions - move block      
                                    self.border.pos = touch.pos
                                    self.fill.pos = (touch.pos[X]+BLOCK_BORDER/2,touch.pos[Y]+BLOCK_BORDER/2)
                                    self.label.pos = (touch.pos[X]+BLOCK_BORDER, touch.pos[Y] - (self.border.size[Y]/2))
                                    self.move_connectors(touch,allowX,allowY)                                                                               

    def release_block(self,touch):
        self.selected = RELEASED 

    def is_touch_detected(self,touch,moving):
        if touch.pos[X] > self.border.pos[X] and touch.pos[X] < (self.border.pos[X] + self.border.size[X]):
            if touch.pos[Y] > self.border.pos[Y] and touch.pos[Y] < (self.border.pos[Y] + self.border.size[Y]):
                if moving == STILL:
                    self.selected = SELECTED
                    self.is_inside_connector(touch,ASSIGN_LINE) #assign a line if inside a connector
                    return 1 
        return 0            
                    
    def is_collision(self,secondBlock):
        if self.border.pos[X] < secondBlock.border.pos[X] + secondBlock.border.size[X] + THRESH:        
            if self.border.pos[X] + self.border.size[X] > secondBlock.border.pos[X] - THRESH:
                if self.border.pos[Y] < secondBlock.border.pos[Y] + secondBlock.border.size[Y] + THRESH:        
                    if self.border.pos[Y] + self.border.size[Y] > secondBlock.border.pos[Y] - THRESH:
                        return COLLISION

        #  kivy collide_widget method (don't think it works well)
        # if self.name is not None:
        #     if self.collide_widget(secondBlock):
        #         return COLLISION
        return NO_COLLISION                

    def assign_line(self,touch, start_connector):
        with self.canvas:
            conLine = MyLine(touch,self,start_connector)
            self.lines.append(conLine)

    def move_connectors(self,touch,moveX,moveY):
            if self.numInputs == 1:
                print(self.inputs[0].pos)
                temp = list(self.inputs[0].pos)
                if moveX:
                    temp[X] = touch.pos[X]
                if moveY:
                    temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/2
                self.inputs[0].pos = tuple(temp)

            elif self.numInputs == 2:
                temp = list(self.inputs[0].pos)
                if moveX:
                    temp[X] = touch.pos[X]
                if moveY:
                    temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3
                self.inputs[0].pos = tuple(temp)

                temp = list(self.inputs[1].pos)
                if moveX:
                    temp[X] = touch.pos[X]
                if moveY:
                    temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3*2
                self.inputs[1].pos = tuple(temp)

            # if self.numOutputs == 1:
                # if move     

              
            # for conLine in self.lines: # move connected lines
            #     if conLine.start_block.name == self.name:
            #         if conLine.start_connector == INPUT:
            #             conLine.move_line(temp[X]+CONNECTOR_WIDTH/2,temp[Y]+CONNECTOR_HEIGHT/2) 
            #     elif conLine.end_block.name == self.name:
            #         if conLine.end_connector == INPUT:
            #             conLine.move_line(temp[X]+CONNECTOR_WIDTH/2,temp[Y]+CONNECTOR_HEIGHT/2) 


    def is_inside_connector(self,touch,allow_assign_line):

        # #============================================
        # if self.inputConnector:
        #     if touch.pos[X] > self.input.pos[X] and touch.pos[X] < (self.input.pos[X] + self.input.size[X]):
        #         if touch.pos[Y] > self.input.pos[Y] and touch.pos[Y] < (self.input.pos[Y] + self.input.size[Y]):
        #             self.selected = RELEASED
        #             if allow_assign_line:
        #                 if self.lines != []: # if there are lines
        #                     for conLine in self.lines:
        #                         if conLine.start_block.name == self.name: #line starts in this block
        #                             if conLine.start_connector == INPUT: #dont assign a new line if there is one on this connector   
        #                                 return INPUT 
        #                         elif conLine.end_block.name == self.name: #line ends in this block
        #                             if conLine.end_connector == INPUT: #dont assign a new line if there is one on this connector   
        #                                 return INPUT  
        #                     self.assign_line(touch,INPUT)                  
        #                 else: #assign a line as there are none connected to this block
        #                     self.assign_line(touch,INPUT)
        #             return INPUT  
                
        # #============================================
        # if self.outputConnector:
        #     if touch.pos[X] > self.output.pos[X] and touch.pos[X] < (self.output.pos[X] + self.output.size[X]):
        #         if touch.pos[Y] > self.output.pos[Y] and touch.pos[Y] < (self.output.pos[Y] + self.output.size[Y]):
        #             self.selected = RELEASED
        #             if allow_assign_line:
        #                 if self.lines != []: # if there are lines
        #                     for conLine in self.lines:
        #                         if conLine.start_block.name == self.name: #line starts in this block
        #                             if conLine.start_connector == OUTPUT: #dont assign a new line if there is one on this connector   
        #                                 return OUTPUT  
        #                         elif conLine.end_block.name == self.name: #line ends in this block
        #                             if conLine.end_connector == OUTPUT: #dont assign a new line if there is one on this connector   
        #                                 return OUTPUT  
        #                     self.assign_line(touch,OUTPUT)                  
        #                 else: #assign a line as there are none connected to this block
        #                     self.assign_line(touch,OUTPUT)
        #             return OUTPUT 
        return 0