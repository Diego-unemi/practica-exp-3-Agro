

archivo = open("ls_orchid.fasta", "r")
contenido = archivo.read()
print(contenido[:500])
archivo.close()

secuencia = "ATGCGTACGTAGCTAGCTAGCTA"

def length(secuencia) :
    return len(secuencia)




def bases_count(secuencia):
    return {
        "A": secuencia.count("A"),
        "T": secuencia.count("T"),
        "C": secuencia.count("C"),
        "G": secuencia.count("G"),
    }

#CALCULAR EL PORCENTAJE DE GC

def percentGC(secuencia):
    GC = secuencia.count("G") + secuencia.count("C")
    return (GC / len(secuencia))*100

print("******* RESULTADOS OBTENIDOS *******")
print(f"Secuencia Elegida: {secuencia}")
print(f"Longitud de la Secuencia: {len(secuencia)}")
print("Conteo de las bases GC:", bases_count(secuencia))
print(f"Porcentajes de la bases GC: {percentGC(secuencia):.2f}%")


































