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

-- INSERT into pokemon(id, name, height, weight) values(1, "charmer", 5,7);
-- INSERT into pokemon(id, name, height, weight) values(2, "charm", 5,4);
-- INSERT into pokemon(id, name, height, weight) values(3, "charme", 5,9);

-- INSERT into trainer(name, town) values('rano','bdkbs');
-- INSERT into trainer(name, town) values('ran','bds');
-- INSERT into trainer(name, town) values('ro','dkbs');

-- INSERT INTO pokemon_trainer(trainer_name,pokemon_id) VALUES("rano",1);
-- INSERT INTO pokemon_trainer(trainer_name,pokemon_id) VALUES("rano",2);
-- INSERT INTO pokemon_trainer(trainer_name,pokemon_id) VALUES("ran",1);
-- INSERT INTO pokemon_trainer(trainer_name,pokemon_id) VALUES("rano",3);

-- select * from pokemon_trainer;

-- SELECT trainer_name,pokemon_id,name,id 
SELECT trainer_name 
FROM pokemon AS p ,pokemon_trainer AS pt
WHERE p.id = pt.pokemon_id AND p.name = "charmer"
