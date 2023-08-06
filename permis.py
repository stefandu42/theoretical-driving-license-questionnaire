from tkinter import *
from tkinter.messagebox import *
import random


class principal(Tk):
    def __init__(self):

        
        
        Tk.__init__(self)
        
        self.title("Permis de conduire")

        #questions des fichiers
        
        self.v= open("questions/voiture.txt","r",encoding='utf8')
        self.voiture_question = self.v.readlines()
        self.v.close()

        #reponses des fichiers
        self.vR= open("reponses/voiture.txt","r",encoding='utf8')
        self.voiture_reponses = self.vR.readlines()
        self.vR.close()
        
        #noms
        

        titre= Label(self, text="Code de la route belge", fg="green",font=("Helvetica", 20))

        titre.grid(row=0, column=1)

        voiture= Label(self, text="Voiture", font=("Helvetica", 15))

        voiture.grid(row=1, column=0)

        camion= Label(self, text="Camion", font=("Helvetica", 15))

        camion.grid(row=1, column=1)

        moto= Label(self, text="Moto", font=("Helvetica", 15))

        moto.grid(row=1, column=2)


        ligne=Label(self, text="---------", font=("Helvetica", 15))

        ligne.grid(row=3, column=1)


        #menu
        menu = Menu(self)

        menu1= Menu(menu, tearoff=0)

        menu1.add_command(label="Informations", command=self.message)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quitter)
        menu.add_cascade(label="A propos de nous", menu=menu1)

        self.config(menu=menu)

        #boutons

        bvoiture=Button(self,text="Voiture", command=lambda o="1" : self.essaye(o))
        bvoiture.grid(row=2,column=0)

        bcamion=Button(self,text="Camion",command=lambda o="2" : self.essaye(o))
        bcamion.grid(row=2,column=1)

        bmoto=Button(self,text="Moto",command=lambda o="3" : self.essaye(o))
        bmoto.grid(row=2,column=2)

        sortir= Button(self,text="Quitter",command=self.destroy)
        sortir.grid(row=4,column=1)

    def message(self):
        showinfo("Informations",
                 "Nous sommes une équipe spécialisée dans les programmes, \n nous sommes donc une entreprise qui recrute des experts. \n\n Toute image et question de ce quizz sont réservés")
    def quitter(self):
        a=askyesno("Quitter","Etes vous sur de vouloir quitter ?")
        if a == True:
            self.destroy()
    def essaye(self,o):
        if o=="1":
            self.destroy()
            voiture("Voiture",
                    ["voiture/1.png",#debut images
                     "voiture/2.png",
                     "voiture/3.png",
                     "voiture/4.png",
                     "voiture/5.png",
                     "voiture/6.png",
                     "voiture/7.png",
                     "voiture/8.png",
                     "voiture/9.png",
                     "voiture/10.png",
                     "voiture/11.png",
                     "voiture/12.png",
                     "voiture/13.png",
                     "voiture/14.png",
                     "voiture/15.png"],
                    ["voiture/1.png", #debut images2
                      "voiture/2.png",
                      "voiture/3.png",
                      "voiture/4.png",
                      "voiture/5.png",
                      "voiture/6.png",
                      "voiture/7.png",
                      "voiture/8.png",
                      "voiture/9.png",
                      "voiture/10.png",
                      "voiture/11.png",
                      "voiture/12.png",
                      "voiture/13.png",
                      "voiture/14.png",
                      "voiture/15.png"],
                    self.voiture_question,
                    self.voiture_reponses
                    
                    )
            
        if o=="2":
            self.destroy()
            camion()
        if o=="3":
            self.destroy()
            moto()


