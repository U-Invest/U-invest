create table pg_curso
(id_curso char(8) constraint pg_id_pk primary key,
progresso_user number(3),
ultimo_acesso data,
u_coins number(5));

insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c001', 50, '2022-01-01', 1000);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c002', 80, '2022-02-14', 2500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c003', 10, '2022-03-07', 500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c004', 25, '2022-04-19', 1500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c005', 90, '2022-05-23', 3500);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c006', 75, '2022-06-08', 2000);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c007', 40, '2022-07-04', 800);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c008', 70, '2022-08-12', 1800);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c009', 20, '2022-09-20', 600);
insert into pg_curso (id_curso, progresso_user, ultimo_acesso, u_coins) values ('c010', 100, '2022-10-31', 5000);

// relacionamento entre pg_curso e usuario 
CREATE TABLE possui (                     
    fk_usuario_cpf CHAR(11),
    fk_pg_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf),
    FOREIGN KEY (fk_pg_curso_id_curso) REFERENCES pg_curso(id_curso)
);

INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('12345678910', 'c001');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('23456789012', 'c002');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('34567890123', 'c003');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('45678901234', 'c004');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('56789012345', 'c005');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('67890123456', 'c006');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('78901234567', 'c007');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('89012345678', 'c008');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('90123456789', 'c009');
INSERT INTO possui (fk_usuario_cpf, fk_pg_curso_id_curso) VALUES ('01234567890', 'c010');

CREATE TABLE usuario (
    cpf CHAR(11) CONSTRAINT us_cpf_pk PRIMARY KEY NOT NULL,
    email VARCHAR(50) NOT NULL,
    celular CHAR(11) UNIQUE NOT NULL,
    nome VARCHAR(50) NOT NULL,
    saldo NUMBER(5) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    perfil_investidor VARCHAR(20) NOT NULL
);

insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('12345678910', 'joao@gmail.com', '99999999999', 'João Silva', 10000, 'senha123', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('23456789012', 'maria@hotmail.com', '88888888888', 'Maria Souza', 5000, 'abc123', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('34567890123', 'pedro@yahoo.com', '77777777777', 'Pedro Almeida', 20000, 'senha456', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('45678901234', 'ana@outlook.com', '66666666666', 'Ana Santos', 15000, 'senha789', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('56789012345', 'felipe@gmail.com', '55555555555', 'Felipe Costa', 8000, 'senhaabc', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('67890123456', 'lucas@hotmail.com', '44444444444', 'Lucas Oliveira', 12000, 'senha456', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('78901234567', 'carla@yahoo.com', '33333333333', 'Carla Lima', 7000, 'senha789', 'conservador');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('89012345678', 'vitoria@outlook.com', '22222222222', 'Vitória Pereira', 25000, 'senhaabc', 'moderado');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('90123456789', 'gustavo@gmail.com', '11111111111', 'Gustavo Martins', 18000, 'senha123', 'agressivo');
insert into usuario (cpf, email, celular, nome, saldo, senha, perfil_investidor) values ('01234567890', 'marcos@hotmail.com', '00000000000', 'Marcos Santos', 9000, 'abc123', 'conservador');

// relacionamento entre pg_curso e curso
CREATE TABLE gera (
    fk_curso_id_curso CHAR(8),
    fk_pg_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (fk_pg_curso_id_curso) REFERENCES pg_curso(id_curso)
);

INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('jsb1', 'c001');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('htmlec1', 'c002');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('phpi1', 'c003');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('exa1', 'c004');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('aad1', 'c005');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('pyad1', 'c006');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('jfx1', 'c007');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('unity1', 'c008');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('react1', 'c009');
INSERT INTO gera (fk_curso_id_curso, fk_pg_curso_id_curso) VALUES ('prm1', 'c010');

// relacionamento entre usuario e curso
CREATE TABLE faz (
    fk_usuario_cpf CHAR(11),
    fk_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf),
    FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678910', 'jsb1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('23456789012', 'htmlec1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('34567890123', 'phpi1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('45678901234', 'exa1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('56789012345', 'aad1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('67890123456', 'pyad1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('78901234567', 'jfx1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('89012345678', 'unity1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('90123456789', 'react1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('01234567890', 'prm1');

CREATE TABLE curso (
    duracao NUMBER(2) NOT NULL,
    avaliacao NUMBER(2) NOT NULL,
    resumo VARCHAR(250) NOT NULL,
    nome_professor VARCHAR(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    id_curso CHAR(8) NOT NULL,
    recompensa NUMBER(3) NOT NULL,
    CONSTRAINT curso_pk PRIMARY KEY (id_curso)
);

insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (10, 8, 'aprenda os fundamentos do javascript', 'joão da silva', 'javascript básico', 'jsb1', 50);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (15, 9, 'aprenda a construir websites com html e css', 'maria souza', 'html e css essencial', 'htmlec1', 75);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (20, 7, 'aprenda a criar aplicações web dinâmicas com php', 'pedro oliveira', 'php para iniciantes', 'phpi1', 100);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (5, 10, 'aprenda a usar ferramentas de análise de dados com excel', 'ana santos', 'excel avançado', 'exa1', 150);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (30, 8, 'aprenda a desenvolver aplicações móveis para android', 'rafael costa', 'android app development', 'aad1', 200);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (25, 6, 'aprenda a programar em python para análise de dados', 'juliana fernandes', 'python para análise de dados', 'pyad1', 125);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (12, 9, 'aprenda a criar interfaces gráficas com javafx', 'lucas mendes', 'javafx para desenvolvedores', 'jfx1', 175);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (8, 7, 'aprenda a criar jogos com a unity', 'felipe santos', 'desenvolvimento de jogos com unity', 'unity1', 100);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (18, 8, 'aprenda a usar o react para criar aplicações web', 'gabriel almeida', 'react para desenvolvedores web', 'react1', 150);
insert into curso (duracao, avaliacao, resumo, nome_professor, nome, id_curso, recompensa)
values (7, 10, 'aprenda a usar ferramentas de edição de vídeo com adobe premiere', 'paulo roberto', 'edição de vídeo com adobe premiere', 'prm1', 75);

create table modulo
(resumo varchar(100),
id_modulo char(8)constraint mod_id_pk  primary key,
nome varchar(30)
);

insert into modulo (resumo, id_modulo, nome)
values ('Introdução à programação', 'mod001', 'Programação básica');
insert into modulo (resumo, id_modulo, nome)
values ('Estrutura de dados', 'mod002', 'Algoritmos e estruturas de dados');
insert into modulo (resumo, id_modulo, nome)
values ('Desenvolvimento web', 'mod003', 'Front-end com HTML, CSS e JavaScript');
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

// relacionamento entre curso e modulo 
CREATE TABLE contem (
    fk_modulo_id_modulo CHAR(8),
    fk_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_modulo_id_modulo) REFERENCES modulo(id_modulo),
    FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod001', 'jsb1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod002', 'htmlec1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod003', 'phpi1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod004', 'exa1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod005', 'aad1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod006', 'pyad1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod007', 'jfx1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod008', 'unity1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod009', 'react1');
INSERT INTO contem (fk_modulo_id_modulo, fk_curso_id_curso)
VALUES ('mod010', 'prm1');

create table aula (
  tipo_contendo VARCHAR(30),
  duracao DATE,
  nome_aula VARCHAR(30),
  id_aula CHAR(8) CONSTRAINT aula_id_pk PRIMARY KEY,
  conteudo VARCHAR(40),
  avaliacao NUMBER(2)
);

insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'Introdução ao curso', 'aula001', 'Apresentação do curso', 90);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', TO_DATE('2022-03-02', 'YYYY-MM-DD'), 'Conceitos básicos', 'aula002', 'O que é programação?', 85);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2022-03-03', 'YYYY-MM-DD'), 'Tipos de dados', 'aula003', 'Números, texto, datas e booleanos', 80);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', TO_DATE('2022-03-04', 'YYYY-MM-DD'), 'Estruturas de controle', 'aula004', 'If, for, while, switch', 75);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2022-03-05', 'YYYY-MM-DD'), 'Funções', 'aula005', 'Criando e usando funções', 90);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'Arrays', 'aula006', 'Trabalhando com listas de valores', 80);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2022-03-07', 'YYYY-MM-DD'), 'Objetos', 'aula007', 'Classes, propriedades e métodos', 85);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Vídeo', TO_DATE('2022-03-08', 'YYYY-MM-DD'), 'Herança', 'aula008', 'Compartilhando comportamentos', 90);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2022-03-09', 'YYYY-MM-DD'), 'Interfaces', 'aula009', 'Contratos e implementações', 80);
insert into aula (tipo_contendo, duracao, nome_aula, id_aula, conteudo, avaliacao)
values ('Texto', TO_DATE('2024-05-09', 'YYYY-MM-DD'), 'Interfaces', 'aula010', 'Interpretação da linguagem', 70);

// Relacionamento entre aula e modulo
CREATE TABLE tem (
    fk_modulo_id_modulo CHAR(8),
    fk_aula_id_aula CHAR(8),
    FOREIGN KEY (fk_modulo_id_modulo) REFERENCES modulo(id_modulo),
    FOREIGN KEY (fk_aula_id_aula) REFERENCES aula(id_aula)
);

INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod001', 'aula001');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod002', 'aula002');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod003', 'aula003');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod004', 'aula004');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod005', 'aula005');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod006', 'aula006');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod007', 'aula007');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod008', 'aula008');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod009', 'aula009');
INSERT INTO tem (fk_modulo_id_modulo, fk_aula_id_aula) VALUES ('mod010', 'aula010');

