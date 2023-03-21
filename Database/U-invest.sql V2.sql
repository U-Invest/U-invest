CREATE TABLE pg_curso (
  id_curso CHAR(8) CONSTRAINT pg_id_pk PRIMARY KEY,
  progresso_user NUMBER(3) NOT NULL,
  ultimo_acesso DATE,
  u_coins NUMBER(5) NOT NULL
);

insert into pg_curso  values ('c001', 50, '22-01-2022', 1000);
insert into pg_curso  values ('c002', 80, '14-02-2022', 2500);
insert into pg_curso  values ('c003', 10, '07-03-2022', 500);
insert into pg_curso  values ('c004', 25, '19-04-2022', 1500);
insert into pg_curso  values ('c005', 90, '23-05-2022', 3500);
insert into pg_curso  values ('c006', 75, '08-06-2022', 2000);
insert into pg_curso  values ('c007', 40, '04-07-2022', 800);
insert into pg_curso  values ('c008', 70, '12-08-2022', 1800);
insert into pg_curso  values ('c009', 20, '20-09-2022', 600);
insert into pg_curso  values ('c010', 100, '31-10-2022', 5000);

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
    cpf CHAR(11) CONSTRAINT us_cpf_pk PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    celular CHAR(11) UNIQUE NOT NULL,
    nome VARCHAR(50) NOT NULL,
    saldo NUMBER(5) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    perfil_investidor VARCHAR(20) NOT NULL,
    nascimento date,
    usuario varchar2(20) not null
);

insert into usuario  values ('12345678910', 'joao@gmail.com', '99999999999', 'Joï¿½o Silva', 10000, 'senha123', 'conservador','10-Jan-00','Joao_Silva');
insert into usuario  values ('23456789012', 'maria@hotmail.com', '88888888888', 'Maria Souza', 5000, 'abc123', 'moderado','12-Fev-22','Maria0233');
insert into usuario  values ('34567890123', 'pedro@yahoo.com', '77777777777', 'Pedro Almeida', 20000, 'senha456', 'agressivo','17-abr-22','pedrinho12');
insert into usuario  values ('45678901234', 'ana@outlook.com', '66666666666', 'Ana Santos', 15000, 'senha789', 'moderado','07-dez-22','ana_Claudia');
insert into usuario  values ('56789012345', 'felipe@gmail.com', '55555555555', 'Felipe Costa', 8000, 'senhaabc', 'conservador','14-ago-22','felip');
insert into usuario  values ('67890123456', 'lucas@hotmail.com', '44444444444', 'Lucas Oliveira', 12000, 'senha456', 'agressivo','27-out-22','Luxcas');
insert into usuario  values ('78901234567', 'carla@yahoo.com', '33333333333', 'Carla Lima', 7000, 'senha789', 'conservador','02-mai-22','Carloo');
insert into usuario values  ('89012345678', 'vitoria@outlook.com', '22222222222', 'Vitoria Pereira', 25000, 'senhaabc', 'moderado', '13-jun-22', 'Vitoria');
insert into usuario  values ('90123456789', 'gustavo@gmail.com', '11111111111', 'Gustavo Martins', 18000, 'senha123', 'agressivo','21-fev-22','Gustavo');
insert into usuario  values ('01234567890', 'marcos@hotmail.com', '00000000000', 'Marcos Santos', 9000, 'abc123', 'conservador','20-jan-22','MarcosS');


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
    professor VARCHAR(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    id_curso CHAR(8) NOT NULL,
    recompensa NUMBER(3) NOT NULL,
    pontuacao number(5) not null,
    CONSTRAINT curso_pk PRIMARY KEY (id_curso)
);

