#with shortened code
from tkinter import*
from tkinter import ttk
import mysql.connector
connection=mysql.connector.connect(host='localhost',user='vaidu',password='vaiducomp',database='sem1proj')
cursor=connection.cursor()
def screen1():
    global root
    root=Tk()
    root.title("Car Rental Management System")
    root.geometry("1200x800")
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome to Bon Voyage Rentals!", bg='black', fg='white', font=('Courier',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    btn1=Button(root,text="Rent a car",command=rent,bg="black",fg='white',font=('arial',15,'bold'))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    btn2=Button(root,text="Return a car",command=returns,bg="black",fg='white',font=('arial',15,'bold'))
    btn2.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    
    root.mainloop()


def rent():
    root.destroy()
    global screen2
    screen2=Tk()
    screen2.geometry("1200x800")
    screen2.title("Car Rentals")
    lb2=Label(screen2,text="Please fill in your specifications",bg="black",fg="white",font=("Segoe Print",20,'bold')).place(relx=0.33,rely=0.01)
    lb3=Label(screen2,text="Seater capacty",bg="black", fg="white",font=("Arial",15,'bold')).place(relx=0.03, rely=0.08)
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11
    var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11 =IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
    cb1= Checkbutton(screen2,text="5-seater", variable=var1,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.12)
    cb2= Checkbutton(screen2,text="7-seater", variable=var2,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.16)
    cb3= Checkbutton(screen2,text="8-seater", variable=var3,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.20)
    '''
    cb1.deselect()
    cb2.deselect()
    cb3.deselect()
    '''
    
    lb4=Label(screen2,text="Pick-up Location",bg="black", fg="white",font=("Arial",15,'bold')).place(relx=0.03, rely=0.28)
    cb4= Checkbutton(screen2,text="Bellandur", variable=var4,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.32)
    cb5= Checkbutton(screen2,text="Shivajinagar", variable=var5,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.36)
    cb6= Checkbutton(screen2,text="Koramangala", variable=var6,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.40)
    cb7= Checkbutton(screen2,text="Banashankari", variable=var7,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.44)
    cb8= Checkbutton(screen2,text="Indiranagar", variable=var8,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.48)
    cb9= Checkbutton(screen2,text="Hsr Layout", variable=var9,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.52)
    lb5=Label(screen2,text="Driver Needed?",bg="black", fg="white",font=("Arial",15,'bold')).place(relx=0.03, rely=0.59)
    cb10= Checkbutton(screen2,text="Yes", variable=var10,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.63)
    cb11= Checkbutton(screen2,text="No", variable=var11,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.67)
    lb6=Label(screen2,text="Price Range",bg="black", fg="white",font=("Arial",15,'bold')).place(relx=0.03, rely=0.74)
    cb12= Checkbutton(screen2,text="2000-3000", variable=var4,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.78)
    cb13= Checkbutton(screen2,text="3000-4000", variable=var5,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.82)
    cb14= Checkbutton(screen2,text="4000-5000", variable=var6,font=('Calibri',14,'bold')).place(relx=0.03, rely=0.86)
    btn3= Button(screen2, text= "OK",font=('Calibri',15)).place(relx=0.9,rely=0.9)
    screen2.mainloop()

def returns():
    #root.destroy()
    screen3=Tk()
    screen3.geometry("1200x800")
    screen3.title("Car Returns")
    lbblablahgd=Label(screen3,text="Return a car",bg="black",fg="white",font=("arial",20,'bold')).pack()
    screen3.mainloop()



screen1()