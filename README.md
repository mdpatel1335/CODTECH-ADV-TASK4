# CODTECH-ADV-TASK4
# Advanced Encryption Tool - AES File Encryption/Decryption

# Personal information

* Name : Patel Mihir

* Company : CODTECH IT SOLUTIONS PVT.LTD

* ID : CT08DAB

* Domain : Cyber Security & Ethical Hacking

* Duration: 20th Dec 2024 To 20th Jan 2025

* Mentor : Neela Santhosh kumar

# Overview

The Advanced Encryption Tool is a graphical user interface (GUI)-based application that allows you to encrypt and decrypt files using AES-256 encryption. This tool supports both encryption and decryption of files and provides a simple, easy-to-use interface for secure file handling. The encryption key must be 32 bytes long for AES-256 encryption.

This tool is built using Python and Tkinter, and it utilizes the PyCryptodome library for performing AES encryption and decryption operations.


# Features:

- AES-256 Encryption: Provides secure file encryption using AES in CBC mode.
- File Encryption & Decryption: Encrypt any file and decrypt it using a specified key.
- Key Padding: If the key provided is shorter than 32 bytes, it automatically pads the key to 32 bytes.
- GUI Interface: User-friendly graphical interface built using Tkinter for easy interaction.
- Error Handling: Displays meaningful error messages for incorrect operations or missing files.
- Owner Information: Displays tool owner details in the application window.


# Requirements:

To run the Advanced Encryption Tool, the following dependencies are required:

- Python 3.x - Python must be installed on your machine. The tool has been tested with Python 3.x.
- PyCryptodome - A library used for cryptographic operations such as AES encryption/decryption.
- kinter - Used to create the graphical user interface.

# Install Required Libraries

You can install the required libraries using the following commands:

    pip install pycryptodome
    pip install tk

Make sure Python 3.x is installed on your system before running the tool.

# Installation Steps
- Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

    git clone https://github.com/mdpatel1335/CODTECH-ADV-TASK4.git
    cd CODTECH-ADV-TASK4

- Step 2: Install Dependencies

Install the required dependencies using pip. Run the following commands in your terminal or command prompt:

    pip install pycryptodome
    pip install tk

- Step 3: Run the Application

Run the Python application by executing the following command:

    python task4.py

- Step 4: Use the Tool

    - The tool will open a window where you can input the encryption key and browse for the file you want to encrypt or decrypt.
    - Enter a 32-byte encryption key (AES-256).
    - Browse for a file to encrypt or decrypt.
    - Click Encrypt File to encrypt the selected file or Decrypt File to decrypt the selected file.
    - The encrypted file will be saved with a .enc extension, and the decrypted file will be saved with a .dec extension.
 

# Usage Instructions

- Key: The encryption key you enter must be 32 bytes long. If the key is shorter, the tool will automatically pad it to 32 bytes.

- File Selection: You can use the browse button to select a file you wish to encrypt or decrypt. After selecting the file, you will need to click the appropriate button (Encrypt File or Decrypt File) to perform the operation.

- Encrypted File: After encrypting a file, the tool will save the encrypted file with an .enc extension. Similarly, after decryption, it will save the decrypted file with a .dec extension.

# Example Workflow:

- open the application.
- Enter your key (32 characters for AES-256 encryption).
- Browse and select a file to encrypt.
- Click Encrypt File.
- The encrypted file will be saved with the .enc extension in the same directory as the original file.
- To decrypt, load the .enc file, enter the key, and click Decrypt File.

# File Format Details

The encrypted file will contain two parts:
- Initialization Vector (IV): This is the random value used to initialize the encryption.
- Encrypted Data: The actual encrypted content of the file.

# Acknowledgments

This tool uses the following libraries:

- PyCryptodome: A Python library for cryptographic operations, including AES encryption.
- Tkinter: A built-in Python library for creating desktop applications with graphical user interfaces.


# Practical Screenshots:

![Screenshot From 2025-01-16 15-11-45](https://github.com/user-attachments/assets/4e8dc86b-885b-433c-85ab-ab30a3c561a0)

![Screenshot From 2025-01-16 15-12-17](https://github.com/user-attachments/assets/cddbdc1a-2d10-4f5e-8c70-21b701375c9b)

![Screenshot From 2025-01-16 15-14-39](https://github.com/user-attachments/assets/a5d58113-e3b8-4fdb-a767-6d8479909e8c)

![Screenshot From 2025-01-16 15-14-57](https://github.com/user-attachments/assets/734a1de3-8a6c-491b-bd0b-f9a766b73852)

![Screenshot From 2025-01-16 15-15-31](https://github.com/user-attachments/assets/36d14257-e2a6-448b-92d1-7faac2f42a0c)

![Screenshot From 2025-01-16 15-15-40](https://github.com/user-attachments/assets/2bf8a93e-4407-4ee0-b7e0-a688a1dc568d)

![Screenshot From 2025-01-16 15-15-56](https://github.com/user-attachments/assets/7375f543-578c-49b3-82f6-15c6620c5eab)

![Screenshot From 2025-01-16 15-16-32](https://github.com/user-attachments/assets/6209ae19-7b56-4e8e-8eae-d20492aae021)

![Screenshot From 2025-01-16 15-16-42](https://github.com/user-attachments/assets/bca02a52-3956-46ff-baa5-e52d32267b39)

![Screenshot From 2025-01-16 15-16-51](https://github.com/user-attachments/assets/8aefc1d0-ae53-4319-975c-189eed1dff79)
