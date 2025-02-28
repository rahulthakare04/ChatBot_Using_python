from django.shortcuts import render
import google.generativeai as genai 
import markdown

# response_text = markdown.markdown(gemini_response)  # Convert Markdown to HTML



# config gen API
genai.configure(api_key="AIzaSyA_C_S5FXV5r9blQACJUeSzrlv_BUm59MQ")

# gemini model
model=genai.GenerativeModel("gemini-1.5-pro")

# response funtion
# def get_gemini_responce(question):
#     response=model.generate_content(question)
#     return response.text

def home(request):
    response_text = ""
    user_query = ""

    if request.method == "POST":
        user_query = request.POST.get("question")
        if user_query:
            response = model.generate_content(user_query)
            response_text = markdown.markdown(response.text)  # Convert Markdown to HTML

    return render(request, "home.html", {"response_text": response_text, "user_query": user_query})
