import zipfile

with zipfile.ZipFile("voyna-i-mir.zip", "r") as myzip:
    myzip.extractall()
voyna_i_mir = open('voyna-i-mir.txt', 'r', encoding='utf-8')
text = voyna_i_mir.read().split()
symbols = ''.join(text)
quantity = {}
for letter in symbols:
    quantity.setdefault(letter, 0)
    quantity[letter] += 1
sort_voyna_i_mir = sorted(quantity.items(), key=lambda x: x[1])
sort_voyna_i_mir_dict = dict(sort_voyna_i_mir)
print(sort_voyna_i_mir_dict)
