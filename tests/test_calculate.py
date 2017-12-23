import sys
from PyQt5.QtWidgets import QApplication, QLineEdit
from chemicalc import calculate

app = QApplication(sys.argv)

reagent_inputs = [{QLineEdit(text='NH4ClO4'): QLineEdit(text="6")},
                  {QLineEdit(text='Al'): QLineEdit(text="4")}
                  ]
product_inputs = [{QLineEdit(text='Al2O3'): QLineEdit(text="1")},
                    {QLineEdit(text='HCl'): QLineEdit(text="1")},
                    {QLineEdit(text='H2O'): QLineEdit(text="1")},
                    {QLineEdit(text='N2'): QLineEdit(text="1")},
                ]

calculate.calculate_yield(reagent_inputs, product_inputs)