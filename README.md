# Python Quote Generator

A simple desktop app that fetches random quotes and displays them in a GUI. Click **Random Quote** to load a new one.

## Features

- Random quotes from the [Forismatic](http://forismatic.com/en/) API
- Desktop UI built with [Dear PyGui](https://github.com/hoffstadt/DearPyGui)
- Graceful handling of network errors (shows a message instead of crashing)

## Requirements

- Python 3.10+ (3.11 or 3.12 recommended)
- Internet connection (quotes are fetched online)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/email362/python-quote-generator.git
   cd python-quote-generator
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the app:

```bash
python main.py
```

A window opens with a quote and author. Click **Random Quote** to fetch another.

## Project structure

| File | Description |
|------|-------------|
| `main.py` | App logic, API calls, and GUI |
| `requirements.txt` | Python dependencies (`dearpygui`, `requests`) |

## License

See [LICENSE](LICENSE).
