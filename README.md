<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=AI%20Image%20Tool%20Recommender&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Intelligent%20prompt%20analysis%20powered%20by%20Zero-Shot%20Learning&descAlignY=55&descSize=16" width="100%"/>

<br/>

<!-- Badges Row 1 -->
<img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/HuggingFace-BART--MNLI-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/Zero--Shot-Classification-FF6B6B?style=for-the-badge&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge"/>

<br/><br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/PRs-Welcome-8B5CF6?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Active-22C55E?style=flat-square"/>
<img src="https://img.shields.io/badge/CLI-Interface-0EA5E9?style=flat-square"/>
<img src="https://img.shields.io/badge/No%20Training%20Data-Required-F59E0B?style=flat-square"/>
<img src="https://img.shields.io/github/stars/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli?style=flat-square&color=yellow"/>

<br/><br/>

> **Stop guessing which AI image tool to use.**  
> Enter your prompt. Get an intelligent, scored recommendation — instantly.

<br/>

<!-- Demo GIF placeholder - replace with your actual demo -->
<img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" width="80%"/>

</div>

---

## 📌 Table of Contents

- [🌟 What Is This?](#-what-is-this)
- [🧠 How It Works](#-how-it-works)
- [🎨 Supported AI Tools](#-supported-ai-tools)
- [⚡ Quickstart](#-quickstart)
- [📦 Installation](#-installation)
- [💻 Usage](#-usage)
- [📊 Example Output](#-example-output)
- [🏗️ Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)

---

## 🌟 What Is This?

<table>
<tr>
<td width="60%">

**AI Image Tool Recommender** is a smart CLI system that analyzes your image generation prompt using **Zero-Shot Learning** and tells you exactly which AI tool will produce the best result.

Powered by **`facebook/bart-large-mnli`** from HuggingFace, it understands the *meaning* and *context* of your prompt — not just keywords — and matches it against the strengths of today's leading AI image tools.

**No training data. No fine-tuning. Just intelligence.**

</td>
<td width="40%" align="center">

```
🖊️  Enter your prompt
        ↓
🧠  BART-MNLI analyzes meaning
        ↓
📊  Scores 6 AI tools (0–100)
        ↓
🏆  Best tool selected
        ↓
💡  Explanation provided
```

</td>
</tr>
</table>

---

## 🧠 How It Works

<div align="center">
<img src="https://mermaid.ink/img/pako:eNptkMFqwzAMhl9F-NRC-wI-lNJ1sMMOg0E3kIPiyIkhmRxiJ2Mo793ZbQZju0j6_n9JliUooxlYgNe6J1cHfIRHC5RMSY6VCFkJnmFzaXa8v9DK5GiS-kJ7v2e3M_nIrB0hFGIAz5b5OB2T-kh2aBcuQVfZhNkLPnGEv8FnXhp1Hl9lKG2_EK5bL3y5e2YRVmNOz_AAAD__wYFaXg" width="700"/>
</div>

<br/>

The model uses **Natural Language Inference** to compare your prompt against descriptions of what each AI tool excels at. Here's the pipeline:

```
User Prompt  ──►  BART-MNLI  ──►  Entailment Scores  ──►  Ranked Tools  ──►  Recommendation
```

| Stage | Description |
|-------|-------------|
| **1. Input** | User types a natural-language image prompt |
| **2. Inference** | BART-MNLI computes entailment score against each tool's capability label |
| **3. Scoring** | Scores are normalized to 0–100 and ranked |
| **4. Output** | Top tool displayed with score breakdown |

---

## 🎨 Supported AI Tools

<div align="center">

| Tool | Score Specialty | Best For |
|------|----------------|----------|
| 🎨 **Midjourney** | Artistic & cinematic flair | Fantasy, concept art, moody aesthetics |
| 🖼️ **DALL·E 3** | Photorealistic & factual accuracy | Product shots, realistic scenes |
| ⚡ **Stable Diffusion** | Technical control & customization | Custom models, fine-tuned outputs |
| 🎯 **Canva AI** | Social media & marketing design | Banners, posts, branded graphics |
| 🔥 **Adobe Firefly** | Commercial-safe professional design | Ad campaigns, editorial content |
| ⚙️ **Leonardo AI** | Game assets & character creation | RPG assets, creature design, UI art |

</div>

---

## ⚡ Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli.git

# 2. Navigate into the project
cd image-Generation-through-Facebook_BART_large_mnli

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the recommender
python main.py
```

---

## 📦 Installation

### Prerequisites

- Python **3.8+**
- pip
- Internet connection (for model download on first run)

### Step-by-step

```bash
# Clone
git clone https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli.git
cd image-Generation-through-Facebook_BART_large_mnli

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# Install requirements
pip install -r requirements.txt
```

### Dependencies

```txt
transformers>=4.30.0
torch>=2.0.0
```

> 💡 On first run, HuggingFace will automatically download the `facebook/bart-large-mnli` model (~1.6 GB). Subsequent runs load from cache and are much faster.

---

## 💻 Usage

```bash
python main.py
```

You'll be greeted by the CLI:

```
╔══════════════════════════════════════════════════╗
║       🎯  AI Image Tool Recommender              ║
║       Powered by facebook/bart-large-mnli        ║
╚══════════════════════════════════════════════════╝

Enter your image prompt: _
```

Type any creative prompt and press Enter.

---

## 📊 Example Output

**Prompt:** *"A dark fantasy knight standing in fog at the edge of a cliff, cinematic lighting"*

```
🔍 Analyzing your prompt...

📊 Tool Scores:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎨 Midjourney          ████████████  94
  ⚙️  Leonardo AI         ████████░░░░  72
  ⚡ Stable Diffusion    ███████░░░░░  65
  🖼️  DALL·E 3            █████░░░░░░░  48
  🔥 Adobe Firefly       ████░░░░░░░░  38
  🎯 Canva AI            ██░░░░░░░░░░  21
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 RECOMMENDATION:  Midjourney  (Score: 94/100)

💡 Why? Your prompt features cinematic, atmospheric, and artistic
   qualities — exactly where Midjourney shines.
```

---

## 🏗️ Project Structure

```
📂 image-Generation-through-Facebook_BART_large_mnli/
│
├── 📄 main.py               # Entry point — CLI interface & orchestration
├── 📄 classifier.py         # BART-MNLI zero-shot classification logic
├── 📄 tools.py              # AI tool definitions and capability labels
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md             # You are here
```

---

## 🤝 Contributing

Contributions are welcome! To add a new AI tool or improve scoring:

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/add-new-tool`
3. **Commit** your changes: `git commit -m 'Add Ideogram AI support'`
4. **Push** to the branch: `git push origin feature/add-new-tool`
5. **Open** a Pull Request

---

<div align="center">

<!-- Footer wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Built with 🧠 by [Eman Fatima](https://github.com/EmanFatima045)**

*If this helped you, please consider giving it a ⭐ — it means a lot!*

[![GitHub Stars](https://img.shields.io/github/stars/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli?style=social)](https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli)

</div>
