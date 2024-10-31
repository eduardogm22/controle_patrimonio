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
