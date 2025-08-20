import requests
from bs4 import BeautifulSoup

WIKTIONARY_URL = "https://en.wiktionary.org/wiki/"

def fetch_data(word):
    url = f"{WIKTIONARY_URL}{word}"

    try: 
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None 
def parse_latin(html_content):
    if not html_content:
        return ("Could not retrieve page content")
    
    soup = BeautifulSoup(html_content, 'html.parser')
    etymology_heading = soup.find(id="Etymology")

    if etymology_heading: 
        etymology_text_element = etymology_heading.parent.find_next_sibling('p')
        if etymology_text_element and etymology_text_element.text: 
            etymology_text = etymology_text_element.text.strip()
            if "Latin" in etymology_text:
                return etymology_text
            else:
                return etymology_text + "\n" + "..no latin etymology found"
        else: 
            return "no etymology section found"
    else: 
        return "no etymology section recived. google it."

def main():
    print("Hello, knowledge seeker!")
    print("Type a word to find it's latin etymology, or 'quit' to exit.")

    while True: 
            word = input ("\nEnter a word:")
            if word.lower() == 'quit':
                break

            html_content = fetch_data(word)

            if html_content:
                etymology = parse_latin(html_content)
                print(f"Latin etymology for '{word.capitalize()}':")
                print(etymology)
            else: 
                print("No word found. Try another.")

if __name__ == "__main__":
    main()


