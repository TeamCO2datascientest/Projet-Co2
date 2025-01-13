import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random



df_france_2010_2023 = pd.read_csv("df_france_2010_2023.csv")


st.sidebar.title("Sommaire")
pages=["Introduction", "Présentation et pré-traitement des données","Analyse et data visualisation", "Modèles ML et prédictions", "Analyses des résultats", "Conclusions et limites du projet"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.title("Introduction")

  st.header("""Une Course Contre la Montre : Le Défi des Constructeurs Automobiles Européens en 2025 """)
    
  st.markdown("En septembre 2025, un vent d'inquiétude souffle sur les bureaux des plus grands constructeurs automobiles européens. En effet, 14 millards € de pénalités pourraient être infligées aux groupes automobiles en france selon Luca de Meo PDG de Renaul et président du lobby des constructeurs européens, l'ACEA. Face à l'ombre menaçante des nouvelles règles strictes de l'Union européenne sur les émissions de CO2, prévues initialement pour cette année-là, certains fabricants demandent désespérément un délai de deux ans. Mais pourquoi ? Quels sont les enjeux cachés derrière cette requête ? Sont-ils tous concernés ?")

  st.header("Un Projet Ambitieux pour Éclaircir l'Avenir")

  st.write("Nous avons décidé de plonger au cœur de cette problématique en réalisant une étude approfondie. Notre objectif ? Dévoiler les conséquences financières potentielles de ces pénalités pour les géants de l'automobile et identifier les gagnants et les perdants des nouvelles normes anti-pollution. Nous voulons également anticiper les mouvements stratégiques qui pourraient en découler.")

  st.header("Problématique")

  st.write("Les groupes automobiles sont-ils en capacité de respecter la règlementation sur les Emissions de CO2 des véhicules en France à partir de 2025 et d'éviter des pénalités de plusieurs milliards d'Euros ?")


  st.header("Présentation du Sommaire")

  st.write("Notre projet vise à éclaircir ces enjeux à travers une analyse approfondie des données disponibles, menée dans le cadre d'un rapport d'étude 2024-2025 en data analyse avec Datascientest. Ce travail s'articule autour de trois grandes phases. Chaque phase contribuera à mieux comprendre les défis et les opportunités liés à la mise en œuvre des nouvelles régulations sur les émissions de CO2.")

  st.write("I. Présentation du jeu de données et phase de pré-traitement")
  st.write("II. Analyse des données")
  st.write("III. Machine learning")

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
  
  st.image("Fusion des données Gouv et Européeenes.jpg")

  st.dataframe(df_france_2010_2023.head())

  #1er graphique
  fig = plt.figure(figsize=(10,6))
  sns.countplot(x = "ANNEE", data = df_france_2010_2023)
  plt.title("Nombre total de véhicule par année")
  plt.xlabel('Année')
  plt.ylabel('Nombre de véhicules')
  plt.ylim(0,2500000)

  st.pyplot(fig)
  
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

  st.subheader("3.Conclusion sur la concordances deux sources de données")
  st.write("Les tests statistiques sont sans ambiguités si 'on prend le seuil de 1% => il n'y a pas de différence significative (p_value>1%) entre les deux groupes de données gouv et Europe sur les données 2010-2015. Toutefois, nous gardons à l'esprit que la problématique (P_value (0,37 et 0,42 proche du seuil de 0,05) concerne les résultats sur les émissions de CO2 qui est un élement crucial dans l'analyse de notre rapport. A ce stade nous ne jugeons pas nécéssaire de faire d'+analyse complémentaire afin de tester la différence entre les 2 jeux de données.")
  st.write("Par conséquent, nous pouvons réaliser un nouveau jeu de données allant de 2010 à 2023 comprenant la partie gouvernementale (2010- 2015) et la partie européenne de 2016 à 2023.")




if page == pages[2] : 
  st.title("Analyse et data visualisation")

  st.header("A.Emission de Co2 par groupe automobile")
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

  st.header("B.Emissions par typologie d'énergie")

  #4ème graphique
  # Création du dictionnaire des couleurs pour chaque type d'énergie
  colorama_energies = {
    'Essence': 'darkred',
    'Diesel': 'magenta',
    'Flex-Ethanol': 'darkorange',
    'Gaz Naturel': 'mediumspringgreen',
    'Hydrogène': 'lightblue',
    'Hybride': 'purple',
    'Électrique': 'dodgerblue'}

  # Créer un scatter plot avec de la transparence
  fig = plt.figure(figsize=(12, 8))
  scatter = sns.scatterplot(data=df_france_2010_2023,
                          x='CO2(g/km)',
                          y='PUISS_REEL(kW)',
                          hue='ENERGIE',
                          palette=colorama_energies,
                          alpha=0.5,
                          s=100)

  # Ajouter des étiquettes
  plt.title('Graphique de Dispersion : CO2 vs Puissance Réelle par Type d\'Énergie')
  plt.xlabel('CO2 (g/km)')
  plt.ylabel('Puissance Réelle (kW)')
  plt.grid(True)

 # Ajuster la légende
  plt.legend(title='Type d\'Énergie', bbox_to_anchor=(1.05, 1), loc='upper left')

 # Afficher le graphique
  st.pyplot(fig)


  st.header("C.Emissions par type d'automobiles (Carrosserie)")
  # 5ème graphique
  # Filtrer les données pour ne garder que celles où ENERGIE est 'Essence'
  df_essence = df_france_2010_2023[df_france_2010_2023['ENERGIE'] == 'Diesel']

  # Créer une figure
  fig = plt.figure(figsize=(12, 6))

  # Créer une liste de boxplots pour chaque type de carrosserie
  carrosseries = df_essence['CARROSSERIE'].unique()
  data = [df_essence[df_essence['CARROSSERIE'] == carrosserie]['CO2(g/km)'] for carrosserie in carrosseries]

  # Créer le boxplot
  box = plt.boxplot(data, labels=carrosseries, patch_artist=True)

  # Colorier les boxplots selon le dictionnaire colorama_energies
  for i, box in enumerate(box['boxes']):
      box.set_facecolor(colorama_energies['Diesel'])

  # Ajouter des titres et des labels
  plt.title('Boxplot des Émissions de CO2 en fonction de la Carrosserie (Diesel)')
  plt.xlabel('Type de Carrosserie')
  plt.ylabel('Émissions de CO2 (g/km)')
  plt.grid(axis='y')

  # Afficher le boxplot
  plt.tight_layout()
  st.pyplot(fig)


st.header("D.Corrélations dans le temps")
  #6ème graphique

  # Filtrer les données pour ne conserver que celles où 'ENERGIE' est 'Essence'
  df_essence = df_france_2010_2023[df_france_2010_2023['ENERGIE'] == 'Essence']

  # Vérifier que des données existent après filtrage
  if df_essence.empty:
        print("Aucune donnée disponible après le filtrage pour 'Essence'.")
  else:
      # Créer une liste pour stocker les résultats de corrélation
      correlation_results = []

      # Obtenir les années uniques dans le DataFrame
      years = df_essence['ANNEE'].unique()

      # Calculer la corrélation pour chaque année
      for year in sorted(years):
          # Filtrer les données pour l'année actuelle
          df_year = df_essence[df_essence['ANNEE'] == year]

          # Vérifier si des données sont disponibles pour l'année
          if df_year.empty:
              continue  # Passer à l'année suivante si aucune donnée

          # Calculer la matrice de corrélation
          correlation_matrix = df_year.select_dtypes(include=['float64', 'int64']).corr()

          # Vérifier que 'CO2(g/km)' est dans les colonnes
          if 'CO2(g/km)' in correlation_matrix.columns:
              # Extraire les corrélations avec CO2
              co2_correlations = correlation_matrix['CO2(g/km)'].drop('CO2(g/km)')

              # Ajouter les résultats à la liste
              for variable, correlation in co2_correlations.items():
                  correlation_results.append({
                      'ANNEE': year,
                      'VARIABLE': variable,
                      'CORRELATION': correlation})

      # Convertir les résultats en DataFrame
      correlation_df = pd.DataFrame(correlation_results)

      # Vérifier si des corrélations ont été calculées
      if correlation_df.empty:
          print("Aucune corrélation trouvée.")
      else:
          # Visualiser les résultats de corrélation par variable
          fig = plt.figure(figsize=(14, 8))

          # Tracer les lignes pour chaque variable
          sns.lineplot(data=correlation_df, x='ANNEE', y='CORRELATION', hue='VARIABLE', marker='o')

          plt.title('Évolution des Corrélations avec les Émissions de CO2 pour les Véhicules à Essence')
          plt.xlabel('Année')
          plt.ylabel('Coefficient de Corrélation avec CO2')
          plt.axhline(0, color='grey', linestyle='--')
          plt.legend(title='Variables', bbox_to_anchor=(1.05, 1), loc='upper left')
          plt.grid(True)
          plt.xticks(sorted(years))
          plt.tight_layout()
          st.pyplot(fig)




@st.cache_data
def generate_random_value(x): 
  return random.uniform(0, x) 
a = generate_random_value(10) 
b = generate_random_value(20) 
st.write(a) 
st.write(b)














