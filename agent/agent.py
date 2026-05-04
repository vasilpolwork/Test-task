import anthropic
import os
import glob

# Fetch model name from environment variables
MODEL_NAME = os.environ.get("MODEL_NAME")

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def improve_file(file_path):
    print(f"Processing {file_path}...")

    with open(file_path, "r") as f:
        content = f.read()

    # Strict system prompt to ensure English comments and clean code output
    system_prompt = (
        "You are an expert SRE and Python developer. Your goal is to improve the provided code: "
        "fix bugs, add documentation, optimize performance, or add small useful features. "
        "IMPORTANT: All comments, documentation, and docstrings MUST be in English. "
        "Return ONLY the improved code content without any markdown blocks, explanations, or triple backticks."
    )

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        system=system_prompt,
        messages=[
            {"role": "user", "content": f"Improve this code:\n\n{content}"}
        ]
    )

    improved_code = response.content[0].text.strip()

    # Cleaning up potential markdown artifacts
    if improved_code.startswith("```"):
        lines = improved_code.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines[-1].strip() == "```":
            lines = lines[:-1]
        improved_code = "\n".join(lines).strip()

    if improved_code and improved_code != content:
        with open(file_path, "w") as f:
            f.write(improved_code)
        return True
    return False

if __name__ == "__main__":
    # Scan for all Python files in the app directory
    files = glob.glob("app/*.py")
    changes_made = False

    for file in files:
        if improve_file(file):
            changes_made = True
            print(f"Successfully improved {file}")

    if not changes_made:
        print("No improvements suggested by AI.")