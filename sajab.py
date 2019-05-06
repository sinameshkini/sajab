from tkinter import *
import serial
import RPi.GPIO as GPIO
from threading import * 
import time,datetime,json
from urllib.request import urlretrieve
from hashlib import md5
import requests

ultra1 = serial.Serial("/dev/ttyUSB0",baudrate=9600, timeout=1)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT) #Relay 1
GPIO.setup(33,GPIO.OUT) #Relay 2
GPIO.setup(35,GPIO.OUT) #Relay 3
GPIO.setup(37,GPIO.OUT) #Relay 4
GPIO.setup(12,GPIO.OUT) #Sensor1 Enable

root=Tk()
root.geometry("%dx%d+%d+%d"%(800,480,100,50)) #x,y,horizental,vertical
root.title('SAJAB')
root.configure(background='lightblue')



# with open("conf.json", "r") as conf_file: #opened conf json file
# # conf_file = str(open("conf.json",'r'))
#   global conf_json
#   conf_json = json.load(conf_file)
# conf_file.close()


# v1 = IntVar()
# v1.set(int(conf_json["relay1"]))  # initializing the choice, i.e. Python

# v2 = IntVar()
# v2.set(int(conf_json["relay2"]))  # initializing the choice, i.e. Python

# v3 = IntVar()
# v3.set(int(conf_json["relay3"]))  # initializing the choice, i.e. Python

# v4 = IntVar()
# v4.set(int(conf_json["relay4"]))  # initializing the choice, i.e. Python

# GPIO.output(31,v1.get())
# GPIO.output(33,v2.get())
# GPIO.output(35,v3.get())
# GPIO.output(37,v4.get())

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

def config_req():
    URL = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1"
    try:
        global r
        r = requests.get(URL) 
        global conf_json
        conf_json = r.json()
        
        # urlretrieve("http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1","conf.json")
    except:
        print("request faild\n")
        pass
    # global conf_json
    
    # print(conf_json)
    v1.set(int(conf_json["relay1"]))  # initializing the choice, i.e. Python
    
    v2.set(int(conf_json["relay2"]))  # initializing the choice, i.e. Python
    
    v3.set(int(conf_json["relay3"]))  # initializing the choice, i.e. Python
    
    v4.set(int(conf_json["relay4"]))  # initializing the choice, i.e. Python
    # # print(int(conf_json["relay1"]))
    GPIO.output(31,int(conf_json["relay1"]))
    GPIO.output(33,int(conf_json["relay2"]))
    GPIO.output(35,int(conf_json["relay3"]))
    GPIO.output(37,int(conf_json["relay4"]))    
    # # save_conf()

    global sampling_rate
    global sr_label
    sampling_rate = conf_json['sampling_rate']
    sr_label.config(text=sampling_rate)

config_req()




global config_rate
config_rate = 8

#Variables

pass_main='1120'
time_xloc= 10
time_yloc= 10

date_xloc=10
date_yloc=30

table_x=20
table_y=120

step = 25
stepx = 38

def save_conf():
    with open("conf.json", "w+") as conf_file:
        json.dump(conf_json, conf_file)
    conf_file.close()
   
    

def refresh_conf():
    # with open("conf.json", "r") as conf_file: #opened conf json file
    #     global conf_json
    #     conf_json = json.load(conf_file)
    # conf_file.close()

    # conf_file = str(open("conf.json",'r'))
    global conf_json
    # conf_json = json.loads(conf_file)
    # conf_file.close()


    v1 = IntVar()
    v1.set(int(conf_json["relay1"]))  # initializing the choice, i.e. Python

    v2 = IntVar()
    v2.set(int(conf_json["relay2"]))  # initializing the choice, i.e. Python

    v3 = IntVar()
    v3.set(int(conf_json["relay3"]))  # initializing the choice, i.e. Python

    v4 = IntVar()
    v4.set(int(conf_json["relay4"]))  # initializing the choice, i.e. Python
    # print(int(conf_json["relay1"]))
    GPIO.output(31,int(conf_json["relay1"]))
    GPIO.output(33,int(conf_json["relay2"]))
    GPIO.output(35,int(conf_json["relay3"]))
    GPIO.output(37,int(conf_json["relay4"]))
    

