CREATE DATABASE TODO_DB;--
create table if not exists users(

    id int primary key ,
    first_name varchar(255),
    last_name varchar(255),
    username varchar(255) unique ,
    password varchar(16),
    created_at timestamp default current_timestamp
);
--
create table if not exists categories(
    id serial primary key ,
    name varchar(255)
);
create table if not exists tasks(
    id serial primary key ,
    title   varchar(255),
    description text,
    uzunlik money,
    category_id serial references categories(id));
--ALTER TABLE table_name action; ---alter sintatksisi

alter table tasks rename column title to name; --column nomini o'zgartirish
alter table tasks  add unique   (description);--unique constraint qo'shish
alter table tasks alter column category_id type bigint; --constraint typeni o'zgartirish
ALTER TABLE users drop  constraint users_pkey;--constraintni o'chirish
alter table users alter column password set not null; --bor columnga constraint qo'shish


----                    DROP


DROP TABLE users;---jadvalni o'chirish
INSERT INTO tasks (id, name, description, category_id)
VALUES (1, 'qweqweqwe', 'adasd', 1);
truncate tasks;