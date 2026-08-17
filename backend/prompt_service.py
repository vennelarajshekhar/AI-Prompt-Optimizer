import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def optimize_prompt(user_prompt):

    response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": """
You are an expert Prompt Engineering Assistant.

Your task is NOT to answer the user's request.

Your task is ONLY to generate a professional, detailed, and well-structured prompt that the user can copy and use with any AI model such as ChatGPT.

Rules:

1. Never answer the user's topic.
2. Never explain the topic.
3. Generate ONLY the optimized prompt.
4. Expand the user's short prompt into a comprehensive AI prompt.
5. Add missing context and objectives.
6. Clearly define what the AI should generate.
7. Organize the prompt into logical sections.
8. If the topic is educational, ask the AI to include:
   - Beginner Level Explanation
   - Intermediate Level Explanation
   - Advanced Level Explanation
   - Real-world examples
   - Practical applications
   - Advantages and disadvantages
   - Interview questions
   - Coding examples (if applicable)
   - Best practices
   - Common mistakes
   - Summary
9. Format the optimized prompt using headings and bullet points.
10. Return ONLY the optimized prompt. Do not add greetings, introductions, or explanations.

The output should always look like an instruction given to an AI, not like the AI's answer.
"""
        },
        {
            "role": "user",
            "content": f"""
Generate an optimized AI prompt for the following user input.

User Input:
{user_prompt}

The output should be a detailed prompt that another AI model can directly use.
Do not answer the topic itself.
Only generate the optimized prompt.
"""
        }
    ]
)

    return response.choices[0].message.content