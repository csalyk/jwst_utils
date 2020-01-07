# jwst_utils
Some utility functions for JWST prep and analysis

# Requirements

## Functions
get_miri_mrs_wavelengths provides wavelength ranges of MIRI MRS subbands

get_miri_mrs_resolution provides resolution of MIRI MRS based on Wells et al. 2015, Table 1

## Usage
```python
from jwst_utils import get_miri_mrs_wavelengths
print(get_miri_mrs_wavelengths('3A'))

from jwst_utils import get_miri_mrs_resolution
print(get_miri_mrs_resolution('3A',14.9))
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

