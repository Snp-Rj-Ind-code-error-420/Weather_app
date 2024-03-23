# ui of the program
import tkinter as tk 
import ttkbootstrap as ttkb  


class Appn(ttkb.Window):
	def __init__(self,title,size):
		super().__init__(themename='pulse')
		# print(title)
		self.title(title)
		# self.style = Style('journal')s
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])


		#diff frame
		self.head=Header(self)
		self.search=Search_frm(self)

		# btn_1=ttkb.Button(self,text='btn1',bootstyle='primary')
		# btn_1.pack()


		self.mainloop()
class Header(ttkb.Frame):
	def __init__(self,parent):
		super().__init__(parent,style='primary') #style='info'
		self.place(relx = 0.0, rely = 0.0, 
			relwidth = 1, relheight = 0.15)
		self.create_title()

	def create_title(self):
		lab1=ttkb.Label(self,text='Weather app', font=('JetBrains Mono NL', 20),style='info')
		lab1.pack(side='left',expand=True,fill='both',padx=10,pady=10)

class Search_frm(ttkb.Frame):
	def __init__(self,parent):
		super().__init__(parent,style='danger')
		self.place(relx = 0.0, rely = 0.15, 
			relwidth = 1, relheight = 0.15)
		self.widgit()

	def prnt(self):
		print(self.input_city.get())
	def widgit(self):
		self.input_city = tk.StringVar()
		self.columnconfigure((0,1,2),weight=1,uniform='a')
		self.rowconfigure(0,weight=1,uniform='a')
		entry1=ttkb.Entry(self,style='primary',textvariable=self.input_city,width=10 )
		# entry1.insert('enter the city')
		btn1=ttkb.Button(self,text='search',style='secondary',command=self.prnt)
		entry1.grid(row=0,column=0,sticky='nsew',columnspan=2,padx = 20, pady = 10)
		btn1.grid(row=0,column=2,sticky='nsew',padx = 20, pady = 10)









Appn("Weather App",(600,400))


