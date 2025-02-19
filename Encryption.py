# encryption.py
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

# Create the main window
root = tk.Tk()
root.title("Image Encryption")

# Global variables
img = None
password = None
msg_length = None

# ASCII Dictionary
d = {chr(i): i for i in range(255)}

# Function to load an image
def load_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        img = cv2.imread(file_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        
        # Show the image in the window
        img_label.config(image=img_tk)
        img_label.image = img_tk

# Function for encryption
def encrypt_image():
    global img, password, msg_length
    if img is None:
        messagebox.showerror("Error", "Please load an image first.")
        return

    msg = msg_entry.get()
    password = pass_entry.get()
    
    if not msg or not password:
        messagebox.showerror("Error", "Please enter a message and a password.")
        return

    msg_length = len(msg)
    encrypted_img = img.copy()

    if msg_length > (encrypted_img.shape[0] * encrypted_img.shape[1]):
        messagebox.showerror("Error", "Message too long for the selected image.")
        return

    encrypted_img[0, 0, 0] = msg_length

    n, m = 0, 1
    for i in range(msg_length):
        encrypted_img[n, m, 0] = d[msg[i]]
        m += 1
        if m >= encrypted_img.shape[1]:
            m = 0
            n += 1

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not save_path:
        return
    
    cv2.imwrite(save_path, encrypted_img)
    messagebox.showinfo("Success", f"Image encrypted successfully. Saved at: {save_path}")

# Create GUI elements
msg_label = tk.Label(root, text="Enter Secret Message:")
msg_label.pack()

msg_entry = tk.Entry(root, width=50)
msg_entry.pack()

pass_label = tk.Label(root, text="Enter Password:")
pass_label.pack()

pass_entry = tk.Entry(root, width=50, show="*")
pass_entry.pack()

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=5)

img_label = tk.Label(root)
img_label.pack()

root.mainloop()
