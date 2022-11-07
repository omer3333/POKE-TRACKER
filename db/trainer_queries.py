SELECT_POKEMON_BY_TRAINER = "select name from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id where pokemon_trainer.trainer_name='{trainer_name}'"
SELECT_TRAINER="select * from trainer where name='{name}"

INSERT_TRAINER ="INSERT IGNORE into trainer(name, town) values('{name}','{town}')"
INSERT_POKEMON_TO_TRAINER = "INSERT into pokemon_trainer(pokemon_id, trainer_name) values({pokemon_id}, '{trainer_name}'"

DELETE_POKEMON_FROM_TRAINER = "delete pt from pokemon_trainer as pt join pokemon on pokemon.id=pt.pokemon_id where pt.trainer_name='{trainer_name}' and pokemon.name='{pokemon_name}'"

UPDATE_TRAINER_CITY = "update trainer set town='{town}' where name='{trainer_name}'"
