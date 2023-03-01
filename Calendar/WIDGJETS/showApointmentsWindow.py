from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from WIDGJETS.services.dataServices import getAppointments,getApointmentDay,deleteApointment
from WIDGJETS.editForm import editForm
columns = ('Dia','Serviço','Tempo','Inicio','Fim','ID')


def showApointment(tree,day):
    apointments = getApointmentDay(day)
    for contact in apointments:
        tree.insert('', END, values=contact)
    


def showApointments(tree):
    apointments = []
    apointments = getAppointments()
    for contact in apointments:
        tree.insert('', END, values=contact)
    
def edit(tree,root,showApointment_topLevel,day):
    # Get selected item to Edit
    selected_item = tree.selection()[0]
    item_props = tree.item(selected_item)
    editForm(root,item_props)

    
    #tree.item(selected_item, text="blub", values=data)

def delete(tree):
    selected_item = tree.selection()[0]
    item_props = tree.item(selected_item)
    item_values = item_props['values']#get the values
    day = item_values[0]
    id_number = item_values[-1]
    # Access the properties of the selected item
    deleteApointment(day,id_number)
    # Delete the selected item from the Treeview
    tree.delete(selected_item)
    

def refresh_treeview(root,tree,top_level,day):
    
    # Clear the existing data from the TreeView
    for item in tree.get_children():
        tree.delete(item)
    top_level.destroy()
    showApointmentsWindow(root,"day",day)   


def defineTreeColumns(tree):
    count = 1
    for x in columns:
        tree.column('# ' + str(count) ,anchor=CENTER)
        tree.heading('# ' +str(count) ,text=x)
        count = count + 1


def showApointmentsWindow(root,dayOrAll = "All", day = ""):
    top_level = tk.Toplevel(root)
    top_level.title("Show Apointments")
    top_level.geometry("1000x350")
    

    tree = ttk.Treeview(top_level, column=("c1", "c2","c3","c4","c5","c6"), show='headings', height=12)
   
    defineTreeColumns(tree)
    tree.pack()
    try:
        if(dayOrAll =="All"):
            showApointments(tree)
        if(dayOrAll =="day"):
            showApointment(tree,day)
    
        # Add Buttons to Edit and Delete the Treeview items
        edit_btn = ttk.Button(top_level, text="Edit", command=(lambda : edit(tree,root,top_level,day)))
        edit_btn.pack()
        del_btn = ttk.Button(top_level, text="Delete", command=(lambda : delete(tree)))
        del_btn.pack()
        refresh_btn = ttk.Button(top_level, text="Refresh", command=(lambda : refresh_treeview(root,tree,top_level,day)))
        refresh_btn.pack()
        tree.bind('<<TreeviewSelect>>', lambda event :item_selected(event,tree))
        top_level.mainloop()
    except:
        print("error")

  ### fazer o edit tree e o delete tree

def item_selected(event,tree):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
        #messagebox.showinfo(title='Information', message=','.join(record))