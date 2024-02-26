import tkinter as tk
from tkinter import ttk
import sqlite3

def view_data():
    # Connect to SQLite database
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Define SQL query to select all data from the table
    select_query = '''
    SELECT * FROM attendance;
    '''

    # Execute SQL query
    cursor.execute(select_query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Create a tkinter window
    root = tk.Tk()
    root.title("Attendance Data")

    # Create a treeview to display data
    tree = ttk.Treeview(root)
    tree["columns"] = ("ID", "Employee Number", "Clock In Time", "Clock Out Time", "Entry Location", "Leaving Location", "Time Duration")
    tree.heading("#0", text="ID")
    tree.column("#0", minwidth=0, width=50, stretch=tk.NO)
    for col in tree["columns"]:
        tree.heading(col, text=col)

    # Insert data into the treeview
    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(expand=tk.YES, fill=tk.BOTH)

    # Start the tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    view_data()
