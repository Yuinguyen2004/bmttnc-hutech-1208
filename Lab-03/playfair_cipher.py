import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.UI.btn_create_matrix.clicked.connect(self.call_api_create_matrix)
        self.UI.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.UI.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_create_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
        "key": self.UI.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Flatten the nested lists into strings
                matrix_string = "\n".join([" ".join(row) for row in data["playfair_matrix"]])
                self.UI.txt_matrix.setPlainText(matrix_string)
                
                msg = QMessageBox()
                msg.setText("Matrix Created Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.UI.txt_plain_text.toPlainText(),
            "key": self.UI.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.UI.txt_cipher_text.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()                
                msg.setText("Message Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
        
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.UI.txt_cipher_text.toPlainText(),
            "key": self.UI.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.UI.txt_plain_text.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setText("Message Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())