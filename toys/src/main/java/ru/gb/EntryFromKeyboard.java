package ru.gb;

import java.util.Scanner;
public class EntryFromKeyboard {
    private final Scanner scanner = new Scanner(System.in);
    private StringBuilder data;

    public int inputId() {
        System.out.println("Введите id игрушки");
        return scanner.nextInt();
    }

    public int inputItemMenu() {
        System.out.println("Введите пункт меню");
        return this.scanner.nextInt();
    }

    public String inputToy() {
        this.data = new StringBuilder();
        System.out.println("Введите поля игрушки через пробел " +
                           "(id, имя, кол-во, частота выпадания)");

        for(int i = 0; i < 4; i++) {
            this.data.append(this.scanner.next());
            this.data.append(" ");
        }

        return this.data.toString();
    }

    public String inputFrequencyToy(){
        this.data = new StringBuilder();
        System.out.println("Введите id и частоту через пробел чтобы изменить");
        for(int i = 0; i < 2; i++) {
            this.data.append(this.scanner.next());
            this.data.append(" ");
        }

        return this.data.toString();
    }

}