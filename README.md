# thistothat
There are a bunch of empirical or modeled relations between various quantities for stars and other astrophysical objects. This package include a handy little wrapper for loading and interpolating those relations.


### Installation
To install, this simplest way is probably simply to install it directly via `pip` from any UNIX prompt:
```
pip install git+https://github.com/zkbt/thistothat
```

If you want to be able to modify the code yourself, please also feel free to fork/clone this repository onto your own computer and install directly from that editable package. For example, this might look like:
```
git clone https://github.com/zkbt/thistothat.git
cd thistothat/
pip install -e .
```
This will link the installed version of the `thistothat` package to your local repository. Changes you make to the code in the repository should be reflected in the version Python sees when it tries to `import thistothat`.


### Usage
For a slightly more detailed example, check out the `jupyter` notebook in the `notebooks/` folder. Here's a quick preview:

```
import matplotlib.pyplot as plt, numpy as np
from thistothat import Mamajek

m = Mamajek()
temperature = m.tofrom('Teff')('V-Ic')
vminusi = np.linspace(-1,5)

plt.plot(vminusi, temperature(vminusi))
plt.xlabel('$V-I_c$'); plt.ylabel("Temperature (K)")
plt.show();
```

### Authors
This wrapper was made by [Zach Berta-Thompson](http://casa.colorado.edu/~bertathompson/). The individual relations are drawn from the literature. If you use a particular relation, please be sure to cite the original reference for it, as indicated by the `.bibcode` attribute of that relation object.
