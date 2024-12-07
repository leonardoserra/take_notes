"""
    Questo modulo serve a creare o modificare o eliminare dei file txt,
    salva i file nella cartella './notes'
    è praticamente un block notes. Però volevo farlo 
    in python dato che è un sabato e sono a casa
"""

import os
import sys
import glob
import argparse


def main(args):

    # Check if folder exists or create one
    PATH = "./notes/"
    try:
        os.mkdir(PATH)
        print('Cartella "/notes" creata')

    except FileExistsError as e:
        pass

    # new file.
    if name := args.new:

        filename = f"{PATH}{name}.txt"
        mode = 'a'
        
        if name in get_filename_list(PATH):
            answer = input( f'Il file {name} esiste gia, vuoi sovrascriverlo? "y" | "n" ').lower()

            if answer and answer in ("y", "yes", "si", "s"):
                mode = 'w'

        with open(filename, mode) as note:
            note.writelines(input("Scrivi: \n"))

    # read
    elif name := args.read:
        if name in get_filename_list(PATH):
            filename = f"{PATH}{name}.txt"
            with open(filename, "r") as note:
                print(note.readlines())
        else:
            print("File non esistente, usa -l o --list per vedere la lista di note")

    # notes list
    elif args.list:
        l_names = get_filename_list(PATH)
        names = "- " + "\n- ".join(l_names)

        print(names)

    return 0


def get_filename_list(path):

    files = glob.glob(path + "*")
    names = [f.split("\\")[1][:-4] for f in files]

    return names if names else ["nessun file presente nella cartella"]


def cli():
    parser = argparse.ArgumentParser("notes")

    parser.add_argument(
        "-n",
        "--new",
        action="store",
        help="take in input the filename, Create new file, if the file exists it asks if you want to replace it or open the existing one",
    )
    parser.add_argument(
        "-r",
        "--read",
        action="store",
        help="take in input the filename, read it if exists it",
    )
    parser.add_argument(
        "-e",
        "--edit",
        action="store",
        help="take in input the filename, if it exists open it in edit mode, if not asks if you want to create a new one",
    )
    parser.add_argument(
        "-d", "--del", action="store", help="given a filename, deletes it."
    ),
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="gives the list of all the notes in the folder.",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = cli()
    code = main(args)
    sys.exit(code)
