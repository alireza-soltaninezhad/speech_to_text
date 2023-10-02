# Speech to Text Transcription App

Hello there! I'm **Alireza Soltani Nezhad**. Welcome to my Speech to Text transcription app using OpenAI's Whisper API!


## Overview

This application allows users to:
1. Select an audio file for transcription.
2. Choose the desired Whisper model for transcription.
3. Start the transcription process.
4. Save the transcribed text to a PDF file.

In the next versions, expect:
- Noise reduction features.
- Increased speed for transcription.
- Improved UX and UI.
- Support for additional languages and translation options.

## Links
- [LinkedIn Profile](https://www.linkedin.com/in/alirezasoltaninezhad/)
- [My GitHub](https://github.com/alireza-soltaninezhad)
- [Repository](https://github.com/alireza-soltaninezhad/speech_to_text)
- [Whisper API by OpenAI](https://github.com/openai/whisper)

## Installation Instructions


```markdown
## Running Instructions:

1. **Environment Setup**:
   Ensure that Python (preferably Python 3.6 or higher) is installed on your machine.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/alireza-soltaninezhad/speech_to_text.git
   cd speech_to_text
   ```

3. **Install Dependencies**:
   If your project requires additional dependencies (like OpenAI's Whisper or ReportLab), make sure they are listed in a `requirements.txt` file. If they are, you can install them using:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main_filename.py
   ```
   Replace `main_filename.py` with the actual filename containing the main code.

---

## Libraries and Functions Used:

1. **tkinter**: 
   - This library provides tools to create Graphical User Interfaces.
   - Used functions and classes:
     - `Tk`: For the main application window.
     - `Label`: To display text or images.
     - `Button`: For clickable buttons.
     - `StringVar`: To handle string variables in tkinter.
     - `filedialog`: To provide the file dialog function that lets users select files.
     - `OptionMenu`: Dropdown menu widget.
     - `DISABLED`, `NORMAL`: Constants to set the state of widgets.

2. **os**:
   - This library provides a way of using operating system-dependent functionality.
   - Used functions:
     - `os.environ`: A mapping object representing the environment. Used to silence Tkinter deprecation warnings.

3. **whisper**:
   - OpenAI's Whisper ASR system used to transcribe the audio.
   - Used functions:
     - `load_model`: Load a Whisper model for transcription.

4. **reportlab**:
   - This library is used for creating complex PDF documents.
   - Used modules and functions:
     - `pagesize`: To define the size of pages in a PDF document (used the `letter` size).
     - `canvas`: Used to define the canvas of the PDF where text and graphics are drawn.

5. **ttk**:
   - Themed versions of certain tkinter widgets. 
   - Used widgets:
     - `Progressbar`: A widget to show the progress of certain operations.

6. **textwrap**:
   - Text wrapping and filling.
   - Used functions:
     - `wrap`: Wrap a single paragraph of text.

7. **re**:
   - This library provides support for regular expressions.
   - Used functions:
     - `sub`: Used for string substitution using regex patterns.

---

```


