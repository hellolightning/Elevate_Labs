# 🛡️ STEGANOGRAPHY TOOL FOR IMAGE/FILE HIDING

## INTRODUCTION
This Python-based tool allows users to hide and extract text messages within images using steganography.  
It employs the Least Significant Bit (LSB) technique to embed data without altering the image’s appearance.  
The GUI is built with Tkinter and supports PNG, BMP, and JPEG formats.

---

## FEATURES
- Hide text messages in images.  
- Extract hidden text from images.  
- Supports multiple image formats (PNG, BMP, JPEG).  
- Easy-to-use graphical interface with drag-and-drop functionality.

## PROJECT PHASE
- Phase 1: GUI Design and Architecture
- Phase 2: Image Processing Implementation
- Phase 3: Steganography Algorithm Development
- Phase 4: User Interface Enhancement
- Phase 5: Testing and Validation

## STEPS INVOLVED IN BUILDING THE PROJECT

- **Step 1: Environment Setup and Library Installation -**
The project began with setting up the Python development environment and installing necessary libraries.
The PIL library was installed for image processing capabilities, while Tkinter provided the foundation for the graphical user interface.
- **Step 2: GUI Design and Layout Creation -**
A modern, dark-themed interface was designed with three main sections: image upload panel on the left, text hiding section on the right-top, and message extraction section on the right-bottom.
Custom styling was applied to create an attractive and professional appearance.
- **Step 3: Image Upload and Display Functionality -**
The image upload feature was implemented using file dialog boxes to allow users to select images from their system.
Image preview functionality was added to display thumbnails of selected images within the application interface.
- **Step 4: Text-to-Binary Conversion System -**
A robust text-to-binary conversion system was developed to transform user messages into binary format.
This includes proper handling of character encoding and the addition of end delimiters to mark message boundaries.
- **Step 5: LSB Steganography Implementation -**
The core steganography algorithm was implemented using the Least Significant Bit technique.
 This involves modifying the last bit of each color channel (RGB) in image pixels to embed the binary message data while maintaining visual integrity.
- **Step 6: Message Hiding Functionality -**
The hide message feature was developed to take user input text, convert it to binary, and embed it within the selected image using LSB modification.
 The system includes error handling for oversized messages and file saving capabilities.
- **Step 7: Message Extraction Algorithm -**
The extraction functionality was implemented to reverse the hiding process by reading LSB values from image pixels, reconstructing the binary message, and converting it back to readable text format.
- **Step 8: Testing and Error Handling -**
Comprehensive testing was conducted to ensure reliability across different image formats and message sizes.
 Error handling mechanisms were implemented to manage file operations, image processing errors, and user input validation

## RESULTS

### Stegnography Tool Tab

![Stegno Tool Tab](https://github.com/user-attachments/assets/2b7ccd17-1b4c-4307-a59a-511b282351c4)

---

| Image/File selected to Encrypt | Result |
| --- | --- | 
| ![Encrypt S](https://github.com/user-attachments/assets/959911d3-2183-434b-bf57-900c636f467a)   | ![Encrypt R](https://github.com/user-attachments/assets/ce160d01-d217-461f-bab9-db303dff0ba7)  | 

--- 

| Image/File selected to Decrypt | Result |
| --- | --- | 
| ![Decrypt S](https://github.com/user-attachments/assets/cfa1c0e6-2b84-461a-a187-b15be871d717) | ![Decrypt R](https://github.com/user-attachments/assets/ac7b80ac-6cc6-48ee-98fe-e32e6b088871) | 


## KEY ACHIEVEMENTS

**1. Successful Implementation:** Developed a fully functional steganography tool with both hiding and extraction capabilities using the LSB technique.

**2. User-Friendly Interface:** Created an intuitive GUI with modern styling, drag-and-drop functionality, and clear visual feedback for all operations.

**3. Multi-Format Support:** Implemented support for various image formats including PNG, BMP, and JPEG with automatic format handling.

**4. Robust Error Handling:** Integrated comprehensive error handling for file operations, image processing, and user input validation ensuring stable operation.


## FUTURE ENHANCEMENTS

**1. Advanced Encryption Integration:** Implement AES or RSA encryption for the hidden messages to add an additional layer of security beyond simple hiding.

**2. Multiple File Format Support:** Extend the tool to hide various file types (documents, images, audio) within cover images, not just text messages.

**3. Steganographic Analysis Features:** Add detection capabilities to analyze images for potential hidden content and measure steganographic capacity of different images.

--- 

### Security Note:
This tool is developed strictly for educational and learning purposes to demonstrate steganography concepts. It should not be used for malicious or unauthorized data hiding.
