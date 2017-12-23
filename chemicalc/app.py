import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLabel, QGroupBox,
                             QLineEdit, QFormLayout, QComboBox,
                             QSpinBox, QVBoxLayout, QGridLayout,
                             QGroupBox)

from calculate import calculate_yield

class main_widget(QWidget):
    def __init__(self):
        # generate window
        super().__init__()
        # populate window
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 240)
        self.setWindowTitle('ChemiCalc')
        # containers for reactant counting and reactant data
        self.reagent_count, self.product_count = 0, 0
        self.reagent_list, self.product_list = {}, {}
        # button to add a reagent
        reagentAdder = QPushButton("Add Reagent")
        reagentAdder.clicked.connect(self.addReagent)
        # the reagent input list
        self.reagentGrid = QGridLayout()
        self.reagentGrid.addWidget(reagentAdder, 0, 0)
        # button to add product
        productAdder = QPushButton("Add Product")
        productAdder.clicked.connect(self.addProduct)
        # the product input list
        self.productGrid = QGridLayout()
        self.productGrid.addWidget(productAdder, 0, 0)
        # submit button
        yieldButton = QPushButton("Calculate Yield")
        yieldButton.clicked.connect(self.get_yield)
        # yield section grid
        self.outputGrid = QGridLayout()
        self.outputGrid.addWidget(yieldButton, 0, 0)
        # stitch together all grids
        masterGrid = QGridLayout()
        masterGrid.addLayout(self.reagentGrid, 0, 0)
        masterGrid.addLayout(self.productGrid, 0, 1)
        masterGrid.addLayout(self.outputGrid,  0, 2)
        self.setLayout(masterGrid)

        self.show()

    def addReagent(self):
        # increment reagent count and add a form to reagents
        self.reagent_count += 1
        self.reagentGrid.addWidget(self.inputForm("Reagent", self.reagent_count))

    def addProduct(self):
        # increment product count and add a form to products
        self.product_count += 1
        self.productGrid.addWidget(self.inputForm("Product", self.product_count))

    def get_yield(self):
        # submit inputs and output yield
        calculate_yield(self.reagent_list,
                        self.product_list)

    def inputForm(self, type=str, index=int):
        # a section with indexed label
        label = "{0} {1}:".format(type, index)
        # grouped form
        reagentGroup = QGroupBox(label)
        # two text entries, formula and amount (grams, etc)
        formula = QLineEdit()
        amount = QLineEdit()
        # stitch form
        vbox = QFormLayout()
        vbox.addRow(QLabel("Formula:"), formula)
        vbox.addRow(QLabel("Amount:"), amount)
        reagentGroup.setLayout(vbox)
        # the current input
        group_info = {formula: amount}
        # save entry widgets to corresponding list to get data later
        if type.lower() == 'reagent':
            self.reagent_list.append(group_info)
        else:
            self.product_list.append(group_info)
        # return form to window
        return(reagentGroup)

def main_app():
    app = QApplication(sys.argv)
    ex = main_widget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_app()

