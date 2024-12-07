``` 
This module is used to create or modify or delete txt files.
Save the files in the './notes' folder.
It's basically a notepad. But I wanted to do it 
in python since it's a Saturday and I'm at home, a little exercise never hurts.

python -m notes --help

options:
  -h, --help                  show this help message and exit
  -n NEW, --new NEW           take in input the filename, Create new file, if the file exists it asks if you want to replace it or open the existing one
  -r READ, --read READ        take in input the filename, read it if exists it
  -e EDIT, --edit EDIT        take in input the filename, if it exists open it in edit mode, if not asks if you want to create a new one
  -rn RENAME, --rename RENAME take in input the filename, if it exists open it in edit mode, if not asks if you want to create a new one
  -d DELETE, --delete DELETE  given a filename, deletes it.
  -da, --delete_all           deletes all the notes.
  -l, --list                  gives the list of all the notes in the folder.
```

