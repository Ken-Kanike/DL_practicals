# Notebooks

Ten standalone practicals. Open a notebook in Colab, Kaggle, or local Jupyter
and run all cells. Data is downloaded from public URLs at runtime; no local
dataset is required.

| # | Notebook | Practical | Colab |
|---|---|---|---|
| 1 | [01_xor_mlp.ipynb](01_xor_mlp.ipynb) | XOR classification with a multi-layer perceptron | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/01_xor_mlp.ipynb) |
| 2 | [02_libraries_overview.ipynb](02_libraries_overview.ipynb) | Comparison of TensorFlow/Keras, PyTorch, and scikit-learn | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/02_libraries_overview.ipynb) |
| 3 | [03_single_layer_optimizers.ipynb](03_single_layer_optimizers.ipynb) | Single-layer network with different optimizers | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/03_single_layer_optimizers.ipynb) |
| 4 | [04_deep_ffn_multiclass.ipynb](04_deep_ffn_multiclass.ipynb) | Deep feed-forward multiclass classifier | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/04_deep_ffn_multiclass.ipynb) |
| 5 | [05_autoencoder_compression.ipynb](05_autoencoder_compression.ipynb) | Autoencoder for data compression | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/05_autoencoder_compression.ipynb) |
| 6 | [06_cnn_mnist.ipynb](06_cnn_mnist.ipynb) | CNN for MNIST digit classification | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/06_cnn_mnist.ipynb) |
| 7 | [07_cnn_cifar10.ipynb](07_cnn_cifar10.ipynb) | CNN for CIFAR-10 classification with augmentation | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/07_cnn_cifar10.ipynb) |
| 8 | [08_rnn_imdb_seq2seq.ipynb](08_rnn_imdb_seq2seq.ipynb) | IMDB sentiment analysis and sequence-to-sequence reversal | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/08_rnn_imdb_seq2seq.ipynb) |
| 9 | [09_optimizer_comparison_mnist.ipynb](09_optimizer_comparison_mnist.ipynb) | SGD, MiniBatch, Momentum, Nesterov, Adagrad, and Adam on MNIST | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/09_optimizer_comparison_mnist.ipynb) |
| 10 | [10_dl_case_studies.ipynb](10_dl_case_studies.ipynb) | Domain case studies with CNN, RNN, and GAN demos | [Open](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/10_dl_case_studies.ipynb) |

## How to run

### Colab

1. Open a Colab link above.
2. Select **Runtime -> Change runtime type -> T4 GPU** for the training-heavy
   notebooks.
3. Select **Runtime -> Run all**.

### Local

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate
pip install -r ../requirements.txt
jupyter lab
```

## Runtime notes

- Experiments 1-4 are fast on CPU.
- Experiments 5-7 and 9 benefit from a GPU; CPU runs are supported.
- Experiment 8 trains an LSTM and a small seq2seq model; a GPU is recommended.
- Experiment 10 trains a CNN, an LSTM, and a small GAN; use a GPU for the
  quickest run.
- Outputs are written to `outputs/` relative to the notebook working
  directory. That directory is ignored by Git.

## Notebook format

Notebooks are stored without execution outputs so the repository stays small
and results are always reproduced locally. See the root
[README](../README.md) for the full documentation map and
[notes/](../notes/) for the written record of each experiment.
