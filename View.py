
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class View(Tk):

    def __init__(self, controller):
        super().__init__()  # Tk jaoks

        # Mõned muutujad
        self.controller = controller
        self.userinput = StringVar()

        # Värvid

        # Fondid
        self.bigFontStyle = tkFont.Font(
            family='Courier', size=12, weight='bold')        # suur tekst
        self.defaultStyle = tkFont.Font(family='Vendara', size=10)  # Tavaline
        self.defaultStyleBold = tkFont.Font(
            family='Vendara', size=10, weight='bold')

        # Põhiaken
        self.geometry('450x200')  # akna suurus
        self.resizable(True, True)  # akna suurust saab muuta
        self.title('Ilmaapp')

        # Framed
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        # vidinad
        # self.create_popup_button()
        self.button = self.loo_protsessi_nupp()  # uue mängu nupp
        self.char_input, self.label_error = self.loo_teised_nupud()
        self.lable = self.create_result_label()

        #######################################################################

    def main(self):
        self.mainloop()

    # Framede tegemine
    def create_top_frame(self):
        frame = Frame(self, bg='lightgray', height=50)
        frame.pack(expand=True, fill='both')
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='lightgray')
        frame.pack(expand=True, fill='both')
        return frame

        # Nupud ja sildid

    def loo_protsessi_nupp(self):
        button = Button(self.top_frame, text='Protsessi',
                        font=self.defaultStyle, command=lambda: self.controller.protsessi())
        button.grid(row=1, column=0, padx=5, pady=5, sticky=EW)
        return button

    def loo_teised_nupud(self):

        char_input = Entry(self.top_frame, textvariable=self.userinput, justify='center',
                           font=self.defaultStyle)
        char_input.grid(row=1, column=2, padx=5, pady=5)
        char_input.focus()  # aktiivne koht

        label_error = Label(
            self.top_frame, text='Küsi ilmaandmeid, sisesta linna nimi lahtrisse.', anchor='w', font=self.defaultStyleBold)
        label_error.grid(row=0, column=0, columnspan=3,
                         sticky=EW, padx=5, pady=5)

        return char_input, label_error

    def create_result_label(self):

        label = Label(self.bottom_frame, text='Tulemus',
                      font=self.bigFontStyle)
        label.pack(padx=5, pady=5)
        return label
