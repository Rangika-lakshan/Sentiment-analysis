# Hugging Face Sentiment Analysis

A lightweight Python script that utilizes the Hugging Face `transformers` library to perform text-based sentiment analysis. It classifies input sentences as either `POSITIVE` or `NEGATIVE` along with a confidence score.

## Features
- Implements the Hugging Face `pipeline` API for NLP.
- Pre-trained models are automatically loaded (`distilbert-base-uncased-finetuned-sst-2-english`).
- Processes a batch of sentences and prints formatted results.
- Includes an interactive user input loop to test custom sentences in real-time.

## How to Run
1. Install the required dependencies:
   ```bash
   pip install transformers torch
   ```
2. Run the analysis script:
   ```bash
   python script1.py
   ```
