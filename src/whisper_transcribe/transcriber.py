import whisper
from pathlib import Path
import docx
import argparse


def transcribe_wav(source_dir, dest_dir):
    # 1. Convert string paths to Path objects
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    # Ensure the destination directory exists
    dest_path.mkdir(parents=True, exist_ok=True)

    # 2. Load the model
    print("Loading Whisper model (this might take a moment)...")
    model = whisper.load_model("medium")

    # 3. Find and process each .wav file in the source directory
    wav_files = list(source_path.glob("*.wav"))

    if not wav_files:
        print(f"No .wav files found in {source_path}")
        return  # Exit the function if no files are found

    for audio_path in wav_files:
        print(f"Transcribing: {audio_path.name}...")

        # Transcribe the file
        # Whisper expects a string path, so we convert the Path object using str()
        result = model.transcribe(str(audio_path))

        # 4. Create a new Word document and add the text
        doc = docx.Document()
        doc.add_paragraph(result["text"])

        # 5. Save the document in the destination folder
        output_file = dest_path / f"{audio_path.stem}.docx"
        doc.save(output_file)

        print(f"Saved transcription to: {output_file.name}")

    print("Batch processing complete!")


# 6. Execution block for command-line usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe WAV files to DOCX.")
    parser.add_argument("source", help="The folder path containing your .wav files")
    parser.add_argument("dest", help="The folder path where you want the .docx files saved")

    args = parser.parse_args()

    transcribe_wav(args.source, args.dest)

#Terminal Execution
#python Whisper_Transcriptions.py "C:\Users\benma\Documents\audio_test_input" "C:\Users\benma\Documents\audio_test_output"