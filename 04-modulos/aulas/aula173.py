# json.dumps e json.loads com strings 
# typing.TypedDict

import json
from typing import TypedDict

# classe com tipagem
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float
    

json_str = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''


filme: Movie = json.loads(json_str)
print(filme['title']) # formato: dict


json_ = json.dumps(filme, ensure_ascii=False, indent=2)

print(json_) # formato: json