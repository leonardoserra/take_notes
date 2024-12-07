"""
    This module is used to create or modify or delete txt files.
    Save the files in the './notes' folder.
    It's basically a notepad. But I wanted to do it 
    in python since it's a Saturday and I'm at home, a little exercise never hurts.
"""

import os
import sys
import glob
import shutil
import argparse


def main(args: argparse.Namespace):

    # if some error exit code is 1 exit_program_dirty(e)
    try:
        # Check if folder exists or create one
        NOTES_DIR = "./notes/"
        CONFIRM = ("y", "yes", "si", "s")
        NOT_FOUND_MSG = (
            "File not found, use 'python -m notes -l' to check the list of notes"
        )

        try:
            os.mkdir(NOTES_DIR)
            print('Folder "/notes" created')

        except FileExistsError as e:
            pass

        # new file.
        if name := args.new:

            file_path = f"{NOTES_DIR}{name}.txt"
            mode = "a"

            if name in get_filename_list(NOTES_DIR):
                answer = input(
                    f'Name "{name}" already exists, want to overwrite it? "y" | "n" '
                ).lower()

                if answer is not None and answer in CONFIRM:
                    mode = "w"

                else:
                    answer = input(
                        f'Do you want to edit note "{name}"? "y" | "n" '
                    ).lower()

                    if answer is not None and answer in CONFIRM:
                        read_note(file_path)
                        edit_note(file_path)
                        print("Note Edited: \n")
                        read_note(file_path)

                        return exit_program_clean()

                    else:
                        return exit_program_clean()

            create_note(file_path, mode)
            print("Note Saved: \n")
            read_note(file_path)

        # edit file.
        elif name := args.edit:

            file_path = f"{NOTES_DIR}{name}.txt"

            if name not in get_filename_list(NOTES_DIR):
                answer = input(
                    f'File "{name}" not exists, want to create it? "y" | "n" '
                ).lower()

                print(answer)

                if answer is not None and answer not in CONFIRM:
                    return exit_program_clean()

            read_note(file_path)
            edit_note(file_path)
            print("Note Edited: \n")
            read_note(file_path)

        # read
        elif name := args.read:

            if name in get_filename_list(NOTES_DIR):
                file_path = f"{NOTES_DIR}{name}.txt"
                read_note(file_path)

            else:
                print(NOT_FOUND_MSG)

        # delete
        elif name := args.delete:

            if name in get_filename_list(NOTES_DIR):
                file_path = f"{NOTES_DIR}{name}.txt"
                answer = input(
                    f'Are you sure to delete {name}? File can\'t be restored after deletion. "y" | "n" > '
                )

                if answer is not None and answer in CONFIRM:
                    delete_note(file_path)

            else:
                print(NOT_FOUND_MSG)

        # delete folder and all notes
        elif args.delete_all:

            answer = input(
                f'Are you sure to delete EVERY file? Files can\'t be restored after deletion. "y" | "n" > '
            )

            if answer is not None and answer in CONFIRM:
                delete_folder(NOTES_DIR)

            if not get_filename_list(NOTES_DIR):
                print("All files has been deleted!")

        # notes list
        elif args.list:

            l_names = get_filename_list(NOTES_DIR)
            names = "- " + "\n- ".join(l_names)

            print(names)

        return exit_program_clean()

    except BaseException as e:
        print(e)

        return exit_program_dirty(e)


def create_note(file_path: str, mode: str = "w") -> None:

    with open(file_path, mode) as note:
        note.writelines(input("Write your text: \n> "))
        note.write("\n")


def edit_note(file_path: str) -> None:

    with open(file_path, "a") as note:
        note.writelines(input("Write your text: \n> "))
        note.write("\n")


def read_note(file_path: str) -> None:

    with open(file_path, "r") as note:
        print("\n")
        lines = note.readlines()
        print("".join(lines))


def delete_note(file_path: str) -> None:

    os.remove(file_path)
    print(f"{file_path} deleted from the notes.")


def delete_folder(dir_path: str) -> None:

    shutil.rmtree(dir_path)


def exit_program_clean() -> int:

    print("Program exited.")
    return 0


def exit_program_dirty(error: BaseException) -> int:

    print(f"Program exited with errors. {error}")
    return 1


def get_filename_list(path: str) -> list[str]:

    files = glob.glob(path + "*")
    names = [f.split("\\")[1][:-4] for f in files]

    return names if names else ["Empty folder!"]


def cli() -> argparse.Namespace:

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
        "-rn",
        "--rename",
        action="store",
        help="take in input the filename, if it exists open it in edit mode, if not asks if you want to create a new one",
    )
    parser.add_argument(
        "-d", "--delete", action="store", help="given a filename, deletes it."
    ),
    parser.add_argument(
        "-da", "--delete_all", action="store_true", help="deletes all the notes."
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
