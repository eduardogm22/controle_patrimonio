use cadastro;

#Procedure criada (como modelo) para cadastrar varios produtos diferentes com base na quantidade
DELIMITER $$
CREATE PROCEDURE cadastra_varios (in nome varchar(100), in valor float, in quantidade integer)
BEGIN
	declare contador integer default 1;
    while contador <= quantidade do
		insert into teste_produtos (nome, valor) values (nome, valor);
		set contador = contador + 1;
	end while;
END $$
DELIMITER ;

#testando procedure
call cadastra_varios('cadeira', 50, 5);
#verificando se tudo ocorreu direito
select * from teste_produtos;
