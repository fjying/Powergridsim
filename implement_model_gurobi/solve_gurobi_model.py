import time

# Set Gurobi Solving Model Status
mipgap = 0.01
threads = 9

model.Params.MIPGap = mipgap
model.Params.Threads = threads

# logfile = '/Users/jf3375/Desktop/Gurobi/output'
# model.Params.LogFile = logfile
# model.Params.OutputFlag = 1

solvemodel_start_time = time.time()
model.optimize()
print('solvemodel_time', time.time()- solvemodel_start_time)

# Tune the Model
model.Params.TuneCriterion = 2
# Increase the number of tuning trials to control the randomness of MIP models
model.Params.TuneTrials = 100
model.Params.TuneResults = 1
model.tune()
for i in range(model.tuneResultCount):
    model.write('Tune_UnitCommitment.prm'.format(i))

# Output and Read the Current Model Parameter File to set Model Parameters
model.read('Tune_UnitCommitment.prm')

solvemodel_start_time = time.time()
model.optimize()
print('solvemodel_time', time.time()- solvemodel_start_time)


# if model.status == 4:
#     model.Params.DualReductions = 0
#     model.optimize()
#     print(model.status)
#     if model.status == 3:
#         # drop binary constraints
#         model_relax = model.relax()
#         model_relax.optimize()
#         print(model_relax.status)
