package ru.gb;

public class Toy implements Comparable<Toy>{
    private final int id;
    private final String name;
    private int total;
    private int frequency;

    public Toy(int id, String name, int total, int frequency) {
        this.id = id;
        this.name = name;
        this.total = total;
        this.frequency = frequency;
    }

    @Override
    public String toString() {
        return String.format("id: %d; игрушка %s; количество: %d; вес: %d;",
                             this.id, this.name, this.total, this.frequency);
    }

    @Override
    public int compareTo(Toy o) {
        return Integer.compare(o.frequency, this.frequency);
    }

    public int getTotal() {
        return total;
    }
    
    public void decrement() {
        --this.total;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}