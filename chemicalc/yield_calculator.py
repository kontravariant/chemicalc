def calc_yield(self):
    rgt_formula = self.formula_var.get()
    prd_formula = self.prd_formula_var.get()

    if len(rgt_formula) > 2:
        rgt_pt_formula = pt.formula(rgt_formula)
        reagent_weight = rgt_pt_formula.mass
    else:
        reagent_weight = self.molar_var.get()

    if len(prd_formula) > 2:
        prd_pt_formula = pt.formula(prd_formula)
        product_weight = prd_pt_formula.mass
    else:
        product_weight = self.prd_molar_var.get()

    reagent_mass = self.reagent_mass_var.get()
    product_mass = self.prd_mass_var.get()

    rgt_moles = reagent_mass / reagent_weight
    prd_moles = product_mass / product_weight

    pct_yield = prd_moles / rgt_moles * 100
    yd = '{:6.2f}%'.format(pct_yield)
    self.pct_yield_var.set(yd)