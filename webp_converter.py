import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image
from tqdm import tqdm

class WebPConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk WebP Converter")
        self.root.geometry("600x450")
        self.root.resizable(True, True)
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title and About button frame
        title_frame = ttk.Frame(self.main_frame)
        title_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        title_label = ttk.Label(title_frame, text="Bulk WebP Converter", font=('Helvetica', 12, 'bold'))
        title_label.pack(side=tk.LEFT)
        
        about_btn = ttk.Button(title_frame, text="About", command=self.show_about, width=10)
        about_btn.pack(side=tk.RIGHT)
        
        # Source folder selection
        ttk.Label(self.main_frame, text="Source Folder:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.source_path = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.source_path, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(self.main_frame, text="Browse", command=self.select_source).grid(row=1, column=2)
        
        # Destination folder selection
        ttk.Label(self.main_frame, text="Output Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.dest_path = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.dest_path, width=50).grid(row=2, column=1, padx=5)
        ttk.Button(self.main_frame, text="Browse", command=self.select_destination).grid(row=2, column=2)
        
        # Prefix input and checkbox
        prefix_frame = ttk.Frame(self.main_frame)
        prefix_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(prefix_frame, text="Image Prefix:").pack(side=tk.LEFT, padx=(0, 5))
        self.prefix = tk.StringVar()
        ttk.Entry(prefix_frame, textvariable=self.prefix, width=30).pack(side=tk.LEFT, padx=5)
        
        self.use_prefix = tk.BooleanVar(value=False)
        ttk.Checkbutton(prefix_frame, text="Apply prefix to all images", variable=self.use_prefix).pack(side=tk.LEFT, padx=5)
        
        # Quality slider
        ttk.Label(self.main_frame, text="Quality (1-100):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.quality = tk.IntVar(value=80)
        quality_slider = ttk.Scale(self.main_frame, from_=1, to=100, variable=self.quality, orient=tk.HORIZONTAL)
        quality_slider.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Label(self.main_frame, textvariable=self.quality).grid(row=4, column=2)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var)
        self.status_label.grid(row=6, column=0, columnspan=3, pady=5)
        
        # Convert button
        self.convert_btn = ttk.Button(self.main_frame, text="Convert to WebP", command=self.convert_images)
        self.convert_btn.grid(row=7, column=0, columnspan=3, pady=10)

    def show_about(self):
        about_text = """Bulk WebP Converter v1.0

Author: SonicWP
Email: sonicWP@gmail.com
GitHub: github.com/lamtc

A simple tool to convert images to WebP format
while maintaining quality and reducing file size.

 2024 All rights reserved."""
        
        messagebox.showinfo("About", about_text)
        
    def select_source(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_path.set(folder)
            
    def select_destination(self):
        folder = filedialog.askdirectory()
        if folder:
            self.dest_path.set(folder)
            
    def convert_images(self):
        source = self.source_path.get()
        destination = self.dest_path.get()
        quality = self.quality.get()
        prefix = self.prefix.get() if self.use_prefix.get() else ""
        
        if not source or not destination:
            self.status_var.set("Please select both source and destination folders")
            return
            
        supported_formats = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
        images = [f for f in os.listdir(source) if f.endswith(supported_formats)]
        
        if not images:
            self.status_var.set("No supported images found in source folder")
            return
            
        self.convert_btn.state(['disabled'])
        self.status_var.set("Converting images...")
        
        for i, img_name in enumerate(images):
            try:
                input_path = os.path.join(source, img_name)
                
                # Generate output filename with optional prefix
                if prefix:
                    output_name = f"{prefix}_{i+1}.webp"
                else:
                    output_name = os.path.splitext(img_name)[0] + '.webp'
                    
                output_path = os.path.join(destination, output_name)
                
                with Image.open(input_path) as img:
                    img.save(output_path, 'WEBP', quality=quality, method=6)
                
                progress = (i + 1) / len(images) * 100
                self.progress_var.set(progress)
                self.root.update()
                
            except Exception as e:
                self.status_var.set(f"Error converting {img_name}: {str(e)}")
                self.convert_btn.state(['!disabled'])
                return
        
        self.status_var.set("Conversion completed successfully!")
        self.convert_btn.state(['!disabled'])
        self.progress_var.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPConverter(root)
    root.mainloop()
