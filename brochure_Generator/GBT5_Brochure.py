# imports
import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI

# Initialize and constants
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and len(api_key) > 10:
    print("✓ API key looks good")
else:
    print("⚠ Warning: API key issue detected. Please check your .env file!")
    
MODEL = 'gpt-5-nano'  #you can choose any model you want 
openai = OpenAI()

# First step: Have GPT figure out which links are relevant

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(url):
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company, 
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt

def select_relevant_links(url):
    print(f"🔍 Selecting relevant links for {url} by calling {MODEL}")
    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": link_system_prompt},
                {"role": "user", "content": get_links_user_prompt(url)}
            ],
            response_format={"type": "json_object"}
        )
        result = response.choices[0].message.content
        links = json.loads(result)
        print(f"✓ Found {len(links['links'])} relevant links")
        return links
    except Exception as e:
        print(f"⚠ Error selecting links: {e}")
        return {"links": []}

# Second step: make the brochure!

def fetch_page_and_all_relevant_links(url):
    print(f"📄 Fetching page content and relevant links...")
    contents = fetch_website_contents(url)
    relevant_links = select_relevant_links(url)
    result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
    for link in relevant_links['links']:
        result += f"\n\n### Link: {link['type']}\n"
        try:
            result += fetch_website_contents(link["url"])
        except Exception as e:
            print(f"⚠ Could not fetch {link['url']}: {e}")
    return result

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_all_relevant_links(url)
    user_prompt = user_prompt[:5_000]  # Truncate if more than 5,000 characters
    return user_prompt

def create_brochure(company_name, url):
    print(f"📝 Creating brochure for {company_name}...")
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": brochure_system_prompt},
                {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
            ],
        )
        result = response.choices[0].message.content
        display(Markdown(result))
        return result
    except Exception as e:
        print(f"⚠ Error creating brochure: {e}")
        return None

# Stream version with typewriter animation
def stream_brochure(company_name, url):
    print(f"📝 Streaming brochure for {company_name}...")
    try:
        stream = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": brochure_system_prompt},
                {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
            ],
            stream=True
        )    
        response = ""
        display_handle = display(Markdown(""), display_id=True)
        for chunk in stream:
            if chunk.choices[0].delta.content:
                response += chunk.choices[0].delta.content
                update_display(Markdown(response), display_id=display_handle.display_id)
        return response
    except Exception as e:
        print(f"⚠ Error streaming brochure: {e}")
        return None

def main():
    """
    Main function to generate company brochures.
    Prompts user for company name and URL via terminal input.
    """
    print("=" * 60)
    print("Company Brochure Generator".center(60))
    print("=" * 60)
    print()
    
    # Get user input from terminal
    company_name = input("Enter the company name: ").strip()
    url = input("Enter the company website URL (e.g., https://example.com): ").strip()
    
    # Validate inputs
    if not company_name:
        print("⚠ Error: Company name cannot be empty!")
        return
    
    if not url.startswith(('http://', 'https://')):
        print("⚠ Error: URL must start with http:// or https://")
        return
    
    print(f"\n🚀 Generating brochure for {company_name}...\n")
    
    # Use streaming version for better UX
    # Change to create_brochure() if you don't want streaming
    result = stream_brochure(company_name, url)
    
    if result:
        print("\n" + "=" * 60)
        print("✓ Brochure generation complete!".center(60))
        print("=" * 60)
    else:
        print("\n⚠ Brochure generation failed. Please try again.")

if __name__ == "__main__":
    main()