# Example Usage

This folder contains example usage scenarios for the LSB Steganography project.

## Quick Start

### 1. Hiding Simple Text

```bash
python steganography.py

```

Select Option 1 and enter:

* Carrier image: Any PNG file
* Output image: `encoded_output.png`
* Hidden message: `This is a secret message!`

### 2. Extracting a Message

```bash
python steganography.py

```

Select Option 2 and enter:

* Encoded image: `encoded_output.png`

## Example Scenarios

### Scenario 1: Personal Notes

Hide daily notes inside your photos:

```
Message: "2026-01-31: I had a great day today!"

```

### Scenario 2: Secure Communication

Secure messaging with friends:

```
Message: "Let's meet tomorrow at 3:00 PM."

```

### Scenario 3: Digital Watermarking

Add information to your images for copyright purposes:

```
Message: "© 2026 - All rights reserved"

```

## Important Notes

* Message capacity depends on the image size.
* Each pixel stores 3 bits (RGB).
* Example: 800x600 pixels = 1,440,000 bits ≈ 180,000 characters capacity.
* Use PNG format (JPEG uses lossy compression which destroys the hidden data).

## Testing

Use the test script included with the project:

```bash
python test_steganography.py

```

This script automatically:

1. Creates a test image
2. Embeds a message
3. Extracts the message
4. Verifies correctness
