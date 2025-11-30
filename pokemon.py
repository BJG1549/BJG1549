
from formatting_pokeDicts import main_formatting

def format_per_type(input_dict_per_pokemon): #formats effectiveness dictionary so keys/catergories are the types not the pokemon
    output_dict_per_type = {} #end dictionary

    for pokemon in input_dict_per_pokemon: #iterates through the individual pokemon in the origiopnal dictionary

        for element in input_dict_per_pokemon[pokemon]: #iterates through the elements each pokemon is effective against

            if element in output_dict_per_type: #for if set already created for that type
                output_dict_per_type[element].add(pokemon) #adds pokemon to the type's set

            else: #for when this type's set hasn't already been created
                output_dict_per_type[element] = {pokemon} #creates new key under that type with the pokemon as a value

    return output_dict_per_type #returns the end dictionary

def type_left_list_creator(input_dict_per_type): #creates a set holding all the types covered by pokemon stored
    type_list = [] #set of all the types

    for element in input_dict_per_type: #iterates through all the types in the dictionary per type 
        type_list.append(element) #adds weach type to the set
    
    return type_list #returns the end set

def remove_pokemon_fromDicts(per_pokemon_dict_in, per_type_dict_in, pokemon):


    per_pokemon_dict_out = per_pokemon_dict_in
    per_type_dict_out = per_type_dict_in

    for type in per_pokemon_dict_in[pokemon]:
        per_type_dict_out[type].remove(pokemon)
    per_pokemon_dict_out.pop(pokemon)
    
def make_copy_list(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item)
    
    return output_list

def make_copy_set(input_set):
    output_set = set()
    for item in input_set:
        output_set.add(item)
    return output_set

def type_iterator(effectiveness_per_pokemon_input, end_list_teams_input, effectiveness_per_type_input, type_left_list_input, current_team_set_input, team_added): 
    #iterates through all pokemon in a remaining type

    if len(type_left_list_input) != 0: #tests for if all types have been covered (type's left set is empty) 

        for type in type_left_list_input:
            for pokemon in effectiveness_per_type_input[type]: #arbitrarily selects a type from the types left and iterates through th epokemon 
                                                                                #for it
                current_team_set_output = make_copy_set(current_team_set_input)
                 #stores the input current team as variable                                                                   
                type_left_list_output = make_copy_list(type_left_list_input) #stores the types left each iteration so that each loop is separate 
                for pok_type in effectiveness_per_pokemon_input[pokemon]: #iterates through the types that the selected pokemon covers
                    if pok_type in type_left_list_output: #checks to see if pok_type is already removed from the set, stops error
                        type_left_list_output.remove(pok_type) #removes the type from the remaining types  
                    else: #if type already removed
                        pass #fine, just keep going
                current_team_set_output.add(pokemon)
                end_list_teams_output, team_added_out = type_iterator(effectiveness_per_pokemon_input, end_list_teams_input, effectiveness_per_type_input, 
                                                                    type_left_list_output, current_team_set_output, team_added)
        return end_list_teams_output, team_added_out

    else: #the type's left set is empty, so all types have been covered
        end_list_teams_output = end_list_teams_input
        if not team_added:
            team_added_out = team_added
            end_list_teams_output.append(current_team_set_input)
            print(current_team_set_input)
            team_added_out = True

        return end_list_teams_output, team_added_out



def main(): #runs everything
    effectiveness_per_pokemon = {"snorlax": {"psychic", "ghost"}, #dictionary for input for what each pokemon is effective against
                               "arcanine": {"grass", "ice", "bug", "steel", "psychic", "ghost"},
                               "sandslash": {"fire", "electric", "poison", "rock", "steel"},
                               "nidoking": {"grass", "fairy"},
                               "vileplume": {"water", "ground", "rock", "fighting", "dragon", "dark"},
                               "pikachu": {"water", "flying"},
                               "raticate_normal": {"psychic", "ghost"},
                               "butterfree": {"grass", "psychic", "dark", "fighting", "poison"},
                               "spearow": {"grass", "fighting", "bug"},
                               "guarados": {"fire", "ground", "psychic", "ghost"},
                               "golbat": {"grass", "dark", "ghost"},
                               "graveler": {"fire", "electric", "poison", "rock"},

                               }
    
    output_list_teams = [] #the end list of sets of the teams

    set_current_team = set()
    
    effectiveness_per_type = format_per_type(effectiveness_per_pokemon) #runs the function that changes the previous dictionary to be per pokemon type vs per 
                                                                        #pokemon

    main_formatting(effectiveness_per_type)
    
    type_left_list = type_left_list_creator(effectiveness_per_type) #creates the set of the remaining types which need to be covered  

    all_team_list, team_built_var = type_iterator(effectiveness_per_pokemon, output_list_teams, effectiveness_per_type, 
                                                  type_left_list, set_current_team, False) #runs the function which creates the 
    # full list containing all the teams as sets
    print(all_team_list)
    return all_team_list
for team in main():
    if len(team) <= 10:
        print(True)
        print(team)
    else:
        print(team)

'''should start with one random type like it currently does then iterate through each remaining 
type instead of randomly selecting another type and sticking with that one. right now it locks 
in a particular order and iterates and then unfolds, instead of trying each type for the current 
type selected. '''
    






