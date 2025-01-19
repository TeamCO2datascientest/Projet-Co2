import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import config

df_france_2010_2023 = pd.read_csv("df_france_2010_2023.csv")


st.sidebar.title("Sommaire")
pages=["Introduction", "Présentation et pré-traitement des données","Analyse et data visualisation", "Modèles ML et prédictions", "Analyses des résultats", "Conclusions et limites du projet"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.image("Image introduction 1.jpg")
  st.title("Introduction")

  st.header("""Une Course Contre la Montre : Le Défi des Constructeurs Automobiles Européens en 2025 """)
    
  st.markdown("En septembre 2025, un vent d'inquiétude souffle sur les bureaux des plus grands constructeurs automobiles européens. En effet, 14 millards € de pénalités pourraient être infligées aux groupes automobiles en france selon Luca de Meo PDG de Renaul et président du lobby des constructeurs européens, l'ACEA. Face à l'ombre menaçante des nouvelles règles strictes de l'Union européenne sur les émissions de CO2, prévues initialement pour cette année-là, certains fabricants demandent désespérément un délai de deux ans. Mais pourquoi ? Quels sont les enjeux cachés derrière cette requête ? Sont-ils tous concernés ?")

  st.header("Un Projet Ambitieux pour Éclaircir l'Avenir")

  st.write("Nous avons décidé de plonger au cœur de cette problématique en réalisant une étude approfondie. Notre objectif ? Dévoiler les conséquences financières potentielles de ces pénalités pour les géants de l'automobile et identifier les gagnants et les perdants des nouvelles normes anti-pollution. Nous voulons également anticiper les mouvements stratégiques qui pourraient en découler.")

  st.image("Image introduction 2.jpg")
  st.header("Problématique")

  st.write("Les groupes automobiles sont-ils en capacité de respecter la règlementation sur les Emissions de CO2 des véhicules en France à partir de 2025 et d'éviter des pénalités de plusieurs milliards d'Euros ?")


  st.header("Présentation du Sommaire")

  st.write("Notre projet vise à éclaircir ces enjeux à travers une analyse approfondie des données disponibles, menée dans le cadre d'un rapport d'étude 2024-2025 en data analyse avec Datascientest. Ce travail s'articule autour de trois grandes phases. Chaque phase contribuera à mieux comprendre les défis et les opportunités liés à la mise en œuvre des nouvelles régulations sur les émissions de CO2.")

  st.markdown("I. Présentation du jeu de données et phase de pré-traitement")
  st.markdown("II. Analyse des données")
  st.markdown("III. Machine learning")

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
  st.write("Les deux jeux de données étaient très différents tant en terme quantitatif que du nombre de variable.Nous avons analysé les variable des deux jeux de données pour n'y garder uniquement que les variables communes utiles à notre projet.")
  st.write("Nous avons donc décidé de concatener les données des deux sources entre 2010 et 2023 avec 9 variables communes et utiles à notre projet.")
  
  st.image("df_france_2010_2023 HEAD.jpg")



  st.image("Nombre total de véhicule par année.jpg")
  
  st.write("Nous constatons une grande différence dans le nombre de véhicules avant et après 2016. Après vérification sur divers sites, nous validons le fait qu'il y ait si peu de données sur les années antérieures 2017. L'analyse descriptive prendra en compte l'ensemble de la période tandis que le machine learning se portera sur les données à compter de 2017.")
  st.subheader("2.Réalisation des tests statistiques")
  st.write("Réalisation de 4 test statistiques afin valider ou pas la concordance des données.")
  st.write("TEST1 / un test sur les médianes des émissions de CO2/MARQUEÉ")

  st.image("test statistique 1.jpg")

  st.write("Avec le TEST1 (médianes des Émissions de CO2 par Marque), la valeur p-value=0.14,soit au-dessus du seuil de 0.05, on ne peut rejeter l'hypothèse nulle =>il n'y a pas de différence significative entre les deux groupes comparés pour les médianes d'emission de CO2")

  st.write("TEST2 / un test sur les moyennes des émissions de CO2/MARQUE")
  st.image("test statistique 2.jpg")
  st.write("Avec le TEST2 sur les moyennes des émissions de CO2 par marque, nous avons obtenu une valeur p de 0.04, qui est proche du seuil de signification de 0.05. Cela signifie que nous pouvons rejeter l'hypothèse nulle, concluant qu'il existe une différence significative entre les deux groupes comparés")
  
  st.write("TEST3 / un test sur les médianes la consommation/marque")
  st.image("test statistique 3.jpg")
  st.write("Selon le TEST3, qui compare les médianes des consommations par marque, la valeur p obtenue est de 0.76, bien supérieure au seuil de 0.05. Par conséquent, nous ne pouvons pas rejeter l'hypothèse nulle, ce qui indique qu'il n'existe pas de différence significative entre les deux groupes comparés en ce qui concerne les médianes de puissance réelle.")
  
  
  
  st.write("TEST4 / un test sur les moyennes la consommation/marque")
  st.image("test statistique 4.jpg")
  st.write("Selon le TEST4, qui a examiné les moyennes des consommations par marque, nous avons obtenu une valeur p de 0,80, bien supérieure au seuil de 0,05. Par conséquent, nous ne pouvons pas rejeter l'hypothèse nulle. Cela signifie qu'il n'existe pas de différence significative entre les deux groupes comparés en ce qui concerne les moyennes des consommations.")
  st.write("Les tests statistiques sont sans ambiguités si 'on prend le seuil de 1% => il n'y a pas de différence significative (p_value>1%) entre les deux groupes de données gouv et Europe sur les données 2010-2015. Toutefois, nous gardons à l'esprit que la problématique (P_value (0,37 et 0,42 proche du seuil de 0,05) concerne les résultats sur les émissions de CO2 qui est un élement crucial dans l'analyse de notre rapport. A ce stade nous ne jugeons pas nécéssaire de faire d'+analyse complémentaire afin de tester la différence entre les 2 jeux de données.")
  
  st.subheader("3.Conclusion sur la concordances deux sources de données")
  st.image("Fusion des données Gouv et Européeenes.jpg")
  st.write("Par conséquent et étant donné la disparité du nombre de donnée entre les deux source :")
  
  st.markdown("Nous avons préféré ne pas prendre en compte les données de 2001 à 2009 de la source française car nous constations trop peu de donnée. Nous avons fusionnés les données des deux sources entre 2010 et 2015 car nous avons démontré une concordance des données sur la gamme et le type de véhicule (carrosserie).")
  st.markdown("Nous avons donc réalisé un nouveau jeu de données allant de 2010 à 2023 comprenant la partie gouvernementale (2010- 2015) et la partie européenne de 2010 à 2023.")

  


if page == pages[2] : 
  st.title("Analyse et datavisualisation")
  
  #Graphique 1

  st.subheader("A.Emissions de CO2 par groupe automobile")
  st.image("Distribution de CO2 par groupe automobile -graph 1 page 2.jpg")

  st.write("On perçoit 3 grandes catégories de marque:")
  st.markdown("-Les grands emetteurs de CO2 (violet) représentés par des marques de voiture de sport :Aston Martin, Ferrari, Subaru, Mc Laren etc..")
  st.markdown("-Les marques généralistes (en vert) avec beaucoup d'outliers. Cependant, ces derniers restent inférieurs à 600g/gm.")
  st.markdown("-les voitures éléctrique (dont les emissions sont à 0)")


  #Graphique 2
  st.image("Histogramme des emissions de CO2 - graph 2 page 2.jpg")

  st.write("L'analyse des valeurs extrêmes montre l'importance du nombre de valeurs extrêmes au-dessus et en dessous des bornes. Cependant, pour les valeurs extrêmes au-dessus, leur visualisation montre une certaine tenue en dessous de 600g/km pour l'ensemble des groupes. Aussi, nous decidons de conserver ces valeurs et les considérons comme les véhicules les plus emetteurs de CO2. S'agissant des valeurs en dessous de la borne basse, il s'agit des meilleurs véhicules. Les valeurs à 0 correspondent aux véhicules principalement électriques.")



  #Graphique 3
  st.subheader("B.Emissions par typologie d'énergie")
  st.image("Graphique de Dispersion CO2 vs Puissance réelle par type d'Energie - graph 3 page 2.jpg")


  st.subheader("C.Emissions par type d'automobiles (Carrosserie)")
  # graphique 4
  st.image("Boxplot des emissions de CO2 en fonction de la carrosserie (essence) graph 4 page 2.jpg")


  st.subheader("D.Corrélations dans le temps")
  # graphique 5
  st.image("Evolution des corrélations avec les emissions de CO2 pour les véhicules à essence graph 5 page 2.jpg")





@st.cache_data
def generate_random_value(x): 
  return random.uniform(0, x) 
a = generate_random_value(10) 
b = generate_random_value(20) 
st.write(a) 
st.write(b)














