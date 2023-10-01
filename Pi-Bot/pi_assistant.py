import os
import subprocess
import psutil
import shutil

# Function to display possible commands
def show_possible_commands():
    print("You can ask me things like:")
    print("- What is the current directory?")
    print("- List files.")
    print("- Show me CPU info.")
    print("- What's the memory usage?")
    print("- Disk usage.")
    print("- Ping Google.")
    print("- Search for a file or folder.")
    print("- What's my IP address?")
    print("- Reboot the system.")
    print("- Shut down the system.")
    print("- List network interfaces.")
    print("- List running processes.")
    print("- Show available storage.")
    print("- Make an SSH connection.")
    print("- Show live SSH users.")
    print("- Copy a file.")
    print("- Move a file.")
    print("- Delete a file.")
    print("- GPU info.")
    print("- CPU temperature.")

# Simple NLP to identify user command
def simple_nlp(command):
    command = command.lower().strip()
    if 'current directory' in command:
        return '1'
    elif 'list files' in command:
        return '2'
    elif 'cpu info' in command:
        return '3'
    elif 'memory usage' in command:
        return '4'
    elif 'disk usage' in command:
        return '5'
    elif 'ping google' in command:
        return '6'
    elif 'search for a file or folder' in command:
        return '7'
    elif "what's my ip address" in command:
        return '8'
    elif 'reboot the system' in command:
        return '9'
    elif 'shut down the system' in command:
        return '10'
    elif 'list network interfaces' in command:
        return '11'
    elif 'list running processes' in command:
        return '12'
    elif 'show available storage' in command:
        return '13'
    elif 'make an ssh connection' in command:
        return '14'
    elif 'show live ssh users' in command:
        return '15'
    elif 'copy a file' in command:
        return '16'
    elif 'move a file' in command:
        return '17'
    elif 'delete a file' in command:
        return '18'
    elif 'gpu info' in command:
        return '19'
    elif 'cpu temperature' in command:
        return '20'
    else:
        return 'unknown'

# Function to handle Pi specific requests
def handle_pi_request(command):
    choice = simple_nlp(command)
    response = ''

    if choice == '1':
        response = "Current directory is: " + os.getcwd()
    elif choice == '2':
        response = "Files in the current directory: " + str(os.listdir('.'))
    elif choice == '3':
        response = subprocess.getoutput("lscpu")
    elif choice == '4':
        response = subprocess.getoutput("free -h")
    elif choice == '5':
        response = subprocess.getoutput("df -h")
    elif choice == '6':
        response = subprocess.getoutput("ping -c 4 google.com")
    elif choice == '7':
        target = input("Enter the name of the file or folder you're searching for: ")
        response = search_files(target)
    elif choice == '8':
        ip_address = subprocess.getoutput("hostname -I").strip()
        response = f"IP Address: {ip_address}"
    elif choice == '9':
        os.system("sudo reboot")
        response = "Rebooting..."
    elif choice == '10':
        os.system("sudo shutdown now")
        response = "Shutting down..."
    elif choice == '11':
        response = list_network_interfaces()
    elif choice == '12':
        response = list_running_processes()
    elif choice == '13':
        response = show_available_storage()
    elif choice == '14':
        host = input("Enter the SSH host: ")
        username = input("Enter the SSH username: ")
        response = make_ssh_connection(host, username)
    elif choice == '15':
        response = show_live_ssh_users()
    elif choice == '16':
        source = input("Enter the source file path: ")
        destination = input("Enter the destination path: ")
        response = copy_file(source, destination)
    elif choice == '17':
        source = input("Enter the source file path: ")
        destination = input("Enter the destination path: ")
        response = move_file(source, destination)
    elif choice == '18':
        target = input("Enter the file path to delete: ")
        response = delete_file(target)
    elif choice == '19':
        response = get_gpu_info()
    elif choice == '20':
        response = get_cpu_temperature()
    else:
        response = "I'm sorry, I didn't understand that command."
        
    return response

# Function to search for files or folders
def search_files(target):
    for root, dirs, files in os.walk('.'):
        if target in files:
            return f"File found: {os.path.join(root, target)}"
        if target in dirs:
            return f"Folder found: {os.path.join(root, target)}"
    return "File or folder not found."

# Function to list network interfaces
def list_network_interfaces():
    interfaces = psutil.net_if_addrs()
    output = ""
    for interface, addrs in interfaces.items():
        output += f"{interface}\n"
        for addr in addrs:
            output += f"  {addr.family.name}: {addr.address}\n"
    return output

# Function to list running processes
def list_running_processes():
    output = ""
    for process in psutil.process_iter(attrs=['pid', 'name']):
        output += f"PID: {process.info['pid']}, Name: {process.info['name']}\n"
    return output

# Function to show available storage
def show_available_storage():
    output = ""
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        output += f"{partition.device} mounted on {partition.mountpoint}\n"
        output += f"  Total: {usage.total}, Used: {usage.used}, Free: {usage.free}\n"
    return output

# Function to make SSH connection
def make_ssh_connection(host, username):
    try:
        os.system(f"ssh {username}@{host}")  # Secure if SSH keys are used
        return "SSH session closed."
    except Exception as e:
        return f"Failed to make SSH connection: {e}"

# Function to show live SSH users
def show_live_ssh_users():
    try:
        output = subprocess.getoutput("w -hs")
        return output
    except Exception as e:
        return f"Failed to fetch SSH users: {e}"

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        return "File copied successfully."
    except Exception as e:
        return f"Failed to copy file: {e}"

# Function to move a file
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        return "File moved successfully."
    except Exception as e:
        return f"Failed to move file: {e}"

# Function to delete a file
def delete_file(target):
    try:
        os.remove(target)
        return "File deleted successfully."
    except Exception as e:
        return f"Failed to delete file: {e}"

# Function to get GPU information (this may not work as expected on all systems)
def get_gpu_info():
    try:
        output = subprocess.getoutput("vcgencmd get_mem gpu")
        return output
    except Exception as e:
        return f"Failed to fetch GPU info: {e}"

# Function to get CPU temperature
def get_cpu_temperature():
    try:
        output = subprocess.getoutput("/opt/vc/bin/vcgencmd measure_temp")
        return output
    except Exception as e:
        return f"Failed to fetch CPU temperature: {e}"

#while True:
#    command = input("Pi-assistant: How may I assist you with your Pi? Type 'exit' to return to the main chat. ")
#    if command.lower() == 'exit':
#        break
#    response = handle_pi_request(command)
#    if response:
#        print(f"Pi-assistant: {response}")
#    show_possible_commands()
