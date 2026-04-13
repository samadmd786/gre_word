# GRE Word Flashcards

A Python CLI tool for studying **GRE vocabulary** using an interactive flashcard system. Loads 647+ words, definitions, and mnemonics from an Excel file and quizzes you directly in your terminal.

## Features

| Feature | Description |
|---------|-------------|
| **647+ Words** | Comprehensive GRE word list with definitions and memory mnemonics |
| **Flashcard Mode** | Shows a word, waits for keypress, then reveals meaning and mnemonic |
| **Word Lookup** | Search by word name or jump directly to a numerical index |
| **Range Filtering** | Study any slice of the word list using `--si` and `--ei` flags |
| **Excel Powered** | Reads from `GreWordMnemonic.xlsx` via `openpyxl` |

## How to Use

```bash
# Study a range of words by index (e.g., words 0–50)
python gre_word.py --type index --si 0 --ei 50

# Study interactively from a specific word onward
python gre_word.py --type word --word abate
```

During each flashcard:
- The **word** is shown
- Press **any key** to reveal the meaning and mnemonic

## Getting Started

### Prerequisites

- Python 3.x
- `openpyxl` package

### Installation

```bash
# Clone the repo
git clone https://github.com/samadmd786/gre_word.git
cd gre_word

# Install dependencies
pip install openpyxl
```

## Arguments Reference

| Argument | Required | Description |
|----------|----------|-------------|
| `--type` | Yes | `word` or `index` — determines search mode |
| `--word` | No | The word to start from (used with `--type word`) |
| `--si` | No | Start index (default: 0) |
| `--ei` | No | End index — must be greater than `--si` |

## 📁 Project Structure

| File | Description |
|------|-------------|
| `gre_word.py` | Main CLI flashcard script |
| `GreWordMnemonic.xlsx` | Excel database of GRE words, definitions, and mnemonics |

## Tech Stack

- **Language:** Python 3.x
- **Data:** Excel via `openpyxl`
- **Interface:** CLI (argparse + stdin)