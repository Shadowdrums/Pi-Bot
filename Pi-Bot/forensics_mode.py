import os

def recover_deleted_files(directory):
    # This is a very basic way to find potentially deleted files
    # Real recovery would require direct disk access and more complex methods
    potentially_deleted_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".bak") or file.endswith(".tmp"):
                potentially_deleted_files.append(os.path.join(root, file))
    return potentially_deleted_files

def analyze_file_metadata(file_path):
    # For real metadata extraction, you'd use a library like exifread for images
    # Here's a simple example using os.stat
    try:
        file_info = os.stat(file_path)
        metadata = {
            "size": file_info.st_size,
            "last_modified": file_info.st_mtime,
            "last_accessed": file_info.st_atime,
            "created": file_info.st_ctime,
        }
        return metadata
    except FileNotFoundError:
        return None

def scan_file_signatures(directory):
    # This is a basic way to look for specific file headers (like JPG, PNG, etc.)
    # A real-world approach would scan file bytes for known headers
    file_signatures = {
        "jpg": b'\xFF\xD8\xFF',
        "png": b'\x89\x50\x4E\x47',
        # Add more signatures as needed
    }
    
    detected_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                header = f.read(4)  # Read the first 4 bytes
                for file_type, signature in file_signatures.items():
                    if header.startswith(signature):
                        detected_files.append((file_type, file_path))
    
    return detected_files

def forensics_mode():
    while True:
        print("\n--- Forensics Mode ---")
        print("1. Recover potentially deleted files")
        print("2. Analyze file metadata")
        print("3. Scan for file signatures")
        print("4. Exit forensics mode")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            directory = input("\nEnter the directory to scan: ")
            results = recover_deleted_files(directory)
            if results:
                print("\nPotentially deleted files:")
                for file in results:
                    print(file)
            else:
                print("\nNo potentially deleted files found.")
        
        elif choice == "2":
            file_path = input("\nEnter the file path to analyze: ")
            metadata = analyze_file_metadata(file_path)
            if metadata:
                print("\nFile metadata:")
                for key, value in metadata.items():
                    print(f"{key}: {value}")
            else:
                print("\nFile not found.")
        
        elif choice == "3":
            directory = input("\nEnter the directory to scan: ")
            results = scan_file_signatures(directory)
            if results:
                print("\nDetected files by signature:")
                for file_type, file_path in results:
                    print(f"{file_type.upper()}: {file_path}")
            else:
                print("\nNo files detected by their signatures.")
        
        elif choice == "4":
            break

if __name__ == "__main__":
    forensics_mode()
