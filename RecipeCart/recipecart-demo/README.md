# RecipeCart Demo
This folder contains an executable build of the RecipeCart backend server (`CSE-403-RecipeCart-1.0-SNAPSHOT.jar`) along with a script to demonstrate its functionality (`demo_script.py`).

## Running the Demo
First, run the executable JAR file to start up the backend server. This can be done by running `java -jar CSE-403-RecipeCart-1.0-SNAPSHOT.jar -f demo_entities.ser` in the same directory as this file. (Optionally, you can also run `java -jar CSE-403-RecipeCart-1.0-SNAPSHOT.jar -h` to see all command line arguments.)

Then, in another terminal, run `python demo_script.py > output.txt`, which will send some HTTP requests to the server to perform its functionalities. A file named `demo_entities.ser`, which stores information about recipes, users, etc., will be created if it doesn't already exist. Details of the requests made will be outputted to `output.txt`.

You can also run the demo script again (e.g. `python demo_script.py > output2.txt`), and the HTTP responses will be different due to recipes, etc. already being stored by the server, even if the server is stopped (typing "quit" into the terminal and pressing enter will gracefully stop the server) and started again.

## Environment
Java is required to run the executable JAR file. Python 3 is required to run the demo script. More details on obtaining the JAR file are in `developer_manual.md` in the RecipeCart repository, under ["How to build the software"](https://github.com/jteng2/CSE-403-RecipeCart/blob/main/developer_manual.md#how-to-build-the-software).