# src/agents/real_ai_generator_agent.py

import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()   # Load GROQ_API_KEY from .env

API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

def generate_real_ai_solution(problem_text, temperature=0.2):
    """
    Uses GROQ API (Llama-3 / Mixtral) to generate a real C++ CP solution.
    """
    try:
        resp = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Write a clean, efficient, competitive-programming style C++ solution "
                        "for the following problem. Return ONLY valid C++ code, no explanation:\n\n"
                        f"{problem_text}"
                    )
                }
            ],
            temperature=temperature,
            max_tokens=2048
        )
        ai_code = resp.choices[0].message["content"]
        return ai_code

    except Exception as e:
        print("Groq API Error:", e)
        return "// AI generation failed. Returning empty code.\nint main(){return 0;}"


def generate_ai_samples_for_problem(problem_text, outdir, num=3):
    """
    Generates multiple AI solutions for comparison.
    Saves them inside run directory.
    """
    samples = []

    for i in range(num):
        print(f"[AI SAMPLE] Generating sample {i+1}/{num}...")
        ai_code = generate_real_ai_solution(problem_text)

        filename = os.path.join(outdir, f"ai_sample_{i}.cpp")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ai_code)

        samples.append(filename)
        time.sleep(1)   # avoid rate limits

    print("[AI SAMPLE] Done.")
    return samples
