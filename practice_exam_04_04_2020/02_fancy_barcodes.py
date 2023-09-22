import re

n = int(input())
pattern_barcode = r'@#+([A-Z][A-Za-z\d]{4,}[A-Z])@#+'
pattern_numbers = r'\d'
for barcodes in range(n):
    barcode = input()
    match = re.findall(pattern_barcode, barcode)
    if len(match) == 0:
        print("Invalid barcode")
    else:
        number_match = re.findall(pattern_numbers, barcode)
        if len(number_match) == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(number_match)}")
