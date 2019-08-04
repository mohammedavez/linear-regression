import pandas as pd

df = pd.read_csv('studentsanswers.csv')
print(df)
xbar = df.correct.mean()
ybar = df.attitude.mean()
stdy = df.attitude.std()
stdx = df.correct.std()
corr = df['correct'].corr(df['attitude'])
slope = (corr*stdy)/stdx
yintercept = ybar - (slope*xbar)


y = yintercept + (slope*17)
x=(94-yintercept)/slope
print(y,x)