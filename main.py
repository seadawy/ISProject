from tkinter import *
from customtkinter import *
from tkinter import messagebox
from PIL import Image
from tkinter.filedialog import *
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import uuid
import os
import shutil
import mysql.connector


userID = 0
dbMain = mysql.connector.connect(
    host="localhost", user="root", password="", database="isp"
)
db = dbMain.cursor()

set_appearance_mode("Dark")
set_default_color_theme("blue")


app = CTk()  # create CTk window like you do with the Tk window
app.geometry("500x500")
app.resizable(False, False)
tempuploadimg = "\\asset\\user.png"

# CLEAR
def clear():
    for widgets in app.winfo_children():
        widgets.destroy()


# LOGIN PAGE
def start():
    clear()

    def upload_file():
        global tempuploadimg
        f_types = [("Png Files", "*.png")]
        filename = askopenfilename(filetypes=f_types)
        tempuploadimg = filename
        xxx = "asset/" + uuid.uuid4().hex[:8] + ".png"
        shutil.copyfile(filename, xxx)
        u3.configure(text=filename)
        tempuploadimg = xxx
        filename = xxx

    def readytogo():
        if not (
            name.get() and iid.get() and adress.get() and typ.get() and password.get()
        ):
            messagebox.showwarning(
                "notice", "make sure you have write all the information"
            )

        else:
            sql = "INSERT INTO `student`(`name`, `IId`, `adress`, `img`,`type`, `password`) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (
                name.get(),
                iid.get(),
                adress.get(),
                tempuploadimg,
                typ.get(),
                password.get(),
            )
            db.execute(sql, val)
            dbMain.commit()
            CTkLabel(frame, text="student insert successfully").pack()
            tabview.set("Login")

    def login():
        global userID
        userID = user.get()
        sql = "SELECT * FROM admin WHERE user= %s AND password= %s"
        db.execute(sql, (userID, pas.get()))
        if len(db.fetchall()):
            admin()
        else:
            sql = "SELECT * FROM student WHERE id= %s AND password= %s"
            db.execute(sql, (userID, pas.get()))
            arr = db.fetchall()
            if len(arr) == 1:
                student(arr[0])
            else:
                messagebox.showerror("showerror", "invalid User OR password")

    tabview = CTkTabview(app, width=500)
    tabview.pack(padx=10, pady=10, fill=BOTH, expand=True)

    tabview.add("Login")
    tabview.add("Register")
    tabview.set("Login")

    frame = tabview.tab("Login")
    # login
    CTkLabel(frame, text="Login", font=("defult", 30)).pack(pady=10)
    user = StringVar()
    pas = StringVar()
    CTkLabel(frame, width=20, text="International ID", font=("Verdana", 14)).place(
        x=100, y=55
    )
    CTkEntry(
        frame,
        textvariable=user,
        placeholder_text="User ID",
        width=282,
        height=30,
        corner_radius=25,
    ).pack(pady=30)
    CTkLabel(frame, font=("Verdana", 14), text="Password").place(x=100, y=120)
    CTkEntry(
        frame,
        textvariable=pas,
        width=282,
        height=30,
        corner_radius=25,
        placeholder_text="Password",
        show="*",
    ).pack()
    CTkButton(frame, corner_radius=25, text="Go", command=login).pack(padx=5, pady=5)
    msg = CTkLabel(frame, text="")
    logo = CTkImage(dark_image=Image.open("asset/ctrl.png"), size=(200, 200))
    CTkLabel(frame, image=logo, text="", fg_color="transparent").pack()
    # Register
    name = StringVar()
    iid = StringVar()
    typ = StringVar()
    adress = StringVar(value="Select Adress")
    password = StringVar()
    frame2 = tabview.tab("Register")
    CTkLabel(frame2, text="Register", font=("defult", 30)).pack(pady=10)

    CTkLabel(frame2, text="Name ", font=("Verdana", 14)).place(x=103, y=40)
    CTkEntry(
        frame2,
        textvariable=name,
        width=282,
        height=30,
        corner_radius=25,
    ).pack(pady=15)

    CTkLabel(frame2, text="International ID", font=("Verdana", 14)).place(x=100, y=99)
    CTkEntry(
        frame2,
        textvariable=iid,
        width=282,
        height=30,
        corner_radius=25,
    ).pack(pady=11)

    CTkLabel(
        frame2, text="Adress ", font=("Verdana", 14), fg_color="transparent"
    ).place(x=100, y=156)
    CTkOptionMenu(
        frame2,
        width=282,
        height=30,
        corner_radius=25,
        values=["KFS", "ALEX", "LUXOR", "CAIRO"],
        variable=adress,
    ).pack(pady=15)
    CTkSegmentedButton(
        frame2,
        variable=typ,
        values=["Male", "Female", "Coder"],
        font=("Verdana", 14),
        fg_color="#343638",
        width=200,
        corner_radius=5,
    ).pack(ipadx=30, pady=(0, 10))
    CTkLabel(frame2, font=("Verdana", 14), text="Password ").place(x=100, y=260)
    CTkEntry(
        frame2, textvariable=password, width=282, height=30, corner_radius=25, show="*"
    ).pack(pady=20)
    CTkLabel(frame2, font=("Verdana", 14), text="Avatar Image").place(x=100, y=320)
    frame22 = CTkFrame(frame2)
    CTkButton(
        frame22, text="Select Image", width=20, command=lambda: upload_file()
    ).pack(side=LEFT, padx=10)
    u3 = CTkLabel(frame22, text="No File Selected")
    u3.pack(side=LEFT)
    frame22.pack(padx=10, pady=10, ipadx=55, ipady=10)
    CTkButton(frame2, text="ready  to go", command=readytogo).pack()

    app.mainloop()


