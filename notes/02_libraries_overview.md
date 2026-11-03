# Experiment 2 - Overview of Deep Learning Libraries

[Notebook](../notebooks/02_libraries_overview.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP02.docx) | [Back to README](../README.md)

## Aim

Compare the major Python deep learning libraries - Theano, TensorFlow, Keras,
and PyTorch - and understand their execution models, abstraction levels,
hardware support, and practical trade-offs.

## Theory in brief

Deep learning frameworks provide tensors, automatic differentiation, neural
network layers, losses, optimizers, and training utilities. They differ in
whether the computation graph is static or dynamic, whether the API is low or
high level, and which hardware and deployment tools they support. The lab
sheet is primarily a comparative study; the notebook adds a small hands-on
implementation so the differences are visible in code.

## Dataset

Iris, loaded from a public URL:

- Primary:
  `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv`
- Fallback:
  `https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data`

The CSV has four measurements and three species (150 rows). No local dataset
file is used.

## Process

1. Load and inspect the Iris data from the URL.
2. Split into 70% train, 15% validation, and 15% test with stratification.
3. Standardize using training-set statistics only.
4. Build the same 4 -> 16 ReLU -> 3 softmax classifier in Keras/TensorFlow.
5. Train with Adam, early stopping, and sparse categorical cross-entropy.
6. Show a low-level TensorFlow `GradientTape` calculation to explain what
   Keras automates.
7. Build and train the same classifier in PyTorch with an explicit training
   loop.
8. Compare test loss, test accuracy, and training time.
9. Run inference with both models on raw measurements.
10. Optionally demonstrate PyTensor, the maintained symbolic-graph successor
    to Theano.

## Framework comparison

| Library | Developer | Graph | Level | Hardware | Status |
|---|---|---|---|---|---|
| Theano | MILA | Static symbolic | Low | CPU / GPU | Discontinued after 2017; historical |
| TensorFlow | Google | Static graph + eager execution | Low / high via Keras | CPU / GPU / TPU | Active |
| Keras | Chollet / Google | Backend-dependent | High | CPU / GPU / TPU | Active; Keras 3 is multi-backend |
| PyTorch | Meta | Dynamic define-by-run | Low / high | CPU / GPU | Active; research-dominant |

## Expected outcome

The lab sheet does not record a numeric accuracy for this experiment because it
is conceptual. The notebook should produce high test accuracy for both models
on Iris (typically in the 93-100% range), and the comparison table should show
similar predictive quality with different amounts of boilerplate.

> **Execution status:** the notebook was syntax-checked and the model
> definitions were reviewed during repository preparation. The full training
> run was not performed locally. Treat the accuracy range above as a typical
> expectation, not a reproduced measurement.

## Observations

- Keras expresses the model and training loop in only a few lines.
- PyTorch requires an explicit loop (`zero_grad`, forward pass, loss,
  `backward`, `step`) but makes every step visible and easy to customize.
- TensorFlow's `GradientTape` shows that both high-level APIs ultimately rely
  on automatic differentiation.
- Theano is historically important but should not be used for new work. The
  PyTensor/Aesara forks preserve its symbolic approach.
- The framework choice depends on the task: rapid prototyping (Keras),
  production deployment (TensorFlow/TFX/ONNX), or research flexibility
  (PyTorch).

## Files and artifacts

- Notebook: `notebooks/02_libraries_overview.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP02.docx`
- Runtime Keras model: `outputs/exp02_iris_keras.keras`
- Runtime PyTorch state: `outputs/exp02_iris_torch.pt`
- Runtime results: `outputs/exp02_framework_results.csv`
- Runtime plots: `outputs/exp02_iris_scatter.png`,
  `outputs/exp02_framework_training_curves.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/02_libraries_overview.ipynb`.
2. Select **Runtime -> Run all**. TensorFlow and PyTorch are preinstalled.
3. If you want the optional PyTensor section, run
   `!pip install pytensor` in a separate cell first.

### Kaggle

1. Import the notebook.
2. Enable **Internet** in the notebook settings; Iris is fetched from a URL.
3. Run all cells.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/02_libraries_overview.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Iris download fails | No internet or URL blocked | Enable internet; the notebook tries the UCI fallback |
| PyTorch not found | Requirements not installed | `pip install torch` or use Colab/Kaggle |
| PyTensor section skipped | Optional package not installed | `pip install pytensor` |
| PyTorch reload warning | Newer `torch.load` defaults | The state dict still loads; pass `weights_only=True` explicitly if desired |

## Conclusion

The experiment shows that modern frameworks solve the same problem at
different abstraction levels. Keras minimizes code, TensorFlow exposes the
gradient machinery when needed, PyTorch gives full control of the training
loop, and Theano remains a historical reference rather than a practical
choice.

**Previous:** [Experiment 1 - XOR MLP](01_xor_mlp.md) |
**Next:** [Experiment 3 - Single-Layer Network Optimizers](03_single_layer_optimizers.md)
