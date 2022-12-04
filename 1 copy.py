#**************************************************************  START APP FOR CODES **********************************************************************************
#************************************************************** LIBRARIES ************************************************************************************************
from MY_LISTS1 import *
import json
from tkinter import *
from tkinter import Spinbox
from tkinter import messagebox
from tkinter import ttk
from tkinter import Button
from tkinter import Checkbutton 
from random import choice                      
#************************************************************ DEFS ************************************************************************************************
#probable = ascii_letters + digits
#captcha = ""
#for i in range(8):
#    captcha += choice(probable)   
#    if captcha==captcha:
#        messagebox.showinfo("Info","Logged in.")
#    else:
#        messagebox.showwarning("Warning","Wrong Captcha.")
def get_price_num_bus():
    return int(num_passengers_bus.get())*250000
def get_price_num_airplane_iran():
    return int(num_passengers_iran.get())*1000000
def get_price_num_train():
    return int(Num_Passengers_Train.get())*450000
def get_price_num_airplane_world():
    return int(num_passengers_world.get())*2500000
def get_price_num_hotel_iran_adult():
    return int(num_of_person_Adult_iran.get()+ num_of_person_Child_iran.get())*750000
def get_price_num_hotel_world_adult():
    return int(num_of_person_Adult_world.get()+ num_of_person_Child_world.get())*950000   
def toggle_password():
    if show_pass.get() == 1:
        e_Password.config(show= '')
    else:
        e_Password.config(show= '●')
def save_airplane_iran():
    query3 = "INSERT INTO `travel`.`airplane`\
    (`cmb_origin`,`cmb_destination`,`dt_flight`,`num_passengers`,`air_companey`,`type_flight`,`time_flight_h`,\
        `time_flight_m`,`seat_number`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    date = f"{dt_flight_year.get()}-{dt_flight_month.get()}-{dt_flight_day.get()}"
    values3 = cmb_origin.get(),cmb_destination.get(),date, num_passengers_world.get()\
        ,air_companey.get(),type_flight.get(),time_flight_h.get(),time_flight_m.get(),seat_number.get()
    cursor.execute(query3,values3)
    connection.commit()
    information = {}
    information['Cmb Origin']= cmb_origin.get()
    information['Cmb Destination']= cmb_destination.get()
    information['Dt Flight Year']= dt_flight_year.get()
    information['Dt Flight Month']= dt_flight_month.get()
    information['Dt Flight Day']= dt_flight_day.get()
    information['Num Passengers']= num_passengers_iran.get()
    information['Air Companey']= air_companey.get()
    information['Type Flight']= type_flight.get()
    information['Time Flight (Hour)']= time_flight_h.get()
    information['Time Flight (Month)']= time_flight_m.get()
    information['Seat Number']= seat_number.get()
    information['price']= get_price_num_airplane_iran()
    f = open(f'Ticket_Airplane_{e_Username.get()}.json','w')
    json.dump(information, f,indent=4)
    f.close()
def save_bus():
    query5 = "INSERT INTO `travel`.`bus` (`cmb_origin`,`cmb_destination`,`dt_deprature`,\
    `num_passengers`,`time_deprature_h`,`time_deprature_m`,`seat_number`)\
     VALUES (%s,%s,%s,%s,%s,%s,%s);"
    date = f"{dt_Departure_year_bus.get()}-{dt_Departure_month_bus.get()}-{dt_Departure_day_bus.get()}"
    values = cmb_origin_bus.get(),cmb_destination_bus.get(),date,num_passengers_bus.get(),time_depatture_h_bus.get(),time_depatture_m_bus.get()\
        ,seat_number_bus.get(),get_price_num_bus()
    cursor.execute(query5,values)
    connection.commit()
    information = {}
    information['Cmb Origin']= cmb_origin_bus.get()
    information['Cmb Destination']= cmb_destination_bus.get()
    information['Dt Departure Year']= dt_Departure_year_bus.get()
    information['dt departure Month']= dt_Departure_month_bus.get()
    information['Dt Departure Day']= dt_Departure_day_bus.get()
    information['Num Depatture (Hour)']= time_depatture_h_bus.get()
    information['Num Depatture (Month)']= time_depatture_m_bus.get()
    information['Seat Number']= seat_number_bus.get()
    information['price']= get_price_num_bus()
    f = open(f'Ticket_Bus_{e_Username.get()}.json','w')
    json.dump(information, f,indent=4)
    f.close()
def save_train():
    query4 = "INSERT INTO `travel`.`train` (`cmb_origin`,`cmb_destination`,`dt_deprature`,\
        `num_passengers`,`time_deprature_h`,`time_deprature_m`,`seat_number`)\
         VALUES (%s,%s,%s,%s,%s,%s,%s);"
    date = f"{Dt_Departure_Year.get()}-{Dt_Departure_Month.get()}-{Dt_Departure_Day.get()}"
    values = Cmb_Origin.get(),Cmb_Destination.get(),date,Num_Passengers_Train.get(),Time_Depatture_Hour.get(),Time_Depatture_Minute.get()\
        ,seat_number.get(),get_price_num_train()
    cursor.execute(query4,values)
    connection.commit()
    information = {}
    information['Cmb Origin']= Cmb_Origin.get()
    information['Cmb Destination']= Cmb_Destination.get()
    information['Dt Departure Year']= Dt_Departure_Year.get()
    information['Dt Departure Month']= Dt_Departure_Month.get()
    information['Dt Departure Day']= Dt_Departure_Day.get()
    information['Num Passengers']= Num_Passengers_Train.get()
    information['Time Deprature (Hour)']= Time_Depatture_Hour.get()
    information['Time Deprature (Month)']= Time_Depatture_Minute.get()
    information['Seat Number']= seat_number.get()
    information['price']= get_price_num_train()
    f = open(f'Ticket Train_{e_Username.get()}.json','w')
    json.dump(information, f,indent=2)
    f.close()
