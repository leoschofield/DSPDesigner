import random
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from line_class import MyLine
from config import *


class Block(Widget):
    def __init__(self,name,nameID,numInputs, numOutputs,numParams, isFungible, **kwargs):
        super(Block, self).__init__(**kwargs)     
        self.name = name+" "+str(nameID)
        self.ID = nameID
        self.xPos = random.randrange(0, WIDGET_MAX_WIDTH-BLOCK_WIDTH*2)
        self.yPos = random.randrange(0, WIDGET_MAX_HEIGHT-BLOCK_HEIGHT*2)
        self.selected = RELEASED
        self.numInputs = numInputs
        self.numOutputs = numOutputs
        self.numParams = numParams
        self.lines = []
        self.inputs = []
        self.outputs = []
        self.params = []
        self.isFungible = isFungible
        
        with self.canvas:     
            Color(0.0,0.0,0.0,OPAQUE, mode="rgba")
            self.border = Rectangle(pos=(self.xPos,self.yPos), size=(BLOCK_WIDTH,BLOCK_HEIGHT))
            Color(1.0,1.0,1.0,OPAQUE, mode="rgba")
            self.fill = Rectangle(pos=(self.xPos+BLOCK_BORDER/2,self.yPos+BLOCK_BORDER/2), size=(BLOCK_WIDTH-BLOCK_BORDER, BLOCK_HEIGHT-BLOCK_BORDER))
            if self.isFungible: # dont need to show the user which instation of the block it is
                self.label = Label(pos=(self.xPos+LABEL_X_OFFSET, self.yPos + LABEL_Y_OFFSET),text=self.name.split(' ', 1)[0],color=(0,0,0,OPAQUE))
            else:
                self.label = Label(pos=(self.xPos+LABEL_X_OFFSET, self.yPos + LABEL_Y_OFFSET),text=self.name,color=(0,0,0,OPAQUE))

            Color(0.0,0.0,1.0,OPAQUE, mode="rgba")
            if self.numInputs == 1:
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            elif self.numInputs == 2:
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/3), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
                self.inputs.append(Rectangle(pos=(self.xPos,self.yPos+BLOCK_HEIGHT/3*2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
            
            Color(0.0,0.0,1.0,OPAQUE, mode="rgba")
            if self.numOutputs == 1:
                self.outputs.append(Rectangle(pos=(self.xPos+BLOCK_WIDTH-CONNECTOR_WIDTH,self.yPos+BLOCK_HEIGHT/2), size=(CONNECTOR_WIDTH,CONNECTOR_HEIGHT)))
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

    def extract_after_substring(self, main_string, substring):
        """
        Finds a substring in the main string and returns characters between
        the first and second space after the substring.
        
        Args:
        main_string (str): The full string to search in
        substring (str): The substring to locate
        
        Returns:
        str: Characters between first and second space after substring, 
            or an empty string if conditions are not met
        """
        # Find the index of the substring
        substr_index = main_string.find(substring)
        
        # If substring is not found, return empty string
        if substr_index == -1:
            return ""
        
        # Find the first space after the substring
        first_space = main_string.find(" ", substr_index + len(substring))
        
        # If no first space found, return empty string
        if first_space == -1:
            return ""
        
        # Find the second space
        second_space = main_string.find(" ", first_space + 1)
        
        # If no second space found, return from first space to end of string
        if second_space == -1:
            return main_string[first_space + 1:]
        
        # Return the substring between the two spaces
        return main_string[first_space + 1:second_space]


    def get_connector_name(self,connector):
        if connector == INPUT_ID + 1:
            return 'Input 1'
        if connector == INPUT_ID + 2:
            return 'Input 2'
        if connector == OUTPUT_ID + 1:
            return 'Output 1'
        if connector == OUTPUT_ID + 2:
            return 'Output 2'
        if connector == PARAM_INPUT_ID + 1:
            return 'Param 1'
        if connector == PARAM_INPUT_ID + 2:
            return 'Param 2'
        if connector == PARAM_INPUT_ID + 3:
            return 'Param 3'
        if connector == PARAM_INPUT_ID + 4:
            return 'Param 4'
        if connector == PARAM_INPUT_ID + 5:
            return 'Param 5'
        if connector == PARAM_INPUT_ID + 6:
            return 'Param 6'
        
        return "Todo"
        
    def remove_block(self):
        with self.canvas:
            self.canvas.remove(self.border)
            self.canvas.remove(self.fill)
            self.label.text = ""
            for i in range(0,self.numInputs):
                self.canvas.remove(self.inputs[i])
            for i in range(0,self.numOutputs):
                self.canvas.remove(self.outputs[i])
            for i in range(0,self.numParams):
                self.canvas.remove(self.params[i])
            self.canvas.ask_update()

    def move_block(self,touch):
        if self.selected == SELECTED:
            if touch.pos[X] > WINDOW_EDGE_MARGIN:
                if touch.pos[X] + self.border.size[X] + WINDOW_EDGE_MARGIN < WIDGET_MAX_WIDTH:
                    if touch.pos[Y] > WINDOW_EDGE_MARGIN:
                        if touch.pos[Y] + self.border.size[Y] + WINDOW_EDGE_MARGIN < WIDGET_MAX_HEIGHT - BUTTON_HEIGHT:
                            # if len(blocks) == 1:#if only this block is in the list - move block                    
                            self.border.pos = touch.pos
                            self.fill.pos = (touch.pos[X]+BLOCK_BORDER/2,touch.pos[Y]+BLOCK_BORDER/2)
                            self.label.pos = (touch.pos[X]+LABEL_X_OFFSET, touch.pos[Y]+LABEL_Y_OFFSET)
                            self.move_connectors(touch)
                            
                            for line in self.lines:
                                print(line.name)
                                if self.name in line.name:
                                    print("Match " + self.name)
                                    new_line_pos = None
                                    connector = self.extract_after_substring(line.name,self.name)
                                    print ("Connector " + connector)
                                    connector = int(connector)
                                    if connector == INPUT_ID + 1:
                                        new_line_pos = list(self.inputs[0].pos)
                                    if connector == INPUT_ID + 2:
                                        new_line_pos = list(self.inputs[1].pos)
                                    if connector == OUTPUT_ID + 1:
                                        new_line_pos = list(self.outputs[0].pos)
                                    if connector == OUTPUT_ID + 2:
                                        new_line_pos = list(self.outputs[1].pos)
                                    if connector == PARAM_INPUT_ID + 1:
                                        new_line_pos = list(self.param[0].pos)
                                    if connector == PARAM_INPUT_ID + 2:
                                        new_line_pos = list(self.param[1].pos)
                                    if connector == PARAM_INPUT_ID + 3:
                                        new_line_pos = list(self.param[2].pos)
                                    if connector == PARAM_INPUT_ID + 4:
                                        new_line_pos = list(self.param[3].pos)
                                    if connector == PARAM_INPUT_ID + 5:
                                        new_line_pos = list(self.param[4].pos)
                                    if connector == PARAM_INPUT_ID + 6:
                                        new_line_pos = list(self.param[5].pos)
                                    
                                    if new_line_pos != None:
                                        print(new_line_pos)
                                        new_line_pos[X] += CONNECTOR_WIDTH / 2
                                        new_line_pos[Y] += CONNECTOR_HEIGHT / 2
                                        line.move_line(new_line_pos)

    def release_block(self):
        self.selected = RELEASED 

    def is_touch_detected(self,touch,moving):
        if touch.pos[X] > self.border.pos[X] and touch.pos[X] < (self.border.pos[X] + self.border.size[X]):
            if touch.pos[Y] > self.border.pos[Y] and touch.pos[Y] < (self.border.pos[Y] + self.border.size[Y]):
                if moving == STILL:
                    self.selected = SELECTED
                    self.is_inside_connector(touch,ASSIGN_LINE) #assign a line if inside a connector
                    return 1 
        return 0                          

    def assign_line(self,touch, start_connector):
        with self.canvas:
            line = MyLine(touch,self,start_connector)
            self.lines.append(line)

    def move_lines(self,touch):
        pass
        # for line in self.lines: # move connected lines
            # if line.start_block.name == self.name:
            #     if line.start_connector == INPUT:
            #         line.move_line(temp[X]+CONNECTOR_WIDTH/2,temp[Y]+CONNECTOR_HEIGHT/2) 
            # elif line.end_block.name == self.name:
            #     if line.end_connector == INPUT:
            #         line.move_line(temp[X]+CONNECTOR_WIDTH/2,temp[Y]+CONNECTOR_HEIGHT/2)
   
    def move_connectors(self,touch):
            if self.numInputs == 1:
                temp = list(self.inputs[0].pos)
                temp[X] = touch.pos[X]
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/2
                self.inputs[0].pos = tuple(temp)

            elif self.numInputs == 2:
                temp = list(self.inputs[0].pos)
                temp[X] = touch.pos[X]
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3
                self.inputs[0].pos = tuple(temp)

                temp = list(self.inputs[1].pos)
                temp[X] = touch.pos[X]
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3*2
                self.inputs[1].pos = tuple(temp)

            if self.numOutputs == 1:
                temp = list(self.outputs[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH-CONNECTOR_WIDTH
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/2
                self.outputs[0].pos = tuple(temp)

            elif self.numOutputs == 2:
                temp = list(self.outputs[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH-CONNECTOR_WIDTH
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3
                self.outputs[0].pos = tuple(temp)

                temp = list(self.outputs[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH-CONNECTOR_WIDTH
                temp[Y] = touch.pos[Y] + BLOCK_HEIGHT/3*2
                self.outputs[1].pos = tuple(temp)
            
            if self.numParams == 1:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

            elif self.numParams == 2:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/3-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

                temp = list(self.params[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/3*2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[1].pos = tuple(temp)
            
            elif self.numParams == 3:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/4-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

                temp = list(self.params[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[1].pos = tuple(temp)

                temp = list(self.params[2].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/4*3-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[2].pos = tuple(temp)
            
            elif self.numParams == 4:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/5-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

                temp = list(self.params[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/5*2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[1].pos = tuple(temp)

                temp = list(self.params[2].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/5*3-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[2].pos = tuple(temp)

                temp = list(self.params[3].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/5*4-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[3].pos = tuple(temp)
            
            elif self.numParams == 5:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/6-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

                temp = list(self.params[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/6*2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[1].pos = tuple(temp)

                temp = list(self.params[2].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/6*3-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[2].pos = tuple(temp)

                temp = list(self.params[3].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/6*4-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[3].pos = tuple(temp)

                temp = list(self.params[4].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/6*5-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[4].pos = tuple(temp)

            elif self.numParams == 6:
                temp = list(self.params[0].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[0].pos = tuple(temp)

                temp = list(self.params[1].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7*2-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[1].pos = tuple(temp)

                temp = list(self.params[2].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7*3-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[2].pos = tuple(temp)

                temp = list(self.params[3].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7*4-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[3].pos = tuple(temp)

                temp = list(self.params[4].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7*5-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[4].pos = tuple(temp)

                temp = list(self.params[5].pos)
                temp[X] = touch.pos[X] + BLOCK_WIDTH/7*6-CONNECTOR_WIDTH/2
                temp[Y] = touch.pos[Y]
                self.params[5].pos = tuple(temp)

    def is_inside_connector(self,touch,allow_assign_line):
        insideConnector = False
        for i in range(0, self.numInputs):
            if touch.pos[X] > self.inputs[i].pos[X] and touch.pos[X] < (self.inputs[i].pos[X] + self.inputs[i].size[X]):
                if touch.pos[Y] > self.inputs[i].pos[Y] and touch.pos[Y] < (self.inputs[i].pos[Y] + self.inputs[i].size[Y]):
                    insideConnector = INPUT_ID + i + 1

        for i in range(0, self.numOutputs):
            if touch.pos[X] > self.outputs[i].pos[X] and touch.pos[X] < (self.outputs[i].pos[X] + self.outputs[i].size[X]):
                if touch.pos[Y] > self.outputs[i].pos[Y] and touch.pos[Y] < (self.outputs[i].pos[Y] + self.outputs[i].size[Y]):
                    insideConnector = OUTPUT_ID + i + 1

        for i in range(0, self.numParams):
            if touch.pos[X] > self.params[i].pos[X] and touch.pos[X] < (self.params[i].pos[X] + self.params[i].size[X]):
                if touch.pos[Y] > self.params[i].pos[Y] and touch.pos[Y] < (self.params[i].pos[Y] + self.params[i].size[Y]):
                    insideConnector = PARAM_INPUT_ID + i + 1

        if insideConnector != False:
            self.selected = RELEASED
            if allow_assign_line:
                if self.lines != []:
                    for line in self.lines:
                        if line.start_block.name == self.name: # line starts in this block
                            if line.start_connector == insideConnector: #dont assign a new line if there is one on this connector   
                                allow_assign_line = DONT_ASSIGN_LINE
                                break
                        elif line.end_block.name == self.name: # line ends in this block
                            if line.end_connector == insideConnector: #dont assign a new line if there is one on this connector   
                                allow_assign_line = DONT_ASSIGN_LINE
                                break
                    if allow_assign_line:
                        self.assign_line(touch,insideConnector)                  
                else: # assign a line as there are none connected to this block
                    self.assign_line(touch,insideConnector)
        return insideConnector