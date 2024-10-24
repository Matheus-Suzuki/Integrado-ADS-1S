import cDefs
df = cDefs.management('stock')

df.addProduct(input('nome '), input('quantidade'))

df.connsultProduct(input('produto'))

df.connsultProducts()