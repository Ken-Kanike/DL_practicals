# Experiment 7 - CNN for CIFAR-10 with Data Augmentation

[Notebook](../notebooks/07_cnn_cifar10.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP07.docx) | [Back to README](../README.md)

## Aim

Build a deeper convolutional neural network for CIFAR-10 natural-image
classification, using data augmentation and dropout to improve generalization.

## Theory in brief

CIFAR-10 images are only 32x32, but the objects vary in pose, lighting,
background, and scale. A deeper CNN learns a hierarchy of features: early
filters detect edges and colour transitions, later filters detect textures and
object parts. Pooling reduces spatial resolution and adds tolerance to small
translations. Random flips and translations augment the training data, and
dropout prevents the dense head from memorizing the training set.

## Dataset

CIFAR-10, downloaded at runtime from:

`https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz`

- 50,000 training images
- 10,000 test images
- 32x32 colour images
- 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship,
  truck
- normalized to `[0, 1]`

The notebook parses the original Python pickle batches directly. No local
dataset file is used.

## Architecture

| Block | Layers |
|---|---|
| Input | 32 x 32 x 3 |
| Augmentation | Random horizontal flip; random translation (0.1, 0.1) |
| Block 1 | Conv2D 32 (3x3, ReLU) -> Conv2D 32 (3x3, ReLU) -> MaxPool -> Dropout 0.25 |
| Block 2 | Conv2D 64 (3x3, ReLU) -> Conv2D 64 (3x3, ReLU) -> MaxPool -> Dropout 0.25 |
| Block 3 | Conv2D 128 (3x3, ReLU) -> MaxPool -> Dropout 0.25 |
| Head | Flatten -> Dense 256 (ReLU) -> Dropout 0.5 -> Dense 10 (softmax) |

- **Loss:** sparse categorical cross-entropy
- **Optimizer:** Adam (default learning rate)
- **Epochs:** 15 (or 2 in `FAST_DEV_RUN` mode)
- **Batch size:** 128
- **Validation split:** 10%
- **Seed:** 42

## Process

1. Download and extract the CIFAR-10 tar archive from the explicit URL.
2. Locate the extracted `cifar-10-batches-py` directory robustly across Keras
   versions.
3. Unpickle the five training batches, the test batch, and the class metadata.
4. Reshape to `(32, 32, 3)`, normalize to `[0, 1]`, and verify shapes.
5. Display random training images with their class names.
6. Define the augmentation stack.
7. Build the three-block CNN.
8. Train with checkpointing, early stopping, and learning-rate reduction.
9. Evaluate on the 10,000-image test set.
10. Report per-class precision, recall, and F1 plus a confusion matrix.
11. Plot training curves, sample predictions, and misclassified images.
12. Run single-image inference and save the model.

## Expected outcome

The original lab sheet records **76.76% test accuracy** and a loss near
**0.67** after 15 epochs. Augmentation and dropout should make the model
generalize better than an unaugmented dense network, but CIFAR-10 remains
difficult at this model size; fine-grained confusions between cats/dogs and
automobiles/trucks are expected.

> **Execution status:** the notebook was syntax-checked, the CIFAR-10 pickle
> loader was smoke-tested on synthetic pickle files, and the model was
> forward-passed with random tensors during repository preparation. The full
> 15-epoch training run was not performed locally. The accuracy above is the
> outcome recorded in the original lab sheet.

## Observations

- Augmentation is especially important for CIFAR-10 because the dataset is
  small relative to the variety of natural images.
- `RandomTranslation` fills empty regions using reflection by default; this
  keeps the image size fixed.
- The deeper convolution stack increases capacity but also training time.
- Early stopping and learning-rate reduction make the 15-epoch budget more
  robust without changing the architecture.
- GPU acceleration is strongly recommended; a CPU run is possible but slow.

## Files and artifacts

- Notebook: `notebooks/07_cnn_cifar10.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP07.docx`
- Runtime models:
  - `outputs/exp07_cifar10_cnn.keras`
  - `outputs/exp07_best_cifar_cnn.keras`
- Runtime metrics: `outputs/exp07_metrics.csv`, `outputs/exp07_history.csv`
- Runtime plots:
  - `outputs/exp07_cifar_samples.png`
  - `outputs/exp07_confusion_matrix.png`
  - `outputs/exp07_training_curves.png`
  - `outputs/exp07_sample_predictions.png`
  - `outputs/exp07_misclassified.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/07_cnn_cifar10.ipynb`.
2. Select **Runtime -> Change runtime type -> GPU**.
3. Select **Runtime -> Run all**.
4. For a quick check, set `FAST_DEV_RUN = True` in the configuration cell.
   This uses 10,000 training images for 2 epochs.
5. The first run downloads about 170 MB of CIFAR-10 data.

### Kaggle

1. Import the notebook and enable **Internet**.
2. Select a GPU accelerator.
3. Run all cells.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/07_cnn_cifar10.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `FileNotFoundError: data_batch_1` | Extraction directory not found | Delete `~/.keras/datasets/cifar-10-python*` and rerun the download cell |
| Download is slow or fails | Large archive / no internet | Enable internet and retry; the file is cached after the first download |
| Accuracy stays near 10% | Labels misaligned or pixels not normalized | Re-run the loader; keep the `transpose(0, 2, 3, 1)` and `/255.0` steps |
| Out of memory | GPU memory too small for batch 128 | Reduce `BATCH_SIZE` to 64 |
| Runtime is very long | Running on CPU | Use a GPU runtime or `FAST_DEV_RUN = True` |
| Reload check fails | Different model checkpoint | Use the same TensorFlow/Keras version for save and load |

## Conclusion

The augmented CNN is a substantial improvement over a plain dense classifier
on CIFAR-10. It demonstrates how convolution, pooling, augmentation, and
dropout work together for natural-image classification. The lab sheet's
recorded accuracy of about 76.76% is the reference outcome; exact numbers
depend on hardware and the early-stopping point.

**Previous:** [Experiment 6 - CNN on MNIST](06_cnn_mnist.md) |
**Next:** [Experiment 8 - RNN Classification and Seq2Seq](08_rnn_imdb_seq2seq.md)
