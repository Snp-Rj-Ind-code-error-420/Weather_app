# global constant for various data

#theme name 

debug=False
# debug=True
THM='darkly'
TITLE_BAR='Weather App' # tital bar title
SIZE_WIN=(405,390)

WIN_TITLE='WEATHER APP' #window headinfg title
fnt='JetBrains Mono NL'
# title sub title text size and type 0 wintitle 1 additional info title 3celcies titel
FONT_TP=((fnt, 20),(fnt, 10),(fnt, 25))

if debug==True:
	LST=0
else:
	LST=1
# 0 for debug true and 1 for false
STYL=(('secondary','')# header 0
	,('primary','danger') # header title lable 1
	,('danger','') # all frame stle 2
	,('info','') # all frm frm1 search 3
	,('primary','') # all frm1 display output 4
	,('primary','danger')# all fr1 search unit entry 5
	,('warning.TButton','danger.Outline.TButton') # all frm1 search unit button 6
	,('success.Inverse','danger') # all frm1 display unit all_lable 7
	)



