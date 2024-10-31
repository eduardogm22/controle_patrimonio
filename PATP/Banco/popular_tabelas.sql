-- Populando tabelas

insert into categorias 
values 
(default, 'Notebook'),
(default, 'Cadeira'),
(default, 'Mesa'),
(default, 'Armário');

insert into situacoes
values
(default, 'Pronto para uso');

insert into info_notas
values
(default, 123123123, 1, 1, 1, '2024-10-27');

insert into setores_responsaveis
values
(default, 'Laboratório');

insert into estados
values
(default, 'Rio Grande do Sul', 'RS');

insert into cidades
values
(default, 'Passo Fundo', 1);

insert into enderecos
values
(default, 'Av Rui Barbosa', 'Petrópolis', 103, '99050-120', 1);

insert into fornecedores
values
(default, 'teste fornecedor', '12.123.123/0001-12', 1);

insert into cargos
values
(default, 'Desenvolvedor', 's', 's', 's','s','s','s');

insert into pessoas
values
(default, 'Eduardo Grosselli de Mello', 'edu_grosselli@hotmail.com', '2002-08-10', 1);

insert into usuarios
values
(1, 'eduardogm', '1234', 1);

call cadastra_quantidade('Notebook', 3000, current_date(), 1, 1, 1, 1, 1, 2);

call cadastra_quantidade('Cadeira', 150, current_date(), 1, 2, 1, 1, 1, 2);

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

