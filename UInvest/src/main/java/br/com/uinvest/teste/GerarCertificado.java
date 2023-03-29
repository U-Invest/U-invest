package br.com.uinvest.teste;

import br.com.uinvest.controller.CertificadoController;
import com.lowagie.text.DocumentException;

import java.io.IOException;

public class GerarCertificado {
    public static void main(String[] args) throws DocumentException, IOException {
        CertificadoController certificadoController = new CertificadoController();
        certificadoController.gerarCertificado();
    }
}

