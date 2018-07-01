# PODEM
ATPG system
ECE 6140
Language : Python 3
Interpreter : Python 3.5.4
Compiler: PyCharm Community Edition 2017.2.3
How to run the code:

1)	Use Command prompt to run the code.
2)	If possible put all the test circuit, fault_list text files in the same path as the code.
3)	Use the following line to run any circuit file:

python “PODEMv1.py” /path/testcircuit.txt /path/Output.txt /path/Inputvectors.txt /path/FaultList.txt /path/InputVectorsforDeductive.txt

Example line for running s27.txt test circuit having all text files in same directory will look like:

python PODEMv1.py s27.txt Outputs27.txt InpVectors27.txt fault_list27.txt Dedinpvec27.txt

Note: Only test circuit and fault list filenames should be exact. Other filenames can be whatever the user wishes.
4)	After program execution, 3 text files will open which will show PODEM results, Input vectors to detect the given faults in fault_list and the input vectors to test the faults in Deductive fault simulator.
