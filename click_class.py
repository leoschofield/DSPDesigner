from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.button import Label
from block_class import Block
from config import *


class Click(Widget):
    def __init__(self, **kwargs):
        super(Click, self).__init__(**kwargs)     
        with self.canvas:
            Rectangle(pos=(0,0), size=(WIDGET_MAX_WIDTH,WIDGET_MAX_HEIGHT-BUTTON_HEIGHT))
            self.paramlabel = Label(pos=(0, 0),text="",color=(0,0,0))
            
        self.label_released = 1

    def destroy_label(self):
        with self.canvas:
            self.paramlabel.text =""
            self.label_released = 1

    def update_label(self,mousepos,name):
        if name is not None:
            with self.canvas:
                if self.label_released == 1:
                    self.paramlabel.pos=(mousepos[X], mousepos[Y]+BLOCK_HEIGHT)
                    self.paramlabel.text=name
                    self.label_released = 0

    def assign_block(self,name,numInputs,numOutputs,numParams,isFungible):
        with self.canvas:
            nameCounter = 0
            create_block = 0

            if blocks == []:
                block = Block(name,nameCounter,numInputs,numOutputs,numParams,isFungible)   
                blocks.append(block)
            else:
                while create_block == 0:
                    for block in blocks:
                        temp = name + " " + str(nameCounter)
                        if temp[:-1] == block.label.text[:-1]: # if block names match
                            for block in blocks: # now check for block names and number matches
                                temp = name + " " + str(nameCounter)
                                if temp == block.name:
                                    nameCounter = nameCounter + 1
                            create_block = 1
                        else:
                            create_block = 1
                block = Block(name,nameCounter,numInputs,numOutputs,numParams,isFungible) 
                blocks.append(block)
                
    def detect_collisions(self, touch, moving):
        for block in blocks:
            if block.is_touch_detected(touch,moving): 
                return True
        return False

    def on_touch_down(self, touch):
        if blocks != []:
            for block in blocks:
                if block.lines != []:
                    for line in block.lines:   
                        if line.dragging == DRAGGING:
                            line.drag_line(touch,DRAG_MODE0)
                            return #don't check for collision with block if dragging a line
            self.detect_collisions(touch,STILL)

    def on_touch_move(self, touch):
        if blocks != []:
            for block in blocks:
                block.move_block(touch)
                # if block.lines != []: 
                #     for line in block.lines:
                #         if line.dragging == DRAGGING:
                #             line.drag_line(touch,DRAG_MODE0)

    def on_touch_up(self,touch):
        for block1 in blocks:
            block1.release_block()
            if block1.lines != []: # if there are lines 
                for line in block1.lines: 
                    if line.dragging == DRAGGING: # letting go of a line that hasn't been linked to end block yet
                        for block2 in blocks: # search through the other blocks to see if end of line (mouse pointer) is inside a connector
                            if block1.name != block2.name: # dont let a block connect to itself
                                newConnector = block2.is_inside_connector(touch,DONT_ASSIGN_LINE)
                                if newConnector != False: # inside a connector of block 2?  
                                    if block2.lines != []: # block2 has lines?
                                        for line2 in block2.lines:
                                            if line2.start_block.name == block2.name: #only check the connections that start on block 2
                                                if line2.start_connector == newConnector:
                                                    return # found line that is connected here so break out so cursor keeps hold of line
                                            elif line2.end_block.name == block2.name: #...or end on block 2 
                                                if line2.end_connector == newConnector:
                                                    return # found line that is connected here so break out so that cursor keeps hold of line              
                                        line.dragging = NOT_DRAGGING
                                        line.end_block = block2
                                        line.end_connector = newConnector
                                        line.name += (" " + block2.name + " " + str(line.end_connector))
                                        # print(line.name)
                                        block2.lines.append(line) # add the newly connected line to the list of lines    
                                    else: # block 2 has no lines            
                                        line.dragging = NOT_DRAGGING
                                        line.end_block = block2
                                        line.end_connector = newConnector
                                        line.name += (" " + block2.name + " " + str(line.end_connector))
                                        block2.lines.append(line) # add the newly connected line to the list of lines
                                        # print(line.name)
                                        break       