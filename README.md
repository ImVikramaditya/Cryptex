This repository is a college project written in 2020 to demostrate encryption/decryption algorithm AES-Advance Encryption Standard. 

The source code is completely in python.

The file ProjectSc.py serves as the entry point for running the project through terminal.

To launch a GUI, run cryptext.py file. Tkinter(Okay, I know no one uses it anymore but I had to use it in 2020.) and pySQL are the required dependencies for GUI. 


PySQL would also require additional database configurations.
A local SQL database is used to store filename and hashkey that are used for encryption. When there is a mismatch with the key during decryption, the file cannot be decyphered.
