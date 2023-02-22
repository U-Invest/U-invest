package repository;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class UsuarioRepository {
    private final String fileName = "users.json";

    public List<User> readUsers() {
        List<User> users = new ArrayList<>();
        ObjectMapper mapper = new ObjectMapper();
        try {
            users
