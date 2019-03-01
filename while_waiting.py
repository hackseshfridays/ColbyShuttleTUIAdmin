import npyscreen
from datetime import datetime

class DateForm(npyscreen.Form):
    def while_waiting(self):
        npyscreen.notify_wait("Update")
        self.display()

    def create(self):
        self.add(npyscreen.FixedText, value=datetime.now(), editable=False)

class DateApp(npyscreen.NPSAppManaged):

    keypress_timeout_default = 50

    def onStart(self):
        self.addForm("MAIN", DateForm, name="Time")

if __name__ == '__main__':
    app = DateApp()
    app.run()
