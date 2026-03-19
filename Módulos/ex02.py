import calendar

# A
print(calendar.isleap(2018))

# B
dia = calendar.weekday(1992, 5, 22)
print(dia)

# C
dia = calendar.weekday(2000, 7, 1)
dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
print(dias[dia])