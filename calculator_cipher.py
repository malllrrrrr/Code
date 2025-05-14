import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class CaesarCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Калькулятор Цезаря')
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel('Введите текст:')
        self.layout.addWidget(self.label)
        
        self.input_text = QLineEdit(self)
        self.layout.addWidget(self.input_text)
        
        self.label_key = QLabel('Введите ключ (число):')
        self.layout.addWidget(self.label_key)
        
        self.input_key = QLineEdit(self)
        self.layout.addWidget(self.input_key)
        
        self.encrypt_btn = QPushButton('Зашифровать', self)
        self.encrypt_btn.clicked.connect(self.encrypt_text)
        self.layout.addWidget(self.encrypt_btn)
        
        self.decrypt_btn = QPushButton('Расшифровать', self)
        self.decrypt_btn.clicked.connect(self.decrypt_text)
        self.layout.addWidget(self.decrypt_btn)
        
        self.result = QLabel('Результат:', self)
        self.layout.addWidget(self.result)
        
        self.setLayout(self.layout)
    
    def caesar_cipher(self, text, shift, decrypt=False):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        small_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        shift = -shift if decrypt else shift  # Если расшифровка, делаем сдвиг в обратную сторону

        result = ''
        for char in text:
            if char in alphabet:
                new_index = (alphabet.index(char) + shift) % len(alphabet)
                result += alphabet[new_index]
            elif char in small_alphabet:
                new_index = (small_alphabet.index(char) + shift) % len(small_alphabet)
                result += small_alphabet[new_index]
            else:
                result += char  # Пропускаем символы, которых нет в алфавите
        return result
    
    def encrypt_text(self):
        text = self.input_text.text()
        try:
            shift = int(self.input_key.text())
            self.result.setText(f'Результат: {self.caesar_cipher(text, shift)}')
        except ValueError:
            self.result.setText('Ошибка: ключ должен быть числом')
    
    def decrypt_text(self):
        text = self.input_text.text()
        try:
            shift = int(self.input_key.text())
            self.result.setText(f'Результат: {self.caesar_cipher(text, shift, decrypt=True)}')
        except ValueError:
            self.result.setText('Ошибка: ключ должен быть числом')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    caesar = CaesarCipher()
    caesar.show()
    sys.exit(app.exec_())
