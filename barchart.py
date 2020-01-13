#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

index = np.arange(5)
bar_width = 0.35

filename = 'multiensembletime'
fftime  = [10172.57, 33427.12,0,0,0]
rftime  = [ 902.88, 20864.30,0,0,0]
data1 = fftime
data2 = rftime 



fig, ax = plt.subplots(figsize=(16,13))

ff = ax.bar(index, data1, bar_width,label="Full features",color = "black")
rf = ax.bar(index+bar_width, data2,bar_width,label="Reduced features",color = "grey")

ax.set_xlabel('Datasets',fontsize=20)
ax.set_ylabel('Execution \n time  \n (seconds)', rotation=0, fontsize=20, labelpad=50)
#ax.set_ylabel('Accuracy  \n Percentage \n (%)', rotation=0, fontsize=20, labelpad=50)
ax.set_xticks(index + bar_width /2)

#ax.set_xticklabels(['Random \n Forest','Neural \n Network \n Model','Gaussian \n Naive \n Bayes','Logistic \n Regression','Linear \n Discriminant \n Analysis'],fontsize=17)
#ax.set_xticklabels(['Support Vector Machine \n'],fontsize=17)

#ax.set_xticklabels(['Average Binary classification \n'],fontsize=17)

#ax.set_xticklabels(['-4', '-2' , '0', '2', '4 \n'],fontsize=17)

#ax.set_xticklabels(['Multiclass \n (CICIDS2017)','Multiclass \n (KDD CUP 99)\n'],fontsize=17)
ax.set_xticklabels(['Average Binary \n classification','Multiclass \n (CICIDS2017)\n','Multiclass \n (KDD CUP 99)\n'],fontsize=17)
ax.legend(fontsize=15)

plt.show()
fig.savefig(filename)