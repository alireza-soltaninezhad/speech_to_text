# Import library
from tkinter import Tk, Label, Button, StringVar, filedialog, OptionMenu, DISABLED, NORMAL
import os
import whisper
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import ttk
import textwrap
import re
os.environ['TK_SILENCE_DEPRECATION'] = '1'

class TranscriptionApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Transcription App")

        # Create a label
        self.label = Label(window, text="Select an audio file for transcription")
        self.label.pack(pady=20)

        # Create a browse button
        self.browse_btn = Button(window, text="Browse", command=self.load_file)
        self.browse_btn.pack(pady=20)

        # Create a dropdown for model selection
        self.mode = StringVar(window)
        self.modes = ["tiny.en", "base.en", "small.en", "medium.en"]
        self.mode.set(self.modes[1])  # default value is "base.en"
        self.optionMenu = OptionMenu(window, self.mode, *self.modes)
        self.optionMenu.pack(pady=20)

        # Create a button to start transcription
        self.transcribe_btn = Button(window, text="Transcribe", command=self.transcribe_file)
        self.transcribe_btn.pack(pady=20)

        # Progress bar
        self.progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

        # Label to show percentage
        self.percentage_label = Label(window, text="0%")
        self.percentage_label.pack()

        # Button to save the result as PDF (disabled initially)
        self.save_btn = Button(window, text="Save as PDF", command=self.save_as_pdf, state=DISABLED)
        self.save_btn.pack(pady=20)

    def wrap_text(self, text, max_chars):
        """Wrap text to ensure that words aren't broken."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            if len(' '.join(current_line) + ' ' + word) <= max_chars:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        return lines

    def update_progress(self, increment):
        current_value = self.progress["value"] + increment
        self.progress["value"] = current_value
        self.percentage_label.config(text=f"{int(current_value)}%")
        self.window.update_idletasks()

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Select a file")
        if file_path:
            self.file_path = file_path
            self.label.config(text=f"Selected file: {file_path}")

    def transcribe_file(self):
        if hasattr(self, "file_path"):
            with open(self.file_path, "rb") as audio_file:
                self.update_progress(10)
                model = whisper.load_model(self.mode.get())
                self.update_progress(10)
                self.result_text = model.transcribe(self.file_path)
                self.update_progress(70)
                self.update_progress(10)
            self.save_btn.config(state=NORMAL)
        adjusted_text = re.sub(r'(?<=[^\.!?])\s+(?=[A-Z])', '. ', self.result_text["text"])
        self.result_text["text"] = adjusted_text
    def save_as_pdf(self):
        if hasattr(self, "result_text"):
            save_location = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if save_location:
                c = canvas.Canvas(save_location, pagesize=letter)

                # Margins for A4 sized PDF
                margin = 85
                width, height = letter
                available_width = width - 2 * margin

                text_object = c.beginText(margin, height - margin)  # Start from top-left margin
                text_object.setFont("Times-Roman", 12)

                # Adjust max_chars_per_line to fit the available width.
                # Let's assume each character is about 5 points wide on average, this is a guess and might need adjusting.
                max_chars_per_line = int(available_width / 4.4)
                lines = textwrap.wrap(self.result_text["text"], max_chars_per_line)

                for line in lines:
                    text_object.textLine(line)

                c.drawText(text_object)
                c.save()


if __name__ == "__main__":
    root = Tk()
    app = TranscriptionApp(root)
    root.mainloop()
