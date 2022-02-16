#program to create a GUI calendar and give year as input and get calendar as output
#we begin by installing tkinter

#now we begin the code by importing calendar module
import calendar
#import tkinter module
from tkinter import *
import tkinter

#code to display calendar 
def CalendarDisplay():
    CalendarScreen = Tk()
    CalendarScreen.config(background='cyan')      
    CalendarScreen.title("Calendar of the Year")        
    CalendarScreen.geometry("800x600")      
    year = int(year_field.get())
    CalendarScreen_content = calendar.calendar(year)
    CalendarYear = Label(CalendarScreen, text= CalendarScreen_content)
    CalendarYear.grid(row=1, column=1, padx=30)
    CalendarScreen.mainloop()

#code to provide year as input 
if __name__=='__main__':        #to show that the module (main.py file) source code is the main program.
    SideBox = Tk()
    SideBox.config(background='grey')
    SideBox.title("Calendar")
    SideBox.geometry("250x140")
    Cal = Label(SideBox, text="Calendar", bg= 'grey', font=("times", 28, "bold"))
    #label for enter year
    year = Label(SideBox, text= "Enter Year", bg= 'magenta')
    #text box for year input
    year_field = Entry(SideBox)
    button = Button(SideBox, text='Show Calendar', fg='black', bg='yellow', command= CalendarDisplay) #CalendarDisplay 
    #adjusting widgets in position
    Cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=6, column=1)
    SideBox.mainloop()

#END OF THE PROGRAM