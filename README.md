# Check Text Resource

Check in text resource excel that all tags and variables needed still existing in all languages.

The programm will read your excel display all languages who needs to be corrected wtith an array of the tags and variables.

In this example the variable {TERMS} is translated:

```bash
Danish

['{VILKÅR}', '{PRIVACYPOLICY}', '<span id="addHref">', '</span>
```

In this example all tags and variables is removed (or the translation in Hebrew is missing):

```bash
Hebrew

[]
```

## Requirement

Python 3:
You can download from https://www.python.org/downloads/

## How to set up

After download the project and extrat it, open the second folder "CheckTextResource-main"
on vs code.

Install from the vs code terminal:

```bash
  py -m venv venv
```

Open the Command Prompt on windows:

```bash
  cd yourpath\CheckTextResource-main
  venv\Scripts\pip.exe install -r requirements.txt
```

Now you can run it and enjoy!
