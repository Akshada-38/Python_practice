#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = f"The price is {x:F} dollars."
print(txt)

#same example, but with a lower case f:

txt = f"The price is {x:f} dollars."
print(txt)
