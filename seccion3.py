from seccion1 import secuencia
from Bio import SeqIO
import matplotlib.pyplot as plt

ids = []
longitudes = []
for record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    ids.append(record.id)
    longitudes.append(len(record.seq))
#grafico de barra
plt.figure(figsize = (10,10))
plt.bar(ids[:10], longitudes[:10])
plt.xticks(rotation = 90)
plt.ylabel("Longitud de la secuencia")
plt.title("Longitud de las 10 primeras secuencias")
plt.tight_layout()
plt.savefig("grafico_barra.png")
plt.show()

#grafico pastel
primer_record = next(SeqIO.parse("ls_orchid.fasta", "fasta"))
secuencia = str(primer_record.seq)

bases = {
    "A": secuencia.count("A"),
    "C": secuencia.count("C"),
    "T": secuencia.count("T"),
    "G": secuencia.count("G"),
}

plt.figure(figsize = (10,10))
plt.pie(bases.values(), labels = bases.keys(),autopct = "%1.2f%%",startangle = 90,colors = ['green','blue','red','yellow'])
plt.savefig("grafico_pastel.png")
plt.show()