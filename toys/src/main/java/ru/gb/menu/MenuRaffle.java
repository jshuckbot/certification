package ru.gb.menu;

public class MenuRaffle extends MenuStore{
    {
        super.fieldsMenu = new StringBuilder();
    }

    public MenuRaffle() {
        this.createMenu();
    }

    @Override
    protected void createMenu() {
        this.fieldsMenu.append("1. Разыграть игрушки\n");
        this.fieldsMenu.append("0. Выход из приложения\n");
    }
}