import ollama
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import datetime

MODEL_NAME = "deepseek-r1"
WINDOW_TITLE = "Ultimate AI Assistant"
WINDOW_SIZE = "900x600"

SYSTEM_PERSONA = """
You are a powerful, smart, and friendly AI assistant. You answer clearly, logically, and in detail.
"""



def timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def ask_ai(user_input):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PERSONA},
                {"role": "user", "content": user_input}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        return f"⚠️ error: {str(e)}"

class UltimateAIApp:

    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)

        # --- Chat Area ---
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Segoe UI", 11),
            state="disabled"
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # --- Input Frame ---
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.user_input = tk.Entry(
            input_frame,
            font=("Segoe UI", 12)
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Segoe UI", 11),
            command=self.send_message
        )
        send_btn.pack(side=tk.RIGHT)

        # --- Bottom Buttons ---
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=5)

        clear_btn = tk.Button(
            bottom_frame,
            text="Clear Chat",
            command=self.clear_chat
        )
        clear_btn.pack(side=tk.LEFT)

        exit_btn = tk.Button(
            bottom_frame,
            text="Exit",
            command=self.exit_app
        )
        exit_btn.pack(side=tk.RIGHT)

        self.write_ai("AI hi how are you?")



    def write_user(self, text):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"[{timestamp()}] You: {text}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def write_ai(self, text):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"[{timestamp()}] AI: {text}\n\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)


    def send_message(self, event=None):
        text = self.user_input.get().strip()

        if text == "":
            return

        self.user_input.delete(0, tk.END)
        self.write_user(text)

        threading.Thread(target=self.process_ai, args=(text,), daemon=True).start()

    def process_ai(self, text):
        self.write_ai("⌛ thinking...")
        answer = ask_ai(text)

        # remove "thinking" line
        self.chat_area.config(state="normal")
        self.chat_area.delete("end-3l", "end-1l")
        self.chat_area.config(state="disabled")

        self.write_ai(answer)

    def clear_chat(self):
        self.chat_area.config(state="normal")
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state="disabled")

    def exit_app(self):
        if messagebox.askyesno("Exit", "are you sure you want to exit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = UltimateAIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()