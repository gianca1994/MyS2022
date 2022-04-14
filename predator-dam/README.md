## Welcome to Predator vs Dam


For the execution you must first read the file "INSTALL.md", once you have installed the libraries you must execute the file "main.py": ```python3 main.py```

- If desired, you can use the parameters ``-d or --dam``, to delimit the number of prey the model will have, ``-p or --predator`` for the number of predators, ``-c or --capcity``, for the size of the terrain and ``-w or --week`` to define the number of weeks the model will be simulated. Example:

1. ``python3 main.py -d 500 -p 10 -c 5000 -w 5``, generates a simulation of 500 prey, 10 predators, in a 5000-space terrain and for 5 weeks.
2. ``python3 main.py``, will generate a default simulation of: 500 prey, 10 predators, 5000 terrain slots and 1 week.

- Once the program is executed, it will generate a jpg file called "PredatorVsDam-Model.jpg" in the root of the directory "predator-dam" which will contain a graph detailing the simulation performed. 