CREATE TABLE certificado (
  nome_curso VARCHAR(50),
  nome_aluno VARCHAR(50),
  assinatura_plat CHAR(30),
  carga_horaria VARCHAR(10),
  dt_emissao DATE,
  dt_conclusao DATE,
  id_certificado CHAR(8) CONSTRAINT cert_id_pk PRIMARY KEY,
  nome_professor CHAR(30)
);

insert into certificado 
values ('Introdução à Programação', 'João da Silva', 'Digital Signature Inc.', '30h', TO_DATE('2022-03-05', 'YYYY-MM-DD'), TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'cert001', 'Maria Souza');
insert into certificado 
values  ('Python para Iniciantes', 'Ana Santos', 'CertSign', '40h', TO_DATE('2022-03-10', 'YYYY-MM-DD'), TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'cert002', 'Paulo Oliveira');
insert into certificado 
values  ('Desenvolvimento Web com JavaScript', 'Pedro Alves', 'GlobalSign', '60h', TO_DATE('2022-03-15', 'YYYY-MM-DD'), TO_DATE('2022-03-10', 'YYYY-MM-DD'), 'cert003', 'Lucas Souza');
insert into certificado 
values  ('Algoritmos e Lógica de Programação', 'Maria Lima', 'DigiCert', '20h', TO_DATE('2022-03-20', 'YYYY-MM-DD'), TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'cert004', 'José Santos');
insert into certificado 
values  ('Java Avançado', 'Luiz Silva', 'Entrust Datacard', '80h', TO_DATE('2022-03-25', 'YYYY-MM-DD'), TO_DATE('2022-03-20', 'YYYY-MM-DD'), 'cert005', 'Roberto Oliveira');
insert into certificado 
values  ('PHP Básico', 'Carla Santos', 'Comodo CA', '30h', TO_DATE('2022-04-01', 'YYYY-MM-DD'), TO_DATE('2022-03-27', 'YYYY-MM-DD'), 'cert006', 'Marcelo Souza');
insert into certificado 
values  ('SQL para Iniciantes', 'Fernando Lima', 'Symantec', '20h', TO_DATE('2022-04-05', 'YYYY-MM-DD'), TO_DATE('2022-04-01', 'YYYY-MM-DD'), 'cert007', 'Paula Oliveira');
insert into certificado 
values  ('C++ Avançado', 'Gabriela Almeida', 'Thawte', '60h', TO_DATE('2022-01-28', 'YYYY-MM-DD'), TO_DATE('2022-02-28', 'YYYY-MM-DD'), 'cert008', 'Luciano Santos');
insert into certificado 
values  ('Java para Desenvolvimento Web', 'Aline Silva', 'Entrust Datacard', '50h', TO_DATE('2022-02-28', 'YYYY-MM-DD'), TO_DATE('2022-02-15', 'YYYY-MM-DD'), 'cert009', 'André Souza');
insert into certificado 
values  ('Python Avançado', 'Felipe Rodrigues', 'CertSign', '70h', TO_DATE('2022-03-01', 'YYYY-MM-DD'), TO_DATE('2022-02-20', 'YYYY-MM-DD'), 'cert010', 'Pedro Oliveira');

