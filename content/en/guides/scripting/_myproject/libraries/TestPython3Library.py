#! python3

from importlib import reload
from testmodule import riazi
reload(riazi)

print(riazi.add(21, 21))
print(riazi.numpy_random())