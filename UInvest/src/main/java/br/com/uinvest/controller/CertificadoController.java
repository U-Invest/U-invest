package br.com.uinvest.controller;

import com.lowagie.text.DocumentException;
import org.xhtmlrenderer.pdf.ITextRenderer;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

public class CertificadoController {
    public void gerarCertificado() throws IOException, DocumentException {
        String inputFile = "src/main/resources/certificadoTemplate.html";
        String outputFile = "src/main/resources/certificado.pdf";

        // Criar um objeto ITextRenderer
        ITextRenderer renderer = new ITextRenderer();

        // Configurar o arquivo de entrada
        renderer.setDocument(new File(inputFile));

        // Renderizar o documento
        renderer.layout();

        // Salvar o documento em um arquivo PDF
        try (FileOutputStream outputStream = new FileOutputStream(outputFile)) {
            renderer.createPDF(outputStream);
        }
    }
}
