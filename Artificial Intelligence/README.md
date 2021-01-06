first install the packages required i.e. mainly pyomo and pandas.<br>

`pip install -r requirements.txt`

Also, make sure you download GLPK solvers from <a href="https://sourceforge.net/projects/winglpk/files/winglpk/GLPK-4.55/winglpk-4.55.zip/download">here.</a><br>
Extract the folder, you will have a folder named 'w64'. Add this folder to your 'PATH' environment variable.

main.dat contains the data required for the task.<br>
another.dat also contains the data have 6 days in a week including 'Saturday'.<br>

### Given Assumptions
1. A teacher cannot teach more than 2 classes to a batch in a day.
2. All the batches should have at least 5 lectures of each subject.

### My Assumptions
1. Given 5 teachers and 5 different subject they are specialized in. Hence, each teacher teaches one subject. (teacher and subject is one to one related).
2. Each time slot should be occupied compulsorily by only one teacher.
3. A teacher cannot have multiple classes at once. (No clubbed classes)

main.py has the main code to load the data and solve it.<br>
We can also comment the code from line no 79 and run the following command line code.

`pyomo solve --solver=glpk main.py main.dat` or<br>
`pyomo solve --solver=glpk main.py another.dat`

This will create 'results.yml' with solution.
<br>

The code from line 79 does some visualization using pandas. (_I think this visualization looks better_)

So, just run the main.py file and check out the output.
