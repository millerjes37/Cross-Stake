import requests
import os

# Define the API endpoint and headers for Claude 3.5 Sonnet
claude_api_url = "https://api.claude.com/parse-pdf"
headers = {
    'Authorization': f"Bearer {os.getenv('CLAUDE_API_KEY')}",
    'Content-Type': 'application/pdf'
}

def parse_pdf_with_claude(pdf_path):
    # Read the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_content = file.read()

    # Send the PDF file and prompt to Claude
    response = requests.post(
        claude_api_url,
        headers=headers,
        files={'file': ('race_calendar.pdf', pdf_content, 'application/pdf')}
    )

    # Extract the JSON string from the response
    if response.status_code == 200:
        json_string = response.json()
        return json_string
    else:
        print(f"Failed to parse PDF with Claude: {response.status_code}")
        return None

if __name__ == "__main__":
    pdf_path = 'race_calendar.pdf'
    json_string = parse_pdf_with_claude(pdf_path)
    print(f"Parsed JSON:\n{json_string}")
