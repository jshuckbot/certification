package ru.gb.manager;

import ru.gb.Toy;
import java.util.ArrayList;

public class ManagerToys extends Manager {

    @Override
    public void putToys(String data) {
        for (String line : data.split(";")) {
            Toy toy = createToy(line);
            this.updateToys(toy);
        }
        System.out.println("Игрушки выгружены со склада\n");
    }

    public void putToy(String line) {
        Toy toy = createToy(line);
        super.toys.put(toy.getId(), toy);
    }

    private Toy createToy(String line) {
        String[] parseLine = line.split(" ");
        int id = Integer.parseInt(parseLine[0].strip());
        String name = parseLine[1];
        int total = Integer.parseInt(parseLine[2].strip());
        int frequency = Integer.parseInt(parseLine[3].strip());
        return new Toy(id, name, total, frequency);
    }

    @Override
    public void remove(int id) {
        if (super.toys.containsKey(id))
            super.toys.remove(id);
        else
            System.out.println("Игрушки с таким id не существует!\n");

    }

    public void setFrequencyToy(String line) {
        String[] parseLine = line.split(" ");
        int id = Integer.parseInt(parseLine[0].strip());
        int frequency = Integer.parseInt(parseLine[1].strip());

        if (super.toys.containsKey(id)) {
            Toy getToy = super.toys.get(id);
            getToy.setFrequency(frequency);
            super.toys.replace(id, getToy);
        } else
            System.out.println("Игрушки с таким id не существует!\n");
    }

    public ArrayList<Toy> getToys() {
        ArrayList<Toy> correntToys = new ArrayList<>();
        for (Toy toy : super.toys.values())
            if (toy.getTotal() > 0)
                correntToys.add(toy);
        
        return correntToys;
    }

    public void updateToys(Toy uploadToys) {
        super.toys.put(uploadToys.getId(), uploadToys);
    }
}