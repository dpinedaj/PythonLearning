#%%
from functools import partial

#%%
def func(a, b):
    print(a, b)

#%%

from multiprocessing.pool import ThreadPool

with ThreadPool(processes=3) as tp:
    tp.map(partial(func, b="mundo"), ["hola", "chao", "ciao"])
# %%

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as tp:
    tp.map(partial(func, b="mundo"), ["hola", "chao", "ciao"])
# %%
