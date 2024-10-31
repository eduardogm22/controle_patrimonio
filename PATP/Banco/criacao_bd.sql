drop database cadastro;
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

-- Inserção de Dados Utilizados para testes
INSERT INTO patrimonios (nome, valor_unitario, data_recebimento, num_patrimonio, num_serie, idnota, idcategoria, idsetor_responsavel, idsituacao)
VALUES
    ('Computador Dell', 3500.00, '2023-01-15', 'PATR001', 'SN001', 101, 1, 2, 1),
    ('Mesa de Escritório', 750.00, '2023-03-10', 'PATR002', 'SN002', 102, 2, 3, 1),
    ('Impressora HP LaserJet', 1200.00, '2022-11-05', 'PATR003', 'SN003', 103, 3, 4, 2),
    ('Projetor Epson', 2500.00, '2022-12-20', 'PATR004', 'SN004', 104, 4, 2, 1),
    ('Notebook Lenovo', 4000.00, '2023-05-07', 'PATR005', 'SN005', 105, 1, 5, 1),
    ('Cadeira Ergonômica', 450.00, '2023-04-02', 'PATR006', 'SN006', 106, 2, 3, 1),
    ('Telefone IP Cisco', 320.00, '2022-08-11', 'PATR007', 'SN007', 107, 3, 6, 2),
    ('Monitor Samsung', 800.00, '2023-01-18', 'PATR008', 'SN008', 108, 4, 2, 1),
    ('Roteador TP-Link', 250.00, '2023-02-22', 'PATR009', 'SN009', 109, 3, 7, 1),
    ('Estabilizador APC', 350.00, '2023-06-30', 'PATR010', 'SN010', 110, 4, 5, 2);
-- idcategoria, nome
select * from categorias;
INSERT INTO categorias (idcategoria, nome) VALUES
    (1, 'Equipamentos de Informática'),
    (2, 'Mobiliário'),
    (3, 'Acessórios'),
    (4, 'Periféricos'),
    (5, 'Rede');
-- idnota, chave_acesso, numero, serie, idfornecedor, data_aquisicao
select * from info_notas;
delete from info_notas;
INSERT INTO info_notas (idnota, chave_acesso, numero, serie, idfornecedor, data_aquisicao) VALUES
    (101, '123456', '001', 'Série A', 1, '2023-01-15'),
    (102, '234567', '002', 'Série B', 2, '2023-03-10'),
    (103, '345678', '003', 'Série C', 3, '2022-11-05'),
    (104, '456789', '004', 'Série D', 1, '2022-12-20'),
    (105, '567890', '005', 'Série E', 2, '2023-05-07');
-- idsituacao, nome
select * from situacoes;
INSERT INTO situacoes (idsituacao, nome) VALUES
    (1, 'Ativo'),
    (2, 'Inativo');
-- idcidade, nome, idestado
select * from cidades;
INSERT INTO cidades (idcidade, nome, idestado) VALUES
    (1, 'São Paulo', 1),
    (2, 'Rio de Janeiro', 2),
    (3, 'Belo Horizonte', 3),
    (4, 'Porto Alegre', 4),
    (5, 'Curitiba', 5);
-- idsetor_responsavel, nome
select * from setores_responsaveis;
INSERT INTO setores_responsaveis (idsetor_responsavel, nome) VALUES
    (1, 'TI'),
    (2, 'Administrativo'),
    (3, 'Financeiro'),
    (4, 'Compras'),
    (5, 'Vendas'),
    (6, 'Marketing');
