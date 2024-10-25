CREATE TABLE produtos (
 id_produto INTEGER PRIMARY KEY AUTO_INCREMENT,
 nome VARCHAR(100) NOT NULL,
 valor_unitario FLOAT NOT NULL,
 numero_patrimonio VARCHAR(30) UNIQUE,
 idinfo_nota INTEGER (FK),
 idcategoria INTEGER NOT NULL (FK),
 idsetor_responsavel INTEGER NOT NULL (FK),
 idsituacao INTEGER NOT NULL (FK),
 idfornecedor INTEGER NOT NULL (FK)


); 