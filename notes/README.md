# Experiment Notes

One Markdown note per practical. Each note records the aim, the relevant
theory, the dataset and preprocessing, the process, the expected outcome, the
observations, the runtime artifacts, run instructions, troubleshooting, and a
conclusion.

| # | Note | Practical | Notebook |
|---|---|---|---|
| 1 | [01_xor_mlp.md](01_xor_mlp.md) | XOR classification with a multi-layer perceptron | [Notebook](../notebooks/01_xor_mlp.ipynb) |
| 2 | [02_libraries_overview.md](02_libraries_overview.md) | Comparison of TensorFlow/Keras, PyTorch, and scikit-learn | [Notebook](../notebooks/02_libraries_overview.ipynb) |
| 3 | [03_single_layer_optimizers.md](03_single_layer_optimizers.md) | Single-layer network with different optimizers | [Notebook](../notebooks/03_single_layer_optimizers.ipynb) |
| 4 | [04_deep_ffn_multiclass.md](04_deep_ffn_multiclass.md) | Deep feed-forward multiclass classifier | [Notebook](../notebooks/04_deep_ffn_multiclass.ipynb) |
| 5 | [05_autoencoder_compression.md](05_autoencoder_compression.md) | Autoencoder for data compression | [Notebook](../notebooks/05_autoencoder_compression.ipynb) |
| 6 | [06_cnn_mnist.md](06_cnn_mnist.md) | CNN for MNIST digit classification | [Notebook](../notebooks/06_cnn_mnist.ipynb) |
| 7 | [07_cnn_cifar10.md](07_cnn_cifar10.md) | CNN for CIFAR-10 classification with augmentation | [Notebook](../notebooks/07_cnn_cifar10.ipynb) |
| 8 | [08_rnn_imdb_seq2seq.md](08_rnn_imdb_seq2seq.md) | IMDB sentiment analysis and seq2seq reversal | [Notebook](../notebooks/08_rnn_imdb_seq2seq.ipynb) |
| 9 | [09_optimizer_comparison_mnist.md](09_optimizer_comparison_mnist.md) | Gradient descent variants on MNIST | [Notebook](../notebooks/09_optimizer_comparison_mnist.ipynb) |
| 10 | [10_dl_case_studies.md](10_dl_case_studies.md) | Domain case studies with CNN, RNN, and GAN demos | [Notebook](../notebooks/10_dl_case_studies.ipynb) |

## Reference results

These are the outcomes recorded in the original lab sheets. The notebooks
recompute their own metrics; exact values vary with library versions, seeds,
and hardware.

| Experiment | Reference result |
|---|---|
| 1 | 100% XOR accuracy |
| 2 | Conceptual framework comparison; no single metric |
| 3 | ~99.75% accuracy, loss 0.01-0.05 |
| 4 | ~96.67% accuracy, loss ~0.07 |
| 5 | Test MSE ~0.0137; 24.5x compression ratio |
| 6 | 99.03% accuracy, loss ~0.028 |
| 7 | 76.76% accuracy, loss ~0.67 |
| 8 | IMDB ~86%; sequence reversal ~99.87% token accuracy |
| 9 | SGD 97.42, MiniBatch 94.46, Momentum 97.34, Nesterov 97.23, Adagrad 90.50, Adam 97.05 |
| 10 | Case study; demos are illustrative, not exact reproductions |

## Execution status

The notebooks were syntax-checked, and key model/data paths were smoke-tested
during repository preparation. Full training runs were not performed locally.
Each note states the execution status for its experiment and avoids presenting
the lab-sheet values as freshly reproduced results.

## Note structure

Most notes use the same sections:

1. Aim
2. Theory in brief
3. Dataset
4. Model or process
5. Expected outcome and execution status
6. Observations
7. Files and artifacts
8. How to run
9. Troubleshooting
10. Conclusion
11. Previous/next navigation

Experiments 8 and 10 use task-specific subsections because they contain two
and three models respectively.

[Back to the main README](../README.md)
