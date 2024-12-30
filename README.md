# Cyber-Command Assistant

Cyber-Command Assistant is a Python-based desktop tool designed to combine AI-powered features with an easy-to-use interface. This application allows users to interact with an AI assistant, perform commands, and access websites effortlessly. Built with Tkinter, it features a customizable layout and saves your session history for convenience.

## Key Features

- **AI-Driven Commands:** Execute tasks and interact with Groq AI for assistance.
- **Quick Web Access:** Open popular websites like Google, YouTube, and GitHub directly from the app.
- **Session Memory:** Automatically saves and reloads your conversational history.
- **Flexible Design:** A responsive GUI with a resizable background image for a polished look.
- **Error Notifications:** Clear and friendly messages for unexpected issues.

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or newer
- Libraries:
  - `tkinter`
  - `pillow`
  - `groq`

## Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cyber-command-assistant.git
   cd cyber-command-assistant
   ```

2. Install the required libraries:
   ```bash
   pip install pillow groq
   ```

3. Add your Groq API key:
   Open the script and update the `aiProcess` function:
   ```python
   client = Groq(api_key="your_api_key_here")
   ```

4. Place a background image (e.g., `Hacked.jpg`) in the project directory or update the file path in the code to use your own image.

## How to Use

1. Run the app:
   ```bash
   python cyber_command_assistant.py
   ```

2. Input a command:
   - To open a website, type commands like "open google".
   - To interact with the AI assistant, type your query or task.

3. Check the results in the scrollable output area.

4. When you close the app, your session context will be saved automatically.

## File Structure

```plaintext
.
├── cyber_command_assistant.py  # Main application script
├── Hacked.jpg                 # Default background image
├── context.json               # Saved session context
└── README.md                  # Documentation file
```

## Customization Options

- **Adding New Commands:**
  To include more website shortcuts, update the `url_map` dictionary in the `process_command` function.

- **Using a Different Background:**
  Replace the `Hacked.jpg` file with your chosen image or update its file path in the code.

## Contributing

Contributions are always welcome! You can open an issue or submit a pull request with new ideas, features, or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Special Thanks

- [Groq AI](https://groq.com) for powering the AI capabilities.
- The Tkinter library for providing a robust and simple GUI framework.
- Pillow for handling image resizing and processing.

---

Enjoy using Cyber-Command Assistant! If you like this project, don’t forget to ⭐ it on GitHub.
