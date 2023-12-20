import os
import tkinter as tk
from tkinter import filedialog
from heic2png import HEIC2PNG

def convert_heic_to_png(input_path, output_path, quality=100, overwrite=False):
    os.makedirs(output_path, exist_ok=True)

    for filename in os.listdir(input_path):
        if filename.lower().endswith('.heic'):
            heic_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + '.png')

            if not overwrite and os.path.exists(output_file):
                print(f"Skipping {filename} - PNG file already exists.")
                continue

            heic_img = HEIC2PNG(heic_file, quality=quality)
            heic_img.save(output_file)
            print(f"Converted {filename} to {output_file} with quality set to {quality}")

def open_folder():
    try:
        global input_directory
        input_directory = filedialog.askdirectory()
        entry_folder_path.delete(0, tk.END)
        entry_folder_path.insert(0, input_directory)
    except Exception as e:
        print(f"Error en open_folder: {e}")

def save_folder():
    try:
        global output_directory
        output_directory = filedialog.askdirectory()
        entry_save_path.delete(0, tk.END)
        entry_save_path.insert(0, output_directory)
    except Exception as e:
        print(f"Error en save_folder: {e}")

def update_quality_label(value):
    quality_label.config(text=f"Calidad: {value}")

def start_conversion():
    try:
        quality = quality_var.get()
        convert_heic_to_png(input_directory, output_directory, quality=quality, overwrite=False)
        status_label.config(text="Conversión completa. Archivos guardados en la carpeta especificada.")
    except Exception as e:
        print(f"Error en start_conversion: {e}")

root = tk.Tk()
root.title("HEIC2JPG FREE - por @soypato")

input_directory = ""
output_directory = ""

label_folder = tk.Label(root, text="Carpeta de entrada:")
label_folder.grid(row=0, column=0, pady=5)

entry_folder_path = tk.Entry(root, width=40)
entry_folder_path.grid(row=0, column=1, padx=5, pady=5)

button_open = tk.Button(root, text="Abrir carpeta", command=open_folder)
button_open.grid(row=0, column=2, pady=5)

label_save = tk.Label(root, text="Carpeta de salida:")
label_save.grid(row=1, column=0, pady=5)

entry_save_path = tk.Entry(root, width=40)
entry_save_path.grid(row=1, column=1, padx=5, pady=5)

button_save = tk.Button(root, text="Seleccionar salida", command=save_folder)
button_save.grid(row=1, column=2, pady=5)

label_quality = tk.Label(root, text="De 0 a 100, entre más la cantidad, más la calidad")
label_quality.grid(row=2, column=1, pady=5)

quality_var = tk.IntVar()
quality_var.set(100)

quality_label = tk.Label(root, text="Calidad:")
quality_label.grid(row=3, column=0, pady=5)

quality_scale = tk.Scale(root, from_=1, to=100, orient="horizontal", variable=quality_var, command=lambda value: update_quality_label(value))
quality_scale.set(100)  # Valor predeterminado
quality_scale.grid(row=3, column=1, pady=5)

button_convert = tk.Button(root, text="Iniciar Conversión", command=start_conversion)
button_convert.grid(row=4, column=1, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=5, column=1)

root.mainloop()
