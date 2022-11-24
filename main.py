from mainPage import MainPage
from manager import Manager
from Filter import Filter

def main():
    filtro=Filter()
    manager=Manager("base1.csv",filtro)
    page = MainPage(manager)

    page.mainloop()

if __name__ == "__main__":
    main()

