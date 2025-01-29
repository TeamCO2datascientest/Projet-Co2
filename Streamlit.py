import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random


df_france_2010_2023 = pd.read_csv("df_france_2010_2023.csv")


st.sidebar.title("Sommaire")
pages=["Introduction", "Présentation et pré-traitement des données","Analyse et data visualisation", "Modèles ML et prédictions", "Calcul des pénalités","Conclusions et limites du projet"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.title("Introduction")
  st.subheader("1.Qu'est que le CO2 et les gas à effet de serre?")
  st.image("Introduction image 1 et 2.jpg")
  st.subheader("2.Prise de conscience des enjeux climatiques")
  st.image("Introduction image 3.jpg")
  st.subheader("3.L'impact des risques naturels")
  st.image("Introduction image 4.jpg")
  st.subheader("4.Objectif de limité la hausse de 2 degrés Celsius d'ici 2100")
  st.image("Introduction image 5.jpg")
  st.subheader("5.Les 10 pays les plus émetteurs de CO2")
  st.image("Introduction image 6.jpg")
  st.subheader("6.Les sources d'émission au sein de l'Union Européenne")
  st.image("Introduction image 7.jpg")




if page == pages[1] : 
  st.title("Présentation et pré-traitement des données")

  URL = "https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_"

  st.write("Pour présenter cette analyse, nous nous sommes appuyés sur deux sources de donnée: ")
  st.write("1. Source gouvernement français: Emissions de CO2 et de polluants des véhicules commercialisés en France entre 2001 et 2015 [Lien vers le jeu de donnée](https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_)")
  st.write("2. Souce European Environment Agency: Monitoring of CO2 emissions from passenger cars Regulation (EU) 2019/631 entre 2010 et 2023 [Lien vers le jeu de donnée](https://www.eea.europa.eu/en/datahub/datahubitem-view/fa8b1229-3db6-495d-b18e-9c9b3267c02b)")

  st.markdown("La concordance des données se réalisera en trois grandes étapes:")

  st.markdown("1.Uniformisation des données")
  st.markdown("2.Réalisation des tests statistiques")
  st.markdown("3.Conclusion sur la concordance")

  st.subheader("1. Uniformisation des données entres les deux sources de donneés")
  st.image("Prétraitement des données - image 1.jpg")
  st.write("Les deux jeux de données étaient très différents tant en terme quantitatif que du nombre de variable.Nous avons analysé les variable des deux jeux de données pour n'y garder uniquement que les variables communes utiles à notre projet.")
  st.image("Prétraitement des données - image 2.jpg")
  st.write("Nous avons donc décidé de concatener les données des deux sources entre 2010 et 2023 avec 9 variables communes et utiles à notre projet.")
  st.image("Prétraitement des données - image 3 et 4.jpg")
  st.subheader("2.Réalisation des tests statistiques")
  st.image("Prétraitement des données - image 5.jpg")
  
  st.subheader("3.Conclusion sur la concordances deux sources de données")
  st.markdown("Les résultats des test statistiques sont concluants avec une similarité des jeux de données sur 3 tests sur 4")
  st.markdown("Nous avons préféré ne pas prendre en compte les données de 2001 à 2009 de la source française car nous constations trop peu de donnée. Nous avons fusionnés les données des deux sources entre 2010 et 2015 car nous avons démontré une concordance des données sur la gamme et le type de véhicule (carrosserie).")
  st.markdown("Nous avons donc réalisé un nouveau jeu de données allant de 2010 à 2023 comprenant la partie gouvernementale (2010- 2015) et la partie européenne de 2010 à 2023.")

  

if page == pages[2] : 
  st.title("Analyse et datavisualisation")
  
  st.subheader("A.Emissions de CO2 par groupe automobile")
  st.image("Datavisualisation - image 1.jpg")

  st.write("On perçoit 3 grandes catégories de marque:")
  st.markdown("-Les grands emetteurs de CO2 (violet) représentés par des marques de voiture de sport :Aston Martin, Ferrari, Subaru, Mc Laren etc..")
  st.markdown("-Les marques généralistes (en vert) avec beaucoup d'outliers. Cependant, ces derniers restent inférieurs à 600g/gm.")
  st.markdown("-les voitures éléctrique (dont les emissions sont à 0)")

  st.image("Datavisualisation - image 2.jpg")
  st.write("L'analyse des valeurs extrêmes montre l'importance du nombre de valeurs extrêmes au-dessus et en dessous des bornes. Cependant, pour les valeurs extrêmes au-dessus, leur visualisation montre une certaine tenue en dessous de 600g/km pour l'ensemble des groupes. Aussi, nous decidons de conserver ces valeurs et les considérons comme les véhicules les plus emetteurs de CO2. S'agissant des valeurs en dessous de la borne basse, il s'agit des meilleurs véhicules. Les valeurs à 0 correspondent aux véhicules principalement électriques.")

 
  st.subheader("B.Emissions par typologie d'énergie")
  st.image("Datavisualisation - image 3.jpg")


  st.subheader("C.Emissions par type d'automobiles (Carrosserie)")
  st.image("Datavisualisation - image 4.jpg")
  st.image("Datavisualisation - image 5.jpg")


  st.subheader("D.Corrélations dans le temps")
  st.image("Datavisualisation - image 6.jpg")

if page == pages[3] :
  st.title("Modèles ML et prédictions")
  st.subheader("Présentation globale de la méthode")
  st.image("Présentation globale de la méthode - image 1.jpg")

  st.subheader("1.Modèle Machine learning : Arbre de décisions")
  st.image("Arbre de décisions - image 1.jpg")
  st.image("Arbre de décisions - image 2.jpg")
  st.image("Arbre de décisions - image 3.jpg")
  st.image("Arbre de décisions - image 4.jpg")

  st.subheader("2.Les autres modèles de Machine Learning")
  st.image("Autres modèles de ML - image 1.jpg")
  st.image("Autres modèles de ML - image 2.jpg")
  st.image("Autres modèles de ML - image 3.jpg")

  st.subheader("3.Focus régression multiple")
  st.image("Focus régression multiple - image 1.jpg")
  st.image("Focus régression multiple - image 2.jpg")
  st.image("Focus régression multiple - image 3.jpg")
  st.image("Focus régression multiple - image 4.jpg")
  st.image("Focus régression multiple - image 5.jpg")

if page == pages[4] :
  st.title("Calcul des penalités")
  st.subheader("1.Mode de calcul")
  st.markdown("(ÉMISSIONS EXCÉDENTAIRES × 95 EUR) × NOMBRE DE VÉHICULES NOUVELLEMENT IMMATRICULÉS*.")
  st.write("RÈGLEMENT (UE) 2019/ 631 DU PARLEMENT EUROPÉEN ET DU CONSEIL - du 17 avril 2019 [Lien vers l'URL](https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX:32019R0631)")

  st.subheader("2.Comparaison des pénalités selon les modèles de Machine Learning")
  st.image("Pénalités - image 1.jpg")
  st.image("Pénalités - image 2.jpg")

if page == pages[5] :
  st.title("Conclusions et limites du projet")
  st.subheader("1.Les options stratégiques")
  st.image("conclusions - image 1.jpg")

  st.subheader("2.Avantages et limites du projet")
  st.image("conclusions - image 2.jpg")