import tkinter as tk
import socket # for socket 
import sys
import time



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Baglanti al"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.hi_there1 = tk.Button(self)
        self.hi_there1["text"] = "Baglan"
        self.hi_there1["command"] = self.baglan
        self.hi_there1.pack(side="top")

        self.hi_there2 = tk.Button(self)
        self.hi_there2["text"] = "Bilgi al"
        self.hi_there2["command"] = self.bilgi_al
        self.hi_there2.pack(side="top")

        self.hi_there3 = tk.Button(self)
        self.hi_there3["text"] = "Davet hazirla"
        self.hi_there3["command"] = self.davet_et
        self.hi_there3.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    def davet_et(self):
        ip2=input("ip adresi:")
        print("yagcilar chate davet edildiniz ip adresi:"+ip2)
    def bilgi_al(self):
        b=input("Choose type:")
        if b=="covid19":
            print("Covid19:Solunum yollarini etkileyen bir cesit coronavirus")
            print("Belirtiler: Ates,Oksuruk,halsizlik,nefes darligi")
            print("Yakindaki hastaneler 1.Ekin tip merkezi 2.edremit devlet hastanesi")
            print("Alo 185 kovid danisma hatti.")
        else:
            print("Wrong type selected")
            
    def say_hi(self):
        nick=input("nickname:")
        s = socket.socket()
        print ("Socket successfully created")
        port = 123                
        s.bind(('', port))         
        print ("socket binded to %s" %(port)) 
        s.listen(10)     
        print ("socket is listening")            
        c, addr = s.accept() 
        print ('Got connection from', addr )
        c.send('you connected to '+nick)
        while True:
            rec2=s.recevie()
            print(rec2)
            message=input("Message:")
            s.send(message )





        
    def baglan(self):
        nick2=input("nickaname:")
        ip=input("ip Adress:")
        try: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            print ("Socket successfully created")
        except socket.error as err: 
            print ("socket creation failed with error %s" %(err))
        port = 80
  
        try: 
            host_ip = ip
            s.connect((host_ip, port))
        except socket.gaierror:  
            print ("there was an error resolving the host")
            sys.exit()
        while True:
            message=input("Message:")
            s.send(message+nick2)
            time.wait(10)
            rec1=s.recevie()
            print(rec1)
             
    

root = tk.Tk()
root.title("yagcilar_altinoluk")
app = Application(master=root)
app.mainloop()