# ADMIN
def admin():
    def home():
        app.geometry("500x500")
        clear()
        out = CTkImage(dark_image=Image.open("asset/out.png"), size=(20, 20))
        PPPframe = CTkFrame(app)
        PPframe = CTkFrame(PPPframe)
        Pframe = CTkFrame(PPframe)
        frame = CTkFrame(Pframe)
        photo = CTkImage(
            dark_image=Image.open("asset/n1.png"),
            size=(130, 130),
        )
        CTkButton(
            frame,
            corner_radius=25,
            text="",
            fg_color="transparent",
            hover="disable",
            width=120,
            height=120,
            image=photo,
            command=manage,
        ).place(x=0, y=20)
        photo = CTkImage(
            dark_image=Image.open("asset/n2.png"),
            size=(130, 130),
        )
        CTkButton(
            frame,
            corner_radius=25,
            text="",
            fg_color="transparent",
            hover="disable",
            width=120,
            height=120,
            image=photo,
            command=quiz,
        ).place(x=160, y=20)
        photo = CTkImage(
            dark_image=Image.open("asset/n3.png"),
            size=(130, 130),
        )
        CTkButton(
            frame,
            corner_radius=25,
            text="",
            fg_color="transparent",
            hover="disable",
            width=120,
            height=120,
            image=photo,
            command=matrial,
        ).place(x=0, y=170)
        photo = CTkImage(
            dark_image=Image.open("asset/n4.png"),
            size=(130, 130),
        )
        CTkButton(
            frame,
            corner_radius=25,
            text="",
            fg_color="transparent",
            hover="disable",
            width=120,
            height=120,
            image=photo,
            command=team,
        ).place(x=160, y=170)
        CTkButton(
            app,
            image=out,
            text="",
            width=20,
            hover_color="#333333",
            corner_radius=0,
            command=start,
        ).place(x=430, y=40)
        frame.pack(fill=BOTH, expand=True, padx=20, ipady=240, pady=20)
        Pframe.pack(fill=BOTH, expand=True, padx=22, ipady=200, pady=20)
        PPframe.pack(fill=BOTH, expand=True, padx=20, ipady=200, pady=20)
        PPPframe.pack(fill=BOTH, expand=True, padx=20, ipady=200, pady=20)
        app.mainloop()

    def manage():
        def deleteStu(x):
            sql = "DELETE FROM student WHERE id =%s"
            db.execute(sql, [x])
            dbMain.commit()
            manage()

        def show(x):
            global imgdb

            def chimg():
                global imgdb
                f_types = [("Png Files", "*.png")]
                filename = askopenfilename(filetypes=f_types)
                btn1.configure(fg_color="#A30000")
                imgdb = filename
                img.configure(dark_image=Image.open(imgdb))

            def edit(x):
                sql = "UPDATE `student` SET `name`=%s,`IId`=%s,`adress`=%s,`type`=%s,`img`=%s WHERE id=%s"
                db.execute(
                    sql, (name.get(), iid.get(), adress.get(), typ.get(), imgdb, x)
                )
                dbMain.commit()
                manage()

            info = CTkToplevel()
            info.title("info")
            info.geometry("400x500")
            db.execute("SELECT * FROM `student` WHERE id =%s", [x])
            arr = db.fetchall()
            img = CTkImage(dark_image=Image.open(str(arr[0][5])), size=(150, 150))
            sss = CTkImage(dark_image=Image.open("asset/s.png"), size=(50, 50))
            name = StringVar()
            iid = StringVar()
            typ = StringVar(value=str(arr[0][4]))
            adress = StringVar(value=str(arr[0][3]))
            imgdb = str(arr[0][5])
            CTkLabel(
                info,
                image=img,
                text="",
                fg_color="transparent",
            ).place(x=130, y=10)
            CTkLabel(
                info,
                image=sss,
                text="",
                fg_color="transparent",
            ).place(x=165, y=165)
            CTkLabel(
                info,
                font=("defult", 20),
                text=arr[0][6],
                fg_color="transparent",
            ).place(x=230, y=175)
            btn1 = CTkButton(
                info,
                text="🛠",
                font=("defult", 26),
                width=20,
                corner_radius=0,
                height=20,
                command=chimg,
            )
            btn1.place(x=300, y=10)
            # ID
            CTkLabel(
                info,
                text="ID",
            ).place(x=70, y=220)
            ID = str(arr[0][0])
            IDe = CTkEntry(
                info,
                corner_radius=0,
                width=200,
            )
            IDe.insert(0, ID)
            IDe.configure(state="disable")
            IDe.place(x=120, y=220)
            # Name
            CTkLabel(info, text="Name").place(x=70, y=260)
            Name = arr[0][1]
            Namee = CTkEntry(
                info,
                textvariable=name,
                corner_radius=0,
                width=200,
            )
            Namee.insert(0, Name)
            Namee.place(x=120, y=260)
            # IND
            CTkLabel(info, text="NID").place(x=70, y=300)
            IND = arr[0][2]
            INDe = CTkEntry(
                info,
                textvariable=iid,
                corner_radius=0,
                width=200,
            )
            INDe.insert(0, IND)
            INDe.place(x=120, y=300)
            # Adress
            CTkLabel(info, text="Adress").place(x=70, y=340)
            CTkOptionMenu(
                info,
                width=200,
                corner_radius=0,
                values=["KFS", "ALEX", "LUXOR", "CAIRO"],
                variable=adress,
            ).place(x=120, y=340)
            # type
            CTkLabel(info, text="Type").place(x=70, y=380)
            CTkSegmentedButton(
                info,
                width=2000,
                variable=typ,
                values=["Male", "Female", "Coder"],
                font=("Verdana", 14),
                fg_color="#343638",
                corner_radius=0,
            ).place(x=140, y=380)

            CTkButton(info, text="cancel", fg_color="red", command=info.destroy).place(
                y=460, x=50
            )
            CTkButton(info, text="edit", command=lambda: edit(x)).place(y=460, x=200)
            info.mainloop()

        app.geometry("700x500")
        clear()
        db.execute("SELECT id,name,IId,adress,type,rank FROM `student`")
        arr = db.fetchall()
        i = 1
        frame = app
        e = CTkEntry(
            frame,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=60,
            text_color="white",
        )
        e.grid(row=0, column=0)
        e.insert(END, "ID")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            fg_color="#808080",
            corner_radius=0,
            border_color="#fff",
            width=150,
            text_color="white",
        )
        e.grid(row=0, column=1)
        e.insert(END, "NAME")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            fg_color="#808080",
            corner_radius=0,
            border_color="#fff",
            width=120,
            text_color="white",
        )
        e.grid(row=0, column=2)
        e.insert(END, "National ID")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            fg_color="#808080",
            corner_radius=0,
            border_color="#fff",
            width=80,
            text_color="white",
        )
        e.grid(row=0, column=3)
        e.insert(END, "ADRESS")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            fg_color="#808080",
            corner_radius=0,
            border_color="#fff",
            width=80,
            text_color="white",
        )
        e.grid(row=0, column=4)
        e.insert(END, "TYPE")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            corner_radius=0,
            border_color="#fff",
            width=50,
            fg_color="#808080",
            text_color="white",
        )
        e.grid(row=0, column=5)
        e.insert(END, "SCORE")
        e.configure(state="disable")
        e = CTkEntry(
            frame,
            border_width=1,
            fg_color="#808080",
            corner_radius=0,
            border_color="#fff",
            width=159,
            text_color="white",
        )

        e.grid(row=0, column=6, columnspan=2)
        e.insert(END, "ACTIONS")
        e.configure(state="disable")
        for j in arr:
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=60,
                text_color="white",
            )
            e.grid(row=i, column=0)
            e.insert(END, str(j[0]))
            e.configure(state="disable")
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=150,
                text_color="white",
            )
            e.grid(row=i, column=1)
            e.insert(END, str(j[1]))
            e.configure(state="disable")
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=120,
                text_color="white",
            )
            e.grid(row=i, column=2)
            e.insert(END, str(j[2]))
            e.configure(state="disable")
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=80,
                text_color="white",
            )
            e.grid(row=i, column=3)
            e.insert(END, str(j[3]))
            e.configure(state="disable")
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=80,
                text_color="white",
            )
            e.grid(row=i, column=4)
            e.insert(END, str(j[4]))
            e.configure(state="disable")
            e = CTkEntry(
                frame,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=50,
                text_color="white",
            )
            e.grid(row=i, column=5)
            e.insert(END, str(j[5]))
            e.configure(state="disable")

            CTkButton(
                frame,
                text="Del",
                width=70,
                corner_radius=0,
                fg_color="#990000",
                hover_color="#ff3333",
                command=lambda number=j[0]: deleteStu(number),
            ).grid(row=i, column=7)
            CTkButton(
                frame,
                text="Edit",
                width=90,
                corner_radius=0,
                command=lambda number=j[0]: show(number),
            ).grid(row=i, column=6)

            i += 1

        CTkButton(app, text="To Home", command=home).place(x=280, y=460)

    def matrial():
        clear()

        def deleteFile(x):
            sql = "DELETE FROM matrial WHERE idFile =%s"
            db.execute(sql, [x])
            dbMain.commit()
            matrial()

        def upload_file():
            global tempuploadimg
            f_types = [("Files", "*")]
            filename = askopenfilename(filetypes=f_types)
            tempuploadimg = filename
            u3.configure(text=filename)

        def readytogo():
            global tempuploadimg
            if tempuploadimg and fname.get():
                sql = (
                    "INSERT INTO `matrial`(`filename`,`file`,`date`) VALUES (%s,%s,%s)"
                )
                val = (fname.get(), tempuploadimg, date.today())
                db.execute(sql, val)
                dbMain.commit()
                CTkLabel(frame2, text="file added sucessfully & redirect. . .").pack()
                matrial()
                tempuploadimg = ""
            else:
                messagebox.showwarning(
                    "notice", "make sure you have write all the information"
                )

        tabview = CTkTabview(app, width=500)
        tabview.pack(padx=10, pady=10, fill=BOTH, expand=True)

        tabview.add("Add New")
        tabview.add("Manage")
        tabview.set("Manage")
        frame2 = tabview.tab("Add New")
        fname = StringVar()
        CTkLabel(frame2, text="Add Matrial", font=("defult", 30)).pack(pady=60)
        CTkLabel(frame2, text="File Name", font=("defult", 14)).place(x=105, y=120)
        CTkEntry(frame2, textvariable=fname, width=260).pack()
        frame22 = CTkFrame(frame2)
        CTkButton(
            frame22, text="Select File", width=20, command=lambda: upload_file()
        ).pack(side=LEFT, padx=10)
        u3 = CTkLabel(frame22, text="No File Selected")
        u3.pack(side=LEFT)
        frame22.pack(padx=10, pady=10, ipadx=55, ipady=10)
        CTkButton(frame2, text="Save", width=100, command=readytogo).pack(pady=10)
        frame3 = tabview.tab("Manage")
        db.execute("SELECT * FROM `matrial`")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=0)
        e.insert(END, "File")
        e.configure(state="disable")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=1)
        e.insert(END, "Date")
        e.configure(state="disable")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=63,
            text_color="white",
        )
        e.grid(row=0, column=2)
        e.insert(END, "Action")
        e.configure(state="disable")
        ajs = db.fetchall()
        r = 0
        for i in ajs:
            r += 1
            e = CTkEntry(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=0)
            e.insert(END, str(i[2]))
            e.configure(state="disable")
            e = CTkEntry(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=1)
            e.insert(END, str(i[3]))
            e.configure(state="disable")
            CTkButton(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=63,
                fg_color="red",
                text_color="white",
                text="DEL",
                command=lambda number=i[0]: deleteFile(number),
            ).grid(row=r, column=2)

        CTkButton(app, text="To Home", command=home).place(x=180, y=450)

    def quiz():
        def deletequiz(x):
            sql = "DELETE FROM quiz WHERE idQuiz =%s"
            db.execute(sql, [x])
            sql = "DELETE FROM questions WHERE quizId =%s"
            db.execute(sql, [x])
            dbMain.commit()
            quiz()

        def addq():
            def sendit():
                sql = (
                    "INSERT INTO `questions`(`quizId`, `ques`, `ans`) VALUES (%s,%s,%s)"
                )
                for i in range(QN.get()):
                    db.execute(sql, (qid, q[i].get(), a[i].get()))
                    dbMain.commit()
                quiz()

            frame72 = CTkFrame(app)
            q = [StringVar() for i in range(QN.get())]
            a = [IntVar() for i in range(QN.get())]
            yaxis = 20
            for i in range(QN.get()):
                CTkLabel(frame72, text=str(i + 1)).place(x=60, y=yaxis)
                CTkEntry(frame72, width=250, textvariable=q[i]).place(x=100, y=yaxis)

                CTkCheckBox(frame72, text="", variable=a[i]).place(x=380, y=yaxis + 1)
                yaxis += 40

            CTkButton(frame72, text="done", command=sendit).place(y=yaxis, x=70)
            CTkButton(
                frame72, text="cancel", fg_color="red", command=lambda: deletequiz(qid)
            ).place(y=yaxis, x=250)
            frame72.pack(fill=BOTH, expand=True, padx=20, ipady=240, pady=20)

        def go():
            sql = "INSERT INTO `quiz`(`idQuiz`,`name`, `time`, `QN`, `date`) VALUES (%s,%s,%s,%s,%s)"
            db.execute(sql, (qid, qname.get(), qtime.get(), QN.get(), date.today()))
            dbMain.commit()
            clear()
            addq()

        clear()
        qname = StringVar()
        qtime = IntVar()
        QN = IntVar()
        qid = uuid.uuid4().hex[:8]
        tabview = CTkTabview(app, width=500)
        tabview.pack(padx=10, pady=10, fill=BOTH, expand=True)
        tabview.add("Add New")
        tabview.add("Manage")
        tabview.set("Manage")
        frame23 = tabview.tab("Add New")
        CTkLabel(frame23, text="Add Quiz", font=("defult", 30)).pack(pady=20)
        CTkLabel(frame23, text="Quiz Name", font=("defult", 18)).place(x=117, y=70)
        CTkEntry(frame23, textvariable=qname, corner_radius=25, width=220).place(
            x=120, y=100
        )

        CTkLabel(frame23, text="Number of Question", font=("defult", 18)).place(
            x=117, y=140
        )
        CTkEntry(frame23, textvariable=QN, corner_radius=25, width=220).place(
            x=120, y=165
        )

        CTkLabel(frame23, text="Time with minutes", font=("defult", 18)).place(
            x=117, y=205
        )
        CTkEntry(frame23, textvariable=qtime, corner_radius=25, width=220).place(
            x=120, y=230
        )

        CTkButton(
            frame23,
            text="set up questions",
            height=40,
            width=100,
            font=("defult", 18),
            command=go,
            fg_color="green",
        ).place(x=160, y=300)
        frame7 = tabview.tab("Manage")
        db.execute("SELECT idQuiz ,name,date FROM `quiz`")
        e = CTkEntry(
            frame7,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=0)
        e.insert(END, "Quiz Name")
        e.configure(state="disable")
        e = CTkEntry(
            frame7,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=1)
        e.insert(END, "Date")
        e.configure(state="disable")
        e = CTkEntry(
            frame7,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=63,
            text_color="white",
        )
        e.grid(row=0, column=2)
        e.insert(END, "Action")
        e.configure(state="disable")
        ajs = db.fetchall()
        r = 0
        for i in ajs:
            r += 1
            e = CTkEntry(
                frame7,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=0)
            e.insert(END, str(i[1]))
            e.configure(state="disable")
            e = CTkEntry(
                frame7,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=1)
            e.insert(END, str(i[2]))
            e.configure(state="disable")
            CTkButton(
                frame7,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=63,
                fg_color="red",
                text_color="white",
                text="DEL",
                command=lambda number=i[0]: deletequiz(number),
            ).grid(row=r, column=2)
        CTkButton(app, text="To Home", command=home).place(x=180, y=400)

    def team():
        clear()
        img = CTkImage(dark_image=Image.open("asset/team.png"), size=(500, 500))
        CTkLabel(app, image=img, text="").pack()
        CTkButton(
            app,
            width=140,
            text="To Home",
            fg_color="#8a5f2c",
            corner_radius=0,
            command=home,
        ).place(x=190, y=460)

    home()


