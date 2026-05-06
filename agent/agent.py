import anthropic
import os
import glob
from datetime import datetime

# Model is retrieved from environment variables
MODEL_NAME = os.environ.get("MODEL_NAME", "").strip()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def process_with_ai(prompt, content):
    system_prompt = (
        "You are a professional SRE and Python developer. "
        "CRITICAL: All code comments, documentation, and text MUST be in ENGLISH ONLY. "
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
    # Search for all Python files in the app/ directory
    files = glob.glob("app/*.py")
    all_summaries = []
    app_context = ""

    # Ensure the app directory exists
    if not os.path.exists("app"):
        print("Directory 'app/' not found.")
        return

    # 1. Code improvement and context gathering
    for file_path in files:
        with open(file_path, "r") as f:
            original_code = f.read()

        app_context += f"\n--- File: {os.path.basename(file_path)} ---\n{original_code}\n"

        print(f"Improving {file_path}...")
        improvement_prompt = "Improve this code. Fix bugs, optimize, and ensure ALL comments are in English."
        improved_code = process_with_ai(improvement_prompt, original_code)

        if improved_code and improved_code != original_code:
            with open(file_path, "w") as f:
                f.write(improved_code)

            summary = process_with_ai("Describe what you changed in this code in exactly 5-7 words (in English).", improved_code)
            all_summaries.append(f"{os.path.basename(file_path)}: {summary}")

    if not all_summaries:
        print("No changes made.")
        return

    # 2. Update app/README.md
    app_readme_path = "app/README.md"
    current_readme = ""
    if os.path.exists(app_readme_path):
        with open(app_readme_path, "r") as f:
            current_readme = f.read()

    print(f"Updating {app_readme_path}...")
    readme_prompt = (
        "Update the professional README.md for the 'app/' directory in ENGLISH. "
        f"Context of all files:\n{app_context}\n\n"
        f"Include these recent changes:\n{all_summaries}"
    )
    new_readme = process_with_ai(readme_prompt, current_readme)
    with open(app_readme_path, "w") as f:
        f.write(new_readme)

    # 3. Update CHANGELOG.md (Root directory)
    changelog_path = "CHANGELOG.md"
    current_changelog = ""
    if os.path.exists(changelog_path):
        with open(changelog_path, "r") as f:
            current_changelog = f.read()

    print(f"Updating {changelog_path}...")
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    changes_list = "\n".join([f"- {s}" for s in all_summaries])

    # Generate a professional entry for the changelog
    changelog_entry_prompt = (
        f"Create a professional changelog entry in Markdown for the date {date_str}. "
        f"Summarize these changes clearly:\n{changes_list}"
    )
    new_entry = process_with_ai(changelog_entry_prompt, "")

    # Prepend the new entry to the top of the file
    with open(changelog_path, "w") as f:
        f.write(f"## [{date_str}]\n\n{new_entry}\n\n{current_changelog}")

    # 4. Finalize commit message
    print("Generating detailed commit message...")

    # We ask the AI to format all collected summaries into a professional Git commit
    commit_prompt = (
        "Create a professional Git commit message based on these changes. "
        "Use Conventional Commits format. "
        "Header: feat(auto): AI-driven code improvement and docs update\n"
        "Body: List all changes as bullet points.\n"
        f"Changes list:\n{all_summaries}"
    )

    detailed_commit_msg = process_with_ai(commit_prompt, "")

    with open(".commit_msg", "w") as f:
        # We ensure the message is written exactly as AI generated it
        f.write(detailed_commit_msg)

if __name__ == "__main__":
    main()