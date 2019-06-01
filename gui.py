from tkinter import *
import tkinter as tk
import html_parse
import Query
import sys

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Search Engine 2.0")
        
        self.frame_root = Frame(self.root)
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        self.frame_root.grid(row=0, column=0, sticky=N+S+E+W)
        
        self.frame = Frame(self.frame_root)
        self.frame.pack()
        self.frame.grid(sticky=N+S+E+W, column=3, row=3)
        Grid.rowconfigure(self.frame_root, 2, weight=1)
        Grid.columnconfigure(self.frame_root, 2, weight=1)
        
        for x in range(50):
            Grid.columnconfigure(self.frame, x, weight=1)
            Grid.rowconfigure(self.frame, x, weight=1)

        
        self.search_button = Button(self.frame, text='Search', bg = "blue", 
                                    command=self.start_search)
        self.search_button.grid(row=0, column=1, rowspan=2, sticky=N+S+E+W)
        
        self.search_input = tk.StringVar()
        self.search_box = Entry(self.frame, textvariable=self.search_input,
                                bd=30)
        self.search_box.grid(row=0, column=0, rowspan=2, sticky=N+S+E+W)
        
        
        self.scroll = Scrollbar(self.frame, orient="vertical")
    
        
        self.top_results = Text(self.frame, yscrollcommand=self.scroll.set)
        self.top_results.config(font=("consolas", 12), state=DISABLED,)
        
        # self.result = tk.StringVar()
        # self.results = Message(self.frame, text=" ", bd=100)
        # self.results.grid(row=2, sticky=N+S+E+W, columnspan=3)
        # self.results.config(bg='lightgreen', textvariable=self.result)
        
        self.scroll.config(command=self.top_results.yview)
        self.scroll.grid(row=2, column=3, sticky=N+S)
        self.top_results.grid(row=2, sticky=N+S+E+W, columnspan=3)
        self.top_results.config(bg='lightgreen')
        self.top_results.delete(1.0, END)
        
        self.type = IntVar()
        self.type.set(0)
        self.index_type = Radiobutton(self.frame, text="Index",
                                      variable=self.type, value=1)
        self.index_type.grid(row=0, column=2)
        self.query_type = Radiobutton(self.frame, text="Query",
                                      variable=self.type, value=2)
        self.query_type.grid(row=1, column=2)
       

        

        
    def get_search_input(self):
        return self.search_input
    
    def start_search(self):
        print(self.type.get())
        if self.type.get() == 1:
            self.top_results.delete(1.0, END)
            # OUTPUT to file called output.txt
            sys.stdout = open("output2.txt", "w")
            i = html_parse.InvertedIndex()
            i.html_parse()
            i.calculate_all_tf_idf()
            i.write_inverted_ind()
            i.write_total_docs()
            i.write_doc_length()
            
        elif self.type.get() == 2:
            self.top_results.delete(1.0, END)
            query = Query.Query(self.search_input.get())

            self.top_results.configure(state="normal")
            i = 1
            for q in query.run_query_gui():
                self.top_results.insert(END, str(i) + ". " + q + '\n\n')
                i += 1
            self.top_results.configure(state="disabled")
            
                
        self.type.set(0)

    
    def get_type_of_input(self):
        return self.type

    def run(self):
        self.root.mainloop()
        
if __name__ == '__main__':
    g = GUI()
    g.run()
