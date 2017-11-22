# thistothat
There are a bunch of empirical or modeled relations between various quantities for stars and other astrophysical objects. This package include a handy little wrapper for loading and interpolating those relations.


### Installation
To install, feel free to fork/clone this repository and install it into you local Python library via the command
```
python setup.py install
```
from the main `thistothat/` repository directory.

You should also be able to install it directly via `pip` with
```
pip install git+https://github.com/zkbt/thistothat
```
from any UNIX prompt.


### Usage
For a slightly more detailed example, check out the `jupyter` notebooks in the `notebooks/` folder. Here's a quick preview:

```
import matplotlib.pyplot as plt, numpy as np
from thistothat import Mamajek

m = Mamajek()
temperature = m.tofrom('Teff')('V-Ic')
vminusi = np.linspace(-1,5)

plt.plot(vminusi, temperature(vminusi))
plt.xlabel('$V-I_c$'); plt.ylabel("Temperature (K)");
```

### Authors
This wrapper was make by [Zach Berta-Thompson](http://casa.colorado.edu/~bertathompson/). The individual relations are drawn from the literature. If you use a particular relation, please be sure to cite the original reference for it, as indicated by the `.bibcode` attribute of that relation object.
