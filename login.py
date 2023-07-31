import customtkinter as ctk


def click():
    print('login!')


root = ctk.CTk()
root.geometry('400x250')

label = ctk.CTkLabel(root, text='Login')
entry1 = ctk.CTkEntry(root, placeholder_text='User')
entry2 = ctk.CTkEntry(root, placeholder_text='Password', show='*')
checkbox = ctk.CTkCheckBox(root, text='Remember')
button = ctk.CTkButton(root, text='Login', command=click)

label.pack(padx=10, pady=10)
entry1.pack(padx=10, pady=10)
entry2.pack(padx=10, pady=10)
checkbox.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)

root.mainloop()
