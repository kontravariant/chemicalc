import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLabel, QGroupBox,
                             QLineEdit, QFormLayout, QComboBox,
                             QSpinBox, QVBoxLayout, QGridLayout,
                             QGroupBox)

class main_widget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 240)
        self.setWindowTitle('ChemiCalc')

        self.reagent_count, self.product_count = 0, 0
        self.reagent_list, self.product_list = [], []

        reagentAdder = QPushButton("Add Reagent")
        reagentAdder.clicked.connect(self.addReagent)

        self.reagentGrid = QGridLayout()
        self.reagentGrid.addWidget(reagentAdder, 0, 0)

        productAdder = QPushButton("Add Product")
        productAdder.clicked.connect(self.addProduct)

        self.productGrid = QGridLayout()
        self.productGrid.addWidget(productAdder, 0, 0)

        yieldButton = QPushButton("Calculate Yield")
        yieldButton.clicked.connect(self.yield_calculator)

        self.outputGrid = QGridLayout()
        self.outputGrid.addWidget(yieldButton, 0, 0)

        masterGrid = QGridLayout()
        masterGrid.addLayout(self.reagentGrid, 0, 0)
        masterGrid.addLayout(self.productGrid, 0, 1)
        masterGrid.addLayout(self.outputGrid,  0, 2)

        self.setLayout(masterGrid)

        self.show()

    def addReagent(self):
        self.reagent_count += 1
        self.reagentGrid.addWidget(self.inputForm("Reagent", self.reagent_count))

    def addProduct(self):
        self.product_count += 1
        self.productGrid.addWidget(self.inputForm("Product", self.product_count))

    def yield_calculator(self):
        pass

    def inputForm(self, type=str, index=int):
        label = "{0} {1}:".format(type, index)
        reagentGroup = QGroupBox(label)
        formula = QLineEdit()
        weight = QLineEdit()
        amount = QLineEdit()

        vbox = QFormLayout()
        vbox.addRow(QLabel("Formula:"), formula)
        vbox.addRow(QLabel("Molar Weight:"), weight)
        vbox.addRow(QLabel("Amount:"), amount)
        reagentGroup.setLayout(vbox)

        group_info = {label: (formula, weight, amount)}

        if type.lower() == 'reagent':
            self.reagent_list.append(group_info)
        else:
            self.product_list.append(group_info)

        return(reagentGroup)


def main_app():
    app = QApplication(sys.argv)
    ex = main_widget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_app()

