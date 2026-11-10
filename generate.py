import asyncio
import sys
import edge_tts

async def main():
    text = "# Intro\nBenvenuti nel podcast..."
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        pass
    
    sections = text.split("#")
    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue
        lines = section.split("\n")
        title = lines[0].strip()
        content = "\n".join(lines[1:]).strip() or title
        
        output_file = f"output_{i}.mp3"
        print(f"Generazione voce per: {title}")
        communicate = edge_tts.Communicate(content, "it-IT-FilippoNeural")
        await communicate.save(output_file)

if __name__ == "__main__":
    asyncio.run(main())
