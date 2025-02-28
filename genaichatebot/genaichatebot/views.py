from django.shortcuts import render
import google.generativeai as genai 
import markdown



# config gen API
genai.configure(api_key="Your API key")

# gemini model
model=genai.GenerativeModel("gemini-1.5-pro")



def home(request):
    response_text = ""
    user_query = ""

    if request.method == "POST":
        user_query = request.POST.get("question")
        if user_query:
            response = model.generate_content(user_query)
            response_text = markdown.markdown(response.text)  # Convert Markdown to HTML

    return render(request, "home.html", {"response_text": response_text, "user_query": user_query})