#VOITURE
class voiture(principal):
    def __init__(self,nom,images,images2,questions,message):
        Tk.__init__(self)
        self.title(nom)

        #TEMPS

        self.seconds = 15
        self.labeel = Label(self, text="15 s")
        self.labeel.grid(row=9)

        self.test=True

        #images
        self.images=images
        self.images2=images2
        self.image3=[]


        #questions
        self.questions=questions
        self.questions2=[]

        #message
        self.message=message
        self.message2=[]


        #melange image et questions
        for i in range(len(self.images)):
            self.hasard = random.choice(self.images)
            self.index_hasard = self.images2.index(self.hasard)
            self.questions2.append(self.questions[self.index_hasard])
            self.image3.append(self.hasard)
            self.images.remove(self.hasard)
            self.message2.append(self.message[self.index_hasard].replace('\n',''))

        

        
        #frame1

        
        
        self.Frame1 = Frame(self, borderwidth=2, relief=GROOVE)
        self.Frame1.grid(row=0)

        #photo
        self.photo = PhotoImage(file="debut.png")
        self.can=Canvas(self.Frame1, bg ="white")
        self.can.create_image(0, 0, anchor=NW, image=self.photo)
        self.can.grid(row=0,columnspan=4)
                      

        #reponses + question
        question = Label(self.Frame1,text="La question est :")
        question.grid(row=1)

        #change texte --
        self.texto= StringVar()
        self.texto.set("Instruction : A partir d'une image et d'une question trouvez la bonne reponse. \n Voici un exemple devant vous. Ici devrait apparaitre la question. \nReussite à plus de 11 sur 15 \n Cliquez sur 'Commencer'")
        
        self.label = Label(self.Frame1,textvariable=self.texto)
        self.label.grid(row=2,columnspan=3)#--

        #LABEL FRAME 1--
        self.reponse = LabelFrame(self.Frame1, text="Reponses", padx=20, pady=20)
        self.reponse.grid(row=3,column=1)

        #boutons
        self.h=["La réponse A","La réponse B","La réponse C"]
        self.A= Button(self.reponse, text=self.h[0],command=lambda j=self.h[0]: self.command(j))
        self.A.pack()
        self.B= Button(self.reponse, text=self.h[1],command=lambda j=self.h[1]: self.command(j))
        self.B.pack()
        self.C= Button(self.reponse, text=self.h[2],command=lambda j=self.h[2]: self.command(j))
        self.C.pack()

        self.A["state"]=DISABLED
        self.B["state"]=DISABLED
        self.C["state"]=DISABLED#--

        #nombre question
        self.ok=StringVar()
        self.oo=1
        label= Label(self.Frame1,textvariable=self.ok)
        label.grid(row=3,column=0)
        #resulat
        self.resultat= StringVar()
        e = Label(self.Frame1, textvariable=self.resultat)
        e.grid(row=6,column=0)

        #LABEL FRAME 2--
        self.messages = LabelFrame(self.Frame1, text="Message" )
        self.messages.grid(row=4,column=1)

        self.variable= StringVar()
        self.erreur = Label(self.messages,textvariable=self.variable)
        self.erreur.pack()



        #change image + texte (incremente)
        self.t=0
        self.i=0
        
        

        #suivant
        self.suivant= Button(self.Frame1,text="Commencer",command= self.change)
        self.suivant.grid(row=5,column=3)

        #quitter
        quitter= Button(self.Frame1,text="Retourner au menu",command= self.menu)
        quitter.grid(row=5,column=0)

        #resultat final
        self.fini=0
        self.affiche=StringVar()
        self.label2= Label(self.Frame1,textvariable=self.affiche)
        self.label2.grid(row=6,column=1)

        self.u=Button(self.Frame1,text='Recommencer',command=self.recommencer)
        self.u.grid(row=7,column=1)
        self.u["state"]=DISABLED
    def change(self):
        #activer le temps
        self.seconds=16
        self.test=True
        self.labeel.after(0000, self.compteur)
        self.labeel["fg"]="black"
        
        self.photo = PhotoImage(file=self.image3[self.t])
        self.can=Canvas(self.Frame1)
        self.can.create_image(0, 0, anchor=NW, image=self.photo)
        self.can.grid(row=0,columnspan=4)

        self.texto.set(self.questions2[self.t].replace('\\n','\n'))
        
        self.t+=1
        
        self.A["state"]="normal"
        self.B["state"]="normal"
        self.C["state"]="normal"
        self.suivant["state"]=DISABLED

        self.variable.set("")
        
        self.ok.set(str(self.oo)+"/15 question")
        self.oo+=1

        self.suivant["text"]="Suivant"
        

    def command(self,d):
        self.test=False
        if d == self.message2[self.i] and self.i == len(self.message2)-1:
           self.variable.set("Tu as juste")
           self.A["state"]=DISABLED
           self.B["state"]=DISABLED
           self.C["state"]=DISABLED
           self.suivant["state"]=DISABLED
           self.suivant["text"]="Fini!"
           self.fini+=1

           self.u["state"]='normal'
           
           if self.fini>=11:
               self.label2["fg"]="green"
               self.affiche.set(str(self.fini)+"/15, tu as donc reussi.")
           else:
               self.label2["fg"]="red"
               self.affiche.set(str(self.fini)+"/15, tu as donc raté.")
               
           self.i+=1
        elif d != self.message2[self.i] and self.i == len(self.message2)-1:
           self.variable.set("Tu as faux et c'est fini")
           self.A["state"]=DISABLED
           self.B["state"]=DISABLED
           self.C["state"]=DISABLED
           self.suivant["state"]=DISABLED
           self.suivant["text"]="Fini!"

           self.u["state"]='normal'
           
           if self.fini>=11:
               self.label2["fg"]="green"
               self.affiche.set(str(self.fini)+"/15, tu as donc reussi.")
           else:
               self.label2["fg"]="red"
               self.affiche.set(str(self.fini)+"/15, tu as donc raté.")
               
           self.i+=1
        elif d == self.message2[self.i]:
           self.variable.set("Tu as juste")
           self.A["state"]=DISABLED
           self.B["state"]=DISABLED
           self.C["state"]=DISABLED
           self.suivant["state"]="normal"
           self.fini+=1
           self.i+=1

        else:
            self.A["state"]=DISABLED
            self.B["state"]=DISABLED
            self.C["state"]=DISABLED
            self.suivant["state"]="normal"
            self.variable.set("Tu as faux, la reponse était "+self.message2[self.i])
            self.i+=1


    def recommencer(self):
            
        self.destroy()
        voiture()

    def menu(self):
        self.destroy()
        principal()
    def compteur (self):
        self.seconds -= 1

        if self.test==True:
        
            if self.seconds >=0:
                if self.seconds<=5:
                    self.labeel["fg"]="red"
                    self.labeel.configure(text="%i s" % self.seconds) #remplace les secondes dans le texte
                    # redemarre la fonction apres 1sec 
                    self.labeel.after(1000, self.compteur)
                else:
                    self.labeel.configure(text="%i s" % self.seconds) #remplace les secondes dans le texte
                    # redemarre la fonction apres 1sec 
                    self.labeel.after(1000, self.compteur)
            else:
                self.labeel['text'] = "Temps ecoulé !"
                self.A["state"]=DISABLED
                self.B["state"]=DISABLED
                self.C["state"]=DISABLED
                self.suivant["state"]="normal"
        else:
            self.test=False















        
