# NexusChatAI

Intelligent Discord Bot Template with Rolling Context

## Overview

NexusChatAI serves as a base project for building complex AI chatbots for Discord. It provides a robust foundation with features like rolling context management, customizable AI interactions, and easy integration with AI providers. Users can build upon this template to create sophisticated AI-powered Discord bots tailored to their specific needs.

## Features

-   Rolling context management for persistent conversations
-   Customizable AI character and behavior
-   Easy integration with AI providers (default: Together AI)
-   Modular design for easy expansion and modification

## Getting Started

### Prerequisites

-   Python 3.8 or higher
-   Discord account and bot token
-   Together AI API key (or another AI provider of your choice)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/VenkatLohithDasari/NexusChatAI.git
    cd NexusChatAI
    ```

2. Create a virtual environment (optional but recommended):

    ```
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory with the following content:

    ```
    DISCORD_TOKEN=your_discord_bot_token
    TOGETHER_API_KEY=your_together_ai_api_key
    ```

2. Configure the `config/config.json` file:

    ```json
    {
        "system_prompt": "You are a helpful assistant.",
        "ai_name": "NexusChatAI",
        "custom_instructions": "{ai_name} will always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.",
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "max_tokens": 150,
        "temperature": 0.98,
        "top_p": 0.37,
        "top_k": 100,
        "repetition_penalty": 1.18,
        "stream": true,
        "stop": "<|eot_id|>"
    }
    ```

    - `system_prompt`: Defines the AI's base behavior and role.
    - `ai_name`: The name of your AI assistant.
    - `custom_instructions`: Additional instructions for the AI. You can use `{ai_name}` as a variable to include the AI's name.
    - Other fields: AI model and sampling parameters.

### Running the Bot

Run the bot using the following command:

```
python bot.py
```

## Customization

### AI Provider

By default, NexusChatAI uses Together AI. To use a different AI provider:

1. Create a new file in the `ai_api` directory (e.g., `custom_ai_provider.py`).
2. Implement a class similar to `TogetherAI` in `together_ai.py`.
3. Modify `bot.py` to use your new AI provider.

### Extending Functionality

-   Add new commands by creating functions with the `@bot.command()` decorator in `bot.py`.
-   Modify the `ContextManager` in `context_manager/context_manager.py` to change how context is stored and managed.
-   Adjust the `PromptCreator` in `prompt_creator/prompt_creator.py` to alter how prompts are formatted.

## Contributing

Contributions to NexusChatAI are welcome! Please feel free to submit pull requests, create issues, or suggest enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

-   Discord.py library
-   Together AI (or your chosen AI provider)
-   All contributors and users of NexusChatAI

## Support

For support, please open an issue in the GitHub repository or contact the maintainers directly.

---

Happy coding with NexusChatAI! 🤖💬
