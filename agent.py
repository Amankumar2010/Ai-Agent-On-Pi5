import ollama
import subprocess
import json

def agent_speak(text):
    """Prints the agent's response to the terminal."""
    print(f"\n🤖 Agent: {text}")

def get_user_input():
    """Gets input from the user's keyboard."""
    return input(f"\n👤 You: ")

def run_agentic_loop(user_prompt):
    """The main logic for the agent. This remains the powerful core."""
    system_prompt = """
    You are a helpful AI assistant running on a Raspberry Pi.
    Your goal is to assist the user by running shell commands on the Ubuntu Server.
    You must assess the user's request and decide if a shell command is needed.
    Respond in JSON format with three fields:
    1. "thought": Your reasoning process and a brief explanation of the command if you use one.
    2. "action": Either "shell" if a command is needed, or "speak" if not.
    3. "command_or_speak_text": The exact shell command to run, or the text for you to speak directly.
    Example: If the user asks 'what is the system uptime', you would respond:
    {"thought": "The user wants the system uptime. The `uptime -p` command will provide this in a human-readable format.", "action": "shell", "command_or_speak_text": "uptime -p"}
    Example: If the user says 'hello', you would respond:
    {"thought": "The user is greeting me. I will greet them back.", "action": "speak", "command_or_speak_text": "Hello there! How can I help you today?"}
    """
    
    print("\n🤔 Agent: Thinking...")
    try:
        response = ollama.chat(
            model='qwen2:1.5b',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ],
            format='json'
        )
        response_data = json.loads(response['message']['content'])
        thought = response_data.get("thought", "I didn't have a clear thought process.")
        action = response_data.get("action")
        command_or_speak_text = response_data.get("command_or_speak_text")

        print(f"🧠 Agent's Thought: {thought}")

        if action == "shell":
            agent_speak("Okay, I will run this command:")
            print(f"   💻 `{command_or_speak_text}`")
            try:
                result = subprocess.run(command_or_speak_text, shell=True, check=True, capture_output=True, text=True)
                output = result.stdout.strip()
                agent_speak(f"Here is the result:\n\n---\n{output}\n---")
            except subprocess.CalledProcessError as e:
                agent_speak(f"An error occurred: {e.stderr.strip()}")
        elif action == "speak":
            agent_speak(command_or_speak_text)
        else:
            agent_speak("I'm sorry, I wasn't sure how to respond to that.")

    except Exception as e:
        agent_speak(f"I encountered an error: {e}")

# --- Main Loop ---
if __name__ == "__main__":
    agent_speak("Agent is online. Type your commands below. Type 'exit' or 'quit' to end.")
    while True:
        prompt = get_user_input()
        if not prompt or prompt.lower() in ["exit", "quit", "goodbye"]:
            agent_speak("Goodbye!")
            break
        run_agentic_loop(prompt)
