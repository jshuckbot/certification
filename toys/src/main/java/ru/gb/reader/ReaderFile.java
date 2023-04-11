package ru.gb.reader;

import java.io.FileReader;
import java.io.IOException;

public class ReaderFile implements Reader {
    private final String fileInput;
    private final StringBuilder data;

    public ReaderFile() {
        this.fileInput = "toys.txt";
        this.data = new StringBuilder();
    }

    @Override
    public String read() {
        int nextChar;
        try (FileReader fileReader = new FileReader(this.fileInput)){

            while ((nextChar = fileReader.read()) != -1) {
                this.data.append((char) nextChar);
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        
        return this.data.toString();
    }
}