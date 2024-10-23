#Procedure criada (como modelo) para cadastrar varios produtos diferentes com base na quantidade
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

call cadastra_varios(1, 'cadeira', 5);

#criando tables para chave estrangeira
create table categorias (
	idcategoria integer not null auto_increment primary key,
    nome varchar(100) not null unique
);

create table fornecedores (
	idfornecedor integer not null auto_increment primary key,
    nome varchar(30)
);

#alterando nomes do campo id, pois cada tabela precisa ter o seu próprio
alter table usuario
change id id_usuario integer not null auto_increment;

alter table produto
change id id_produto integer not null auto_increment;

#inserindo a chave estrangeira das tabelas categorias e fornecedores

#alterando o nome das colunas e mudando seus types pra integer
alter table produto
change categoria id_categoria integer not null;

alter table produto
change fornecedor id_fornecedor integer not null;

#adicionando a chave estrangeira nas tabelas
alter table produto
add constraint fk_prd_categorias foreign key (id_categoria) references categorias (id_categoria);

alter table produto
add constraint fk_prd_fornecedores foreign key (id_fornecedor) references fornecedores (id_fornecedor);

#criando tabela para fazer a auditoria(logs) da tabela produtos

create table produtos_audit(
	
);
