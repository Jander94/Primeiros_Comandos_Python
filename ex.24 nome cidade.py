#cidade = str(input('Nome da cidade: ')).strip()
#p = cidade.split()
#a = p[0].lower()
#print(a == 'santo')

#outo jeito
cid = str(input('Nome da cidade: ')).strip()
print(cid[:5].lower() == 'santo')
