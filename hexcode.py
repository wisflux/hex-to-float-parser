# hexcode
hex = "7B3160F"

# stride of 2 digits
n = 2

# Taking 2 digits at a time
for i in range(0, len(hex), n):
    stride = hex[i:i+n]
    # convert hex to decimal
    dec = int(str(stride), 16)
    print(dec)
