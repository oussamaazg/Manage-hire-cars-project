from tkinter import *
from datetime import time,date
from AllClass import *
from tkinter import messagebox


class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Accuiel")
        self.width =self.winfo_screenwidth()
        self.height =self.winfo_screenheight()
        self.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.state('zoomed')
        #--------frame top---------
        self.frametop=Frame(self,bg='#1b9ea4',height=50)
        self.frametop.pack(fill=X)
        self.title=Label(self.frametop,text='ACCUIEL',bg='#1b9ea4',
                         fg='white',font=('tahoma',30),pady=10)
        self.title.pack()
        #----interfac utilisateur---------
        self.ListUser=[]
        def AjouterUtilisateur():
            from functools import partial
            from tkinter import messagebox
            def validateLogin(username, password, email):
                if username.get() == "" or password.get() == "" or email.get() == "":
                    messagebox.showerror("Invalid", "les champs sont obligatoires")
                else:
                    l = [email.get(), username.get(), password.get()]
                    messagebox.showinfo("Ajouter","utilisateur ajouter")
                    self.ListUser.append(l)
            def quitter():
                tkWindow.destroy()
                
            self.tkWindow = Tk()
            self.tkWindow.resizable(False, False)
            self.tkWindow.title('Ajouter utilisateurs')
            self.tkWindow.geometry('555x260')
            usernameLabel = Label(self.tkWindow, text="UserName", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=50)
            username = StringVar()
            usernameEntry = Entry(self.tkWindow, textvariable=username, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230,                                                                                                                 y=50)
            emailLabel = Label(self.tkWindow, text="Email", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=80)
            email = StringVar()
            emailEntry = Entry(self.tkWindow, textvariable=email, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=80)

            ppasswordLabel = Label(self.tkWindow, text="Password",width=20, pady=5,bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55,y=110)
            password = StringVar()
            passwordEntry = Entry(self.tkWindow, textvariable=password,width=30,show='*',font=('Microsoft YaHei UI Light', 11)).place(x=230,y=110)

            validateLogin = partial(validateLogin, username, password, email)
            loginButton = Button(self.tkWindow, text="Ajouter", command=validateLogin, width=20, cursor='hand2', pady=5, bg='green',border='4').place(x=120, y=180)
            quitter = Button(self.tkWindow, text="Quitter", command=quitter, width=20, cursor='hand2', pady=5, bg='red',border='4').place(x=300, y=180)
            self.tkWindow.mainloop()
        
        def AfficherUtilisateurs():
            self.fenetre = Tk()
            self.fenetre.geometry('1200x1200')
            frame = Frame(self.fenetre, width=1400, height=1000, bg='black')
            frame.place(x=0, y=0)
            heading = Label(frame, text='aucun utilasateur exist', bg='pink', fg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
            heading.place(x=500, y=80)
        #----interfac client---------
        self.ListClient=[]
        def AjouterClient():
            from functools import partial
            from tkinter import messagebox
            def validateClient(CIN, NOM, PRENOM,tel,NumPermis):
                if CIN.get() == "" or NOM.get() == "" or PRENOM.get() == "" or tel.get()=="" or NumPermis.get()=="":
                    messagebox.showerror("Invalid", "les champs sont obligatoires")
                else:
                    l = [CIN.get(), NOM.get(), PRENOM.get(),tel.get(),NumPermis.get()]
                    messagebox.showinfo("Ajouter", "Client ajouter")
                    self.ListClient.append(l)

            def quitter():
                self.tkWindow.destroy()
        
            self.tkWindow = Tk()
            self.tkWindow.resizable(False, False)
            self.tkWindow.title('Ajouter Clients ')
            self.tkWindow.geometry('555x260')

            CINLabel = Label(self.tkWindow, text="CIN", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=35)
            CIN = StringVar()
            CINEntry = (Entry(self.tkWindow, textvariable=CIN, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230,y=35))

            NOMLabel = Label(self.tkWindow, text="NOM", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=65)
            NOM = StringVar()
            NOMEntry = Entry(self.tkWindow, textvariable=NOM, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=65)

            PRENOMLabel = Label(self.tkWindow, text="PRENOM", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=95)
            PRENOM = StringVar()
            PRENOMEntry = Entry(self.tkWindow, textvariable=PRENOM, width=30,font=('Microsoft YaHei UI Light', 11)).place(x=230, y=95)

            telLabel = Label(self.tkWindow, text="tel", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=125)
            tel = StringVar()
            telEntry = Entry(self.tkWindow, textvariable=tel, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=125)

            NumPermisLabel = Label(self.tkWindow, text="NumPermis", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=155)
            NumPermis = StringVar()
            NumPermisEntry = Entry(self.tkWindow, textvariable=NumPermis, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230,y=155)

            validateClient = partial(validateClient, CIN, PRENOM,NOM,tel,NumPermis)
            AjouterButton = Button(self.tkWindow, text="Ajouter", command=validateClient, width=20, cursor='hand2', pady=5, bg='green',border='4').place(x=120, y=200)
            quitter = Button(self.tkWindow, text="Quitter", command=quitter, width=20, cursor='hand2', pady=5, bg='red', border='4').place(x=300, y=200)
            self.tkWindow.mainloop()
        def AfficherClients():
            self.fenetre=Tk()
            self.fenetre.geometry('1200x1200')
            frame = Frame(self.fenetre, width=1400, height=1000, bg='black')
            frame.place(x=0, y=0)
            heading = Label(frame, text='aucun client exist', bg='pink', fg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
            heading.place(x=500, y=80)
        
        #----interfac location---------
        self.ListLocation=[]
        def AjouterLocation():
            from functools import partial
            from tkinter import messagebox
            def validateLocations(datedelocation,dureedelocation,prixdelocation,Voiture,Client):
                if datedelocation.get() == "" or dureedelocation.get() == "" or prixdelocation.get() == "" or Client.get() == "" or Voiture.get() == "":
                    messagebox.showerror("Invalid", "les champs sont obligatoires")
                else:
                    l = [datedelocation.get(),dureedelocation.get(),prixdelocation.get(), Voiture.get(), Client.get()]
                    messagebox.showinfo("Location", "Location ajouter")
                    self.ListLocation.append(l)

            def quitter():
                self.tkWindow.destroy()

            self.tkWindow = Tk()
            self.tkWindow.resizable(False, False)
            self.tkWindow.title('Ajouter Locations')
            self.tkWindow.geometry('555x260')
            datedelocationLabel = Label(self.tkWindow, text="Date de location ", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=35)
            datedelocation = StringVar()

            datedelocationEntry = (Entry(self.tkWindow, textvariable=datedelocation, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=35))

            dureedelocationLabel = Label(self.tkWindow, text="Durée de location", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=65)
            dureedelocation = StringVar()
            dureedelocationEntry = Entry(self.tkWindow, textvariable=dureedelocation, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=65)

            prixdelocationLabel = Label(self.tkWindow, text="Prix de location", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=95)
            prixdelocation = StringVar()
            prixdelocationEntry = Entry(self.tkWindow, textvariable=prixdelocation, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=95)
            VoitureLabel = Label(self.tkWindow, text="Voiture", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=125)
            Voiture = StringVar()
            VoitureEntry = (Entry(self.tkWindow, textvariable=Voiture, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=125))
            ClientLabel = Label(self.tkWindow, text="Client", width=20, pady=5, bg='aqua', fg='black', border=0,font=('Microsoft YaHei UI Light', 9)).place(x=55, y=155)
            Client = StringVar()
            ClientEntry = (Entry(self.tkWindow, textvariable=Client, width=30, font=('Microsoft YaHei UI Light', 11)).place(x=230, y=155))
            validateLocations = partial(validateLocations,datedelocation,dureedelocation,prixdelocation,Voiture,Client)
            AjouterButton = Button(self.tkWindow, text="Ajouter", command=validateLocations, width=20, cursor='hand2', pady=5,bg='green', border='4').place(x=120, y=200)
            quitter = Button(self.tkWindow, text="Quitter", command=quitter, width=20, cursor='hand2', pady=5, bg='red',border='4').place(x=300, y=200)
            self.tkWindow.mainloop()
        def AfficherLocations():
            self.fenetre= Tk()
            self.fenetre.geometry('1200x1200')
            frame = Frame(self.fenetre, width=1400, height=1000, bg='black')
            frame.place(x=0, y=0)
            heading = Label(frame, text='aucun location exist', bg='black', fg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
            heading.place(x=500, y=80)
        
        
    
        def option1():
            Button(self, width=16, pady=7, text='Ajouter Utilisateur',command=AjouterUtilisateur, bg='#8e44ad', fg='white').place(x=220, y=180)
            Button(self, width=16, pady=7, text='Afficher Utilisateurs',command=AfficherUtilisateurs, bg='#8e44ad', fg='white').place(x=350, y=180)

        def option2():
            Button(self, width=16, pady=7, text='Ajouter Client',command=AjouterClient, bg='#8e44ad', fg='white').place(x=220, y=220)
            Button(self, width=16, pady=7, text='Afficher Clients',command=AfficherClients, bg='#8e44ad', fg='white').place(x=350, y=220)
        def option3():
            Button(self, width=16, pady=7, text='Ajouter Voiture', bg='#8e44ad',command=AjouterVoiture,fg='white').place(x=775, y=260)
            Button(self, width=16, pady=7, text='Afficher Voitures', bg='#8e44ad',command=AfficherVoitures, fg='white').place(x=905, y=260)
        def option4():
            Button(self, width=16, pady=7, text='Ajouter Location', bg='#8e44ad',command=AjouterLocation, fg='white').place(x=220, y=300)
            Button(self, width=16, pady=7, text='Afficher Locations', bg='#8e44ad',command=AfficherLocations,fg='white').place(x=350, y=300)
        def Quitter():
            self.destroy() 
        Button(self, width=39, pady=7, text='Gestion utilisateur',command=option1, bg='#57a1f8', fg='white', border=0).place(x=645,y=180)
        Button(self, width=39, pady=7, text='Gestion Client',command=option2, bg='#57a1f8', fg='white', border=0).place(x=645,y=220)
        Button(self, width=39, pady=7, text='Gestion Voiture',command=option3, bg='#57a1f8', fg='white', border=0).place(x=645,y=260)
        Button(self, width=39, pady=7, text='Gestion Locations',command=option4, bg='#57a1f8', fg='white', border=0).place(x=645,y=300)
        Button(self, width=39, pady=7, text='Quitter',command=Quitter, bg='red', fg='white', border=0).place(x=645,y=360)
        
        


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Authentification")

        app_width = 600
        app_height = 600
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width / 2) - (app_width / 2)
        y = (height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.resizable(False, False)
        """
        self.iconbitmap("C:\\Users\\Lenovo\\Desktop\\OFPPT\\DEV 1\\python\\IDLE\\tkinter\\cc2\\icon.ico")
        """
        self.config(background="silver")
        title=Label(self,text="login system login=login password=login",font=('Courier',15),bg='black',fg='white')
        title.pack(fill=X)
        frame=Frame(self,width="500",height="600",bg="whitesmoke")
        frame.pack(pady=30)
        lebeltitle=Label(frame,text='*Login*',font=('Arial',60,'italic','underline'),bg='whitesmoke',fg="#57a1f8")
        lebeltitle.place(x=120,y=20)
        
        login=StringVar()
        mdp=StringVar()
        login.set("login")
        mdp.set("123456")

        text_login = self.Labels(frame, "LOGIN:", 120)
        self.login = self.Entrys(frame, 185,textvariable=login)
        
        text_pwd = self.Labels(frame, "PASSWORD:", 235)
        self.password = self.Entrys(frame, 300,textvariable=mdp)
        c1=Checkbutton(frame,text="Forget password !",font=('Courier',10),bg='whitesmoke',fg='black')
        c1.place(x=172,y=350)
        
        btn_login = Button(frame,
                           text="LOGIN",
                           fg='black',
                           bg="#57a1f8",
                           bd=15,
                           font=("arial", 18),
                           cursor="heart",
                           activebackground='green',
                           command=self.authentification)
        btn_login.place(x=180, y=380, width=150, height=50)
        
    def Entrys(self, pos, y,textvariable):
        entry_obj = Entry(pos,font=("Courier", 18, "bold"))
        entry_obj.place(x=77, y=y, width=350, height=45)
        return entry_obj

    def Labels(self, pos, text, y):
        Label(pos,text=text,fg="black",bg="whitesmoke", font=(
            "Courier", 18), pady=20).place(x=78, y=y)
    

    def authentification(self):
        listUser=[]
        user1=['login','login']
        listUser.append(user1)
        isValid=((self.login.get()).strip()=='login' and
                 (self.password.get()).strip()=='login')
        
        isEmpty = (self.login.get() == "" and self.password.get() == "")

        if isValid:
            #======= Destroy Main Loop =======#
            self.destroy()
            main = MainApp()

        elif isEmpty:
            messagebox.showerror("Info", "Empty login or Password Try Again")

        else:
            messagebox.showerror(
                "Error", "Invalide login or Password Try Again")


def main():
    app = Login()
    app.mainloop()


if "__main__" == __name__:
    main()
