CREATE DATABASE IF NOT EXISTS cadastro;
USE cadastro;

create table produtos (
	idproduto INTEGER not null AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL,
	numero_patrimonio VARCHAR(30) UNIQUE,
	num_serie varchar (30),
	idnota INTEGER,
	idcategoria INTEGER NOT NULL,
    idsetor_responsavel INTEGER NOT NULL,
	idsituacao INTEGER NOT NULL,
	idfornecedor INTEGER NOT NULL
); 

CREATE TABLE categorias(
	idcategoria integer primary key auto_increment,
    nome varchar(30) not null unique
);

CREATE TABLE info_notas( 
 id_nota INTEGER not null PRIMARY KEY AUTO_INCREMENT,  
 chave_acesso integer not null unique,  
 numero integer not null unique,  
 serie integer not null unique,  
 data_aquisicao DATE NOT NULL
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

CREATE TABLE pessoas ( 
	idpessoa integer not null auto_increment primary key,  
	nome varchar(30) not null,  
	email varchar(40),  
	data_nascimento date,  
	logradouro varchar(30),  
	numero_residencia varchar(10),  
	cep VARCHAR(9),  
	idcidade integer  
); 

CREATE TABLE cargos ( 
	idcargo INT PRIMARY KEY AUTO_INCREMENT,  
	nome VARCHAR(30) NOT NULL,  
	acesso_geral CHAR(1) NOT NULL,  
	pode_registrar CHAR(1) NOT NULL,  
	controle_adm CHAR(1) NOT NULL,  
	controle_usuario CHAR(1) NOT NULL,  
	pode_modificar CHAR(1) NOT NULL,  
	pode_visualizar CHAR(1) NOT NULL  
);

CREATE TABLE usuarios ( 
	idusuario integer not null auto_increment primary key,  
	usuario VARCHAR(30) not null unique,  
	senha VARCHAR(20) NOT NULL,
    idpessoa INTeger not null,  
	idcargo INTEGER NOT NULL,
    
    constraint fk_usr_pessoas foreign key (idpessoa) references pessoas (idpessoa),
    constraint fk_usr_cargos foreign key (idcargo) references cargos (idcargo)
); 
