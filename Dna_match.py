sample = ['GTA','GGG','CAC']
def read_dna(dna_file):
  dna_data=""
  with open(dna_file,"r") as f:
    for line in f.readline():
      dna_data+=line
   
  return dna_data

def dna_codons(dna):
  codons=[]
  for i in range(0,len(dna),3):
    if((i+3)<len(dna)):
      codons.append(dna[i:i+3])
    return codons  
      

def match_dna(dna):
  matches=0
  for codon in dna:
    if codon in sample:
      print "\n\t"+ codon
      matches+=1
  return matches

def is_criminal(dna_sample):
  dna_data=read_dna(dna_sample)
  codons=dna_codons(dna_data)
  num_matches=match_dna(codons)
  print num_matches
  if(num_matches>=3):
    print "Invaestigation should continue"
  else:
    print "suspect is free"
    
is_criminal("suspect1.txt")    
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
    
  