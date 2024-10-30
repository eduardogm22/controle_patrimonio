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
