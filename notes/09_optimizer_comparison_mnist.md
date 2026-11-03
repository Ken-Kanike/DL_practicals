# Experiment 9 - Gradient Descent Variants on MNIST

[Notebook](../notebooks/09_optimizer_comparison_mnist.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP09.docx) | [Back to README](../README.md)

## Aim

Compare six gradient-based optimizers on the same dense MNIST classifier and
measure how the optimizer affects convergence and test accuracy.

## Theory in brief

Gradient descent updates parameters in the direction that reduces the loss.
The variants differ in how they estimate and scale that update:

| Optimizer | Key idea |
|---|---|
| SGD | One sample per update; frequent but noisy |
| Mini-batch SGD | Average over a small batch; smoother and more stable |
| Momentum | Carries a fraction of the previous update |
| Nesterov | Looks ahead to the anticipated next position |
| Adagrad | Per-parameter rate scaled by accumulated squared gradients |
| Adam | Momentum plus adaptive second-moment scaling |

The network is the same in every run, so any difference in accuracy or
convergence is attributable to the optimizer and its batch size.

## Dataset

MNIST, downloaded at runtime from:

`https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz`

- 60,000 training images and 10,000 test images
- 28x28 grayscale, flattened to 784
- normalized to `[0, 1]`
- 48,000 train / 12,000 validation / 10,000 test in the full protocol

No local dataset file is used.

## Model

| Item | Value |
|---|---|
| Architecture | 784 -> 128 ReLU -> 64 ReLU -> 10 softmax |
| Loss | Sparse categorical cross-entropy |
| Optimizers | SGD, MiniBatch, Momentum, Nesterov, Adagrad, Adam |
| Epochs | 5 (full protocol) |
| Batch sizes | 1 for SGD; 32 for the others |
| Seed | 42 |

`FAST_DEV_RUN = True` reduces the data and epochs for a quick functional
check. Set it to `False` for the full experiment.

## Process

1. Download and normalize MNIST.
2. Split 48k train / 12k validation / 10k test.
3. Create fresh optimizer instances for each run.
4. Reset the seed before every model so all runs start from the same weights.
5. Train each optimizer for 5 epochs with its configured batch size.
6. Evaluate on the test set and record training time.
7. Plot validation loss and accuracy curves.
8. Compare test accuracy and training time in bar charts.
9. Select the best model, report its confusion matrix and per-class metrics.
10. Run inference on sample digits and save the best model.

## Expected outcome

The original lab sheet records:

| Optimizer | Test accuracy |
|---|---|
| SGD | 97.42% |
| Mini-Batch SGD | 94.46% |
| Momentum | 97.34% |
| Nesterov | 97.23% |
| Adagrad | 90.50% |
| Adam | 97.05% |

Momentum, Nesterov, and Adam are close to plain SGD in that run; Mini-Batch
SGD and Adagrad lag. The exact ordering can change with the library version,
the random seed, and the early stopping point, so compare the overall pattern
and the training curves rather than only the final decimals.

> **Execution status:** the notebook was syntax-checked and the model
> architecture was reviewed during repository preparation. The full
> six-optimizer training run was not performed locally. The table above is the
> outcome recorded in the original lab sheet.

## Observations

- Batch-size-1 SGD makes many small updates; it can be slow in wall-clock time
  even though each update is cheap.
- Mini-batch SGD with the default learning rate can underperform on this
  short schedule, which is why tuning the learning rate matters.
- Momentum and Nesterov smooth the trajectory and usually converge faster than
  plain mini-batch SGD.
- Adagrad's learning rate shrinks over time; on a short schedule it may not
  catch up.
- Adam is a strong default, but it is not automatically the best on every
  problem.
- Training time is not the same as convergence speed: a slow optimizer may
  still reach a good accuracy.

## Files and artifacts

- Notebook: `notebooks/09_optimizer_comparison_mnist.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP09.docx`
- Runtime model: `outputs/exp09_best_mnist_optimizer.keras`
- Runtime results: `outputs/exp09_optimizer_results.csv`
- Runtime plots:
  - `outputs/exp09_validation_curves.png`
  - `outputs/exp09_accuracy_and_time.png`
  - `outputs/exp09_best_confusion_matrix.png`
  - `outputs/exp09_sample_predictions.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/09_optimizer_comparison_mnist.ipynb`.
2. Use a GPU runtime for the full protocol. The batch-size-1 SGD run is the
   slowest part.
3. For a quick check, set `FAST_DEV_RUN = True` in the configuration cell.
4. Select **Runtime -> Run all**.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/09_optimizer_comparison_mnist.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| SGD takes very long | Batch size 1 and 48k samples per epoch | Use a GPU, reduce the subset, or set `FAST_DEV_RUN = True` |
| A bar is clipped | Accuracy below the y-axis limit | Widen the bar-chart limits; the printed table has the exact value |
| Accuracy differs from the lab sheet | Different TensorFlow version, seed, or early stopping | Compare the pattern across optimizers, not exact decimals |
| Out of memory | Unlikely for this dense model | Reduce the batch size or use a smaller subset |
| Best-model reload fails | Keras version mismatch | Use the same TensorFlow/Keras version for save and load |

## Conclusion

Optimizer choice affects both how quickly the network trains and how well it
generalizes within a fixed epoch budget. The experiment reinforces the value of
comparing optimizers empirically and of reporting training curves rather than
a single final accuracy.

**Previous:** [Experiment 8 - RNN Classification and Seq2Seq](08_rnn_imdb_seq2seq.md) |
**Next:** [Experiment 10 - Deep Learning Case Studies](10_dl_case_studies.md)
