"""
Ecrire un script python permettant :
1-recuperer la liste des etudiant
2-les sauvegarder dans un fichier texte 
3-verifier si un nom donner existe deja dans le fichier 
"""
n = int(input("donner le nombre des etudiants \n"))
listeEtudiant = open("liste_etudiant.txt", "w")

for i in range(n):
    nom = input(f"donner le nom etudiant {i+1} : \n ")
    listeEtudiant.write(f"{nom}\n")

listeEtudiant.close()

# rechercher etudiant existe ou pas
print("\n--- recherche etudiant---\n")
nomRecherche = input("donner la recherche : \n")
nomRecherche = nomRecherche+"\n"
listeEtudiant = open("liste_etudiant.txt", "r")
trouve = False
for line in listeEtudiant:
    if line == nomRecherche:
        trouve = True

print(" \n la resultat ----\n")
if trouve == True:
    print("existe\n")
else:
    print("n existe pas\n ")
