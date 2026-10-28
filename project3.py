from Bio import SeqIO
import matplotlib.pyplot as plt

print("Читаю файл ecoli.fasta...")
record = SeqIO.read("ecoli.fasta", "fasta")
genome = record.seq

taa_count = genome.count("TAA")
tag_count = genome.count("TAG")
tga_count = genome.count("TGA")

print(f"Количество TAA: {taa_count}")
print(f"Количество TAG: {tag_count}")
print(f"Количество TGA: {tga_count}")

codons = ["TAA", "TAG", "TGA"]
counts = [taa_count, tag_count, tga_count]

plt.figure(figsize=(8, 6))
plt.bar(codons, counts, color=["blue", "green", "red"])
plt.xlabel("Стоп-кодоны")
plt.ylabel("Количество в геноме")
plt.title("Количество стоп-кодонов в геноме E. coli")
plt.show()