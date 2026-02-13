from os import path, mkdir, listdir
from shutil import copytree, rmtree

def main():
    if path.exists("public"):
        rmtree("public")
    copytree("static", "public")


if __name__ == "__main__":
    main()
