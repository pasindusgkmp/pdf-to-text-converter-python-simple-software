import tkinter as tk
from tkinter import filedialog, scrolledtext
from PyPDF2 import PdfReader

def convert_pdf_to_text():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    pdf_text = ""
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

    text_area.delete(1.0, tk.END)  # Clear previous text
    text_area.insert(tk.END, pdf_text)

def save_text_to_file():
    text_to_save = text_area.get(1.0, tk.END)
    if not text_to_save.strip():
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as text_file:
        text_file.write(text_to_save)

# Create the main window
window = tk.Tk()
window.title("PDF to Text Converter")

# Upload File button
upload_button = tk.Button(window, text="Upload File", command=convert_pdf_to_text)
upload_button.grid(row=0, column=0, padx=20, pady=10)

# Save Text button
save_button = tk.Button(window, text="Save Text", command=save_text_to_file)
save_button.grid(row=0, column=1, padx=20, pady=10)

# Text Area for converted text
text_area = scrolledtext.ScrolledText(window, width=80, height=20)
text_area.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

# Run the Tkinter event loop
window.mainloop()
