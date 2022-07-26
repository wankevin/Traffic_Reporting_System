import os

name = "sambo_upload_info"

if __name__ == "__main__":
    os.system("pyside2-uic " + name + ".ui -o " + name + ".py")
