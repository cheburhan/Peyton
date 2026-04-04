import re

text = input()
sequences = re.findall('\d{2,}', text)
#квантификатор {2,} значит повторятся от 2храз
if sequences:
    print(' '.join(sequences))
else:
    print() 