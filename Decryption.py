import cv2
import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main window
root = tk.Tk()
root.title("Image Decryption")

# ASCII Dictionary
c = {i: chr(i) for i in range(255)}

# Function for decryption
def decrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])
    if not file_path:
        messagebox.showerror("Error", "No image selected for decryption.")
        return

    encrypted_img = cv2.imread(file_path)
    messagebox.showinfo("Selected File", f"Decrypting image from: {file_path}")

    pas = pass_entry.get()
    if not pas:
        messagebox.showerror("Error", "Please enter a password.")
        return

    msg_length = encrypted_img[0, 0, 0]

    message = ""
    n, m = 0, 1
    for i in range(msg_length):
        message += c[encrypted_img[n, m, 0]]
        m += 1
        if m >= encrypted_img.shape[1]:
            m = 0
            n += 1

    messagebox.showinfo("Decrypted Message", "Decrypted message: " + message)

# Create GUI elements
pass_label = tk.Label(root, text="Enter Password:")
pass_label.pack()

pass_entry = tk.Entry(root, width=50, show="*")
pass_entry.pack()

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=5)

root.mainloop()
