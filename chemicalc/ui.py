from tkinter import *

def build_window(self):
    self.in_label = Label(frame, text="Enter limiting reagent formula or molar mass:", wraplength=1000)
    self.in_label.grid(row=0, columnspan=2)

    self.formula_var = StringVar()
    self.formula_label = Label(frame, text="Reagent formula:")
    self.formula_label.grid(row=1, column=0)
    self.cpd1 = Entry(frame, textvariable=self.formula_var)
    self.cpd1.grid(row=1, column=1)

    self.molar_var = DoubleVar()
    self.mol_label = Label(frame, text="Regent molar mass:")
    self.mol_label.grid(row=2, column=0)
    self.mol1 = Entry(frame, textvariable=self.molar_var)
    self.mol1.grid(row=2, column=1)

    self.rgt_mass_label = Label(frame, text="Reagent mass:")
    self.rgt_mass_label.grid(row=3, column=0)
    self.reagent_mass_var = DoubleVar()
    self.rgt_mass = Entry(frame, textvariable=self.reagent_mass_var)
    self.rgt_mass.grid(row=3, column=1)

    self.in_label = Label(frame, text="Enter product formula or molar mass:", wraplength=1000)
    self.in_label.grid(row=4, columnspan=2)

    self.prd_formula_var = StringVar()
    self.prd_formula_label = Label(frame, text="Product formula:")
    self.prd_formula_label.grid(row=5, column=0)
    self.cpd2 = Entry(frame, textvariable=self.prd_formula_var)
    self.cpd2.grid(row=5, column=1)

    self.prd_molar_var = DoubleVar()
    self.prd_label = Label(frame, text="Product molar mass:")
    self.prd_label.grid(row=6, column=0)
    self.prd_mol = Entry(frame, textvariable=self.prd_molar_var)
    self.prd_mol.grid(row=6, column=1)

    self.prd_mass_var = DoubleVar()
    self.prd_g_label = Label(frame, text="Product yield:")
    self.prd_g_label.grid(row=7, column=0)
    self.prd_mass = Entry(frame, textvariable=self.prd_mass_var)
    self.prd_mass.grid(row=7, column=1)

    self.calc_btn = Button(frame, text="Calculate", command=self.calc_yield)
    self.calc_btn.grid(row=8, column=0, columnspan=2)

    self.pct_yield_var = StringVar()
    self.pct_label = Label(frame, text="Percent yield: ")
    self.pct_yield = Label(frame, textvariable=self.pct_yield_var)
    self.pct_label.grid(row=9, column=0)
    self.pct_yield.grid(row=9, column=1)

    self.quit_btn = Button(frame, text="QUIT", fg="red", command=frame.quit)
    self.quit_btn.grid(row=10, column=0, columnspan=2)
