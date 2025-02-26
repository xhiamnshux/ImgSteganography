Project Title: Secure Data Hiding in Image Using Steganography
Description:
This project implements image steganography using the Least Significant Bit (LSB) technique in Python. It allows users to hide a secret message inside an image and later extract it without altering the image quality noticeably. For enhanced security, messages can also be encrypted using AES encryption before embedding.

Features:
- Hide text inside an image (Encoding)
- Extract hidden text from an image (Decoding)
- Supports PNG and JPEG image formats
- Uses Least Significant Bit (LSB) technique
- AES encryption for secure message encoding (optional)
- Simple GUI using Tkinter for user interaction
- Works on Windows, macOS, and Linux

Requirements:
Ensure you have Python 3.8+ installed. Install dependencies using:

sh
Copy
Edit
pip install pillow numpy opencv-python pycryptodome matplotlib

How to Use

1️) Hide a Message in an Image (Encoding)
Run the following command:

sh
Copy
Edit
python steganography.py
Select an image (JPG/PNG)
Enter the secret message
The program will generate an encoded image (encoded_image.png)


2️) Extract a Message from an Image (Decoding)
sh
Copy
Edit
python steganography.py
Select the encoded image
The program will extract and display the hidden message

Encryption (Optional)
For additional security, you can encrypt messages before embedding them.

Modify steganography.py to use encryption.py
Use AES encryption & decryption before encoding
To encrypt:

python
Copy
Edit
from encryption import encrypt_message
encrypted_text = encrypt_message("Your Secret Message")
To decrypt:

python
Copy
Edit
from encryption import decrypt_message
decrypted_text = decrypt_message(encrypted_text)

Graphical User Interface (GUI):
To use the GUI version, run:

sh
Copy
Edit
python gui.py
Click "Encode Message" → Select an image → Enter a message → Saves as encoded_image.png
Click "Decode Message" → Select an encoded image → Displays the hidden message

## 🔧 Technologies Used
- **Python 3.8+** - Core programming language
- **Pillow (PIL)** - Image processing
- **NumPy** - Pixel manipulation
- **PyCryptodome** - AES encryption
- **Tkinter** - GUI for user interaction (Optional)
- **Matplotlib** - Image visualization (Optional)

To install dependencies:
```sh

pip install pillow numpy opencv-python pycryptodome matplotlib


📂 Project Structure
graphql
Copy
Edit
SteganographyProject/
│── steganography.py  # Main script for encoding & decoding
│── encryption.py     # AES encryption for security (optional)
│── gui.py            # GUI implementation using Tkinter
│── test_image.png    # Sample image for testing
│── README.md         # Project documentation


🛠 How to Run the Project

1️⃣ Hide a Message in an Image (Encoding)
sh
Copy
Edit
python steganography.py
Select an image (PNG/JPG)
Enter the secret message
The program generates an encoded image (encoded_image.png)


2️⃣ Extract a Message from an Image (Decoding)
sh
Copy
Edit
python steganography.py
Select the encoded image
The program will extract and display the hidden message


🔐 AES Encryption (Optional)
To encrypt:
python
Copy
Edit
from encryption import encrypt_message
encrypted_text = encrypt_message("Your Secret Message")
To decrypt:

python
Copy
Edit
from encryption import decrypt_message
decrypted_text = decrypt_message(encrypted_text)


🎨 GUI Usage (Optional)
Run the GUI:
sh
Copy
Edit
python gui.py
"Encode Message" → Select an image → Enter a message → Saves as encoded_image.png
"Decode Message" → Select an encoded image → Displays the hidden message


🎯 Unique Features
✅ AES Encryption for extra security
✅ Minimal image distortion using Least Significant Bit (LSB)
✅ Graphical User Interface (GUI) for easy interaction
✅ Error detection mechanism to verify the hidden message
✅ Optimized for fast encoding & decoding

👥 End Users
🔹 Cybersecurity Professionals - Secure data transmission
🔹 Journalists & Whistleblowers - Covert communication
🔹 Intelligence & Military - Secure classified information
🔹 General Privacy Users - Personal secure messaging
🔹 Businesses - Digital watermarking and data security
🔹 Healthcare - Protecting patient data in medical images

📜 Limitations
Image Size - Large messages may slightly affect image quality
JPEG Compression - May cause loss of hidden data, prefer PNG
Encryption Key - Must be remembered for decryption

🔗 References
Least Significant Bit (LSB) Steganography
Pillow Library
PyCryptodome AES Encryption

📌 Author
👨‍💻 Your Name – Himanshu Kardam
📧 Contact: m9818366@gmail.com
