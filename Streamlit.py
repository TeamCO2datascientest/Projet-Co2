import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib





df_france_2010_2023 = pd.read_csv("df_france_2010_2023.csv")


st.sidebar.title("Sommaire")
pages=["Introduction", "Jeu de données", "Phase de Pré-traitement","Analyse et data visualisation", "Modèles ML et prédictions", "Analyses des résultats", "Conclusions et limites du projet"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
    st.title("Introduction")

    st.header("Une Course Contre la Montre : Le Défi des Constructeurs Automobiles Européens en 2025 ")
    
    st.write("En septembre 2025, un vent d'inquiétude souffle sur les bureaux des plus grands constructeurs automobiles européens. En effet, 14 millards € de pénalités pourraient être infligées aux groupes automobiles en france selon Luca de Meo PDG de Renaul et président du lobby des constructeurs européens, l'ACEA. Face à l'ombre menaçante des nouvelles règles strictes de l'Union européenne sur les émissions de CO2, prévues initialement pour cette année-là, certains fabricants demandent désespérément un délai de deux ans. Mais pourquoi ? Quels sont les enjeux cachés derrière cette requête ? Sont-ils tous concernés ?")

    st.header("Un Projet Ambitieux pour Éclaircir l'Avenir")

    st.write("Nous avons décidé de plonger au cœur de cette problématique en réalisant une étude approfondie. Notre objectif ? Dévoiler les conséquences financières potentielles de ces pénalités pour les géants de l'automobile et identifier les gagnants et les perdants des nouvelles normes anti-pollution. Nous voulons également anticiper les mouvements stratégiques qui pourraient en découler.")

    st.header("Problématique")

    st.write("Les groupes automobiles sont -ils en capacité de respecter la règlementation sur les Emissions de CO2 des véhicules en France à partir de 2025 et d'éviter des pénalités de plusieurs milliards d'Euros ?")


    st.header("Présentation du Sommaire")

    st.write("Notre projet vise à éclaircir ces enjeux à travers une analyse approfondie des données disponibles, menée dans le cadre d'un rapport d'étude 2024-2025 en data analyse avec Datascientest. Ce travail s'articule autour de trois grandes phases. Chaque phase contribuera à mieux comprendre les défis et les opportunités liés à la mise en œuvre des nouvelles régulations sur les émissions de CO2.")

    st.write("I. Présentation du jeu de données et phase de pré-traitement")
    st.write("II. Analyse des données")
    st.write("III. Machine learning")

if page == pages[1] : 
  st.title("Présentation du jeu de données")







if page == pages[2] : 
  st.title("Phase de Pré-traitement")

  st.markdown("Afin de nous assurer de la continuité des données de 2010 à 2023, nous devons nous vérifier la concordance des données entre les données gouv et les données européennes")

  st.image('Fusion des données Gouv et Européeenes.jpg')

  st.markdown("La concordance des données se réalisera en trois grandes étapes:")

  st.markdown("1.Uniformisation des données")
  st.markdown("2.Réalisation des tests statistiques")
  st.markdown("3.Conclusion sur la concordance")



if page == pages[3] : 
  st.title("Analyse et data visualisation")

  st.header("A.Présentation du jeu de données")

  # Aperçu général
  st.dataframe(df_france_2010_2023.head())


  st.subheader("Statistiques descriptives")
  st.dataframe(df_france_2010_2023.describe())

  sns.set()

  #1er graphique
  fig = plt.figure(figsize=(10,6))
  sns.countplot(x = "ANNEE", data = df_france_2010_2023)
  plt.title("Nombre total de véhicule par année")
  plt.xlabel('Année')
  plt.ylabel('Nombre de véhicules')
  plt.ylim(0,2500000)

  st.pyplot(fig)

  st.write("Nous constatons une grande différence dans le nombre de véhicules avant et après 2016. Après vérification sur divers sites, nous validons le fait qu'il y ait si peu de données sur les années antérieures 2017. L'analyse descriptive prendra en compte l'ensemble de la période tandis que le machine learning se portera sur les données à compter de 2017.")


  st.header("B.Emission de Co2 par groupe automobile")
  #2ème graphique
  # Calculer les médianes de 'CO2(g/km)' par groupe automobile
  medians = df_france_2010_2023.groupby('Groupe_auto')['CO2(g/km)'].median().sort_values(ascending=False)

  # Calculer les médianes de 'CO2(g/km)' par groupe automobile
  medians = df_france_2010_2023.groupby('Groupe_auto')['CO2(g/km)'].median().sort_values(ascending=False)

  # Réorganiser les groupes automobiles par médiane décroissante
  df_france_2010_2023['Groupe_auto'] = pd.Categorical(df_france_2010_2023['Groupe_auto'], categories=medians.index, ordered=True)

  # Tracer le boxplot
  fig = plt.figure(figsize=(15, 7))
  sns.boxplot(x='Groupe_auto', y='CO2(g/km)', data=df_france_2010_2023, palette='viridis')

  # Ajuster les étiquettes de l'axe des x pour une meilleure lisibilité
  plt.xticks(rotation=90)

  # Titre et étiquettes des axes
  plt.title('Distribution de CO2 (g/km) par Groupe Automobile', fontsize=15)
  plt.xlabel('Groupe Automobile', fontsize=12)
  plt.ylabel('CO2 (g/km)', fontsize=12)

  # Afficher le graphique
  st.pyplot(fig)

  st.write("On perçoit 3 grandes catégories de marque:")
  st.write("Les grands emetteurs de CO2 (violet) représentés par des marques de voiture de sport :Aston Martin, Ferrari, Subaru, Mc Laren etc..")
  st.write("Les marques généralistes (en vert) avec beaucoup d'outliers. Cependant, ces derniers restent inférieurs à 600g/gm.")
  st.write("les voitures éléctrique (dont les emissions sont à 0)")


  #3ème graphique
  # Calcul des quartiles et de l'IQR
  Q1 = df_france_2010_2023['CO2(g/km)'].quantile(0.25)
  Q3 = df_france_2010_2023['CO2(g/km)'].quantile(0.75)
  IQR = Q3 - Q1

  # Détection des valeurs aberrantes
  borne_inferieure = Q1 - 1.5 * IQR
  borne_superieure = Q3 + 1.5 * IQR

  # Séparation des valeurs aberrantes en fonction des bornes
  valeurs_aberrantes_inferieures = df_france_2010_2023[df_france_2010_2023['CO2(g/km)'] < borne_inferieure]
  valeurs_aberrantes_superieures = df_france_2010_2023[df_france_2010_2023['CO2(g/km)'] > borne_superieure]
  valeurs_normales = df_france_2010_2023[(df_france_2010_2023['CO2(g/km)'] >= borne_inferieure) & (df_france_2010_2023['CO2(g/km)'] <= borne_superieure)]

  fig = plt.figure(figsize=(12, 6))

  # Histogramme pour les valeurs normales
  sns.histplot(valeurs_normales['CO2(g/km)'], color='blue', label='Valeurs normales', bins=30)

  # Histogramme pour les valeurs aberrantes inférieures
  if not valeurs_aberrantes_inferieures.empty:
    sns.histplot(valeurs_aberrantes_inferieures['CO2(g/km)'], color='red', label='Valeurs aberrantes inférieures', bins=30)

  # Histogramme pour les valeurs aberrantes supérieures
  if not valeurs_aberrantes_superieures.empty:
    sns.histplot(valeurs_aberrantes_superieures['CO2(g/km)'], color='green', label='Valeurs aberrantes supérieures', bins=30)

  # Ajouter des lignes pour les bornes
  plt.axvline(borne_inferieure, color='r', linestyle='--', label='Borne inférieure')
  plt.axvline(borne_superieure, color='g', linestyle='--', label='Borne supérieure')

  plt.title('Histogramme des émissions de CO2 (g/km)')
  plt.xlabel('CO2 (g/km)')
  plt.ylabel('Fréquence')
  plt.legend()
  st.pyplot(fig)

  st.write("L'analyse des valeurs extrêmes montre l'importance du nombre de valeurs extrêmes au-dessus et en dessous des bornes. Cependant, pour les valeurs extrêmes au-dessus, leur visualisation montre une certaine tenue en dessous de 600g/km pour l'ensemble des groupes. Aussi, nous decidons de conserver ces valeurs et les considérons comme les véhicules les plus emetteurs de CO2. S'agissant des valeurs en dessous de la borne basse, il s'agit des meilleurs véhicules. Les valeurs à 0 correspondent aux véhicules principalement électriques.")







 
 



  
  
  

 
  



  





















