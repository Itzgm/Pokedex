import requests
# Pokedex - Um programa simples para buscar informções sobre Pokémons usando a PokeAPI
# Uma lista de tradução dos tipos de Pokémon

traducao_tipos = {
    "normal": "Normal",
    "fire": "Fogo",
    "water": "Água",
    "electric": "Elétrico",
    "grass": "Planta",
    "ice": "Gelo",
    "fighting": "Lutador",
    "poison": "Venenoso",
    "ground": "Terrestre",
    "flying": "Voador",
    "psychic": "Psíquico",
    "bug": "Inseto",
    "rock": "Pedra",
    "ghost": "Fantasma",
    "dragon": "Dragão",
    "dark": "Sombrio",
    "steel": "Metálico",
    "fairy": "Fada"
}

while True:
    pokemon = input("Digite o nome de um Pokémon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        nome_pokemon = dados['name']
        tipos = [traducao_tipos.get(t['type']['name'], t['type']['name'].capitalize()) for t in dados['types']]
        tipos_pokemon = ", ".join(tipos)
        altura_pokemon = dados['height']
        experiencia_pokemon = dados['base_experience']
        print(f"""{'-'*30}
Nome: {nome_pokemon.capitalize()}
{'-'*30}
Tipo: {tipos_pokemon.capitalize()}
{'-'*30}
Altura: {altura_pokemon*10} cm
{'-'*30}
Experiência Base: {experiencia_pokemon}
{'-'*30}""")
    else:
        print("Pokémon não encontrado. Tente novamente.")
        continue
    novamente = input("Deseja pesquisar outro Pokémon? (s/n): ").strip().lower()
    if novamente not in ['s', 'sim']:
        print("Obrigado por usar o Pokedex!")
        break