def save_airplane_world():
    query2 = "INSERT INTO `travel`.`airplane`\
        (`cmb_origin`,`cmb_destination`,`dt_flight`,`num_passengers`,`air_companey`,`type_flight`,`time_flight_h`,\
            `time_flight_m`,`seat_number`,`price`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    date = f"{dt_flight_year.get()}-{dt_flight_month.get()}-{dt_flight_day.get()}"
    values2 = cmb_origin.get(),cmb_destination.get(),date, num_passengers_world.get()\
        ,air_companey.get(),type_flight.get(),time_flight_h.get(),time_flight_m.get(),seat_number.get(),get_price_num_airplane_world()
    cursor.execute(query2,values2)
    connection.commit()
    information = {}
    information['Cmb Origin']= cmb_origin.get()
    information['Cmb Destination']= cmb_destination.get()
    information['Dt Flight Year']= dt_flight_year.get()
    information['Dt Flight Month']= dt_flight_month.get()
    information['Dt Flight Day']= dt_flight_day.get()
    information['Num Passengers']= num_passengers_world.get()
    information['Air Companey']= air_companey.get()
    information['Type Flight']= type_flight.get()
    information['Time Flight (Hour)']= time_flight_h.get()
    information['Time Flight (Month)']= time_flight_m.get()
    information['Seat Number']= seat_number.get()
    information['price']= get_price_num_airplane_world()
    f = open(f'Ticket_Airplane_{e_Username.get()}.json','w')
    json.dump(information, f,indent=4)
    f.close()
def save_hotel_iran():
    query3 = "INSERT INTO `travel`.`hotel` (`desired_hotel`, `quality_degree`,\
        `departure_dt`, `avrrival_t_h`, `avrrival_t_m`, `departure_t_h`, `departure_t_m`,\
        `num_person_adult`, `num_person_child`, `num_rooms`, `price`) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s);"
    date = f"{Dt_Departure_Year.get()}-{Dt_Departure_Month.get()}-{Dt_Departure_Day.get()}"
    values = de_hotel.get(),qu_degree.get(),date, time_arrival_h.get(), time_arrival_m.get(),\
        time_departure_h.get(), time_departure_m.get(), num_of_person_Adult_iran.get(),\
            num_of_person_Child_iran.get(), num_of_rooms.get(), get_price_num_hotel_iran_adult()
    cursor.execute(query3,values)
    connection.commit()
    information = {}
    information['Desired Hotel']= de_hotel.get()
    information['Quality Degree']= qu_degree.get()
    information['Number Of Rooms']= num_of_rooms.get()
    information['Departure Date Y']= Dt_Departure_Year.get()
    information['Departure Date M']= Dt_Departure_Month.get()
    information['Departure Date D']= Dt_Departure_Day.get()
    information['Arrival Time H']= time_arrival_h.get()
    information['Arrival Time M']= time_arrival_m.get()
    information['Departure Time H']= time_departure_h.get()
    information['Departure Time M']= time_departure_m.get()
    information['Number Of Person(Adult)']= num_of_person_Adult_iran.get()
    information['Number Of Person(Child)']= num_of_person_Child_iran.get()
    information['price']= get_price_num_hotel_iran_adult()
    f = open(f'Ticket_Hotel_Iran_{e_Username.get()}.json','w')
    json.dump(information, f,indent=4)
    f.close()
def save_hotel_world():
    query3 = "INSERT INTO `travel`.`hotel` (`desired_hotel`, `quality_degree`,\
    `departure_dt`, `avrrival_t_h`, `avrrival_t_m`, `departure_t_h`, `departure_t_m`,\
    `num_person_adult`, `num_person_child`, `num_rooms`, `price`) \
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s);"
    date = f"{Dt_Departure_Year.get()}-{Dt_Departure_Month.get()}-{Dt_Departure_Day.get()}"
    values = de_hotel.get(),qu_degree.get(),date, time_arrival_h.get(), time_arrival_m.get(),\
        time_departure_h.get(), time_departure_m.get(), num_of_person_Adult_world.get(),\
            num_of_person_Child_world.get(), num_of_rooms.get(), get_price_num_hotel_world_adult()
    cursor.execute(query3,values)
    connection.commit()
    information = {}
    information['Desired Hotel']= de_hotel.get()
    information['Quality Degree']= qu_degree.get()
    information['Number Of Rooms']= num_of_rooms.get()
    information['Departure Date Y']= Dt_Departure_Year.get()
    information['Departure Date M']= Dt_Departure_Month.get()
    information['Departure Date D']= Dt_Departure_Day.get()
    information['Arrival Time H']= time_arrival_h.get()
    information['Arrival Time M']= time_arrival_m.get()
    information['Departure Time H']= time_departure_h.get()
    information['Departure Time M']= time_departure_m.get()
    information['Number Of Person(Adult)']= num_of_person_Adult_world.get()
    information['Number Of Person(Child)']= num_of_person_Child_world.get()
    information['price']= get_price_num_hotel_world_adult()
    f = open(f'Ticket_Hotel_World{e_Username.get()}.json','w')
    json.dump(information, f,indent=4)
    f.close()
def back():
    login2.withdraw()
    login .deiconify()
def Login():
    login.withdraw()
    try:
        f = open(f'{e_Username.get()}.json','r')
        information = json.load(f)
        f.close()
        if e_Password.get() == information['password']:
            messagebox.showinfo("Information",f"Welcome : {information['firstname']} {information['lastname']}")
            login2.deiconify()
        else:
            messagebox.showwarning("Warning","The Information Entered Is Incorrect. Please Re-Enter The Information.")
            login.deiconify()
    except FileNotFoundError:
        messagebox.showwarning("Warning","Can't Find This Username.")
        login.deiconify()
