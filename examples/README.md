# Example Usage

This folder contains example usage scenarios for the LSB Steganography project.

## Quick Start

### 1. Simple Text Hiding (Encoding)

```bash
python steganography.py

```

Select **Option 1** and provide:

* **Carrier image:** Any PNG file
* **Output image:** `encoded_output.png`
* **Secret message:** `This is a secret message!`

### 2. Message Extraction (Decoding)

```bash
python steganography.py

```

Select **Option 2** and provide:

* **Encoded image:** `encoded_output.png`

---

## Example Scenarios

### Scenario 1: Personal Notes

Hide your daily notes within your photos:

```
Message: "2026-01-31: Had a great day today!"

```

### Scenario 2: Secure Communication

Exchange secure messages with friends:

```
Message: "Let's meet tomorrow at 15:00."

```

### Scenario 3: Digital Watermarking

Embed metadata into your images for copyright protection:

```
Message: "© 2026 - All rights reserved"

```

---

## Important Notes

* **Capacity:** The maximum message size depends on the image dimensions.
* **Bit Depth:** Each pixel (RGB) can store **3 bits** (1 bit per channel).
* **Calculation:** For an 800x600 pixel image:
 bits  characters.
* **Format:** Always use **PNG** or other lossless formats. Avoid JPEG, as its lossy compression will corrupt the hidden bits.

---

## Testing

You can use the automated test script included in the repository:

```bash
python test_steganography.py

```

This script automatically performs the following:

1. Generates a synthetic test image.
2. Embeds a sample message.
3. Extracts the message.
4. Verifies data integrity and accuracy.

