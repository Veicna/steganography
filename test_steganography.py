from PIL import Image
import os

def create_test_image(filename="test_input.png", size=(800, 600)):
    img = Image.new('RGB', size, color=(73, 109, 137))
    
    pixels = img.load()
    for i in range(size[0]):
        for j in range(size[1]):
            pixels[i, j] = ((i * 255) // size[0], (j * 255) // size[1], 128)
    
    img.save(filename)
    print(f"Test image created: {filename}")
    return filename

def run_test():
    from steganography import encode_image, decode_image
    
    print("=" * 60)
    print("LSB Steganography Test Program")
    print("=" * 60)
    print()
    
    test_image = create_test_image()
    
    test_message = "This is a test message. Steganography is working!"
    output_image = "test_encoded.png"
    
    print(f"\nOriginal message: {test_message}")
    print(f"Message length: {len(test_message)} characters")
    print()
    
    print("Encoding process starting...")
    encode_image(test_image, output_image, test_message)
    print()
    
    print("Decoding process starting...")
    decoded_message = decode_image(output_image)
    print(f"Extracted message: {decoded_message}")
    print()
    
    if test_message == decoded_message:
        print("✅ TEST SUCCESSFUL: Message embedded and extracted correctly!")
    else:
        print("❌ TEST FAILED: Messages do not match!")
        print(f"Expected: {test_message}")
        print(f"Received: {decoded_message}")
    
    print()
    print("Test files:")
    print(f"  - {test_image}")
    print(f"  - {output_image}")
    
    file_size_original = os.path.getsize(test_image)
    file_size_encoded = os.path.getsize(output_image)
    print(f"\nFile sizes:")
    print(f"  Original: {file_size_original} bytes")
    print(f"  Encoded: {file_size_encoded} bytes")
    print(f"  Difference: {abs(file_size_encoded - file_size_original)} bytes")

if __name__ == "__main__":
    run_test()
