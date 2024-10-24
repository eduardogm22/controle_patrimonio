
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

#call cadastra_varios('cadeira', 50, 5);

select * from teste_produtos;

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
change id id_usuario integer auto_increment;

alter table produto
change id id_produto integer auto_increment;

alter table pessoas
change id id_pessoa integer auto_increment;

alter table cargo
change id id_cargo integer auto_increment;

#alterando o nome das colunas e mudando seus types pra integer
alter table produto
change categoria id_categoria integer not null;

alter table produto
change fornecedor id_fornecedor integer not null;

alter table pessoas
change cargo id_cargo integer not null default 2; ###verificar pois tem valores null

#adicionando a chave estrangeira nas tabelas
alter table produto
add constraint fk_prd_categorias foreign key (id_categoria) references categorias (id_categoria);

alter table produto
add constraint fk_prd_fornecedores foreign key (id_fornecedor) references fornecedores (id_fornecedor);

alter table pessoas
add constraint fk_pes_cargo foreign key (idcargo) references cargo (idcargo);

#criando tabela para fazer a auditoria(logs) da tabela produtos

#create table produtos_audit();

select * from teste_produtos;

select * from `pessoas`;

#1 administrador 7
#2 funcionario leitor
#3 funcionario controle
#4 supervisor