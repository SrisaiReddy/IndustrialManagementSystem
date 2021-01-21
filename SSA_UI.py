from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import tkinter as tk
from tkinter import PhotoImage
from tkinter import font as tkfont
import re
from tkinter import StringVar, Entry, Frame, Listbox, Scrollbar
from tkinter.constants import *
import cx_Oracle 

access_flag="Y"
app="None"
userentered="None"

def autoscroll(sbar, first, last):
    """Hide and show scrollbar as needed."""
    first, last = float(first), float(last)
    if first <= 0 and last >= 1:
        sbar.grid_remove()
    else:
        sbar.grid()
    sbar.set(first, last)



class Login_Page:

    def __init__(self,root):
        self.root=root
        self.root.title("Sri Siva Chaitanya Agro Login Page")
        self.root.geometry("1920x1080+0+0")

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=220,y=200,height=240,width=350)
        
        title=Label(Frame_login,text="Login Here",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=15,y=10)
        #i=IntVar()
        def caps(event):
            v.set(v.get().upper())
        v= StringVar()
        #r1 = Radiobutton(Frame_login, text="Admin", value=1,font=("Edo",12,"normal"), variable=i,fg="grey",bg="white").place(x=25,y=80)
        #r2 = Radiobutton(Frame_login, text="Employee", value=2,font=("Edo",12,"normal"),variable=i,fg="grey",bg="white").place(x=125,y=80)
        lbl_user=Label(Frame_login,text="Username",font=("Comfortaa",12,"bold"),fg="grey",bg="white").place(x=15,y=70)

        self.txt_user=Entry(Frame_login,font=("times new roman",15),fg="black",bg="lightgrey",textvariable=v)
        self.txt_user.place(x=15,y=100,width=320,height=35)
        self.txt_user.bind("<KeyRelease>",caps)


        lbl_pass=Label(Frame_login,text="Password",font=("Comfortaa",12,"bold"),fg="grey",bg="white").place(x=15,y=140)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),fg="black",bg="lightgrey",show="*")
        self.txt_pass.place(x=15,y=170,width=320,height=35)
        login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login Here",fg="white",bg="#d77337",bd=1,font=("Trajan Pro",12)).place(x=240,y=420,width=180,height=40)

    def login_function(self):
            
            if self.txt_pass.get()=="" or self.txt_user.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root).place(x=550,y=150)
            else:
                user_cred=self.txt_user.get()
                pass_cred=self.txt_pass.get()
                con = cx_Oracle.connect('SSAGRO/SSAGRO')
                cursor = con.cursor()
                cursor.execute("select * from SS_USER_ACCESS")
                raw=cursor.fetchall()
                cred_flag=0
                for i in raw:
                    if(i[0]==user_cred and i[1]!=pass_cred):
                        cred_flag=1
                        messagebox.showerror("Error 404","Recheck your password")
                    elif(i[0]!=user_cred and i[1]==pass_cred):
                        cred_flag=1
                        messagebox.showerror("Error 404","Recheck your username")
                    elif(i[0]==user_cred and i[1]==pass_cred):
                        cred_flag=1
                        if(i[3]=="N"):
                            messagebox.showerror("Error 404","You are no longer an active user. Please contact Admin")
                        else:
                            root.destroy()
                            global userentered
                            userentered=i[0]
                            global access_flag
                            access_flag=i[4]
                            global app
                            app = SampleApp()
                            app.wm_attributes('-fullscreen','true')
                            app.state("zoomed")
                            marquee = Marquee(app, text="Sri Siva Chaitanya Agro Industries, Anaparthi.", borderwidth=0, relief="sunken",fps=100)
                            marquee.pack(side="top", fill="x",pady=0)
                            cursor.close()
                            app.mainloop()


                        break
                if cred_flag==0:
                    messagebox.showerror("Error 404","Account doesn't exist")
                            
           
class GradientFrame(tk.Canvas):
       #'''A gradient frame which uses a canvas to draw the background'''
        def __init__(self, parent, color1="red", color2="black", **kwargs):
            tk.Canvas.__init__(self, parent, **kwargs)
            self._color1 = color1
            self._color2 = color2
            self.bind("<Configure>", self._draw_gradient)

        def _draw_gradient(self, event=None):
            '''Draw the gradient'''
            self.delete("gradient")
            width = self.winfo_width()
            height = self.winfo_height()
            limit = width
            (r1,g1,b1) = self.winfo_rgb(self._color1)
            (r2,g2,b2) = self.winfo_rgb(self._color2)
            r_ratio = float(r2-r1) / limit
            g_ratio = float(g2-g1) / limit
            b_ratio = float(b2-b1) / limit

            for i in range(limit):
                nr = int(r1 + (r_ratio * i))
                ng = int(g1 + (g_ratio * i))
                nb = int(b1 + (b_ratio * i))
                color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
                self.create_line(i,0,i,height, tags=("gradient",), fill=color)
            self.lower("gradient")

