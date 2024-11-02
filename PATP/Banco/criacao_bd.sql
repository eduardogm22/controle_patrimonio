create database if not exists cadastro;
use cadastro;

-- criando as tabelas 

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

create table patrimonios (
	idpatrimonio integer not null auto_increment primary key,
	nome varchar(100) not null,
	valor_unitario decimal(10,2) not null,
    data_recebimento date,
    num_patrimonio varchar(30),
    num_serie varchar(30),
	idnota integer,
	idcategoria integer not null,
    idsetor_responsavel integer not null,
	idsituacao integer not null,
    
    constraint fk_ptr_info_notas foreign key (idnota) references info_notas (idnota),
    constraint fk_ptr_categorias foreign key (idcategoria) references categorias (idcategoria),
    constraint fk_ptr_setores_responsaveis foreign key (idsetor_responsavel) references setores_responsaveis (idsetor_responsavel),
    constraint fk_ptr_situacoes foreign key (idsituacao) references situacoes (idsituacao)
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

-- Criação tabela auditoria para verificar logs
-- drop table patrimonios_audit;
create table patrimonios_audit (
    idusuario integer,
    tipo_alteracao varchar(10),
    data_alteracao timestamp,
    idpatrimonio integer not null,
	nome varchar(100) default null,
	valor_unitario decimal(10,2) default null,
    data_recebimento date default null,
    num_patrimonio varchar(30) default null,
    num_serie varchar(30) default null,
	idnota integer default null,
	idcategoria integer default null,
    idsetor_responsavel integer default null,
	idsituacao integer default null   
);

-- stored procedures

-- procedure que recebe a quantidade e cadastra 1 produto para cada distinto vezes o valor da quantidade
 -- drop procedure cadastra_quantidade;
delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor_unitario decimal(10, 2), in data_recebimento date, in idnota integer, in idcategoria integer, 
in idsetor_responsavel integer, in idsituacao integer, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
				insert into patrimonios (idpatrimonio, nome, valor_unitario, num_patrimonio, num_serie, data_recebimento, idnota, idcategoria, idsetor_responsavel, idsituacao)
				values
                (default, nome, valor_unitario, null, null, data_recebimento, idnota, idcategoria, idsetor_responsavel, idsituacao);
			set contador = contador + 1;
	end while;
end 
$$ delimiter ;

-- procedure que faz o cadastro das notas
delimiter $$
create procedure cadastra_nota(in chave_acesso integer, in numero integer, in serie integer, in data_aquisicao date)
begin
	insert into info_notas (chave_acesso, numero, serie, idfornecedor, data_aquisicao)
    values
    (chave_acesso, numero, serie, idfornecedor, data_aquisicao);
end
$$ delimiter ;

-- views 

-- drop view usuario_nome_view; -- descomentar caso fizer alteração
create view usuario_nome_view as
SELECT 
	usr.idpessoa, 
	usr.usuario, 
    pss.nome 
FROM 
	usuarios as usr
inner join 
	pessoas as pss on usr.idpessoa = pss.idpessoa;

-- drop view principal_patrimonio_view; -- descomentar caso fizer alteração
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

-- drop procedure st_pesquisar; descomentar caso fizer alteração
delimiter $$
create procedure st_pesquisar (in pesquisado varchar(30))
begin
select
    ptr.nome as "Patrimônio",
    cat.nome as "Categoria",
    ptr.valor_unitario as "Valor Unitário",
    ptr.data_recebimento as "Data Receb.",
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
left outer join situacoes as sit on ptr.idsituacao = sit.idsituacao
where ptr.nome like concat('%', pesquisado, '%') or cat.nome like concat('%', pesquisado, '%') or srp.nome like concat('%', pesquisado, '%');
end;
$$ delimiter ;

-- triggers auditoria

delimiter $$
create trigger patrimonios_trigger_insert 
after insert on patrimonios 
for each row
begin
	insert into patrimonios_audit (idusuario, tipo_alteracao, data_alteracao, idpatrimonio)
	values
	(@idusuario, 'insert', current_date(), 1);
end $$
delimiter ;
