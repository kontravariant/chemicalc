from PyQt5.QtWidgets import QMessageBox
from chempy import balance_stoichiometry
import periodictable as pt

# calculation module
def calculate_yield(reagent_list, product_list):
    # dict of {reagent: grams}
    reagent_formulae = parse_inputs(reagent_list)
    # dict of {product: grams}
    product_formulae = parse_inputs(product_list)

    # get all molar input
    #reagent_moles = mole_calc(reagent_formulae)

    # determine limiting reagent

    # calculate theoretical yield

    # calculate percent yield
    ###
    limiter, rxn_eq = get_limiter(reagent_formulae, product_formulae)
    print(limiter, rxn_eq)
    moles_in = int(reagent_formulae.get(limiter)) / pt.formula(limiter).mass
    print(moles_in)
    moles_out = moles_in * rxn_eq

def parse_inputs(input_list):
    return({formula.text(): int(amt.text()) for group in input_list for formula, amt in group.items()})

# get the limiting reagent and product
def get_limiter(reagent_formulae, product_formulae):
     # stoichiometric coefficients
    reac, prod = balance_stoichiometry(reagent_formulae, product_formulae)
    # reagent rxn-moles
    reac_eq = {r: int(reagent_formulae.get(r))/eq for r, eq in reac.items()}
    # produt rxn-moles
    prod_eq = {p: int(product_formulae.get(p))/eq for p, eq in prod.items()}
    for rg, eq in reac_eq.items():
        if eq == min(reac_eq.values()):
            limiter = rg
            rxn_mol = eq
    return (limiter, rxn_mol)