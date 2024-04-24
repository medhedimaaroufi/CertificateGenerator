import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
import os
import platform

# Declare entry widgets as global variables
names_entry = None
template_entry = None
font_entry = None
font_file_entry = None
output_entry = None
test_fonts_var = None
progress_bar = None

def Capital_letter(name):
    name = name.split(" ")
    for i in range(len(name)):
        name[i] = name[i].capitalize()
    name = " ".join(name)
    return name

def generate_certificate(name, template_path, font, output_dir):
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    if len(name) > 15:
        font_size = 150
    else:
        font_size = 180

    font = ImageFont.truetype(font, font_size)

    text_width, text_height = draw.textsize(name, font=font)
    text_x = (template.width - text_width) / 2 - 10
    text_y = (template.height - text_height) / 2

    draw.text((text_x, text_y), Capital_letter(name), fill=(0, 0, 0), font=font)

    output_path = os.path.join(output_dir, f'{Capital_letter(name)}_certificate.png')
    template.save(output_path)

def generate_certificates(root):
    global names_entry, template_entry, font_entry, font_file_entry, output_entry, test_fonts_var, progress_bar

    names_file = names_entry.get()
    if not names_file:
        names_file = filedialog.askopenfilename(title="Select Names File")
        if not names_file:
            return

    names = open(names_file, "r").read().splitlines()
    
    template_path = template_entry.get()
    if not template_path:
        template_path = filedialog.askopenfilename(title="Select Certificate Template")
        if not template_path:
            return

    font_folder = font_file_entry.get()
    if not font_folder:
        font_folder = filedialog.askdirectory(title="Select Font Folder")
        if not font_folder:
            return

    filename = font_file_entry.get()
    if not filename:
        filename = filedialog.askopenfilename(title="Select Font File")
        if not filename:
            return

    output_dir = output_entry.get()
    if not output_dir:
        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", style="red.Horizontal.TProgressbar")
    progress_bar.grid(row=7, column=0, columnspan=3, pady=20)

    progress_bar["maximum"] = len(names)
    progress_bar["value"] = 0

    for name in names:
        generate_certificate(name, template_path, filename, output_dir)
        progress_bar["value"] += 1
        progress_bar.update()

    messagebox.showinfo("Success", "Certificates generated successfully! \n\n© Medhedimaaroufi 2024")

    # Open output directory
    if platform.system() == 'Windows':
        os.startfile(output_dir)
    elif platform.system() == 'Linux':
        os.system(f"xdg-open {output_dir}")
    elif platform.system() == 'Darwin':
        os.system(f"open {output_dir}")
    else:
        messagebox.showwarning("Unsupported Platform", "Cannot open output directory automatically on this platform.")

def main():
    global names_entry, template_entry, font_entry, font_file_entry, output_entry, test_fonts_var, progress_bar

    root = tk.Tk()
    root.title("Certificate Generator")
    root.configure(bg='#1E1E1E')  # Dark background color

    # Style for the progress bar
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("red.Horizontal.TProgressbar", background='#fc6044')

    # Labels and entry widgets for each input
    names_label = tk.Label(root, text="Names File:", bg='#1E1E1E', fg='white')
    names_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    names_entry = tk.Entry(root, width=40)
    names_entry.grid(row=1, column=1, padx=10, pady=5)
    names_entry.bind("<Control-o>", lambda event: names_entry.insert(tk.END, filedialog.askopenfilename(title="Select Names File")))
    names_button = tk.Button(root, text="Browse", command=lambda: names_entry.insert(tk.END, filedialog.askopenfilename(title="Select Names File")), bg='#333333', fg='white', relief='flat')
    names_button.grid(row=1, column=2, padx=10, pady=5)

    template_label = tk.Label(root, text="Certificate Template:", bg='#1E1E1E', fg='white')
    template_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    template_entry = tk.Entry(root, width=40)
    template_entry.grid(row=2, column=1, padx=10, pady=5)
    template_entry.bind("<Control-o>", lambda event: template_entry.insert(tk.END, filedialog.askopenfilename(title="Select Certificate Template")))
    template_button = tk.Button(root, text="Browse", command=lambda: template_entry.insert(tk.END, filedialog.askopenfilename(title="Select Certificate Template")), bg='#333333', fg='white', relief='flat')
    template_button.grid(row=2, column=2, padx=10, pady=5)

    font_file_label = tk.Label(root, text="Font File:", bg='#1E1E1E', fg='white')
    font_file_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    font_file_entry = tk.Entry(root, width=40)
    font_file_entry.grid(row=4, column=1, padx=10, pady=5)
    font_file_entry.bind("<Control-o>", lambda event: font_file_entry.insert(tk.END, filedialog.askopenfilename(title="Select Font File")))
    font_file_button = tk.Button(root, text="Browse", command=lambda: font_file_entry.insert(tk.END, filedialog.askopenfilename(title="Select Font File")), bg='#333333', fg='white', relief='flat')
    font_file_button.grid(row=4, column=2, padx=10, pady=5)

    output_label = tk.Label(root, text="Output Directory:", bg='#1E1E1E', fg='white')
    output_label.grid(row=5, column=0, padx=10, pady=5, sticky='w')
    output_entry = tk.Entry(root, width=40)
    output_entry.grid(row=5, column=1, padx=10, pady=5)
    output_entry.bind("<Control-o>", lambda event: output_entry.insert(tk.END, filedialog.askdirectory(title="Select Output Directory")))
    output_button = tk.Button(root, text="Browse", command=lambda: output_entry.insert(tk.END, filedialog.askdirectory(title="Select Output Directory")), bg='#333333', fg='white', relief='flat')
    output_button.grid(row=5, column=2, padx=10, pady=5)

    generate_button = tk.Button(root, text="Generate Certificates", command=lambda: generate_certificates(root), bg='#0060DF', fg='white', relief='flat')
    generate_button.grid(row=8, column=0, columnspan=3, pady=20)

    # Copyright label
    copyright_label = tk.Label(root, text="© Medhedimaaroufi 2024", bg='#1E1E1E', fg='white')
    copyright_label.grid(row=9, column=0, columnspan=3)

    # Configure column and row weights for responsiveness
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)
    for i in range(10):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
