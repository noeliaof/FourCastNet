import h5py
import numpy as np
from functools import reduce

# Open the original HDF5 file
with h5py.File('/storage/workspaces/giub_hydro/hydro/data/Global_hourly/out_of_sample/2021_orig.h5', 'r') as f_in:
    # Get the shapes of each dataset
    shapes = [dset.shape for dset in f_in.values()]

    # Get the number of samples, which should be the same for each variable
    n_samples = shapes[0]
    print(n_samples)
    # Create a new HDF5 file
    with h5py.File('/storage/workspaces/giub_hydro/hydro/data/Global_hourly/out_of_sample/2021.h5', 'w') as f_out:
        # Create a new dataset in the output file
        # shape = (n_samples,) + reduce(lambda x, y: x + y, [shape[1:] for shape in shapes])
        shape = ( 1460, 21, 721, 1440 )  #/ ( 1460, 21, 721, 1440 )
        dset_out = f_out.create_dataset('fields', shape=shape, dtype='f')

        # Concatenate the arrays along the first axis
        offset = 0
        for dset in f_in.values():
            dset_out[:, offset:offset+dset.shape[1], ...] = dset[:]
            offset += dset.shape[1]

        # Add any necessary attributes to the new dataset
        # ...

        # Close the output file
        f_out.close()

    # Close the input file
    f_in.close()
