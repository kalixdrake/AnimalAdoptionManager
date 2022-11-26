from mainPage import MainPage
from manager import Manager
from Filter import Filter

def main():
    filt=Filter()
    manager=Manager("base1.csv",filt)
    page = MainPage(manager)

    page.mainloop()

if __name__ == "__main__":
    main()