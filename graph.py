import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl
from matplotlib import interactive
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Create data
df = pd.read_csv('stats.csv')
y = df['Rapid Rating']
x= df['Puzzle Rating']
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)



# Plot
mpl.scatter(x, y)
mpl.plot(x, slope*x+intercept, 'r')
mpl.title('Rapid Rating vs Puzzle Rating')
mpl.xlabel('Puzzle Rating')
mpl.ylabel('Rapid Rating')
mpl.show()

mpl.hist(y, bins = 25)
mpl.show()


#OLS Model
# model = ols('Q("Rapid Rating") ~ Q("Puzzle Rating")', data=df).fit()
# print(model.summary())
# anova_results = anova_lm(model)
# print('\nANOVA results')
# print(anova_results)