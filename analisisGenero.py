import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

df_movies_copy = df_movies.copy()

df_genres_exploded = df_movies_copy.assign(
    genre=df_movies_copy['genre'].dropna().str.split(',')
).explode('genre')

df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

promedio_por_genero = df_genres_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)

print("Top 10 géneros con mayor promedio de audiencia:\n")
print(promedio_por_genero.head(10))

top_10_generos = promedio_por_genero.head(10)

plt.figure(figsize=(7,7))
top_10_generos.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Top 10 géneros por calificación promedio de audiencia")
plt.ylabel("")
plt.tight_layout()
plt.show()
