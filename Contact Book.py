import tkinter as tk
from tkinter import messagebox, simpledialog

# -------------------------------
# CONTACT BOOK APPLICATION
# -------------------------------
# Features:
# 1. Add Contact (name, phone, email, address)
# 2. View All Contacts
# 3. Search Contact (by name or phone)
# 4. Update Contact
# 5. Delete Contact
# 6. Simple, user-friendly interface
# -------------------------------

# Contact storage (list of dictionaries)
contacts = []


def add_contact():
    """Add a new contact to the list."""
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    clear_entries()
    refresh_contact_list()


def view_contacts():
    """Display all contacts in the listbox."""
    refresh_contact_list()


def search_contact():
    """Search contacts by name or phone number."""
    query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
    if not query:
        return

    results = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"]]

    listbox.delete(0, tk.END)
    if results:
        for c in results:
            listbox.insert(tk.END, f"{c['name']} - {c['phone']}")
    else:
        messagebox.showinfo("No Results", "No contact found!")


def update_contact():
    """Update selected contact."""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return

    index = selected[0]
    contact = contacts[index]

    # Ask for new values
    new_name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact["name"])
    new_phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact["phone"])
    new_email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact["email"])
    new_address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact["address"])

    # Update contact details
    contacts[index] = {
        "name": new_name or contact["name"],
        "phone": new_phone or contact["phone"],
        "email": new_email or contact["email"],
        "address": new_address or contact["address"],
    }

    messagebox.showinfo("Updated", "Contact updated successfully!")
    refresh_contact_list()


def delete_contact():
    """Delete the selected contact."""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return

    index = selected[0]
    contact = contacts[index]
    confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{contact['name']}'?")
    if confirm:
        del contacts[index]
        refresh_contact_list()
        messagebox.showinfo("Deleted", "Contact deleted successfully!")


def refresh_contact_list():
    """Refresh the contact list display."""
    listbox.delete(0, tk.END)
    for c in contacts:
        listbox.insert(tk.END, f"{c['name']} - {c['phone']}")


def clear_entries():
    """Clear input fields."""
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# -------------------------------
# GUI DESIGN
# -------------------------------

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Title Label
tk.Label(root, text="📒 Contact Book", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

# Input Frame
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Name:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame_input, text="Phone:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_phone = tk.Entry(frame_input, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(frame_input, text="Email:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(frame_input, width=30)
entry_email.grid(row=2, column=1)

tk.Label(frame_input, text="Address:", bg="#f0f0f0", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_address = tk.Entry(frame_input, width=30)
entry_address.grid(row=3, column=1)

# Button Frame
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add", width=10, bg="#4CAF50", fg="white", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="View All", width=10, bg="#2196F3", fg="white", command=view_contacts).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Search", width=10, bg="#9C27B0", fg="white", command=search_contact).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Update", width=10, bg="#FF9800", fg="white", command=update_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Delete", width=10, bg="#F44336", fg="white", command=delete_contact).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Clear", width=10, bg="#607D8B", fg="white", command=clear_entries).grid(row=1, column=2, padx=5, pady=5)

# Contact Listbox
listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Footer
tk.Label(root, text="© 2025 Contact Book App", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)

# Run the application
root.mainloop()
