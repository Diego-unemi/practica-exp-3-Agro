from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

proteina = dna.translate()

print('-------------------------')

print("Traducir una secuencia DNA a proteínas")
print("DNA:      ", dna)
print("Proteína: ", proteina)
print('-------------------------')

# Buscar el motivo

motivos = ["ATG", "GCGG", "TGG"]
print("Buscar un motivo dentro de una secuencia (ATG, GCGG, etc.)")
for motivo in motivos:
    posicion = dna.find(motivo)
    if posicion != -1:
        print(f"Motivo '{motivo}' encontrado en la posición {posicion}")
    else:
        print(f"Motivo '{motivo}' no encontrado")

print()
print("Tabla de resultados")
print("{:<10} {:<20}".format("Motivo", "Posición (índice)"))
print("-" * 30)

for motivo in motivos:
    posicion = dna.find(motivo)
    if posicion != -1:
        print("{:<10} {:<20}".format(motivo, posicion))
    else:
        print("{:<10} {:<20}".format(motivo, "No encontrado"))

# Tabla de resultados

with open("resultados.txt", "w") as f:
    f.write("Resultados del análisis de secuencia DNA\n")
    f.write(f"DNA: {dna}\n")
    f.write(f"Proteína: {proteina}\n\n")
    f.write("Motivo\tPosición (índice)\n")
    f.write("-" * 30 + "\n")
    for motivo in motivos:
        posicion = dna.find(motivo)
        if posicion != -1:
            f.write(f"{motivo}\t{posicion}\n")
        else:
            f.write(f"{motivo}\tNo encontrado\n")
