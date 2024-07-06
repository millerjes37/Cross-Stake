import openai
import os

# Load your OpenAI API key from an environment variable or other secure location
openai.api_key = os.getenv('OPENAI_API_KEY')

def parse_pdf_with_openai(pdf_path):
    # Read the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_content = file.read()

    # Send the PDF file and prompt to OpenAI
    response = openai.File.create(
        file=open(pdf_path, 'rb'),
        purpose='answers'
    )
    file_id = response['id']

    # Use the file_id to create an answer
    response = openai.Answer.create(
        file=file_id,
        prompt="Please parse the following PDF document and return the data as a JSON string:",
        max_tokens=2000
    )

    # Extract the JSON string from the response
    json_string = response['answers'][0]
    return json_string

if __name__ == "__main__":
    pdf_path = 'race_calendar.pdf'
    json_string = parse_pdf_with_openai(pdf_path)
    print(f"Parsed JSON:\n{json_string}")
