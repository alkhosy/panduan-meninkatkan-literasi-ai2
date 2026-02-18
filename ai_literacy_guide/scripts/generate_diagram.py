import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_rag_diagram():
    fig, ax = plt.subplots(figsize=(12, 6))

    # Hide axes
    ax.axis('off')

    # Define box style
    box_style = dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=2)

    # Nodes
    ax.text(0.1, 0.8, "User Question", ha="center", va="center", size=12, bbox=box_style)
    ax.text(0.1, 0.2, "Vector Database\n(Knowledge Base)", ha="center", va="center", size=12, bbox=box_style)
    ax.text(0.5, 0.8, "LLM (GPT-4)", ha="center", va="center", size=12, bbox=box_style)
    ax.text(0.5, 0.2, "Final Answer", ha="center", va="center", size=12, bbox=box_style)

    # Arrows
    # 1. User -> DB
    ax.annotate("", xy=(0.1, 0.3), xytext=(0.1, 0.7), arrowprops=dict(arrowstyle="->", lw=2))
    ax.text(0.12, 0.5, "1. Search", va="center")

    # 2. DB -> LLM
    ax.annotate("", xy=(0.4, 0.75), xytext=(0.2, 0.2), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", lw=2))
    ax.text(0.3, 0.5, "2. Retrieve Context", va="center")

    # 3. User -> LLM
    ax.annotate("", xy=(0.4, 0.8), xytext=(0.2, 0.8), arrowprops=dict(arrowstyle="->", lw=2))

    # 4. LLM -> Answer
    ax.annotate("", xy=(0.5, 0.3), xytext=(0.5, 0.7), arrowprops=dict(arrowstyle="->", lw=2))
    ax.text(0.52, 0.5, "3. Generate", va="center")

    plt.title("RAG (Retrieval Augmented Generation) Workflow", fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('ai_literacy_guide/images/rag_diagram.png', dpi=300)
    print("Diagram generated: ai_literacy_guide/images/rag_diagram.png")

if __name__ == "__main__":
    create_rag_diagram()
