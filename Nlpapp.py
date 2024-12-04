from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import Api
class NLPApp:
    def __init__(self):

        self.api = Api()
        self.db = Database()
        self.root = Tk()
        self.root.title("Abhi's NLPApp")
        self.root.geometry('400x600')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.configure(bg='#f39c12')

        self.login_gui()



        self.root.mainloop()

    def login_gui(self):

        self.clear()

        header = Label(self.root,text='NLP Tools',bg='#f39c12')
        header.pack(pady = (10,10))
        header.configure(font=('Caligna',24,'bold'))

        label1 = Label(self.root,text='Enter Email ID')
        label1.pack(pady = (60,10))

        self.email_input = Entry(self.root,width=31)
        self.email_input.pack(ipady=5)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=25, show='*')
        self.password_input.pack(ipady=5)

        login_butn = Button(self.root,text='Login',width=12, command=self.process_login)
        login_butn.pack(pady=(10,10))

        label3 = Label(self.root, text="Don't have an Account?")
        label3.pack(pady=(30, 2))

        reg_butn = Button(self.root, text='Register', width=12, command= self.register_gui)
        reg_butn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        header = Label(self.root, text='NLP Tools', bg='#f39c12')
        header.pack(pady=(10, 10))
        header.configure(font=('Caligna', 24, 'bold'))

        label_name = Label(self.root, text='Enter your Name')
        label_name.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=26)
        self.name_input.pack(ipady=5)

        label_email_input = Label(self.root, text='Enter Email ID')
        label_email_input.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=31)
        self.email_input.pack(ipady=5)

        label_password_input = Label(self.root, text='Set Password')
        label_password_input.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=31, show='*')
        self.password_input.pack(ipady=5)

        reg_butn = Button(self.root, text='Register', width=12, command=self.process_register)
        reg_butn.pack(pady=(10, 10))

        btl_butn = Button(self.root, bg= 'grey', text='Back to login', width=12, command=self.login_gui)
        btl_butn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def process_register(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        result = self.db.add_data(name, email, password)

        if result:
            messagebox.showinfo('success',"You're registered succesfully.\n login now")
            self.login_gui()
        else:
            messagebox.showerror('error','email already exists,\n try login')

    def home_gui(self):
        self.clear()

        label_tools = Label(self.root, text='Choose your required tool for Analysis')
        label_tools.pack(pady=(160, 10))

        sen_butn = Button(self.root, bg="red", text='Sentiment Analysis', width=25, command=self.sent_gui)
        sen_butn.pack(pady=(10, 10))

        ldet_butn = Button(self.root, bg= "brown",text='Language Detection', width=25)
        ldet_butn.pack(pady=(10, 10))

        reph_butn = Button(self.root, bg='green', text='Rephrase text', width=25)
        reph_butn.pack(pady=(10, 10))

        btl_butn = Button(self.root, bg='grey', text='Logout', width=12, command=self.login_gui)
        btl_butn.pack(pady=(10, 10))

    def process_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        result = self.db.check_user(email,password)

        if result:
            messagebox.showinfo('success','You have logged in succesfully')
            self.home_gui()
        else:
            messagebox.showerror('error','You have entered wrong emailiD/password\n Please retry with correct details')

    def sent_gui(self):
        self.clear()

        text_label = Label(self.root, text="Enter the text for Analysis")
        text_label.pack(pady=(10,10))

        self.text = Entry(self.root, width=31)
        self.text.pack(ipady=5)

        anl_butn = Button(self.root, text='Analyze', width=12, command=self.analyze)
        anl_butn.pack(pady=(10, 10))

    def analyze(self):

        text = self.text.get()
        result = self.api.sent_analysis(text)
        print(result)



nlp = NLPApp()