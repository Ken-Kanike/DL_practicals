# Experiment 10 - Deep Learning Case Studies Across Domains

[Notebook](../notebooks/10_dl_case_studies.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP10.docx) | [Back to README](../README.md)

## Aim

Analyse how CNNs, RNNs, and GANs are applied in healthcare, natural language
processing, autonomous vehicles, finance, and art, and connect the case studies
to compact hands-on demonstrations of each architecture family.

## Case-study scope

The original lab sheet is a written case study, not a single training
procedure. This repository preserves the analysis and adds small runnable
demos so the architectural ideas can be inspected in code.

| Domain | Architecture | Application | Reported impact | Main challenges |
|---|---|---|---|---|
| Healthcare | CNN | Skin-cancer image classification | Dermatologist-level accuracy on the reported task | Privacy, demographic generalization, regulation |
| NLP | LSTM + attention / Transformers | Tweet sentiment analysis | About 88% accuracy on a three-class task | Sarcasm, class imbalance, domain shift |
| Autonomous vehicles | CNN + RNN | Perception and path planning | Real-time detection and fleet learning | Long-tail scenarios, safety validation |
| Finance | RNN | Price forecasting with news sentiment | Improved short-horizon forecasts | Volatility, regime change, data quality |
| Art | GAN | Style transfer and image generation | Accessible creative tools | Copyright, attribution, subjective quality |

The full domain discussion is in the notebook.

## Demo datasets

| Demo | Dataset | URL |
|---|---|---|
| CNN | MNIST subset (12,000 train / 2,000 test) | `https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz` |
| RNN | IMDB subset (5,000 train / 2,000 test, 5,000-word vocabulary) | `https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz` |
| GAN | MNIST subset (12,000 images) | `https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz` |

No local dataset file is used. The IMDB word index is downloaded from the
official Keras URL for raw-text inference.

## Demo A - CNN image classification

- Architecture: Conv2D(16) -> pool -> Conv2D(32) -> pool -> Dense(64) ->
  Dense(10, softmax)
- Loss: sparse categorical cross-entropy
- Optimizer: Adam
- Epochs: 2
- Batch size: 128
- Input: 28x28x1 normalized to `[0, 1]`

The task is digit classification, used as a stand-in for a small grayscale
medical image. The demo reports a confusion matrix, per-class precision and
recall, and sample predictions.

## Demo B - RNN sentiment analysis

- Architecture: Embedding(5,000, 32) -> LSTM(32) -> Dense(1, sigmoid)
- Loss: binary cross-entropy
- Optimizer: Adam
- Epochs: 2
- Batch size: 128
- Sequence length: 200 tokens

The demo reports a confusion matrix, classification report, and raw-text
inference on custom reviews.

## Demo C - GAN image generation

- Generator: Dense(7x7x128) -> reshape -> Conv2DTranspose(64) ->
  Conv2DTranspose(1, tanh)
- Discriminator: Conv2D(64) -> Conv2D(128) -> Dense(1, logit)
- Loss: binary cross-entropy from logits
- Optimizers: Adam(1e-4, beta_1=0.5)
- Epochs: 8
- Batch size: 128
- Latent dimension: 100

The demo saves generated grids every two epochs, plots adversarial losses, and
generates digits for inference.

## Expected outcome

There is no single accuracy for the written case study. For the demos, expect:

- CNN: roughly 98% test accuracy after two epochs on 12,000 images.
- RNN: roughly 80-85% test accuracy after two epochs on 5,000 reviews.
- GAN: digit-like but blurry samples; adversarial losses are noisy and do not
  decrease monotonically.

These ranges are illustrative. The exact values depend on the random seed,
GPU/CPU differences, and library versions.

> **Execution status:** the notebook was syntax-checked and the CNN, RNN, and
> GAN model definitions and one GAN training step were smoke-tested during
> repository preparation. The full demo training runs were not performed
> locally. The case-study analysis is based on the original lab sheet and its
> references.

## Observations

- The CNN learns spatial features and is the easiest of the three demos to
  evaluate with standard classification metrics.
- The LSTM handles variable-length text after padding, but the small
  vocabulary and short schedule limit accuracy.
- The GAN is the most compute-intensive demo even though the images are tiny.
- GAN loss values are not a reliable quality metric; visual inspection and
  downstream evaluation are needed.
- Published systems operate at a very different scale from these teaching
  demos.
- Every domain raises data-quality, interpretability, robustness, and ethics
  questions; architecture alone does not determine success.

## Files and artifacts

- Notebook: `notebooks/10_dl_case_studies.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP10.docx`
- Runtime artifacts:
  - `outputs/exp10_demo_cnn.keras`
  - `outputs/exp10_demo_rnn.keras`
  - `outputs/exp10_gan_generator.keras`
  - `outputs/exp10_gan_discriminator.keras`
  - `outputs/exp10_demo_metrics.csv`
  - `outputs/exp10_cnn_confusion_matrix.png`
  - `outputs/exp10_cnn_predictions.png`
  - `outputs/exp10_rnn_confusion_matrix.png`
  - `outputs/exp10_gan_epoch_02.png` through `outputs/exp10_gan_epoch_08.png`
  - `outputs/exp10_gan_losses.png`
  - `outputs/exp10_gan_generated.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/10_dl_case_studies.ipynb`.
2. Use a GPU runtime. CPU execution is possible but slower.
3. Select **Runtime -> Run all**.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/10_dl_case_studies.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| GAN losses oscillate | Normal adversarial training behaviour | Inspect generated images, not only losses |
| Generated digits are noise | Too few epochs or unstable run | Train longer, lower the learning rate, or rerun with another seed |
| CNN or RNN accuracy is low | Data subset is small or training was interrupted | Increase the subset/epochs in the configuration cell |
| Out of memory | GAN batch too large for the GPU | Reduce `GAN_BATCH_SIZE` |
| IMDB download fails | Network or cache issue | Retry the data cell or clear `~/.keras/datasets/imdb.npz` |
| `pad_sequences` import error | Very old TensorFlow | Use TensorFlow 2.16+ as pinned in `requirements.txt` |

## Conclusion

The case studies show that architecture choice follows data structure and task
requirements: CNNs for images, RNNs/LSTMs for sequences, and GANs for
generation. The demos make the workflow concrete while also showing the gap
between a teaching example and a production system. Across every domain, the
recurring constraints are data quality, compute, interpretability, robustness,
and ethics.

**Previous:** [Experiment 9 - Optimizer Comparison on MNIST](09_optimizer_comparison_mnist.md) |
**Back to:** [All notes](README.md)
