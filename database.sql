USE poketracker;
-- create database poketracker;

-- Create table pokemon(
--     id int Not null primary key,
--     name varchar(20),
--     height int,
--     weight int
-- );

-- create table trainer(
--     name varchar(20) not null primary key,
--     town varchar(20)
-- );

-- create table types(
--     name varchar(20) not null primary key
-- );

-- create table pokemon_types(
--     pokemon_id int not null,
--     type_name varchar(20) not null,
--     foreign key(pokemon_id) references pokemon(id),
--     foreign key(type_name) references types(name),
--     primary key (pokemon_id, type_name) 
-- );

-- create table pokemon_trainer(
--     trainer_name varchar(20) not null,
--     pokemon_id int not null,
--     foreign key(pokemon_id) references pokemon(id),
--     foreign key(trainer_name) references trainer(name),
--     primary key(trainer_name, pokemon_id) 

-- );

select * from pokemon_types;
-- select * from pokemon;
-- INSERT into pokemon_types(pokemon_id, type_name) values(1,'fire');

-- select * from types;
-- INSERT IGNORE into types(name) values('water');
-- SELECT * FROM pokemon_trainer
-- SELECT name FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id=pt.pokemon_id AND pt.trainer_name ="rano"
-- SELECT name,COUNT(pokemon_id) FROM pokemon AS p ,pokemon_trainer AS pt WHERE p.id=pt.pokemon_id GROUP BY name