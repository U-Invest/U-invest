create table pg_curso (
    id_curso char(4) primary key,
    progresso_user number(3),
    ultimo_acesso date,
    u_coins number(5)
);

insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c001', 50, to_date('2022-01-01', 'YYYY-MM-DD'), 1000);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c002', 80, to_date('2022-02-14', 'YYYY-MM-DD'), 2500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c003', 10, to_date('2022-03-07', 'YYYY-MM-DD'), 500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c004', 25, to_date('2022-04-19', 'YYYY-MM-DD'), 1500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c005', 90, to_date('2022-05-23', 'YYYY-MM-DD'), 3500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c006', 75, to_date('2022-06-08', 'YYYY-MM-DD'), 2000);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c007', 40, to_date('2022-07-04', 'YYYY-MM-DD'), 800);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c008', 70, to_date('2022-08-12', 'YYYY-MM-DD'), 1800);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c009', 20, to_date('2022-09-20', 'YYYY-MM-DD'), 600);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins)
values ('c010', 100, to_date('2022-10-31', 'YYYY-MM-DD'), 5000);


create table usuario (
    cpf char(11) constraint us_cpf_pk primary key 
                 constraint us_cpf_nn not null,
    email varchar(50) not null,
    celular char(11) unique,
    nome varchar(50),
    saldo number(5),
    senha varchar(20) not null ,
    perfil_investidor varchar(20)
);
drop table usuario
desc usuario

insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('12345678901', 'joao@gmail.com', '99999999999', 'João Silva', 10000, 'senha123', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('23456789012', 'maria@hotmail.com', '88888888888', 'Maria Souza', 5000, 'abc123', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('34567890123', 'pedro@yahoo.com', '77777777777', 'Pedro Almeida', 20000, 'senha456', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('45678901234', 'ana@outlook.com', '66666666666', 'Ana Santos', 15000, 'senha789', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('56789012345', 'felipe@gmail.com', '55555555555', 'Felipe Costa', 8000, 'senhaabc', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('67890123456', 'lucas@hotmail.com', '44444444444', 'Lucas Oliveira', 12000, 'senha456', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('78901234567', 'carla@yahoo.com', '33333333333', 'Carla Lima', 7000, 'senha789', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('89012345678', 'vitoria@outlook.com', '22222222222', 'Vitória Pereira', 25000, 'senhaabc', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('90123456789', 'gustavo@gmail.com', '11111111111', 'Gustavo Martins', 18000, 'senha123', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('01234567890', 'marcos@hotmail.com', '00000000000', 'Marcos Santos', 9000, 'abc123', 'conservador');

create table curso (
    duracao number(2),
    avaliacao number(2),
    resumo varchar(250),
    nome_professor varchar(50),
    nome varchar(50),
    id_curso char(4) constraint curso_pk primary key
                    constraint curso_nn not null,
    recompensa number(3)
);
select * from curso
DELETE FROM curso;

insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (10, 8, 'aprenda os fundamentos do javascript', 'joão da silva', 'javascript básico', 'jsb1', 50); 1
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (15, 9, 'aprenda a construir websites', 'maria souza', 'html e css essencial', 'html', 75); 2
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (20, 7, 'aprenda a criar aplicações web dinâmicas com php', 'pedro oliveira', 'php para iniciantes', 'php', 100); 3
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (5, 10, 'aprenda a usar ferramentas de análise de dados com excel', 'ana santos', 'excel avançado', 'exa1', 150); 4
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (30, 8, 'aprenda a desenvolver aplicações móveis para android', 'rafael costa', 'android app development', 'aad1', 200); 5
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (25, 6, 'aprenda a programar em python para análise de dados', 'juliana fernandes', 'python para análise de dados', 'pyad', 125); 6
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (12, 9, 'aprenda a criar interfaces gráficas com javafx', 'lucas mendes', 'javafx para desenvolvedores', 'jfx1', 175); 7
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (8, 7, 'aprenda a criar jogos com a unity', 'felipe santos', 'desenvolvimento de jogos com unity', 'unit', 100); 8
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (18, 8, 'aprenda a usar o JS para criar aplicações web', 'gabriel almeida', 'JS para desenvolvedores web', 'JS', 150); 
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (7, 10, 'ferramentas de edição de vídeo, adobe premiere', 'paulo roberto', 'edição de vídeo com premiere', 'prm1', 75); 10

create table modulo (
    resumo varchar(100),
    id_modulo char(8) constraint mod_id_pk primary key,
    nome varchar(30)
);

select * from modulo
insert into modulo (resumo, id_modulo, nome)
values ('Introdução à programação', 'mod001', 'Programação básica');
insert into modulo (resumo, id_modulo, nome)
values ('Estrutura de dados', 'mod002', 'Estruturas de dados');
insert into modulo (resumo, id_modulo, nome)
values ('Desenvolvimento web', 'mod003', 'Front-end com HTML e CSS');
insert into modulo (resumo, id_modulo, nome)
values ('Lógica de programação', 'mod004', 'Lógica para iniciantes');
insert into modulo (resumo, id_modulo, nome)
values ('Banco de dados', 'mod005', 'MySQL e SQL Server');
insert into modulo (resumo, id_modulo, nome)
values ('Programação orientada a objetos', 'mod006', 'POO com Java');
insert into modulo (resumo, id_modulo, nome)
values ('Desenvolvimento mobile', 'mod007', 'Android Studio');
insert into modulo (resumo, id_modulo, nome)
values ('Programação funcional', 'mod008', 'JavaScript avançado');
insert into modulo (resumo, id_modulo, nome)
values ('Data Science', 'mod009', 'Introdução ao R');
insert into modulo (resumo, id_modulo, nome)
values ('Redes de computadores', 'mod010', 'Fundamentos de redes');

create table aula(
    tipo_contendo varchar(30),
    duracao date,
    nome_aula varchar(30),
    id_aula char(8) constraint aula_id_pk primary key,
    contudo char(20),
    avaliacao number(2)
);
desc aula
select * from aula
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', '2022-03-01', 'Introdução ao curso', 'aula001', 'Apresentação do curso', 90);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', '2022-03-02', 'História da programação', 'aula002', 'Breve história da programação', 85);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', '2022-03-03', 'Variáveis e tipos', 'aula003', 'Tipos de dados e variáveis em Python', 95);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', '2022-03-04', 'Operadores aritméticos', 'aula004', 'Explicação dos operadores aritméticos em C', 80);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', '2022-03-05', 'Funções em JavaScript', 'aula005', 'Como criar e usar funções em JavaScript', 90);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', '2022-03-06', 'Laços de repetição', 'aula006', 'Explicação sobre laços de repetição em Python', 75);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', '2022-03-07', 'Banco de dados relacional', 'aula007', 'Modelagem e criação de tabelas em MySQL', 85);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', '2022-03-08', 'Estruturas condicionais', 'aula008', 'Explicação sobre if-else em C', 70);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', '2022-03-09', 'POO em Java', 'aula009', 'Classes, objetos e herança em Java', 95);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', '2022-03-10', 'Manipulação de arquivos', 'aula010', 'Explicação sobre leitura e escrita de arquivos em Python', 80);

create table certificado
(nome_curso varchar(50),
nome_aluno varchar(50),
assinatura_plat char(20),
carga_horaria date,
dt_emissao date,
dt_conclusao date,
id_certificado char(8) constraint cert_id_pk primary key,
nome_professor char(30));

insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('Introdução à Programação', 'João da Silva', 'Digital Signature', '30h', TO_DATE('08/06/2022', 'DD/MM/YYYY'), TO_DATE('09/07/2022', 'DD/MM/YYYY'), 'cert001', 'Maria Souza');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('Python para Iniciantes', 'Ana Santos', 'CertSign', '40h', '2022-03-10', '2022-03-06', 'cert002', 'Paulo Oliveira');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('Desenvolvimento Web com JavaScript', 'Pedro Alves', 'GlobalSign', '60h', '2022-03-15', '2022-03-10', 'cert003', 'Lucas Souza');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('Algoritmos e Lógica de Programação', 'Maria Lima', 'DigiCert', '20h', '2022-03-20', '2022-03-15', 'cert004', 'José Santos');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('Java Avançado', 'Luiz Silva', 'Entrust Datacard', '80h', '2022-03-25', '2022-03-20', 'cert005', 'Roberto Oliveira');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('PHP Básico', 'Carla Santos', 'Comodo CA', '30h', '2022-04-01', '2022-03-27', 'cert006', 'Marcelo Souza');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('SQL para Iniciantes', 'Fernando Lima', 'Symantec', '20h', '2022-04-05', '2022-04-01', 'cert007', 'Paula Oliveira');
insert into certificado (nome_curso, nome_aluno, assinatura_plat, carga_horaria, dt_emissao, dt_conclusao, id_certificado, nome_professor)
values ('C++ Avançado', 'Gabriela Almeida', 'Thawte', '60h', '2022-04-10', '2022-04-05', 'cert008', 'Luciano Santos');

create table login (
    id_sessao char(8),
    hrs_plataforma number(6),
    nome_aula varchar(30),
    ultima_sessao date,
    hr_sessao_atual date
);
SELECT value FROM nls_session_parameters WHERE parameter = 'NLS_DATE_FORMAT';
SELECT value FROM nls_session_parameters WHERE parameter = 'NLS_TIME_FORMAT';

INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('12345678', 10, 'Introdução ao SQL', '10/03/23', '2022-02-28 15:30:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('87654321', 20, 'Operações com Tabelas', '14/04/23', '2022-03-01 09:45:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('45678901', 5, 'Funções de Agregação', '22/07/22', '2022-03-02 13:15:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('78901234', 12, 'Joins em SQL', '20/03/21', '2022-03-03 10:00:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('23456789', 8, 'Subconsultas', '06/03/21', '2022-03-04 14:20:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('34567890', 15, 'Indexação em SQL', '10/12/21', '2022-03-05 11:30:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('90123456', 7, 'Stored Procedures', '09/02/20', '2022-03-06 16:00:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('67890123', 18, 'Transações em SQL', '03/02/17', '2022-03-07 12:45:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('01234567', 3, 'Backup e Restore', '03/07/21', '2022-03-08 14:10:00');
INSERT INTO login (id_sessao, hrs_plataforma, nome_aula, ultima_sessao, hr_sessao_atual)
VALUES ('76543210', 22, 'Análise de Dados com SQL','07/12/2022','09:30:00');
dd
commit;
