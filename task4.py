import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tkinter import Tk, filedialog, Button, Label, StringVar, messagebox, Entry

# AES encryption/decryption utility functions
def encrypt_file(key, filename):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(filename, 'rb') as file:
        data = file.read()
    
    # Pad the data to make its length a multiple of 16
    padded_data = pad(data, AES.block_size)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Save the IV (Initialization Vector) along with the encrypted data
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    
    return iv, encrypted_data_base64

def decrypt_file(key, iv, encrypted_data):
    iv = base64.b64decode(iv)
    encrypted_data = base64.b64decode(encrypted_data)
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    # Decrypt the data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    return decrypted_data

# Functions for GUI interaction
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    file_path_var.set(file_path)

def encrypt():
    key = key_var.get().encode('utf-8')
    if len(key) < 32:
        key += b' ' * (32 - len(key))  # Padding key to 256 bits
    file_path = file_path_var.get()
    
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File does not exist")
        return

    iv, encrypted_data = encrypt_file(key, file_path)

    output_file = file_path + '.enc'
    with open(output_file, 'w') as enc_file:
        enc_file.write(f"{iv}\n{encrypted_data}")
    
    messagebox.showinfo("Success", f"File encrypted and saved as {output_file}")

def decrypt():
    key = key_var.get().encode('utf-8')
    if len(key) < 32:
        key += b' ' * (32 - len(key))  # Padding key to 256 bits
    
    file_path = file_path_var.get()
    
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File does not exist")
        return
    
    with open(file_path, 'r') as enc_file:
        iv = enc_file.readline().strip()
        encrypted_data = enc_file.read().strip()
    
    try:
        decrypted_data = decrypt_file(key, iv, encrypted_data)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")
        return
    
    output_file = file_path + '.dec'
    with open(output_file, 'wb') as dec_file:
        dec_file.write(decrypted_data)
    
    messagebox.showinfo("Success", f"File decrypted and saved as {output_file}")

# GUI Application
root = Tk()
root.title("ADVANCED ENCRYPTION TOOL")  # Update the title of the window

key_var = StringVar()
file_path_var = StringVar()

# Tool owner information
owner_label = Label(root, text="Owner: Mihir Patel", font=('Helvetica', 10, 'italic'))
owner_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

# Key input
Label(root, text="Enter encryption key (32 bytes for AES-256):").grid(row=1, column=0, sticky='w', padx=10, pady=5)
key_entry = Entry(root, textvariable=key_var, show='*', width=40)
key_entry.grid(row=1, column=1, padx=10, pady=5)

# File selection
Label(root, text="Select a file:").grid(row=2, column=0, sticky='w', padx=10, pady=5)
file_entry = Entry(root, textvariable=file_path_var, width=40)
file_entry.grid(row=2, column=1, padx=10, pady=5)
browse_button = Button(root, text="Browse", command=browse_file)
browse_button.grid(row=2, column=2, padx=10, pady=5)

# Encrypt and Decrypt buttons
encrypt_button = Button(root, text="Encrypt File", command=encrypt, width=20, bg='green', fg='white')
encrypt_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

decrypt_button = Button(root, text="Decrypt File", command=decrypt, width=20, bg='red', fg='white')
decrypt_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
