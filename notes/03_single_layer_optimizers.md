# Experiment 3 - Single-Layer Feed-Forward Network with Six Optimizers

[Notebook](../notebooks/03_single_layer_optimizers.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP03.docx) | [Back to README](../README.md)

## Aim

Train a single-layer feed-forward neural network for binary classification and
compare six gradient-based optimizers: SGD, mini-batch SGD, Momentum,
Nesterov, Adagrad, and Adam.

## Theory in brief

A single sigmoid neuron is the simplest feed-forward classifier. It computes a
weighted sum of the inputs plus a bias, passes the result through a sigmoid,
and is trained by minimizing binary cross-entropy. The optimizer determines
how the gradient is turned into a parameter update:

| Optimizer | Update idea |
|---|---|
| SGD | One sample per step; fast but noisy |
| Mini-batch SGD | Average gradient over a small batch; more stable |
| Momentum | Adds a fraction of the previous update to the current one |
| Nesterov | Looks ahead to the anticipated next position before computing the gradient |
| Adagrad | Per-parameter learning rate from accumulated squared gradients |
| Adam | Momentum plus adaptive second-moment scaling with bias correction |

## Dataset

A synthetic linearly separable dataset is generated in the notebook:

- 400 points drawn from a standard normal distribution,
- label 1 when `x0 + 2*x1 + 0.5 > 0`, otherwise 0,
- 75% train / 25% test split, stratified by class.

No local dataset or download is needed.

## Process

1. Generate the 2D data and verify its shape and class balance.
2. Plot the training points and the true linear boundary.
3. Build a fresh single Dense sigmoid unit for each optimizer.
4. Use the same seed before every model so all runs start from the same
   initial weights.
5. Train each model for 200 epochs with the batch size and learning rate from
   the lab sheet.
6. Record training time, train loss/accuracy, and test loss/accuracy.
7. Plot loss curves and the six learned decision boundaries.
8. Compare test accuracy in a bar chart.
9. Select the best test model and run inference on individual points.
10. Save the best model and the results CSV.

## Optimizer configurations

| Run | Learning rate | Batch size | Extra settings |
|---|---|---|---|
| SGD | 0.5 | 1 | None |
| Mini-batch SGD | 0.5 | 32 | None |
| Momentum | 0.1 | 32 | `momentum=0.9` |
| Nesterov | 0.1 | 32 | `momentum=0.9`, `nesterov=True` |
| Adagrad | 0.5 | 32 | Default accumulator |
| Adam | 0.05 | 32 | Default beta values |

## Expected outcome

The original lab sheet reports approximately **99.75% accuracy** for all six
optimizers, with losses between **0.01 and 0.05**. Because the dataset is
linearly separable and the model has only three parameters, every optimizer
should reach a high accuracy; the interesting differences are in convergence
speed and stability, not the final ceiling.

> **Execution status:** the notebook was syntax-checked during repository
> preparation. The full six-optimizer training run was not performed locally.
> The numbers above are the outcome recorded in the original lab sheet; a
> rerun may differ slightly because of TensorFlow version and mini-batch
> ordering.

## Observations

- Batch-size-1 SGD takes many more parameter updates than the other runs, but
  each update is cheap. Its loss curve is noisier.
- Momentum and Nesterov smooth the trajectory and usually converge in fewer
  effective steps than plain mini-batch SGD.
- Adagrad's per-parameter rates shrink over time; on an easy problem this can
  make the final approach slower.
- Adam is typically the most reliable default when no tuning is done.
- On a linearly separable problem, all six variants eventually find a good
  boundary; a non-separable dataset would separate them more clearly.

## Files and artifacts

- Notebook: `notebooks/03_single_layer_optimizers.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP03.docx`
- Runtime results: `outputs/exp03_optimizer_results.csv`
- Runtime model: `outputs/exp03_best_single_layer.keras`
- Runtime plots:
  - `outputs/exp03_dataset.png`
  - `outputs/exp03_optimizer_losses.png`
  - `outputs/exp03_decision_boundaries.png`
  - `outputs/exp03_accuracy_comparison.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/03_single_layer_optimizers.ipynb`.
2. Select **Runtime -> Run all**. CPU is sufficient.
3. Expect roughly half a minute to a minute of training time.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/03_single_layer_optimizers.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| One optimizer stays near 50% | Learning rate far too large or too small | Use the exact configurations in the notebook |
| Training is slow | Batch-size-1 SGD creates many small steps | Reduce `N` or `EPOCHS` for a quick check; keep the defaults for the reported protocol |
| Results differ from the lab sheet | Different library version, GPU nondeterminism, or data generation order | Compare the pattern (all high accuracy), not exact decimals |
| Decision-boundary plot is clipped | `ax.set_ylim` in the bar chart is narrow | Widen the limits if an optimizer underperforms in your run |

## Conclusion

All six optimizers can train a single sigmoid neuron on a linearly separable
problem. The experiment demonstrates the trade-off between update frequency,
stability, and adaptivity, and it motivates the optimizer comparisons on a
harder dataset in Experiment 9.

**Previous:** [Experiment 2 - Deep Learning Libraries](02_libraries_overview.md) |
**Next:** [Experiment 4 - Deep Feed-Forward Network](04_deep_ffn_multiclass.md)
