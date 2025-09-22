# ChatGPT Query

A simple command-line tool to quickly open ChatGPT with your query in the browser.

## Installation

```bash
pip install chatgpt-query
```

## Usage

### Basic Usage

```bash
# Simple query
chat Hello world
```

### Options

```bash
# Dry run - just print the URL without opening browser
chat -d "What is AI?"
# Output: Generated URL: https://chat.openai.com/?q=What+is+AI%3F&model=auto

# Specify a model
chat -m gpt-4 "Explain quantum computing"

# Ask ChatGPT to run search on your query
chat -s "Latest news about AI"
```
