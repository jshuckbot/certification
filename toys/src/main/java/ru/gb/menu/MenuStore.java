package ru.gb.menu;

import java.util.HashMap;


public class MenuStore implements Menu{
    protected StringBuilder fieldsMenu;

    {
        fieldsMenu = new StringBuilder();
    }

    public MenuStore() {
        this.createMenu();
    }

    protected void createMenu() {
        this.fieldsMenu.append("1. Добавить игрушку в магазин\n");
        this.fieldsMenu.append("2. Изменить частоту выпадания игрушки для розыгрыша\n");
        this.fieldsMenu.append("3. Удалить игрушку из магазина\n");
        this.fieldsMenu.append("4. Выгрузить игрушки со склада\n");
        this.fieldsMenu.append("5. ЗАПУСК РОЗЫГРЫША игрушек\n");
        this.fieldsMenu.append("6. ПОЛУЧИТЬ ИГРУШКУ\n");
        this.fieldsMenu.append("0. Выход из приложения\n");
    }

    @Override
    public void showMenu() {
        System.out.println(this.fieldsMenu.toString());
    }
}