import tkinter as tk
import pymongo

#Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["PythonChat"]
messages_col = db["messages"]


# GUI
root = tk.Tk()
root.title("Python Chat")
root.geometry("300x300")


entry = tk.Entry(root, width=40)
entry.pack(pady=5)


root.mainloop()




# git status
# git add .
# git commit -m"<Kommentar>"
# git push