insert into curso values (10, 8, 'aprenda os fundamentos do javascript', 'joï¿½o da silva', 'javascript bï¿½sico', 'jsb1', 50,90);
insert into curso values (15, 9, 'aprenda a construir websites com html e css', 'maria souza', 'html e css essencial', 'htmlec1', 75,100);
insert into curso values (20, 7, 'aprenda a criar aplicaï¿½ï¿½es web dinï¿½micas com php', 'pedro oliveira', 'php para iniciantes', 'phpi1', 100,60);
insert into curso values (5, 10, 'aprenda a usar ferramentas de anï¿½lise de dados com excel', 'ana santos', 'excel avanï¿½ado', 'exa1', 150,80);
insert into curso values (30, 8, 'aprenda a desenvolver aplicaï¿½ï¿½es mï¿½veis para android', 'rafael costa', 'android app development', 'aad1', 200,90);
insert into curso values (25, 6, 'aprenda a programar em python para anï¿½lise de dados', 'juliana fernandes', 'python para anï¿½lise de dados', 'pyad1', 125,30);
insert into curso values (12, 9, 'aprenda a criar interfaces grï¿½ficas com javafx', 'lucas mendes', 'javafx para desenvolvedores', 'jfx1', 175,100);
insert into curso values (8, 7, 'aprenda a criar jogos com a unity', 'felipe santos', 'desenvolvimento de jogos com unity', 'unity1', 100,68);
insert into curso values (18, 8, 'aprenda a usar o react para criar aplicaï¿½ï¿½es web', 'gabriel almeida', 'react para desenvolvedores web', 'react1', 150,90);
insert into curso values (7, 10, 'aprenda a usar ferramentas de ediï¿½ï¿½o de vï¿½deo com adobe premiere', 'paulo roberto', 'edicao de vïdeo com adobe premiere', 'prm1', 75,78);

create table modulo
(resumo varchar(100),
id_modulo char(8)constraint mod_id_pk  primary key,
nome varchar(40) not null
);

insert into modulo values ('Introducao há programação', 'mod001', 'Programação básica');
insert into modulo values ('Estrutura de dados', 'mod002', 'Algoritmos e estruturas de dados');
insert into modulo values ('Desenvolvimento web', 'mod003', 'Front-end com HTML, CSS e JavaScript');
insert into modulo values ('linguagem de programacao', 'mod004', 'Lógica para iniciantes');
insert into modulo values ('Banco de dados', 'mod005', 'MySQL e SQL Server');
insert into modulo values ('Programação orientada a objetos', 'mod006', 'POO com Java');
insert into modulo values ('Desenvolvimento mobile', 'mod007', 'Android Studio');
insert into modulo values ('Programação funcional', 'mod008', 'JavaScript avançado');
insert into modulo values ('Data Science', 'mod009', 'Introdução ao R');
insert into modulo values ('Redes de computadores', 'mod010', 'Fundamentos de redes');


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
  tipo_conteudo VARCHAR(30) not null,
  duracao DATE not null,
  nome_aula VARCHAR(30) not null,
  id_aula CHAR(8) CONSTRAINT aula_id_pk PRIMARY KEY,
  conteudo VARCHAR(40) not null,
  avaliacao NUMBER(2) not null
);

INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'Introdução ao curso', 'aula001', 'Apresentação do curso', 90);
INSERT INTO aula VALUES ('Vídeo', TO_DATE('2022-03-02', 'YYYY-MM-DD'), 'Conceitos básicos', 'aula002', 'O que é programação?', 85);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-03', 'YYYY-MM-DD'), 'Tipos de dados', 'aula003', 'Números, texto, datas e booleanos', 80);
INSERT INTO aula VALUES ('Vídeo', TO_DATE('2022-03-04', 'YYYY-MM-DD'), 'Estruturas de controle', 'aula004', 'If, for, while, switch', 75);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-05', 'YYYY-MM-DD'), 'Funções', 'aula005', 'Criando e usando funções', 90);
INSERT INTO aula VALUES ('Vídeo', TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'Arrays', 'aula006', 'Trabalhando com listas de valores', 80);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-07', 'YYYY-MM-DD'), 'Objetos', 'aula007', 'Classes, propriedades e métodos', 85);
INSERT INTO aula VALUES ('Vídeo', TO_DATE('2022-03-08', 'YYYY-MM-DD'), 'Herança', 'aula008', 'Compartilhando comportamentos', 90);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-09', 'YYYY-MM-DD'), 'Interfaces', 'aula009', 'Contratos e implementações', 80);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-05-09', 'YYYY-MM-DD'), 'Interpretação da linguagem', 'aula010', 'Entendendo como o código é executado', 70);


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
  nome_curso VARCHAR(50) NOT NULL,
  nome_aluno VARCHAR(50) NOT NULL,
  assinatura_plat CHAR(30)NOT NULL,
  carga_horaria VARCHAR(10)NOT NULL,
  dt_emissao DATE NOT NULL,
  dt_conclusao DATE NOT NULL,
  id_certificado CHAR(8) CONSTRAINT cert_id_pk PRIMARY KEY,
  professor CHAR(30) NOT NULL
);
delete from certificado
insert into certificado values ('Introducao há Programacao', 'Joao da Silva', 'Digital Signature Inc.', '30h', TO_DATE('2022-03-05', 'YYYY-MM-DD'), TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'cert001', 'Maria Souza');
insert into certificado values  ('Python para Iniciantes', 'Ana Santos', 'CertSign', '40h', TO_DATE('2022-03-10', 'YYYY-MM-DD'), TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'cert002', 'Paulo Oliveira');
insert into certificado values  ('Desenvolvimento Web com JavaScript', 'Pedro Alves', 'GlobalSign', '60h', TO_DATE('2022-03-15', 'YYYY-MM-DD'), TO_DATE('2022-03-10', 'YYYY-MM-DD'), 'cert003', 'Lucas Souza');
insert into certificado values  ('Algoritmos e Logica de Programacao', 'Maria Lima', 'DigiCert', '20h', TO_DATE('2022-03-20', 'YYYY-MM-DD'), TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'cert004', 'Josï¿½ Santos');
insert into certificado values  ('Java Avancado', 'Luiz Silva', 'Entrust Datacard', '80h', TO_DATE('2022-03-25', 'YYYY-MM-DD'), TO_DATE('2022-03-20', 'YYYY-MM-DD'), 'cert005', 'Roberto Oliveira');
insert into certificado values  ('PHP Bascio', 'Carla Santos', 'Comodo CA', '30h', TO_DATE('2022-04-01', 'YYYY-MM-DD'), TO_DATE('2022-03-27', 'YYYY-MM-DD'), 'cert006', 'Marcelo Souza');
insert into certificado values  ('SQL para Iniciantes', 'Fernando Lima', 'Symantec', '20h', TO_DATE('2022-04-05', 'YYYY-MM-DD'), TO_DATE('2022-04-01', 'YYYY-MM-DD'), 'cert007', 'Paula Oliveira');
insert into certificado values  ('C++ Avancado', 'Gabriela Almeida', 'Thawte', '60h', TO_DATE('2022-01-28', 'YYYY-MM-DD'), TO_DATE('2022-02-28', 'YYYY-MM-DD'), 'cert008', 'Luciano Santos');
insert into certificado values  ('Java para Desenvolvimento Web', 'Aline Silva', 'Entrust Datacard', '50h', TO_DATE('2022-02-28', 'YYYY-MM-DD'), TO_DATE('2022-02-15', 'YYYY-MM-DD'), 'cert009', 'Andrï¿½ Souza');
insert into certificado values  ('Python Avancado', 'Felipe Rodrigues', 'CertSign', '70h', TO_DATE('2022-03-01', 'YYYY-MM-DD'), TO_DATE('2022-02-20', 'YYYY-MM-DD'), 'cert010', 'Pedro Oliveira');

// relacionamento entre curso e certificado
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
  hrs_plataforma date NOT NULL,
  ultima_sessao date NOT NULL,
  hr_sessao_atual date NOT NULL
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

//relacionamento entre usuario e login   
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
