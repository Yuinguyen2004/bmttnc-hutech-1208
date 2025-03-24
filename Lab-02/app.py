from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    caesar_cipher = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    caesar_cipher = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route('/playfair/creatematrix', methods=['POST'])
def playfair_create_matrix():
    key = request.form['inputKey']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    formatted_matrix = "<br/>".join([" ".join(row) for row in matrix])
    return f"Matrix:<br/>{formatted_matrix}"

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)