# chemicalc
GUI Percent Yield calculator for chemical experiments

Graphical application coded in python utilizing Tkinter GUI framework and 'periodictable' library.

Usage:
The application accepts a chemical formula or molar mass for the limiting reagent, as well as the mass used, as well as the chemical formula or molar mass and weight of the product recovered. It produces a percent yield. The calculator prioritizes the chemical formula for calculating molar mass (through the periodictable library).

![application screenshot](https://cloud.githubusercontent.com/assets/7653713/21279640/0fb51eda-c396-11e6-9e07-12255a8e1601.png)

Future Improvements:
* Add an option, i.e. a button that allows you to add as many reagents as participated in the reaction, and let the application determine the limiting reagent from there.
* Add an exception handler, in the case that a chemical formula AND molar mass are entered for any reagent or the product, to determine if they are close enough (\<1 g/mol) and if not, throw an error message indicating that they are not equivalent.

Background:
As a chemistry major, I was constantly calculating percent yield for reactions done in lecture laboratories. I figured it would be useful to have a quick application to access that would calculate it for me, especially one that would determine the limiting reagent for me. I decided it would be especially useful (and distributable) if I added a GUI, and this allowed me to learn tkinter at the same time.

Requirements:
* python3
* periodic table library (easy_install periodictable)

