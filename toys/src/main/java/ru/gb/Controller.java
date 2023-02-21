package ru.gb;

import ru.gb.manager.ManagerToys;
import ru.gb.menu.Menu;
import ru.gb.menu.MenuStore;
import ru.gb.reader.Reader;
import ru.gb.reader.ReaderFile;
import ru.gb.writer.WriterFile;


public class Controller {

    private EntryFromKeyboard entry;
    private Menu menu;
    private SwitchMenu switchMenu;

    public Controller() {
        this.entry = new EntryFromKeyboard();
        this.menu = new MenuStore();
        this.switchMenu = new SwitchMenu();
    }

    public void run () {
        menu.showMenu();
        int itemMenu = entry.inputItemMenu();

        while (itemMenu != 0) {
            switchMenu.selectMenu(entry, itemMenu);
            menu.showMenu();
            itemMenu = entry.inputItemMenu();
        }
    }
}

class SwitchMenu {
    private Reader reader;
    private WriterFile writer;
    private ManagerToys manager;
    private Raffler raffler;

    public SwitchMenu() {
        this.manager = new ManagerToys();
        this.reader = new ReaderFile();
        this.writer = new WriterFile();
        this.raffler = new Raffler();
    }

    public void selectMenu(EntryFromKeyboard entry, int item) {
        switch (item) {
            case 1 -> this.manager.putToy(entry.inputToy());
            case 2 -> this.manager.setFrequencyToy(entry.inputFrequencyToy());
            case 3 -> this.manager.remove(entry.inputId());
            case 4 -> this.manager.putToys(this.reader.read());
            case 5 -> {
                this.raffler.createLottery(this.manager.getToys());
                this.writer.write(this.manager.getToys().size());
            }
            case 6 -> this.writer.write(this.raffler.getToys());
        }
    }
}