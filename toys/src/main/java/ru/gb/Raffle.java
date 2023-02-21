package ru.gb;

import java.util.ArrayList;
import java.util.PriorityQueue;

/**
 * лотерея
 *
 */
public class Raffle {
    private PriorityQueue<Toy> luckyQueue = new PriorityQueue<>();

    public void setToyOfQueue(Toy luckyToy) {
        this.luckyQueue.add(luckyToy);
    }

    public ArrayList<Toy> getQueueLuckyToys() {
        return new ArrayList<>(this.luckyQueue);
    }
    
    public Toy getLuckyToy() {
        return luckyQueue.poll();
    }
}