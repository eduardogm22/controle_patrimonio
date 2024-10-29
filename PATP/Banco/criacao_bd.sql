create database if not exists cadastro;
use cadastro;

-- criando as tabelas

create table patrimonios (
	idpatrimonio integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario decimal(10,2) not null,
	num_patrimonio varchar(30) unique,
	num_serie varchar(30) unique,
    data_recebimento date,
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null
); 

create table categorias(
	idcategoria integer primary key auto_increment,
    nome varchar(30) not null unique
);

create table info_notas( 
	idnota integer not null primary key auto_increment,  
	chave_acesso integer not null unique,  
	numero integer not null unique,  
	serie integer not null,
    idfornecedor integer not null,
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

create table enderecos (
	idendereco integer not null auto_increment primary key,
    logradouro varchar(30),
    bairro varchar(40),
	numero varchar(10),  
	cep varchar(9),  
	idcidade integer 
    
);

create table fornecedores (
	idfornecedor integer not null auto_increment primary key,
    nome varchar(50) not null,
    cnpj varchar(18),
    idendereco integer,
    
    constraint id_fcd_enderecos foreign key (idendereco) references enderecos(idendereco)
);

create table pessoas ( 
	idpessoa integer not null auto_increment primary key,  
	nome varchar(30) not null,  
	email varchar(40),  
	data_nascimento date,  
	idendereco integer,
    
    constraint fk_pes_endereco foreign key (idendereco) references enderecos (idendereco)
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

delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor_unitario decimal(10, 2), in num_patrimonio varchar(30), in num_serie varchar(30), 
in idnota integer, in idcategoria integer, in idsetor_responsavel integer, in idsituacao integer, in idfornecedor integer, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
			insert into
				patrimonios (nome, valor_unitario, num_patrimonio, num_serie, idnota, idcategoria, idsetor_responsavel, idsituacao, idfornecedor)
                values 
				(nome, valor_unitario, num_patrimonio, num_serie, idnota, idcategoria, idsetor_responsavel, idsituacao, idfornecedor);
			set contador = contador + 1;
	end while;
end 
$$ delimiter ;

-- procedure que faz o cadastro das notas
delimiter $$
create procedure cadastra_nota(in chave_acesso integer, in numero integer, in serie integer, in data_aquisicao date)
begin
	insert into info_notas (chave_acesso, numero, serie, data_aquisicao)
    values
    (chave_acesso, numero, serie, data_aquisicao);
end
$$ delimiter ;

-- views

create view usuario_nome_view as
SELECT 
	usr.idpessoa, 
	usr.usuario, 
    pss.nome 
FROM 
	usuarios as usr
inner join 
	pessoas as pss on usr.idpessoa = pss.idpessoa;

create view principal_patrimonio_view as
select
	ptr.idpatrimonio as "ID",
    ptr.nome as "Patrimônio",
    cat.nome as "Categoria",
    ptr.valor_unitario as "Valor Unitário",
    ptr.num_patrimonio as "Núm. Patrimônio",
    nta.data_aquisicao as "Data de Aquisição",
    srp.nome as "Setor Resp.",
    sit.nome as "Situação"
from
	patrimonios as ptr
inner join
	categorias as cat on ptr.idcategoria = cat.idcategoria
left outer join
	info_notas as nta on ptr.idnota = nta.idnota
left outer join
	setores_responsaveis as srp on ptr.idsetor_responsavel = srp.idsetor_responsavel
left outer join situacoes as sit on ptr.idsituacao = sit.idsituacao;

-- Criação tabela auditoria para verificar logs

create table patrimonios_audit (
    idusuario integer,
    tipo_alteracao varchar(10),
    data_alteracao timestamp,
    idpatrimonio integer,
	nome varchar(100),
	valor_unitario decimal(10,2),
	num_patrimonio varchar(30),
	num_serie varchar(30),
	idnota integer,
	idcategoria integer,
    idsetor_responsavel integer,
	idsituacao integer,
	idfornecedor integer    
);

-- triggers auditoria

DELIMITER $$
create trigger patrimonios_trigger_insert 
before insert on patrimonios 
for each row 
begin
	insert into patrimonios_audit (idusuario, tipo_alteracao, data_alteracao, idpatrimonio, nome, valor_unitario, num_patrimonio, num_serie, idnota, idcategoria, idsetor_responsavel, idsituacao, idfornecedor)
    values
    (@idusuario,'insert', now(), new.idpatrimonio, new.nome, new.valor_unitario, new.num_patrimonio, new.num_serie, new.idnota, new.idcategoria, new.idsetor_responsavel, new.idsituacao, new.idfornecedor);
end;
DELIMITER $$;
