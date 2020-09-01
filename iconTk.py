from tkinter import *
from PIL import ImageTk, Image
import os

class Application(Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_image()

	def create_image(self):
		self.img = PhotoImage(file = '/home/neko/Pictures/.Mãe de Deus.png')
		self.img = self.img.subsample(2,2)
		self.panel = Label(root, image = self.img)
		self.panel.bind('<Button-1>', self.on_click)
		self.panel.pack()
		self.pos = 1

	def on_click(self, event=None):
		if self.pos == 1:
			root.geometry('253x350+3033+694')
			self.pos = 2
		elif self.pos == 2:
			root.geometry('253x350+0+1082')
			self.pos = 3
		else:
			root.geometry('253x350+1366+694')
			self.pos = 1

root = Tk()
app = Application(master = root)
root.geometry('253x350+1366+694')
root.overrideredirect(1)
root.title("Mais venerável")
root.resizable(0,0)
app.mainloop()