def Singup():
    global e_firstname
    global e_lastname
    global e_username_sign_up
    def save():
        try:
            query = "INSERT INTO `travel`.`singup`\
            (`firstname`, `lastname`, `age`, `nationality`, `gender`, `email`, `username`,\
            `password`, `datebirthday`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            date = f"{date_year.get()}-{date_month.get()}-{date_day.get()}"
            values = e_firstname.get(),e_lastname.get(),sp_age.get(),e_natinality.get(),g.get(),e_email.get()\
                ,e_username_sign_up.get(),e_password_sign_up.get(),date
            cursor.execute(query,values)
            connection.commit()
            messagebox.showinfo("Success", "Account Created Succesfully.")
        except:
            messagebox.showerror("Fail", "Account did not create Succesfully.\n Maybe username or email is already taken!")
        # اینجا
        info ={}
        info['firstname']= e_firstname.get()
        info['lastname']= e_lastname.get()
        info['date_birthday']= f"{date_year.get()}/{date_month.get()}/{date_day.get()}"
        info['age']= sp_age.get()
        info['gender']= g.get()
        info['nationality']= e_natinality.get()
        info['username']= e_username_sign_up.get()
        info['password']= e_password_sign_up.get()
        info['email']= e_email.get()
        f = open(f'{e_username_sign_up.get()}.json','w') 
        json.dump(info, f, indent=4)
        f.close()
        # اینجا
    window2 = Tk()
    window2.title('Signup')
    window2.geometry('910x500')
    window2.config(bg=COLOR1)
    l_welcome= Label(window2,text='Sing up',font=('',40),bg=COLOR1,fg=COLOR2)
    l_Firstname= Label(window2,text='Firstname: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Lastname= Label(window2,text='Lastname: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Date_on_birthday= Label(window2,text='Date on birthday: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Age= Label(window2,text='Age: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Gender= Label(window2,text='Gender: ',font=('',18),bg=COLOR1,fg=COLOR2)
    g= StringVar(window2)
    frm_rbuttons= Frame(window2)
    frm_rbuttons.grid(row=4,column=6,sticky='e')
    rb1= Radiobutton(frm_rbuttons, text="Male", variable=g, value='Male',bg=COLOR1,fg=COLOR2)
    rb2= Radiobutton(frm_rbuttons, text="Female", variable=g, value='Female',bg=COLOR1,fg=COLOR2)
    rb3= Radiobutton(frm_rbuttons, text="Rather Not to say", variable=g, value='_',bg=COLOR1,fg=COLOR2)
    g.set('_')
    rb1.grid(row=1,column=1,sticky='e')
    rb2.grid(row=1,column=2,sticky='e')
    rb3.grid(row=1,column=3,sticky='e')
    l_Nationality= Label(window2,text='Nationality: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Email= Label(window2,text='Email: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Uaername= Label(window2,text='Username: ',font=('',18),bg=COLOR1,fg=COLOR2)
    l_Password= Label(window2,text='Password: ',font=('',18),bg=COLOR1,fg=COLOR2)
    e_firstname= Entry(window2,bg=COLOR2)
    e_lastname= Entry(window2,bg=COLOR2)
    sp_age= Spinbox(window2,from_=12,to=50)
    e_natinality= ttk.Combobox(window2,values=list_of_countries)
    e_natinality.config(state='readonly')
    e_natinality.grid(row=5,column=4)
    e_email= Entry(window2,bg=COLOR2)
    e_email.insert(0,'@Gmail.Com')
    e_username_sign_up= Entry(window2,bg=COLOR2)
    e_password_sign_up= Entry(window2,bg=COLOR2)
    e_firstname.grid(row=2,column=4)
    e_lastname.grid(row=2,column=6)
    sp_age.grid(row=4,column=4)
    e_email.grid(row=7,column=4)
    e_username_sign_up.grid(row=6,column=4)
    e_password_sign_up.grid(row=6,column=6)
    date_year= Spinbox(window2,text='Year:',from_=1960,to=2022)
    date_year.config(state='readonly')
    date_year.grid(row=3,column=4,padx=30,pady=5)
    date_month= Spinbox(window2,text='Month:',from_=1,to=12)
    date_month.config(state='readonly')
    date_month.grid(row=3,column=5,padx=30,pady=5)
    date_day= Spinbox(window2,text='Day:',from_=1,to=31)
    date_day.insert(0,1)
    date_day.config(state='readonly')
    date_day.grid(row=3,column=6,padx=30,pady=5)
    l_welcome.grid(row=1,column=4,padx=20,pady=5,sticky='news')
    l_Firstname.grid(row=2,column=3,padx=20,pady=5,sticky='news')
    l_Lastname.grid(row=2,column=5,padx=20,pady=5,sticky='news')
    l_Date_on_birthday.grid(row=3,column=3,padx=20,pady=5,sticky='news')
    l_Age.grid(row=4,column=3,padx=20,pady=5,sticky='news')
    l_Gender.grid(row=4,column=5,padx=20,pady=5,sticky='news')
    l_Nationality.grid(row=5,column=3,padx=20,pady=5,sticky='news')
    l_Uaername.grid(row=6,column=3,padx=20,pady=5,sticky='news')
    l_Password.grid(row=6,column=5,padx=20,pady=5,sticky='news')
    l_Email.grid(row=7,column=3,padx=20,pady=5,sticky='news')
    btn_save= Button(window2,text='Save',font=('',15),command=save,activebackground=COLOR1,bg=COLOR2,fg=COLOR1)
    btn_back= Button(window2,text='Back',font=('',15),command=window2.destroy,activebackground=COLOR1,bg=COLOR2,fg=COLOR1) 
    btn_exit= Button(window2,text='Exit',font=('',15),command=exit,activebackground=COLOR1,bg=COLOR2,fg=COLOR1) 
    btn_save.grid(row=8,column=3,sticky='e')
    btn_back.grid(row=8,column=4,sticky='e')
    btn_exit.grid(row=8,column=5,sticky='e')
import pymysql
connection = pymysql.connect(host='127.0.0.1',user='root',password='ROOT'.lower())
cursor = connection.cursor()
for query in list_of_db_queries:
    cursor.execute(query)
#************************************************************ ROOT ***********************************************************************************************************

login= Tk()
login.title('Login')
login.geometry('570x350')
login.config  (bg=COLOR1)
#********************************************************** LBL,BTN,ENTRY ROOT ***************************************************************************************************
l_welcome=Label(login,text='Welcome',font=('',40),bg=COLOR1,fg=COLOR3)
l_Username=Label(login,text='Username: ',font=('',18),bg=COLOR1,fg=COLOR2)
l_Password=Label(login,text='Password: ',font=('',18),bg=COLOR1,fg=COLOR2)
#l_captcha=Label(login,text=f"Captcha:\n{captcha}",font=('',18),bg=COLOR1,fg=COLOR3)
l_dont_account=Label(login,text="Don't Have An Account? ",font=('',15),bg=COLOR1,fg=COLOR3)
e_Username=Entry(login,bg=COLOR2)
e_Password=Entry(login,show='●',bg=COLOR2)
#e_captcha=Entry(login,bg=COLOR3)
btn_login=Button(login,text='Log in',activebackground=COLOR1,command=Login,fg=COLOR1,bg=COLOR2)
btn_Singup=Button(login,text='Sing Up',activebackground=COLOR1,command=Singup,fg=COLOR1,bg=COLOR2)
show_pass=IntVar()
checkbutton=Checkbutton(login, text='', variable=show_pass,bg=COLOR1 ,command=toggle_password)
#********************************************************** LBL,BTN,ENTRY FOR GIRD ****************************************************************************************
l_welcome.grid(row=1,column=3,padx=20,pady=5 ,columnspan=2,sticky='w')
l_Username.grid(row=2,column=2,padx=20,pady=5 ,sticky='news')
l_Password.grid(row=3,column=2,padx=20,pady=5 ,sticky='news')
#l_captcha.grid(row=4,column=2,padx=20,pady=5,sticky='news')
l_dont_account.grid(row=6,column=3,padx=20,pady=5 ,sticky='w')
e_Username.grid(row=2,column=3,padx=20,pady=5 ,sticky='news')
e_Password.grid(row=3,column=3,padx=20,pady=5 ,sticky='news')
#e_captcha.grid(row=4,column=3,padx=20,pady=5 ,sticky='news')
checkbutton.grid(row=3,column=4,padx=20,pady=5 ,sticky='news')
btn_login.grid(row=5,column=3,padx=20,pady=5)
btn_Singup.grid(row=6,column=4,padx=20,pady=5 ,sticky='news')
#********************************************************** LOGIN2 ********************************************************************************************
login2=Toplevel(login)
lbl_travel=Label(login2,text='Travel Agency',bg=COLOR1,fg=COLOR4,font=('',30))
tabs=ttk.Notebook(login2)
passive_color="#9CEBB3"
active_color="#2A2B2A"
style=ttk.Style()
login2.withdraw()
login2.title('Travel Agency')
login2.geometry('880x480')
login2.config(bg=COLOR1)
style.theme_create ("yummy", parent="alt", 
settings={
        "TNotebook": 
            {"configure": 
                {"tabmargins": [2, 5, 2, 0] }
            },
            "TNotebook.Tab": 
            {
            "configure":
                {"padding": [5, 1], "background": passive_color },
                "map":
                    {
                        "background": [("selected", active_color)],
                            "expand": [("selected", [1, 1, 1, 0])]
                    }
            }
    }
)
style.theme_use("yummy")
tabs.grid(row=2,column=3)
lbl_travel.grid(row=1,column=3)
#********************************************************** FRM ***********************************************************************************************
frm_airplane_iran=Frame(tabs,bg=COLOR1)
frm_airplane_world=Frame(tabs,bg=COLOR1)
frm_train=Frame(tabs,bg=COLOR1)
frm_Bus=Frame(tabs,bg=COLOR1)
frm_hotel_iran=Frame(tabs,bg=COLOR1)
frm_hotel_world=Frame(tabs,bg=COLOR1)
frm_prospal=Frame(tabs,bg=COLOR1)
#5564644864
treev = ttk.Treeview(frm_prospal, selectmode ='browse')
treev.grid(row=1, column=1, columnspan=9)
verscrlbar = ttk.Scrollbar(frm_prospal,orient ="vertical",command = treev.yview)
horizontalscrlbar = ttk.Scrollbar(frm_prospal,orient ="horizontal",command = treev.xview)
verscrlbar.grid(row=1, column=10, sticky='ns')
horizontalscrlbar.grid(row=2, column=1, columnspan=9, sticky='ew')
treev.configure(yscrollcommand = verscrlbar.set, xscrollcommand=horizontalscrlbar.set)
treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
treev['show'] = 'headings'
treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='c')
treev.column("3", width = 40, anchor ='c')
treev.column("4", width = 90, anchor ='c')
treev.column("5", width = 90, anchor ='c')
treev.column("6", width = 90, anchor ='c')
treev.column("7", width = 90, anchor ='c')
treev.column("8", width = 90, anchor ='c')
treev.column("9", width = 90, anchor ='c')
treev.heading("1", text ="cmb origin")
treev.heading("2", text ="cmb destination")
treev.heading("3", text ="Date")
treev.heading("4", text ="num passengers ")
treev.heading("5", text ="time")
treev.heading("6", text ="seat number")
treev.heading("7", text ="num depatture")
treev.heading("8", text ="Link")
treev.heading("9", text ="Description")
iv_airplane_iran = IntVar()
cb_airplane_iran = Checkbutton(frm_prospal,variable=iv_airplane_iran,bg=COLOR4)
lbl_airplane_iran = Label(frm_prospal,text='Search Prospal By Airplane Iran : ',bg='white')
e_airplane_iran = Entry(frm_prospal,bg='black',fg='white')
cb_airplane_iran.grid(row=3,column=1,sticky='e')
lbl_airplane_iran.grid(row=3,column=2,sticky='w')
e_airplane_iran.grid(row=3,column=3)

iv_airplane_world = IntVar()
cb_airplane_world = Checkbutton(frm_prospal,variable=iv_airplane_world,bg=COLOR4)
lbl_airplane_world = Label(frm_prospal,text='Search Prospal By Airplane World : ',bg='white')
e_airplane_world = Entry(frm_prospal,bg='black',fg='white')
cb_airplane_world.grid(row=4,column=1,sticky='e')
lbl_airplane_world.grid(row=4,column=2,sticky='w')
e_airplane_world.grid(row=4,column=3)

iv_train = IntVar()
cb_train = Checkbutton(frm_prospal,variable=iv_train,bg=COLOR4)
lbl_train = Label(frm_prospal,text='Search Prospal By Train: ',bg='white')
e_train   = Entry(frm_prospal,bg='black',fg='white')
cb_train.grid(row=5,column=1,sticky='e')
lbl_train.grid(row=5,column=2,sticky='w')
e_train.grid(row=5,column=3)

iv_bus = IntVar()
cb_bus = Checkbutton(frm_prospal,variable=iv_bus,bg=COLOR4)
lbl_bus = Label(frm_prospal,text='Search Prospal By Bus : ',bg='white')
e_bus = Entry(frm_prospal,bg='black',fg='white')
cb_bus.grid(row=6,column=1,sticky='e')
lbl_bus.grid(row=6,column=2,sticky='w')
e_bus.grid(row=6,column=3)

iv_hotel_iran = IntVar()
cb_hotel_iran = Checkbutton(frm_prospal,variable=iv_hotel_iran,bg=COLOR4)
lbl_hotel_iran = Label(frm_prospal,text='Search Prospal By Hotel Iran : ',bg='white')
e_hotel_iran = Entry(frm_prospal,bg='black',fg='white')
cb_hotel_iran.grid(row=7,column=1,sticky='e')
lbl_hotel_iran.grid(row=7,column=2,sticky='w')
e_hotel_iran.grid(row=7,column=3)

iv_hotel_world = IntVar()
cb_hotel_world = Checkbutton(frm_prospal,variable=iv_hotel_world,bg=COLOR4)
lbl_hotel_world = Label(frm_prospal,text='Search Prospal By Hotel World : ',bg='white')
e_hotel_world = Entry(frm_prospal,bg='black',fg='white')
cb_hotel_world.grid(row=8,column=1,sticky='e')
lbl_hotel_world.grid(row=8,column=2,sticky='w')
e_hotel_world.grid(row=8,column=3)

btn_search = Button(frm_prospal,text='Search',command=save_airplane_iran)
btn_save = Button(frm_prospal,text='Save',command=save_airplane_iran)
btn_exit = Button(frm_prospal,text='Exit',command=exit)
btn_search.grid(row=3, column=9)
btn_save.grid(row=4, column=9)
btn_exit.grid(row=5, column=9)
#******************************************************* LBL FOR AIRPLANE IRAN ********************************************************************************
Label(frm_airplane_iran,text='Your Origin:         ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Your Destination:    ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Flight Date:         ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Number Of Passengers:',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Airline Companey:    ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Flight Type:         ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Flight Time:         ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=6,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_iran,text='Seat Number:         ',bg=COLOR1,fg=COLOR5,font=('',15)).grid(row=7,column=1,padx=20,pady=5,sticky='news')
#******************************************************* LBL FOR AIRPLANE WORLD *******************************************************************************
Label(frm_airplane_world,text='Your Origin:          ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Your Destination:     ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Flight Date:          ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Number Of Passengers: ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Airline Companey:     ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Flight Type:          ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Flight Time:          ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=6,column=1,padx=20,pady=5,sticky='news')
Label(frm_airplane_world,text='Seat Number:          ',bg=COLOR1,fg=COLOR6,font=('',15)).grid(row=7,column=1,padx=20,pady=5,sticky='news')
#******************************************************* LBL FOR BUS  ******************************************************************************************
Label(frm_Bus,text='Your Origin: '                    ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_Bus,text='Your Destination: '               ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='news')
Label(frm_Bus,text='Departure Date: '                 ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_Bus,text='Number Of Passengers: '           ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_Bus,text='Departure Time: '                 ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_Bus,text='Seat Number: '                    ,bg=COLOR1,fg=COLOR7,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
#******************************************************* LBL FOR TRAIN ****************************************************************************************
Label(frm_train,text='Your Origin: '                  ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_train,text='Your Destination: '             ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='news')
Label(frm_train,text='Departure Date: '               ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_train,text='Number Of Passengers: '         ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_train,text='Departure Time: '               ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_train,text='Seat Number: '                  ,bg=COLOR1,fg=COLOR8,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
#******************************************************* LBL FOR HOTEL IRAN ***********************************************************************************
Label(frm_hotel_iran,text='Desired Hotel: '           ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Quality Degree: '          ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Number Of Rooms: '         ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Departure Date: '          ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Arrival Time: '            ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Departure Time: '          ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Number Of Person(Adult): ' ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=6,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_iran,text='Number Of Person(Child): ' ,bg=COLOR1,fg=COLOR9,font=('',15)).grid(row=7,column=1,padx=20,pady=5,sticky='news')
#******************************************************* LBL FOR HOTEL WORLD **********************************************************************************************
Label(frm_hotel_world,text='Desired Hotel: '          ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=1,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Quality Degree: '         ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=1,column=3,padx=20,pady=5,sticky='w')
Label(frm_hotel_world,text='Number Of Rooms: '        ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=2,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Departure Date: '         ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=3,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Arrival Time: '           ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=4,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Departure Time: '         ,bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=5,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Number Of Person(Adult): ',bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=6,column=1,padx=20,pady=5,sticky='news')
Label(frm_hotel_world,text='Number Of Person(Child): ',bg=COLOR1,fg=COLOR10,font=('',15)).grid(row=7,column=1,padx=20,pady=5,sticky='news')
#******************************************************* TABS *************************************************************************************************************
tabs.add (frm_airplane_iran,text='Airplane_iran')
tabs.add (frm_airplane_world,text='Airplane_world')
tabs.add (frm_train,text='Train')
tabs.add (frm_Bus,text='Bus')
tabs.add (frm_hotel_iran,text='Hotel Of Iran')
tabs.add (frm_hotel_world,text='Hotel Of World')
tabs.add (frm_prospal,text='Prospal')
#******************************************************* AIRPLANE FOR IRAN  ******************************************************************************************************
cmb_origin= ttk.Combobox(frm_airplane_iran,values=list_of_iran_cities)
cmb_origin.config(state='readonly')
cmb_origin.grid(row=1,column=2)
cmb_destination= ttk.Combobox(frm_airplane_iran,values=list_of_iran_cities)
cmb_destination.config(state='readonly')
cmb_destination.grid(row=1,column=4)
dt_flight_year= Spinbox(frm_airplane_iran,from_=2022,to=2050)
dt_flight_year.config(state='readonly')
dt_flight_year.grid(row=2,column=2,padx=20,pady=5)
dt_flight_month= Spinbox(frm_airplane_iran,from_=1,to=12)
dt_flight_month.config(state='readonly')
dt_flight_month.grid(row=2,column=3,padx=20,pady=5)
dt_flight_day= Spinbox(frm_airplane_iran,from_=1,to=31)
dt_flight_day.config(state='readonly')
dt_flight_day.grid(row=2,column=4,padx=20,pady=5)
num_passengers_iran= Spinbox(frm_airplane_iran,from_=1,to=20)
num_passengers_iran.config(state='readonly')
num_passengers_iran.grid(row=3,column=2,padx=20,pady=5)
air_companey= ttk.Combobox(frm_airplane_iran,values=list_of_airlines_iran)
air_companey.config(state='readonly')
air_companey.grid(row=4,column=2,padx=20,pady=5)
type_flight= ttk.Combobox(frm_airplane_iran,values=['First Class','Business Class','Economy Class',
                                                  'Prenium Economy Class'])
type_flight.config(state='readonly')
type_flight.grid(row=5,column=2,padx=20,pady=5)
time_flight_h= Spinbox(frm_airplane_iran,from_=00,to=24)
time_flight_h.config(state='readonly')
time_flight_h.grid(row=6,column=2,padx=20,pady=5)
time_flight_m= Spinbox(frm_airplane_iran,from_=00,to=59)
time_flight_m.config(state='readonly')
time_flight_m.grid(row=6,column=3,padx=20,pady=5)
seat_number= ttk.Combobox(frm_airplane_iran,values=list_of_seat_numbers)
seat_number.config(state='readonly')
seat_number.grid(row=7,column=2,padx=20,pady=5)
#******************************************************* AIRPLANE FOR WORLD *****************************************************************************************************
cmb_origin= ttk.Combobox(frm_airplane_world,values=list_of_world_cities)
cmb_origin.config(state='readonly')
cmb_origin.grid(row=1,column=2)
cmb_destination= ttk.Combobox(frm_airplane_world,values=list_of_world_cities)
cmb_destination.config(state='readonly')
cmb_destination.grid(row=1,column=4)
dt_flight_year= Spinbox(frm_airplane_world,from_=2022,to=2050)
dt_flight_year.config(state='readonly')
dt_flight_year.grid(row=2,column=2,padx=20,pady=5)
dt_flight_month= Spinbox(frm_airplane_world,from_=1,to=12)
dt_flight_month.config(state='readonly')
dt_flight_month.grid(row=2,column=3,padx=20,pady=5)
dt_flight_day= Spinbox(frm_airplane_world,from_=1,to=31)
dt_flight_day.config(state='readonly')
dt_flight_day.grid(row=2,column=4,padx=20,pady=5)
num_passengers_world= Spinbox(frm_airplane_world,from_=1,to=20)
num_passengers_world.config(state='readonly')
num_passengers_world.grid(row=3,column=2,padx=20,pady=5)
air_companey= ttk.Combobox(frm_airplane_world,values=list_of_airlines_world)
air_companey.config(state='readonly')
air_companey.grid(row=4,column=2,padx=20,pady=5)
type_flight= ttk.Combobox(frm_airplane_world,values=['First Class','Business class', 
                                                'Economy Class','Prenium Economy Class'])
type_flight.config(state='readonly')
type_flight.grid(row=5,column=2,padx=20,pady=5)
time_flight_h= Spinbox(frm_airplane_world,from_=00,to=24)
time_flight_h.config(state='readonly')
time_flight_h.grid(row=6,column=2,padx=20,pady=5)
time_flight_m= Spinbox(frm_airplane_world,from_=00,to=59)
time_flight_m.config(state='readonly')
time_flight_m.grid(row=6,column=3,padx=20,pady=5)
seat_number= ttk.Combobox(frm_airplane_world,values=list_of_seat_numbers)
seat_number.config(state='readonly')
seat_number.grid(row=7,column=2,padx=20,pady=5)
#******************************************************* BUS ********************************************************************************************************************
cmb_origin_bus= ttk.Combobox(frm_Bus,values=list_of_iran_cities)
cmb_origin_bus.config(state='readonly')
cmb_origin_bus.grid(row=1,column=2)
cmb_destination_bus= ttk.Combobox(frm_Bus,values=list_of_iran_cities)
cmb_destination_bus.config(state='readonly')
cmb_destination_bus.grid(row=1,column=4)
dt_Departure_year_bus= Spinbox(frm_Bus,from_=2022,to=2050)
dt_Departure_year_bus.config(state='readonly')
dt_Departure_year_bus.grid(row=2,column=2,padx=20,pady=5)
dt_Departure_month_bus= Spinbox(frm_Bus,from_=1,to=12)
dt_Departure_month_bus.config(state='readonly')
dt_Departure_month_bus.grid(row=2,column=3,padx=20,pady=5)
dt_Departure_day_bus= Spinbox(frm_Bus,from_=1,to=31)
dt_Departure_day_bus.config(state='readonly')
dt_Departure_day_bus.grid(row=2,column=4,padx=20,pady=5)
num_passengers_bus= Spinbox(frm_Bus,from_=1,to=20)
num_passengers_bus.config(state='readonly')
num_passengers_bus.grid(row=3,column=2,padx=20,pady=5)
time_depatture_h_bus= Spinbox(frm_Bus,from_=00,to=24)
time_depatture_h_bus.config(state='readonly')
time_depatture_h_bus.grid(row=4,column=2,padx=20,pady=5)
time_depatture_m_bus= Spinbox(frm_Bus,from_=00,to=59)
time_depatture_m_bus.config(state='readonly')
time_depatture_m_bus.grid(row=4,column=3,padx=20,pady=5)
seat_number_bus= ttk.Combobox(frm_Bus,values=list_of_seat_numbers)
seat_number_bus.config(state='readonly')
seat_number_bus.grid(row=5,column=2,padx=20,pady=5)
#******************************************************* TRAIN ********************************************************************************************************************
Cmb_Origin= ttk.Combobox(frm_train,values=list_of_iran_cities)
Cmb_Origin.config(state='readonly')
Cmb_Origin.grid(row=1,column=2)
Cmb_Destination= ttk.Combobox(frm_train,values=list_of_iran_cities)
Cmb_Destination.config(state='readonly')
Cmb_Destination.grid(row=1,column=4)
Dt_Departure_Year= Spinbox(frm_train,from_=2022,to=2050)
Dt_Departure_Year.config(state='readonly')
Dt_Departure_Year.grid(row=2,column=2,padx=20,pady=5)
Dt_Departure_Month= Spinbox(frm_train,from_=1,to=12)
Dt_Departure_Month.config(state='readonly')
Dt_Departure_Month.grid(row=2,column=3,padx=20,pady=5)
Dt_Departure_Day= Spinbox(frm_train,from_=1,to=31)
Dt_Departure_Day.config(state='readonly')
Dt_Departure_Day.grid(row=2,column=4,padx=20,pady=5)
Num_Passengers_Train= Spinbox(frm_train,from_=1,to=20)
Num_Passengers_Train.config(state='readonly')
Num_Passengers_Train.grid(row=3,column=2,padx=20,pady=5)
Time_Depatture_Hour= Spinbox(frm_train,from_=00,to=24)
Time_Depatture_Hour.config(state='readonly')
Time_Depatture_Hour.grid(row=4,column=2,padx=20,pady=5)
Time_Depatture_Minute= Spinbox(frm_train,from_=00,to=59)
Time_Depatture_Minute.config(state='readonly')
Time_Depatture_Minute.grid(row=4,column=3,padx=20,pady=5)
Seat_Number= ttk.Combobox(frm_train,values=list_of_seat_numbers)
Seat_Number.config(state='readonly')
Seat_Number.grid(row=5,column=2,padx=20,pady=5)
#******************************************************* HOTEL FOR IRAN *************************************************************************************************************
de_hotel= ttk.Combobox(frm_hotel_iran,values=list_of_hotel_iran)
de_hotel.config(state='readonly')
de_hotel.grid(row=1,column=2)
qu_degree= ttk.Combobox(frm_hotel_iran,values=list_of_hotel_degree_iran)
qu_degree.config(state='readonly')
qu_degree.grid(row=1,column=4)
num_of_rooms= Spinbox(frm_hotel_iran,from_=0,to=10)
num_of_rooms.config(state='readonly')
num_of_rooms.grid(row=2,column=4)
dt_Departure_year= Spinbox(frm_hotel_iran,from_=2022,to=2050)
dt_Departure_year.config(state='readonly')
dt_Departure_year.grid(row=3,column=2)
dt_Departure_month= Spinbox(frm_hotel_iran,from_=1,to=12)
dt_Departure_month.config(state='readonly')
dt_Departure_month.grid(row=3,column=3)
Dt_Departure_Day= Spinbox(frm_hotel_iran,from_=1,to=31)
Dt_Departure_Day.config(state='readonly')
Dt_Departure_Day.grid(row=3,column=4)
time_arrival_h= Spinbox(frm_hotel_iran,from_=00,to=24)
time_arrival_h.config(state='readonly')
time_arrival_h.grid(row=4,column=2)
time_arrival_m= Spinbox(frm_hotel_iran,from_=00,to=59)
time_arrival_m.config(state='readonly')
time_arrival_m.grid(row=4,column=3)
time_departure_h= Spinbox(frm_hotel_iran,from_=00,to=24)
time_departure_h.config(state='readonly')
time_departure_h.grid(row=5,column=2)
time_departure_m= Spinbox(frm_hotel_iran,from_=00,to=59)
time_departure_m.config(state='readonly')
time_departure_m.grid(row=5,column=3)
num_of_person_Adult_iran= Spinbox(frm_hotel_iran,from_=0,to=20)
num_of_person_Adult_iran.config(state='readonly')
num_of_person_Adult_iran.grid(row=6,column=2)
num_of_person_Child_iran= Spinbox(frm_hotel_iran,from_=0,to=20)
num_of_person_Child_iran.config(state='readonly')
num_of_person_Child_iran.grid(row=7,column=2)
#******************************************************* HOTEL FOR WORLD *********************************************************************************************************
de_hotel= ttk.Combobox(frm_hotel_world,values=list_of_hotel_world)
de_hotel.config(state='readonly')
de_hotel.grid(row=1,column=2)
qu_degree= ttk.Combobox(frm_hotel_world,values=list_of_hotel_degree_world)
qu_degree.config(state='readonly')
qu_degree.grid(row=1,column=4)
num_of_rooms= Spinbox(frm_hotel_world,from_=0,to=20)
num_of_rooms.config(state='readonly')
num_of_rooms.grid(row=2,column=4)
dt_Departure_year= Spinbox(frm_hotel_world,from_=2022,to=2050)
dt_Departure_year.config(state='readonly')
dt_Departure_year.grid(row=3,column=2)
dt_Departure_month= Spinbox(frm_hotel_world,from_=1,to=12)
dt_Departure_month.config(state='readonly')
dt_Departure_month.grid(row=3,column=3)
Dt_Departure_Day= Spinbox(frm_hotel_world,from_=1,to=31)
Dt_Departure_Day.config(state='readonly')
Dt_Departure_Day.grid(row=3,column=4)
time_arrival_h= Spinbox(frm_hotel_world,from_=00,to=24)
time_arrival_h.config(state='readonly')
time_arrival_h.grid(row=4,column=2)
time_arrival_m= Spinbox(frm_hotel_world,from_=00,to=59)
time_arrival_m.config(state='readonly')
time_arrival_m.grid(row=4,column=3)
time_departure_h= Spinbox(frm_hotel_world,from_=00,to=24)
time_departure_h.config(state='readonly')
time_departure_h.grid(row=5,column=2)
time_departure_m= Spinbox(frm_hotel_world,from_=00,to=59)
time_departure_m.config(state='readonly')
time_departure_m.grid(row=5,column=3)
num_of_person_Adult_world= Spinbox(frm_hotel_world,from_=0,to=20)
num_of_person_Adult_world.config(state='readonly')
num_of_person_Adult_world.grid(row=6,column=2)
num_of_person_Child_world= Spinbox(frm_hotel_world,from_=0,to=20)
num_of_person_Child_world.config(state='readonly')
num_of_person_Child_world.grid(row=7,column=2)
#******************************************************* BUTTONS ******************************************************************************************************************
Button(frm_airplane_world,text ='Confirm Operation',activebackground=COLOR6,command=save_airplane_world,bg=COLOR5,fg=COLOR1).grid(row=8,column=1)
Button(frm_airplane_world,text ='Back'             ,activebackground=COLOR6,command=back               ,bg=COLOR5,fg=COLOR1).grid(row=8,column=3)
Button(frm_airplane_iran ,text ='Confirm Operation',activebackground=COLOR5,command=save_airplane_iran ,bg=COLOR6,fg=COLOR1).grid(row=8,column=1)
Button(frm_airplane_iran ,text ='Back'             ,activebackground=COLOR5,command=back               ,bg=COLOR6,fg=COLOR1).grid(row=8,column=3)
Button(frm_Bus           ,text ='Confirm Operation',activebackground=COLOR7,command=save_bus           ,bg=COLOR7,fg=COLOR1).grid(row=6,column=1)
Button(frm_Bus           ,text ='Back'             ,activebackground=COLOR7,command=back               ,bg=COLOR7,fg=COLOR1).grid(row=6,column=3)                  
Button(frm_train         ,text ='Confirm Operation',activebackground=COLOR8,command=save_train         ,bg=COLOR8,fg=COLOR1).grid(row=6,column=1)
Button(frm_train         ,text ='Back'             ,activebackground=COLOR8,command=back               ,bg=COLOR8,fg=COLOR1).grid(row=6,column=3) 
Button(frm_hotel_iran    ,text ='Confirm Operation',activebackground=COLOR9,command=save_hotel_iran    ,bg=COLOR9,fg=COLOR1).grid(row=8,column=1)
Button(frm_hotel_iran    ,text ='Back'             ,activebackground=COLOR9,command=back               ,bg=COLOR9,fg=COLOR1).grid(row=8,column=3) 
Button(frm_hotel_world   ,text='Confirm Operation' ,activebackground=COLOR10,command=save_hotel_world   ,bg=COLOR10,fg=COLOR1).grid(row=8,column=1)
Button(frm_hotel_world   ,text='Back'              ,activebackground=COLOR10,command=back               ,bg=COLOR10,fg=COLOR1).grid(row=8,column=3)                                                     
#******************************************************* FINISH APP FO CODES ******************************************************************************************************************
login.mainloop()
#*********************************************************************** END ******************************************************************************************************************