def relay1():
    config_req()
    GPIO.setup(31,GPIO.OUT) #Relay 1
    if v1.get()==0:
        GPIO.output(31,0)
        conf_json["relay1"] = "0"
    else:
        GPIO.output(31,1)
        conf_json["relay1"] = "1"
    conf_str = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1&status=0&relay1=%s" %(conf_json['relay1'])
    try:
        urlretrieve(conf_str)
    except:
        pass
def relay2():
    config_req()
    GPIO.setup(33,GPIO.OUT) #Relay 1
    if v2.get()==0:
        GPIO.output(33,0)
        conf_json["relay2"] = "0"
    else:
        GPIO.output(33,1)
        conf_json["relay2"] = "1"
    conf_str = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1&status=0&relay2=%s" %(conf_json['relay2'])
    try:
        urlretrieve(conf_str)
    except:
        pass
def relay3():
    config_req()
    GPIO.setup(35,GPIO.OUT) #Relay 1
    if v3.get()==0:
        GPIO.output(35,0)
        conf_json["relay3"] = "0"
    else:
        GPIO.output(35,1)
        conf_json["relay3"] = "1"
    conf_str = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1&status=0&relay3=%s" %(conf_json['relay3'])
    try:
        urlretrieve(conf_str)
    except:
        pass
def relay4():
    config_req()
    GPIO.setup(37,GPIO.OUT) #Relay 1
    if v4.get()==0:
        GPIO.output(37,0)
        conf_json["relay4"] = "0"
    else:
        GPIO.output(37,1)
        conf_json["relay4"] = "1"
    conf_str = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1&status=0&relay4=%s" %(conf_json['relay4'])
    try:
        urlretrieve(conf_str)
    except:
        pass

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def sen1_read():
    t = time.time()
    while(1):
        if((time.time()-t)>(sampling_rate*2)):
            return 0
            break
        GPIO.output(12,0)
        ultra1.flushInput()
        u1 = ultra1.read(100)
        GPIO.output(12,1)
        u1 = str(u1)
        if(u1[2]=='R'):
            break
    t_loc = u1.find('T')
    t1 = u1[t_loc+1:t_loc+4]
    loc = u1.find('R')
    u1 = u1[loc+1:loc+6]
    return int(str(u1))






#Functions for splitting the different components of date and time
def nowYear():
    now = datetime.datetime.now()
    year = now.year
    return str(year)

def nowMonth():
    now = datetime.datetime.now()
    month = now.month
    return str(month)

def nowDay():
    now = datetime.datetime.now()
    day = now.day
    return str(day)

def nowHour():
    now = datetime.datetime.now()
    hour = now.hour
    return str(hour)

def nowMinute():
    now = datetime.datetime.now()
    minute = now.minute
    return str(minute)

def nowSecond():
    now = datetime.datetime.now()
    second = now.second
    return str(second)

def year_label(label):
  def count1():
    label.config(text=nowYear())
    label.after(1000, count1)
  count1()

def month_label(label):
  def count2():
    label.config(text=nowMonth())
    label.after(1000, count2)
  count2()

def day_label(label):
  def count3():
    label.config(text=nowDay())
    label.after(1000, count3)
  count3()

def hour_label(label):
  def count4():
    label.config(text=nowHour())
    label.after(1000, count4)
  count4()

def minute_label(label):
  def count5():
    label.config(text=nowMinute())
    label.after(1000, count5)
  count5()

def second_label(label):
  def count6():
    label.config(text=nowSecond())
    label.after(1000, count6)
  count6()

def about():
   filewin = Toplevel(root)
   tx ="""
    Development by: Sina Meshkini
    +98 911 380 6028
    SinaMeshkini7@gmail.com
    @SinaMeshkini
    """
   message = Message(filewin, text=tx, relief = RIDGE , width = 400)
   message.pack(fill="both", expand="yes")
#End Functions

#Desigen Param


color = 'lightblue'
top_fg_color = 'lightblue'
top_bg_color = '#111131'
#End Desigen Param

