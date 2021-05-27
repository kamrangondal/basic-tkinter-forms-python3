from tkinter import *
import sys

root = Tk()
root.geometry('700x700')
root.title('FORM')

def only_numeric_input(k):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if k.isdigit() or k == "":
        return True
    return False


class NoDigits(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar(master)
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.var.trace('w', self.validate)

    def validate(self, *args):
        if not self.var.get().isalpha():
            corrected = ''.join(filter(str.isalpha, self.var.get()))
            self.var.set(corrected)



label_0 = Label(root, text="EMPLOYEES' PROVIDENT FUND SCHEME, 1952\n(PARA 57)",font=('bold', 20))
label_0.place(x=90, y=45)
#root.iconbitmap(r'ccc.ico')

label_1 = Label(root,text="To,",font=('bold', 13))
label_1.place(x=10, y=110)

label_2 = Label(root,text="The Regional P F Comissioner,",font=('bold', 13))
label_2.place(x=10, y=130)

label_3 = Label(root,text="FORM 13 (REVISED)",font=('bold', 14))
label_3.place(x=35, y=2)

label_4 = Label(root,text="{For EPFO Use Only}",font=('bold', 13))
label_4.place(x=600,y=2)


label_5 = Label(root,text="Office Name: ",font=('bold', 13))
label_5.place(x=10,y=151)

entry_1 = NoDigits(root,width = 30)
entry_1.place(x=150, y= 151)

label_6 =Label(root,text="Office Address: ",font=('bold', 13))
label_6.place(x=10, y=171)

entry_2 = Entry(root, width = 30)
entry_2.place(x=150, y=171)

label_7 = Label(root,text="To,",font=('bold',13))
label_7.place(x=400,y=110)

label_8 = Label(root,text="Trust Name: ",font=('bold',13))
label_8.place(x=400,y=130)

entry_3 = NoDigits(root, width = 30)
entry_3.place(x=540,y=130)

label_9 = Label(root,text="Trust Address: ",font=('bold',13))
label_9.place(x=400,y=151)

entry_4 = Entry(root, width = 30)
entry_4.place(x=540,y=151)

label_9 = Label(root,text="{in case the PF A/C is with Exempted Establishment}",font=('bold',13))
label_9.place(x=400,y=195)

label_10 = Label(root,text="(Please see instruction 3)",font=('bold',13))
label_10.place(x=10,y=195)

label_11 = Label(root,text="Sir,",font=('bold',14))
label_11.place(x=10,y=241)

label_12 = Label(root,text="I request that my provident fund balance along with my pension service details may please be",font=('bold',13))
label_12.place(x=70,y=261)

label_13 = Label(root,text="transferred to my present account under intimation to me. My details are as under:",font=('bold',13))
label_13.place(x=10,y=281)

label_14 = Label(root,text="PART A: PERSONAL INFORMATION",font=('bold',14))
label_14.place(x=260,y=315)

label_15 = Label(root,text="1. *Name: ",font=('bold',13))
label_15.place(x=10,y=346)

entry_5 = NoDigits(root, width=30)
entry_5.place(x=250, y=346)

label_16 = Label(root,text="2. *Father's/Husband's name: ",font=('bold',13))
label_16.place(x=10,y=367)

entry_6 = NoDigits(root, width=30)
entry_6.place(x=250,y=367)

label_17 = Label(root,text="3. Mobile number: ",font=('bold',13))
label_17.place(x=10,y=388)

entry_7 = Entry(root, width=25)
entry_7k = root.register(only_numeric_input)
entry_7.configure(validate="key", validatecommand=(entry_7k, "%P"))
entry_7.place(x=180, y=388)

label_18 = Label(root,text="4. Email id: ",font=('bold',13))
label_18.place(x=400,y=388)

entry_8= Entry(root, width=35)
entry_8.place(x=540, y=388)

label_19 = Label(root,text="5. Bank A/C number: ",font=('bold',13))
label_19.place(x=10,y=410)

entry_9 = Entry(root, width=25)
entry_9k = root.register(only_numeric_input)
entry_9.configure(validate="key", validatecommand=(entry_9k, "%P"))
entry_9.place(x=180, y=410)

label_20 = Label(root,text="6. IFS code of Bank branch: ",font=('bold',13))
label_20.place(x=400,y=410)

entry_10 = Entry(root)
entry_10.place(x=630, y=410)

label_21 = Label(root,text="PART B: DETAILS OF PREVIOUS ACCOUNT (WHICH IS TO BE TRANSFERRED)",font=('bold',14))
label_21.place(x=60,y=450)

label_22 = Label(root,text="1. *PF Account No: ",font=('bold',13))
label_22.place(x=10,y=480)

entry_11 = Entry(root, width=50)
entry_11k = root.register(only_numeric_input)
entry_11.configure(validate="key", validatecommand=(entry_11k, "%P"))
entry_11.place(x=190, y=480)

label_23 = Label(root,text="In case the previous establishment is exempted under Employees' Provident Fund Scheme,1952",font=('bold',13))
label_23.place(x=30,y=502)

label_24 = Label(root,text="Pension Fund Account No: ",font=('bold',13))
label_24.place(x=30,y=523)

entry_12 = Entry(root, width=38)
entry_12.place(x=260, y=523)

label_25 = Label(root,text="2. *Name and Address of the previous establishment: ",font=('bold',13))
label_25.place(x=10,y=546)

entry_13 = Entry(root, width=30)
entry_13.place(x=480, y=546)

label_26 = Label(root,text="3. *PF Account is held by: (Name of EPF Office/ PF Trust) ",font=('bold',13))
label_26.place(x=10,y=567)

entry_14 = NoDigits(root, width=30)
entry_14.place(x=480, y=567)

label_27 = Label(root,text="4. *Date of Birth: ",font=('bold',13))
label_27.place(x=10, y=589)

entry_15 = Entry(root)
entry_15.place(x=160, y=589)

label_28 = Label(root,text="{dd/mm/yyyy}",font=('bold',13))
label_28.place(x=275, y=589)

label_29 = Label(root,text="5. *Date of joining: ",font=('bold',13))
label_29.place(x=410, y=589)

entry_16 = Entry(root)
entry_16.place(x=570, y=589)

label_30 = Label(root,text="{dd/mm/yyyy}",font=('bold',13))
label_30.place(x=685, y=589)

label_31 = Label(root,text="6. *Date of leaving: ",font=('bold',13))
label_31.place(x=10, y=612)

entry_17 = Entry(root)
entry_17.place(x=160, y=612)

label_32 = Label(root,text="{dd/mm/yyyy}",font=('bold',13))
label_32.place(x=275, y=612)


root.mainloop()
