import random

films = [
"Dark Knight",
"Tenet",
"Avengers",
"Fight Club",
"TED"
]

def get_recommendations():
    random.shuffle(films)
    return films[:3]
