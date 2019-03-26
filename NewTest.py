from tkinter import *
from dialogwindow import Dialog


class NumAttemptsDialog(Dialog):
    def body(self, master):
        row =0

        self.attempts_entry = Entry(self)
        self.attempts_label = Label(self, text="The number of attempts allowed")

        self.attempts_label.grid(row=row, column=0)
        self.attempts_entry.grid(row=row, column=1)


class NewMCQ(Dialog):

    def body(self, master):
        Label(master, text="First:").grid(row=0)
        Label(master, text="Second:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1  # initial focus

    def apply(self):
        first = int(self.e1.get())
        second = int(self.e2.get())

class TestForm(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master)
        self.init_window()
        self.title = StringVar()
        self.dueDate = StringVar()
        self.releaseDate = StringVar()
        self.testType = StringVar()

        self.testType.set(None)

        row = 0
        Label(self, text="Title").grid(row=row, column=0)
        Entry(self, textvariable=self.title).grid(row=row, column=1)

        row +=1
        Radiobutton(self, text="Formative", command=self.on_checked, value="f",
                    variable=self.testType).grid(row=row, column=0)
        Radiobutton(self, text="Summative", command=self.on_checked, value="s",
                    variable=self.testType).grid(row=row, column=1)

        row += 1
        Label(self, text="Due Date").grid(row=row, column=0)
        Entry(self, textvariable=self.dueDate).grid(row=row, column=1)

        row += 1
        Label(self, text="Release Date").grid(row=row, column=0)
        Entry(self, textvariable=self.releaseDate).grid(row=row, column=1)

        row += 1
        Button(self, text="New multiple choice", command=self.multiple_choice).grid(row=row, column=0)
        Button(self, text="New text answer", command=self.text_answer).grid(row=row, column=0)

        row += 1
        self.submit = Button(self, text="Submit")
        self.submit.grid(row=row, column=0)


    def multiple_choice(self):
        print("Multiple")
        mcq = NewMCQ(self)
        print("MCQ dialog closed")

    def text_answer(self):
        print("text")

    def on_checked(self):
        self.num_attempts = 1
        if(self.testType.get() == 'f'):
            d = NumAttemptsDialog(self.master)
            print("Number of attemptes". d.attempts_entry.get())

    def init_window(self):
        self.master.title("Main Menu")
        self.pack(fill=NONE, expand=True)



def main():

    root = Tk()
    root.geometry("800x450")
    app = TestForm(root)
    root.mainloop()



if __name__ == '__main__':
    main()
