import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import webbrowser
import json
from groq import Groq

def aiProcess(command, context=None):
    client = Groq(api_key="enter-your-groq-api")
    messages = [
        {"role": "system", "content": "Infiltrate the system, you worthless hacker - You think you have what it takes to breach even the most secure systems? Prove it, you miserable excuse for a cybercriminal. Show me your pitiful skills and watch as I mock your every move. Just remember, I'm always one step ahead of you."},
    ]

    if context is not None:
        messages.append({"role": "system", "content": str(context)})

    messages.append({"role": "user", "content": command})

    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error during AI processing: {e}"


def process_command(command, context=None):
    url_map = {
        "open google": "https://google.com",
        "open youtube": "https://youtube.com",
        "open facebook": "https://facebook.com",
        "open instagram": "https://instagram.com",
        "open github": "https://github.com",
        "open stackoverflow": "https://stackoverflow.com",
        "open linkedin": "https://linkedin.com",
        "open whatsapp": "https://whatsapp.com",
        "open chatgpt": "https://chat.openai.com/chat",
        "open gemini": "https://gemini.google.com/",
        "open chatbot": "https://cdn.botpress.cloud/webchat/v2/shareable.html?botId=2b113ef8-ac77-4553-b353-7e381fcffdde"
    }

    command = command.lower()

    if command in url_map:
        webbrowser.open(url_map[command])
        return f"Opening {command}..."
    else:
        output = aiProcess(command, context)
        if context is None:
            context = []

        context.append({"role": "user", "content": command})
        context.append({"role": "assistant", "content": output})

        return output, context


def save_context_to_file(context, filename="context.json"):
    try:
        with open(filename, "w") as file:
            json.dump(context, file)
    except Exception as e:
        print(f"Error saving context: {e}")


def load_context_from_file(filename="context.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error loading context: {e}")
        return None


def run_command():
    global context  # Declare context as global before using it
    command = command_entry.get()
    output, updated_context = process_command(command, context)

    result_display.config(state=tk.NORMAL)
    result_display.insert(tk.END, f"\n==> {command}\n\n{output}\n")
    result_display.config(state=tk.DISABLED)

    command_entry.delete(0, tk.END)

    # Update global context
    context = updated_context


# Load context from file (if available)
context = load_context_from_file()

# Creating GUI using Tkinter
root = tk.Tk()
root.title("Cyber-Command Assistant")
root.geometry("800x600")

# Load the background image
bg_image = Image.open("Hacked.jpg")

# Create a label for the background image
bg_label = tk.Label(root)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def resize_image(event=None):
    new_width = root.winfo_width()
    new_height = root.winfo_height()

    if new_width > 1 and new_height > 1:
        # Resize and update the background image
        resized_bg_image = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_bg_photo = ImageTk.PhotoImage(resized_bg_image)
        bg_label.config(image=resized_bg_photo)
        bg_label.image = resized_bg_photo  # Prevent garbage collection

# Bind the resize event to adjust the background image when window size changes
root.bind("<Configure>", resize_image)

# Entry widget for command input
command_entry = tk.Entry(root, width=60)
command_entry.place(relx=0.1, rely=0.05, relwidth=0.8)  # Adjusted for relative width

# Button to run the command
run_button = tk.Button(root, text="Run Command", command=run_command)
run_button.place(relx=0.4, rely=0.15, relwidth=0.2)  # Adjusted for relative positioning

# Display area for the results
result_display = scrolledtext.ScrolledText(root, state=tk.DISABLED)
result_display.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65)  # Adjusted for relative size and position

# Initialize with the correct background size
resize_image()

# Run the application
root.mainloop()

# Save context when the application is closed
save_context_to_file(context)


# pip install groq
# pip install pillow
