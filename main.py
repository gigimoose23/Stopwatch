import tkinter
import time
import tkinter.messagebox
root = tkinter.Tk()
introLabel = tkinter.Label(root, text="Welcome to stopwatch app", font=("Arial", 16, "bold"))
root.title("Stopwatch")
totalTime = 0
def logic():
    global totalTime
    
    totalTime-=1
    if totalTime == -1:
        tkinter.messagebox.showinfo("Info", "Time is up!")
        return
    minutes, seconds = divmod(totalTime, 60)
  
    hours = 0
    if minutes > 60:
        hours,minutes = divmod(minutes, 60)
          #  root.update()
        
            
            

    hour.set(str(hours))
    min.set(str(minutes))
    sec.set(str(seconds))
    root.update()
    root.after(1000, logic)
   
    
def startTime():
    global totalTime
    hourEntered = int(hour.get())
    minEntered = int(min.get())
    secEntered = int(sec.get())
    totalTime = (3600 * hourEntered) + (60 * minEntered) + secEntered
    root.after(1000, logic)

            
            

startButton = tkinter.Button(root, text="Start",command=startTime)

hour = tkinter.StringVar()
hourEntryBox = tkinter.Entry(root,textvariable=hour,font=("Arial",16),width=2)
hour.set("00")

min = tkinter.StringVar()
minuteEntryBox = tkinter.Entry(root,textvariable=min,font=("Arial",16),width=2)
min.set("00")

sec = tkinter.StringVar()
secondEntryBox = tkinter.Entry(root,textvariable=sec,font=("Arial",16),width=2)
sec.set("00")

root.geometry("500x200")
introLabel.place(x=250, y=30, anchor="center")
hourEntryBox.place(x=200,y=80, anchor="center")
minuteEntryBox.place(x=235,y=80, anchor="center")
secondEntryBox.place(x=270,y=80, anchor="center")
startButton.place(x=230, y=130, anchor="center")
root.resizable(False, False)

tkinter.mainloop()
