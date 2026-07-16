use sistema_locadora_carros;

-- Mostrar todos os valores das tabelas
select * from veiculo;
select * from funcionario;
select * from cliente;
select * from locacao;

-- Mostrar os valores com filtros 
select * from veiculo
where valor_diaria < 200;

select * from funcionario
where id_funcionario = 2;

select * from cliente
where nome_completo like '%Carlos%';

select * from locacao
where data_devolucao_real < '2026-01-01';

select * from veiculo order by marca asc;

select categoria_carro, count(*) as quantidade_categoria from veiculo 
group by categoria_carro;

select status_locacao, sum(valor_total) as caixa from locacao
group by status_locacao;

select avg(valor_diaria) as valor_medio_diarias from veiculo;

select status_locacao, count(*) as quantidade from locacao 
group by status_locacao;

-- INNER JOIN completo
select
    locacao.id_locacao,
    cliente.nome_completo,
    veiculo.modelo,
    veiculo.placa,
    funcionario.nome_funcionario,
    locacao.data_inicio_locacao,
    locacao.data_prevista_devolucao,
    locacao.valor_total,
    locacao.status_locacao
from locacao
inner join cliente on locacao.id_cliente = cliente.id_cliente
inner join veiculo on locacao.id_carro = veiculo.id_carro
inner join funcionario on locacao.id_funcionario = funcionario.id_funcionario;

-- INNER JOIN filtrando locacoes em andamento
select
    locacao.id_locacao,
    cliente.nome_completo,
    veiculo.modelo,
    veiculo.placa,
    funcionario.nome_funcionario,
    locacao.data_inicio_locacao,
    locacao.data_prevista_devolucao,
    locacao.valor_total,
    locacao.status_locacao
from locacao
inner join cliente on locacao.id_cliente = cliente.id_cliente
inner join veiculo on locacao.id_carro = veiculo.id_carro
inner join funcionario on locacao.id_funcionario = funcionario.id_funcionario
where status_locacao = 'em_andamento';

-- Dias previstos por locacao
select
    locacao.id_locacao,
    cliente.nome_completo,
    veiculo.modelo,
    datediff(data_prevista_devolucao, data_inicio_locacao) as dias_previstos
from locacao
inner join cliente on locacao.id_cliente = cliente.id_cliente
inner join veiculo on locacao.id_carro = veiculo.id_carro;