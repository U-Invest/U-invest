package service;

import model.Usuario;
import org.mindrot.jbcrypt.BCrypt;
import repository.UsuarioRepository;

import java.util.ArrayList;
import java.util.List;

public class UsuarioService {

    private List<Usuario> usuarios = new ArrayList<>();
    private UsuarioRepository usuarioRepository;

    public UsuarioService(UsuarioRepository usuarioRepository) {
        this.usuarioRepository = usuarioRepository;
        this.usuarios = usuarioRepository.readUsers();
    }

    public void registerUser(Usuario usuario) {
        String hashedPassword = BCrypt.hashpw(usuario.getSenha(), BCrypt.gensalt());
        usuario.setSenha(hashedPassword);
        usuarios.add(usuario);
        usuarioRepository.writeUsers(usuarios);
    }

    public boolean authenticateUser(String email, String password) {
        User user = getUserByEmail(email);
        if (user != null) {
            return BCrypt.checkpw(password, user.getPassword());
        }
        return false;
    }

    private User getUserByEmail(String email) {
        for (User user : users) {
            if (user.getEmail().equals(email)) {
                return user;
            }
        }
        return null;
    }

}
