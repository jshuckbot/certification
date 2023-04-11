package ru.gb.writer;

import java.io.FileWriter;
import java.io.IOException;
import ru.gb.Toy;

public class WriterFile implements Writer {
    private final String fileOutput;
    private int count = 1;
    public WriterFile() {
        this.fileOutput = "luckyToys.txt";
    }

    @Override
    public void write(Toy luckyToy) {
        if (luckyToy != null) {
            System.out.printf("Счасливая игрушка: %s\n",
                             luckyToy.getName());
            try (FileWriter writer = new FileWriter(this.fileOutput, true)) {
                writer.write(luckyToy.getName());
                writer.append('\n');
                writer.flush();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    public void write(int totalToys) {
        if (totalToys > 0) {
            try (FileWriter writer = new FileWriter(this.fileOutput, true)) {
                writer.write(String.format("Латерея №%d!\n", this.count++));
                //            writer.append('\n');
                writer.flush();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}