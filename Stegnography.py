import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

class SteganographyTool:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Steganography Tool")
        self.root.geometry("900x650")
        self.root.configure(bg='#1a1a2e')
        
        # Variables
        self.image_path = ""
        self.original_image = None
        
        self.setup_gui()
    
    def setup_gui(self):
        # Main title
        title_frame = tk.Frame(self.root, bg='#1a1a2e')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="🔒 Steganography Tool", 
                              font=("Arial", 24, "bold"), 
                              fg='#00d4ff', bg='#1a1a2e')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Hide & Extract Secret Messages in Images", 
                                 font=("Arial", 12), 
                                 fg='#a0a0a0', bg='#1a1a2e')
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Left Panel - Image Upload
        left_frame = tk.Frame(main_frame, bg='#16213e', relief='ridge', bd=0)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))
        left_frame.configure(highlightbackground='#00d4ff', highlightthickness=2)
        
        # Image section header
        img_header = tk.Label(left_frame, text="📁 Select Image", 
                             font=("Arial", 16, "bold"), 
                             fg='#00d4ff', bg='#16213e')
        img_header.pack(pady=15)
        
        # Image preview frame
        self.image_frame = tk.Frame(left_frame, bg='#0f1419', width=300, height=200)
        self.image_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.image_frame.pack_propagate(False)
        
        # Default image placeholder
        self.image_label = tk.Label(self.image_frame, text="No Image Selected\n📷", 
                                   font=("Arial", 14), 
                                   fg='#666', bg='#0f1419')
        self.image_label.pack(expand=True)
        
        # Upload button
        upload_btn = tk.Button(left_frame, text="🔍 Browse Image", 
                              command=self.upload_image,
                              font=("Arial", 12, "bold"),
                              bg='#00d4ff', fg='white',
                              relief='flat', bd=0,
                              padx=30, pady=10)
        upload_btn.pack(pady=20)
        
        # Right Panel - Hide/Extract
        right_frame = tk.Frame(main_frame, bg='#16213e', relief='ridge', bd=0)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(15, 0))
        right_frame.configure(highlightbackground='#00d4ff', highlightthickness=2)
        
        # Hide Text Section
        hide_frame = tk.Frame(right_frame, bg='#16213e')
        hide_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        hide_header = tk.Label(hide_frame, text="🔒 Hide Secret Text", 
                              font=("Arial", 16, "bold"), 
                              fg='#00ff88', bg='#16213e')
        hide_header.pack(pady=10)
        
        tk.Label(hide_frame, text="Enter message to hide:", 
                font=("Arial", 10), fg='#ccc', bg='#16213e').pack(anchor='w', padx=20)
        
        self.hide_text = tk.Text(hide_frame, height=6, width=40,
                                font=("Arial", 10),
                                bg='#0f1419', fg='white',
                                insertbackground='white',
                                relief='flat', bd=5)
        self.hide_text.pack(pady=5, padx=20, fill=tk.X)
        
        hide_btn = tk.Button(hide_frame, text="🔐 Hide Text in Image", 
                            command=self.hide_message,
                            font=("Arial", 11, "bold"),
                            bg='#00ff88', fg='#1a1a2e',
                            relief='flat', bd=0,
                            padx=20, pady=8)
        hide_btn.pack(pady=15)
        
        # Separator
        separator = tk.Frame(right_frame, height=2, bg='#00d4ff')
        separator.pack(fill=tk.X, padx=20, pady=10)
        
        # Extract Text Section
        extract_frame = tk.Frame(right_frame, bg='#16213e')
        extract_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        extract_header = tk.Label(extract_frame, text="🔓 Extract Hidden Text", 
                                 font=("Arial", 16, "bold"), 
                                 fg='#ff6b6b', bg='#16213e')
        extract_header.pack(pady=10)
        
        tk.Label(extract_frame, text="Hidden message will appear here:", 
                font=("Arial", 10), fg='#ccc', bg='#16213e').pack(anchor='w', padx=20)
        
        self.extract_text = tk.Text(extract_frame, height=6, width=40,
                                   font=("Arial", 10),
                                   bg='#0f1419', fg='white',
                                   insertbackground='white',
                                   relief='flat', bd=5,
                                   state='disabled')
        self.extract_text.pack(pady=5, padx=20, fill=tk.X)
        
        extract_btn = tk.Button(extract_frame, text="🔍 Extract Hidden Text", 
                               command=self.extract_message,
                               font=("Arial", 11, "bold"),
                               bg='#ff6b6b', fg='white',
                               relief='flat', bd=0,
                               padx=20, pady=8)
        extract_btn.pack(pady=15)
    
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        
        if file_path:
            self.image_path = file_path
            self.display_image(file_path)
    
    def display_image(self, path):
        try:
            # Load and resize image for preview
            image = Image.open(path)
            self.original_image = image.copy()
            
            # Resize for preview
            image.thumbnail((280, 180), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            
            # Update image label
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {str(e)}")
    
    def text_to_binary(self, text):
        """Convert text to binary"""
        return ''.join(format(ord(char), '08b') for char in text)
    
    def binary_to_text(self, binary):
        """Convert binary to text"""
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                text += chr(int(byte, 2))
        return text
    
    def hide_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        message = self.hide_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showerror("Error", "Please enter a message to hide!")
            return
        
        try:
            # Add delimiter to mark end of message
            message += "<<<END>>>"
            binary_message = self.text_to_binary(message)
            
            # Load image
            img = Image.open(self.image_path)
            img = img.convert('RGB')
            pixels = list(img.getdata())
            
            # Check if image is large enough
            if len(binary_message) > len(pixels) * 3:
                messagebox.showerror("Error", "Message too long for this image!")
                return
            
            # Hide message in LSB
            pixel_index = 0
            bit_index = 0
            
            for i, pixel in enumerate(pixels):
                r, g, b = pixel
                
                if bit_index < len(binary_message):
                    # Modify red channel LSB
                    r = (r & 0xFE) | int(binary_message[bit_index])
                    bit_index += 1
                
                if bit_index < len(binary_message):
                    # Modify green channel LSB
                    g = (g & 0xFE) | int(binary_message[bit_index])
                    bit_index += 1
                
                if bit_index < len(binary_message):
                    # Modify blue channel LSB
                    b = (b & 0xFE) | int(binary_message[bit_index])
                    bit_index += 1
                
                pixels[i] = (r, g, b)
                
                if bit_index >= len(binary_message):
                    break
            
            # Create new image with hidden message
            stego_img = Image.new('RGB', img.size)
            stego_img.putdata(pixels)
            
            # Save the image
            save_path = filedialog.asksaveasfilename(
                title="Save Steganographic Image",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("BMP files", "*.bmp")]
            )
            
            if save_path:
                stego_img.save(save_path)
                messagebox.showinfo("Success", f"Message hidden successfully!\nSaved as: {os.path.basename(save_path)}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to hide message: {str(e)}")
    
    def extract_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        try:
            # Load image
            img = Image.open(self.image_path)
            img = img.convert('RGB')
            pixels = list(img.getdata())
            
            # Extract binary data from LSB
            binary_message = ""
            
            for pixel in pixels:
                r, g, b = pixel
                
                # Extract LSB from each channel
                binary_message += str(r & 1)
                binary_message += str(g & 1)
                binary_message += str(b & 1)
            
            # Convert binary to text
            message = ""
            for i in range(0, len(binary_message), 8):
                byte = binary_message[i:i+8]
                if len(byte) == 8:
                    char = chr(int(byte, 2))
                    message += char
                    
                    # Check for end delimiter
                    if message.endswith("<<<END>>>"):
                        message = message[:-9]  # Remove delimiter
                        break
            
            # Display extracted message
            self.extract_text.config(state='normal')
            self.extract_text.delete("1.0", tk.END)
            self.extract_text.insert("1.0", message)
            self.extract_text.config(state='disabled')
            
            if message.strip():
                messagebox.showinfo("Success", "Hidden message extracted successfully!")
            else:
                messagebox.showwarning("No Message", "No hidden message found in this image.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract message: {str(e)}")

def main():
    root = tk.Tk()
    app = SteganographyTool(root)
    
    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()