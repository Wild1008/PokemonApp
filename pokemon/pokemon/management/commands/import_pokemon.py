import requests
from django.core.management.base import BaseCommand
from pokemon.models import DatosPokemon

class Command(BaseCommand):
    help = "Importa los datos pokemon desde el API"

    def handle(self, *args, **kwargs):
        start = 1
        end = 50 #puede ser editable Segun se necesite    
        
        for pokemon_id in range(start, end +1):
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                # extraer los datos del API
                nombre = data['name']
                tipos = ", ".join([tipo["type"]["name"] for tipo in data["types"]]),
                peso = data["weight"] 
                altura = data["height"]

                # Guardar los datos en la BD
                DatosPokemon.objects.update_or_create(
                    nombre = nombre,
                    tipos = ", ".join(tipos),
                    peso = peso,
                    altura = altura
                )
                self.stdout.write(f"Pokémon {nombre} (ID {pokemon_id}) importado!")
                                           
                          
            except requests.exceptions.HTTPError as error: 
                self.stdout.write(f"Error en Pokémon ID {pokemon_id}: {error}")
            except Exception as e:  
                self.stdout.write(f"Error al importar Pokémon ID {pokemon_id}: {str(e)}")

