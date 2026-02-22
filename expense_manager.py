import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

FILE="expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_data():
    with open(FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)

def valid_amount(v):
    try:
        x=float(v)
        return x>0
    except:
        return False

def refresh_list():
    tree.delete(*tree.get_children())
    q=search_var.get().lower()
    for i,e in enumerate(data):
        text=f"{e['amount']} {e['category']} {e['date']} {e['note']}".lower()
        if q in text:
            tree.insert("", "end", iid=str(i), values=(
                i+1,
                f"{e['amount']:.2f}",
                e["category"],
                e["date"],
                e["note"]
            ))
    update_stats()

def update_stats():
    total=sum(e["amount"] for e in data)
    now=datetime.now().strftime("%Y-%m")
    month=sum(e["amount"] for e in data if e["date"].startswith(now))
    cat=defaultdict(float)
    for e in data:
        cat[e["category"]]+=e["amount"]
    high=max(cat,key=cat.get) if cat else "-"
    total_lbl.config(text=f"Total: {total:.2f}")
    month_lbl.config(text=f"This Month: {month:.2f}")
    cat_lbl.config(text=f"Top Category: {high}")

def clear_inputs():
    amount_var.set("")
    cat_var.set("")
    date_var.set(datetime.now().strftime("%Y-%m-%d"))
    note_var.set("")

def add():
    a=amount_var.get().strip()
    c=cat_var.get().strip()
    d=date_var.get().strip()
    n=note_var.get().strip()
    if not valid_amount(a):
        messagebox.showerror("Error","Amount must be positive number")
        return
    if not c:
        messagebox.showerror("Error","Category required")
        return
    if not d:
        d=datetime.now().strftime("%Y-%m-%d")
    data.append({"amount":float(a),"category":c,"date":d,"note":n})
    save_data()
    refresh_list()
    clear_inputs()

def selected_index():
    s=tree.selection()
    if not s: return None
    return int(s[0])

def delete():
    i=selected_index()
    if i is None: return
    if i<len(data):
        del data[i]
        save_data()
        refresh_list()

def edit():
    i=selected_index()
    if i is None or i>=len(data): return
    a=amount_var.get().strip()
    c=cat_var.get().strip()
    d=date_var.get().strip()
    n=note_var.get().strip()
    if not valid_amount(a):
        messagebox.showerror("Error","Amount must be positive number")
        return
    if not c:
        messagebox.showerror("Error","Category required")
        return
    data[i]={"amount":float(a),"category":c,"date":d,"note":n}
    save_data()
    refresh_list()

def on_select(e):
    i=selected_index()
    if i is None or i>=len(data): return
    x=data[i]
    amount_var.set(str(x["amount"]))
    cat_var.set(x["category"])
    date_var.set(x["date"])
    note_var.set(x["note"])

def clear_all():
    if messagebox.askyesno("Confirm","Clear all expenses?"):
        data.clear()
        save_data()
        refresh_list()

def focus_search(e=None):
    search_entry.focus_set()

def charts():
    if not data:
        messagebox.showinfo("Info","No data")
        return
    cat=defaultdict(float)
    mon=defaultdict(float)
    for e in data:
        cat[e["category"]]+=e["amount"]
        m=e["date"][:7]
        mon[m]+=e["amount"]
    plt.figure()
    plt.bar(list(cat.keys()),list(cat.values()))
    plt.title("Spending by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.figure()
    ks=sorted(mon.keys())
    plt.bar(ks,[mon[k] for k in ks])
    plt.title("Monthly Spending")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

root=tk.Tk()
root.title("Personal Expense Manager By Ayush Prabhakhar")
root.geometry("900x520")

data=load_data()

top=tk.Frame(root,padx=10,pady=10)
top.pack(fill="x")

amount_var=tk.StringVar()
cat_var=tk.StringVar()
date_var=tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
note_var=tk.StringVar()
search_var=tk.StringVar()

tk.Label(top,text="Amount").grid(row=0,column=0,sticky="w")
tk.Entry(top,textvariable=amount_var,width=12).grid(row=1,column=0,padx=5)

tk.Label(top,text="Category").grid(row=0,column=1,sticky="w")
tk.Entry(top,textvariable=cat_var,width=14).grid(row=1,column=1,padx=5)

tk.Label(top,text="Date (YYYY-MM-DD)").grid(row=0,column=2,sticky="w")
tk.Entry(top,textvariable=date_var,width=14).grid(row=1,column=2,padx=5)

tk.Label(top,text="Note").grid(row=0,column=3,sticky="w")
tk.Entry(top,textvariable=note_var,width=22).grid(row=1,column=3,padx=5)

btns=tk.Frame(top)
btns.grid(row=1,column=4,padx=8)

tk.Button(btns,text="Add Expense",command=add,width=14).pack(pady=1)
tk.Button(btns,text="Edit Selected",command=edit,width=14).pack(pady=1)
tk.Button(btns,text="Delete Selected",command=delete,width=14).pack(pady=1)
tk.Button(btns,text="Clear All",command=clear_all,width=14).pack(pady=1)
tk.Button(btns,text="Show Analytics",command=charts,width=14).pack(pady=1)

mid=tk.Frame(root,padx=10)
mid.pack(fill="both",expand=True)

tk.Label(mid,text="Search").pack(anchor="w")
search_entry=tk.Entry(mid,textvariable=search_var)
search_entry.pack(fill="x",pady=4)
search_var.trace_add("write",lambda *a:refresh_list())

cols=("No","Amount","Category","Date","Note")
tree=ttk.Treeview(mid,columns=cols,show="headings")
for c in cols:
    tree.heading(c,text=c)
tree.column("No",width=50,anchor="center")
tree.column("Amount",width=90,anchor="e")
tree.column("Category",width=150)
tree.column("Date",width=110)
tree.column("Note",width=300)
tree.pack(side="left",fill="both",expand=True)

scroll=ttk.Scrollbar(mid,command=tree.yview)
scroll.pack(side="right",fill="y")
tree.configure(yscrollcommand=scroll.set)
tree.bind("<<TreeviewSelect>>",on_select)

bottom=tk.Frame(root,padx=10,pady=6)
bottom.pack(fill="x")

total_lbl=tk.Label(bottom,text="Total: 0")
total_lbl.pack(side="left",padx=10)

month_lbl=tk.Label(bottom,text="This Month: 0")
month_lbl.pack(side="left",padx=10)

cat_lbl=tk.Label(bottom,text="Top Category: -")
cat_lbl.pack(side="left",padx=10)

root.bind("<Return>",lambda e:add())
root.bind("<Delete>",lambda e:delete())
root.bind("<Control-f>",focus_search)

refresh_list()
root.mainloop()