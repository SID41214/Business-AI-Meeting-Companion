🚧 Project Status

This repository hosts a personal project that is **currently in the active development phase**.

* **Status:** In Progress / Work in Progress
* *For inquiries or further information, please contact me directly at sidhub41214@gmail.com.*
--------------------------------------------------------------------------------------------------------------------------------
# 🎙️ Business AI Meeting Companion STT

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Interface-Gradio-orange)](https://www.gradio.app/)
[![LLM](https://img.shields.io/badge/LLM-Llama%203%20%2F%20WatsonX-red)](https://www.ibm.com/products/watsonx)

## ✨ Project Introduction

The **Business AI Meeting Companion STT** is an advanced AI application designed to capture, transcribe, summarize, and extract key insights from business meeting conversations.

This project demonstrates the powerful integration of Speech-to-Text (STT) technology with Large Language Models (LLMs) to transform raw audio into structured, actionable business intelligence.The resulting application not only provides high-accuracy transcriptions but also concise summaries, emphasizing key points and decisions made during the meeting.

### 💡 Key Capabilities

This lab-based project covers the creation of the following core functionalities:

* **Accurate Speech-to-Text (STT):** Utilizes **OpenAI's Whisper** technology to accurately convert audio recordings (like lecture recordings) into text.
* **Intelligent Summarization:** Implements **IBM Watson's AI** to effectively summarize transcribed text and extract crucial key points.
* **Prompt Engineering:** Establishes a structured **Prompt Template** using `langchain` to guide the LLM's output and ensure organizational consistency.
* **User Interface:** Develops an intuitive and user-friendly web interface using **Hugging Face Gradio**.
* **LLM Integration:** Demonstrates how to generate text and integrate services like **Llama 3** (via IBM WatsonX) using `ibm_watson_machine_learning` and `langchain`.

---

## 🛠️ Technology Stack

The project relies on the following key tools and libraries:

| Component | Library/Tool | Role |
| :--- | :--- | :--- |
| **Speech-to-Text** | `OpenAI Whisper` | Generates highly accurate transcripts from audio files. |
| **LLM Service** | `IBM WatsonX` (using Llama 3) | Provides the LLM for summarization and key point extraction. |
| **Interface** | `Hugging Face Gradio` | Creates the web application UI for audio upload and text output. |
| **Orchestration** | `LangChain` | Used for prompt templating and chaining the STT output to the LLM. |
| **Dependencies** | `transformers`, `torch`, `ibm_watson_machine_learning` | Core libraries for handling models and accessing IBM services. |
| **Audio Handling** | `ffmpeg` | Required to enable Python to work effectively with audio files. |

---

## ⚙️ Getting Started

Follow these steps to set up the environment and run the application.

### Prerequisites

* Python 3+
* Git
* Administrative access to install `ffmpeg` (e.g., `sudo apt install ffmpeg -y` on Linux).
* Access to IBM WatsonX or appropriate API keys for the chosen LLM (OpenAI/HuggingFace).

### 1. Environment Setup

Use `virtualenv` to create and activate a dedicated Python environment:

```bash
# Install virtualenv if needed
pip3 install virtualenv 

# Create a virtual environment named 'my_env'
virtualenv my_env 

# Activate the environment
source my_env/bin/activate # For macOS/Linux 
# or .\my_env\Scripts\activate # For Windows
```
### 2. Install Dependencies
Install the required libraries, including specific version constraints used in the lab:

```
pip install transformers==4.36.0 torch==2.1.1 gradio==5.23.2 langchain==0.0.343 ibm_watson_machine_learning==1.0.335 huggingface-hub==0.28.1 
```
### 3. Install FFmpeg

Install ffmpeg for audio file handling:

```
sudo apt update 
sudo apt install ffmpeg -y
```
(Changes according to the terminal)
### 4. Running the Complete Application

The final integrated application is created in the file speech_analyzer.py. This script combines the Whisper STT model, the LLM prompt template, and the Gradio interface.

To run the application:

```

# Ensure your 'my_env' is active
python3 speech_analyzer.py 
The Gradio web application will typically launch on a local host port (e.g., http://0.0.0.0:7860).
```

### Core Application Logic
The project's key functions are demonstrated through several steps:
#### A. Speech-to-Text Implementation (simple_speech2text.py)
-  This step uses the Hugging Face transformers library with the openai/whisper-tiny.en model to create a speech recognition pipeline.




#### Initialization
```
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-tiny.en", chunk_length_s=30)

# Transcription
prediction = pipe(sample, batch_size=8)["text"] 
```
#### B. LLM Integration Example (simple_llm.py)
This demonstrates setting up the Llama 3 model via WatsonxLLM for text generation, defining key parameters like MAX_NEW_TOKENS and TEMPERATURE:



##### Model initialization uses specific credentials, parameters, and project ID 
```
LLAMA3_model = Model(model_id='meta-llama/llama-3-2-11b-vision-instruct', ...) 
llm = WatsonxLLM(LLAMA3_model) 

# Text generation
print(llm("How to read a book effectively?")) 
```
#### C. Final Chain (speech_analyzer.py)
The final application connects the components via a PromptTemplate and LLMChain:
- Transcription: transcript_audio(audio_file) function converts uploaded audio to text using Whisper.
- Prompting: The transcribed text (transcript_txt) is passed to an LLMChain object, which integrates it with a Llama 2/3 structured prompt template.
- Summarization: The LLMChain sends the prompt to the LLM (e.g., WatsonxLLM) to generate the final summarized output, which is then returned.
--------------------------------------------------------------------------------------------------------------------------------
<img width="1913" height="887" alt="1" src="https://github.com/user-attachments/assets/7b520b5f-c005-4afd-8fd9-7f55c8bff475" />
<img width="1918" height="887" alt="2" src="https://github.com/user-attachments/assets/3076d868-bb86-4ee1-b2cc-b2697050ee37" />
<!-- <img width="1897" height="607" alt="3" src="https://github.com/user-attachments/assets/825441b5-23cb-4320-b68c-53f65483a5d7" /> -->
<img width="1920" height="887" alt="4" src="https://github.com/user-attachments/assets/ff34e44e-0cd7-4b76-8738-ad0ee090e2e6" />
<img width="820" height="585" alt="5" src="https://github.com/user-attachments/assets/b45fb3e7-b1dc-4d7d-a134-663406daef8e" />
