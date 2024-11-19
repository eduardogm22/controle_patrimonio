call cadastra_nota(999999, 123, 123, 1, '2024-10-10', @nota_sel_id);
select @nota_sel_id;
call cadastra_quantidade ('verificando logs', 20, '2024-10-10', 1, 1, 
1, 1, 1);

-- executar isso
alter table info_notas
drop index chave_acesso;

alter table info_notas
drop index numero;

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


#testando cadastro pela procedure

create table patrimonios_teste (
	idpatrimonio integer auto_increment primary key,
	nome varchar(100),
	valor_unitario decimal(10,2),
    data_recebimento date,
    num_patrimonio varchar(30),
    num_serie varchar(30),
	idnota integer,
	idcategoria integer,
    idsetor_responsavel integer,
	idsituacao integer
);
drop procedure cadastra_quantidade_teste;
delimiter $$
create procedure cadastra_quantidade_teste (in nome varchar(100), in valor_unitario decimal(10, 2), in categoria integer, in quantidade integer)
begin
	declare contador integer default 1;
    while 
		contador <= quantidade do
				insert into patrimonios_teste (idpatrimonio, nome, valor_unitario, num_patrimonio, num_serie, data_recebimento, idnota, idcategoria, idsetor_responsavel, idsituacao)
				values
                (default, nome, valor_unitario, null, null, current_date(), null, categoria, null, null);
			set contador = contador + 1;
	end while;
end 
$$ delimiter ;

call cadastra_quantidade_teste('testecat1', 50, 1, 1);
select * from patrimonios_teste;
