create database if not exists  sistema_locadora_carros;
use sistema_locadora_carros;

create table if not exists veiculo(
id_carro int auto_increment primary key not null ,
placa varchar(8) unique key not null,
ano year not null,
modelo varchar(50) not null,
quant_km_rodados integer not null,
marca varchar(60) not null,
valor_diaria decimal(10,2) not null,
categoria_carro varchar(60) not null
);

create table if not exists funcionario(
id_funcionario integer primary key not null  auto_increment,
nome_funcionario varchar(60) not null,
cargo_funcionario varchar(60) not null);

create table if not exists cliente(
id_cliente int auto_increment primary key not null,
cpf varchar(11) unique not null,
rg varchar(15)  not null,
nome_completo varchar(150) not null,
telefone varchar(15) not null,
cnh varchar(11) unique not null
);


create table if not exists locacao(
id_locacao integer primary key not null auto_increment,
id_cliente int  not null,
id_carro int  not null,
id_funcionario integer not null,
data_inicio_locacao datetime not null,
data_prevista_devolucao datetime not null,
data_devolucao_real datetime,
valor_diaria_aplicada decimal(10,2) not null,
valor_total decimal(10,2) not null,
status_carro enum('reservada','em_andamento','finalizada','cancelada') not null,
foreign key (id_cliente) references cliente(id_cliente),
foreign key (id_funcionario) references funcionario(id_funcionario),
foreign key (id_carro) references veiculo(id_carro)
);