#Header
w = Canvas(root,width= 800,height= 100)
w.pack()
w.create_rectangle(0,0,800,100,fill=top_bg_color)

Label(root,text='SAJAB Management System',fg=top_fg_color,bg=top_bg_color,font="tahoma 24 bold",pady=10).place(x=150,y=5)

#Time
hourLabel = Label(root,text=nowHour(),fg=top_fg_color,bg=top_bg_color,font=(14))
hourLabel.place(x=time_xloc,y=time_yloc)
hour_label(hourLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=time_xloc+step,y=time_yloc)

minuteLabel = Label(root, text = nowMinute(),fg=top_fg_color,bg=top_bg_color,font=(14))
minuteLabel.place(x=time_xloc+2*step,y=time_yloc)
minute_label(minuteLabel)

colon = Label(root, text = ":",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=time_xloc+3*step,y=time_yloc)

secondLabel = Label(root, text = nowSecond(),fg=top_fg_color,bg=top_bg_color,font=(14))
secondLabel.place(x=time_xloc+4*step,y=time_yloc)
second_label(secondLabel)
#End Time

#Date
yearLabel = Label(root,text=nowYear(),fg=top_fg_color,bg=top_bg_color,font=(14))
yearLabel.place(x=date_xloc,y=date_yloc)
year_label(yearLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=date_xloc+45,y=date_yloc)

monthLabel = Label(root,text=nowMonth(),fg=top_fg_color,bg=top_bg_color,font=(14))
monthLabel.place(x=date_xloc+55,y=date_yloc)
month_label(monthLabel)

colon = Label(root, text = "/",fg=top_fg_color,bg=top_bg_color,font=(14))
colon.place(x=date_xloc+75,y=date_yloc)

dayLabel = Label(root,text=nowDay(),fg=top_fg_color,bg=top_bg_color,font=(14))
dayLabel.place(x=date_xloc+85,y=date_yloc)
day_label(dayLabel)
#End Date

