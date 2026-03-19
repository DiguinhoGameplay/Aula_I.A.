pib = {
    "china": 23120,
    "usa": 19360,
    "india": 9447,
    "japan": 5405,
    "germany": 4150,
    "russia": 4000,
    "indonesia": 3243,
    "brazil": 3219
}

valores = list(pib.values())
print(valores)

total = sum(valores)
pib["total"] = total

print(pib)