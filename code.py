from tkinter import *
from tkinter.filedialog import askopenfile
from tkVideoPlayer import TkinterVideo

root = Tk()
root.geometry('250x100')
root.config(bg='cyan')

def openFile():
   file = askopenfile(mode='r', filetypes=[('Video Files', ["*.mp4",'*.avi'])])
   if file is not None:
      # root.geometry('900x600')
      root.attributes('-fullscreen', True)
      global filename
      filename = file.name
      global videoplayer
      videoplayer = TkinterVideo(master=root, scaled=True, pre_load=False)
      videoplayer.load(r"{}".format(filename))
      videoplayer.pack(expand=True, fill="both")
      videoplayer.play() 

def exitWindow():
   root.destroy()
   root.quit()

b1=Button(root,bg='green',fg='white',text="Select Video and 'PLAY'",relief=RAISED,font=('Arial Bold',11),activeforeground='green',command=openFile)
b1.pack(padx=8,pady=10)
b2=Button(root,bg='red',fg='white',text="Exit",relief=SUNKEN,font=("Courier", 13, "italic"),activebackground='red',command=exitWindow)
b2.pack(padx=8,pady=2)

root.mainloop()
