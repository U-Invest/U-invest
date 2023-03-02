package service;

import org.mindrot.jbcrypt.BCrypt;

public class Criptografia {

    public static String criptografarSenha(String senha) {
        String senhaCriptografada = BCrypt.hashpw(senha, BCrypt.gensalt());
        return senhaCriptografada;
    }

    public static boolean verificarSenha(String senha, String senhaCriptografada) {
        boolean senhaValida = BCrypt.checkpw(senha, senhaCriptografada);
        return senhaValida;
    }
}
