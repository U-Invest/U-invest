CREATE TABLE usuario (
    email VARCHAR2(50),
    nome  VARCHAR2(50),
    senha VARCHAR2(20),
    cpf   CHAR(11)
        CONSTRAINT user_cpf_pk PRIMARY KEY
);

CREATE TABLE progresso_curso (
    id_progresso number(3),
    experiencia number(4),
    porcentagem number(2)
);

create table login (
email,
senha
);

create table login