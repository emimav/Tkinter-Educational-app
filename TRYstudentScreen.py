from tkinter import *


class Window(Frame):
    '''
    The top level window
    '''
    def __init__(self, master=None):

        super().__init__(master=None)

        self.studentFrame = StudentFrame(self)
        self.studentFrame.grid(row=0, column=1, columnspan=2)

        #self.newTestFrame = TestForm(self)

        Button(self, text="AAA").grid(row=2, column=0, columnspan=2)
        logoutButton = Button(self, text="Log Out")
        logoutButton.grid(row=1, column=0)

        self.init_window()
    def new_test(self):
        self.studentFrame.grid_forget()
        self.newTestFrame.grid(row=0, column=0, columnspan=2)

    def init_window(self):
        self.master.title("Main Menu")



class StudentFrame(Frame):
    def __init__(self,master=None, **kwargs):
        super().__init__(**kwargs)

        self.table = Frame(self, bg="black")
        self.master = master

        self.rows = 0;

        self.table.grid(row=0, column=1, columnspan=2)

        with open("Test File Example.csv") as f:
            self.columns = next(f, None).split(",")

            for i, column in enumerate(self.columns):
                lb = Label(self.table, text=column)
                lb.grid(row=0, column=i, sticky=W)

            for i, line in enumerate(f):
                parts = line.split(",")
                for j, val in enumerate(parts):
                    Label(self.table, text=val,
                          bg="white", bd=3).grid(row=i+1, column=j, padx=1)

                button = Button(self.table, text="Take Test", command=lambda x=i: self.take_test(x))
                button.grid(row=i+1, column=j+1)

                button = Button(self.table, text="View Test", command=lambda x=i: self.view_test(x))
                button.grid(row=i + 1, column=j + 2)

            self.rows = i + 1

    def take_test(self, x):
        print("take the tet for row ", x)


    def view_test(self, x):
        print("View test", x)


class TestForm(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        Label(self, text="hello").grid(row=0, column=0)


def main():
    root = Tk()
    root.geometry("800x450")
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()