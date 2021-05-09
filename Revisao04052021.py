# 6 ^2 ^ é o bitwise que é uma subtração vai ser sepre o maior menos o menor
# x & y ignora o valor das variaveis e soma 1
# x | y pega o maior valor


# Quantos segundos há em 42 minutos e 42 segundos?
# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

# Se você correr 10 quilômetros em 42 minutos e 42
# segundos, qual é o seu passo médio
# (tempo por milha em minutos e segundos)?
# Qual é a sua velocidade média em milhas por hora?

minutos = 42
segundos = 42
contador = (minutos*60) + segundos
print("Em {minutos} minutos e {segundos} segundos há: " +
str(contador) + "segundos")

km = 10
milha = km/1.61
print("Quantidade de milhas em 10 km: " + str(milha))

print("Se percorreu 1 milha em {:.2f} segundos".format(segundos/6.21))
print("se percorreu 1 milha em {:.2f} minutos".format((segundos/6.21)/60))
print("o corredor fez uma média de {:.2f} milhas por hora".format(6.21/(segundos/3600)))



