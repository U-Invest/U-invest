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
  hr_sessao_atual varchar2(11) NOT NULL, -- dd HH:mm:ss
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
  duracao varchar2(6) NOT NULL, -- HHmmss
  nome_aula varchar2(50) NOT NULL,
  id_aula CHAR(8) CONSTRAINT aula_id_pk PRIMARY KEY,
  conteudo varchar2(40) NOT NULL, --Questionar esse campo com o professor.
  avaliacao NUMBER(2) NOT NULL,
  fk_modulo_id_modulo CHAR(8),
  FOREIGN KEY (fk_modulo_id_modulo) REFERENCES modulo(id_modulo)
);

INSERT INTO usuario VALUES ('12345678910', 'joao@gmail.com', '99999999999', 'Jo�o Silva', 10000, 'senha123', 'conservador','joaoGamer','10042000');
INSERT INTO usuario VALUES ('12345678911', 'maria@hotmail.com', '88888888888', 'Maria Souza', 5000, 'abc123', 'moderado','marimari','11042000');
INSERT INTO usuario VALUES ('12345678912', 'pedro@yahoo.com', '77777777777', 'Pedro Almeida', 20000, 'senha456', 'agressivo','pedroGamer','12042000');
INSERT INTO usuario VALUES ('12345678913', 'ana@outlook.com', '66666666666', 'Ana Santos', 15000, 'senha789', 'moderado','aninhaDoGrau','13042000');
INSERT INTO usuario VALUES ('12345678914', 'felipe@gmail.com', '55555555555', 'Felipe Costa', 8000, 'senhaabc', 'conservador','Felps','14042000');
INSERT INTO usuario VALUES ('12345678915', 'lucas@hotmail.com', '44444444444', 'Lucas Oliveira', 12000, 'senha456', 'agressivo','luqueta','15042000');
INSERT INTO usuario VALUES ('12345678916', 'carla@yahoo.com', '33333333333', 'Carla Lima', 7000, 'senha789', 'conservador','carlaPeres','16042000');
INSERT INTO usuario VALUES ('12345678917', 'vitoria@outlook.com', '22222222222', 'Vitoria Pereira', 25000, 'senhaabc', 'moderado', 'vic02', '17042000');
INSERT INTO usuario VALUES ('12345678918', 'gustavo@gmail.com', '11111111111', 'Gustavo Martins', 18000, 'senha123', 'agressivo','guguiha','18042000');
INSERT INTO usuario VALUES ('12345678919', 'marcos@hotmail.com', '00000000000', 'Marcos Santos', 9000, 'abc123', 'conservador','marcolas','19042000');

INSERT INTO login VALUES ('sessao01', 10, '0102102313', '12 15:23:12', 12345678910);
INSERT INTO login VALUES ('sessao02', 11, '0202102314', '13 16:11:56', 12345678911);
INSERT INTO login VALUES ('sessao03', 12, '0302102315', '14 17:35:44', 12345678912);
INSERT INTO login VALUES ('sessao04', 13, '0402102316', '15 18:54:56', 12345678913);
INSERT INTO login VALUES ('sessao05', 14, '0502102317', '16 19:33:22', 12345678914);
INSERT INTO login VALUES ('sessao06', 15, '0602102318', '17 20:22:46', 12345678915);
INSERT INTO login VALUES ('sessao07', 16, '0702102319', '18 21:32:34', 12345678916);
INSERT INTO login VALUES ('sessao08', 17, '0802102320', '19 22:54:43', 12345678917);
INSERT INTO login VALUES ('sessao09', 18, '0902102321', '20 23:21:54', 12345678918);
INSERT INTO login VALUES ('sessao10', 19, '1002102322', '21 24:12:11', 12345678919);

INSERT INTO pg_curso  values (100,'22-01-2022', 1000,'12345678910', 'jsb1');
INSERT INTO pg_curso  values (70,'14-02-2022', 2500,'12345678911','htmlec1');
INSERT INTO pg_curso  values (87,'07-03-2022', 500,'12345678912', 'phpi1');
INSERT INTO pg_curso  values (96,'19-04-2022', 1500,'12345678913','exa1');
INSERT INTO pg_curso  values (94,'23-05-2022', 3500,'12345678914','aad1');
INSERT INTO pg_curso  values (78,'08-06-2022', 2000,'12345678915','pyad1');
INSERT INTO pg_curso  values (87,'04-07-2022', 800,'12345678916','jfx1');
INSERT INTO pg_curso  values (85,'12-08-2022', 1800,'12345678917','unity1');
INSERT INTO pg_curso  values (100,'20-09-2022', 600,'12345678918','react1');
INSERT INTO pg_curso  values (32,'31-10-2022', 5000,'12345678919','prm1');

INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678910', 'jsb1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678911', 'htmlec1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678912', 'phpi1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678913', 'exa1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678914', 'aad1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678915', 'pyad1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678916', 'jfx1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678917', 'unity1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678918', 'react1');
INSERT INTO faz (fk_usuario_cpf, fk_curso_id_curso) VALUES ('12345678919', 'prm1');

