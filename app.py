# ui of the program
from PIL import Image, ImageTk
from api import pull
from constvar import *
import tkinter as tk 
import ttkbootstrap as ttkb  
import json,time

#debug purpose
# data=json.loads('{"coord":{"lon":86.1833,"lat":22.8},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":31.9,"feels_like":31.64,"temp_min":31.9,"temp_max":31.9,"pressure":1013,"humidity":37},"visibility":3000,"wind":{"speed":1.54,"deg":270},"clouds":{"all":20},"dt":1711258148,"sys":{"type":1,"id":9121,"country":"IN","sunrise":1711239320,"sunset":1711283254},"timezone":19800,"id":1269300,"name":"Jamshedpur","cod":200}')


class Appn(ttkb.Window):
	def __init__(self,title,size,*args, **kwargs):
		super().__init__(themename=THM)
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


# heading frame
class Header(ttkb.Frame):
	def __init__(self,parent,*args, **kwargs):
		super().__init__(parent,style=STYL[0][LST]) #style='info'
		self.place(relx = 0.0, rely = 0.0, 
			relwidth = 1, relheight = 0.15)
		self.create_title()

	def create_title(self):
		lab1=ttkb.Label(self,text=WIN_TITLE, font=FONT_TP[0],style=STYL[1][LST])
		lab1.pack(side='left',expand=True,fill='both',padx=10,pady=10)






# all the frame including display and change frame

class All_frm(ttkb.Frame):
	def __init__(self,parent,*args, **kwargs):
		super().__init__(parent,style=STYL[2][LST])

		self.degree = tk.StringVar()	

		self.place(relx = 0.0, rely = 0.15, 
			relwidth = 1, relheight = 1)


		frm1=ttkb.Frame(self,style=STYL[3][LST])
		frm1.place(relx = 0.0, rely = 0.0, relwidth = 1, relheight = 0.15)

		frm2=ttkb.Frame(self,style=STYL[2][LST])
		frm2.place(relx = 0.0, rely = 0.15, relwidth = 1, relheight = 0.15)

		frm3=ttkb.Frame(self,style=STYL[4][LST])
		frm3.place(relx=0.0,rely=0.30,relwidth=1,relheight=0.24)

		self.search_unit(frm1)
		self.location_unit(frm2)
		self.display_unit(frm3)




	def search_unit(self,parent):
		self.input_city = tk.StringVar()
		parent.columnconfigure((0,1,2),weight=1,uniform='a')
		parent.rowconfigure(0,weight=1,uniform='a')

		s = ttkb.Style()
		s.configure(STYL[6][LST], font=FONT_TP[1])

		entry1=ttkb.Entry(parent,style=STYL[5][LST],font=FONT_TP[1],textvariable=self.input_city,width=10)
		self.btn1=ttkb.Button(parent,text='search',style=STYL[6][LST],command=self.prnt)
		# self.btn1.configure(font=FONT_TP[1])

		# entry1.insert('enter the city')

		entry1.grid(row=0,column=0,sticky='nsew',columnspan=2,padx = 20, pady = 10)
		self.btn1.grid(row=0,column=2,sticky='nsew',padx = 20, pady = 10)
	
	def location_unit(self,parent):
		parent.columnconfigure((0),weight=1,uniform='c')
		parent.rowconfigure(0,weight=1,uniform='c')
		self.location=ttkb.Label(parent,text='location',font=FONT_TP[0],style=STYL[7][LST],justify='center')
		self.location.grid(row=0,column=0,sticky='ns',padx=10,pady=10)


	def display_unit(self,parent):
		# print(self.degree.get())
		parent.columnconfigure((0,1,2,3),weight=1,uniform='b')
		parent.rowconfigure(0,weight=1,uniform='b')
		parent.rowconfigure(1,weight=1,uniform='b')

		self.python_dark = Image.open('sun-regular-24.png').resize((35,35))
		self.python_dark_tk = ImageTk.PhotoImage(self.python_dark)

		self.labimg=ttkb.Label(parent,compound='left',text='op',image=self.python_dark_tk,font=FONT_TP[2],style=STYL[7][LST],padding=5)
		self.pressure=ttkb.Label(parent,text='pressure',font=FONT_TP[1],style=STYL[7][LST])
		self.humidity =ttkb.Label(parent,text='humidity',font=FONT_TP[1],style=STYL[7][LST])
		self.windspeed=ttkb.Label(parent,text='windspeed',font=FONT_TP[1],style=STYL[7][LST])
		self.cloud=ttkb.Label(parent,text='cloud',font=FONT_TP[1],style=STYL[7][LST])


		# self.lab101=ttkb.Label(parent,text='', font=('JetBrains Mono NL', 20),style='secondary.Inverse')/
		self.labimg.grid(row=0,column=0,sticky='nswe',columnspan=2,rowspan=2,padx = 10, pady = 10)
		self.pressure.grid(row=0,column=2,sticky='nswe',padx = 10, pady = 10)
		self.humidity.grid(row=1,column=2,sticky='nswe',padx = 10, pady = 10)
		self.windspeed.grid(row=0,column=3,sticky='nswe',padx = 10, pady = 10)
		self.cloud.grid(row=1,column=3,sticky='nswe',padx = 10, pady = 10)

		# self.lab101.grid(row=0,column=1,sticky='nsew',padx = 20, pady = 10)/



	def prnt(self):
		self.btn1.config(state='disabled')
		print(self.input_city.get())
		if self.input_city.get()!='':
			data=pull(self.input_city.get(),0)
			date_today=time.localtime(data['dt'])

			print(f'date = {data['dt']} {time.localtime(data['dt'])}\n {date_today[2]}/{date_today[1]}/{date_today[0]} {date_today[3]}:{date_today[4]}:{date_today[5]} ')
			self.location.config(text=f'{ data['name']},{data['sys']['country']}')
			self.labimg.config(text=f'  {data['main']['temp']}°C ,{data['weather'][0]['description']}')
			self.pressure.config(text=f'pressure {data['main']['pressure']} hPa')
			self.humidity.config(text=f'humidity {data['main']['humidity']} %')
			self.windspeed.config(text=f'windspeed {data['wind']['speed']} m/s')
			self.cloud.config(text=f'cloud {data['clouds']['all']} %')
			self.btn1.config(state='active')
		else:
			print('empty string')
			self.btn1['state']='active'













# prn() debug 
Appn(TITLE_BAR,SIZE_WIN)


