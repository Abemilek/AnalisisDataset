import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

conteo_directores = df_movies['directors'].value_counts()

top_10_directores = conteo_directores.head(10)
print("Top 10 directores con más películas:\n")
print(top_10_directores)

top_10_nombres = top_10_directores.index.tolist()
df_top_directores = df_movies[df_movies['directors'].isin(top_10_nombres)].copy()

promedio_rating_directores = df_top_directores.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

print("\nPromedio de calificación del tomatómetro por cada uno de los 10 directores:")
print(promedio_rating_directores)

top_5_directores = promedio_rating_directores.head(5)

plt.figure(figsize=(8,5))
top_5_directores.plot(kind='bar', color='salmon', edgecolor='black')
plt.title("Top 5 directores con mejor calificación promedio del tomatómetro")
plt.xlabel("Director")
plt.ylabel("Promedio tomatometer_rating")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.show()
