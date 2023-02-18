/*Relacionamento de Usuário com progresso*/
create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);


create table possui
(fk_progresso number(5) constraint possui_progresso_fk references progresso_curso,
fk_usuario char(11) constraint possui_usuario references usuario);


create table progresso_curso
(id_progresso number(5) constraint id_progresso_pk primary key,
experiencia number(7),
porcentagem number(4,2));


/*Relacionamento Usuario e contato*/


create table contato
(cd_msg char(8) constraint cd_msg_pk primary key,
mensagem varchar(150) constraint mensagem not null,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null);


create table solicita
(fk_usuario_cpf char(11) constraint possui_usuario references usuario,
fk_cd_msg char(8) constraint possui_contato references contato);



/*Relacionamento Usuario e cursos*/

create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);


create table cursos
(id_curso char(8) constraint id_curso_pk primary key,
duracao_curso data constraint drc_curso_,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);