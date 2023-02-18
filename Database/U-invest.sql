
create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email varchar(50) constraint email_pk not null,
nome varchar(50) constraint nome_pk_nn not null,
senha varchar(30) constraint senha_ck_nn unique);

create table progresso_curso
(id_progresso number(5) constraint id_progresso_pk primary key,
experiencia number(7) constraint exp_curso,
);








