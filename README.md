# faces_scrape

the main file to get all those saucy emails from faces

DON'T FORGET TO:
1. Install the browser driver into the browser's application directory AND write the driver's path in the code (line 28). [Further instructions can be found here.](https://selenium-python.readthedocs.io/installation.html#drivers)
2. Write your login and password on lines 43-44.
3. Create a directory called "out" in the same directory as the script. (I don't know how to create new folders in Python)
4. Change the name of the output file as needed (line 90).

Some notes when you're running the script:
1. You will be prompted for DUO authentication, with a 10 second window for you to pick up your phone and log in.
2. The output is in `.csv` format, with duplicates, so you'll have to remove duplicates in another program like Excel.
3. This program searches for two-letter strings starting with 'aa,' 'ab,' etc. You can start "halfway" through the alphabet if you need to (for instance, if your Internet crashes) by changing the arrays in lines 56-57.