# STUDENT
def student(y):
    x = y

    def starttest(tid):
        def check():
            score = 0
            yyy = x
            for i in range(arr[0][3]):
                if ta[i] == a[i].get():
                    score += 1

            db.execute(
                "INSERT INTO `history`(`studentId`, `quizId`, `score`) VALUES (%s,%s,%s)",
                (yyy[0], tid, score),
            )
            db.execute(
                "UPDATE `student` SET `rank`=rank+%s WHERE id =%s", (score, yyy[0])
            )
            dbMain.commit()
            yy = list(yyy)
            yy[6] += score
            yyy = tuple(yy)
            student(yyy)

        clear()
        db.execute("SELECT * FROM quiz WHERE idQuiz = %s", [tid])
        arr = db.fetchall()
        db.execute("SELECT * FROM questions WHERE quizId = %s", [tid])
        qarr = db.fetchall()
        frame72 = CTkFrame(app)
        ta = []
        for j in qarr:
            ta.append(j[2])

        a = [IntVar() for i in range(arr[0][3])]
        yaxis = 20
        for i, j in enumerate(qarr):
            CTkLabel(frame72, text=str(i + 1)).place(x=60, y=yaxis)
            CTkLabel(frame72, width=250, text=j[1]).place(x=100, y=yaxis)
            CTkCheckBox(frame72, text="", variable=a[i]).place(x=380, y=yaxis + 1)
            yaxis += 40

        CTkButton(frame72, text="send", command=check).place(y=yaxis, x=170)
        frame72.pack(fill=BOTH, expand=True, padx=22, ipady=200, pady=20)

    def home():
        def openfile(z):
            os.system(z)

        clear()
        ava = CTkImage(dark_image=Image.open(str(x[5])), size=(200, 200))
        out = CTkImage(dark_image=Image.open("asset/out.png"), size=(20, 20))
        CTkLabel(app, image=ava, text="").place(x=150, y=10)
        CTkButton(
            app, image=out, text="", width=20, fg_color="transparent", command=start
        ).place(x=320, y=50)
        CTkLabel(
            app,
            text=str(x[1]),
            font=("Verdana", 14),
            fg_color="#DFF6FF",
            width=120,
            corner_radius=25,
            text_color="black",
        ).place(x=190, y=210)
        tabview = CTkTabview(app, width=500)
        tabview.pack(padx=10, pady=(250, 10), fill=BOTH)
        tabview.add("Matrial")
        tabview.add("Quizes")
        tabview.add("Statics")
        tabview.set("Matrial")
        frame33 = tabview.tab("Quizes")
        frame3 = tabview.tab("Matrial")
        # Matrial
        db.execute("SELECT * FROM `matrial`")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=0)
        e.insert(END, "File")
        e.configure(state="disable")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=200,
            text_color="white",
        )
        e.grid(row=0, column=1)
        e.insert(END, "Date")
        e.configure(state="disable")
        e = CTkEntry(
            frame3,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=63,
            text_color="white",
        )
        e.grid(row=0, column=2)
        e.insert(END, "Action")
        e.configure(state="disable")
        ajs = db.fetchall()
        r = 0
        for i in ajs:
            r += 1
            e = CTkEntry(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=0)
            e.insert(END, str(i[2]))
            e.configure(state="disable")
            e = CTkEntry(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=200,
                text_color="white",
            )
            e.grid(row=r, column=1)
            e.insert(END, str(i[3]))
            e.configure(state="disable")
            CTkButton(
                frame3,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=63,
                text_color="white",
                text="Open",
                command=lambda fp=str(i[1]): openfile(fp),
            ).grid(row=r, column=2)

        # Quizes

        height = []
        bars = []

        db.execute("SELECT * FROM `quiz`")
        e = CTkEntry(
            frame33,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=140,
            text_color="white",
        )
        e.grid(row=0, column=0)
        e.insert(END, "Name")
        e.configure(state="disable")
        e = CTkEntry(
            frame33,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=50,
            text_color="white",
        )
        e.grid(row=0, column=1)
        e.insert(END, "Q.N")
        e.configure(state="disable")
        e = CTkEntry(
            frame33,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=90,
            text_color="white",
        )
        e.grid(row=0, column=2)
        e.insert(END, "Time")
        e.configure(state="disable")
        e = CTkEntry(
            frame33,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=120,
            text_color="white",
        )
        e.grid(row=0, column=3)
        e.insert(END, "Date")
        e.configure(state="disable")
        e = CTkEntry(
            frame33,
            border_width=1,
            corner_radius=0,
            fg_color="#808080",
            border_color="#fff",
            width=60,
            text_color="white",
        )
        e.grid(row=0, column=4)
        e.insert(END, "Status")
        e.configure(state="disable")
        arr = db.fetchall()
        r = 0
        for i in arr:
            bars.append(i[1])
            r += 1
            e = CTkEntry(
                frame33,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=140,
                text_color="white",
            )
            e.grid(row=r, column=0)
            e.insert(END, str(i[1]))
            e.configure(state="disable")
            e = CTkEntry(
                frame33,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=50,
                text_color="white",
            )
            e.grid(row=r, column=1)
            e.insert(END, str(i[3]))
            e.configure(state="disable")
            e = CTkEntry(
                frame33,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=90,
                text_color="white",
            )
            e.grid(row=r, column=2)
            e.insert(END, str(i[2]))
            e.configure(state="disable")
            e = CTkEntry(
                frame33,
                border_width=1,
                corner_radius=0,
                border_color="#fff",
                width=120,
                text_color="white",
            )
            e.grid(row=r, column=3)
            e.insert(END, str(i[4]))
            e.configure(state="disable")
            db.execute(
                "SELECT score FROM history WHERE studentId =%s AND quizId=%s",
                (x[0], i[0]),
            )
            temparr = db.fetchall()
            if temparr == []:
                height.append(0)
                CTkButton(
                    frame33,
                    border_width=1,
                    corner_radius=0,
                    border_color="#fff",
                    width=60,
                    text_color="white",
                    text="Open",
                    command=lambda idtest=i[0]: starttest(idtest),
                ).grid(row=r, column=4)

            else:
                height.append(temparr[0][0])
                CTkButton(
                    frame33,
                    border_width=1,
                    corner_radius=0,
                    border_color="#fff",
                    width=60,
                    text_color="white",
                    text=str(temparr[0][0]),
                ).grid(row=r, column=4)

        y_pos = np.arange(len(bars))
        plt.bar(y_pos, height)
        plt.xticks(y_pos, bars)
        plt.savefig("graph.png")
        plt.clf()
        frame0 = tabview.tab("Statics")
        sss = CTkImage(dark_image=Image.open("asset/s.png"), size=(50, 50))
        CTkLabel(frame0, image=sss, text="").place(x=10, y=10)
        CTkLabel(
            frame0,
            font=("defult", 20),
            text=x[6],
            fg_color="transparent",
        ).place(x=25, y=50)
        ss = CTkImage(dark_image=Image.open("graph.png"), size=(400, 180))
        CTkLabel(frame0, image=ss, text="").place(x=90, y=10)
        CTkLabel(
            frame0,
            font=("defult", 20),
            text=x[6],
            fg_color="transparent",
        ).place(x=25, y=50)

    home()


start()
app.mainloop()