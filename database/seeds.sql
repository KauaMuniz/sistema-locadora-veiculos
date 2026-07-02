use sistema_locadora_carros;

insert into veiculo
(
    placa,
    ano,
    modelo,
    quant_km_rodados,
    marca,
    valor_diaria,
    categoria_carro
)
values
(
    'BRA2C81',
     2007,
     'FIT',
     120000,
     'HONDA',
     100.00,
     'HATCH'
),

(
	'KTM4J56',
	 2012,
     'ONIX',
     110000,
     'CHEVROLET',
     150.00,
     'HATCH'
),

(
	'QWE8R19',
	 2021,
     'COROLLA',
     30000,
     'TOYOTA',
     250.00,
     'SEDAN'
),

(
	'LXP3M72',
	 2024,
     'COMPASS',
     25000,
     'JEEP',
     350.00,
     'SUV'

),

(
	'HGF6T45',
	 2023,
     'POLO',
     40000,
     'VOLKSWAGEN',
     150.00,
     'HATCH'	

);


insert into funcionario
(
	nome_funcionario,
    cargo_funcionario
)

values
(
	'Fernando',
    'Gerente'

),

(
  'Maria',
  'Vendedora'
),

(
	'Marcos',
    'Vendedor'
),

(
	'Rodrigo',
    'Vendedor'
),

( 	
	'Ana',
    'Vendedora'
);

insert into cliente
(
	cpf,
    rg,
    nome_completo,
    telefone,
    cnh
 )
 values
 
(
	'81745296310',
    '28.475.963-1',
    'João Carlos da Silva',
    '(11)98765-4321',
    '45871236901'
 ),

 (
	'29481657308',
    '51.720.384-6',
    'Maria Fernanda Oliveira',
    '(11)99874-2156',
    '93614582730'
 ),
 
(
	'63019548271',
    '69.318.427-5',
    'Pedro Henrique Santos',
    '(11)99123-7845',
    '27481956342'
 ),
 
(
	'75102836495',
    '40.851.739-2',
    'Ana Beatriz Costa',
    '(11)99658-3012',
    '58143697218'
 ),
 
(
	'48276391520',
    '73.196.254-8',
    'Lucas Gabriel Almeida',
    '(11)99471-8563',
    '71928463540'
 );
 
 insert into locacao(
	id_cliente,
    id_carro,
    id_funcionario,
    data_inicio_locacao,
    data_prevista_devolucao,
    data_devolucao_real,
    valor_diaria_aplicada,
    valor_total,
    status_locacao
 )
 
 values
(
	1,
    2,
    3,
    '2026-06-01 08:00:00',
    '2026-07-01 10:00:00',
    null,
    150.00,
    4500.00,
    'em_andamento'
 ),
(
	2,
    1,
    4,
    '2025-01-09 11:30:00',
    '2025-03-09 12:00:00',
    '2025-03-09 12:00:00',
    100.00,
    5900.00,
    'finalizada'
 ),
 (
	3,
    3,
    2,
    '2026-11-09 14:30:00',
    '2026-12-09 14:30:00',
    null,
    250.00,
    7500.00,
    'reservada'
 ),
(
	4,
    5,
    4,
    '2024-10-10 17:00:00',
    '2024-11-09 17:30:00',
    '2024-11-09 17:30:00',
    350.00,
    10500.00,
    'finalizada'
 ),
(
	5,
    4,
    5,
    '2026-03-01 17:00:00',
    '2026-03-21 17:30:00',
    '2026-03-21 17:30:00',
    150.00,
    3000.00,
    'finalizada'
 );
 

