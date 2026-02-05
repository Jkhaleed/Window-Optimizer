# Windows Optimizer

A Python desktop application that centralizes Windows system optimization and customization tools into a single, modern interface. Manage performance settings, monitor system resources, and configure Windows features without navigating through multiple control panels.

## Features

### 🖥️ Computer Information
- Display detailed system specifications
- View CPU, RAM, storage, and OS information
- Real-time system resource monitoring

### 🎨 Visual Effects
- Adjust Windows visual effects settings
- Choose between performance and appearance
- Options: Let Windows decide, Best appearance, Best performance, or Custom
- Direct access to Windows Performance Options

### 💾 Virtual Memory
- Monitor paging file status and usage
- View total, used, and free virtual memory
- Quick access to virtual memory settings
- Real-time swap usage statistics

### 🚀 Startup Apps
- Manage applications that run at system startup
- Direct access to Task Manager's Startup tab
- Optimize boot time by controlling startup programs

### 🖱️ Mouse Settings
- Configure mouse acceleration modes
- Options: Disable Enhanced Pointer Precision, Legacy Acceleration, or Enable Enhanced Pointer Precision
- Fine-tune mouse responsiveness for gaming or productivity

### 🔆 Screen Brightness
- Adjust screen brightness with an intuitive slider
- Quick preset buttons (25%, 50%, 75%, 100%)
- Real-time brightness control
- Support for multiple monitors

## Installation

### Prerequisites
- Python 3.8 or higher
- Windows OS (7, 10, or 11)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/window-optimizer.git
   cd window-optimizer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

```txt
customtkinter>=5.0.0
psutil>=5.9.0
screen-brightness-control>=0.20.0
```

## Usage

### Running the Application

```bash
python GUI.py
```

### Using Individual Modules (CLI)

Each module can also be run independently from the command line:

```bash
# Computer Information
python scripts/compinfo.py

# Visual Effects
python scripts/visualfx.py

# Virtual Memory
python scripts/virtualmemory.py

# Mouse Settings
python scripts/mouse.py

# Brightness Control
python scripts/brightness.py

# Startup Apps
python scripts/startup.py
```

## Project Structure

```
window-optimizer/
│
├── GUI.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
└── scripts/
    ├── compinfo.py            # System information module
    ├── visualfx.py            # Visual effects configuration
    ├── virtualmemory.py       # Virtual memory management
    ├── mouse.py               # Mouse acceleration settings
    ├── brightness.py          # Screen brightness control
    └── startup.py             # Startup applications manager
```

## Configuration

### Visual Effects Values
- `0` - Let Windows choose what's best for my computer
- `1` - Adjust for best appearance
- `2` - Adjust for best performance
- `3` - Custom (opens Windows Performance Options)

### Mouse Acceleration Values
- `0` - Disabled Enhanced Pointer Precision
- `1` - Legacy Acceleration
- `2` - Enable Enhanced Pointer Precision

## Troubleshooting

### Common Issues

**"Module not found" error**
```bash
pip install --upgrade -r requirements.txt
```

**Brightness control not working**
- Ensure you have compatible display drivers
- Some monitors may not support software brightness control
- Try running the application as Administrator

**Registry access errors**
- Run the application as Administrator
- Check Windows User Account Control (UAC) settings

**Visual Effects not applying**
- Restart Windows Explorer after changing settings
- Some settings may require a system restart

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **CustomTkinter** - Modern GUI framework for Python
- **psutil** - Cross-platform system and process utilities
- **screen-brightness-control** - Monitor brightness management library

## Disclaimer

This application modifies Windows system settings and registry values. While designed to be safe, use at your own risk. It's recommended to:
- Create a system restore point before making significant changes
- Understand what each setting does before applying it
- Back up important data regularly

## Author

Your Name - [GitHub Profile](https://github.com/Jkhaleed)

## Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/yourusername/window-optimizer/issues)
- Contact: khaleedjimoh05@gmail.com

---

**Note:** This application requires Windows and administrative privileges for certain features like registry modifications and system property access.
