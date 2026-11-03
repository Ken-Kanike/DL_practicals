# Experiment 1 - XOR Gate using a Multilayer Perceptron

[Notebook](../notebooks/01_xor_mlp.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP01.docx) | [Back to README](../README.md)

## Aim

Implement the XOR logic gate with a multilayer perceptron and show that a
network with a nonlinear hidden layer can learn a function that is not
linearly separable.

## Theory in brief

XOR outputs 1 only when its two binary inputs differ. No single straight line
can separate the `(0,0)` and `(1,1)` rows from `(0,1)` and `(1,0)`, so a
single-layer perceptron cannot solve XOR. An MLP adds a hidden layer whose
nonlinear activation creates an internal representation where the classes
become separable. The network is trained end-to-end with backpropagation.

## Dataset

The XOR truth table is created directly in the notebook:

| A | B | XOR |
|---|---|-----|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

No URL or local dataset file is required.

## Process

1. Set seeds for Python, NumPy, and TensorFlow.
2. Define the four XOR input rows and encoded targets.
3. Build a 2-4-1 MLP:
   - input: 2 features,
   - hidden: 4 units with `tanh`,
   - output: 1 unit with `sigmoid`.
4. Compile with Adam (`learning_rate=0.05`) and binary cross-entropy.
5. Train for 1000 epochs with batch size 4.
6. Evaluate loss, accuracy, and the predicted probability for every row.
7. Plot the loss and accuracy curves.
8. Run inference through a small `predict_xor(a, b)` helper.
9. Save the model to `outputs/exp01_xor_mlp.keras` and reload it to verify
   that predictions are identical.

## Model summary

| Item | Value |
|---|---|
| Architecture | 2 -> 4 (`tanh`) -> 1 (`sigmoid`) |
| Parameters | 17 |
| Loss | Binary cross-entropy |
| Optimizer | Adam, learning rate 0.05 |
| Epochs / batch | 1000 / 4 |
| Seed | 42 |

## Expected outcome

The original lab record reports **100% accuracy** on the XOR truth table after
1000 epochs. The notebook contains an assertion that fails if the model does
not fit all four rows, so a successful run is a direct check of the result.

Typical predictions after training:

| A | B | Expected | Predicted |
|---|---|----------|-----------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

> **Execution status:** the notebook was syntax-checked and its structure was
> validated during repository preparation. The full training run was not
> performed locally. The result above is the outcome recorded in the original
> lab sheet; rerunning the notebook with seed 42 should reproduce it.

## Observations

- The hidden layer is essential. Replacing `tanh` with no hidden layer would
  collapse the model to logistic regression, which tops out near 50% on XOR.
- The problem is tiny, so 1000 epochs take only a few seconds on a CPU.
- The sigmoid output makes the decision threshold explicit: probability
  `>= 0.5` means class 1.

## Files and artifacts

- Notebook: `notebooks/01_xor_mlp.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP01.docx`
- Runtime model: `outputs/exp01_xor_mlp.keras`
- Runtime plot: `outputs/exp01_training_curves.png`

The `outputs/` directory is ignored by Git and is never committed.

## How to run

### Google Colab

1. Upload `notebooks/01_xor_mlp.ipynb` to Colab, or open it from GitHub once
   the repository is public.
2. Select **Runtime -> Run all**. No GPU is needed.
3. Download the files in `outputs/` if you want to keep the trained model.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/01_xor_mlp.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Accuracy stays near 50% | Hidden layer removed or `tanh` changed to a linear activation | Use the 2-4-1 architecture exactly as written |
| Predictions differ slightly | Different TensorFlow/Keras version or nondeterministic GPU kernels | Use the seed and compare the predicted classes, not the exact probability |
| `ModuleNotFoundError: tensorflow` | Environment not installed | `pip install -r requirements.txt` or use Colab |

## Conclusion

A small MLP with a nonlinear hidden layer solves XOR perfectly. This is the
classic demonstration that depth plus nonlinearity overcomes the limits of a
single perceptron.

**Next:** [Experiment 2 - Deep Learning Libraries](02_libraries_overview.md)
