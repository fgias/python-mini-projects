# Prices in excel-like structure.

# Pseudocode:

position = 0
bank = 200

for price in data:
    if MAC > 0 and position  != 1:
        position = 1
    elif MAC < 0 and position != -1:
        position = -1
    elif MAC > 0:
        pass # Hold.
    elif MAC < 0: 
        pass # Hold.

    exposure = position * (price)
    bank = 200 - exposure


