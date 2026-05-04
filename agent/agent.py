import anthropic
import os
import glob

# Using model from environment variable with Haiku as fallback
MODEL_NAME = os.environ.get("MODEL_NAME", "").strip() or "claude-3-haiku-20240307"
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def process_with_ai(prompt, content):
    system_prompt = (
        "You are a professional SRE and Python developer. "
        "IMPORTANT: All text MUST be in ENGLISH ONLY. "
        "Return ONLY the requested content without markdown backticks or explanations."
    )

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2048,
        system=system_prompt,
        messages=[{"role": "user", "content": f"{prompt}\n\n{content}"}]
    )
    return response.content[0].text.strip()

def main():
    files = glob.glob("app/*.py")
    all_summaries = []

    # 1. Improve Application Code
    for file_path in files:
        with open(file_path, "r") as f:
            original_code = f.read()

        print(f"Improving {file_path}...")
        improved_code = process_with_ai("Improve this code. Fix bugs, optimize, and add English comments.", original_code)

        if improved_code and improved_code != original_code:
            with open(file_path, "w") as f:
                f.write(improved_code)

            # Generate a 5-word summary of what was done
            summary = process_with_ai("Describe what you changed in this code in exactly 5-7 words.", improved_code)
            all_summaries.append(f"{os.path.basename(file_path)}: {summary}")

    if not all_summaries:
        print("No changes made.")
        return

    # 2. Update README.md
    readme_path = "README.md"
    current_readme = ""
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            current_readme = f.read()

    print("Updating README.md...")
    changes_text = "\n".join([f"- {s}" for s in all_summaries])
    readme_prompt = f"Update this README.md to reflect these recent improvements. Keep it professional and concise:\n{changes_text}"
    new_readme = process_with_ai(readme_prompt, current_readme)

    with open(readme_path, "w") as f:
        f.write(new_readme)

    # 3. Create a commit message file for the workflow
    commit_msg = "feat(auto): " + "; ".join(all_summaries)
    with open(".commit_msg", "w") as f:
        f.write(commit_msg)

if __name__ == "__main__":
    main()