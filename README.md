# CentiBot
 This code is a relatively simple program that implements an intellegent chat bot named "CentiBot."

 The program can `"read"` documents (.pdf,.txt) or code `(.py,.hpp,.cpp)` and accurately answer questions on the contents.

 The program requires an API Key to OpenAI. Place your key at the top of both read.py and chat.py files. Alternatively, add your key to your environment variables.
 
 The code is written in Python, and requires quite a few dependencies, run the following command to install all required modules.

### Installation

1. **Clone the repository:**

    ```python
    git clone https://github.com/aditya-dom/Centibot.git
    cd CentiBot
    ```

2. **Create a virtual environment and activate it:**

    ```python
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```python
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**

    Copy the `.env.example` to `.env` and update it with your OpenAI API key.

    ```bash
    cp .env.example .env
    ```

    Update the `.env` file:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```
***
> [!NOTE]
> If you are on a Windows machine, replace requirements.txt with requirements_windows.txt. You will also need to install Microsoft C++ Build Tools (visualstudio.microsoft.com/visual-cpp-build-tools)

***

## Running the Application

Start the FastAPI application:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```