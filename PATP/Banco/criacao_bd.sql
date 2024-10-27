create database if not exists cadastro;
use cadastro;

create table produtos (
	idproduto integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario decimal(10,2) not null,
	numero_patrimonio varchar(30) unique,
	num_serie varchar(30) unique,
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null,
	idfornecedor integer not null
); 

create table categorias(
	idcategoria integer primary key auto_increment,
    nome varchar(30) not null unique
);

create table info_notas( 
 id_nota integer not null primary key auto_increment,  
 chave_acesso integer not null unique,  
 numero integer not null unique,  
 serie integer not null unique,  
 data_aquisicao date not null
); 

create table setores_responsaveis (
	idsetor_responsavel integer not null primary key auto_increment,
    nome varchar(30) not null
);

create table situacoes (
	idsituacao integer not null auto_increment primary key,
    nome varchar(30) not null
);

create table estados (
	idestado integer not null auto_increment primary key,
    nome varchar(20) not null unique,
    sigla char(2) not null unique
);

create table cidades (
	idcidade integer not null auto_increment primary key,
    nome varchar(50) not null,
    idestado integer not null,
    
    constraint fk_est_cidades foreign key (idestado) references estados (idestado)
);

create table enderecos_fornecedores (
	idendereco_fornecedor integer not null primary key,
    logradouro varchar(30),  
	numero varchar(10),  
	cep varchar(9),  
	idcidade integer 
    
);

create table fornecedores (
	idfornecedor integer not null auto_increment primary key,
    nome varchar(50) not null,
    idendereco_fornecedor integer not null,
    
    constraint id_fcd_enderecos_fornecedores foreign key (idendereco_fornecedor) references enderecos_fornecedores(idendereco_fornecedor)
);

create table enderecos_pessoas (
	idendereco_pessoa integer not null primary key,
    logradouro varchar(30),  
	numero_residencia varchar(10),  
	cep varchar(9),  
	idcidade integer 
);

create table pessoas ( 
	idpessoa integer not null auto_increment primary key,  
	nome varchar(30) not null,  
	email varchar(40),  
	data_nascimento date,  
	idendereco_pessoa integer,
    
    constraint fk_pes_endereco_pessoas foreign key (idendereco_pessoa) references enderecos_pessoas (idendereco_pessoa)
); 



create table cargos ( 
	idcargo int primary key auto_increment,  
	nome varchar(30) not null,  
	acesso_geral char(1) not null,  
	pode_registrar char(1) not null,  
	controle_adm char(1) not null,  
	controle_usuario char(1) not null,  
	pode_modificar char(1) not null,  
	pode_visualizar char(1) not null  
);

create table usuarios (
	idpessoa integer not null primary key,
	usuario varchar(30) not null unique,  
	senha varchar(20) not null,
	idcargo integer not null,
    
    constraint fk_usr_pessoas foreign key (idpessoa) references pessoas (idpessoa),
    constraint fk_usr_cargos foreign key (idcargo) references cargos (idcargo)
); 

-- stored procedures

-- procedure que recebe a quantidade e cadastra 1 produto para cada distinto vezes o valor da quantidade

/*delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor float, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
			insert into
				teste_produtos (idproduto, nome, valor_unitario)
                values 
				(default, nome, valor);
			set contador = contador + 1;
	end while;
end $$
delimiter ;

	idproduto integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario float not null,
	numero_patrimonio varchar(30) unique,
	num_serie varchar (30),
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null,
	idfornecedor integer not null

#testando procedure
call cadastra_varios('cadeira', 50, 5);
#verificando se tudo ocorreu direito
select * from teste_produtos;
*/

create database if not exists cadastro;
use cadastro;

create table produtos (
	idproduto integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario decimal(10,2) not null,
	numero_patrimonio varchar(30) unique,
	num_serie varchar(30) unique,
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null,
	idfornecedor integer not null
); 

create table categorias(
	idcategoria integer primary key auto_increment,
    nome varchar(30) not null unique
);

create table info_notas( 
 id_nota integer not null primary key auto_increment,  
 chave_acesso integer not null unique,  
 numero integer not null unique,  
 serie integer not null unique,  
 data_aquisicao date not null
); 

create table setores_responsaveis (
	idsetor_responsavel integer not null primary key auto_increment,
    nome varchar(30) not null
);

create table situacoes (
	idsituacao integer not null auto_increment primary key,
    nome varchar(30) not null
);

create table estados (
	idestado integer not null auto_increment primary key,
    nome varchar(20) not null unique,
    sigla char(2) not null unique
);

create table cidades (
	idcidade integer not null auto_increment primary key,
    nome varchar(50) not null,
    idestado integer not null,
    
    constraint fk_est_cidades foreign key (idestado) references estados (idestado)
);

create table fornecedores (
	idfornecedor integer not null auto_increment primary key,
    nome varchar(50) not null,
    idcidade integer not null,
    
    constraint id_fcd_cidades foreign key (idcidade) references cidades(idcidade)
);

create table pessoas ( 
	idpessoa integer not null auto_increment primary key,  
	nome varchar(30) not null,  
	email varchar(40),  
	data_nascimento date,  
	logradouro varchar(30),  
	numero_residencia varchar(10),  
	cep varchar(9),  
	idcidade integer  
); 

create table cargos ( 
	idcargo int primary key auto_increment,  
	nome varchar(30) not null,  
	acesso_geral char(1) not null,  
	pode_registrar char(1) not null,  
	controle_adm char(1) not null,  
	controle_usuario char(1) not null,  
	pode_modificar char(1) not null,  
	pode_visualizar char(1) not null  
);

create table usuarios ( 
	idusuario integer not null auto_increment primary key,  
	usuario varchar(30) not null unique,  
	senha varchar(20) not null,
    idpessoa integer not null,  
	idcargo integer not null,
    
    constraint fk_usr_pessoas foreign key (idpessoa) references pessoas (idpessoa),
    constraint fk_usr_cargos foreign key (idcargo) references cargos (idcargo)
); 

-- stored procedures

-- procedure que recebe a quantidade e cadastra 1 produto para cada distinto vezes o valor da quantidade

delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor float, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
			insert into
				teste_produtos (idproduto, nome, valor_unitario)
                values 
				(default, nome, valor);
			set contador = contador + 1;
	end while;
end $$
delimiter ;

	idproduto integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario float not null,
	numero_patrimonio varchar(30) unique,
	num_serie varchar (30),
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null,
	idfornecedor integer not null

#testando procedure
call cadastra_varios('cadeira', 50, 5);
#verificando se tudo ocorreu direito
select * from teste_produtos;
