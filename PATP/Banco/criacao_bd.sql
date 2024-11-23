
create database if not exists asset_ctrl;
use asset_ctrl;

-- criando as tabelas 

create table categorias(
	idcategoria integer primary key auto_increment,
    nome varchar(30) not null unique
);

create table info_notas( 
	idnota integer not null primary key auto_increment,  
	chave_acesso varchar(44) not null unique,  
	numero integer not null,  
	serie integer not null,
    idfornecedor integer not null,
	data_aquisicao date not null
); 

create table setores_responsaveis (
	idsetor integer not null primary key auto_increment,
    nome varchar(30) not null
);

create table locais(
	idlocal integer primary key auto_increment,
    nome varchar(255)
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
    idsetor integer not null,
    idlocal integer,
	idsituacao integer not null,
    
    constraint fk_ptr_info_notas foreign key (idnota) references info_notas (idnota),
    constraint fk_ptr_categorias foreign key (idcategoria) references categorias (idcategoria),
    constraint fk_ptr_setores_responsaveis foreign key (idsetor) references setores_responsaveis (idsetor),
    constraint fk_ptr_locais foreign key (idlocal) references locais (idlocal),
    constraint fk_ptr_situacoes foreign key (idsituacao) references situacoes (idsituacao)
);

create table fornecedores (
	idfornecedor integer not null auto_increment primary key,
    nome varchar(50) not null,
    cnpj varchar(18)
);

create table pessoas ( 
	idpessoa integer not null auto_increment primary key,  
	nome varchar(30) not null,  
	email varchar(40),  
	dt_create date  
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
	idpessoa integer not null primary key auto_increment,
	usuario varchar(30) not null unique,  
	senha varchar(20) not null,
	idcargo integer not null,
    
    constraint fk_usr_pessoas foreign key (idpessoa) references pessoas (idpessoa),
    constraint fk_usr_cargos foreign key (idcargo) references cargos (idcargo)
); 

-- stored procedures

-- procedure que recebe a quantidade e cadastra 1 produto para cada distinto vezes o valor da quantidade
 -- drop procedure cadastra_quantidade;
delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor_unitario decimal(10, 2), in data_recebimento date, in idnota integer, in idcategoria integer, 
in idsetor integer, in idlocal integer, in idsituacao integer, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
				insert into patrimonios (idpatrimonio, nome, valor_unitario, num_patrimonio, num_serie, data_recebimento, idnota, idcategoria, idsetor, idlocal, idsituacao)
				values
                (default, nome, valor_unitario, null, null, data_recebimento, idnota, idcategoria, idsetor, idlocal, idsituacao);
			set contador = contador + 1;
	end while;
end 
$$ delimiter ;

-- procedure que faz o cadastro das notas
-- drop procedure cadastra_nota;
delimiter $$
create procedure cadastra_nota(in e_chave_acesso varchar(44), in e_numero integer, in e_serie integer, in e_idfornecedor integer,in e_data_aquisicao date, out s_idnota integer)    
begin
	set @s_idnota = null;
    
	select idnota 
	into s_idnota 
	from info_notas 
    where 
		chave_acesso = e_chave_acesso;
    
    if s_idnota is null then
		insert into info_notas (chave_acesso, numero, serie, idfornecedor, data_aquisicao)
        values
        (e_chave_acesso, e_numero, e_serie, e_idfornecedor, e_data_aquisicao);
        
        set @s_idnota = last_insert_id();
    end if;
end
$$ delimiter ;

-- views 

-- drop procedure st_select_editar;

delimiter $$
create procedure st_select_editar (in idpatrimonio_in integer)
begin
select 
	nts.chave_acesso, 
	fcd.nome as "Fornecedor", 
    ptr.num_serie, 
    ptr.num_patrimonio, 
    nts.data_aquisicao,
    ptr.data_recebimento, 
    lcl.nome as "local", 
    ptr.nome, 
    ptr.valor_unitario, 
    sit.nome as "situação", 
    srp.nome as "setor", 
    ctr.nome as "categoria"
from 
	patrimonios as ptr
left outer join
	info_notas as nts on ptr.idnota = nts.idnota
left outer join
	fornecedores as fcd on nts.idfornecedor = fcd.idfornecedor
left outer join
	situacoes as sit on ptr.idsituacao = sit.idsituacao
left outer join
	setores_responsaveis as srp on ptr.idsetor = srp.idsetor
left outer join
	categorias as ctr on ptr.idcategoria = ctr.idcategoria
left outer join
	locais as lcl on ptr.idlocal = lcl.idlocal
where 
	idpatrimonio = idpatrimonio_in;
end;
$$ delimiter;

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
	setores_responsaveis as srp on ptr.idsetor = srp.idsetor
left outer join situacoes as sit on ptr.idsituacao = sit.idsituacao;

-- drop procedure st_pesquisar; descomentar caso fizer alteração
delimiter $$
create procedure st_pesquisar (in pesquisado varchar(30))
begin
select
	ptr.idpatrimonio as "ID",
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
	setores_responsaveis as srp on ptr.idsetor = srp.idsetor
left outer join situacoes as sit on ptr.idsituacao = sit.idsituacao
where ptr.nome like concat('%', pesquisado, '%') or cat.nome like concat('%', pesquisado, '%') or srp.nome like concat('%', pesquisado, '%');
end;
$$ delimiter ;

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
    idsetor integer default null,
    idlocal integer default null,
	idsituacao integer default null   
);

-- triggers auditoria

delimiter $$
create trigger patrimonios_trigger_insert 
after insert on patrimonios 
for each row
begin
	insert into patrimonios_audit (idusuario, tipo_alteracao, data_alteracao, idpatrimonio)
	values
	(@idusuario, 'insert', current_timestamp(), new.idpatrimonio);
end $$
delimiter ;

delimiter $$
create trigger patrimonios_trigger_update 
after update on patrimonios 
for each row
begin
	insert into patrimonios_audit (idusuario, tipo_alteracao, data_alteracao, idpatrimonio, nome, valor_unitario, data_recebimento, num_patrimonio, num_serie, idnota, idcategoria, idsetor, idlocal, idsituacao)
	values
	(@idusuario, 'update', current_timestamp(), old.idpatrimonio, old.nome, old.valor_unitario, old.data_recebimento, old.num_patrimonio, old.num_serie, old.idnota, old.idcategoria, old.idsetor, old.idlocal, old.idsituacao);
end $$
delimiter ;

delimiter $$
create trigger patrimonios_trigger_delete
before delete on patrimonios 
for each row
begin
	insert into patrimonios_audit (idusuario, tipo_alteracao, data_alteracao, idpatrimonio, nome, valor_unitario, data_recebimento, num_patrimonio, num_serie, idnota, idcategoria, idsetor, idlocal, idsituacao)
	values
	(@idusuario, 'delete', current_timestamp(), old.idpatrimonio, old.nome, old.valor_unitario, old.data_recebimento, old.num_patrimonio, old.num_serie, old.idnota, old.idcategoria, old.idsetor, old.idlocal, old.idsituacao);
end $$
delimiter ;