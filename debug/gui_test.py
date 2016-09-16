from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='start craw', command=self.craw)
        self.alertButton.pack()

    def craw(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'crawing, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('web spider')
# 主消息循环:
app.mainloop()