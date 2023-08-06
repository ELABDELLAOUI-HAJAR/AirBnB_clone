<p align="center">
   <img src="/images/hbnb_logo.png" alt="AirBnb Clone logo"
	width="720" height="300"/>
</p>

# Team Project AirBnb Clone
Hbnb: HolbertonBnb is AirBnb Clone, a complete web application that composed by :
 - A Command interpreter to manipulate data without a visual interface.
 - A website (the Front-end) that shows the final product to everybody: static and dynamic.
 - A database or files that store data.
 - An API that provides a communication interface between the front-end and data (retrieve, create, delete, update them).

In this project, we will start implementing the first part: The console.

# Execution

The shell is executed in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

Also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb) 
$
```

# Tests

Launch tests:
```
python3 -m unittest discover tests
```

All tests should also pass in non-interactive mode: 
```
$ echo "python3 -m unittest discover tests" | bash
```

# Authors :
- **HAJAR EL ABDELLAOUI** <[ELABDELLAOUI-HAJAR](https://github.com/ELABDELLAOUI-HAJAR)>
- **YASSINE AIT MENSOUR** <[aitmensouryassine](https://github.com/aitmensouryassine)>
