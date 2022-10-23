
from ssl import RAND_add
import tkinter as tk
import random

def show_answer():
    blank.insert(tk.END, '')
    Ans = password_generator(int(length.get()),int(capitalization_check.get()), int(number_check.get()),int(special_check.get())  )
    blank.insert(tk.INSERT, Ans)
    


def password_generator(length, capitalization_check, number_check, special_check ):
    
    if length == 0:
        return "Entered zerro as the length"

    elif capitalization_check + number_check + special_check>length:
        return 'Conditions exceed the length of the password'
    else :
        
        gen_list=[] #list that will contain the password
        rand=1 # list will contain the range of ascii values to draw from
        lis = ['c'] #list that will contain possible types
        
        if capitalization_check == 1:
                gen_list.append(generate_Cletters())
                rand+=1
                lis.append('C')

        if number_check == 1:
            gen_list.append(generate_numbers())
            rand+=1
            lis.append('n')

        if special_check == 1:
            gen_list.append(generate_special())
            rand+=1
            lis.append('s')
    
    gen_list = create_list(rand, length, gen_list,lis)
    password = ''
    for i in gen_list:
        password+=i
    return password

def create_new_pass():
    blank.delete(0, tk.END)
    blank.insert(0, '')
        
def generate_Cletters():
    return chr(random.randrange(65,91))

def generate_numbers():
    return chr(random.randrange(48,58))

def generate_special():
    i = random.randrange(1,4)
    if i==1:
        return chr(random.randrange(58,65))
    elif i==2:
        return chr(random.randrange(91,97))
    else :
        return chr(random.randrange(123,127))

def generate_letters():
    return chr(random.randrange(97,123))

def create_list(rand, length, gen_list,lis):
    length=int(length)
    length=length-rand
    gen_list.append(generate_letters())
    for j in range(1,length+1):
        
        k=random.randrange(0,rand)
        
        if lis[k]=='c':
            gen_list.append(generate_letters())
        elif lis[k]=='C':
            gen_list.append(generate_Cletters())
        elif lis[k]=='n':
            gen_list.append(generate_numbers())
        elif lis[k]=='s':
            gen_list.append(generate_special())
    
    return gen_list


#initializing the root
master=tk.Tk()

#Setting tittle name
master.title("Random Password Generator")

#Inputs

#Requesting the length of password
tk.Label(master, text='Length of password').grid(row=3)
length = tk.Entry(master)
length.grid(row =3, column = 1)

#Asking if user wants lower and uppercase letters
capitalization_check = tk.IntVar()
tk.Checkbutton(master, text = 'Capital Letters', variable=capitalization_check).grid(row = 5, sticky = tk.E)

#Asking if user wants Numbers
number_check = tk.IntVar()
tk.Checkbutton(master, text = 'Numbers', variable = number_check).grid(row = 6, sticky = tk.E)

#Asking if user wants Special characters
special_check = tk.IntVar()
tk.Checkbutton(master, text = "Special Characters", variable = special_check).grid(row = 7, sticky = tk.E)

#displaying output
tk.Label(master, text = 'Your password is').grid(row=8)
output = tk.Entry(master)
output.grid(row = 8, column = 1)


#Start creating password 

begin = tk.Button(master, text = 'Create Password', width = 50, command=show_answer)
begin.grid(row = 9, column = 1)
blank = tk.Entry(master, relief=tk.GROOVE)
blank.grid(row=8, column=1)

#create new password
create_new_password = tk.Button(master, text = 'Create new Password', width = 50, command=create_new_pass)
create_new_password.grid(row = 10, column = 1)

#end program
end = tk.Button(master,text = 'Exit', width=50,command=master.destroy)
end.grid(row = 11, column = 1)

tk.mainloop()