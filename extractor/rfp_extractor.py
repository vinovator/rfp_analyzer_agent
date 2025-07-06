from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key = OPENAI_API_KEY)

def generate_prompt(rfp_text):
    return f"""
You are an AI assistant that extracts structured information from a Request for Proposal (RFP).

Here is the RFP text:
\"\"\"
{rfp_text}
\"\"\"

Extract and return the following fields in JSON format:
- Title
- Reference number
- Issued date
- Closing date
- Eligibility criteria
- Submission Instructions
- Evaluation Criteria
- Required Documentation
- Contact information
    """


def extract_rfp_info(rfp_text):
    prompt = generate_prompt(rfp_text)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a helpful assistant that extracts structured info from business documents"},
            {"role": "user", "content": prompt}
        ],
        temperature = 0.2 # Low randomness; good for extraction tasks
    )
    return response.choices[0].message.content