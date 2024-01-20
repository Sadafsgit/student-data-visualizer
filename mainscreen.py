from tkinter import font  as tkfont  # python 3
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # This library is for embading graphg window in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
from PIL import Image, ImageTk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Student Mark Data Visualizer")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)


        self.config(menu=menubar)
    def donothing(self):
        pass
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="light sky blue")

        self.controller = controller
        self.controller.title("Data Visualizer")
        self.controller.resizable(0, 0)
        self.controller.state("zoomed")

        self.welcome_label_frame = tk.LabelFrame(self, text="", bg='deep sky blue')
        # self.welcome_label_frame.place(x=10, y=10, height=400, relwidth=1,pady=10)
        self.welcome_label_frame.pack(padx=20,pady=20,expand=True,fill=tk.BOTH)
        welcome_label = tk.Label(self.welcome_label_frame,
                                 text="Welcome",
                                 font=("verdana", 45, 'bold'),
                                 # image=render,
                                 background="deep sky blue"
                                 )
        welcome_label.place(relx=0.4)

        caption_label1 = tk.Label(self.welcome_label_frame,
                                  text="Hello,This is the free graph making tool to visualize csv "
                                       "file and data visualize your data.This software is developed "
                                       "in the Python prpgramming language..", background="deep sky blue",
                                  font=('Times', '16'))
        caption_label2 = tk.Label(self.welcome_label_frame, text="The plotting of the data is "
                                                                 "done by using Matplotlib library of the python",
                                  font=('Times', '16'), background="deep sky blue")
        caption_label3 = tk.Label(self.welcome_label_frame,
                                  text="The Python 'Dictionary' Datastructure which is key-value pair data "
                                       "structure is used to store data whenever required.", background="deep sky blue",
                                  font=('Times', '16'),
                                  )
        caption_label1.place(x=30, rely=0.3)
        caption_label2.place(x=30, rely=0.38)
        caption_label3.place(x=30, rely=0.46)


        file_button = tk.Button(self.welcome_label_frame, text="Visualize by Excel Sheet Data",bg='light sky blue',font=('Times', '16',),
                                borderwidth=3,
                                command=lambda: controller.show_frame("PageTwo"))
        file_button.place(relx=0.3,rely=0.7)

        manual_button = tk.Button(self.welcome_label_frame, text="Visualize manually", bg='light sky blue',
                                  font=('Times', '16',), borderwidth=3,
                                  command=lambda: controller.show_frame("PageOne"))
        manual_button.place(relx=0.5, rely=0.7)

        def raise_frame(self, frame):
            frame.tkraise()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        bg = tk.PhotoImage(file="C:/Users/Sattya/Downloads/jpg2png/dataBc.png")
        self.bg = bg
        tk.Frame.__init__(self, parent, bg="darkorange")
        self.controller = controller
        self.keyss = {}
        bg = tk.PhotoImage(file="C:/Users/Sattya/Downloads/jpg2png/dataBc.png")
        self.bg = bg
        combostyle = ttk.Style()
        # self.drop=drop
        combostyle.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                              {'configure':
                                                   {'selectbackground': 'blue',
                                                    'fieldbackground': '#3d3d5c',
                                                    'background': 'green'
                                                    }}}
                                )
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        combostyle.theme_use('combostyle')
        subject = ["Math", 'physics', 'Chemistry', 'Biology', 'Marathi', 'Hindi', 'Environment', 'socialscience']
        clicked = tk.StringVar()
        self.clicked = clicked
        clicked.set(subject[0])

        notice = tk.Label(self,

                          text="Select the subject and Enter the Marks",
                          font=("verdana", 30, 'bold',),
                          foreground="black",
                          background="darkorange")
        notice.place(x=290, y=150)

        drop = tk.OptionMenu(self, clicked, *subject, )
        drop.config(bg='Black', foreground="white", font=(25))
        self.drop = drop
        drop.place(x=500, y=240, height=50, width=200)

        sub = tk.Entry(self,
                       text="Enter",
                       width=22,
                       background="orange",
                       foreground='white')
        sub.place(x=10,
                  y=10,
                  width=200,
                  height=50)
        sub.insert(0, "Enter Marks")
        sub.place(x=800, y=240)
        self.sub = sub

        btn1 = tk.Button(self, text="Plot"
                         , background="orange",
                         foreground="white",
                         font='Helvetica',
                         relief='raised',
                         # command=self.get_statistics,
                         command=self.plott
                         # command=lambda: controller.show_frame("StartPage")

                         )
        btn1.place(x=350, y=245)

        btn3 = tk.Button(self, text="Submit"
                         , background="orange",
                         foreground="white",
                         font='Helvetica',
                         command=self.Taking_input_

                         )
        btn3.place(x=1050, y=245)

        btn4 = tk.Button(self, text="reset"
                         , background="orange",
                         foreground="white",
                         font='Helvetica',
                         command=self.reset
                         )
        btn4.pack()


        btn6 = tk.Button(self, text="Statistics details"
                         , background="orange",
                         foreground="white",
                         font='Helvetica',
                         command=self.get_statistics
                         # command=self.creating_plot)
                         )
        btn6.place(x=950, y=350, height=50, width=200)

        # This Block is for the Optionmenu of the user choice for graph
        secClicked = tk.StringVar()
        self.secClicked = secClicked
        plotgraph = ["Scatter Plot", "Bar Graph", "Piechart", "Line Graph"]
        secClicked.set(plotgraph[1])
        drop2 = tk.OptionMenu(self, secClicked, *plotgraph)
        drop2.config(bg='orange', foreground="white", font=(25))
        self.drop2 = drop2
        drop2.place(x=650, y=350, height=50, width=200)

        # T = tk.Text(self, borderwidth=10,width=50,bg="darkorange", fg="black",insertborderwidth=10,state='normal')
        # self.T = T
        # T.place(x=950, y=350)
        # T.config(font=("Courier", 14),height=50)


        bk_btn=tk.Button(self,text="Back",bg="orange",command=lambda:controller.show_frame('StartPage')).pack()
    def Taking_input_(self):
        if self.sub.get() == "":
            messagebox.showerror("Error", "Please Enter Marks")

        else:
            try:
                self.keyss[self.clicked.get()] = float(self.sub.get())

                self.input_string = f"{self.clicked.get()} : {self.sub.get()}\n"
                # self.T.insert(tk.END, self.input_string)

            except ValueError:
                messagebox.showerror("Error", "Marks should be number ")

    def creating_plot(self):
        dic = self.keyss

        if self.secClicked.get() == "Scatter Plot":
            figure = plt.figure(figsize=(5, 4), dpi=100, facecolor='darkorange')
            figure.add_subplot(111).scatter(dic.keys(), dic.values())
            chart = FigureCanvasTkAgg(figure, self)
            plt.xlabel("Subject")
            plt.ylabel("Marks of the student")
            plt.show()
        elif self.secClicked.get() == "Bar Graph":
            figure = plt.figure(figsize=(5, 4), dpi=100, facecolor='darkorange')
            figure.add_subplot(111).bar(dic.keys(), dic.values(), color="black", label="Marks")
            chart = FigureCanvasTkAgg(figure, self)
            plt.title(self.sub.get())
            plt.xlabel("Subject", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
            plt.ylabel("Marks of the student", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.legend()
            plt.show()
        elif self.secClicked.get() == "Line Graph":
            figure = plt.figure(figsize=(5, 4), dpi=100, facecolor='darkorange')
            figure.add_subplot(111).plot(dic.keys(), dic.values(), color="black")
            chart = FigureCanvasTkAgg(figure, self)
            plt.xlabel("Subject")
            plt.ylabel("Marks of the student")
            # ax = plt.axes()
            # ax.set_facecolor("orange")

            plt.show()
        else:
            figure = plt.figure(figsize=(5, 4), dpi=100, facecolor='black')
            figure.add_subplot(111).pie(dic.values())
            chart = FigureCanvasTkAgg(figure, self)
            plt.title(self.sub.get())
            plt.show()

        # self.T.insert(tk.END, self.average, self.mode)

    def reset(self):
        self.keyss = {}
        self.T.delete(1.0, 1.0)

    def plott(self):
        if self.secClicked.get() == "Bar Graph":
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='darkorange')
            a = f.add_subplot(111)
            a.bar(self.keyss.keys(), self.keyss.values(), color="midnightblue", label="marks")
            plt.title("Sattya", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel("mrks of the student", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel("Subjects", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=500, y=60)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(width=250, y=800)
            toolbar.update()
            # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.place(x=10, y=330)
        elif self.secClicked.get() == "Scatter Plot":
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='darkorange')
            a = f.add_subplot(111)
            a.scatter(self.keyss.keys(), self.keyss.values(), color="midnightblue", label="marks")
            plt.title("Sattya", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel("mrks of the student", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel("Subjects", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=500, y=60)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(width=250, y=800)
            toolbar.update()
            # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.place(x=10, y=330)
        elif self.secClicked.get() == "Line Graph":
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='darkorange')
            a = f.add_subplot(111)
            a.plot(self.keyss.keys(), self.keyss.values(), color="midnightblue", label="marks")
            plt.title("Sattya", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel("mrks of the student", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel("Subjects", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=500, y=60)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(width=250, y=800)
            toolbar.update()
            # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.place(x=10, y=330)
        else:
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='darkorange')
            a = f.add_subplot(111)
            a.pie(self.keyss.values(), wedgeprops={"edgecolor": "black",
                                                   'linewidth': 2,
                                                   'antialiased': True},
                  labels=self.keyss.keys(), autopct='%1.1f%%', )
            plt.title("Mark Vs Subject", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=500, y=60)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(width=250, y=800)
            toolbar.update()
            # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas._tkcanvas.place(x=10, y=330)

    def get_statistics(self):

        dic = list(self.keyss.values())
        val = self.keyss.keys()
        average = sum(dic) / len(dic)
        mode = max(dic)
        total = 100 * len(dic)
        percentage = (sum(dic) * 100) / total
        median = 0
        if len(sorted(dic)) % 2 != 0:
            try:
                median_index = len(dic) // 2 + 1
                median = dic[median_index]
            except IndexError:
                median = dic[0]

        l1_frame = tk.LabelFrame(self, text="Statistics details are as follows", bg="orange",
                                 font=("Times", "18", "bold italic"))
        l1_frame.pack()
        left = tk.Label(l1_frame, text=f"Average : {average}", bg="orange", font=("Times", "15", "bold italic"))
        left2 = tk.Label(l1_frame, text=f"Maximum : {median}", bg="orange", font=("Times", "15", "bold italic"))
        left3 = tk.Label(l1_frame, text=f"Percentage : {percentage}", bg="orange", font=("Times", "15", "bold italic"))
        left.pack()
        left2.pack()
        left3.pack()

        l1_frame.place(x=950, y=450, height=150, width=400)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame2 = tk.LabelFrame(self, text="Spreadsheet", bg='orange')
        frame2.place(height=590, width=1000)
        ttk.Style().configure("Treeview", background='black', fieldbackground='black', foreground='white')

        self.frame1 = tk.LabelFrame(self, text="open file", bg='deep sky blue')
        self.frame1.place(height=300, width=400, rely=0.7, x=0)

        self.stat_frame = tk.LabelFrame(self, text="Statistical Details", bg='deep sky blue')
        self.stat_frame.place(width=600, x=400, y=590, relheight=1)

        btn1 = tk.Button(self.frame1, text="Browse file",

                         command=lambda: self.open_file(),
                         )
        btn1.place(rely=0.15, relx=0.3)
        btn1.config(bg="black", foreground="white")

        btn2 = tk.Button(self.frame1, text="View File",
                         command=lambda: self.load_file,

                         )
        btn2.place(rely=0.15, relx=0.5)
        btn2.config(bg="black", foreground="white")

        self.label_file = tk.Label(self.frame1, text="No file selected.Please browse the file and then load it to view",
                                   bg='deep sky blue')
        self.label_file.place(x=0, y=5)

        tv1 = ttk.Treeview(frame2, )
        tv1.place(relwidth=1, relheight=1)
        tree_scroll = tk.Scrollbar(frame2, )
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tv1.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=tv1.yview)

        tscrollX = tk.Scrollbar(frame2, orient='horizontal')
        tscrollX.pack(side=tk.BOTTOM, fill=tk.X)
        tv1.configure(xscrollcommand=tscrollX.set)
        tscrollX.config(command=tv1.xview)


        self.tv1 = tv1

        btn4 = tk.Button(self.stat_frame, text="plot",
                         command=self.line_plot,
                         # command=self.statistics
                         )
        btn4.place(relx=0.9, y=60, width=60)
        btn4.config(bg='black', fg='white', )

        btn5 = tk.Button(self.stat_frame, text="Get Stat",

                         command=self.statistics
                         )
        btn5.place(relx=0.9, y=90, width=60, )
        btn5.config(bg='black', fg='white')

        self.pl = tk.StringVar()
        plot_graph = ["Scatter Plot", "Bar Graph", "Horizontal Bar","Histogram", "Line Graph"]
        self.pl.set(plot_graph[1])
        self.plotdrop = tk.OptionMenu(self.stat_frame, self.pl, *plot_graph)
        self.plotdrop.config(bg='black', foreground="orange")
        self.plotdrop.place(relx=0.85, y=20)

        self.graph_frame = tk.LabelFrame(self, text="Graph", bg='deep sky blue')
        self.graph_frame.place(x=1000, y=0, width=600, height=1000, )


        back_btn=tk.Button(self.graph_frame,text="Back",bg="DodgerBlue3",borderwidth=3,command=lambda:controller.show_frame("StartPage"))
        back_btn.place(relx=0.8,rely=0.8)

    def open_file(self):

        filename = askopenfilename(initialdir="/", title="Select a file", filetypes=[('Python Files', '.csv .xls',), ])
        self.label_file["text"] = filename
        print(filename)

    @property
    def load_file(self):
        filepath = self.label_file["text"]
        filename = r"{}".format(filepath)
        try:
            filename = r"{}".format(filepath)
            self.df = pd.read_csv(filename)
        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {filename}")
            return None

        # Previous spreadsheets are deleted and new one is created
        self.clear_data()

        self.tv1["column"] = list(self.df.columns)
        self.tv1["show"] = "headings"

        for column in self.tv1["column"]:
            self.tv1.heading(column, text=column, anchor=tk.W)

        df_rows = self.df.to_numpy().tolist()
        for row in df_rows:
            self.tv1.insert("", "end", values=row)

        self.take_attribute()
        self.statistics()

    def take_attribute(self):
        # frame3 = tk.LabelFrame(self, text="Select attribute to plot",)
        # frame3.place(x=10, y=700, height=100, width=400)
        self.secClicked = tk.StringVar()
        self.sec = tk.StringVar()

        plotgraph = list(self.df.columns)
        self.secClicked.set(plotgraph[1])
        self.sec.set(plotgraph[2])
        drop2 = tk.OptionMenu(self.frame1, self.secClicked, *plotgraph, )
        drop2.config(bg="black", foreground="white")
        drop3 = tk.OptionMenu(self.frame1, self.sec, *plotgraph)
        drop3.config(bg="black", foreground="white")
        drop2.place(rely=0.5, relx=0.5, height=30, width=110)
        drop3.place(rely=0.5, relx=0.1, height=30, width=110)

        notice = tk.Label(self.frame1, text="Select the column that you want to compare in graph ",
                          bg='deep sky blue').place(x=0, rely=0.32)
        notice2 = tk.Label(self.frame1,
                           text="For X axis and Y axis respectively", bg='deep sky blue').place(
            x=0, rely=0.39)
        vurses_label = tk.Label(self.frame1, text='Vs', bg='deep sky blue')
        vurses_label.place(relx=0.42, rely=0.52)

        drop2.place(rely=0.52, relx=0.5, height=30, width=110)
        drop3.place(rely=0.52, relx=0.1, height=30, width=110)

        try:
            self.clear_frame()
        except AttributeError:
            pass

    def clear_data(self):
        self.tv1.delete(*self.tv1.get_children())

    def line_plot(self):
        if self.pl.get() == 'Line Graph':
            # Label string is for title of the grph
            label_string = f"{self.sec.get()} Vs {self.secClicked.get()}"
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='tab:cyan')
            a = f.add_subplot(111)
            a.plot(self.df[self.sec.get()], self.df[self.secClicked.get()], )

            plt.title(label_string, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel(self.secClicked.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel(self.sec.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=1000, height=600)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(x=1200, width=250, y=600)
            toolbar.update()

        elif self.pl.get() == 'Bar Graph':
            print(self.pl.get())
            # Label string is for title of the grph
            label_string = f"{self.sec.get()} Vs {self.secClicked.get()}"
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='lightskyblue')
            plt.style.use('ggplot')
            a = f.add_subplot(111)
            a.bar(self.df[self.sec.get()], self.df[self.secClicked.get()], color='midnightblue')

            plt.title(label_string, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel(self.secClicked.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel(self.sec.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=1000, height=600)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(x=1200, width=250, y=600)
            toolbar.update()
        elif self.pl.get() == 'Scatter Plot':
            print(self.pl.get())
            # Label string is for title of the grph
            label_string = f"{self.sec.get()} Vs {self.secClicked.get()}"
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='tab:purple')
            a = f.add_subplot(111)
            a.scatter(self.df[self.sec.get()], self.df[self.secClicked.get()], color='black', marker='.')

            plt.title(label_string, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel(self.secClicked.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel(self.sec.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=1000, height=600)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(x=1200, width=250, y=600)
            toolbar.update()

        elif self.pl.get() == 'Horizontal Bar':
            label_string = f"{self.sec.get()} Vs {self.secClicked.get()}"
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='tab:cyan')
            a = f.add_subplot(111)
            a = f.add_subplot(111)
            a.barh(self.df[self.sec.get()], self.df[self.secClicked.get()], color='green', )

            plt.title(label_string, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel(self.secClicked.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel(self.sec.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=1000, height=600)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(x=1200, width=250, y=600)
            toolbar.update()
            # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        else:
            label_string = f"{self.sec.get()} Vs {self.secClicked.get()}"
            f = plt.figure(figsize=(5, 4), dpi=110, facecolor='tab:cyan')
            a = f.add_subplot(111)
            a = f.add_subplot(111)
            a.hist(self.df[self.sec.get()] , )

            plt.title(label_string, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15})
            plt.ylabel(self.secClicked.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15},
                       color="midnightblue")
            plt.xlabel(self.sec.get(), fontdict={'fontname': 'Comic Sans MS', 'fontsize': 15}, color="midnightblue")

            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
            canvas.get_tk_widget().place(x=1000, height=600)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.place(x=1200, width=250, y=600)
            toolbar.update()

        self.statistics()

    def statistics(self):
        self.stat_for_x = f"Statistics for {self.sec.get()} :\n\n {self.df[self.sec.get()].describe()}"
        self.stat_for_y = f"Statistics for{self.secClicked.get()} :\n\n {self.df[self.secClicked.get()].describe()}"
        self.statX = tk.Label(self.stat_frame, text=self.stat_for_x, bg='deep sky blue')
        self.statX.place(relx=0, y=20)
        self.statY = tk.Label(self.stat_frame, text=self.stat_for_y, bg='deep sky blue')
        self.statY.place(relx=0.3, y=20)

        pass

    def clear_frame(self):
        self.statX.destroy()
        self.statY.destroy()
        self.df_stat_label.destroy()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
