# Ai-Agent-On-Pi5
From a bare board to a glowing brain! 🧠 Thrilled to share my latest full-stack project, starting with a serious hardware upgrade for my Raspberry Pi 5.

<div align="center">

# Project Pironman: An AI-Powered & Monitored Raspberry Pi 5 Server

**A comprehensive guide to transforming a Raspberry Pi 5 into an intelligent, voice-less, text-based server with a stunning DIY hardware makeover and a full-stack, real-time performance dashboard.**

</div>

<p align="center">
  <img alt="Pironman 5 Build" src="WhatsApp Image 2025-09-26 at 21.58.31.jpeg" width="600">
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img alt="Prometheus" src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white">
  <img alt="Grafana" src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white">
  <img alt="Raspberry Pi" src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white">
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [✨ Key Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [🚀 The Build & Setup Process](#-the-build--setup-process)
  - [Part 1: The Hardware Makeover (Pironman 5)](#part-1-the-hardware-makeover-pironman-5)
  - [Part 2: The Brain (A Local, Text-Based AI Agent)](#part-2-the-brain-a-local-text-based-ai-agent)
  - [Part 3: The Vitals (Real-Time Performance Monitoring)](#part-3-the-vitals-real-time-performance-monitoring)
- [🕹️ How to Use the System](#️-how-to-use-the-system)
- [🚨 Troubleshooting Guide](#-troubleshooting-guide)
- [💡 Future Improvements](#-future-improvements)
- [📜 License](#-license)

---

## 📝 Overview

This project documents the journey of elevating a standard Raspberry Pi 5 from a bare board to a sophisticated, intelligent server. The transformation follows three key stages:

1.  **The Physical Build:** A hardware makeover using the **SunFounder Pironman 5 case**, providing superior aesthetics, protection, and thermal management.
2.  **The Intelligent Interface:** Development of a **100% local, text-based AI agent**. This agent runs on the Pi, understands natural language, and can execute shell commands to manage the system, acting as a conversational interface to the headless server.
3.  **The Observability Stack:** Implementation of an **enterprise-grade monitoring dashboard** using Prometheus and Grafana, providing deep insights into the server's real-time performance.

The result is a powerful, self-contained, and fully observable homelab server, perfect for any tech enthusiast.

---

## ✨ Key Features

-   **🤖 Local AI Agent:** A text-based conversational interface to the server's command line, powered by a local LLM.
-   **📊 Comprehensive Monitoring:** A stunning Grafana dashboard visualizes CPU, memory, disk I/O, network traffic, and system temperature.
-   **💎 Premium Hardware Build:** A sleek, sturdy, and well-cooled setup thanks to the Pironman 5 case.
-   **🌐 Headless & Remotely Accessible:** Designed for a headless Ubuntu Server, with secure remote access provided by Tailscale.
-   **🐳 Clean & Modern Stack:** Leverages best practices like Docker for services and Python `venv` for dependency management.

---

## 🛠️ Technology Stack

| Component         | Technology                 | Purpose                                     |
| ----------------- | -------------------------- | ------------------------------------------- |
| **Hardware** | Raspberry Pi 5, Pironman 5 Case | The physical server and its enclosure.      |
| **OS** | Ubuntu Server              | Headless OS running on the Pi.              |
| **LLM Engine** | Ollama (`qwen2:1.5b`)      | Local language model inference.             |
| **Agent Logic** | Python 3 (`venv`)          | The main script that runs the agentic loop. |
| **Remote Access** | Tailscale                  | Secure shell access from any network.       |
| **Metrics Agent** | Prometheus Node Exporter   | Collects system stats on the Pi.            |
| **Metrics DB** | Prometheus (via Docker)    | Scrapes and stores the time-series metrics. |
| **Dashboard** | Grafana (via Docker)       | Creates and displays beautiful dashboards.  |
| **Deployment** | Docker & Docker Compose    | To easily run and manage services on the laptop. |

---

## 🚀 The Build & Setup Process

This guide is broken down into the three core stages of the project.

### Part 1: The Hardware Makeover (Pironman 5)

The foundation of this project is a robust physical build. The Raspberry Pi 5 was housed in the **SunFounder Pironman 5 case**.

This NVMe-compatible case provides:
-   Excellent passive and active cooling with its tower cooler and PWM fan.
-   A sleek, protective aluminum alloy body.
-   Convenient access to all ports and GPIO pins.

> 💡 For detailed instructions on assembling the case itself, please refer to the official [SunFounder Pironman 5 documentation](https://docs.sunfounder.com/en/latest/pironman_5.html).

### Part 2: The Brain (A Local, Text-Based AI Agent)

With the hardware assembled, the next step is to give it a brain.

<details>
<summary><strong>► Click to expand: 2.1 - Install Core AI Dependencies on the Pi</strong></summary>

```bash
# Update system and install necessary tools
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-pip python3-venv


# Install Ollama and pull the model
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
ollama pull qwen2:1.5b


</details>

<details>
<summary><strong>► Click to expand: 2.2 - Set up the Python Agent</strong></summary>

1. Create the Virtual Environment

Bash

# Navigate to your home directory
cd ~
python3 -m venv agent-env

# Activate the environment
source agent-env/bin/activate
2. Install Python Packages
With the (agent-env) active, install the required library:

Bash

pip install ollama
3. Create the agent.py Script
Create a new file agent.py and paste the code below into it.

Python

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
    """The main logic for the agent."""
    system_prompt = """
    You are a helpful AI assistant running on a Raspberry Pi.
    Your goal is to assist the user by running shell commands on the Ubuntu Server.
    You must assess the user's request and decide if a shell command is needed.
    Respond in JSON format with three fields:
    1. "thought": Your reasoning process and a brief explanation of the command if you use one.
    2. "action": Either "shell" if a command is needed, or "speak" if not.
    3. "command_or_speak_text": The exact shell command to run, or the text for you to speak directly.
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

if __name__ == "__main__":
    agent_speak("Agent is online. Type your commands below. Type 'exit' or 'quit' to end.")
    while True:
        prompt = get_user_input()
        if not prompt or prompt.lower() in ["exit", "quit", "goodbye"]:
            agent_speak("Goodbye!")
            break
        run_agentic_loop(prompt)
</details>

Part 3: The Vitals (Real-Time Performance Monitoring)
Finally, we give our server a health dashboard.

<details>
<summary><strong>► Click to expand: 3.1 - Install Node Exporter on the Pi</strong></summary>

Bash

# 1. Download and install Node Exporter
cd ~
wget [https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-arm64.tar.gz](https://github.com/prometheus/node_exporter/releases/download/v1.8.1/node_exporter-1.8.1.linux-arm64.tar.gz)
tar xvfz node_exporter-1.8.1.linux-arm64.tar.gz
sudo mv node_exporter-1.8.1.linux-arm64/node_exporter /usr/local/bin/
rm -rf node_exporter-1.8.1.linux-arm64*

# 2. Create a systemd service to run it on boot
sudo nano /etc/systemd/system/node_exporter.service

# Paste this content into the file:
# [Unit]
# Description=Prometheus Node Exporter
# ... (Full content is in the guide above) ...
# [Install]
# WantedBy=multi-user.target

# 3. Enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
</details>

<details>
<summary><strong>► Click to expand: 3.2 - Set up Prometheus & Grafana on Your Laptop</strong></summary>

Install Docker Desktop and the Tailscale client on your laptop.

Create a new project folder and add the following two files inside it.

Find your Pi's Tailscale IP Address (e.g., 100.x.x.x) and use it in prometheus.yml.

prometheus.yml

YAML

global:
  scrape_interval: 15s
scrape_configs:
  - job_name: 'pironman_pi5'
    static_configs:
      - targets: ['<YOUR_PI_TAILSCALE_IP>:9100']
docker-compose.yml

YAML

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports: ["9090:9090"]
    volumes: ["./prometheus.yml:/etc/prometheus/prometheus.yml"]
    command: ['--config.file=/etc/prometheus/prometheus.yml']
    networks: [monitor-net]
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports: ["3000:3000"]
    volumes: [grafana-data:/var/lib/grafana]
    networks: [monitor-net]
volumes:
  grafana-data:
networks:
  monitor-net:
    driver: bridge
Launch the stack from your terminal in the project folder: docker-compose up -d.
```


</details>

<details>
<summary><strong>► Click to expand: 3.3 - Configure the Grafana Dashboard</strong></summary>

Open your browser to http://localhost:3000.

Log in (admin/admin).

Add Data Source: Go to Connections > Data Sources > Prometheus. Set the URL to http://prometheus:9090 and click "Save & Test".

Import Dashboard: Go to Dashboards > New > Import. Use Grafana.com dashboard ID 1860. Select your Prometheus data source and click "Import".

</details>

🕹️ How to Use the System
To Monitor Performance: Open http://localhost:3000 on your laptop to view the Grafana dashboard.

To Access the Pi Remotely: Use ssh your_user@<PI_TAILSCALE_NAME_OR_IP> from any machine on your Tailscale network.

To Talk to the Agent: SSH into the Pi, activate the venv (source ~/agent-env/bin/activate), and run python3 agent.py.

🚨 Troubleshooting Guide
<details>
<summary><strong>Problem: pip install fails with externally-managed-environment.</strong></summary>
✅ Solution: Always use a Python virtual environment (venv) for projects to isolate dependencies from the system. The instructions in this guide follow this best practice.
</details>

<details>
<summary><strong>Problem: docker-compose up fails with address already in use for port 3000.</strong></summary>
✅ Solution: Another service is using the port. Change the port mapping in docker-compose.yml under grafana from &quot;3000:3000&quot; to &quot;3001:3000&quot; and access Grafana at http://localhost:3001.
</details>

<details>
<summary><strong>Problem: In Grafana, I get a lookup prometheus: no such host error.</strong></summary>
✅ Solution: This is a Docker networking issue. The docker-compose.yml file provided solves this by creating an explicit monitor-net network that both services join. Ensure your file matches.
</details>

💡 Future Improvements
Expand Agent Tools: Give the agent the ability to interact with APIs (e.g., weather, home automation).

Implement Memory: Add a vector database for semantic memory, allowing the agent to recall past conversations.

Expand Monitoring: Add exporters for specific services running on the Pi (e.g., a Pi-hole exporter or container monitoring with cAdvisor).

**High-Level Overview
**

```bash
+--------------------------------+
                  |                                |
 (Your Laptop)    |         TAILSCALE NETWORK      |    (Raspberry Pi 5)
+-------------+   |        (Secure VPN)          |   +-------------------+
|             |   |                                |   |                   |
|   Grafana   |<~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~>|   Pironman 5 Case   |
|      &      |<~ ~ ~ SSH & Metrics Data ~ ~ ~ ~ ~ ~>|          +          |
|  Prometheus |   |                                |   |      Agent AI     |
|             |   |                                |   |                   |
+-------------+   +--------------------------------+   +-------------------+
```

📜 License

This project is licensed under the MIT License.
