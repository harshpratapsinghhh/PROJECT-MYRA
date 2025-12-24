**MYRA — Multimodal Yielding Responsive Assistant**

MYRA is a Jarvis-inspired personal AI assistant that combines a Python-based intelligence engine with a lightweight web-based visual interface.
The project focuses on modular design, voice interaction, and a futuristic neural-style visualization.

MYRA is designed as a foundation for building more advanced, autonomous assistant systems.

**Features**
**Backend (Python)**

Voice recognition and command processing

Text-to-speech response system

Music playback control

Web search and Wikipedia summaries

System information (time, date, battery)

Modular command execution architecture

Wake-word based activation

**Frontend (Web Interface)**

Neural-style animated visualization

Activation pulse and listening feedback

Clean HTML, CSS, and JavaScript

Runs directly in the browser without frameworks

**Project Structure**
MYRA/
│
├── main.py                 # Main assistant loop
├── server.py               # Backend to frontend communication
│
├── core/
│   ├── speak.py            # Text-to-speech module
│   ├── listen.py           # Speech recognition module
│   ├── commands.py         # Command mapping
│   ├── executor.py         # Action execution logic
│   ├── trigger.py          # Wake-word detection
│   └── music.py            # Music handling
│
├── frontend/
│   ├── index.html          # Visual interface
│   ├── style.css           # UI styling
│   └── script.js           # Animation and interaction logic
│
└── README.md

**Requirements**

Python 3.9+

Microphone access

**Python Dependencies**
speechrecognition
gtts
wikipedia
psutil
flask
pyaudio

**Installation**

Install required Python packages:

pip install -r requirements.txt


(If PyAudio fails on Windows, install using a precompiled wheel.)

**Usage**

Start the backend server:

python server.py


Run the assistant:

python main.py


Open the frontend interface:
Open frontend/index.html in a web browser.

**Example Commands**

"Myra play music"

"Open YouTube"

"What is artificial intelligence"

"Battery status"

"What time is it"

"Stop music"

**Design Principles**

Separation of UI and logic

Modular and extensible architecture

Minimal dependencies

Readable and maintainable code

**Future Enhancements**

Real-time audio visualization

Face recognition and computer vision

Persistent memory and learning

Home automation integration

Advanced command context handling

**Author**

Harsh Pratap Singh
