import csv
import joblib

def search_pokemon_info(numPokemon, pokedex):
    infosPokemon = []
    for pokemon in pokedex:
        if int(pokemon[0]) == numPokemon:
            infosPokemon = [pokemon[0], pokemon[1], pokemon[4], pokemon[5], pokemon[6], pokemon[7], pokemon[8], pokemon[9], pokemon[10]]
            break
    return infosPokemon

def prediction(numPokemon1, numPokemon2, pokedex) :
    pokemon1 = search_pokemon_info(numPokemon1, pokedex)
    pokemon2 = search_pokemon_info(numPokemon2, pokedex)
    prediction_model = joblib.load('model/pokemon_model.mod')
    prediction_pokemon_1 = prediction_model.predict([[pokemon1[3], pokemon1[4], pokemon1[5], pokemon1[6], pokemon1[7], pokemon1[8]]])
    prediction_pokemon_2 = prediction_model.predict([[pokemon2[3], pokemon2[4], pokemon2[5], pokemon2[6], pokemon2[7], pokemon2[8]]])
    print(f'COMBAT OPPOSANT : {str(pokemon1[1])} VS {str(pokemon2[1])}')
    print(f'Prediction de victoire de {str(pokemon1[1])} : {str(prediction_pokemon_1[0])}')
    print(f'Prediction de victoire de {str(pokemon2[1])} : {str(prediction_pokemon_2[0])}')
    if prediction_pokemon_1 > prediction_pokemon_2:
        print(f'Le vainqueur est : {str(pokemon1[1])}')
    elif prediction_pokemon_1 < prediction_pokemon_2:
        print(f'Le vainqueur est : {str(pokemon2[1])}')
    else:
        print('Match nul')

with open('data/pokedex.csv', newline='') as csvfile:
    pokedex = csv.reader(csvfile)
    next(pokedex)
    prediction(368, 598, pokedex)

