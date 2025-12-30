print("tree")
print(1+2)

somelist = [1, 2, 3, 4, 5]
for item in somelist:
    print(item)

pokemon_List=["bulbasaur","charmander","squirtle"]
for pokemon in pokemon_List:
    choice=input(f"Do you choose {pokemon}? (y/n) ")
    if choice.lower() == 'y':
        print(f"You chose {pokemon}!")
        saved_pokemon = pokemon
        break
    elif choice.lower() == 'n':
        print(f"You did not choose {pokemon}.")

print(f"You saved {saved_pokemon}!")