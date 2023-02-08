# import modules 

from tkinter import *

from lyrics_extractor import SongLyrics 

  
# user defined funtion 

def get_lyrics(): 

    

    extract_lyrics = SongLyrics( 

        "AIzaSyD27R4Wo_o2MJ9gZAoEiMrQ-RN4jL5GeRA", "7593fadfe3d633e73") 

      

    temp = extract_lyrics.get_lyrics(str(e.get())) 

    res = temp['lyrics'] 

    result.set(res) 

  

  
# object of tkinter 
# and background set to light grey 

master = Tk() 

master.configure(bg='#e6e6e6') 

master.title('Lyrics Extracter by G19')

  
# Variable Classes in tkinter 

result = StringVar() 

  
# Creating label for each information 
# name using widget Label 

Label(master, text="Enter Song name : ",  font='arial 10 bold',

      bg="light grey").grid(row=0, sticky=W) 

  

Label(master, text="Lyrics :",   font='arial 10 bold',

      bg="light grey").grid(row=3, sticky=W) 

  

  
# Creating lebel for class variable 
# name using widget Entry 

Label(master, text="", textvariable=result, 

      bg="light grey").grid(row=3, column=1, sticky=W) 

v = Scrollbar(master, orient='vertical')
   
e = Entry(master, width=50) 

e.grid(row=0, column=1) 

  
# creating a button using the widget 

b = Button(master, text="Show", 

           command=get_lyrics, bg="Blue") 

  

b.grid(row=0, column=2, columnspan=2, 

       rowspan=2, padx=5, pady=5,) 

  
mainloop()
