import asyncio
import os
import edge_tts

async def main():
    text = "# Intro\nBenvenuti nel podcast con edge-tts."
    if os.path.exists("input.txt"):
        with open("input.txt", "r", encoding="utf-8") as f:
            text = f.read()
    
    sections = text.split("#")
    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue
        lines = section.split("\n")
        title = lines[0].strip()
        content = "\n".join(lines[1:]).strip() or title
        
        output_file = f"output_{i}.mp3"
        print(f"Generazione in corso per: {title}")
        communicate = edge_tts.Communicate(content, "it-IT-FilippoNeural")
        await communicate.save(output_file)

if __name__ == "__main__":
    asyncio.run(main())

