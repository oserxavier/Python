
# coding: utf-8

# In[10]:


import urllib.request
# urllib.request.urlopen ('link').read -> vou buscar dentro dessa url abaixo
content = urllib.request.urlopen('https://www.melhorcambio.com/dolar-hoje').read()
# Abaixo faço a conversão do que foi extraído da url para string
content = str(content)
# O find é uma variável que está próximo do valor que pretendo buscar, nesse caso o valor do dolar
find = '<input type="hidden" value="'
# Calcula a posição para buscar o valor do dolar
posicao = int(content.index(find) + len(find))
# Na variavel dolar o valor exato da cotação de acordo com a posição
dolar = content[ posicao : posicao  + 4]
# Abaixo se aplicam as mesmas regras conforme citado acima
content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
content = str(content)
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao  + 4]

print("Dolar: " + dolar)
print("Euro: " + euro)

