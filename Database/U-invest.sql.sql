CREATE TABLE usuario (
    cpf CHAR(11) CONSTRAINT us_cpf_pk PRIMARY KEY,
    email varchar2(50) NOT NULL,
    celular CHAR(11) UNIQUE NOT NULL,
    nome varchar2(50) NOT NULL,
    saldo NUMBER(5) NOT NULL,
    senha varchar2(20) NOT NULL,
    perfil_investidor varchar2(20) NOT NULL,
    nickname varchar2(20) NOT NULL,
    nascimento varchar2(8) NOT NULL --DDmmYYYY
);

CREATE TABLE login (
  id_sessao CHAR(8) CONSTRAINT login_id_sessao_pk PRIMARY KEY,
  hrs_plataforma NUMBER(5) NOT NULL,
  ultima_sessao varchar2(10) NOT NULL, --DDmmYYYYhh
  hr_sessao_atual varchar2(10) NOT NULL, --DDmmYYYYhh
  fk_usuario_cpf CHAR(11),
  FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf)
);

CREATE TABLE curso (
    duracao NUMBER(2) NOT NULL,
    avaliacao NUMBER(2) NOT NULL,
    resumo varchar2(250) NOT NULL,
    professor varchar2(50) NOT NULL,
    nome varchar2(50) NOT NULL,
    id_curso CHAR(8) CONSTRAINT curso_id_pk PRIMARY KEY,
    pontuacao NUMBER(5) NOT NULL
);

