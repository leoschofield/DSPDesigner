from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from block_class import Block
from config import *


class Click(Widget):
    def __init__(self, **kwargs):
        super(Click, self).__init__(**kwargs)     
        with self.canvas:
            Rectangle(pos=(0,0), size=(WIDGET_MAX_WIDTH,WIDGET_MAX_HEIGHT-BUTTON_HEIGHT))

    def assign_block(self,name,numInputs,numOutputs,numParams):
        with self.canvas:
            nameCounter = 0
            create_block = 0
                        
            if blocks == []:
                block = Block(name,nameCounter,numInputs,numOutputs,numParams)   
                blocks.append(block)
            else:
                while create_block == 0:
                    for block in blocks:
                        temp = name + " " + str(nameCounter)
                        if temp[:-1] == block.label.text[:-1]: #if block names match
                            for block in blocks: #now check for block names and number matches
                                temp = name + " " + str(nameCounter)
                                if temp == block.name:
                                    nameCounter = nameCounter + 1
                            create_block = 1
                        else:
                            create_block = 1
                name = name + " " + str(nameCounter)
                block = Block(name,nameCounter,numInputs,numOutputs,numParams) 
                blocks.append(block)
                
    def detect_collisions(self, touch, moving):
        for block in blocks:
            if block.is_touch_detected(touch,moving): 
                return TRUE
        return FALSE

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
                #     for conLine in block.lines:
                #         if conLine.dragging == DRAGGING:
                #             conLine.drag_line(touch,DRAG_MODE0)

    def on_touch_up(self,touch):
        for block1 in blocks:
            block1.release_block(touch)
            if block1.lines != []: #if there are lines 
                for conLine in block1.lines: 
                    if conLine.dragging == DRAGGING:#letting go of a line that hasn't been linked to end block yet
                        for block2 in blocks: #search through the other blocks to see if end of line (mouse pointer) is inside a connector
                            if block1.name != block2.name: #dont let a block connect to itself
                                newConnector = block2.is_inside_connector(touch,DONT_ASSIGN_LINE) #inside a connector of block 2?
                                if newConnector != 0:                                             # ...yes!
                                    if newConnector is not None:   #here only allow line to stop dragging if inside a valid connector, which depends on the start connector
                                        if((conLine.start_connector == OUTPUT or conLine.start_connector == SPLITTER+1 or conLine.start_connector == SPLITTER+2) and (newConnector == INPUT or newConnector == MIXER+1 or newConnector == MIXER+2)) or \
                                            ((conLine.start_connector == INPUT or conLine.start_connector == MIXER + 1 or conLine.start_connector == MIXER + 2) and (newConnector == OUTPUT or newConnector == SPLITTER + 1 or newConnector == SPLITTER + 2)) or \
                                            (conLine.start_connector <= MAX_PARAMS and newConnector == VAL_OUT) or \
                                            (conLine.start_connector == VAL_OUT and newConnector <= MAX_PARAMS) or \
                                            ((conLine.start_connector == USER0OUT or conLine.start_connector == USER1OUT) and newConnector == USER_BLOCK_IN) or \
                                            (conLine.start_connector == USER_BLOCK_IN and (newConnector == USER0OUT or newConnector == USER1OUT)) or \
                                            (conLine.start_connector == TAP_IN and newConnector == TAP_OUT) or \
                                            (conLine.start_connector == TAP_OUT and newConnector == TAP_IN) or \
                                            (conLine.start_connector == SWITCH_OUT and (newConnector >= SW0_IN and newConnector <= SW4_IN)) or \
                                            ((conLine.start_connector >= SW0_IN and conLine.start_connector <= SW4_IN) and newConnector == SWITCH_OUT):
                                                if block2.lines != []: # block2 has lines?
                                                    for conLine2 in block2.lines:
                                                        if conLine2.start_block.name == block2.name: #only check the connections that start on block 2
                                                            if conLine2.start_connector == newConnector:
                                                                return #found line that is connected here so break out so cursor keeps hold of line
                                                        elif conLine2.end_block.name == block2.name:#...or end on block 2 
                                                            if conLine2.end_connector == newConnector:
                                                                return #found line that is connected here so break out so that cursor keeps hold of line              
                                                    conLine.dragging = NOT_DRAGGING
                                                    conLine.end_block=block2
                                                    conLine.end_connector = newConnector
                                                    conLine.name += (" " + block2.name + " " + str(conLine.end_connector))
                                                    block2.lines.append(conLine)# add the newly connected line to the list of lines    
                                                else: #block 2 has no lines            
                                                    conLine.dragging = NOT_DRAGGING
                                                    conLine.end_block=block2
                                                    conLine.end_connector = newConnector
                                                    conLine.name += (" " + block2.name + " " + str(conLine.end_connector))
                                                    block2.lines.append(conLine)# add the newly connected line to the list of lines
                                                    break       