create database if not exists  sistema_locadora_carros;
use sistema_locadora_carros;

create table if not exists veiculos(
placa varchar(8) primary key not null,
ano year not null,
modelo varchar(50) not null,
quant_km_rodados integer not null,
marca varchar(60) not null,
valor_diaria decimal(10,2) not null,
categoria_carro varchar(60) not null
);

create table if not exists funcionarios(
id_funcionario integer primary key not null  auto_increment,
nome_funcionario varchar(60) not null,
cargo_funcionario varchar(60) not null);

create table if not exists clientes(
cpf varchar(11) primary key not null,
rg varchar(15)  not null,
nome_completo varchar(150) not null,
telefone varchar(15) not null,
cnh varchar(11) not null
);


create table if not exists locacoes(
id_locacao integer primary key not null auto_increment,
cpf varchar(11)  not null,
placa varchar(8)   not null,
id_funcionario integer not null,
data_inicio_locacao datetime not null,
data_prevista_devolucao datetime not null,
data_devolucao_real datetime,
valor_diaria_aplicada decimal(10,2) not null,
valor_total decimal(10,2) not null,
foreign key (cpf) references clientes(cpf),
foreign key (id_funcionario) references funcionarios(id_funcionario),
foreign key (placa) references veiculos(placa)
);



