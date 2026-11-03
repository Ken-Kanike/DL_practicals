# Experiment 8 - RNN for Temporal Classification and Sequence-to-Sequence Modelling

[Notebook](../notebooks/08_rnn_imdb_seq2seq.ipynb) | [Lab sheet](../docs/Junaid_B23__EXP08.docx) | [Back to README](../README.md)

## Aim

Use recurrent neural networks for two tasks:

1. classify IMDB movie reviews as positive or negative with an LSTM, and
2. train an encoder-decoder LSTM to reverse a short integer sequence.

## Theory in brief

An RNN maintains a hidden state across time, which lets it model order and
context. The LSTM variant gates its memory to capture long-range dependencies
and reduce vanishing gradients.

- **Temporal classification:** an `Embedding` maps word indices to dense
  vectors, padding makes every review the same length, an LSTM summarizes the
  sequence, and a sigmoid produces `P(positive)`.
- **Sequence-to-sequence:** an encoder LSTM compresses the source into a fixed
  vector, `RepeatVector` copies it across the target length, and a decoder LSTM
  with a time-distributed softmax emits one token per time step.

## Datasets

- IMDB reviews:
  `https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz`
- IMDB word index:
  `https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json`
- Sequence-reversal data: generated deterministically in code.

No local dataset is used.

## Part A - IMDB sentiment classifier

### Configuration

| Item | Value |
|---|---|
| Vocabulary | 10,000 most frequent words |
| Sequence length | 200 (post-padding, post-truncation) |
| Embedding dimension | 64 |
| RNN | LSTM, 64 units |
| Output | 1 sigmoid unit |
| Loss | Binary cross-entropy |
| Optimizer | Adam |
| Epochs / batch | 3 / 256 |
| Validation split | 10% |

### Process

1. Download the IMDB NPZ file and word-index JSON from explicit URLs.
2. Load the sequences with the standard Keras loader and a 10,000-word
   vocabulary.
3. Pad/truncate every review to 200 tokens.
4. Build decoding and encoding helpers for raw text.
5. Build and train the Embedding -> LSTM -> Dense(sigmoid) classifier.
6. Evaluate on the 25,000-review test set.
7. Report the confusion matrix and classification report.
8. Plot training curves.
9. Run sentiment inference on new review text.
10. Save the model.

### Expected outcome

The original lab sheet records about **86% test accuracy** on IMDB. The
classifier should clearly separate positive and negative reviews, with errors
concentrated on mixed or sarcastic reviews.

## Part B - Sequence-to-sequence reversal

### Configuration

| Item | Value |
|---|---|
| Sequence length | 6 |
| Vocabulary | 12 tokens (indices 1-11) |
| Training / test | 8,000 / 1,000 sequences |
| Encoder | Embedding(12, 64) -> LSTM(128) |
| Bridge | RepeatVector(6) |
| Decoder | LSTM(128, return sequences) -> TimeDistributed Dense(12, softmax) |
| Loss | Sparse categorical cross-entropy |
| Optimizer | Adam |
| Epochs / batch | 30 / 256 |

### Process

1. Generate random source sequences of length 6 with values 1-11.
2. Create targets by reversing each source sequence.
3. Build the encoder-decoder model.
4. Train with early stopping on validation loss.
5. Evaluate token accuracy and exact-sequence match accuracy.
6. Show source, expected, and predicted sequences.
7. Plot training curves.
8. Run a `reverse_sequence` inference helper.
9. Save the model.

### Expected outcome

The original lab sheet records about **99.87% token accuracy**. The reversal
task is deterministic and the vocabulary is tiny, so the model should learn it
almost perfectly. Exact-sequence accuracy is the stricter metric and is also
expected to be very high.

> **Execution status:** the notebook was syntax-checked and both model
> architectures were forward-passed with random tensors during repository
> preparation. The full training runs were not performed locally. The numbers
> above are the outcomes recorded in the original lab sheet.

## Observations

- The IMDB model is limited by the 200-token truncation; long reviews may lose
  sentiment-bearing text near the end.
- The embedding layer is learned jointly with the classifier, so no pretrained
  word vectors are required.
- The reversal model needs a fixed-length encoder vector; `RepeatVector` is a
  simple bridge. Attention or a direct decoder would be more flexible for
  longer or variable-length sequences.
- Token accuracy can be high even when a whole sequence is slightly wrong;
  exact-match accuracy is the better check for sequence-to-sequence tasks.
- GPU acceleration makes the LSTM training noticeably faster.

## Files and artifacts

- Notebook: `notebooks/08_rnn_imdb_seq2seq.ipynb`
- Lab sheet: `docs/Junaid_B23__EXP08.docx`
- Runtime models:
  - `outputs/exp08_imdb_lstm.keras`
  - `outputs/exp08_seq2seq_lstm.keras`
  - `outputs/exp08_imdb_best.keras`
  - `outputs/exp08_seq2seq_best.keras`
- Runtime metrics and histories:
  - `outputs/exp08_metrics.csv`
  - `outputs/exp08_imdb_history.csv`
  - `outputs/exp08_seq2seq_history.csv`
- Runtime plots:
  - `outputs/exp08_imdb_confusion_matrix.png`
  - `outputs/exp08_imdb_training_curves.png`
  - `outputs/exp08_seq2seq_training_curves.png`

The `outputs/` directory is ignored by Git.

## How to run

### Google Colab

1. Upload `notebooks/08_rnn_imdb_seq2seq.ipynb`.
2. Select **Runtime -> Change runtime type -> GPU** if available.
3. Select **Runtime -> Run all**.
4. The first run downloads the IMDB files automatically.

### Kaggle

1. Import the notebook and enable **Internet**.
2. Run all cells.

### Local

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
jupyter lab notebooks/08_rnn_imdb_seq2seq.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| IMDB download fails | No internet or blocked storage URL | Enable internet and rerun the download cell |
| `ValueError` about input shape | Sequences not padded to 200 | Use the provided `pad_sequences` calls |
| Sentiment inference is inverted | Label convention is 0=negative, 1=positive | Keep the threshold at 0.5 and the label mapping in `predict_sentiment` |
| Seq2seq accuracy stays low | Too few epochs or learning rate mismatch | Train for the full 30 epochs with Adam |
| Token accuracy is high but sequences are wrong | Token-level metric hides order errors | Check `exact_match_accuracy` and the printed examples |
| Out of memory | Batch size too large for the GPU | Reduce `BATCH_SIZE` to 128 or 64 |

## Conclusion

The experiment demonstrates both major RNN use cases. The LSTM sentiment
classifier learns from padded token sequences, and the encoder-decoder model
learns a deterministic sequence transformation. The lab sheet's recorded
outcomes are about 86% IMDB accuracy and about 99.87% reversal token accuracy.

**Previous:** [Experiment 7 - CIFAR-10 CNN](07_cnn_cifar10.md) |
**Next:** [Experiment 9 - Gradient Descent Variants on MNIST](09_optimizer_comparison_mnist.md)
