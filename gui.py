#!/usr/bin/env python
# encoding: utf-8

import npyscreen
import random
import time
import socketio

class GridForm(npyscreen.Form):
    # You need to override custom_print_cell to manipulate how
    # a cell is printed. In this example we change the color of the
    # text depending on the string value of cell.
    def while_waiting(self):
        npyscreen.notify_wait("Update")
        self.grid.values = self.updateGrid()
        self.display()
    def create(self):
        self.grid = self.add(npyscreen.GridColTitles, values=self.updateGrid(), editable=False)

    def updateGrid(self):
        self.nums = []
        for x in range(2):
            row = []
            for y in range(4):
                if bool(random.getrandbits(1)):
                    row.append("PASS")
                else:
                    row.append("FAIL")
            self.nums.append(row)
        return self.nums

    # def custom_print_cell(self, actual_cell, cell_display_value):
    #     if cell_display_value =='FAIL':
    #        actual_cell.color = 'DANGER'
    #     elif cell_display_value == 'PASS':
    #        actual_cell.color = 'GOOD'
    #     else:
    #        actual_cell.color = 'DEFAULT'

class TestApp(npyscreen.NPSAppManaged):

    keypress_timeout_default = 50

    def onStart(self):
        self.addForm("MAIN", GridForm, name="Colby Shuttle Bot Admin GUI")

if __name__ == "__main__":
    App = TestApp()
    App.run()
