/*Relacionamento de Usuário com progresso*/
create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email_usuario varchar(50) constraint email_uk unique
constraint email_nn not null,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn not null);


create table possui
(fk_progresso number(5) constraint possui_progresso_fk 
references progresso_curso,
fk_usuario char(11) constraint possui_usuario references usuario);


create table progresso_curso
(id_progresso number(5) constraint id_progresso_pk primary key,
experiencia number(7),
porcentagem number(4,2));





/*Relacionamento Usuario e contato*/

/*create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);*/


create table contato
(cd_msg char(8) constraint cd_msg_pk primary key,
mensagem varchar(150) constraint mensagem not null,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null);


create table solicita
(fk_usuario_cpf char(11) constraint possui_usuario references usuario,
fk_cd_msg char(8) constraint possui_contato references contato);



/*Relacionamento Usuario e cursos*/

/*create table usuario
(cpf char(11) constraint id_cpf_nn primary key,
email_usuario varchar(50) constraint email_uk_nn unique not null,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);*/


create table cursos
(id_curso number(5) constraint id_curso_pk primary key,
duracao_curso data constraint drc_curso_,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);

create table realiza
(fk_id_curso number(5) constraint realiza_cursos references cursos,
fk_usuario char(11) constraint realiza_usuario references usuario);



/*Relacionamento de Módulo com cursos*/


/*create table cursos
(id_curso number(5) constraint id_curso_pk primary key,
duracao_curso data constraint drc_curso_,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);*/

create table modulo
(cd_mdl number(5) constraint cd_mdl_pk prim
nm_mdl varchar(50) constraint nome_modulo not null,
desc_mdl varchar(150));

create table possui
fk_cd_modulo number(5) constraint possui_modulo references modulo
fk_id_curso number(5) constraint possui_cursos references cursos



/*Relacionamento Cursos e Certificado*/


/*create table cursos
(id_curso number(5) constraint id_curso_pk primary key,
duracao_curso data constraint drc_curso_,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);*/

create table certificado
(cd_certificado number(5) constraint cd_certf_pk primary key
nome_certificado var char(50) constraint nm_certf_nn not null
score number(4,1)) constraint score_nn not null;

create table gera
(fk_id_curso number(5) constraint gera_curso references curso
fk_cd_certificado number(5) gera_certificado references certificado);



/*Relacionamento Usuario com Simullacao de investimento*/


/*create table cursos
(id_curso number(5) constraint id_curso_pk primary key,
duracao_curso data constraint drc_curso_,
nome_usuario varchar(50) constraint nome_pk_nn not null,
senha_usuario varchar(30) constraint senha_ck_nn unique);*/


create table simulacao_investimento
(id_simulacao number(5) constraint id_simu_pk primary key,
tipo varchar(20) constraint tipo_simulacao_nn not null,
taxa_juros number(4,1) constraint tx_juros_nn not null,
duracao data constraint drc_dt_nn);

create table solicita
(fk_usuario_ char(11) constraint solicita_usuario references usuario,
fk_simulacao varchar(20) constraint solicita_simulacao 
references simulacao_investimento);


/*Relacionamento Simulador Investimento e Simulacao Investimento*/



/*create table simulacao_investimento
(id_simulacao number(5) constraint id_simu_pk primary key,
tipo varchar(20) constraint tipo_simulacao_nn not null,
taxa_juros number(4,1) constraint tx_juros_nn not null,
duracao data constraint drc_dt_nn);*/


create table simulador_investimento
(id_simulador number(5) constraint id_simulador_pk primary key
tipo varchar(20) constraint tipo_simulador_nn not null,
resultado_estimado number(8,2) constraint rlt_est_nn not null,
progresso number(4,1));


create table simula
(fk_simulacao_investimento number(5) constraint simula_simulacao 
references simulacao_investimento,
fk_simulador_investimento number(5) constraint simula_simulador
references simulador_investimento);



