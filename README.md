# AirBnB Clone - The Console

This project is the first step towards building a full web application: the AirBnB clone. It involves creating a command interpreter to manage AirBnB objects.

## Command Interpreter

### How to Start It
```bash
./console.py

How to Use It
The command interpreter works in both interactive and non-interactive modes. In interactive mode, you can type commands, and in non-interactive mode, you can provide commands via input redirection.

Example

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$

Description of the Project
BaseModel: The base class for all models.
FileStorage: Handles serialization and deserialization of all the models.
Console: The command interpreter.
Usage
The command interpreter supports the following commands:

create <ClassName>
show <ClassName> <id>
destroy <ClassName> <id>
all <ClassName>
update <ClassName> <id> <attribute_name> <attribute_value>
