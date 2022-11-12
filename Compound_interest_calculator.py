from tkinter import *
def calculate_ci():
    principal=float(principal_field.get())
    rate=float(rate_field.get())
    year=int(year_field.get())
    CI=(principal)*(pow((1+rate/100),year))
    result_field.insert(5,CI)
def clear_all():
    principal_field.delete(0,END)
    rate_field.delete(0,END)
    year_field.delete(0,END)
    result_field.delete(0,END)
    principal_field.focus_set()
if __name__=="__main__":
    root=Tk()
    root.minsize(500,400)
    root.maxsize(500,400)
    root.configure(bg="yellow")
    l=Label(root,text="Compound Interest Calculator",bg="red",fg="black",font="Bold")
    l.grid(row=1,column=0,columnspan=3,padx=145,pady=20)
    l1=Label(root,text="Principle(RS)",bg="green",fg="black",font="Verdana")
    l1.grid(row=2,column=0,padx=5,pady=5)
    l2=Label(root,text="Rate(%)",bg="green",fg="black",font="Verdana")
    l2.grid(row=3,column=0,padx=5,pady=15)
    l3=Label(root,text="Years",bg="green",fg="black",font="Verdana")
    l3.grid(row=4,column=0,padx=5,pady=25)
    principal_field=Entry()
    principal_field.grid(row=2,column=1)
    rate_field=Entry()
    rate_field.grid(row=3,column=1)
    year_field=Entry()
    year_field.grid(row=4,column=1)
    b=Button(text="SUBMIT",bg="light blue",fg="black",command=calculate_ci)
    b.grid(row=7,column=0,padx=20,pady=50)
    l4=Label(root,text="Total After Compound Interset",bg="green",fg="black",font="Verdana")
    l4.grid(row=5,column=0)
    result_field=Entry()
    result_field.grid(row=5,column=1)
    b1=Button(text="CLEAR",bg="light blue",fg="black",command=clear_all)
    b1.grid(row=7,column=1)
    root.mainloop()
    