def change_pass():
    global changepass
    changepass = Toplevel()
    changepass.geometry("%dx%d+%d+%d"%(420,180,100,50)) #x,y,horizental,vertical
    changepass.title('Change Password')
    changepass.configure(background='lightblue')
    Label(changepass,text="Enter Old Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20)
    global old_pass
    old_pass=Entry(changepass,width=18,font=(14))
    old_pass.place(x=230,y=20)

    global new_pass1
    Label(changepass,text="Enter New Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20+stepx)
    new_pass1=Entry(changepass,width=18,font=(14))
    new_pass1.place(x=230,y=20+stepx)

    global new_pass2
    Label(changepass,text="Confirm New Password:",fg=top_bg_color,bg=color,font=(14)).place(x=20,y=20+2*stepx)
    new_pass2=Entry(changepass,width=18,font=(14))
    new_pass2.place(x=230,y=20+2*stepx)

    def op_change_pass():
        if str(make_md5(str(old_pass.get()))) == read_pass():
            if str(new_pass1.get()) == str(new_pass2.get()):
                pass_file = open("passwd.txt","w+")
                pass_file.write(str(make_md5(str(new_pass1.get()), encoding='utf-8')))
                pass_file.close()
                changepass.destroy()
                warning = Toplevel()
                warning.geometry("%dx%d+%d+%d"%(150,70,100,50)) #x,y,horizental,vertical
                warning.title('Done')
                warning.configure(background='lightblue')
                Label(warning,text="Password Changed!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
                Button(warning,text="OK",command=warning.destroy).place(x=70,y=40)
            else:
                warning = Toplevel()
                warning.geometry("%dx%d+%d+%d"%(250,80,100,50)) #x,y,horizental,vertical
                warning.title('Warning')
                warning.configure(background='lightblue')
                Label(warning,text="Entered pass isn't match!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
                Button(warning,text="OK",command=warning.destroy).place(x=70,y=50)
        else:
            warning = Toplevel()
            warning.geometry("%dx%d+%d+%d"%(250,80,100,50)) #x,y,horizental,vertical
            warning.title('Warning')
            warning.configure(background='lightblue')
            Label(warning,text="Entered pass is wrong!",fg=top_bg_color,bg=color,width=0).place(x=10,y=20)
            Button(warning,text="OK",command=warning.destroy).place(x=70,y=50)



    Button(changepass,text="OK",command=op_change_pass,font=(14)).place(x=20,y=140)
    Button(changepass,text="Cancel",command=changepass.destroy,font=(14)).place(x=80,y=140)



def pass_check():
    global passcheck
    passcheck = Toplevel()
    passcheck.geometry("%dx%d+%d+%d"%(220,140,100,50)) #x,y,horizental,vertical
    passcheck.title('Setting')
    passcheck.configure(background='lightblue')
    Label(passcheck,text="Enter Password:",fg=top_bg_color,bg=color,font=(14)).place(x=40,y=20)
    global pass_in
    pass_in=Entry(passcheck,width=18,font=(14),show='*')
    pass_in.place(x=25,y=50)

    Button(passcheck,text="OK",command=pass_check2,font=(14)).place(x=80,y=80)
    
def read_pass():
    pass_file = open("passwd.txt","r")
    pass_main = str(pass_file.read())
    return pass_main
    
def pass_check2():
    if make_md5(str(pass_in.get()), encoding='utf-8')==read_pass():
        passcheck.destroy()
        setting()
    else:
        Label(passcheck,text="Password is wrong!",fg=top_bg_color,bg=color,width=0).place(x=40,y=110)

def setting():
    config_req()
    global setting_frame
    setting_frame = Toplevel()
    setting_frame.geometry("%dx%d+%d+%d"%(700,420,100,50)) #x,y,horizental,vertical
    setting_frame.title('Setting')
    setting_frame.configure(background='lightblue')
    Label(setting_frame,text="Station name:",fg=top_bg_color,bg=color,font=(14)).grid(row=0,column=0,ipadx=30,pady=8)
    global st_name
    st_name=Entry(setting_frame,width=15,font=(14))
    st_name.place(x=180,y=10)
    st_name.insert(10,conf_json['name'])
    Label(setting_frame,text="Sampling rate:",fg=top_bg_color,bg=color,font=(14)).grid(row=1,column=0,ipadx=30,pady=8)
    global samp_rate
    samp_rate=Entry(setting_frame,width=8,font=(14))
    samp_rate.place(x=180,y=10+stepx)
    samp_rate.insert(10,str(sampling_rate))
    Label(setting_frame,text="Sec.",fg=top_bg_color,bg=color).place(x=270,y=10+stepx)
    Label(setting_frame,text="Calibration:",fg=top_bg_color,bg=color,font=(14)).grid(row=2,column=0,ipadx=30,pady=8)
    Label(setting_frame,text="Bias Value:",fg=top_bg_color,bg=color,font=(14)).grid(row=3,column=0,ipadx=30,pady=8)
    global bs_value
    bs_value=Entry(setting_frame,width=8,font=(14))
    bs_value.place(x=180,y=10+3*stepx)
    bs_value.insert(10,conf_json['bias_value'])
    Label(setting_frame,text="Coefficent:",fg=top_bg_color,bg=color,font=(14)).grid(row=4,column=0,ipadx=30,pady=8)
    global coef
    coef=Entry(setting_frame,width=8,font=(14))
    coef.place(x=180,y=10+4*stepx)
    coef.insert(10,conf_json['coefficent'])
    Label(setting_frame,text="Set config rate:",fg=top_bg_color,bg=color,font=(14)).grid(row=5,column=0,ipadx=30,pady=8)
    global set_co_r
    set_co_r=Entry(setting_frame,width=8,font=(14))
    set_co_r.place(x=180,y=10+5*stepx)
    set_co_r.insert(10,str(config_rate))



    Label(setting_frame,text="Alert:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10)
    Label(setting_frame,text="Max level:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+stepx)
    global mx_level
    mx_level=Entry(setting_frame,width=8,font=(14))
    mx_level.place(x=500,y=10+stepx)
    mx_level.insert(10,conf_json['max_level'])
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color).place(x=600,y=10+stepx)
    Label(setting_frame,text="Hysteresis level:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+2*stepx)
    global hys_value
    hys_value=Entry(setting_frame,width=8,font=(14))
    hys_value.place(x=500,y=10+2*stepx)
    hys_value.insert(10,conf_json['hysteresis_value'])
    Label(setting_frame,text="m.m.",fg=top_bg_color,bg=color,width=0).place(x=600,y=10+2*stepx)
    Label(setting_frame,text="Mobile Phone 1:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+3*stepx)
    global mob_phone1
    mob_phone1=Entry(setting_frame,width=15,font=(14))
    mob_phone1.place(x=500,y=10+3*stepx)
    mob_phone1.insert(10,conf_json['mobile_phone1'])
    Label(setting_frame,text="Mobile Phone 2:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+4*stepx)
    global mob_phone2
    mob_phone2=Entry(setting_frame,width=15,font=(14))
    mob_phone2.place(x=500,y=10+4*stepx)
    mob_phone2.insert(10,conf_json['mobile_phone2'])
    Label(setting_frame,text="Mobile Phone 3:",fg=top_bg_color,bg=color,font=(14)).place(x=350,y=10+5*stepx)
    global mob_phone3
    mob_phone3=Entry(setting_frame,width=15,font=(14))
    mob_phone3.place(x=500,y=10+5*stepx)
    mob_phone3.insert(10,conf_json['mobile_phone3'])
    Button(setting_frame,text="OK",command=ok,font=(14)).place(x=20,y=320)
    Button(setting_frame,text="Set as default",command=setasdefault,font=(14)).place(x=90,y=320)
    Button(setting_frame,text="Default values",command=defaultvals,font=(14)).place(x=230,y=320)
    Button(setting_frame,text="Change Pass",command=change_pass,font=(14)).place(x=400,y=320)
    Button(setting_frame,text="Cancel",command=cncl,font=(14)).place(x=580,y=320)

def ok():
    global sampling_rate
    sampling_rate = int(samp_rate.get())
    conf_json['bias_value'] = bs_value.get()
    conf_json['coefficent'] = int(coef.get())
    conf_json['max_level'] = int(mx_level.get())
    conf_json['hysteresis_value'] = int(hys_value.get())
    conf_json['mobile_phone1'] = mob_phone1.get()
    conf_json['mobile_phone2'] = mob_phone2.get()
    conf_json['mobile_phone3'] = mob_phone3.get()

    conf_str = "http://www.mehavira.ir/sajab/server.php?action=station&imei=9359374362&station_index=1&status=0&sampling_rate=%d&bias_value=%s&coefficent=%s&max_level=%s&hysteresis_value=%s&mobile_phone1=%s&mobile_phone2=%s&mobile_phone3=%s" %(sampling_rate,conf_json['bias_value'],conf_json['coefficent'],conf_json['max_level'],conf_json['hysteresis_value'],conf_json['mobile_phone1'],conf_json['mobile_phone2'],conf_json['mobile_phone3'])
    sr_label.config(text=sampling_rate)
    try:
        urlretrieve(conf_str)
    except:
        pass
    # save_conf()
    setting_frame.destroy()
def cncl():
    setting_frame.destroy()


def defaultvals():
    with open("default_conf.json", "r") as def_conf_file: #opened conf json file
        global def_conf_json
        def_conf_json = json.load(def_conf_file)
    def_conf_file.close()
    # conf_file = str(open("conf.json",'r'))
    # global conf_json
    # conf_json = json.loads(conf_file)
    # conf_file.close()

    #samp_rate.delete(0,END)
    #samp_rate.insert(10,str(default_sampling_rate))
    bs_value.delete(0,END)
    bs_value.insert(10,def_conf_json['bias_value'])
    coef.delete(0,END)
    coef.insert(10,def_conf_json['coefficent'])
    mx_level.delete(0,END)
    mx_level.insert(10,def_conf_json['max_level'])
    hys_value.delete(0,END)
    hys_value.insert(10,def_conf_json['hysteresis_value'])
    mob_phone1.delete(0,END)
    mob_phone1.insert(10,def_conf_json['mobile_phone1'])
    mob_phone2.delete(0,END)
    mob_phone2.insert(10,def_conf_json['mobile_phone2'])
    mob_phone3.delete(0,END)
    mob_phone3.insert(10,def_conf_json['mobile_phone3'])



def setasdefault():
    sampling_rate = int(samp_rate.get())
    conf_json['bias_value'] = bs_value.get()
    conf_json['coefficent'] = int(coef.get())
    conf_json['max_level'] = int(mx_level.get())
    conf_json['hysteresis_value'] = int(hys_value.get())
    conf_json['mobile_phone1'] = mob_phone1.get()
    conf_json['mobile_phone2'] = mob_phone2.get()
    conf_json['mobile_phone3'] = mob_phone3.get()
    with open("default_conf.json", "w") as def_conf_file:
        json.dump(conf_json, def_conf_file)
    def_conf_file.close()
    


#Body
sensors = ['Sensor 1:','Sensor 2:','Sensor 3:','Sensor 4:']
relays = ['Relay 1','Relay 2','Relay 3','Relay 4']
r=0
for c in sensors:
    Label(root,text=c,fg=top_bg_color,bg=color,font=(14)).place(x=table_x,y=table_y+r*stepx)
    r=r+1
r=0
for c in relays:
    Label(root,text=c,fg=top_bg_color,bg=color,font=(14)).place(x=table_x+300,y=table_y+r*stepx)
    r=r+1
#Sensors Display
global sen1
sen1 = Label(root,fg=top_bg_color,bg=color,font=(14))
sen1.place(x= table_x+130,y=table_y)
#sensor1_read(sen1)
#End Sensors Display


#Relay control
Radiobutton(root,text="OFF",variable=v1,command=relay1,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y)
Radiobutton(root,text="ON",variable=v1,command=relay1,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y)

Radiobutton(root,text="OFF",variable=v2,command=relay2,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+stepx)
Radiobutton(root,text="ON",variable=v2,command=relay2,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+stepx)

Radiobutton(root,text="OFF",variable=v3,command=relay3,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+2*stepx)
Radiobutton(root,text="ON",variable=v3,command=relay3,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+2*stepx)

Radiobutton(root,text="OFF",variable=v4,command=relay4,value=1,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+400,y=table_y+3*stepx)
Radiobutton(root,text="ON",variable=v4,command=relay4,value=0,fg=top_bg_color,bg=color,font=(14)).place(x= table_x+500,y=table_y+3*stepx)

#End Relay control



def send_data():
    data_link = "http://www.mehavira.ir/sajab/server.php?action=save&station_index=1&ha=%d&hb=3&imei=9359374362" %(sen1_data)
    try:
        urlretrieve(data_link)
    except:
        pass
    #if(urlretrieve(data_link)):
    print (data_link)
    #else:
     #   print("Connection  faild, pleas check network")
Button(root,text="Send Data",command=send_data,font=(14)).place(x=200,y=360)


Label(root,text="Sampling rate:",fg=top_bg_color,bg=color,font=(14)).place(x=table_x,y=table_y+4*stepx)
global sr_label
sr_label = Label(root,fg=top_bg_color,bg=color,font=(14))
sr_label.place(x=table_x+130,y=table_y+4*stepx)
sr_label.config(text=sampling_rate)
#sr_read(sr_label)
Label(root,text="Sec.",fg=top_bg_color,bg=color,font=(14)).place(x=table_x+160,y=table_y+4*stepx)


Button(root,text="Config request",command=config_req,font=(14)).place(x=400,y=360)
Button(root,text="Setting",command=pass_check,font=(14)).place(x=630,y=360)

class print_sen(Thread):
    def run(self):
        while(1):
            #print(sen1_read())
            global sen1
            global sen1_data
            sen1_data = sen1_read()
            sen1.config(text=sen1_data)
            send_data()
            config_req()
            # refresh_conf()
            # print (conf_json)
            time.sleep(sampling_rate-0.8)
            

t_print_sen = print_sen()
t_print_sen.start()

root.mainloop()