INSERT INTO curso VALUES (10, 8, 'aprenda os fundamentos do javascript', 'jo�o da silva', 'javascript basico', 'jsb1', 50);
INSERT INTO curso VALUES (15, 9, 'aprenda a construir websites com html e css', 'maria souza', 'html e css essencial', 'htmlec1', 75);
INSERT INTO curso VALUES (20, 7, 'aprenda a criar aplicacoes web din�micas com php', 'pedro oliveira', 'php para iniciantes', 'phpi1', 100);
INSERT INTO curso VALUES (5, 10, 'aprenda a usar ferramentas de an�lise de dados com excel', 'ana santos', 'excel avancado', 'exa1', 150);
INSERT INTO curso VALUES (30, 8, 'aprenda a desenvolver aplicacoes m�veis para android', 'rafael costa', 'android app development', 'aad1', 200);
INSERT INTO curso VALUES (25, 6, 'aprenda a programar em python para an�lise de dados', 'juliana fernandes', 'python para analise de dados', 'pyad1', 125);
INSERT INTO curso VALUES (12, 9, 'aprenda a criar interfaces graficas com javafx', 'lucas mendes', 'javafx para desenvolvedores', 'jfx1', 175);
INSERT INTO curso VALUES (8, 7, 'aprenda a criar jogos com a unity', 'felipe santos', 'desenvolvimento de jogos com unity', 'unity1', 100);
INSERT INTO curso VALUES (18, 8, 'aprenda a usar o react para criar aplicacoes web', 'gabriel almeida', 'react para desenvolvedores web', 'react1', 150);
INSERT INTO curso VALUES (7, 10, 'aprenda a usar ferramentas de edicao de video com adobe premiere', 'paulo roberto', 'edicao de v�deo com adobe premiere', 'prm1', 75);

INSERT INTO modulo VALUES ('Introducao h� programacao', 'mod001', 'Programacao Basica','jsb1');
INSERT INTO modulo VALUES ('Estrutura de dados', 'mod002', 'Algoritmos e estruturas de dados','htmlec1');
INSERT INTO modulo VALUES ('Desenvolvimento web', 'mod003', 'Front-end com HTML, CSS e JavaScript','phpi1');
INSERT INTO modulo VALUES ('linguagem de programacao', 'mod004', 'Logica para iniciantes','exa1');
INSERT INTO modulo VALUES ('Banco de dados', 'mod005', 'MySQL e SQL Server','aad1');
INSERT INTO modulo VALUES ('Programacao orientada a objetos', 'mod006', 'POO com Java','pyad1');
INSERT INTO modulo VALUES ('Desenvolvimento mobile', 'mod007', 'Android Studio','jfx1');
INSERT INTO modulo VALUES ('Programacao funcional', 'mod008', 'JavaScript avancado','unity1');
INSERT INTO modulo VALUES ('Data Science', 'mod009', 'Introducao ao R','react1');
INSERT INTO modulo VALUES ('Redes de computadores', 'mod010', 'Fundamentos de redes','prm1');

INSERT INTO aula VALUES ('Texto','30h','Introdu��o ao curso', 'aula001', 'Apresenta��o do curso',90,'mod001');
INSERT INTO aula VALUES ('Video','45h','Conceitos basicos', 'aula002', 'O que que � programacao', 85,'mod002');
INSERT INTO aula VALUES ('Texto','53h','Tipos de dados', 'aula003', 'Numeros, texto, datas e booleanos', 80,'mod003');
INSERT INTO aula VALUES ('Video','57h','Estruturas de controle', 'aula004', 'If, for, while, switch', 75,'mod004');
INSERT INTO aula VALUES ('Texto','73h','Funalidades', 'aula005', 'Criando e usando funcionaliddades', 90, 'mod005');
INSERT INTO aula VALUES ('Video','35h','Arrays', 'aula006', 'Trabalhando com listas de valores', 80,'mod006');
INSERT INTO aula VALUES ('Texto','78h','Objetos', 'aula007', 'Classes, propriedades', 85,'mod007');
INSERT INTO aula VALUES ('Video','54h','Heran�a', 'aula008', 'Compartilhando comportamentos', 90,'mod008');
INSERT INTO aula VALUES ('Texto','57h','Interfaces', 'aula009', 'Contratos e implementacao', 80,'mod009');
INSERT INTO aula VALUES ('Texto','75h','Interpretacao da linguagem', 'aula010', 'Entendendo como o codigo e executado', 70,'mod010');

INSERT INTO certificado VALUES ('Introducao h� Programacao', 'Joao da Silva', 'Digital Signature Inc.', 30, '20220305', '20220301','cert001','Maria Souza','jsb1');
INSERT INTO certificado VALUES ('Python para Iniciantes', 'Ana Santos', 'CertSign', 40, '20220310', '20220306','cert002','Paulo Oliveira','htmlec1');
INSERT INTO certificado VALUES ('Desenvolvimento Web com JavaScript', 'Pedro Alves', 'GlobalSign',60, '20220315', '20220310','cert003','Lucas Souza','phpi1');
INSERT INTO certificado VALUES ('Algoritmos e Logica de Programacao', 'Maria Lima', 'DigiCert', 20, '20220320', '20220315','cert004','Jose Santos','exa1');
INSERT INTO certificado VALUES ('Java Avancado', 'Luiz Silva', 'Entrust Datacard', 80 , '20220325', '20220320','cert005','Roberto Oliveira','aad1');
INSERT INTO certificado VALUES ('PHP Bascio', 'Carla Santos', 'Comodo CA', 30, '20220401', '20220327','cert006','Marcelo Souza','pyad1');
INSERT INTO certificado VALUES ('SQL para Iniciantes', 'Fernando Lima', 'Symantec', 20, '20220405', '20220401','cert007','Paula Oliveira','jfx1');
INSERT INTO certificado VALUES ('C++ Avancado', 'Gabriela Almeida', 'Thawte', 60, '20220128', '20220228','cert008','Luciano Santos','unity1');
INSERT INTO certificado VALUES ('Java para Desenvolvimento Web', 'Aline Silva', 'Entrust Datacard', 50, '20220228', '20220215','cert009','Andrade Souza','react1');
INSERT INTO certificado VALUES ('Python Avancado', 'Felipe Rodrigues', 'CertSign', 70, '20220301', '20220220','cert010','Pedro Oliveira','prm1');

commit;