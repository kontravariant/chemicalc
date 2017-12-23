from PyQt5.QtWidgets import QMessageBox
from chempy import balance_stoichiometry

# calculation module
def calculate_yield(reagent_list, product_list):
    get_limiters(reagent_list, product_list)

# get the limiting reagent and product
def get_limiters(reagent_list, product_list):
    # dict of {reagent: grams}
    reagent_formulae = {formula.text(): amt.text() for reagent in reagent_list for formula, amt in reagent.items()}
    # dict of {product: grams}
    product_formulae = {formula.text(): amt.text() for product in product_list for formula, amt in product.items()}
    # stoichiometric coefficients
    reac, prod = balance_stoichiometry(reagent_formulae, product_formulae)
    # reagent rxn-moles
    reac_eq = {r: int(reagent_formulae.get(r))/eq for r, eq in reac.items()}
    # produt rxn-moles
    prod_eq = {p: int(product_formulae.get(p))/eq for p, eq in prod.items()}
    print(reac_eq, prod_eq)