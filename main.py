from tkinter import *

def main():

    def calculate():

        fro = fromentvar.get()

        ans = (fro * 0.0831320833) / 3.1419999987

        toentvar.set(ans)
        resultslb.config(text=("Results : {} pixel  = {} {}".format(fromentvar.get(), toentvar.get(), label4var.get())))

    def Menubar():

        global menubar

        menubar = Menu(mainWindow)

        filemenu = Menu()
        filemenu.add_command(label='Save')

        dev = Menu()
        dev.add_command(label="Antony Alen")

        helpmenu = Menu()
        helpmenu.add_cascade(label='Developer', menu=dev)

        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_cascade(label='Help', menu=helpmenu)


    mainWindow = Tk()

    Menubar()

    # tkinter Variables

    label4var = StringVar()
    label4var.set("Centimeters")
    fromentvar = DoubleVar()
    fromentvar.set(0)
    toentvar = DoubleVar()
    toentvar.set(0)

    # tkinter widgets
    fromlb = Label(mainWindow, text='From :', font='helvetica 12')
    tolb = Label(mainWindow, text=' To :', font='helvetica 12')
    froment = Entry(mainWindow, width=20, font='helvetica 12', textvariable=fromentvar)
    toent = Entry(mainWindow, width=20, font='helvetica 12', textvariable=toentvar)
    fromunits = Label(mainWindow, text="pixels ", font='helvetica 12')
    tounits = Label(mainWindow, textvariable=label4var, font='helvetica 12')
    convertbut = Button(mainWindow, text=" CONVERT ", font='helvetica 12', command=calculate)
    clearbut = Button(mainWindow, text='  CLEAR  ', font='helvetica 12')
    resultslb = Label(mainWindow, text=("Results : {} pixel  = {} {}".format(fromentvar.get(), toentvar.get(), label4var.get())),
                      font='helvetica 12 bold')


    # packing the widgets
    fromlb.grid(row=1, column=1, padx=10, pady=20)
    froment.grid(row=1, column=2, padx=10, pady=20)
    fromunits.grid(row=1, column=3, padx=10, pady=20)
    tolb.grid(row=2, column=1)
    toent.grid(row=2, column=2)
    tounits.grid(row=2, column=3)
    convertbut.grid(row=3, column=1, padx=20, pady=20)
    clearbut.grid(row=3, column=2, padx=20, pady=20)
    resultslb.grid(row=4, column=1, columnspan=4)


    mainWindow.config(bg='white', menu=menubar)
    mainWindow.title("  Pixcel Unit Converter  ")
    mainWindow.geometry("450x200")
    mainWindow.mainloop()


if __name__ == '__main__':
    main()

