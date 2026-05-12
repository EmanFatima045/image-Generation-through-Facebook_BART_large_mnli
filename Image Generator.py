"""
AI Image Tool Recommender — Terminal Script
Run: python ImageGenerator.py
No server needed. Just type your prompt and get a recommendation.
"""

from transformers import pipeline
import torch

# ── Load model ────────────────────────────────────────────────────────────
print("\n⏳ Loading model... (first time downloads ~1.6GB, then cached)\n")
device = 0 if torch.cuda.is_available() else -1
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    device=device
)
print("✅ Model ready!\n")

# ── Tool definitions ──────────────────────────────────────────────────────
TOOLS = {
    "Midjourney": [
        "artistic and painterly image with rich colors and dramatic lighting",
        "cinematic fantasy concept art with intricate details",
        "surrealist or dreamlike illustration with creative composition",
        "epic fantasy landscape or character with cinematic quality",
        "highly stylized aesthetic image with mood and atmosphere",
    ],
    "DALL·E 3": [
        "photorealistic image that looks like a real photograph",
        "accurate and detailed image following the exact description",
        "image with text or words embedded inside it",
        "diverse subject matter rendered with precision and clarity",
        "creative illustration with accurate proportions and details",
    ],
    "Stable Diffusion": [
        "highly customizable image using a fine-tuned or custom model",
        "anime or manga style character or scene",
        "technical image requiring advanced settings and precise control",
        "image requiring ControlNet LoRA or advanced diffusion techniques",
        "unrestricted artistic content with full creative freedom",
    ],
    "Canva AI": [
        "social media graphic or post with clean layout and branding",
        "marketing material like a flyer poster or advertisement",
        "simple graphic design with text and shapes for non-designers",
        "branded template or logo design for a business",
        "business presentation slide or infographic",
    ],
    "Adobe Firefly": [
        "commercially safe image for professional or business publishing",
        "stock photo quality image suitable for advertising",
        "professional design asset with clean polished composition",
        "image integrated into Adobe Photoshop or Illustrator workflow",
        "typography or artistic lettering design",
    ],
    "Leonardo.ai": [
        "game asset or character sprite for a video game",
        "consistent character design across multiple images",
        "concept art for game environment or prop",
        "anime or cartoon character with consistent appearance",
        "3D game-ready texture or asset design",
    ],
}


# ── Recommend function ────────────────────────────────────────────────────
def recommend(prompt: str):
    print("\n🔍 Analyzing your prompt...\n")

    # Build flat label list, track which tool each label belongs to
    all_labels = []
    label_to_tool = {}
    for tool_name, labels in TOOLS.items():
        for label in labels:
            all_labels.append(label)
            label_to_tool[label] = tool_name

    # Run zero-shot classification against all labels
    result = classifier(prompt, candidate_labels=all_labels, multi_label=True)

    # Average scores per tool
    tool_scores = {t: [] for t in TOOLS}
    for label, score in zip(result["labels"], result["scores"]):
        tool_scores[label_to_tool[label]].append(score)

    tool_avg = {t: sum(s) / len(s) for t, s in tool_scores.items()}

    # Normalize to 0–100
    lo, hi = min(tool_avg.values()), max(tool_avg.values())
    span = hi - lo if hi != lo else 1
    normalized = {t: int(((v - lo) / span) * 100) for t, v in tool_avg.items()}

    # Sort best to worst
    ranked = sorted(normalized.items(), key=lambda x: x[1], reverse=True)
    winner = ranked[0][0]

    # ── Print results ──
    print("=" * 55)
    print(f"  PROMPT : {prompt[:50]}{'...' if len(prompt)>50 else ''}")
    print("=" * 55)
    print(f"\n  🏆  BEST TOOL  →  {winner}\n")
    print("  📊  All tools ranked:\n")

    for tool_name, score in ranked:
        filled  = int(score / 5)          # 0–20 blocks
        empty   = 20 - filled
        bar     = "█" * filled + "░" * empty
        star    = "  ⭐ WINNER" if tool_name == winner else ""
        print(f"  {bar}  {score:3d}%  {tool_name}{star}")

    print("\n" + "=" * 55 + "\n")


# ── Main loop ─────────────────────────────────────────────────────────────
print("=" * 55)
print("   AI IMAGE TOOL RECOMMENDER")
print("   Model: facebook/bart-large-mnli")
print("=" * 55)
print("  Type your image prompt and press Enter.")
print("  Type 'quit' to exit.\n")

while True:
    try:
        prompt = input("  Your prompt: ").strip()
        if not prompt:
            print("  ⚠  Please enter a prompt.\n")
            continue
        if prompt.lower() in ("quit", "exit", "q"):
            print("\n  👋 Goodbye!\n")
            break
        recommend(prompt)
    except KeyboardInterrupt:
        print("\n\n  👋 Goodbye!\n")
        break