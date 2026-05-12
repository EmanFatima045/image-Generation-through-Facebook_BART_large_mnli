# 🎯 AI Image Tool Recommender

A smart AI-powered system that analyzes your image prompt and recommends the **best AI image generation tool** using:

🧠 facebook/bart-large-mnli (Zero-Shot Learning)

---

## 🚀 Overview

This project takes a user prompt and intelligently decides which AI tool is best suited to generate the image.

Instead of guessing manually, the model analyzes meaning and context.

---

## ✨ Features

- 🧠 Zero-shot AI classification using BART MNLI
- 🎯 Supports multiple AI image tools
- 📊 Score-based ranking system
- ⚡ Fast CLI terminal interface
- 💡 Intelligent prompt understanding
- 🔥 Works without training dataset

---

## 🧠 Supported AI Tools

| Tool | Best For |
|------|---------|
| 🎨 Midjourney | Artistic & cinematic images |
| 🖼️ DALL·E 3 | Realistic & accurate images |
| ⚡ Stable Diffusion | Custom & advanced control |
| 🎯 Canva AI | Social media & marketing |
| 🔥 Adobe Firefly | Professional commercial design |
| ⚙️ Leonardo AI | Game assets & character design |

---

## 🔍 How It Works

1. User enters a prompt  
2. Model analyzes meaning using **BART MNLI**  
3. Prompt is matched against tool descriptions  
4. Each tool gets a score (0–100)  
5. Best tool is selected and displayed  

---

## ⚙️ Installation

```bash
git clone https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli.git
cd image-Generation-through-Facebook_BART_large_mnli
pip install -r requirements.txt
