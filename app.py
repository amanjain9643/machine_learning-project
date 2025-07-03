from tkinter import *
import json
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):
        # LOGIN GUI 

        self.dbo=Database()
        self.apio=API()
        self.root=Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap("/Users/apple/Documents/MLproject1/utils/images.ico")
        self.root.geometry('350x600')
        self.root.configure(bg="black")

        self.login_gui()
        self.root.mainloop()
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="black",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))


        label1=Label(self.root,text="enter email",bg="black",fg="white")
        label1.pack(pady=(10,10))
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2=Label(self.root,text="enter password",bg="black",fg="white")
        label2.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=50,show="()")
        self.password_input.pack(pady=(5,10),ipady=3)

        login_btn=Button(self.root,text='Login',bg="black",fg="black",height=2,width=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text="NOT A MEMBER",bg="black",fg="white")
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register',bg="black",fg="black",command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="black",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0=Label(self.root,text="enter name",bg="black",fg="white")
        label0.pack(pady=(10,10))
        self.name_input=Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=3)

        label1=Label(self.root,text="enter email",bg="black",fg="white")
        label1.pack(pady=(10,10))
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2=Label(self.root,text="enter password",bg="black",fg="white")
        label2.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=50,show="()")
        self.password_input.pack(pady=(5,10),ipady=3)

        register_btn=Button(self.root,text='Register',bg="black",fg="black",height=2,width=2,command=self.perform_regn)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text="Already A MEMBER",bg="black",fg="white")
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login',bg="black",fg="black",command=self.login_gui)
        redirect_btn.pack(pady=(10,10))



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def perform_regn(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        print(name,email,password)
        response=self.dbo.add_data(name,email,password)
        if response:
            # print("reg success")
            messagebox.showinfo("sucess","registeration succeed")
        else :
            # print("email exists")
            messagebox.showerror("failed","email already exists")
    def perform_login(self):
        email=self.email_input.get()
        password=self.password_input.get()

        response=self.dbo.search(email,password)
        if response:
            messagebox.showinfo("login","sucess")
            self.home_gui()
        else:
            messagebox.showerror("login","error")
    def home_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP APP",bg="black",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn=Button(self.root,text='SENTIMENT ANALYSIS',bg="black",fg="black",height=3,width=20,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))
        ner_btn=Button(self.root,text='Name Entity Recogntion',bg="black",fg="black",height=3,width=20,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))
        emotion_btn=Button(self.root,text='emotion',bg="black",fg="black",height=3,width=20)
        emotion_btn.pack(pady=(10,10))
        logout_btn=Button(self.root,text='LOGOUT',bg="black",fg="black",height=2,width=5 ,command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()
        
        heading=Label(self.root,text="NLP APP",bg="black",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text="SENTIMENT ANALYSIS",bg="black",fg="white")
        heading2.pack(pady=(10,10))
        heading2.configure(font=('verdana',24,'bold'))


        label1=Label(self.root,text="ENTER THE TEXT",bg="black",fg="white")
        label1.pack(pady=(20,10))

        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=3)

        sentiment_btn=Button(self.root,text='ANALYSE SENTIMENT',bg="black",fg="black",height=3,width=20,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text='',bg="black",fg="white")
        self.sentiment_result.pack(pady=(20,10))
        self.sentiment_result.configure(font=('verdana',16))
        goback_btn=Button(self.root,text='GO BACK',bg="black",fg="black",height=3,width=20,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    
    def do_sentiment_analysis(self):
        d={}
        text=self.sentiment_input.get()
        # result=self.apio.sentiment_analysis(text)['scored_labels']
        result=[{'label': 'NEUTRAL', 'score': 1}, {'label': 'surprise', 'score': 1}]
        txt=''
        for i in result:
            d[i['label']]=i['score']
            txt+= i['label']+' -> '+ str(i['score'])+'\n'
        print(txt)
        self.sentiment_result['text']=txt

    def ner_gui(self):
        self.clear()

        heading=Label(self.root,text="NLP APP",bg="black",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text="NER ANALYSIS",bg="black",fg="white")
        heading2.pack(pady=(10,10))
        heading2.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text="ENTER THE TEXT",bg="black",fg="white")
        label1.pack(pady=(20,10))

        self.ner_input=Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=3)

        label2=Label(self.root,text="ENTER THE SEARCHING ENTITY",bg="black",fg="white")
        label2.pack(pady=(20,10))

        self.entity_input=Entry(self.root,width=50)
        self.entity_input.pack(pady=(5,10),ipady=3)

        self.ner_result=Label(self.root,text='',bg="black",fg="white")
        self.ner_result.pack(pady=(20,10))
        self.ner_result.configure(font=('verdana',16))

        ner_btn=Button(self.root,text='NER',bg="black",fg="black",height=3,width=20,command=self.do_ner_analysis)
        ner_btn.pack(pady=(10,10))
        goback_btn=Button(self.root,text='GO BACK',bg="black",fg="black",height=3,width=20,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
    def do_ner_analysis(self):
        text=self.ner_input.get()
        entity=self.entity_input.get()
        
        # print(text,entity)

        if text and entity:
            response=self.apio.ner_analysis(text,entity)
            x=response['entities']
            z=[]
            for i in x:
                z.append(i['text'])
            # print(z)
            self.ner_result['text']=z
        else :
            self.ner_result['text']="invalid input"

        

nlp=NLPApp()