class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)        

        label = tk.Label(self, text="This is the start page",font=("Trajan Pro",16), bg="#dbd4b4", width="300", height="1",relief="sunken")
        label.pack(side="top", fill="x", pady=0)
        Frame_login=tk.Frame(self,bg="white")
        Frame_login.place(x=50,y=150,height=340,width=400)
        Login_Gr=GradientFrame(Frame_login,"#7aa1d2","#cc95c0", borderwidth=0, relief="sunken")
        Login_Gr.place(x=0,y=0,height=340,width=400)

        if (access_flag=="Y"):
                button1 = tk.Button(Frame_login, text="Admin Portal",
                                        command=lambda: controller.show_frame("PageOne"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button2 = tk.Button(Frame_login, text="Stocks",
                                        command=lambda: controller.show_frame("PageTwo"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button3 = tk.Button(Frame_login, text="Purchase",
                                        command=lambda: controller.show_frame("PageThree"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button4 = tk.Button(Frame_login, text="Sales",
                                        command=lambda: controller.show_frame("PageFour"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button5 = tk.Button(Frame_login, text="Expenditure",
                                        command=lambda: controller.show_frame("PageFive"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
        else:
                button1 = tk.Button(Frame_login, text="Create Employee",
                                        command=lambda: controller.show_frame("PageOne"),fg="white",font=("Trajan Pro",12),cursor="hand2",state="disabled")
                button2 = tk.Button(Frame_login, text="stocks",
                                        command=lambda: controller.show_frame("PageTwo"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button3 = tk.Button(Frame_login, text="Purchase",
                                        command=lambda: controller.show_frame("PageThree"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button4 = tk.Button(Frame_login, text="Sales",
                                        command=lambda: controller.show_frame("PageFour"),fg="white",bg="#d77337",font=("Trajan Pro",12),cursor="hand2")
                button5 = tk.Button(Frame_login, text="Expenditure",
                                        command=lambda: controller.show_frame("PageFive"),fg="white",font=("Trajan Pro",12),cursor="hand2",state="disabled")
                 

        button1.place(x=100,y=50,width=200,height=40)
        button2.place(x=100,y=100,width=200,height=40)
        button3.place(x=100,y=150,width=200,height=40)
        button4.place(x=100,y=200,width=200,height=40)
        button5.place(x=100,y=250,width=200,height=40)

        #filename_1= PhotoImage(file = "C:/Users/MrShree/Desktop/Python Projects/Logout.png")
        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1250,y=47,width=100,height=40)
        
    def logout(self):
        app.destroy()
        


class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps

        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)

        # start the animation
        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)

        self.after_id = self.after(int(1000/self.fps), self.animate)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        button = tk.Button(self, text="Go Back",bd=0,bg="#FEC194",font=("Trajan Pro",10),fg="white",
                           command=lambda: controller.show_frame("StartPage"),cursor="hand2")
        button.place(x=5,y=5,width=100,height=35)

        tab_control = ttk.Notebook(self)

        tab1 = ttk.Frame(tab_control)     
        Login_Gr=GradientFrame(tab1,"#7aa1d2","#cc95c0", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        self.insert_frame=Frame(Login_Gr,bg="white")
        self.insert_frame.place(x=50,y=65,height=500,width=400)
        title=Label(self.insert_frame,text="NEW EMPLOYEE",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=100,y=10)
        Label(self.insert_frame,text="Username",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=83)
        def caps(event):
            V2.set(V2.get().upper())
        V2 = StringVar()
        self.user_id=Entry(self.insert_frame,font=("times new roman",10),fg="black",bg="white",textvariable = V2)
        self.user_id.place(x=194,y=89,height=20,width=140)
        self.user_id.bind("<KeyRelease>", caps)
        check = Button(self.insert_frame,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.verify_userid)
        check.place(x=253,y=120,height=25,width=80)
        Label(self.insert_frame,text="Display Name",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=153)   
        Label(self.insert_frame,text="Enter Password",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=203)
        Label(self.insert_frame,text="Confirm Password",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=253)
        Label(self.insert_frame,text="Account Type",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=303)
        Label(self.insert_frame,text="Access",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=353)

        self.username=Entry(self.insert_frame,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.username.place(x=200,y=162,height=20,width=140)
        self.password=Entry(self.insert_frame,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.password.place(x=200,y=212,height=20,width=140)
        self.con_password=Entry(self.insert_frame,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.con_password.place(x=200,y=262,height=20,width=140)
        self.access_flag = ttk.Combobox(self.insert_frame, width = 27, values =["Admin","Employee"],state="disabled") 
  
# Adding combobox drop down list 
  
        self.access_flag.place(x=200,y=312,width=140,height=20)
        self.access_flag.bind("<<ComboboxSelected>>", self.justamethod)
        self.access_flag.current()  # default value
        # def sel():
        #     self.selection = str(var.get())
        # var = IntVar()
        self.active = ttk.Combobox(self.insert_frame, width = 27, values =["Yes","No"],state="disabled")
        self.active.place(x=200,y=362,width=140,height=20)
        self.active.bind("<<ComboboxSelected>>", self.justamethod1)
        self.active.current()

        self.btn_save = tk.Button(self.insert_frame,text='Add Employee',font=("Comfortaa",8),fg="black",bg="lightgrey",borderwidth=0,state="disabled",command=self.add_employee)
        self.btn_save.place(x=237,y=410,width=105,height=25)

        # Radiobutton(inside_frame1, text="YES", value=1,font=("Edo",12,"normal"), variable=var,fg="black",bg="white",command=sel).place(x=200,y=385)
        # Radiobutton(inside_frame1, text="NO", value=2,font=("Edo",12,"normal"),variable=var,fg="black",bg="white", command=sel).place(x=300,y=385)

        self.display_insert=Frame(Login_Gr,bg="white")
        self.display_insert.place(x=500,y=65,height=500,width=600)
        title=Label(self.display_insert,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)


        



        tab2 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(tab2,"#FBD786","#f7797d", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        update_frame=Frame(Login_Gr,bg="white")
        update_frame.place(x=50,y=65,height=500,width=400)

        display_update=Frame(Login_Gr,bg="white")
        display_update.place(x=500,y=65,height=500,width=600)
        title=Label(display_update,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)
        display_update_1=Frame(display_update,bg="white")
        display_update_1.place(x=40,y=93,height=400,width=510)     
        
        title=Label(update_frame,text="Update Here",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=100,y=10)
        Label(update_frame,text="Username",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=83)
        search_label=Frame(update_frame,bg="white")
        search_label.place(x=170,y=90,height=60,width=200)

        con = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con.cursor()
        cursor.execute("select * from SS_USER_ACCESS")
        raw=cursor.fetchall()
        list_of_items=[]
        for i in raw:
            list_of_items.append(i[0])
            
                
        # for i in raw:
        #     list_of_items.append(str(i))
        combobox_autocomplete = Combobox_Autocomplete(search_label, list_of_items, highlightthickness=1)
        combobox_autocomplete.pack()
        combobox_autocomplete.focus()
        self.usernameforupdate=""
        self.userpasswordforupdate=""
        self.useraccessforupdate=""
        self.useractiveforupdate="Y"
        self.useridforupdate=""
        self.aflag=""
        self.accounttype=""
        self.chosen_option=""
        self.chosen_option1=""
        self.variable=""
        def p():
            useridforupdate=combobox_autocomplete.get_value()
            travel_flag=0
            if(useridforupdate==""):
                travel_flag=1
                self.update_name.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
                self.update_pass.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))

                self.save_button.config(state="disabled",bg="lightgrey")
                self.del_button.config(state="disabled",bg="lightgrey")
                self.drop_menu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
                self.drop_menu_1.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
                messagebox.showerror("Error 404","Username Required")
            else:
                cursor.execute("select * from SS_USER_ACCESS")
                masteruser=cursor.fetchall()
                for i in masteruser:
                    if(useridforupdate==i[0]):
                        travel_flag=1
                        cursor.execute("select * from SS_USER_ACCESS where USER_ID = '"+useridforupdate+"'")
                        data=cursor.fetchone()
                        self.save_button.config(state="normal",bg="#b0f28a")
                        self.del_button.config(state="normal",bg="#f23041")
                        # for data in maindata:
                        self.useridforupdate=data[0]
                        self.usernameforupdate=data[2]
                        self.userpasswordforupdate=data[1]
                        self.useraccessforupdate=data[4]
                        self.useractiveforupdate=data[3]
                        datausername=StringVar(update_frame,self.usernameforupdate)
                        datapassword=StringVar(update_frame,self.userpasswordforupdate)
                        dataaccess=self.useraccessforupdate
                        dataactive=self.useractiveforupdate
                        self.update_name.config(state="normal",bg="white",textvariable=datausername)
                        self.update_pass.config(state="normal",bg="white",textvariable=datapassword)
                        self.drop_menu_1.config(state="normal",borderwidth=0)
                        if(dataactive=="Y"):
                            self.drop_menu_1.config(bg="#d4fca9")
                            dataactive="Active"
                            
                        elif(dataactive=="N"):
                            
                            self.drop_menu_1.config(bg="#f59387")
                            dataactive="InActive"
                            
                        var1.set(dataactive)

                        self.drop_menu.config(state="normal",borderwidth=0)
                        if(dataaccess=="Y"):
                            self.drop_menu.config(bg="#d4fca9")
                            dataaccess="Admin"
                        elif(dataaccess=="N"):
                            self.drop_menu.config(bg="#f59387")
                            dataaccess="Employee"
                        var.set(dataaccess)
                        print(var.get())
                        print(var1.get())

                        
                        

                        # if(self.useractiveforupdate=="Y"):
                        #     self.update_active1.select()
                        #     self.update_active2.deselect()
                        # elif(self.useractiveforupdate=="N"):
                        #     self.update_active1.deselect()
                        #     self.update_active2.select()



                        break

            if(travel_flag==0):
                     
                self.update_name.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
                self.update_pass.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
                self.save_button.config(state="disabled",bg="lightgrey")
                self.drop_menu_1.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
                self.drop_menu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
                self.del_button.config(state="disabled",bg="lightgrey")
                messagebox.showerror("Error 404","Username not found")
        def grab_and_assign_1(event):
            option=var1.get()
            if(option=="Active"):
                self.chosen_option1 = "Y"
            elif(option=="InActive"):
                self.chosen_option1 = "N"

        def grab_and_assign(event):
            option1=var.get()
            if(option1=="Admin"):
                self.chosen_option = "Y"
            elif(option1=="Employee"):
                self.chosen_option = "N"


        def displaymodule():
            for widget in display_update.winfo_children():
                widget.destroy()
            
            title=Label(display_update,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)
            if(self.chosen_option!="" and self.chosen_option1!=""):
                cursor.execute("update SS_USER_ACCESS set PASS = '"+self.update_pass.get()+"',USER_NAME = '"+self.update_name.get()+"', ACTIVE = '"+self.chosen_option1+"', ACCESS_FLAG1 = '"+self.chosen_option+"' where USER_ID ='"+self.useridforupdate+"'")
            elif(self.chosen_option!="" and self.chosen_option1==""):
                cursor.execute("update SS_USER_ACCESS set PASS = '"+self.update_pass.get()+"',USER_NAME = '"+self.update_name.get()+"', ACTIVE = '"+self.useractiveforupdate+"', ACCESS_FLAG1 = '"+self.chosen_option+"' where USER_ID ='"+self.useridforupdate+"'")
            elif(self.chosen_option=="" and self.chosen_option1!=""):
                cursor.execute("update SS_USER_ACCESS set PASS = '"+self.update_pass.get()+"',USER_NAME = '"+self.update_name.get()+"', ACTIVE = '"+self.chosen_option1+"', ACCESS_FLAG1 = '"+self.useraccessforupdate+"' where USER_ID ='"+self.useridforupdate+"'")
            else:
                cursor.execute("update SS_USER_ACCESS set PASS = '"+self.update_pass.get()+"',USER_NAME = '"+self.update_name.get()+"', ACTIVE = '"+self.useractiveforupdate+"', ACCESS_FLAG1 = '"+self.useraccessforupdate+"' where USER_ID ='"+self.useridforupdate+"'")    
            
            con.commit()
            self.update_name.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.update_pass.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.save_button.config(state="disabled",bg="lightgrey")
            self.drop_menu_1.config(state="disabled",bg="lightgrey")
            var1.set("")
            self.drop_menu.config(state="disabled",bg="lightgrey")
            var.set("")
            self.del_button.config(state="disabled",bg="lightgrey")


            cursor.execute("select * from SS_USER_ACCESS")
            raw=cursor.fetchall()
            data_1=[]
            Access_Flag=""
            Active_Flag=""
            for i in raw:
                data_1.append(i)
                if(self.useridforupdate==i[0]):
                    Access_Flag=i[4]
                    Active_Flag=i[3]
            
            # if(Active_Flag=="Y"):
            #     self.drop_menu_1.config(bg="#d4fca9")
            #     self.variable="Active"
            #     var1.set(self.variable)
            # elif(Active_Flag=="N"):
            #     self.drop_menu_1.config(bg="#f59387")
            #     self.variable="InActive"
            #     var1.set(self.variable)
            # if(Access_Flag=="Y"):
            #     self.drop_menu.config(bg="#d4fca9")
            #     self.variable="Admin"
            #     var.set(self.variable)
            # elif(Access_Flag=="N"):
            #     self.drop_menu.config(bg="#f59387")
            #     self.variable="Employee"
            #     var.set(self.variable)


            display_update_1=Frame(display_update,bg="white")
            display_update_1.place(x=40,y=93,height=350,width=510)
            tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5), height = 20, show = "headings")
            #tree.place(x=100,y=100,height=500,width=500)
            tree.pack(fill="none", expand=True,side="top")
            tree.heading(1, text="User ID")
            tree.heading(2, text="Password")
            tree.heading(3, text="UserName")
            tree.heading(4, text="Activeness")
            tree.heading(5, text="Admin Account?")

            tree.column(1, width = 100)
            tree.column(2, width = 100)
            tree.column(3, width = 100)
            tree.column(4, width = 100)
            tree.column(5, width = 100)

            scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
            scroll.pack(side = 'right', fill = 'y')

            tree.configure(yscrollcommand=scroll.set)

            for val in data_1:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]) )

        # def justamethod(self, event):
        #     self.aflag = self.access_flag.get()
        #     print(self.aflag)
                            
        def deletemodule():
            MsgBox = tk.messagebox.askquestion ('Are you sure?','Confirm deleting the row?',icon = 'warning')
            if MsgBox == 'yes':
                cursor1=con.cursor()
                cursor1.execute("delete from SS_USER_ACCESS where USER_ID = '"+self.useridforupdate+"'")
                con.commit()
                cursor1.close()
                v=StringVar(update_frame,"")
        
                self.update_name.config(state="disabled",bg="lightgrey",textvariable=v)
                self.update_pass.config(state="disabled",bg="lightgrey",textvariable=v)
                self.save_button.config(state="disabled",bg="lightgrey")
                self.drop_menu_1.config(state="disabled",textvariable=v,bg="lightgrey")
                self.drop_menu.config(state="disabled",textvariable=v,bg="lightgrey")
                self.del_button.config(state="disabled",bg="lightgrey")
                cursor.execute("select * from SS_USER_ACCESS")
                raw=cursor.fetchall()
                data_1=[]
                Access_Flag=""
                Active_Flag=""
                for i in raw:
                    data_1.append(i)

                
                # if(Active_Flag=="Y"):
                #     self.drop_menu_1.config(bg="#d4fca9")
                #     self.variable="Active"
                    
                # elif(Active_Flag=="N"):
                #     self.drop_menu_1.config(bg="#f59387")
                #     self.variable="InActive"
                    
                # if(Access_Flag=="Y"):
                #     self.drop_menu.config(bg="#d4fca9")
                #     self.variable="Admin"
                    
                # elif(Access_Flag=="N"):
                #     self.drop_menu.config(bg="#f59387")
                #     self.variable="Employee"
                    


                display_update_1=Frame(display_update,bg="white")
                display_update_1.place(x=40,y=93,height=350,width=510)
                tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5), height = 25, show = "headings")
                #tree.place(x=100,y=100,height=500,width=500)
                tree.pack(fill="none", expand=True,side="top")
                tree.heading(1, text="User ID")
                tree.heading(2, text="Password")
                tree.heading(3, text="UserName")
                tree.heading(4, text="Activeness")
                tree.heading(5, text="Admin Account?")

                tree.column(1, width = 100)
                tree.column(2, width = 100)
                tree.column(3, width = 100)
                tree.column(4, width = 100)
                tree.column(5, width = 100)

                # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
                # scroll.pack(side = 'right', fill = 'y')

                # tree.configure(yscrollcommand=scroll.set)

                for val in data_1:
                    tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]) )


            else:
                pass


        b = Button(update_frame,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",command=p,borderwidth=0)
        b.place(x=253,y=120,height=25,width=80)
        
        Label(update_frame,text="Display Name",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=153)   
        Label(update_frame,text="Password",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=223)
        Label(update_frame,text="Account Active",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=293)
        Label(update_frame,text="Account Type",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=363)

        self.update_name=Entry(update_frame,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.update_name.place(x=194,y=162,height=20,width=140)

        self.update_pass=Entry(update_frame,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.update_pass.place(x=194,y=232,height=20,width=140)
        #r1 = Radiobutton(Frame_login, text="Admin", value=1,font=("Edo",12,"normal"), variable=i,fg="grey",bg="white").place(x=25,y=80)
        i=IntVar()
        #self.update_active1=Radiobutton(update_frame,text="Yes",value=0,font=("Edo",12,"normal"),variable=i,fg="black",bg="white").place(x=224,y=301)
        #self.update_active2=Radiobutton(update_frame,text="No",value=1,font=("Edo",12,"normal"),variable=i,fg="black",bg="white").place(x=294,y=301)
        # n = tk.StringVar()
        var = StringVar(update_frame)
        var.set("")
        var1 = StringVar(update_frame)
        var1.set("")
        self.drop_menu_1 = OptionMenu(update_frame, var1,  "Active", "InActive",command=grab_and_assign_1)
        self.drop_menu_1.config(state="disabled",bg="lightgrey",borderwidth=0)
        self.drop_menu_1.place(x=214,y=299.5,width=120,height=25)
  
        self.drop_menu = OptionMenu(update_frame, var,  "Admin", "Employee",command=grab_and_assign)
        self.drop_menu.config(state="disabled",bg="lightgrey",borderwidth=0)
        self.drop_menu.place(x=214,y=369.5,width=120,height=25)
  
# Adding combobox drop down list 
        # self.access_flag["values"] = ["Admin","Employee"] 
        # self.access_flag.state="disabled"
        # self.access_flag.place(x=194,y=372,width=140,height=20)
        # self.access_flag.current()
        
        self.save_button=Button(update_frame,text="Save",font=("Comfortaa",8),fg="black",bg="lightgrey",command=displaymodule,borderwidth=0,state="disabled")
        self.save_button.place(x=253,y=422,height=25,width=80)

        self.del_button=Button(update_frame,text="Delete",font=("Comfortaa",8),fg="black",bg="lightgrey",command=deletemodule,borderwidth=0,state="disabled")
        self.del_button.place(x=30,y=422,height=25,width=80)

        # self.clear_button=Button(update_frame,text="Clear",font=("Comfortaa",8),fg="black",bg="lightgrey",command=destroyframe,borderwidth=0)
        # self.clear_button.place(x=30,y=422,height=25,width=80)

        tab3 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(tab3,"#009FFF","#ec2F4B", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        insert_cust=Frame(Login_Gr,bg="white")
        insert_cust.place(x=150,y=65,height=500,width=400)
        insert_cust_1=Frame(Login_Gr,bg="white")
        insert_cust_1.place(x=600,y=65,height=500,width=400)

        title=Label(insert_cust,text="NEW CUSTOMER",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=100,y=10)
        Label(insert_cust,text="Customer ID *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=83)
        def caps(event):
            V3.set(V3.get().upper())
        V3 = StringVar()
        self.cust_id=Entry(insert_cust,font=("times new roman",10),fg="black",bg="white",textvariable = V3)
        self.cust_id.place(x=194,y=89,height=20,width=140)
        self.cust_id.bind("<KeyRelease>", caps)
        self.check = Button(insert_cust,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.verify_custid)
        self.check.place(x=253,y=120,height=25,width=80)
        Label(insert_cust,text="Customer Name *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=153)   
        Label(insert_cust,text="Address",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=203)
        Label(insert_cust,text="Pin Code *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=303)
        Label(insert_cust,text="Phone 1 *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=353)
        Label(insert_cust,text="Phone 2",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=403)

        Label(insert_cust_1,text="Bank Account Number",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=20)   
        Label(insert_cust_1,text="IFSC Code",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=70)
        Label(insert_cust_1,text="Bank Name",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=120)
        Label(insert_cust_1,text="Bank Branch",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=170)
        Label(insert_cust_1,text="Customer Active *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=220)
        Label(insert_cust_1,text="Customer Type *",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=270)
        Label(insert_cust_1,text="Comments",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=320)

        self.custname=Entry(insert_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custname.place(x=200,y=162,height=20,width=140)
        self.address=Entry(insert_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.address.place(x=200,y=212,height=70,width=140)
        self.pincode=onlyNumber(insert_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.pincode.place(x=200,y=312,height=20,width=140)
        self.phone_1=onlyNumber(insert_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.phone_1.place(x=200,y=362,height=20,width=140)
        self.phone_2=onlyNumber(insert_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.phone_2.place(x=200,y=412,height=20,width=140)

        self.bankaccno=onlyNumber(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankaccno.place(x=215,y=29,height=20,width=140)
        self.bankIFSC=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankIFSC.place(x=215,y=79,height=20,width=140)
        self.bankname=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankname.place(x=215,y=129,height=20,width=140)
        self.bankbranch=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankbranch.place(x=215,y=179,height=20,width=140)
        # self.custactive=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custactive = ttk.Combobox(insert_cust_1, width = 27, values =["Active","InActive"],state="disabled") 
        self.custactive.place(x=215,y=229,height=20,width=140)
        self.custactive.bind("<<ComboboxSelected>>", self.cusjustamethod1)
        self.custactive.current()  # default value
        self.custtype = ttk.Combobox(insert_cust_1, width = 27, values =["Seller","Buyer","Both"],state="disabled") 
        self.custtype.place(x=215,y=279,height=20,width=140)
        self.custtype.bind("<<ComboboxSelected>>", self.cusjustamethod)
        self.custtype.current()
        #self.custtype=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")

        self.custcomments=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custcomments.place(x=45,y=360,height=70,width=310)

        self.cus_save = tk.Button(insert_cust_1,text='Add Customer',font=("Comfortaa",8),fg="black",bg="lightgrey",borderwidth=0,state="disabled",command=self.add_customer)
        self.cus_save.place(x=242,y=460,width=105,height=25)


        
        tab4 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(tab4,"#7aa1d2","#cc95c0", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        self.update_cust=Frame(Login_Gr,bg="white")
        self.update_cust.place(x=150,y=65,height=500,width=400)
        self.update_cust_1=Frame(Login_Gr,bg="white")
        self.update_cust_1.place(x=600,y=65,height=500,width=400)

        Label(self.update_cust,text="Update Customer",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=75,y=10)
        Label(self.update_cust,text="Customer ID",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=83)
        search_label=Frame(self.update_cust,bg="white")
        search_label.place(x=170,y=90,height=60,width=200)


        con1 = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con1.cursor()
        cursor.execute("select * from SS_CUST_TABLE")
        raw=cursor.fetchall()
        list_of_custid=[]
        for i in raw:
            list_of_custid.append(i[0])
        
        self.custid_autocomplete=Combobox_Autocomplete(search_label,list_of_custid,highlightthickness=1)
        self.custid_autocomplete.pack()
        self.custid_autocomplete.focus()
        self.checkcustid = Button(self.update_cust,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.fetchcust)
        self.checkcustid.place(x=253,y=120,height=25,width=80)

        Label(self.update_cust,text="Customer Name",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=153)   
        Label(self.update_cust,text="Address",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=203)
        Label(self.update_cust,text="Pin Code",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=303)
        Label(self.update_cust,text="Phone 1",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=353)
        Label(self.update_cust,text="Phone 2",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=403)

        Label(self.update_cust_1,text="Bank Account Number",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=20)   
        Label(self.update_cust_1,text="IFSC Code",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=70)
        Label(self.update_cust_1,text="Bank Name",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=120)
        Label(self.update_cust_1,text="Bank Branch",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=170)
        Label(self.update_cust_1,text="Customer Active",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=220)
        Label(self.update_cust_1,text="Customer Type",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=270)
        Label(self.update_cust_1,text="Comments",font=("Comfortaa",10),bg="white",fg="Grey").place(x=45,y=320)

        self.custnameup=Entry(self.update_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custnameup.place(x=200,y=162,height=20,width=140)
        self.addressup=Entry(self.update_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.addressup.place(x=200,y=212,height=70,width=140)
        self.pincodeup=Entry(self.update_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.pincodeup.place(x=200,y=312,height=20,width=140)
        self.phone_1up=Entry(self.update_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.phone_1up.place(x=200,y=362,height=20,width=140)
        self.phone_2up=Entry(self.update_cust,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.phone_2up.place(x=200,y=412,height=20,width=140)

        self.bankaccnoup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankaccnoup.place(x=215,y=29,height=20,width=140)
        self.bankIFSCup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankIFSCup.place(x=215,y=79,height=20,width=140)
        self.banknameup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.banknameup.place(x=215,y=129,height=20,width=140)
        self.bankbranchup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.bankbranchup.place(x=215,y=179,height=20,width=140)
        self.custactiveup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        # self.custactiveup= ttk.Combobox(update_cust_1, width = 27, values =["Active","InActive"],state="disabled") 
        self.custactiveup.place(x=215,y=229,height=20,width=140)
        # self.custactiveup.bind("<<ComboboxSelected>>", self.cusjustamethod)
        # self.custactive.current()  # default value
        # self.custtype = ttk.Combobox(insert_cust_1, width = 27, values =["Seller","Buyer","Both"],state="disabled") 
        self.custtypeup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custtypeup.place(x=215,y=279,height=20,width=140)
        # self.custtype.bind("<<ComboboxSelected>>", self.cusjustamethod1)
        # self.custtype.current()
        #self.custtype=Entry(insert_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")

        self.custcommentsup=Entry(self.update_cust_1,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.custcommentsup.place(x=45,y=360,height=70,width=310)

        self.cus_saveup = tk.Button(self.update_cust_1,text='Update Customer',font=("Comfortaa",8),fg="black",bg="lightgrey",borderwidth=0,state="disabled",command=self.update_customer)
        self.cus_saveup.place(x=237,y=460,width=115,height=25)

        self.tab5 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(self.tab5,"#FBD786","#f7797d", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        displaycust = Button(Login_Gr,text='Display Table',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.display_cust_table)
        displaycust.place(x=1010,y=20,height=25,width=80)
        self.display_cust=Frame(Login_Gr,bg="white")
        self.display_cust.place(x=70,y=55,height=500,width=1020)
        Label(Login_Gr,text="Customer ID",font=("Comfortaa",11),bg="#fbc284",fg="Grey").place(x=370,y=570)
        search_label=Frame(Login_Gr,bg="white")
        search_label.place(x=490,y=574,height=20,width=100)
        con = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con.cursor()
        cursor.execute("select * from SS_CUST_TABLE")
        raw1=cursor.fetchall()
        list_of_items1=[]
        for i in raw1:
            list_of_items1.append(i[0])
            
                
        # for i in raw:
        #     list_of_items.append(str(i))
        self.combobox_autocomplete_cust = Combobox_Autocomplete(search_label, list_of_items1, highlightthickness=1)
        self.combobox_autocomplete_cust.pack()
        self.combobox_autocomplete_cust.focus()
        
        
        self.del_cust=Button(Login_Gr,text="Delete",font=("Comfortaa",8),fg="black",bg="#b0f28a",command=self.cust_deletion,borderwidth=0)
        self.del_cust.place(x=620,y=570,height=25,width=80)

        
        
        tab6 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(tab6,"#009FFF","#ec2F4B", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        self.insert_prod=Frame(Login_Gr,bg="white")
        self.insert_prod.place(x=50,y=65,height=500,width=400)
        Label(self.insert_prod,text="NEW PRODUCT",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=100,y=10)
        Label(self.insert_prod,text="Product ID",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=83)
        def caps2(event):
            V1.set(V1.get().upper())
        V1 = StringVar()
        self.prod_id=Entry(self.insert_prod,font=("times new roman",10),fg="black",bg="white",textvariable = V1)
        self.prod_id.place(x=194,y=89,height=20,width=140)
        self.prod_id.bind("<KeyRelease>", caps2)
        prod_check = Button(self.insert_prod,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.verify_prodid)
        prod_check.place(x=253,y=120,height=25,width=80)
        Label(self.insert_prod,text="Product Name",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=153)   
        Label(self.insert_prod,text="Product Active",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=203)
        Label(self.insert_prod,text="Product Type",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=253)
        Label(self.insert_prod,text="Comments",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=303)

        self.prod_name=Entry(self.insert_prod,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prod_name.place(x=200,y=162,height=20,width=140)
        self.prod_active = ttk.Combobox(self.insert_prod, width = 27, values =["Yes","No"],state="disabled") 
  
# Adding combobox drop down list 
  
        self.prod_active.place(x=200,y=212,width=140,height=20)
        self.prod_active.bind("<<ComboboxSelected>>", self.justamethod2)
        self.prod_active.current()  # default value
        # def sel():
        #     self.selection = str(var.get())
        # var = IntVar()
        self.prod_type = onlyNumber(self.insert_prod,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prod_type.place(x=200,y=262,width=140,height=20)
        self.type_btn = tk.Button(self.insert_prod,text='?',font=("Comfortaa",8),fg="black",bg="lightgrey",borderwidth=0,state="disabled",command=self.type_info)
        self.type_btn.place(x=360,y=262,width=20,height=20)
        self.prod_comm = Entry(self.insert_prod,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prod_comm.place(x=200,y=312,height=75,width=140)
        self.prod_save = tk.Button(self.insert_prod,text='Add Product',font=("Comfortaa",8),fg="black",bg="lightgrey",borderwidth=0,state="disabled",command=self.add_product)
        self.prod_save.place(x=200,y=430,width=105,height=25)

        # Radiobutton(inside_frame1, text="YES", value=1,font=("Edo",12,"normal"), variable=var,fg="black",bg="white",command=sel).place(x=200,y=385)
        # Radiobutton(inside_frame1, text="NO", value=2,font=("Edo",12,"normal"),variable=var,fg="black",bg="white", command=sel).place(x=300,y=385)

        self.display_prod=Frame(Login_Gr,bg="white")
        self.display_prod.place(x=500,y=65,height=500,width=600)
        title=Label(self.display_prod,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)


        tab7 = ttk.Frame(tab_control)
        Login_Gr=GradientFrame(tab7,"#009FFF","#ec2F4B", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)
        self.updateproduct=Frame(Login_Gr,bg="white")
        self.updateproduct.place(x=50,y=65,height=500,width=400)
        title=Label(self.updateproduct,text="UPDATE PRODUCT",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=90,y=10)
        Label(self.updateproduct,text="Product Name",font=("Comfortaa",10),bg="white",fg="Grey").place(x=30,y=83)
        search_label=Frame(self.updateproduct,bg="white")
        search_label.place(x=170,y=90,height=60,width=200)

        conprod = cx_Oracle.connect('SSAGRO/SSAGRO')
        produpcursor = conprod.cursor()
        produpcursor.execute("select * from SS_PRO_TABLE")
        raw=produpcursor.fetchall()
        list_of_items=[]
        for i in raw:
            list_of_items.append(i[0])
            
                
        # for i in raw:
        #     list_of_items.append(str(i))
        self.combobox_autocomplete_prod = Combobox_Autocomplete(search_label, list_of_items, highlightthickness=1)
        self.combobox_autocomplete_prod.pack()
        self.combobox_autocomplete_prod.focus()
        self.checkprod = Button(self.updateproduct,text='Check',font=("Comfortaa",8),fg="black",bg="#b0f28a",borderwidth=0,command=self.verify_prodidfu)
        self.checkprod.place(x=253,y=120,height=25,width=80)
        Label(self.updateproduct,text="Product Name",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=153)   
        Label(self.updateproduct,text="Product Active",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=223)
        Label(self.updateproduct,text="Product Type",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=293)
        Label(self.updateproduct,text="Comments",font=("Comfortaa",12),bg="white",fg="Grey").place(x=30,y=363)

        self.prodnamefu=Entry(self.updateproduct,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prodnamefu.place(x=194,y=162,height=20,width=140)

        self.prodactfu=Entry(self.updateproduct,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prodactfu.place(x=194,y=232,height=20,width=140)

        self.prodtypefu=Entry(self.updateproduct,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prodtypefu.place(x=194,y=302,height=20,width=140)
        self.prodtypedisfu=Button(self.updateproduct,text="?",font=("Comfortaa",8),fg="black",bg="lightgrey",command=self.type_info,state="disabled",borderwidth=0)
        self.prodtypedisfu.place(x=339,y=302,height=20,width=20)
        self.prodcommentsfu=Entry(self.updateproduct,font=("times new roman",12),fg="black",bg="lightgrey",state="disabled")
        self.prodcommentsfu.place(x=194,y=372,height=20,width=140)


        self.save_produp=Button(self.updateproduct,text="Save",font=("Comfortaa",8),fg="black",bg="lightgrey",command=self.saveupdatedprod,borderwidth=0,state="disabled")
        self.save_produp.place(x=253,y=422,height=25,width=80)
        self.del_produp=Button(self.updateproduct,text="Delete",font=("Comfortaa",8),fg="black",bg="lightgrey",command=self.deleteprodfu,borderwidth=0,state="disabled")
        self.del_produp.place(x=30,y=422,height=25,width=80)

        self.display_productup=Frame(Login_Gr,bg="white")
        self.display_productup.place(x=500,y=65,height=500,width=600)
        title=Label(self.display_productup,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)
        

        tab_control.add(tab1, text='NEW USER CREATION')
        tab_control.add(tab2, text='EXISTING USER UPDATION')
        tab_control.add(tab3, text='NEW CUSTOMER CREATION')
        tab_control.add(tab4, text='EXISTING CUSTOMER UPDATION')
        tab_control.add(self.tab5, text='DISPLAY CUSTOMER')
        tab_control.add(tab6, text='NEW PRODUCT CREATION')
        tab_control.add(tab7, text='EXISTING PRODUCT UPDATION')

        
        tab_control.pack(expand=1, fill='both',padx=100,pady=50)


        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1262,y=5,width=100,height=40)

    def type_info(self):
        messagebox.showinfo("Info",'Product Type can only be as follows.\n''0. For Sales\n''1. For Purchase\n''2. For Both\n',parent=self).place(x=550,y=150)
    
    def justamethod2 (self, event):
        self.pactive = self.prod_active.get()  
    
    def saveupdatedprod(self):
        for widget in self.display_productup.winfo_children():
                widget.destroy()

        conprod=cx_Oracle.connect('SSAGRO/SSAGRO')
        produpcursor = conprod.cursor()
        produpcursor.execute("update SS_PRO_TABLE set PROD_NAME='"+self.prodnamefu.get()+"',PROD_ACTIVE='"+self.prodactfu.get()+"',PROD_TYPE='"+self.prodtypefu.get()+"',PROD_COMMENTS='"+self.prodcommentsfu.get()+"',PROD_UPDATEDBY='"+userentered+"' where PROD_ID='"+self.prodidforupdate+"'")
        conprod.commit()
        self.prodnamefu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
        self.prodactfu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
        self.prodtypefu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
        self.save_produp.config(state="disabled",bg="lightgrey")
        self.del_produp.config(state="disabled",bg="lightgrey")
        self.prodtypedisfu.config(state="disabled",bg="lightgrey")
        self.prodcommentsfu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
        title=Label(self.display_productup,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)
        produpcursor.execute("select * from SS_PRO_TABLE")
        raw=produpcursor.fetchall()
        data_1=[]
        for i in raw:
            data_1.append(i)
        display_update_1=Frame(self.display_productup,bg="white")
        display_update_1.place(x=40,y=93,height=350,width=510)
        tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5,6,7), height = 25, show = "headings")
        #tree.place(x=100,y=100,height=500,width=500)
        tree.pack(fill="none", expand=True,side="top")
        tree.heading(1, text="Product ID")
        tree.heading(2, text="Product Name")
        tree.heading(3, text="Active")
        tree.heading(4, text="Product Type")
        tree.heading(5, text="Created by")
        tree.heading(6, text="Updated by")
        tree.heading(7, text="Comments")

        tree.column(1, width = 70)
        tree.column(2, width = 70)
        tree.column(3, width = 70)
        tree.column(4, width = 70)
        tree.column(5, width = 70)
        tree.column(6, width = 70)
        tree.column(7, width = 70)
        # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
        # scroll.pack(side = 'right', fill = 'y')

        # tree.configure(yscrollcommand=scroll.set)

        for val in data_1:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6]) )


    def deleteprodfu(self):
        MsgBox = tk.messagebox.askquestion ('Are you sure?','Confirm deleting the row?',icon = 'warning')
        if MsgBox == 'yes':
            conprod = cx_Oracle.connect('SSAGRO/SSAGRO')
            produpcursor = conprod.cursor()
            produpcursor.execute("delete from SS_PRO_TABLE where PROD_ID = '"+self.prodidforupdate+"'")
            conprod.commit()
            self.prodnamefu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prodactfu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prodtypefu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.save_produp.config(state="disabled",bg="lightgrey")
            self.del_produp.config(state="disabled",bg="lightgrey")
            self.prodtypedisfu.config(state="disabled",bg="lightgrey")
            self.prodcommentsfu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")

            produpcursor.execute("select * from SS_PRO_TABLE")
            raw=produpcursor.fetchall()
            data_1=[]
            for i in raw:
                data_1.append(i)
            display_update_1=Frame(self.display_productup,bg="white")
            display_update_1.place(x=40,y=93,height=350,width=510)
            tree = ttk.Treeview(self.display_productup, columns = (1,2,3,4,5,6,7), height = 25, show = "headings")
            #tree.place(x=100,y=100,height=500,width=500)
            tree.pack(fill="none", expand=True,side="top")
            tree.heading(1, text="Product ID")
            tree.heading(2, text="Product Name")
            tree.heading(3, text="Active")
            tree.heading(4, text="Product Type")
            tree.heading(5, text="Created by")
            tree.heading(6, text="Updated by")
            tree.heading(7, text="Comments")

            tree.column(1, width = 70)
            tree.column(2, width = 70)
            tree.column(3, width = 70)
            tree.column(4, width = 70)
            tree.column(5, width = 70)
            tree.column(6, width = 70)
            tree.column(7, width = 70)
            # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
            # scroll.pack(side = 'right', fill = 'y')

            # tree.configure(yscrollcommand=scroll.set)

            for val in data_1:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6]) )


        else:
            pass

    def verify_prodid(self):
        name_entered = self.prod_id.get()
        con = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM SS_PRO_TABLE") 
        info = cursor.fetchall()
        flag =0
        for row in info:
            if row[0] == name_entered:
                flag =1
                messagebox.showerror("Info","Product ID already exist",parent=self).place(x=550,y=150)
                break
        if flag == 0:
            self.prod_name.config(state="normal",bg="white")
            self.prod_active.config(state="normal")
            self.prod_type.config(state="normal",bg="white")
            self.prod_comm.config(state="normal",bg="white")
            self.type_btn.config(state="normal",bg="#b0f28a")
            self.prod_save.config(state="normal",bg="#b0f28a")
            messagebox.showinfo("Info","Username Available",parent=self).place(x=550,y=150)
 
    def add_product(self):
        pid_entered = self.prod_id.get()
        prodname_entered = self.prod_name.get()
        active_entered = self.pactive
        type_entered = self.prod_type.get()
        comm_entered = self.prod_comm.get()
        print(active_entered)
        if active_entered == "yes":
            active_entered = "Y"
        else:
            active_entered ="N"
        
        
        if pid_entered =="" or prodname_entered =="" or active_entered =="" or type_entered =="":
            messagebox.showerror("Error","all credentials needed",parent=self).place(x=550,y=150)
        

        else:
            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("insert into SS_PRO_TABLE(PROD_ID, PROD_NAME, PROD_ACTIVE, PROD_TYPE, PROD_CREATEDBY,PROD_UPDATEDBY,PROD_COMMENTS) values('"+pid_entered+"','"+prodname_entered+"','"+active_entered+"','"+type_entered+"','"+userentered+"','"+userentered+"','"+comm_entered+"')")
            con.commit()
            cursor.close()
            con.close()
            #v=StringVar(self.insert_frame,"")
            self.prod_name.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prod_active.config(state="disabled",textvariable=StringVar(""))
            self.prod_type.config(state="disabled",textvariable=StringVar(""))
            self.prod_comm.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.type_btn.config(state="disabled",bg="lightgrey")
            self.prod_save.config(state="disabled",bg="lightgrey")
            for widget in self.display_prod.winfo_children():
                widget.destroy()
                
            title=Label(self.display_prod,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)



            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("select * from SS_PRO_TABLE")
            raw=cursor.fetchall()
            data_1=[]
            for i in raw:
                data_1.append(i)

            display_update_1=Frame(self.display_prod,bg="white")
            display_update_1.place(x=40,y=93,height=350,width=510)
            tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5,6,7), height = 25, show = "headings")
            #tree.place(x=100,y=100,height=500,width=500)
            tree.pack(fill="none", expand=True,side="top")
            tree.heading(1, text="PRODUCT ID")
            tree.heading(2, text="Product name")
            tree.heading(3, text="Product Active")
            tree.heading(4, text="Product Type")
            tree.heading(5, text="Created By")
            tree.heading(6, text="Updated BY")
            tree.heading(7, text="Comments")
            tree.column(1, width = 50)
            tree.column(2, width = 50)
            tree.column(3, width = 50)
            tree.column(4, width = 50)
            tree.column(5, width = 50)
            tree.column(6, width = 50)
            tree.column(7, width = 50)

            # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
            # scroll.pack(side = 'right', fill = 'y')

            # tree.configure(yscrollcommand=scroll.set)

            for val in data_1:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5],val[6]) )


    def verify_prodidfu(self):
        self.prodidforupdate=self.combobox_autocomplete_prod.get_value()
        prod_flag=0
        if(self.prodidforupdate==""):
            prod_flag=1
            self.prodnamefu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prodactfu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prodtypefu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.save_produp.config(state="disabled",bg="lightgrey")
            self.del_produp.config(state="disabled",bg="lightgrey")
            self.prodtypedisfu.config(state="disabled",bg="lightgrey")
            self.prodcommentsfu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            messagebox.showerror("Error 404","Username Required")
        else:
            conprod = cx_Oracle.connect('SSAGRO/SSAGRO')
            produpcursor = conprod.cursor()
            produpcursor.execute("select * from SS_PRO_TABLE")
            masteruser=produpcursor.fetchall()
            for i in masteruser:
                if(self.prodidforupdate==i[0]):
                    prod_flag=1
                    produpcursor.execute("select * from SS_PRO_TABLE where PROD_ID = '"+self.prodidforupdate+"'")
                    data=produpcursor.fetchone()
                    self.save_produp.config(state="normal",bg="#b0f28a")
                    self.del_produp.config(state="normal",bg="#f23041")
                    self.prodtypedisfu.config(state="normal",bg="#78b1eb")
                    # for data in maindata:
                    self.prodidfromdb=data[0]
                    prodactivefromdb=data[2]
                    prodnamefromdb=data[1]
                    prodcommentsfromdb=data[6]
                    prodtypefromdb=data[3]
                    eprodnamefu=StringVar(self.updateproduct,prodnamefromdb)
                    eprodactivefu=StringVar(self.updateproduct,prodactivefromdb)
                    eprodtypefu=StringVar(self.updateproduct,prodtypefromdb)
                    eprodcommentsfu=StringVar(self.updateproduct,prodcommentsfromdb)

                    self.prodnamefu.config(state="normal",bg="white",textvariable=eprodnamefu)
                    self.prodactfu.config(state="normal",bg="white",textvariable=eprodactivefu)
                    self.prodtypefu.config(state="normal",bg="white",textvariable=eprodtypefu)
                    self.prodcommentsfu.config(state="normal",bg="white",textvariable=eprodcommentsfu)
                    break

        if(prod_flag==0):
                
            self.prodnamefu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.prodactfu.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.save_produp.config(state="disabled",bg="lightgrey")
            self.prodtypedisfu.config(state="disabled",bg="lightgrey")
            self.prodcommentsfu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.prodtypefu.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.del_produp.config(state="disabled",bg="lightgrey")
            messagebox.showerror("Error 404","Username not found")

    def justamethod (self, event):
        self.aflag = self.access_flag.get()  
    def justamethod1 (self, event):
        self.actflag = self.active.get()  
    def cusjustamethod (self, event):
        self.cusaflag = self.custtype.get()  
    def cusjustamethod1 (self, event):
        self.cusactflag = self.custactive.get()
    def fetchcust(self):
        self.custidforupdate=self.custid_autocomplete.get_value()
        travel_flag=0
        if(self.custidforupdate==""):
            travel_flag=1
            self.custnameup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.addressup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.pincodeup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.phone_1up.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.phone_2up.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankaccnoup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankIFSCup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankbranchup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.banknameup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custactiveup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custtypeup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custcommentsup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.cus_saveup.config(state="disabled")
            messagebox.showerror("Error 404","Customer ID Required")
        else:
            custcon=cx_Oracle.connect('SSAGRO/SSAGRO')
            custcur=custcon.cursor()
            custcur.execute("select * from SS_CUST_TABLE")
            mastercust=custcur.fetchall()
            for i in mastercust:
                if(self.custidforupdate==i[0]):
                    travelflag=1
                    custcur.execute("select * from SS_CUST_TABLE where CUST_ID = '"+self.custidforupdate+"'")
                    data=custcur.fetchone()
                    self.cus_saveup.config(state="normal",bg="#b0f28a")
                    
                    self.cifu=data[0]
                    self.cnfu=data[1]
                    self.cafu=data[2]
                    self.cpinfu=data[3]
                    self.cphone1fu=data[4]
                    self.cphone2fu=data[5]
                    self.cbafu=data[6]
                    self.cbifscfu=data[7]
                    self.cbbranchfu=data[8]
                    self.cbnfu=data[9]
                    self.cactivefu=data[10]
                    self.ctypefu=data[11]
                    self.ccommentsfu=data[12]
                    self.cupdatedby=userentered

                    custnamefd=StringVar(self.update_cust,self.cnfu)
                    custaddfd=StringVar(self.update_cust,self.cafu)
                    custpinfd=StringVar(self.update_cust,self.cpinfu)
                    custphone1fd=StringVar(self.update_cust,self.cphone1fu)
                    custphone2fd=StringVar(self.update_cust,self.cphone2fu)
                    custbankaccfd=StringVar(self.update_cust_1,self.cbafu)
                    custbankifscfd=StringVar(self.update_cust_1,self.cbifscfu)
                    custbankbranchfd=StringVar(self.update_cust_1,self.cbbranchfu)
                    custbanknamefd=StringVar(self.update_cust_1,self.cbnfu)
                    custactivefd=StringVar(self.update_cust_1,self.cactivefu)
                    custtypefd=StringVar(self.update_cust_1,self.ctypefu)
                    custcomfd=StringVar(self.update_cust_1,self.ccommentsfu)
                    self.custnameup.config(state="normal",bg="white",textvariable=custnamefd)
                    self.addressup.config(state="normal",bg="white",textvariable=custaddfd)
                    self.pincodeup.config(state="normal",bg="white",textvariable=custpinfd)
                    self.phone_1up.config(state="normal",bg="white",textvariable=custphone1fd)
                    self.phone_2up.config(state="normal",bg="white",textvariable=custphone2fd)
                    self.bankaccnoup.config(state="normal",bg="white",textvariable=custbankaccfd)
                    self.bankIFSCup.config(state="normal",bg="white",textvariable=custbankifscfd)
                    self.bankbranchup.config(state="normal",bg="white",textvariable=custbankbranchfd)
                    self.banknameup.config(state="normal",bg="white",textvariable=custbanknamefd)
                    self.custactiveup.config(state="normal",bg="white",textvariable=custactivefd)
                    self.custtypeup.config(state="normal",bg="white",textvariable=custtypefd)
                    self.custcommentsup.config(state="normal",bg="white",textvariable=custcomfd)

    def update_customer(self):
        custnamefu=self.custnameup.get()
        pincodefu=self.pincodeup.get()
        print(pincodefu)
        phone1fu=self.phone_1up.get()
        custactivefu=self.custactiveup.get()
        custtypefu=self.custtypeup.get()
        if(custnamefu==""or custactivefu=="" or custtypefu==""):
            # or pincodefu=="" or phone1fu=="" 
            if(custnamefu==""):messagebox.showerror("Error 404","Updated Customer Name cannot be empty")
            # elif(pincodefu==""):messagebox.showerror("Error 404","Updated Pincode cannot be empty")
            # elif(phone1fu==""):messagebox.showerror("Error 404","Updated Phone 1 cannot be empty")
            elif(custactivefu==""):messagebox.showerror("Error 404","Updated Active Status cannot be empty")
            elif(custtypefu==""):messagebox.showerror("Error 404","Updated Type cannot be empty")
        else:
            # if(self.custtypeup.get()!="0" or self.custtypeup.get()!="1" or self.custtypeup.get()!="2"):
            #     messagebox.showerror("Error 404",'Customer Type can only be 0,1,2.\n''0. Seller \n''1. Buyer \n''2. Both Seller and Buyer\n')
            #     self.custtypeup.config(textvariable=StringVar(""))
            #     return
            # if(self.custactiveup.get()!="Y" or self.custactiveup.get()!="N"):
            #     messagebox.showerror("Error 404",'Customer Activeness can only be 0,1.\n''Y. Active \n''N. InActive \n')
            #     return
            updateconnection=cx_Oracle.connect('SSAGRO/SSAGRO')
            updatecursor=updateconnection.cursor()
            updatecursor.execute("update SS_CUST_TABLE set CUST_NAME='"+self.custnameup.get()+"',CUST_ADDRESS='"+self.addressup.get()+"',CUST_PINCODE='"+self.pincodeup.get()+"',CUST_PHONE1='"+self.phone_1up.get()+"',CUST_PHONE2='"+self.phone_2up.get()+"',BANK_ACCTNO='"+self.bankaccnoup.get()+"',BANK_IFSC='"+self.bankIFSCup.get()+"',BANK_BRANCH='"+self.bankbranchup.get()+"',BANK_NAME='"+self.banknameup.get()+"',CUST_ACTIVE='"+self.custactiveup.get()+"',CUST_TYPE='"+self.custtypeup.get()+"',CUST_COMMENTS='"+self.custcommentsup.get()+"',CUST_UPDATEDBY='"+userentered+"' where CUST_ID='"+self.custidforupdate+"'")
            updateconnection.commit()
            messagebox.showinfo("Success","Update Successful")
            self.custnameup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.addressup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.pincodeup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.phone_1up.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.phone_2up.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankaccnoup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankIFSCup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.bankbranchup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.banknameup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custactiveup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custtypeup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.custcommentsup.config(state="disabled",textvariable=StringVar(""),bg="lightgrey")
            self.cus_saveup.config(state="disabled")

    def verify_custid(self):

        custname_entered = self.cust_id.get()
        if(custname_entered==""):

            self.custname.config(state="disabled",bg="lightgrey")
            self.address.config(state="disabled",bg="lightgrey")
            self.pincode.config(state="disabled",bg="lightgrey")
            self.phone_1.config(state="disabled",bg="lightgrey")
            self.phone_2.config(state="disabled",bg="lightgrey")
            self.bankaccno.config(state="disabled",bg="lightgrey")
            self.bankIFSC.config(state="disabled",bg="lightgrey")
            self.bankname.config(state="disabled",bg="lightgrey")
            self.bankbranch.config(state="disabled",bg="lightgrey")
            self.custtype.config(state="disabled")
            self.custactive.config(state="disabled")
            self.custcomments.config(state="disabled",bg="lightgrey")
            self.cus_save.config(state="disabled",bg="lightgrey")
            messagebox.showerror("Error 404","Customer_ID cannot be empty",parent=self)
        else:
            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("SELECT * FROM SS_CUST_TABLE") 
            info = cursor.fetchall()
            flag =0
            for row in info:
                if row[0] == custname_entered:
                    flag =1
                    messagebox.showerror("Info","Username already exist",parent=self)
                    break
            if flag == 0:
                self.custname.config(state="normal",bg="white")
                self.address.config(state="normal",bg="white")
                self.pincode.config(state="normal",bg="white")
                self.phone_1.config(state="normal",bg="white")
                self.phone_2.config(state="normal",bg="white")
                self.bankaccno.config(state="normal",bg="white")
                self.bankIFSC.config(state="normal",bg="white")
                self.bankname.config(state="normal",bg="white")
                self.bankbranch.config(state="normal",bg="white")
                self.custtype.config(state="normal")
                self.custactive.config(state="normal")
                self.custcomments.config(state="normal",bg="white")
                self.cus_save.config(state="normal",bg="#b0f28a")
                #self.btn_save.config(state="normal",bg="#b0f28a")
                messagebox.showinfo("Info","Username Available",parent=self)
                #self.check.config(command=lambda : self.controller.show_frame(self.tab5))
    def add_customer(self):
        custid_entered = self.cust_id.get()
        custname_entered = self.custname.get()
        address_entered = self.address.get()
        pincode_entered = self.pincode.get()
        phone1_entered = self.phone_1.get()
        phone2_entered= self.phone_2.get()
        bankacc_entered=self.bankaccno.get()
        bankIFSC_entered=self.bankIFSC.get()
        bankbranch_entered=self.bankbranch.get()
        bankname_entered=self.bankname.get()

        custtype_entered = self.cusaflag
        print(custtype_entered)
        #custaccessflag_entered="3"
        if custtype_entered == "Seller":
            custtype_entered="0"
        elif custtype_entered=="Buyer":
            custtype_entered="1"
        elif custtype_entered=="Both":
            custtype_entered="2"
    
        
        custactiveness_entered = self.cusactflag
        if custactiveness_entered == "Active":
            custactiveness_entered ="Y"
        elif custactiveness_entered == "InActive":
            custactiveness_entered ="N"
        comments_entered=self.custcomments.get()

        if custid_entered =="" or custname_entered =="" or custtype_entered =="" or pincode_entered =="" or phone1_entered =="" or custactiveness_entered == "":
            print(custid_entered)
            print(custname_entered)
            print(custtype_entered)
            print(pincode_entered)
            print(custactiveness_entered)
            print(phone1_entered)
            messagebox.showerror("Error","All * marked fields are mandatory",parent=self)
        # elif len(self.pincode.get())!=6:

        #     messagebox.showerror("Error 404","Pincode must have 6 digits. Please Re-Enter")
            
        # elif len(self.phone_1.get())!=10:

        #     messagebox.showerror("Error 404","Pincode must have 10 digits. Please Re-Enter")
            
        # elif(self.phone_2.get()!="" and len(self.phone_2.get())!=10):

        #     messagebox.showerror("Error 404","Pincode must have 10 digits. Please Re-Enter")
            
        else:
            con1 = cx_Oracle.connect('SSAGRO/SSAGRO')    
            custcursor = con1.cursor()
            if address_entered=="":
                address_entered="None"
            if phone2_entered=="":
                phone2_entered="0"
            if bankacc_entered=="":
                bankacc_entered="0"
            if bankIFSC_entered=="":
                bankIFSC_entered="None"
            if bankname_entered=="":
                bankname_entered="None"
            if bankbranch_entered=="":
                bankbranch_entered="None"
            if comments_entered=="":
                comments_entered="None"
            # phone1_entered=int(phone1_entered)
            # phone2_entered=int(phone2_entered)
            # pincode_entered=int(pincode_entered)
            # bankacc_entered=int(bankacc_entered)
            custcursor.execute("insert into SS_CUST_TABLE(CUST_ID,CUST_NAME,CUST_ADDRESS,CUST_PINCODE,CUST_PHONE1,CUST_PHONE2,BANK_ACCTNO,BANK_IFSC,BANK_BRANCH,BANK_NAME,CUST_ACTIVE,CUST_TYPE,CUST_COMMENTS,CUST_CREATEDBY,CUST_UPDATEDBY) values('"+custid_entered+"','"+custname_entered+"','"+address_entered+"','"+pincode_entered+"','"+phone1_entered+"','"+phone2_entered+"','"+bankacc_entered+"','"+bankIFSC_entered+"','"+bankbranch_entered+"','"+bankname_entered+"','"+custactiveness_entered+"','"+custtype_entered+"','"+comments_entered+"','"+userentered+"','"+userentered+"')")
            con1.commit()
            custcursor.close()
            con1.close()
            # v2=StringVar(self,"")
            self.custname.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.address.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.pincode.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.phone_1.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.phone_2.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.bankaccno.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.bankIFSC.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.bankname.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.bankbranch.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.custtype.config(state="disabled",textvariable=StringVar(""))
            self.custactive.config(state="disabled",textvariable=StringVar(""))
            self.custcomments.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.cus_save.config(state="disabled",bg="lightgrey")
            messagebox.showinfo("SuccessFull","Successfull")

    def verify_userid(self):
        name_entered = self.user_id.get()
        con = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM SS_USER_ACCESS") 
        info = cursor.fetchall()
        flag =0
        if(name_entered==""):
            self.username.config(state="disabled",bg="lightgrey")
            self.password.config(state="disabled",bg="lightgrey")
            self.con_password.config(state="disabled",bg="lightgrey")
            self.active.config(state="disabled")
            self.access_flag.config(state="disabled")
            self.btn_save.config(state="disabled",bg="lightgrey")
            messagebox.showerror("Error","Username cannot be NULL",parent=self).place(x=550,y=150)

        for row in info:
            if row[0] == name_entered:
                flag =1
                messagebox.showerror("Info","Username already exist",parent=self).place(x=550,y=150)
                break
        if flag == 0:
            self.username.config(state="normal",bg="white")
            self.password.config(state="normal",bg="white")
            self.con_password.config(state="normal",bg="white")
            self.active.config(state="normal")
            self.access_flag.config(state="normal")
            self.btn_save.config(state="normal",bg="#b0f28a")
            messagebox.showinfo("Info","Username Available",parent=self).place(x=550,y=150)


    def add_employee(self):
        name_entered = self.user_id.get()
        username_entered = self.username.get()
        password_entered = self.password.get()
        conpassword_entered = self.con_password.get()
        accessflag_entered = self.aflag
        if accessflag_entered == "Admin":
            accessflag_entered = "Y"
        else:
            accessflag_entered ="N"
        
        activeness_entered = self.actflag
        if activeness_entered == "Yes":
            activeness_entered ="Y"
        elif activeness_entered == "No":
            activeness_entered ="N"
        
        if name_entered =="" or username_entered =="" or password_entered =="" or conpassword_entered =="" or accessflag_entered =="":
            messagebox.showerror("Error","all credentials needed",parent=self).place(x=550,y=150)
        if password_entered != conpassword_entered:
            messagebox.showerror("Error","Password and Confirm Password are not same")

        else:
            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("insert into SS_USER_ACCESS(USER_ID, PASS, USER_NAME, ACTIVE, ACCESS_FLAG1) values('"+name_entered+"','"+password_entered+"','"+username_entered+"','"+activeness_entered+"','"+accessflag_entered+"')")
            con.commit()
            #v=StringVar(self.insert_frame,"")
            self.username.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.password.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.con_password.config(state="disabled",bg="lightgrey",textvariable=StringVar(""))
            self.active.config(state="disabled",textvariable=StringVar(""))
            self.access_flag.config(state="disabled",textvariable=StringVar(""))
            self.btn_save.config(state="disabled",bg="lightgrey")
            for widget in self.display_insert.winfo_children():
                widget.destroy()
                
            title=Label(self.display_insert,text="Data Display",font=("BigNoodleTitling",35,"bold"),bg="white",fg="Grey").place(x=340,y=10)



            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("select * from SS_USER_ACCESS")
            raw=cursor.fetchall()
            data_1=[]
            for i in raw:
                data_1.append(i)

            display_update_1=Frame(self.display_insert,bg="white")
            display_update_1.place(x=40,y=93,height=350,width=510)
            tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5), height = 25, show = "headings")
            #tree.place(x=100,y=100,height=500,width=500)
            tree.pack(fill="none", expand=True,side="top")
            tree.heading(1, text="User ID")
            tree.heading(2, text="Password")
            tree.heading(3, text="UserName")
            tree.heading(4, text="Activeness")
            tree.heading(5, text="Admin Account?")

            tree.column(1, width = 100)
            tree.column(2, width = 100)
            tree.column(3, width = 100)
            tree.column(4, width = 100)
            tree.column(5, width = 100)

            # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
            # scroll.pack(side = 'right', fill = 'y')

            # tree.configure(yscrollcommand=scroll.set)

            for val in data_1:
                tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4]) )

        # def justamethod(self, event):
        #     self.aflag = self.access_flag.get()
        #     print(self.aflag)
    def cust_deletion(self):
        custidfordeletion = self.combobox_autocomplete_cust.get_value()
        if custidfordeletion == "":
            messagebox.showerror("Error 404","customer ID Required")
        else:
            con = cx_Oracle.connect('SSAGRO/SSAGRO')
            cursor = con.cursor()
            cursor.execute("select * from SS_CUST_TABLE")
            raw1=cursor.fetchall()
            flag = 0
            for i in raw1:
                if i[0] == custidfordeletion:
                    flag=1
                    MsgBox = tk.messagebox.askquestion ('Are you sure?','Confirm deleting the row?',icon = 'warning')
                    if MsgBox == 'yes':
                        cursor1=con.cursor()
                        cursor1.execute("delete from SS_CUST_TABLE where CUST_ID = '"+custidfordeletion+"'")
                        con.commit()
                        cursor1.close()
            if flag == 0:
                messagebox.showerror("Error 404","customer ID does not exist")
        
        con1 = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con1.cursor()
        cursor.execute("select * from SS_CUST_TABLE")
        raw=cursor.fetchall()
        data_1=[]
        for i in raw:
            data_1.append(i)
        
        for widget in self.display_cust.winfo_children():
            widget.destroy()

        display_update_1=Frame(self.display_cust,bg="grey")
        display_update_1.place(x=0,y=0,height=500,width=1020)
        tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), height = 7, show = "headings")
        tree.place(x=0,y=0,height=500,width=1020)
        # tree.pack(fill="none", expand=True,side="top")
        style = ttk.Style() 
        style.configure('Treeview', rowheight=60)
        tree.heading(1, text="CUST_ID")
        tree.heading(2, text="NAME")
        tree.heading(3, text="ADDRESS")
        tree.heading(4, text="PINCODE")
        tree.heading(5, text="PHONE_1")
        tree.heading(6, text="PHONE_2")
        tree.heading(7, text="ACCOUNT NO")
        tree.heading(8, text="IFSC CODE")
        tree.heading(9, text="BANK BRANCH")
        tree.heading(10, text="BANK NAME")
        tree.heading(11, text="ACTIVE")
        tree.heading(12, text="CUST_TYPE")
        tree.heading(13, text="COMMENTS")
        tree.heading(14, text="CREATED_BY")
        tree.heading(15, text="UPDATED_BY")

        tree.column(1, width = 60)
        tree.column(2, width = 65)
        tree.column(3, width = 55)
        tree.column(4, width = 55)
        tree.column(5, width = 55)
        tree.column(6, width = 55)
        tree.column(7, width = 55)
        tree.column(8, width = 55)
        tree.column(9, width = 60)
        tree.column(10, width = 55)
        tree.column(11, width = 55)
        tree.column(12, width = 65)
        tree.column(13, width = 55)
        tree.column(14, width = 55)
        tree.column(15, width = 55)

        # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
        # scroll.pack(side = 'right', fill = 'y')

        # tree.configure(yscrollcommand=scroll.set)

        for val in data_1:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5], val[6], val[7],val[8],val[9],val[10], val[11], val[12],val[13],val[14]))
        con1.close()

        
    def logout(self):
        app.destroy()
    def display_cust_table(self):
    
        con = cx_Oracle.connect('SSAGRO/SSAGRO')
        cursor = con.cursor()
        cursor.execute("select * from SS_CUST_TABLE")
        raw=cursor.fetchall()
        data_1=[]
        for i in raw:
            data_1.append(i)

        display_update_1=Frame(self.display_cust,bg="grey")
        display_update_1.place(x=0,y=0,height=500,width=1020)
        tree = ttk.Treeview(display_update_1, columns = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), height = 7, show = "headings")
        tree.place(x=0,y=0,height=500,width=1020)
        # tree.pack(fill="none", expand=True,side="top")
        style = ttk.Style() 
        style.configure('Treeview', rowheight=60)
        tree.heading(1, text="CUST_ID")
        tree.heading(2, text="NAME")
        tree.heading(3, text="ADDRESS")
        tree.heading(4, text="PINCODE")
        tree.heading(5, text="PHONE_1")
        tree.heading(6, text="PHONE_2")
        tree.heading(7, text="ACCOUNT NO")
        tree.heading(8, text="IFSC CODE")
        tree.heading(9, text="BANK BRANCH")
        tree.heading(10, text="BANK NAME")
        tree.heading(11, text="ACTIVE")
        tree.heading(12, text="CUST_TYPE")
        tree.heading(13, text="COMMENTS")
        tree.heading(14, text="CREATED_BY")
        tree.heading(15, text="UPDATED_BY")

        tree.column(1, width = 60)
        tree.column(2, width = 65)
        tree.column(3, width = 55)
        tree.column(4, width = 55)
        tree.column(5, width = 55)
        tree.column(6, width = 55)
        tree.column(7, width = 55)
        tree.column(8, width = 55)
        tree.column(9, width = 60)
        tree.column(10, width = 55)
        tree.column(11, width = 55)
        tree.column(12, width = 65)
        tree.column(13, width = 55)
        tree.column(14, width = 55)
        tree.column(15, width = 55)

        # scroll = ttk.Scrollbar(display_update_1, orient="vertical", command=tree.yview)
        # scroll.pack(side = 'right', fill = 'y')

        # tree.configure(yscrollcommand=scroll.set)

        for val in data_1:
            tree.insert('', 'end', values = (val[0], val[1], val[2],val[3],val[4],val[5], val[6], val[7],val[8],val[9],val[10], val[11], val[12],val[13],val[14]))
    
class onlyNumber(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            if(self.get()==""):
                self.set("")
            else:
                self.set(self.old_value)    
    
    
class Combobox_Autocomplete(Entry, object):
    def __init__(self, master, list_of_items=None, autocomplete_function=None, listbox_width=None, listbox_height=7, ignorecase_match=False, startswith_match=True, vscrollbar=True, hscrollbar=True, **kwargs):
        if hasattr(self, "autocomplete_function"):
            if autocomplete_function is not None:
                raise ValueError("Combobox_Autocomplete subclass has 'autocomplete_function' implemented")
        else:
            if autocomplete_function is not None:
                self.autocomplete_function = autocomplete_function
            else:
                if list_of_items is None:
                    raise ValueError("If not given complete function, list_of_items can't be 'None'")

                if ignorecase_match:
                    if startswith_match:
                        def matches_function(entry_data, item):
                            return item.startswith(entry_data)
                    else:
                        def matches_function(entry_data, item):
                            return item in entry_data

                    self.autocomplete_function = lambda entry_data: [item for item in self.list_of_items if matches_function(entry_data, item)]
                else:
                    if startswith_match:
                        def matches_function(escaped_entry_data, item):
                            if re.match(escaped_entry_data, item, re.IGNORECASE):
                                return True
                            else:
                                return False
                    else:
                        def matches_function(escaped_entry_data, item):
                            if re.search(escaped_entry_data, item, re.IGNORECASE):
                                return True
                            else:
                                return False
                    
                    def autocomplete_function(entry_data):
                        escaped_entry_data = re.escape(entry_data)
                        return [item for item in self.list_of_items if matches_function(escaped_entry_data, item)]

                    self.autocomplete_function = autocomplete_function
                    
        #item=self.autocomplete_function
        self._listbox_height = int(listbox_height)
        self._listbox_width = listbox_width

        self.list_of_items = list_of_items
        
        self._use_vscrollbar = vscrollbar
        self._use_hscrollbar = hscrollbar

        kwargs.setdefault("background", "white")

        if "textvariable" in kwargs:
            self._entry_var = kwargs["textvariable"]
        else:
            self._entry_var = kwargs["textvariable"] = StringVar()

        Entry.__init__(self, master, **kwargs)

        self._trace_id = self._entry_var.trace('w', self._on_change_entry_var)
        
        self._listbox = None

        self.bind("<Tab>", self._on_tab)
        self.bind("<Up>", self._previous)
        self.bind("<Down>", self._next)
        self.bind('<Control-n>', self._next)
        self.bind('<Control-p>', self._previous)

        self.bind("<Return>", self._update_entry_from_listbox)
        self.bind("<Escape>", lambda event: self.unpost_listbox())
        
    def _on_tab(self, event):
        self.post_listbox()
        return "break"

    def _on_change_entry_var(self, name, index, mode):
        
        entry_data = self._entry_var.get()

        if entry_data == '':
            self.unpost_listbox()
            self.focus()
        else:
            values = self.autocomplete_function(entry_data)
            if values:
                if self._listbox is None:
                    self._build_listbox(values)
                else:
                    self._listbox.delete(0, END)

                    height = min(self._listbox_height, len(values))
                    self._listbox.configure(height=height)

                    for item in values:
                        self._listbox.insert(END, item)
                
            else:
                self.unpost_listbox()
                self.focus()

    def _build_listbox(self, values):
        listbox_frame = Frame()

        self._listbox = Listbox(listbox_frame, background="white", selectmode=SINGLE, activestyle="none", exportselection=False)
        self._listbox.grid(row=0, column=0,sticky = N+E+W+S)

        self._listbox.bind("<ButtonRelease-1>", self._update_entry_from_listbox)
        self._listbox.bind("<Return>", self._update_entry_from_listbox)
        self._listbox.bind("<Escape>", lambda event: self.unpost_listbox())
        
        self._listbox.bind('<Control-n>', self._next)
        self._listbox.bind('<Control-p>', self._previous)

        if self._use_vscrollbar:
            vbar = Scrollbar(listbox_frame, orient=VERTICAL, command= self._listbox.yview)
            vbar.grid(row=0, column=1, sticky=N+S)
            
            self._listbox.configure(yscrollcommand= lambda f, l: autoscroll(vbar, f, l))
            
        if self._use_hscrollbar:
            hbar = Scrollbar(listbox_frame, orient=HORIZONTAL, command= self._listbox.xview)
            hbar.grid(row=1, column=0, sticky=E+W)
            
            self._listbox.configure(xscrollcommand= lambda f, l: autoscroll(hbar, f, l))

        listbox_frame.grid_columnconfigure(0, weight= 1)
        listbox_frame.grid_rowconfigure(0, weight= 1)

        x = -self.cget("borderwidth") - self.cget("highlightthickness") 
        y = self.winfo_height()-self.cget("borderwidth") - self.cget("highlightthickness")

        if self._listbox_width:
            width = self._listbox_width
        else:
            width=self.winfo_width()

        listbox_frame.place(in_=self, x=x, y=y, width=width)
        
        height = min(self._listbox_height, len(values))
        self._listbox.configure(height=height)

        for item in values:
            self._listbox.insert(END, item)

    def post_listbox(self):
        if self._listbox is not None: return

        entry_data = self._entry_var.get()
        if entry_data == '': return

        values = self.autocomplete_function(entry_data)
        if values:
            self._build_listbox(values)

    def unpost_listbox(self):
        if self._listbox is not None:
            self._listbox.master.destroy()
            self._listbox = None

    def get_value(self):
        return self._entry_var.get()


    def set_value(self, text, close_dialog=False):
        self._set_var(text)

        if close_dialog:
            self.unpost_listbox()

        self.icursor(END)
        self.xview_moveto(1.0)
        
    def _set_var(self, text):
        self._entry_var.trace_vdelete("w", self._trace_id)
        self._entry_var.set(text)
        self._trace_id = self._entry_var.trace('w', self._on_change_entry_var)

    def _update_entry_from_listbox(self, event):
        if self._listbox is not None:
            current_selection = self._listbox.curselection()
            
            if current_selection:
                text = self._listbox.get(current_selection)
                self._set_var(text)

            self._listbox.master.destroy()
            self._listbox = None

            self.focus()
            self.icursor(END)
            self.xview_moveto(1.0)
            
        return "break"

    def _previous(self, event):
        if self._listbox is not None:
            current_selection = self._listbox.curselection()

            if len(current_selection)==0:
                self._listbox.selection_set(0)
                self._listbox.activate(0)
            else:
                index = int(current_selection[0])
                self._listbox.selection_clear(index)

                if index == 0:
                    index = END
                else:
                    index -= 1

                self._listbox.see(index)
                self._listbox.selection_set(first=index)
                self._listbox.activate(index)

        return "break"

    def _next(self, event):
        if self._listbox is not None:

            current_selection = self._listbox.curselection()
            if len(current_selection)==0:
                self._listbox.selection_set(0)
                self._listbox.activate(0)
            else:
                index = int(current_selection[0])
                self._listbox.selection_clear(index)
                
                if index == self._listbox.size() - 1:
                    index = 0
                else:
                    index +=1
                    
                self._listbox.see(index)
                self._listbox.selection_set(index)
                self._listbox.activate(index)
        return "break"




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)   
        button = tk.Button(self, text="Go Back",bd=0,bg="#FEC194",font=("Trajan Pro",10),fg="white",
                           command=lambda: controller.show_frame("StartPage"),cursor="hand2")
        button.place(x=5,y=5,width=100,height=35)

        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1262,y=5,width=100,height=40)
        
    def logout(self):
        app.destroy()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)   
        button = tk.Button(self, text="Go Back",bd=0,bg="#FEC194",font=("Trajan Pro",10),fg="white",
                           command=lambda: controller.show_frame("StartPage"),cursor="hand2")
        button.place(x=5,y=5,width=100,height=35)

        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1262,y=5,width=100,height=40)
        
    def logout(self):
        app.destroy()
        
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)   
        button = tk.Button(self, text="Go Back",bd=0,bg="#FEC194",font=("Trajan Pro",10),fg="white",
                           command=lambda: controller.show_frame("StartPage"),cursor="hand2")
        button.place(x=5,y=5,width=100,height=35)


        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1262,y=5,width=100,height=40)
        
    def logout(self):
        app.destroy()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Login_Gr=GradientFrame(self,"#FEC194","#FF0061", borderwidth=1, relief="sunken")
        Login_Gr.place(x=0,y=0,height=1080,width=1920)   
        button = tk.Button(self, text="Go Back",bd=0,bg="#FEC194",font=("Trajan Pro",10),fg="white",
                           command=lambda: controller.show_frame("StartPage"),cursor="hand2")
        button.place(x=5,y=5,width=100,height=35)
        button6 = tk.Button(self,text="Log Out",command=self.logout,fg="white",bg="red",font=("Trajan Pro",12),cursor="hand2")
        button6.place(x=1262,y=5,width=100,height=40)
        
    def logout(self):
        app.destroy()
      

root=Tk()
root.state("zoomed")
root.wm_attributes('-fullscreen','true')
Login_Gr=GradientFrame(root,"#3a1c71","#ffaf7b", borderwidth=1, relief="solid")
Login_Gr.place(x=0,y=0,height=1080,width=1920)
BGFrame=Frame(root)
BGFrame.place(x=42,y=24,height=725,width=1284)
filename= PhotoImage(file = "C:/Users/MrShree/Desktop/Python Projects/Comp.png")
background_label=Label(BGFrame,image=filename)
background_label.place(x=0, y=0)
obj=Login_Page(root)
root.mainloop()

