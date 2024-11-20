insert into categorias 
values 
(default, 'Notebook'),
(default, 'Cadeira'),
(default, 'Mesa'),
(default, 'Armário'),
(default, 'Equipamentos de Informática'),
(default, 'Mobiliário'),
(default, 'Acessórios'),
(default, 'Periféricos'),
(default, 'Rede');

insert into situacoes
values
(default, 'Armazenado'),
(default, 'Ativo'),
(default, 'Inativo');

insert into setores_responsaveis
values
(default, 'Laboratório'),
(default, 'TI'),
(default, 'Administrativo'),
(default, 'Financeiro'),
(default, 'Compras'),
(default, 'Vendas'),
(default, 'Marketing');

insert into fornecedores (nome, cnpj)
values
('Faculdades Ideau', '17.590.477/0001-77'),
('Deltasul', '98.102.924/0001-01');

INSERT INTO info_notas (idnota, chave_acesso, numero, serie, idfornecedor, data_aquisicao) VALUES
    (default, '123456', '001', 1, 1, '2023-01-15'),
    (default, '234567', '002', 1, 2, '2023-03-10'),
    (default, '345678', '003', 1, 3, '2022-11-05'),
    (default, '456789', '004', 1, 1, '2022-12-20'),
    (default, '567890', '005', 1, 2, '2023-05-07');

insert into cargos
values
(default, 'Admin', '1', '1', '1','1','1','1'),
(default, 'Supervisor', '0', '1', '1','1','1','1'),
(default, 'Funcionario Registrador', '0', '1', '0','0','1','1'),
(default, 'Funcionario Leitor', '0', '0', '0','0','0','1');


insert into pessoas
values
(default, 'Eduardo Grosselli de Mello', 'edu_grosselli@hotmail.com', '2002-08-10', 1),
(default, 'Emilly Levandoscki', 'emylevandoscki@gmail.com', '2002-11-15', 1),
(default, 'Luan da Luz', 'luanluz@gmail.com', '2002-10-20', 1);

insert into usuarios
values
(1, 'eduardogm', '1234', 1),
(2, 'emillylv', 1234, 1),
(3, 'luanlz', 1234, 1); 
   
INSERT INTO patrimonios (nome, valor_unitario, data_recebimento, num_patrimonio, num_serie, idnota, idcategoria, idsetor_responsavel, idsituacao)
VALUES
    ('Computador Dell', 3500.00, '2023-01-15', 'PATR001', 'SN001', 1, 1, 2, 1),
    ('Mesa de Escritório', 750.00, '2023-03-10', 'PATR002', 'SN002', 2, 2, 3, 1),
    ('Impressora HP LaserJet', 1200.00, '2022-11-05', 'PATR003', 'SN003', 3, 3, 4, 2),
    ('Projetor Epson', 2500.00, '2022-12-20', 'PATR004', 'SN004', 4, 4, 2, 1),
    ('Notebook Lenovo', 4000.00, '2023-05-07', 'PATR005', 'SN005', 5, 1, 5, 1),
    ('Cadeira Ergonômica', 450.00, '2023-04-02', 'PATR006', 'SN006', 1, 2, 3, 1),
    ('Telefone IP Cisco', 320.00, '2022-08-11', 'PATR007', 'SN007', 2, 3, 6, 2),
    ('Monitor Samsung', 800.00, '2023-01-18', 'PATR008', 'SN008', 3, 4, 2, 1),
    ('Roteador TP-Link', 250.00, '2023-02-22', 'PATR009', 'SN009', 4, 3, 7, 1),
    ('Estabilizador APC', 350.00, '2023-06-30', 'PATR010', 'SN010', 5, 4, 5, 2);
    
-- Fim da inserção 

