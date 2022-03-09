from utilidadescev import moeda
from utilidadescev import dado
moeda.limpar()

p = dado.leiaDinheiro('Digite um valor: R$ ')
moeda.resumo(p, 50, 50)
