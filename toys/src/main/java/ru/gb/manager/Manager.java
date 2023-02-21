package ru.gb.manager;

import java.util.ArrayList;
import java.util.HashMap;
import ru.gb.Toy;

public abstract class Manager {
    protected HashMap<Integer, Toy> toys;

    {
        toys = new HashMap<>();
    }

    public abstract void putToys(String data);
    public abstract ArrayList<Toy> getToys();
    public abstract void remove(int id);
}