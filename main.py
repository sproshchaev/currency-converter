import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from currency import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('currency_exchange_34dp_RGB(78, 68, 72)_FILL0_wght400_GRAD0_opsz40.png'))

        self.ui.input_currency.setPlaceholderText('Из валюты (например, EUR):')
        self.ui.input_amount.setPlaceholderText('У вас есть (сумма):')
        self.ui.output_currency.setPlaceholderText('В валюту (например, RUB):')
        self.ui.output_amount.setPlaceholderText('Вы получите:')

        # Подключение кнопки к методу конвертации
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        # Ваши фиксированные курсы валют
        exchange_rates = {
            'EUR': {'RUB': 103.3, 'USD': 1.04},
            'RUB': {'EUR': 0.009681, 'USD': 0.010078},
            'USD': {'EUR': 0.959, 'RUB': 99.23}
        }

        # Получение данных из полей ввода
        input_currency = self.ui.input_currency.text().strip().upper()
        output_currency = self.ui.output_currency.text().strip().upper()

        try:
            input_amount = float(self.ui.input_amount.text().strip())

            # Проверка наличия валют в словаре
            if input_currency in exchange_rates and output_currency in exchange_rates[input_currency]:
                rate = exchange_rates[input_currency][output_currency]
                output_amount = round(input_amount * rate, 2)
                self.ui.output_amount.setText(str(output_amount))
            else:
                self.ui.output_amount.setText("Ошибка: Валюта недоступна")

        except ValueError:
            self.ui.output_amount.setText("Ошибка: Некорректная сумма")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CurrencyConv()
    application.show()
    sys.exit(app.exec())