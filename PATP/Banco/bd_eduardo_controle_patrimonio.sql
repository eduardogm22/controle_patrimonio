
DELIMITER $$
CREATE PROCEDURE cadastra_varios (in id integer, in nome varchar(30), in quantidade integer)
BEGIN
	declare contador integer default 1;
    while contador <= quantidade do
		insert into teste values (id, nome);
		set contador = contador + 1;
	end while;
END $$
DELIMITER ;

create database teste;

create table teste (
	id integer not null,
    nome varchar(30)
);

call cadastra_varios(1, 'Eduardo', 3);

select * from teste;

truncate table teste;