import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

total_peliculas = len(df_movies)
print(f"Total de películas en el dataset: {total_peliculas}")

estado_tomatometro = df_movies['tomatometer_status'].value_counts()
print("\nDistribución de calificaciones del tomatómetro:")
print(estado_tomatometro)

plt.figure(figsize=(6,6))
estado_tomatometro.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Distribución de calificaciones (Tomatómetro)")
plt.ylabel("")
plt.tight_layout()
plt.show()
