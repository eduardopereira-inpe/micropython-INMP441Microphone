import time

from inmp441 import INMP441, write_wav_header


SAMPLE_RATE = 16000 // 2
RECORD_SECONDS = 5

OUTPUT_FILE = "test.wav"

mic = INMP441(

    sample_rate=SAMPLE_RATE,

    sck_pin=32,
    ws_pin=25,
    sd_pin=33
)

print("Recording...")

total_pcm_bytes = 0

try:
    with open(OUTPUT_FILE, "wb") as f:
        f.seek(44)

        start = time.time()

        while (
            time.time() - start <
            RECORD_SECONDS
        ):
            chunk = mic.read_pcm16(record_mode=False)

            if chunk:
                total_pcm_bytes += f.write(chunk)

        f.seek(0)

        write_wav_header(
            file=f,
            sample_rate=SAMPLE_RATE,
            pcm_size=total_pcm_bytes
        )
finally:
    mic.close()

print("Done.")

print("PCM bytes:", total_pcm_bytes)

print("Saved:", OUTPUT_FILE)