// relação entre curso e certificado
CREATE TABLE libera (
    fk_certificado_id_certificado CHAR(8),
    fk_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_certificado_id_certificado) REFERENCES certificado(id_certificado),
    FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert001', 'jsb1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert002', 'htmlec1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert003', 'phpi1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert004', 'exa1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert005', 'aad1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert006', 'pyad1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert007', 'jfx1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert008', 'unity1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert009', 'prm1');
INSERT INTO libera (fk_certificado_id_certificado, fk_curso_id_curso) VALUES ('cert010', 'react1');

create table login (
  id_sessao char(8) CONSTRAINT login_id_sessao primary key,
  hrs_plataforma date,
  ultima_sessao date,
  hr_sessao_atual date
);

INSERT INTO login VALUES ('sessao01', to_date('2022-03-13 09:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 18:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 09:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao02', to_date('2022-03-13 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 19:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 10:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao03', to_date('2022-03-13 11:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 20:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 11:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao04', to_date('2022-03-13 12:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 21:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 12:20:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao05', to_date('2022-03-13 13:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 22:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 13:10:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao06', to_date('2022-03-13 14:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-12 23:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 14:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao07', to_date('2022-03-13 15:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 15:05:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao08', to_date('2022-03-13 16:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 01:00:00', 'YYYY-MM-DD HH24:MI:SS'), to_date('2022-03-13 16:50:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao09', TO_DATE('2022-03-13 12:30:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2022-03-12 18:30:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2022-03-13 14:15:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO login VALUES ('sessao10', TO_DATE('2022-03-14 10:45:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2022-03-13 20:00:00', 'YYYY-MM-DD HH24:MI:SS'), TO_DATE('2022-03-14 11:30:00', 'YYYY-MM-DD HH24:MI:SS'));

//relação entre usuario e login   
CREATE TABLE realiza (
    fk_usuario_cpf CHAR(11),
    fk_login_id_sessao CHAR(8),
    FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf),
    FOREIGN KEY (fk_login_id_sessao) REFERENCES login(id_sessao)
);
INSERT INTO realiza VALUES ('12345678910', 'sessao01');
INSERT INTO realiza VALUES ('23456789012', 'sessao02');
INSERT INTO realiza VALUES ('34567890123', 'sessao03');
INSERT INTO realiza VALUES ('45678901234', 'sessao04');
INSERT INTO realiza VALUES ('56789012345', 'sessao05');
INSERT INTO realiza VALUES ('67890123456', 'sessao06');
INSERT INTO realiza VALUES ('78901234567', 'sessao07');
INSERT INTO realiza VALUES ('89012345678', 'sessao08');
INSERT INTO realiza VALUES ('90123456789', 'sessao09');
INSERT INTO realiza VALUES ('01234567890', 'sessao10');

commit;
