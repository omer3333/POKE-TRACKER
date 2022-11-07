USE poketracker;

-- -- create database poketracker;

-- -- Create table pokemon(
-- --     id int Not null primary key,
-- --     name varchar(20),
-- --     height int,
-- --     weight int
-- -- );

-- -- create table trainer(
-- --     name varchar(20) not null primary key,
-- --     town varchar(20)
-- -- );

-- -- create table types(
-- --     name varchar(20) not null primary key
-- -- );

-- create table pokemon_types(
--     pokemon_id int not null,
--     type_name varchar(20) not null,
--     foreign key(pokemon_id) references pokemon(id),
--     foreign key(type_name) references types(name),
--     primary key (pokemon_id, type_name) 
-- );

-- -- create table pokemon_trainer(
-- --     trainer_name varchar(20) not null,
-- --     pokemon_id int not null,
-- --     foreign key(pokemon_id) references pokemon(id),
-- --     foreign key(trainer_name) references trainer(name),
-- --     primary key(trainer_name, pokemon_id) 

-- -- );

-- select * from types;
-- select * from pokemon;
-- insert into trainer(name, town) values ('brook', 'palet');
-- select * from trainer;
-- INSERT into pokemon_trainer(pokemon_id, trainer_name) values(3,'ash');

-- select * from pokemon_trainer;
-- DELETE FROM trainer WHERE name='fire';

-- select * from pokemon_trainer;
-- INSERT IGNORE into pokem(name) values('water');
-- select * from trainer; 

-- DELETE FROM pokemon;

-- select * from pokemon;
-- DELETE FROM trainer;

-- select * from pokemon_types;

-- Select * from pokemon where weight = (select MAX(weight) from pokemon);
-- select name from pokemon join pokemon_types on pokemon_types.pokemon_id=pokemon.id WHERE pokemon_types.type_name="grass";
-- 
-- select trainer_name from pokemon_trainer join pokemon on pokemon.id= pokemon_trainer.pokemon_id where pokemon.name="gengar";

-- select name from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id where pokemon_trainer.trainer_name='loga';

--     SELECT column, COUNT(*) AS magnitude 
-- FROM table 
-- GROUP BY column 
-- ORDER BY magnitude DESC
-- LIMIT 1

-- select name, COUNT(*) as val from pokemon join pokemon_trainer on pokemon_trainer.pokemon_id=pokemon.id GROUP BY pokemon.name ORDER by val DESC limit 2;

-- delete from pokemon_trainer as pt join pokemon on pokemon.id=pt.pokemon_id where pt.trainer_name='sabrina' and pokemon.name='lapras';

-- select * from types;

-- flying
-- steel
-- dark
-- unkonwn
-- shadow

-- select * from trainer where name="ash";

-- SELECT name FROM pokemon WHERE MAX(weight);
-- SELECT name FROM pokemon WHERE type='water';
-- SELECT trainer_name FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id = pt.pokemon_id AND p.name ='gengar';


-- select * from pokemon_trainer where trainer_name="ash"; 

select * from pokemon_types where pokemon_id=133; 