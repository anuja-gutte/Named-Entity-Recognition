# Named Entity Recognition (NER)

A simple Named Entity Recognition (NER) web app built using Hugging Face Transformers and Gradio.

## Features

- Detects:
  - Person names
  - Locations
  - Organizations
  - Other entities
- Interactive Gradio interface
- Uses a lightweight Hugging Face NER model

## Tech Stack

- Python
- Hugging Face Transformers
- Gradio

## Model Used

- `elastic/distilbert-base-cased-finetuned-conll03-english`

## Installation

Clone the repository:

```bash
git clone https://github.com/anuja-gutte/Named-Entity-Recognition.git
cd Named-Entity-Recognition
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python app.py
```

Open the Gradio link in your browser.

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

## Example

Input:
> Elon Musk founded SpaceX in the United States.

Output:
- Elon Musk → PER
- SpaceX → ORG
- United States → LOC