-- Fim da inserção teste



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
-- drop procedure cadastra_quantidade;
delimiter $$
create procedure cadastra_quantidade (in nome varchar(100), in valor_unitario decimal(10, 2), in data_recebimento date, in idnota integer, in idcategoria integer, 
in idsetor_responsavel integer, in idsituacao integer, in idpatrimonio_numero integer, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
				insert into patrimonios (idpatrimonio, nome, valor_unitario, num_patrimonio, num_serie, data_recebimento, idnota, idcategoria, idsetor_responsavel, idsituacao)
				values
                (default, nome, valor_unitario, data_recebimento, null, null, idnota, idcategoria, idsetor_responsavel, idsituacao);
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

drop procedure st_pesquisar;

delimiter $$
create procedure st_pesquisar (in pesquisado varchar(30))
begin
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
left outer join situacoes as sit on ptr.idsituacao = sit.idsituacao
where ptr.nome like concat('%', pesquisado, '%') or ptr.idpatrimonio like concat('%', pesquisado, '%') or ptr.num_patrimonio like concat('%', pesquisado, '%');
end;
$$ delimiter ;
select * from categorias;

-- Teste
DELIMITER $$
CREATE PROCEDURE st_pesquisar(IN pesquisado VARCHAR(30))
BEGIN
    SELECT
        ptr.idpatrimonio AS "ID",
        ptr.nome AS "Patrimônio",
        cat.nome AS "Categoria",
        ptr.valor_unitario AS "Valor Unitário",
        ptr.num_patrimonio AS "Núm. Patrimônio",
        nta.data_aquisicao AS "Data de Aquisição",
        srp.nome AS "Setor Resp.",
        sit.nome AS "Situação"
    FROM
        patrimonios AS ptr
    INNER JOIN
        categorias AS cat ON ptr.idcategoria = cat.idcategoria
    LEFT OUTER JOIN
        info_notas AS nta ON ptr.idnota = nta.idnota
    LEFT OUTER JOIN
        setores_responsaveis AS srp ON ptr.idsetor_responsavel = srp.idsetor_responsavel
    LEFT OUTER JOIN
        situacoes AS sit ON ptr.idsituacao = sit.idsituacao
    WHERE
        ptr.nome LIKE CONCAT('%', pesquisado, '%')
        OR ptr.idpatrimonio LIKE CONCAT('%', pesquisado, '%')
        OR ptr.num_patrimonio LIKE CONCAT('%', pesquisado, '%');
END $$

DELIMITER ;
-- Final teste 1
-- Teste busca
CALL st_pesquisar('Computador Dell');


SELECT
    ptr.idpatrimonio AS "ID",
    ptr.nome AS "Patrimônio",
    cat.nome AS "Categoria",
    ptr.valor_unitario AS "Valor Unitário",
    ptr.num_patrimonio AS "Núm. Patrimônio",
    nta.data_aquisicao AS "Data de Aquisição",
    srp.nome AS "Setor Resp.",
    sit.nome AS "Situação"
FROM
    patrimonios AS ptr
INNER JOIN
    categorias AS cat ON ptr.idcategoria = cat.idcategoria
LEFT OUTER JOIN
    info_notas AS nta ON ptr.idnota = nta.idnota
LEFT OUTER JOIN
    setores_responsaveis AS srp ON ptr.idsetor_responsavel = srp.idsetor_responsavel
LEFT OUTER JOIN
    situacoes AS sit ON ptr.idsituacao = sit.idsituacao
WHERE
    ptr.nome LIKE CONCAT('%', 'Computador Dell', '%');




-- Teste 2
SELECT 
    ptr.idpatrimonio AS "ID",
    ptr.nome AS "Patrimônio",
    cat.nome AS "Categoria",
    ptr.valor_unitario AS "Valor Unitário",
    ptr.num_patrimonio AS "Núm. Patrimônio",
    nta.data_aquisicao AS "Data de Aquisição",
    srp.nome AS "Setor Resp.",
    sit.nome AS "Situação"
FROM
    patrimonios AS ptr
INNER JOIN
    categorias AS cat ON ptr.idcategoria = cat.idcategoria
LEFT OUTER JOIN
    info_notas AS nta ON ptr.idnota = nta.idnota
LEFT OUTER JOIN
    setores_responsaveis AS srp ON ptr.idsetor_responsavel = srp.idsetor_responsavel
LEFT OUTER JOIN
    situacoes AS sit ON ptr.idsituacao = sit.idsituacao
WHERE
    ptr.nome;
-- Final Teste 2







call st_pesquisar('');

select * from patrimonios;
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

-- triggers auditoria

select * from usuarios;
select * from cargos;
insert into cargos(nome,acesso_geral,pode_registrar,controle_adm,controle_usuario,pode_modificar,pode_visualizar) values ('Administrador',1,1,1,1,1,1);
insert into usuarios(usuario,senha,idcargo) values ('Luan',123,1);

select usuario,nome from usuarios as u inner join cargos as c where c.idcargo = u.idcargo;

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

select * from patrimonios;


select * from info_notas;
/*
set @idusuario = 444;

call cadastra_quantidade('verificando logs', 50, current_date(), 1, 1, 1, 1, 1, 2);

select * from patrimonios_audit; */
