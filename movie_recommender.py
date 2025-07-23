import requests
from IPython.display import display, Markdown

def get_movie_recommendations(language, genre, top_n=10, model='llama3.2'):
    api_url = "http://localhost:11434/api/generate"
    prompt = (
        f"Recommend {top_n} well-rated {language} movies from the {genre} genre. "
        "For each movie, provide the name and a 1-2 sentence preview of its story. "
        "Return the results as a Markdown table with columns: Title, Short Summary."
    )
    data = {
        "model": model,
        "prompt": prompt,
        "options": {"num_predict": 800},
        "stream": False
    }
    response = requests.post(api_url, json=data)
    return response.json().get("response", "").strip()

# User inputs (can be replaced with static values for testing)
language = input("Enter preferred language (e.g., French, Japanese): ").strip()
genre = input("Enter preferred genre (e.g., Drama, Comedy, Thriller): ").strip()

# Generate and display recommendations
recommendations_md = get_movie_recommendations(language, genre)
display(Markdown(recommendations_md))
