# Data policy

No datasets are stored in this repository. Every notebook downloads its data
from a public URL at runtime and lets TensorFlow/Keras cache it under
`~/.keras/datasets/` (or the platform equivalent).

## Datasets used

| Dataset | Used in | Source URL | Runtime cache |
|---|---|---|---|
| MNIST | Experiments 5, 6, 9, 10 | https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz | `~/.keras/datasets/mnist.npz` |
| CIFAR-10 | Experiment 7 | https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz | `~/.keras/datasets/cifar-10-python.tar.gz` |
| IMDB reviews | Experiments 8, 10 | https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz | `~/.keras/datasets/imdb.npz` |
| IMDB word index | Experiments 8, 10 | https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json | `~/.keras/datasets/imdb_word_index.json` |
| Iris | Experiment 2 | https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv | pandas URL cache (in memory) |

Synthetic data for Experiments 1, 3, 4, and the sequence-reversal task in
Experiment 8 is generated deterministically in the notebook, so no download
is needed.

## Notes

- TensorFlow's `get_file` verifies the official Keras-hosted files against
  their published hashes where available.
- Review the original dataset pages for license and usage terms before
  redistributing derived data.
- To clear a corrupted cache, delete the relevant file under
  `~/.keras/datasets/` and rerun the data-loading cell.
- Do not commit downloaded files. `.gitignore` excludes common dataset and
  archive formats.
