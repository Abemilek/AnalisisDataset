import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

promedio_criticos = df_movies['tomatometer_rating'].mean()
promedio_audiencia = df_movies['audience_rating'].mean()

print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

plt.figure(figsize=(8,5))
plt.hist(df_movies['rating_diff'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Diferencia entre valoraciones (Audiencia - Críticos)")
plt.xlabel("Diferencia de puntuación")
plt.ylabel("Cantidad de películas")
plt.grid(True)
plt.tight_layout()
plt.show()
