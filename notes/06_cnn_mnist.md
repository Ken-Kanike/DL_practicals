# Experiment 6 - Convolutional Neural Network for MNIST Digit Recognition

[Notebook](../notebooks/06_cnn_mnist.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP06.docx) | [Back to README](../README.md)

## Aim

Build, train, and evaluate a convolutional neural network that classifies
handwritten digits from MNIST.

## Theory in brief

A CNN is designed for grid-structured data such as images. Convolutional
filters slide across the input and learn local features such as edges and
strokes. `relu` introduces nonlinearity, pooling reduces the spatial size and
adds translation tolerance, and the dense classifier head maps the learned
features to class probabilities. Dropout helps prevent overfitting, especially
in the dense layers. The final softmax layer produces a distribution over the
ten digits.

## Dataset

MNIST, downloaded at runtime from:

`https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz`

- 60,000 training images
- 10,000 test images
- 28x28 grayscale
- normalized to `[0, 1]`
- channel dimension added: `(28, 28, 1)`

No local dataset file is used.

## Architecture

| Stage | Layer | Details |
|---|---|---|
| Input | Image | 28 x 28 x 1 |
| Block 1 | Conv2D | 32 filters, 3x3, ReLU, same padding |
| Block 1 | MaxPooling2D | 2x2 |
| Block 2 | Conv2D | 64 filters, 3x3, ReLU, same padding |
| Block 2 | MaxPooling2D | 2x2 |
| Head | Flatten | 64 x 7 x 7 = 3136 features |
| Head | Dropout | 0.25 |
| Head | Dense | 128, ReLU |
| Head | Dropout | 0.5 |
| Output | Dense | 10, softmax |

- **Loss:** sparse categorical cross-entropy
- **Optimizer:** Adam (default learning rate)
- **Epochs:** 5
- **Batch size:** 128
- **Validation split:** 10%
- **Seed:** 42

## Process

1. Download MNIST from the explicit URL.
2. Normalize pixels and add the channel dimension.
3. Display sample digits.
4. Build the two-block CNN.
5. Train for 5 epochs with a best-model checkpoint and early stopping.
6. Evaluate on the 10,000-image test set.
7. Report per-digit precision, recall, and F1.
8. Plot the 10x10 confusion matrix.
9. Plot training and validation curves.
10. Display random predictions with confidence scores.
11. Display misclassified examples.
12. Run single-image inference and save the model.

## Expected outcome

The original lab sheet records **99.03% test accuracy** and a test loss near
**0.028** after 5 epochs. Most remaining errors should be visually ambiguous
digits (for example, 4/9 or 3/8 confusions).

> **Execution status:** the notebook was syntax-checked during repository
> preparation. The full training run was not performed locally. The numbers
> above are the outcome recorded in the original lab sheet; rerunning may
> produce slightly different values because of GPU nondeterminism and the
> validation split.

## Observations

- The CNN reaches very high accuracy quickly because convolution shares
  weights across the image and learns local stroke detectors.
- Dropout is important in the dense head; without it, the model can overfit
  the training set.
- Most errors are on digits that are genuinely ambiguous at 28x28 resolution.
- The model is small enough to train on a CPU, but a GPU reduces the run to a
  few minutes.
- The checkpoint and final model are both saved; the checkpoint contains the
  best validation-accuracy weights seen during training.

## Files and artifacts

- Notebook: `notebooks/06_cnn_mnist.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP06.docx`
- Runtime models:
  - `outputs/exp06_best_cnn.keras`
  - `outputs/exp06_mnist_cnn.keras`
- Runtime metrics: `outputs/exp06_metrics.csv`, `outputs/exp06_history.csv`
- Runtime plots:
  - `outputs/exp06_mnist_samples.png`
  - `outputs/exp06_confusion_matrix.png`
  - `outputs/exp06_training_curves.png`
  - `outputs/exp06_sample_predictions.png`
  - `outputs/exp06_misclassified.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/06_cnn_mnist.ipynb`.
2. Select **Runtime -> Change runtime type -> GPU** if available.
3. Select **Runtime -> Run all**.
4. The first run downloads MNIST automatically.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/06_cnn_mnist.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Test accuracy far below 99% | Missing channel dimension or unnormalized pixels | Keep `[..., None]` and divide by 255 |
| Training is very slow | Running on CPU | Use a Colab/Kaggle GPU runtime |
| Confusion matrix has no counts | Predictions or labels are one-hot | Use integer labels with sparse categorical cross-entropy |
| Checkpoint not created | `outputs/` directory absent | The setup cell creates it automatically |
| Reload warning | Keras version mismatch | Use the same TensorFlow version for save and load |

## Conclusion

The CNN solves MNIST with about 99% test accuracy, demonstrating the value of
convolution, pooling, and dropout for image classification. The experiment
also shows how to inspect errors with a confusion matrix and per-class
metrics rather than relying on a single accuracy number.

**Previous:** [Experiment 5 - Autoencoder Compression](05_autoencoder_compression.md) |
**Next:** [Experiment 7 - CIFAR-10 CNN](07_cnn_cifar10.md)
