# Experiment 4 - Deep Feed-Forward Network for Multi-Class Classification

[Notebook](../notebooks/04_deep_ffn_multiclass.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP04.docx) | [Back to README](../README.md)

## Aim

Design and train a fully connected deep neural network with two hidden layers
for three-class classification, and inspect its decision regions and confusion
matrix.

## Theory in brief

A deep feed-forward network stacks Dense layers, each followed by a nonlinear
activation. The hidden layers learn intermediate representations, and the
final softmax layer converts three logits into a probability distribution over
the classes. Training minimizes sparse categorical cross-entropy, which is
the multi-class extension of binary cross-entropy for integer labels. Adam
adapts the learning rate per parameter and is a strong default for small
networks.

## Dataset

Synthetic three-class Gaussian blobs generated in the notebook:

| Class | Centre | Spread | Points |
|---|---|---|---|
| blob_0 | (-2.0, 0.0) | 0.8 | 300 |
| blob_1 | (2.0, 0.0) | 0.8 | 300 |
| blob_2 | (0.0, 2.5) | 0.8 | 300 |

The classes overlap slightly, so the task is not perfectly separable. No
external dataset is used.

## Process

1. Generate 900 points from the three Gaussian distributions.
2. Shuffle the rows and visualize the blobs.
3. Split into 70% train, 15% validation, and 15% test, stratified by class.
4. Build the 2 -> 16 ReLU -> 16 ReLU -> 3 softmax network.
5. Compile with Adam (learning rate 0.01) and sparse categorical
   cross-entropy.
6. Train for 200 epochs with batch size 32.
7. Evaluate on the held-out test split.
8. Report the confusion matrix and per-class precision/recall/F1.
9. Plot loss and accuracy curves.
10. Visualize the learned decision regions over the full input plane.
11. Run inference on individual points and on random test rows.
12. Save the model and metrics.

## Model summary

| Item | Value |
|---|---|
| Architecture | 2 -> 16 ReLU -> 16 ReLU -> 3 softmax |
| Parameters | 339 |
| Loss | Sparse categorical cross-entropy |
| Optimizer | Adam, learning rate 0.01 |
| Epochs / batch | 200 / 32 |
| Split | 70% train / 15% validation / 15% test |
| Seed | 42 |

## Expected outcome

The original lab sheet reports about **96.67% accuracy** and a test loss near
**0.07** after 200 epochs. Most errors should occur near the boundaries where
the Gaussian clouds overlap. The notebook's confusion matrix makes those
boundary errors visible.

> **Execution status:** the notebook was syntax-checked during repository
> preparation. The full training run was not performed locally. The numbers
> above are the outcome recorded in the original lab sheet; rerunning may
> produce slightly different values because of the random split and library
> version.

## Observations

- Two hidden layers are enough to create curved decision boundaries around the
  three blobs.
- The softmax output always sums to 1, so the model's confidence can be read
  directly from the largest probability.
- Errors are concentrated between the closer class pairs; the confusion
  matrix is more informative than a single accuracy number.
- Adam with a moderate learning rate converges quickly on this small problem;
  a longer run mainly reduces boundary noise.

## Files and artifacts

- Notebook: `notebooks/04_deep_ffn_multiclass.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP04.docx`
- Runtime model: `outputs/exp04_deep_ffn.keras`
- Runtime metrics: `outputs/exp04_metrics.csv`
- Runtime plots:
  - `outputs/exp04_blobs.png`
  - `outputs/exp04_confusion_matrix.png`
  - `outputs/exp04_training_curves.png`
  - `outputs/exp04_decision_regions.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/04_deep_ffn_multiclass.ipynb`.
2. Select **Runtime -> Run all**. CPU is enough.
3. The full run should take well under a minute.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/04_deep_ffn_multiclass.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Accuracy near 33% | Output layer or loss mismatch | Use 3 softmax outputs and sparse categorical cross-entropy with integer labels |
| One class is always predicted | Learning rate too high or training interrupted | Restart the kernel and rerun; keep Adam at 0.01 |
| Confusion matrix looks transposed | Rows are true labels, columns are predictions | Read the axis labels in the plot |
| Reprojection points fall outside the grid | Inference point far from the training range | The plot is clipped to the data range; numerical prediction still works |

## Conclusion

The 2-16-16-3 deep network learns the three-class problem and produces a
sensible set of decision regions. The experiment confirms that a fully
connected network with nonlinear hidden layers, a softmax output, and a
categorical cross-entropy loss is a standard solution for multi-class
classification.

**Previous:** [Experiment 3 - Single-Layer Optimizers](03_single_layer_optimizers.md) |
**Next:** [Experiment 5 - Autoencoder Compression](05_autoencoder_compression.md)
