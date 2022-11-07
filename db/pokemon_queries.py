SELECT_HEVIEST_POKEMON = "Select * from pokemon where weight = (select MAX(weight) from pokemon)"
SELECT_BY_TYPE ="select name from pokemon join pokemon_types on pokemon_types.pokemon_id=pokemon.id WHERE pokemon_types.type_name='{type}'"
SELECT_OWNER_BY_POKEMON ="select trainer_name from pokemon_trainer join pokemon on pokemon.id= pokemon_trainer.pokemon_id where pokemon.name='{pokemon_name}'"
SELECT_MOST_OWEND_POKEMON ="select name, COUNT(*) as val from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id GROUP BY pokemon.name ORDER by val DESC limit 2"
SELECT_POKEMON ="select * from pokemon where name='{name}'"

INSERT_POKEMON_TYPES ="INSERT into pokemon_types(pokemon_id, type_name) values({pokemon_id},'{type_name}')"
INSERT_TYPE="INSERT IGNORE into types(name) values('{name}')"
INSERT_POKEMON ="INSERT IGNORE into pokemon(id, name, height, weight) values({id}, '{name}', {height},{weight})"