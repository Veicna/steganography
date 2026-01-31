from PIL import Image
import sys

def encode_image(input_path, output_path, secret_message):
    try:
        img = Image.open(input_path)
        img = img.convert('RGB')
        width, height = img.size
        pixels = img.load()
        
        terminator = "#####"
        full_message = secret_message + terminator
        
        binary_message = ''.join(format(byte, '08b') for byte in full_message.encode('utf-8'))
        
        data_index = 0
        data_len = len(binary_message)
        
        for y in range(height):
            for x in range(width):
                if data_index >= data_len:
                    break
                
                r, g, b = pixels[x, y]
                
                if data_index < data_len:
                    r = r & ~1 | int(binary_message[data_index])
                    data_index += 1
                
                if data_index < data_len:
                    g = g & ~1 | int(binary_message[data_index])
                    data_index += 1
                
                if data_index < data_len:
                    b = b & ~1 | int(binary_message[data_index])
                    data_index += 1
                
                pixels[x, y] = (r, g, b)
            
            if data_index >= data_len:
                break
        
        if data_index < data_len:
            raise ValueError("Image is not large enough to hold the message!")
        
        img.save(output_path, 'PNG')
        print(f"Message successfully embedded: {output_path}")
        print(f"Number of characters embedded: {len(secret_message)}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error during encoding: {str(e)}")
        sys.exit(1)

def decode_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        width, height = img.size
        pixels = img.load()
        
        binary_data = ""
        terminator = "#####"
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                binary_data += str(r & 1)
                binary_data += str(g & 1)
                binary_data += str(b & 1)
        
        message_bytes = []
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            if len(byte) == 8:
                message_bytes.append(int(byte, 2))
                
                try:
                    message = bytes(message_bytes).decode('utf-8')
                    if message.endswith(terminator):
                        return message[:-len(terminator)]
                except UnicodeDecodeError:
                    continue
        
        return "Message terminator not found!"
        
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error during decoding: {str(e)}")
        sys.exit(1)

def main():
    print("=" * 50)
    print("LSB Steganography Tool")
    print("=" * 50)
    print()
    
    print("Select operation:")
    print("1. Hide Message (Encode)")
    print("2. Extract Message (Decode)")
    print()
    
    choice = input("Your choice (1/2): ").strip()
    
    if choice == '1':
        input_image = input("Carrier image path: ").strip()
        output_image = input("Output image path: ").strip()
        secret = input("Message to hide: ").strip()
        
        encode_image(input_image, output_image, secret)
        
    elif choice == '2':
        encoded_image = input("Encoded image path: ").strip()
        
        print("\nExtracted Message:")
        print("-" * 50)
        decoded_msg = decode_image(encoded_image)
        print(decoded_msg)
        print("-" * 50)
        
    else:
        print("Invalid choice!")
        sys.exit(1)

if __name__ == "__main__":
    main()
