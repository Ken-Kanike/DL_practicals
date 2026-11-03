# Experiment 5 - Image Compression with a Dense Autoencoder

[Notebook](../notebooks/05_autoencoder_compression.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP05.docx) | [Back to README](../README.md)

## Aim

Build a dense autoencoder that compresses 28x28 MNIST digits into a
32-dimensional latent vector and reconstructs them, then evaluate the
reconstruction error and compression ratio.

## Theory in brief

An autoencoder is an unsupervised network trained to reconstruct its own
input. The encoder compresses the input into a low-dimensional bottleneck; the
decoder expands the bottleneck back to the original shape. Because all
information must pass through the bottleneck, the network learns a compact,
lossy representation. The loss is mean squared error between the input and the
reconstruction, and the input images are also used as the targets.

## Dataset

MNIST, downloaded at runtime from:

`https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz`

- 60,000 training images and 10,000 test images
- 28x28 grayscale, pixel values 0-255
- normalized to `[0, 1]` and flattened to 784 values

No local dataset file is used.

## Architecture

| Stage | Layer | Output shape |
|---|---|---|
| Input | Flattened image | 784 |
| Encoder | Dense 64, ReLU | 64 |
| Bottleneck | Dense 32, ReLU | 32 |
| Decoder | Dense 64, ReLU | 64 |
| Output | Dense 784, sigmoid | 784 |

- **Loss:** mean squared error
- **Optimizer:** Adam, learning rate 0.001
- **Epochs:** 10 (early stopping with patience 3)
- **Batch size:** 256
- **Validation split:** 10%
- **Seed:** 42

## Process

1. Download MNIST from the explicit URL and inspect its shape.
2. Normalize and flatten the images.
3. Display sample digits.
4. Build the symmetric encoder/decoder/autoencoder.
5. Train with the images as both input and target.
6. Measure test MSE and the per-image MSE distribution.
7. Visualize original and reconstructed digits side by side.
8. Run the encoder and decoder separately and confirm that their composition
   matches the full autoencoder.
9. Project the 32-dimensional latent codes to 2D with PCA and color by digit.
10. Run a single-image compress/reconstruct inference helper.
11. Save the autoencoder, encoder, decoder, metrics, and plots.

## Expected outcome

The original lab sheet records a **test MSE near 0.0137** after 10 epochs with
the 784 -> 64 -> 32 -> 64 -> 784 architecture. Reconstructions should preserve
the digit shape while losing fine stroke detail.

Compression ratio:

- **Dimensional ratio:** 784 / 32 = **24.5x**.
- **Raw byte ratio with float32 latents:** 784 bytes (uint8 image) / 128 bytes
  (32 float32 values) = **6.1x** before any entropy coding. The 24.5x figure
  describes dimensionality, not automatically achievable storage savings.

> **Execution status:** the notebook was syntax-checked and the
> encoder/decoder composition was smoke-tested with random tensors during
> repository preparation. The full training run was not performed locally.
> The MSE above is the outcome recorded in the original lab sheet.

## Observations

- The autoencoder learns a smooth, low-dimensional representation even though
  it is never given digit labels.
- The PCA plot usually shows partial clustering by digit, which is evidence
  that the bottleneck preserves class-relevant structure.
- Reconstructions are blurrier than the originals because MSE encourages
  averaging and the bottleneck is only 32 values.
- Saving the encoder and decoder separately is useful for deployment: only the
  encoder is needed to compress, and only the decoder is needed to decompress.
- The distinction between dimensional compression and byte-level compression
  matters when reporting results.

## Files and artifacts

- Notebook: `notebooks/05_autoencoder_compression.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP05.docx`
- Runtime models:
  - `outputs/exp05_autoencoder.keras`
  - `outputs/exp05_encoder.keras`
  - `outputs/exp05_decoder.keras`
- Runtime metrics: `outputs/exp05_metrics.csv`, `outputs/exp05_history.csv`
- Runtime plots:
  - `outputs/exp05_mnist_samples.png`
  - `outputs/exp05_reconstructions.png`
  - `outputs/exp05_latent_pca.png`
  - `outputs/exp05_single_reconstruction.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/05_autoencoder_compression.ipynb`.
2. Select **Runtime -> Run all**. CPU is sufficient; a GPU makes it faster.
3. MNIST downloads automatically on the first run.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/05_autoencoder_compression.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Download fails | No internet or a blocked storage URL | Enable internet and rerun the data cell |
| MSE is much higher than 0.0137 | Model trained for too few epochs or pixels not normalized | Rerun all cells; keep the `/255.0` normalization |
| Latent codes are all zero | ReLU bottleneck collapsed | Restart with the fixed seed and the same architecture |
| Reload warning about optimizer variables | Model saved before compiling or training | The weights still load; warnings are harmless for inference |
| PCA plot is cluttered | Too many points | Reduce `N_VISUALIZE` or increase alpha transparency |

## Conclusion

The dense autoencoder compresses MNIST digits into 32 values and reconstructs
them with low MSE. It demonstrates the encoder-decoder principle that
underlies image compression, denoising, and representation learning. The lab
sheet's recorded MSE of about 0.0137 is the reference outcome.

**Previous:** [Experiment 4 - Deep Feed-Forward Network](04_deep_ffn_multiclass.md) |
**Next:** [Experiment 6 - CNN on MNIST](06_cnn_mnist.md)
