import os
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.slider import Slider

from click_class import Click
from config import *


class popUpParamLabel(Widget):
    def __init__(self,**kwargs):
        super(popUpParamLabel, self).__init__(**kwargs)
        with self.canvas:
            self.paramlabel = Label(pos=(0, 0),text="")
        self.released = 1

    def destroy_label(self):
        with self.canvas:
            self.paramlabel.text =""
            self.released = 1

    def update_label(self,mousepos,name):
        with self.canvas:
            if self.released == 1:
                self.paramlabel.pos=(mousepos[X]-50, mousepos[Y]+40)
                self.paramlabel.text=name
                self.released = 0


class myMousePos():
    def __init__(self):
        self.pos = [0,0]


class DSPDesignerApp(App):
    def build(self):        
        #self.isOverlay = 0
        Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        Window.bind(mouse_pos=self.on_mouse_pos)
        Window.bind(on_key_down=self.key_action)   

        self.popUpLabel = popUpParamLabel()
        self.click = Click() 
        self.layout = GridLayout(cols = NUM_COLUMNS, row_force_default = True, row_default_height = BUTTON_HEIGHT)

        #--------------------------------IOdrop
        IOdrop = DropDown()
        
        inBtn = Button(text ='Input', size_hint_y = None, height = BUTTON_HEIGHT)
        inBtn.bind(on_release = lambda none: self.click.assign_block('Input',NO_INPUTS,ONE_OUTPUT,NO_PARAMETERS))
        IOdrop.add_widget(inBtn)
        
        outBtn = Button(text ='Output', size_hint_y = None, height = BUTTON_HEIGHT)
        outBtn.bind(on_release = lambda none: self.click.assign_block('Output', ONE_INPUT,NO_OUTPUTS,NO_PARAMETERS))
        IOdrop.add_widget(outBtn)            
        #--------------------------------Operations
        OpsDrop = DropDown()

        test1Btn = Button(text ='test 1 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test1Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,ONE_PARAMETER))
        OpsDrop.add_widget(test1Btn)

        test2Btn = Button(text ='test 2 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test2Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,TWO_PARAMETERS))
        OpsDrop.add_widget(test2Btn)

        test3Btn = Button(text ='test 3 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test3Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,THREE_PARAMETERS))
        OpsDrop.add_widget(test3Btn)

        test4Btn = Button(text ='test 4 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test4Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,FOUR_PARAMETERS))
        OpsDrop.add_widget(test4Btn)

        test5Btn = Button(text ='test 5 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test5Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,FIVE_PARAMETERS))
        OpsDrop.add_widget(test5Btn)

        test6Btn = Button(text ='test 6 param', size_hint_y = None, height = BUTTON_HEIGHT)
        test6Btn.bind(on_release = lambda none: self.click.assign_block('Output', TWO_INPUTS,TWO_OUTPUTS,SIX_PARAMETERS))
        OpsDrop.add_widget(test6Btn)
        # addBtn = Button(text ='Add', size_hint_y = None, height = BUTTON_HEIGHT)
        # addBtn.bind(on_release = lambda none: self.click.assign_block('Add',TWO_INPUTS,ONE_OUTPUT))
        # OpsDrop.add_widget(addBtn)

        # subBtn = Button(text ='Subtract', size_hint_y = None, height = BUTTON_HEIGHT)
        # subBtn.bind(on_release = lambda none: self.click.assign_block('Subtract',TWO_INPUTS,ONE_OUTPUT))
        # OpsDrop.add_widget(subBtn)

        # multBtn = Button(text ='Multiply', size_hint_y = None, height = BUTTON_HEIGHT)
        # multBtn.bind(on_release = lambda none: self.click.assign_block('Multiply',TWO_INPUTS,ONE_OUTPUT))
        # OpsDrop.add_widget(multBtn)

        # divBtn = Button(text ='Divide', size_hint_y = None, height = BUTTON_HEIGHT)
        # divBtn.bind(on_release = lambda none: self.click.assign_block('Divide',TWO_INPUTS,ONE_OUTPUT))
        # OpsDrop.add_widget(divBtn)
        
    
        #--------------------------------Routing
        RoutingDrop = DropDown()
        
        # Splitter
        # splitterBtn = Button(text ='Splitter', size_hint_y = None, height = BUTTON_HEIGHT)
        # splitterBtn.bind(on_release = lambda none: self.click.assign_block('Splitter',1))
        # RoutingDrop.add_widget(splitterBtn)
            #--------------------------------Controls Drop
        ControlsDrop = DropDown()

        # ConstantBtn = Button(text ='Constant', size_hint_y = None, height = BUTTON_HEIGHT)
        # ConstantBtn.bind(on_release = lambda  none: self.click.assign_block('Constant'))
        # ControlsDrop.add_widget(ConstantBtn)
        # 

        #-------------------------------- Buttons For Dropdowns
        IObutton = Button(text ='IO')
        IObutton.bind(on_release = IOdrop.open)

        OpsButton = Button(text ='Ops')
        OpsButton.bind(on_release = OpsDrop.open)

        RoutingButton = Button(text ='Routing')
        RoutingButton.bind(on_release = RoutingDrop.open)

        ControlsButton = Button(text ='Controls')
        ControlsButton.bind(on_release = ControlsDrop.open)

        #--------------------------------
        CodeButton = Button(text ='Generate Code')
        CodeButton.bind(on_release =  lambda none: self.generateCode())

        #--------------------------------
        ClearButton = Button(text ='Clear Screen')
        ClearButton.bind(on_release = lambda none: self.clear_screen())


        #---------------------------------------------
        self.layout.add_widget(IObutton)
        self.layout.add_widget(OpsButton)
        self.layout.add_widget(ControlsButton)
        self.layout.add_widget(RoutingButton)
        self.layout.add_widget(CodeButton)
        self.layout.add_widget(ClearButton)
        self.layout.add_widget(self.popUpLabel)
        self.layout.add_widget(self.click)

        return self.layout

    def key_action(self, *args):
        global blocks
        # print("got a key event: %s" % list(args))
        if args[3] == 'd':
            for block in blocks:
                    if block.selected == 1:
                        block.remove_block()# remove block/connector graphics
                        for line in block.lines:
                            line.remove_line()
                            block.lines.remove(line)
                        for block2 in blocks:
                            for line in block2.lines:
                                if line.start_block.name == block.name:
                                    line.remove_line()
                                    block2.lines.remove(line)
                                elif line.end_block.name == block.name:
                                    line.remove_line()
                                    block2.lines.remove(line)
                        blocks.remove(block)
                    else:
                        for line in block.lines: # search for dragging lines
                            if line.dragging == DRAGGING:
                                line.dragging = NOT_DRAGGING
                                block.lines.remove(line)
                                line.remove_line()
        if args[3] == 'c':
            self.change_constant()    

    def change_constant(self):
        if self.hover == 1:

            box = BoxLayout(orientation = 'vertical', padding = (10))
            btn1 = Button(text = "Save") 
            btn2 = Button(text = "Exit")  
            slider = Slider(min=0, max=1, value=0.5)
            box.add_widget(slider)
            box.add_widget(btn1)
            box.add_widget(btn2)
            popup = Popup(title="Change Constant Value", title_size= (30), 
                    title_align = 'center', content = box,
                    size_hint=(None, None), size=(400, 400),
                    auto_dismiss = True)
            btn1.bind(on_press = lambda none : self.change_constant2(slider.value)) 
            btn2.bind(on_press = popup.dismiss) 
            popup.open()

    def change_constant2(self,val):
        for block in blocks:
            if block.name == self.block_latch:
                block.constant = round(val,2)
        self.block_latch = None  

    def on_mouse_pos(self, window, mousepos):
        myPos = myMousePos() 
        
        if blocks != []:
            for block in blocks:
                if block.selected == RELEASED:
                    myPos.pos[X] = mousepos[0]
                    myPos.pos[Y] = mousepos[1]
                    readConnector = block.is_inside_connector(myPos,DONT_ASSIGN_LINE)
                    # print("readConnector",readConnector) 
                    if readConnector != FALSE:
                        if "Constant" in block.name:
                            self.block_latch = block.name
                            self.hover = TRUE
                            self.popUpLabel.update_label(mousepos,str(block.constant))
                            return
                        self.popUpLabel.update_label(mousepos,block.get_connector_name(readConnector))
                        return
                    else:
                        self.hover = FALSE
                        self.popUpLabel.destroy_label()

                if block.lines != []:
                    for conLine in block.lines:
                        if conLine.dragging == DRAGGING: # when first dragging the line keep hold of it until clicked in block or deleted
                            conLine.drag_line(mousepos,DRAG_MODE1)

    def clear_screen(self):
        box = BoxLayout(orientation = 'vertical', padding = (10))
        btn1 = Button(text = "No")
        btn2 = Button(text = "Yes")
        box.add_widget(btn1)
        box.add_widget(btn2)
        popup = Popup(title="Clear Screen? Can't Undo!", title_size= (30), 
                title_align = 'center', content = box,
                size_hint=(None, None), size=(400, 400),
                auto_dismiss = True)
        btn1.bind(on_press = popup.dismiss)
        btn2.bind(on_press = lambda none:self.clear_screen2(popup))
        popup.open()

    def clear_screen2(self,popup):       
        global blocks
        blocks = []
        self.layout.remove_widget(self.click)
        self.click = Click()
        self.layout.add_widget(self.click)
        popup.dismiss()

        # above method is not working as there is still collision but method commented below doesnt delete all the graphics
        # global blocks
        #     for block in blocks:              
        #         block.remove_block( )# remove block/connector graphics
        #         for line in block.lines:
        #             line.remove_line()
        #             block.lines.remove(line)
        #         blocks.remove(block)            
        #     popup.dismiss()

    # def error_trap(self,error):
    #     box = BoxLayout(orientation = 'vertical', padding = (10))
    #     btn1 = Button(text = "OK")   
    #     box.add_widget(btn1)
    #     if error == "out of reg":
    #         popup = Popup(title="Too many registers used. Try using less mixers and splitters.", title_size= (30), 
    #                 title_align = 'center', content = box,
    #                 size_hint=(None, None), size=(400, 400),
    #                 auto_dismiss = True)
    #     btn1.bind(on_press = popup.dismiss) 
    #     popup.open()
    
    def generateCode():
        pass

if __name__ == '__main__':
    DSPDesignerApp().run()