# ui of the program
import tkinter as tk 
import ttkbootstrap as ttkb  


class Appn(ttkb.Window):
	def __init__(self,title,size):
		super().__init__(themename='minty')
		# print(title)
		self.title(title)
		# self.style = Style('journal')s
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])


		#diff frame
		self.head=Header(self)
		self.whearS

		# btn_1=ttkb.Button(self,text='btn1',bootstyle='primary')
		# btn_1.pack()


		self.mainloop()
class Header(ttkb.Frame):
	def __init__(self,parent):
		super().__init__(parent,style='info') #style='info'
		self.place(relx = 0.0, rely = 0.0, 
			relwidth = 1, relheight = 0.15)
		self.create_title()

	def create_title(self):
		lab1=ttkb.Label(self,text='Weather app', font=('JetBrains Mono NL', 20),style='info')
		lab1.pack(side='left',expand=True,fill='both',padx=10,pady=10)






Appn("ok gg",(600,600))


