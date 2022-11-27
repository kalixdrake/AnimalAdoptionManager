from userInterface.mainPage import MainPage
from BussinesLogic.Manager import Manager
from BussinesLogic.Filter import Filter

def main():
    
    """
    Creates the main window and initializes the application
    """
    
    filt = Filter()
    manager = Manager("resources/base1.csv",filt)
    page = MainPage(manager)

    page.mainloop()


if __name__ == "__main__":
    main()