
from Model import *
from View import *


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()  # View.py failis olev meetod

    def protsessi(self):
        self.model.get_weather_data(self.view.userinput.get().strip())

        self.view.char_input.delete(0, 'end')
        self.view.lable.configure(text=self.model.vastus)
