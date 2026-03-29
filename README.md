# Chatbot CLI

## Overview

Chatbot CLI is a command-line interface application built with Python using the Typer library and the OpenAI API. This chatbot allows users to interact with an AI model in a conversational manner directly from their terminal. 

## Features

- Interactive conversation with an AI model
- Easy-to-use command-line interface
- History tracking of conversations
- Customizable prompts for the AI
- Built-in help and usage information

## Requirements

- Python 3.8 or higher
- `typer`
- `openai`

## Installation

To get started with the Chatbot CLI, follow these installation instructions:

1. Clone the repository:

   ```bash
   git clone https://github.com/malf2/typer-chatbot-openai.git
   cd typer-chatbot-openai
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   uv sync
   ```

4. Set your OpenAI API key:

   Make sure you set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY='your_api_key'  # On Windows, use `set OPENAI_API_KEY='your_api_key'`
   ```

## Usage

Run the chatbot CLI by executing the following command:

```bash
python main.py
```

### Commands

- **start_chat**: Start a conversation with the AI model.

### Example

To initiate a conversation, simply run the chatbot and type your messages:

```bash
$ python main.py
Chat started. Type 'exit' to quit.
> Hello, how are you?
I'm just a computer program, but I'm here to help you!
```

## Acknowledgments

- [Typer](https://typer.tiangolo.com/) for a simple CLI framework
- [OpenAI](https://openai.com/) for their powerful language models