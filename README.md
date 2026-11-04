# Deep Learning Practicals

A public, reproducible collection of ten deep learning practicals built from
the lab sheets in [`docs/`](docs/). Each experiment has a standalone Jupyter
notebook, a linked Markdown note, and a runtime that downloads public data from
its canonical URL.

[![validate](https://github.com/Ken-Kanike/DL_practicals/actions/workflows/validate.yml/badge.svg)](https://github.com/Ken-Kanike/DL_practicals/actions/workflows/validate.yml)

## Highlights

- **10 standalone notebooks** for Google Colab, Kaggle, or local Jupyter.
- **No local datasets and no credentials.** Data is downloaded at runtime.
- **No secrets or model artifacts committed.** `.env`, datasets, notebooks
  outputs, and model weights are ignored.
- **Per-experiment notes** with aims, theory, expected results, observations,
  run instructions, and troubleshooting.
- **Automated checks** for notebook JSON/syntax, saved outputs, and accidental
  secrets.

## Experiments

| # | Practical | Notebook | Notes | Reference result |
|---|---|---|---|---|
| 1 | XOR with a multi-layer perceptron | [Notebook](notebooks/01_xor_mlp.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/01_xor_mlp.ipynb) | [Notes](notes/01_xor_mlp.md) | 100% XOR accuracy |
| 2 | Deep learning libraries overview | [Notebook](notebooks/02_libraries_overview.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/02_libraries_overview.ipynb) | [Notes](notes/02_libraries_overview.md) | Conceptual comparison |
| 3 | Single-layer network optimizer comparison | [Notebook](notebooks/03_single_layer_optimizers.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/03_single_layer_optimizers.ipynb) | [Notes](notes/03_single_layer_optimizers.md) | ~99.75% accuracy, loss 0.01-0.05 |
| 4 | Deep feed-forward network for multiclass classification | [Notebook](notebooks/04_deep_ffn_multiclass.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/04_deep_ffn_multiclass.ipynb) | [Notes](notes/04_deep_ffn_multiclass.md) | ~96.67% accuracy, loss ~0.07 |
| 5 | Autoencoder for data compression | [Notebook](notebooks/05_autoencoder_compression.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/05_autoencoder_compression.ipynb) | [Notes](notes/05_autoencoder_compression.md) | Test MSE ~0.0137; 24.5x compression |
| 6 | CNN for MNIST classification | [Notebook](notebooks/06_cnn_mnist.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/06_cnn_mnist.ipynb) | [Notes](notes/06_cnn_mnist.md) | 99.03% accuracy, loss ~0.028 |
| 7 | CNN for CIFAR-10 classification | [Notebook](notebooks/07_cnn_cifar10.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/07_cnn_cifar10.ipynb) | [Notes](notes/07_cnn_cifar10.md) | 76.76% accuracy, loss ~0.67 |
| 8 | RNN sentiment analysis and seq2seq | [Notebook](notebooks/08_rnn_imdb_seq2seq.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/08_rnn_imdb_seq2seq.ipynb) | [Notes](notes/08_rnn_imdb_seq2seq.md) | IMDB ~86%; reversal ~99.87% |
| 9 | Gradient descent variants on MNIST | [Notebook](notebooks/09_optimizer_comparison_mnist.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/09_optimizer_comparison_mnist.ipynb) | [Notes](notes/09_optimizer_comparison_mnist.md) | SGD 97.42%, Adam 97.05%, Adagrad 90.50% |
| 10 | Deep learning case studies across domains | [Notebook](notebooks/10_dl_case_studies.ipynb) · [Colab](https://colab.research.google.com/github/Ken-Kanike/DL_practicals/blob/main/notebooks/10_dl_case_studies.ipynb) | [Notes](notes/10_dl_case_studies.md) | Case study plus CNN/RNN/GAN demos |

The reference values are the outcomes recorded in the original lab sheets.
Exact numbers depend on library versions, seeds, and hardware. Every notebook
prints its own metrics when run.

## Repository structure

```text
DL_practicals/
├── .github/workflows/validate.yml   # CI: notebook + secret checks
├── data/README.md                   # dataset policy and source URLs
├── docs/                            # original lab sheets (read-only)
├── notebooks/                       # 10 standalone experiment notebooks
├── notes/                           # one Markdown note per experiment
├── scripts/
│   ├── check_for_secrets.py         # scans tracked text files
│   └── validate_notebooks.py        # JSON, syntax, output hygiene
├── .env.example                     # optional integration placeholders
├── .gitignore
├── LICENSE
├── README.md
├── SECURITY.md
└── requirements.txt
```

## Quick start

### Google Colab (recommended)

Open any **Colab** link in the table above, choose a GPU runtime
(**Runtime -> Change runtime type -> T4 GPU**), and select **Runtime -> Run
all**. The notebook downloads its data automatically.

### Local

```bash
git clone https://github.com/Ken-Kanike/DL_practicals.git
cd DL_practicals

python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

Then open a notebook from `notebooks/`. A CUDA GPU is optional; the notebooks
run on CPU but take longer.

### Kaggle

Upload the `.ipynb` file, enable a GPU accelerator, and run all cells. No
Kaggle dataset attachment is needed.

## Datasets

All data is public and downloaded at runtime. Nothing is stored in the
repository.

| Dataset | Used in | Source |
|---|---|---|
| MNIST | Experiments 5, 6, 9, 10 | [mnist.npz](https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz) |
| CIFAR-10 | Experiment 7 | [cifar-10-python.tar.gz](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) |
| IMDB reviews | Experiments 8, 10 | [imdb.npz](https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz) |
| IMDB word index | Experiments 8, 10 | [imdb_word_index.json](https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json) |
| Iris | Experiment 2 | [iris.csv](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv) |

Experiments 1, 3, and 4 generate synthetic data deterministically; Experiment
8 also generates a synthetic sequence-reversal corpus. See
[`data/README.md`](data/README.md) for cache locations and licensing notes.

## Reproducibility

- Random seeds are set in every notebook.
- Data splits and preprocessing are explicit in code.
- Notebook outputs are not saved, so results cannot be mistaken for committed
  evidence.
- Each note records the execution status for that experiment.
- The CI workflow validates notebook JSON and Python syntax and scans for
  likely secrets.

Full training runs were not executed while preparing the repository. Run the
notebooks end-to-end to reproduce the metrics shown in the notes.

## Validation

```bash
python scripts/validate_notebooks.py
python scripts/check_for_secrets.py
```

Both scripts are run by [`.github/workflows/validate.yml`](.github/workflows/validate.yml)
on every push and pull request.

## Security and privacy

- No API keys, tokens, passwords, private keys, or personal data are committed.
- `.env` is ignored; [`.env.example`](.env.example) contains empty optional
  placeholders only.
- All datasets are public and URL-based.
- Model files, downloaded data, and notebook outputs are ignored.
- Report security concerns through GitHub's private security advisory flow;
  see [`SECURITY.md`](SECURITY.md).

## Notebook and note conventions

Every notebook follows the same structure:

1. Title, aim, objectives, and dataset URLs
2. Environment setup and imports
3. Data loading and exploratory checks
4. Model definition with shape summaries
5. Training with validation metrics
6. Evaluation with plots and a classification report or reconstruction metrics
7. Inference on new or held-out samples
8. Saving artifacts to the ignored `outputs/` directory
9. Conclusion
10. Next/previous links

Every note follows the same structure: aim, short theory, dataset, process,
expected outcome, observations, files, how to run, troubleshooting, conclusion,
and experiment navigation.

## Documentation index

- [Notebook index](notebooks/README.md)
- [Notes index](notes/README.md)
- [Lab-sheet index](docs/README.md)
- [Data policy](data/README.md)
- [Security policy](SECURITY.md)

## Requirements

- Python 3.10-3.12
- TensorFlow 2.16-2.20 (Keras 3)
- PyTorch 2.2+ for the library comparison in Experiment 2
- NumPy, pandas, Matplotlib, scikit-learn
- JupyterLab or Google Colab/Kaggle

Install with:

```bash
pip install -r requirements.txt
```

## License

Released under the [MIT License](LICENSE). The original lab sheets in `docs/`
remain the work of their authors.

## Author

**Junaid Shaikh** · [GitHub: Ken-Kanike](https://github.com/Ken-Kanike)

If you find an error or have a suggestion, open an issue on the
[repository](https://github.com/Ken-Kanike/DL_practicals/issues).