#CAMION
class camion(voiture):
    def __init__(self):

        #questions
        self.c= open("questions/camion.txt","r",encoding='utf8')
        self.camion_question = self.c.readlines()
        self.c.close()

        
        #reponses des fichiers
        self.cR= open("reponses/camion.txt","r",encoding='utf8')
        self.camion_reponses = self.cR.readlines()
        self.cR.close()
        voiture.__init__(self,
                    "Camion",
                    ["camion/1.png",#debut images
                     "camion/2.png",
                     "camion/3.png",
                     "camion/4.png",
                     "camion/5.png",
                     "camion/6.png",
                     "camion/7.png",
                     "camion/8.png",
                     "camion/9.png",
                     "camion/10.png",
                     "camion/11.png",
                     "camion/12.png",
                     "camion/13.png",
                     "camion/14.png",
                     "camion/15.png"],
                    ["camion/1.png",#debut images 2
                     "camion/2.png",
                     "camion/3.png",
                     "camion/4.png",
                     "camion/5.png",
                     "camion/6.png",
                     "camion/7.png",
                     "camion/8.png",
                     "camion/9.png",
                     "camion/10.png",
                     "camion/11.png",
                     "camion/12.png",
                     "camion/13.png",
                     "camion/14.png",
                     "camion/15.png"],
                    self.camion_question,
                    self.camion_reponses)

        
    def change(self):
        voiture.change(self)
        

    def command(self,d):
        voiture.command(self,d)


    def recommencer(self):
            
        self.destroy()
        camion()

    def menu(self):
        voiture.menu(self)

    def compteur(self):
        voiture.compteur(self)














#MOTO
class moto(camion):
    def __init__(self):
        #questions
        self.m= open("questions/moto.txt","r",encoding='utf8')
        self.moto_question = self.m.readlines()
        self.m.close()

        #reponses des fichiers
        self.mR= open("reponses/moto.txt","r",encoding='utf8')
        self.moto_reponses = self.mR.readlines()
        self.mR.close()
        voiture.__init__(self,
                    "Moto",
                    ["moto/1.png",#debut images
                     "moto/2.png",
                     "moto/3.png",
                     "moto/4.png",
                     "moto/5.png",
                     "moto/6.png",
                     "moto/7.png",
                     "moto/8.png",
                     "moto/9.png",
                     "moto/10.png",
                     "moto/11.png",
                     "moto/12.png",
                     "moto/13.png",
                     "moto/14.png",
                     "moto/15.png"],
                    ["moto/1.png",#debut images2
                     "moto/2.png",
                     "moto/3.png",
                     "moto/4.png",
                     "moto/5.png",
                     "moto/6.png",
                     "moto/7.png",
                     "moto/8.png",
                     "moto/9.png",
                     "moto/10.png",
                     "moto/11.png",
                     "moto/12.png",
                     "moto/13.png",
                     "moto/14.png",
                     "moto/15.png"],
                    self.moto_question,
                    self.moto_reponses)

    def change(self):
        voiture.change(self)
        

    def command(self,d):
        voiture.command(self,d)


    def recommencer(self):
            
        self.destroy()
        moto()

    def menu(self):
        voiture.menu(self)
    def compteur (self):
        voiture.compteur(self)


o=principal()
