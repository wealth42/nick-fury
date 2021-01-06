from pyomo.environ import *

model = AbstractModel()

# Teachers
model.T = Set()

# Student Batches
model.B = Set()

# Days
model.D = Set()

# Lectures
model.L = Set()

# Preferences of Teacher
model.P = Param(model.T, model.D, within=NonNegativeIntegers)

# Binary indicating if a teacher is teaching a batch on a day for a lecture
model.x = Var(model.B, model.D, model.L, model.T, within=Binary, initialize=0)


# Maximize the preference score
def score_rule(model):
    s = 0
    for i in model.B:
        for j in model.D:
            for k in model.L:
                for m in model.T:
                    # Multiplying preference of the teacher on that day with the boolean if teacher is teaching or not
                    s += model.P[m, j] * model.x[i, j, k, m]
    return s


model.score = Objective(rule=score_rule, sense=maximize)


# No empty time slots i.e. compulsory and only 1 teacher should be there for a time slot
def min_lecture_rule(model, batch, day, lecture):
    return sum(model.x[batch, day, lecture, i] for i in model.T) == 1


model.lecture_lower_limit = Constraint(model.B, model.D, model.L, rule=min_lecture_rule)


# No multiple classes for a teacher at the same time
def no_parallel_teaching_rule(model, day, lecture, teacher):
    return sum(model.x[i, day, lecture, teacher] for i in model.B) <= 1


model.parallel_teaching_limit = Constraint(model.D, model.L, model.T, rule=no_parallel_teaching_rule)


# Limit no more than 2 lectures by a teacher in a day for a class
def lectures_rule(model, batch, day, teacher):
    return sum(model.x[batch, day, i, teacher] for i in model.L) <= 2


model.lectures_limit = Constraint(model.B, model.D, model.T, rule=lectures_rule)


# Minimum number of lectures of a subject per batch
def subject_rule(model, batch, teacher):
    return sum(model.x[batch, i, j, teacher] for i in model.D for j in model.L) >= 5


model.subjects_limit = Constraint(model.B, model.T, rule=subject_rule)

# The code below is just to visualize the result as a time table
# We can just comment the code below and run the following command in the terminal

# pyomo solve --solver=glpk main.py main.dat

# This will generate the output in results.yml where there is solving info and the solution is in the form boolean values.
# In my view, Visualization by code below is a little bit better.


from pyomo.opt import SolverFactory
import pandas as pd

opt = SolverFactory('glpk')

# Reading in a datafile
instance = model.create_instance('main.dat')

# Can also load another dat file instead of the above file with Saturday included here
# instance = model.create_instance('another.dat')

results = opt.solve(instance, tee=True)
results.write()
instance.solutions.load_from(results)

v = instance.component('x')

# result_d is a dictionary with key-value pair like # ('Batch1', 'Monday', 'lecture1', 'teacher1') = 1
result_d = v.extract_values()


# Creating a nested dictionary so as to convert to pandas Dataframe easily. It is of the form
# result_pa_d = {
#                   'Batch1': {
#                       'lecture1': {
#                           'Monday': 'teacher2',
#                           'Tuesday': 'teacher5',
#                               ... },
#                       'lecture2': {..}
#                       ...},
#                   'Batch2': {...},
#                   'Batch3': {..}
#                }
result_pa_d = {}

for key, value in result_d.items():
    if value == 0:
        continue
    if key[0] not in result_pa_d:
        result_pa_d[key[0]] = {key[2]: {key[1]: key[3]}}
    elif key[2] not in result_pa_d[key[0]]:
        result_pa_d[key[0]][key[2]] = {key[1]: key[3]}
    else:
        result_pa_d[key[0]][key[2]][key[1]] = key[3]

# Converting into DataFrame and printing
time_table = {}
for key, value in result_pa_d.items():
    time_table[key] = pd.DataFrame(value)
    print(key)
    print(time_table[key])
    print("=="*30)
