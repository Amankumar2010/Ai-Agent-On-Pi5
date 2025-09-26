# Ai-Agent-On-Pi5
From a bare board to a glowing brain! 🧠 Thrilled to share my latest full-stack project, starting with a serious hardware upgrade for my Raspberry Pi 5.

<div align="center">

# Project Pironman: An AI-Powered & Monitored Raspberry Pi 5 Server

**A comprehensive guide to transforming a Raspberry Pi 5 into an intelligent, voice-less, text-based server with a stunning DIY hardware makeover and a full-stack, real-time performance dashboard.**

</div>

<p align="center">
  <img alt="Pironman 5 Build" src="pironman5.jpg" width="600">
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
