#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = f"The price is {45:.2f} dollars."
print(txt)

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = f"The price is {45:f} dollars."
print(txt)
