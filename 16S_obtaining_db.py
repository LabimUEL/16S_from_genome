#coding:utf-8

import os

path_fasta = input("Digite o nome do arquivo .fasta: ")
nome_fasta = os.path.basename(path_fasta)
f1 = open(path_fasta,"r")
#save_path = '../'

#f1 = open("BacillusamyloLFB112.fasta","r")
seqid0 = f1.read()

seqid = seqid0[1:11]

os.system("barrnap "+nome_fasta+" -outseq rnadata.fa")

f2 = open("rnadata.fa","r")

#16s = os.path.join(save_path, 16s_data+seqid+".fa") 

final16S_seq = open("../16s_data_"+nome_fasta+"","w")

rnaseq = f2.readlines()
#print(rnaseq)	#até aqui ok

f2.seek(0)
final16S_seq.write(f2.readline())
final16S_seq.write(f2.readline())
