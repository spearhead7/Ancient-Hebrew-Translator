# %%
from tf.app import use
import pandas as pd
A = use("etcbc/bhsa", hoist=globals())

# %%
#Get all words with dual ending
query = """ 
word
 g_cons~JM$ nu=du gloss*
"""

results = A.search(query)
A.show(results, end=10)
# A.table(results, condensed=True, condenseType="phrase", end=5)

#example for putting data into DataFrame
# section = [T.sectionFromNode(w) for w in F.otype.s('word') if F.uvf.v(w) == 'H']
# word = [F.g_cons.v(w) for w in F.otype.s('word') if F.uvf.v(w) == 'H']

# pd.DataFrame(zip(section, word))

# %% goes to downloads folder
A.export(results)
# %%
data = pd.read_csv('~/downloads/results.tsv', encoding='utf16', sep='\t')

data.loc[data['gloss1'] == '<space between>']
# %%
# Edit some gloss entries

data['gloss1'].replace(to_replace ="<space between>",
                 value ="double space", inplace=True)
                 
data.loc[data['gloss1'] == 'double space']

# %%

data['gloss1'].value_counts()[:]

# %%
#plot by gloss word

df = data['gloss1'].value_counts()[:].plot(kind='barh', log=True, figsize=(20, 10))

df.set_xlim((0, 360)) #set to highest count
df.set_xlabel("Count")
df.set_ylabel("Dual Word")

# %%
