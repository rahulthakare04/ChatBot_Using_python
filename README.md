# RahulGPT: AI Chatbot using Gemini API

RahulGPT is an interactive chatbot powered by Google Gemini API, built with Django. It allows users to ask questions and receive AI-generated responses in a friendly chat interface.

## Features
- Uses Google Gemini API for AI-powered responses
- Interactive chat interface with user-friendly UI
- Supports Markdown-formatted responses
- Built using Django framework

  ## Video Execution
  
  https://github.com/user-attachments/assets/d7057cf9-8474-44a4-b768-0b016d84da91






## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/rahulgpt.git
   cd rahulgpt
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install django google-generativeai markdown
   ```

4. **Configure Google Gemini API Key:**
   Replace `"Your API key"` in `views.py` with your actual Google Gemini API key.

5. **Run Migrations (if needed):**
   ```sh
   python manage.py migrate
   ```

6. **Run the Django Development Server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the Application:**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Project Structure
```
rahulgpt/
│── templates/
│   ├── home.html  # Chatbot UI
│── chatbot/
│   ├── views.py   # Django views with Gemini API
│── manage.py
│── requirements.txt
│── README.md
```

## Usage
1. Enter your query in the text box.
2. Click the "Ask" button.
3. The AI will respond based on the input provided.

## License
This project is open-source and available for modification and distribution under the MIT License.

