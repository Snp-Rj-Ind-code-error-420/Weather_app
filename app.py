# ui of the program
from PIL import Image, ImageTk
import tkinter as tk 
import ttkbootstrap as ttkb  
import json,time


data=json.loads('{"coord":{"lon":86.1833,"lat":22.8},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":31.9,"feels_like":31.64,"temp_min":31.9,"temp_max":31.9,"pressure":1013,"humidity":37},"visibility":3000,"wind":{"speed":1.54,"deg":270},"clouds":{"all":20},"dt":1711258148,"sys":{"type":1,"id":9121,"country":"IN","sunrise":1711239320,"sunset":1711283254},"timezone":19800,"id":1269300,"name":"Jamshedpur","cod":200}')




def prn():
	#Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
	print(f'temperature {data['main']['temp']}')

	print(f'temperature relative to human {data['main']['feels_like']}')
	print(f'minimum temperature {data['main']['temp_min']}')
	print(f'maximum temperature {data['main']['temp_max']}')
	print()
	print(f'pressure {data['main']['pressure']}') # hPa
	print(f'humidity % {data['main']['humidity']}') # %
	print()
	print(f'visibility {data['visibility']}') # meters /1000 to km
	print()
	#Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
	print(f'wind speed {data['wind']['speed']}')
	print()
	print(f'cloud % {data['clouds']['all']}%') # %
	print()
	x=time.localtime(data['dt'])
	print(f'date = {data['dt']} {time.localtime(data['dt'])}\n {x[2]}/{x[1]}/{x[0]} {x[3]}:{x[4]}:{x[5]} ')
	x=time.gmtime(data['dt'])
	print(f'date = {data['dt']} {time.gmtime(data['dt'])}\n {x[2]}/{x[1]}/{x[0]} {x[3]}:{x[4]}:{x[5]} ')



class Appn(ttkb.Window):
	def __init__(self,title,size,*args, **kwargs):
		super().__init__(themename='pulse')
		# global degree
		# print(title)
		self.title(title)
		# self.style = Style('journal')s
		self.geometry(f'{size[0]}x{size[1]}')
		self.minsize(size[0],size[1])


		#diff frame
		self.head=Header(self)
		self.search=All_frm(self)
		# self.dis=Display_frm(self)
		# btn_1=ttkb.Button(self,text='btn1',bootstyle='primary')
		# btn_1.pack()


		self.mainloop()
class Header(ttkb.Frame):
	def __init__(self,parent,*args, **kwargs):
		super().__init__(parent,style='') #style='info'
		self.place(relx = 0.0, rely = 0.0, 
			relwidth = 1, relheight = 0.15)
		self.create_title()

	def create_title(self):
		lab1=ttkb.Label(self,text='Weather app', font=('JetBrains Mono NL', 20),style='primary')
		lab1.pack(side='left',expand=True,fill='both',padx=10,pady=10)


class Base():
	def __init__(self,parent,*args, **kwargs):
		super().__init__(parent)






class All_frm(ttkb.Frame):
	def __init__(self,parent,*args, **kwargs):
		super().__init__(parent,style='danger')

		self.degree = tk.StringVar()	

		self.place(relx = 0.0, rely = 0.15, 
			relwidth = 1, relheight = 1)


		frm1=ttkb.Frame(self,style='info')
		frm1.place(relx = 0.0, rely = 0.0, relwidth = 1, relheight = 0.15)

		frm2=ttkb.Frame(self,style='primary')
		frm2.place(relx=0.0,rely=0.15,relwidth=1,relheight=0.24)

		self.widgit2(frm1)
		self.widgit1(frm2)




	def widgit2(self,parent):
		self.input_city = tk.StringVar(value=None)
		parent.columnconfigure((0,1,2),weight=1,uniform='a')
		parent.rowconfigure(0,weight=1,uniform='a')

		entry1=ttkb.Entry(parent,style='primary',textvariable=self.input_city,width=10)
		btn1=ttkb.Button(parent,text='search',style='info.Outline',command=self.prnt)

		# entry1.insert('enter the city')

		entry1.grid(row=0,column=0,sticky='nsew',columnspan=2,padx = 20, pady = 10)
		btn1.grid(row=0,column=2,sticky='nsew',padx = 20, pady = 10)
	

	def widgit1(self,parent):
		# print(self.degree.get())
		parent.columnconfigure((0,1,2),weight=1,uniform='b')
		parent.rowconfigure(0,weight=1,uniform='b')
		parent.python_dark = Image.open('sun-regular-24.png')	
		self.lab101=ttkb.Label(parent,text='', font=('JetBrains Mono NL', 20),style='primary')
		self.lab101.grid(row=0,column=0,sticky='nsew',columnspan=2,padx = 20, pady = 10)


	def prnt(self):
		print(self.input_city.get())
		self.lab101['text']=f'{data['main']['temp']}°C'













prn()
Appn("Weather App",(600,400))


