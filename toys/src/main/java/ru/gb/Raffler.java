package ru.gb;


import java.util.ArrayList;


public class Raffler {
    private Raffle raffle;

    public Raffler() {
        raffle = new Raffle();
    }

    public void createLottery(ArrayList<Toy> toys) {
        if (this.raffle.getQueueLuckyToys().isEmpty()) {
            System.out.println("Розыгрыш запущен!\n");
            if (toys.size() > 0)
                this.checkTotalToys(toys);
            else
                System.out.println("В магазине нет игрушек!\n");
        } else
            System.out.println("Очередь еще не пуста! Получите приз!!\n");
    }

    private void checkTotalToys(ArrayList<Toy> toys) {
        for (Toy toy : toys) {
            this.raffle.setToyOfQueue(toy);
            toy.decrement();
        }

    }
    
    public Toy getToys() {
        Toy luckyToy = null;
        if (this.raffle.getQueueLuckyToys().size() != 0)
            luckyToy = this.raffle.getLuckyToy();
        else
            System.out.println("Запустите розыгрыш!\n");

        return luckyToy;
    }
}