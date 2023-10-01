# Pi-Bot
This is a chattbot/assistant still in development for raspberry pi 4

# 🤖 Pi-Bot for Raspberry Pi 4

A versatile bot tailored for Raspberry Pi 4. This bot was designed and developed using Kali Linux on a Raspberry Pi 4. It comes with a suite of programs catering to network analysis, sentiment-based learning, and basic digital forensics.

## 🔧 Setup and Installation

### Prerequisites

#### Libraries Used:

- **`textblob`**: For sentiment analysis in `pi_learning.py`.
- **`psutil`**: This library provides an interface to fetch system details like network statistics, which is vital for `network_assist.py`.
- **`scapy`**: An invaluable tool for network analysis, `scapy` powers many features in `network_assist.py`, especially packet sniffing.
- **`speedtest-cli`**: Used in `network_assist.py` to measure the internet speed of the connected network.
- **`netifaces`**: Facilitates network interface interrogation, primarily used in `network_assist.py`.
- **`os`**: A built-in Python library used in `forensics_mode.py` for interacting with the operating system, especially for tasks related to file management.

#### Installation:

1. Ensure you're running this on a Raspberry Pi 4 with Kali Linux installed.
2. Move into the project directory:

cd path_to_your_directory

3. Install the required dependencies using pip:

pip install textblob psutil scapy speedtest-cli netifaces

4. Provide execute permissions:

chmod +x pi_learning.py network_assist.py forensics_mode.py


## 📚 Modules

### 1. **`pi_learning.py`**: 
This module uses sentiment analysis from the `textblob` library to analyze the sentiment of a given text. It can recognize and respond to greetings, farewells, weather queries, news-related queries, technical issues, and more. Moreover, it learns from user corrections and stores them for future interactions.

### 2. **`network_assist.py`**: 
A utility tool that assists in network-related tasks such as mapping the network topology, packet sniffing, scanning available Wi-Fi networks, checking SSH status, and more. Leveraging the power of `scapy`, `psutil`, and other libraries, this module is vital for those who want to analyze their network.

### 3. **`forensics_mode.py`**: 
This module provides basic digital forensics capabilities. It can recover potentially deleted files, analyze file metadata, and scan for specific file signatures in a given directory.

## 🌟 Conclusion

The Pi-Bot, masterfully crafted by **Shadowdrums**, is an embodiment of the versatility and power that the Raspberry Pi 4 platform offers. Designed and developed on a Raspberry Pi 4 using Kali Linux, this bot encompasses a wide spectrum of functionalities:

- **Sentiment Analysis:** Understand and respond to user inputs based on their sentiment using the power of TextBlob.
  
- **Network Assistance:** Diagnose, monitor, and analyze network activities, from mapping network topologies to performing speed tests.
  
- **Digital Forensics:** Potentially recover deleted files, analyze file metadata, and scan for specific file signatures.

Each module serves a distinct purpose, whether you're diving into the intricacies of user interactions, keen on analyzing your digital environment, or ensuring the robustness of your network.

Furthermore, Pi-Bot is still under active development. This means more features, improvements, and optimizations are on the horizon, offering even more capabilities and utilities in the future.

Whether you're a hobbyist seeking to tap into the potential of your Raspberry Pi, a professional aiming to secure and analyze your network, or someone who is enthusiastic about digital forensics, Pi-Bot is your go-to solution. It exemplifies a blend of utility, innovative design, and the ethos of open-source, mirroring the dedication and vision of its creator, Shadowdrums.

Dive in, explore, and perhaps even contribute as Pi-Bot continues to evolve and redefine the possibilities of the Raspberry Pi 4 platform.

---

**Stay Curious and Happy Exploring!** 🚀

