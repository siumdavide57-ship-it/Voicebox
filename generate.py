import asyncio
import os
import edge_tts

async def main():
    text = "Benvenuti nel podcast generato automaticamente con GitHub Actions."
    if os.path.exists("input.txt"):
        with open("input.txt", "r", encoding="utf-8") as f:
            text = f.read()
    
    output_file = "output_0.mp3"
    print(f"Generazione in corso...")
    # Usiamo una voce standard pienamente compatibile
    communicate = edge_tts.Communicate(text, "it-IT-IsabellaNeural")
    await communicate.save(output_file)
    print("Audio generato con successo!")

if __name__ == "__main__":
    asyncio.run(main())
