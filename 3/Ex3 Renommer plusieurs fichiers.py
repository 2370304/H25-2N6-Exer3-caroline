# importez os
import os
os.chdir(os.path.dirname(__file__))
# # allez dans le dossier Ex3 Videos
os.chdir("Ex3 Videos")
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
for cours in os.listdir():
    nom_fichier,ext =os.path.splitext(cours)
    nom_cour,sujet,numero =nom_fichier.split("_")
    nom_cour =nom_cour.strip()
    sujet =sujet.strip()
    numero =numero.strip()
    numero=numero[1:]
    numero=numero.zfill(2)
    nouveau_nom=(f"{numero} {nom_cour} {sujet}{ext}")
    os.rename(cours,nom_cour)