-- relacionamento entre usuario e curso
CREATE TABLE faz ( -- Questionar com professor
    fk_usuario_cpf CHAR(11),
    fk_curso_id_curso CHAR(8),
    FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf),
    FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE pg_curso (
  progresso_user NUMBER(3) NOT NULL,
  ultimo_acesso varchar2(10) NOT NULL, --DDmmYYYYhh
  u_coins NUMBER(5) NOT NULL,
  fk_usuario_cpf CHAR(11),
  fk_curso_id_curso CHAR(8),
  FOREIGN KEY (fk_usuario_cpf) REFERENCES usuario(cpf),
  FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE certificado (
  nome_curso varchar2(50) NOT NULL,
  nome_aluno varchar2(50) NOT NULL,
  assinatura_plat varchar2(30)NOT NULL, --Questionar com professor
  carga_horaria NUMBER(2) NOT NULL,
  dt_emissao varchar2(8) NOT NULL,
  dt_conclusao varchar2(8) NOT NULL,
  id_certificado CHAR(8) CONSTRAINT certificado_id_pk PRIMARY KEY,
  professor varchar2(50) NOT NULL,
  fk_curso_id_curso CHAR(8),
  FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE modulo (
  resumo varchar2(250),
  id_modulo CHAR(8) CONSTRAINT modulo_id_pk PRIMARY KEY,
  nome varchar2(50) NOT NULL,
  fk_curso_id_curso CHAR(8),
  FOREIGN KEY (fk_curso_id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE aula (
  tipo_conteudo varchar2(30) NOT NULL, --Questionar esse campo com o professor.
  duracao varchar2 NOT NULL, -- HHmmss
  nome_aula varchar2(50) NOT NULL,
  id_aula CHAR(8) CONSTRAINT aula_id_pk PRIMARY KEY,
  conteudo varchar2(40) NOT NULL, --Questionar esse campo com o professor.
  avaliacao NUMBER(2) NOT NULL,
  fk_modulo_id_modulo CHAR(8),
  FOREIGN KEY (fk_modulo_id_modulo) REFERENCES modulo(id_modulo)
);

insert into usuario  values ('12345678910', 'joao@gmail.com', '99999999999', 'Jo�o Silva', 10000, 'senha123', 'conservador','joaoGamer','10042000');
insert into usuario  values ('23456789012', 'maria@hotmail.com', '88888888888', 'Maria Souza', 5000, 'abc123', 'moderado','marimari','11042000');
insert into usuario  values ('34567890123', 'pedro@yahoo.com', '77777777777', 'Pedro Almeida', 20000, 'senha456', 'agressivo','pedroGamer','12042000');
insert into usuario  values ('45678901234', 'ana@outlook.com', '66666666666', 'Ana Santos', 15000, 'senha789', 'moderado','aninhaDoGrau','13042000');
insert into usuario  values ('56789012345', 'felipe@gmail.com', '55555555555', 'Felipe Costa', 8000, 'senhaabc', 'conservador','Felps','14042000');
insert into usuario  values ('67890123456', 'lucas@hotmail.com', '44444444444', 'Lucas Oliveira', 12000, 'senha456', 'agressivo','luqueta','15042000');
insert into usuario  values ('78901234567', 'carla@yahoo.com', '33333333333', 'Carla Lima', 7000, 'senha789', 'conservador','carlaPeres','16042000');
insert into usuario values  ('89012345678', 'vitoria@outlook.com', '22222222222', 'Vitoria Pereira', 25000, 'senhaabc', 'moderado', 'vic02', '17042000');
insert into usuario  values ('90123456789', 'gustavo@gmail.com', '11111111111', 'Gustavo Martins', 18000, 'senha123', 'agressivo','guguiha','18042000');
insert into usuario  values ('01234567890', 'marcos@hotmail.com', '00000000000', 'Marcos Santos', 9000, 'abc123', 'conservador','marcolas','19042000');

INSERT INTO login VALUES ('sessao01', 10, '0802202313', '0803202313', 12345678910);
INSERT INTO login VALUES ('sessao02', 11, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678911);
INSERT INTO login VALUES ('sessao03', 12, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678912);
INSERT INTO login VALUES ('sessao04', 13, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678913);
INSERT INTO login VALUES ('sessao05', 14, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678914);
INSERT INTO login VALUES ('sessao06', 15, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678915);
INSERT INTO login VALUES ('sessao07', 16, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678916);
INSERT INTO login VALUES ('sessao08', 17, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678917);
INSERT INTO login VALUES ('sessao09', 18, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678918);
INSERT INTO login VALUES ('sessao10', 19, 'DDmmYYYYhh', 'DDmmYYYYhh', 12345678919);

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

-- PARAMOS AQUI

insert into curso values (10, 8, 'aprenda os fundamentos do javascript', 'jo�o da silva', 'javascript b�sico', 'jsb1', 50,90);
insert into curso values (15, 9, 'aprenda a construir websites com html e css', 'maria souza', 'html e css essencial', 'htmlec1', 75,100);
insert into curso values (20, 7, 'aprenda a criar aplica��es web din�micas com php', 'pedro oliveira', 'php para iniciantes', 'phpi1', 100,60);
insert into curso values (5, 10, 'aprenda a usar ferramentas de an�lise de dados com excel', 'ana santos', 'excel avan�ado', 'exa1', 150,80);
insert into curso values (30, 8, 'aprenda a desenvolver aplica��es m�veis para android', 'rafael costa', 'android app development', 'aad1', 200,90);
insert into curso values (25, 6, 'aprenda a programar em python para an�lise de dados', 'juliana fernandes', 'python para an�lise de dados', 'pyad1', 125,30);
insert into curso values (12, 9, 'aprenda a criar interfaces gr�ficas com javafx', 'lucas mendes', 'javafx para desenvolvedores', 'jfx1', 175,100);
insert into curso values (8, 7, 'aprenda a criar jogos com a unity', 'felipe santos', 'desenvolvimento de jogos com unity', 'unity1', 100,68);
insert into curso values (18, 8, 'aprenda a usar o react para criar aplica��es web', 'gabriel almeida', 'react para desenvolvedores web', 'react1', 150,90);
insert into curso values (7, 10, 'aprenda a usar ferramentas de edi��o de v�deo com adobe premiere', 'paulo roberto', 'edicao de v�deo com adobe premiere', 'prm1', 75,78);

insert into modulo values ('Introducao h� programa��o', 'mod001', 'Programa��o b�sica');
insert into modulo values ('Estrutura de dados', 'mod002', 'Algoritmos e estruturas de dados');
insert into modulo values ('Desenvolvimento web', 'mod003', 'Front-end com HTML, CSS e JavaScript');
insert into modulo values ('linguagem de programacao', 'mod004', 'L�gica para iniciantes');
insert into modulo values ('Banco de dados', 'mod005', 'MySQL e SQL Server');
insert into modulo values ('Programa��o orientada a objetos', 'mod006', 'POO com Java');
insert into modulo values ('Desenvolvimento mobile', 'mod007', 'Android Studio');
insert into modulo values ('Programa��o funcional', 'mod008', 'JavaScript avan�ado');
insert into modulo values ('Data Science', 'mod009', 'Introdu��o ao R');
insert into modulo values ('Redes de computadores', 'mod010', 'Fundamentos de redes');

INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'Introdu��o ao curso', 'aula001', 'Apresenta��o do curso', 90);
INSERT INTO aula VALUES ('V�deo', TO_DATE('2022-03-02', 'YYYY-MM-DD'), 'Conceitos b�sicos', 'aula002', 'O que � programa��o?', 85);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-03', 'YYYY-MM-DD'), 'Tipos de dados', 'aula003', 'N�meros, texto, datas e booleanos', 80);
INSERT INTO aula VALUES ('V�deo', TO_DATE('2022-03-04', 'YYYY-MM-DD'), 'Estruturas de controle', 'aula004', 'If, for, while, switch', 75);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-05', 'YYYY-MM-DD'), 'Fun��es', 'aula005', 'Criando e usando fun��es', 90);
INSERT INTO aula VALUES ('V�deo', TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'Arrays', 'aula006', 'Trabalhando com listas de valores', 80);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-07', 'YYYY-MM-DD'), 'Objetos', 'aula007', 'Classes, propriedades e m�todos', 85);
INSERT INTO aula VALUES ('V�deo', TO_DATE('2022-03-08', 'YYYY-MM-DD'), 'Heran�a', 'aula008', 'Compartilhando comportamentos', 90);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-03-09', 'YYYY-MM-DD'), 'Interfaces', 'aula009', 'Contratos e implementa��es', 80);
INSERT INTO aula VALUES ('Texto', TO_DATE('2022-05-09', 'YYYY-MM-DD'), 'Interpreta��o da linguagem', 'aula010', 'Entendendo como o c�digo � executado', 70);

insert into certificado values ('Introducao h� Programacao', 'Joao da Silva', 'Digital Signature Inc.', '30h', TO_DATE('2022-03-05', 'YYYY-MM-DD'), TO_DATE('2022-03-01', 'YYYY-MM-DD'), 'cert001', 'Maria Souza');
insert into certificado values  ('Python para Iniciantes', 'Ana Santos', 'CertSign', '40h', TO_DATE('2022-03-10', 'YYYY-MM-DD'), TO_DATE('2022-03-06', 'YYYY-MM-DD'), 'cert002', 'Paulo Oliveira');
insert into certificado values  ('Desenvolvimento Web com JavaScript', 'Pedro Alves', 'GlobalSign', '60h', TO_DATE('2022-03-15', 'YYYY-MM-DD'), TO_DATE('2022-03-10', 'YYYY-MM-DD'), 'cert003', 'Lucas Souza');
insert into certificado values  ('Algoritmos e Logica de Programacao', 'Maria Lima', 'DigiCert', '20h', TO_DATE('2022-03-20', 'YYYY-MM-DD'), TO_DATE('2022-03-15', 'YYYY-MM-DD'), 'cert004', 'Jos� Santos');
insert into certificado values  ('Java Avancado', 'Luiz Silva', 'Entrust Datacard', '80h', TO_DATE('2022-03-25', 'YYYY-MM-DD'), TO_DATE('2022-03-20', 'YYYY-MM-DD'), 'cert005', 'Roberto Oliveira');
insert into certificado values  ('PHP Bascio', 'Carla Santos', 'Comodo CA', '30h', TO_DATE('2022-04-01', 'YYYY-MM-DD'), TO_DATE('2022-03-27', 'YYYY-MM-DD'), 'cert006', 'Marcelo Souza');
insert into certificado values  ('SQL para Iniciantes', 'Fernando Lima', 'Symantec', '20h', TO_DATE('2022-04-05', 'YYYY-MM-DD'), TO_DATE('2022-04-01', 'YYYY-MM-DD'), 'cert007', 'Paula Oliveira');
insert into certificado values  ('C++ Avancado', 'Gabriela Almeida', 'Thawte', '60h', TO_DATE('2022-01-28', 'YYYY-MM-DD'), TO_DATE('2022-02-28', 'YYYY-MM-DD'), 'cert008', 'Luciano Santos');
insert into certificado values  ('Java para Desenvolvimento Web', 'Aline Silva', 'Entrust Datacard', '50h', TO_DATE('2022-02-28', 'YYYY-MM-DD'), TO_DATE('2022-02-15', 'YYYY-MM-DD'), 'cert009', 'Andr� Souza');
insert into certificado values  ('Python Avancado', 'Felipe Rodrigues', 'CertSign', '70h', TO_DATE('2022-03-01', 'YYYY-MM-DD'), TO_DATE('2022-02-20', 'YYYY-MM-DD'), 'cert010', 'Pedro Oliveira');

commit;