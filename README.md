``` 
Questo modulo serve a creare o modificare o eliminare dei file txt,
salva i file nella cartella './notes'
è praticamente un block notes. Però volevo farlo 
in python dato che è un sabato e sono a casa

python -m notes --help

options:
  -h, --help            show this help message and exit
  -n NEW, --new NEW     take in input the filename, Create new file, if the file exists it asks if you want to replace it or open the existing one
  -r READ, --read READ  take in input the filename, read it if exists it
  -e EDIT, --edit EDIT  take in input the filename, if it exists open it in edit mode, if not asks if you want to create a new one
  -d DEL, --del DEL     given a filename, deletes it.
  -l, --list            gives the list of all the notes in the folder.
```

