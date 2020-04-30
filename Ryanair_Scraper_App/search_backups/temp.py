# Multi-frame tkinter application v2.3
import tkinter as tk
from pandastable import Table
from ryanair_scraper_bot import ryanair_bot

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ryanair Scrapper")
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    
    
    def __init__(self, master):
        
        def close_app():
            self.destroy()
            
        def run_app():
            user_city_from = str(from_city_entry.get())
            user_budget = str(budget_entry.get())
            user_date_depart = str(departure_date_entry.get())
            user_date_return = str(return_date_entry.get())
            
            bot = ryanair_bot()
            bot.start_ryanair(user_city_from, user_date_depart, user_date_return, user_budget)
            master.switch_frame(PageOne)
        
        tk.Frame.__init__(self, master)
        frame_header = tk.Frame(master = self, borderwidth=2, pady=2)
        center_frame = tk.Frame(self, borderwidth=2, pady=5)
        bottom_frame = tk.Frame(self, borderwidth=2, pady=5)
        results_frame = tk.Frame(self, borderwidth=2, pady=5)
        frame_header.grid(row=0, column=0)
        center_frame.grid(row=1, column=0)
        bottom_frame.grid(row=2, column=0)
        results_frame.grid(row=2, column=0)
        
        header = tk.Label(frame_header, text = "RYANAIR SCRAPER TOOL", bg='blue', fg='yellow', height='3', width='70', font=("Helvetica 16 bold"))
        header.grid(row=0, column=0)
        
        frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
        frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
        
        from_city = tk.Label(frame_main_1, text = "      FROM:        ")
        budget = tk.Label(frame_main_1, text = "                                    BUDGET:      ")
        departure_date = tk.Label(frame_main_2, text = "    DEPARTURE DATE:")
        return_date = tk.Label(frame_main_2, text = "     RETURN DATE:")
        
        from_city1 = tk.StringVar()
        budget1 = tk.StringVar()
        departure_date1 = tk.StringVar()
        return_date1 = tk.StringVar()
        
        from_city_entry = tk.Entry(frame_main_1, textvariable = from_city1, width=4)
        budget_entry = tk.Entry(frame_main_1, textvariable = budget1, width=4)
        
        departure_date_entry = tk.Entry(frame_main_2, textvariable = departure_date1, width=12)
        return_date_entry = tk.Entry(frame_main_2, textvariable = return_date1, width=12)
        
        button_run = tk.Button(bottom_frame, text="Start",command=run_app , bg='green', fg='black', relief='raised', width=10, font=('Helvetica 9 bold'))
        button_run.grid(column=0, row=0, sticky='w', padx=100, pady=2)
        
        button_close = tk.Button(bottom_frame, text="Exit", command=close_app, bg='red', fg='black', relief='raised', width=10, font=('Helvetica 9'))
        button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)
        
        frame_main_1.pack(fill='x', pady=2)
        frame_main_2.pack(fill='x',pady=2)
        from_city.pack(side="left")
        from_city_entry.pack(side='left', padx=1)
        departure_date.pack(side='left', padx=5)
        departure_date_entry.pack(side='left')
        budget.pack(side='left')
        budget_entry.pack(side='left', padx=1)
        return_date_entry.pack(side='right')
        return_date.pack(side='right', padx=5)



class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        df = ryanair_bot.create_df()
        self.table = pt = Table(tk.Frame, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()