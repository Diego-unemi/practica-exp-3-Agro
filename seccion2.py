
from Bio import SeqIO
lengths = []
print("=== Secuencias leídas del archivo ===")
for record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(record.id)
    print(f"Longitud: {len(record.seq)}")
    lengths.append(len(record.seq))
total_secs = len(lengths)
avg_length = sum(lengths) / total_secs
longer_sec = max(lengths)

print("\n***** Estadísticas generales *****")
print(f"Número total de secuencias: {total_secs}")
print(f"Longitud promedio: {avg_length:.2f}")
print(f"Longitud de la secuencia más larga: {longer_sec:.2f}")