import os

name = "sambo"

if __name__ == "__main__":
    os.system("pyside2-uic " + name + ".ui -o " + "ui_sambo" + ".py")
