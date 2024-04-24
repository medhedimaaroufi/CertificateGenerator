# Certificate Generator

Certificate Generator is a Python application that enables users to create certificates by providing names, a certificate template, fonts, and an output directory. It offers a user-friendly interface built with Tkinter, allowing for easy navigation and operation.

## Features

- **Input Selection**: Choose the file containing the list of names for certificates.
- **Template Selection**: Pick a certificate template image to use.
- **Font Customization**: Specify a font file for the text on the certificates.
- **Output Configuration**: Select an output directory where the generated certificates will be saved.
- **Progress Bar**: Visualize the generation progress through a progress bar.
- **Cross-Platform Compatibility**: Supports Windows, macOS, and Linux operating systems.

## Requirements

- Python 3.x
- Tkinter (usually included in standard Python installations)
- Pillow (Python Imaging Library)
- ttkthemes

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/CertificateGenerator.git

2. **Navigate to the Project Directory:**

   ```bash
   cd CertificateGenerator

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Run the Application:**

   ```bash
   python app.py

5. **Generate Certificates:**

- Use the GUI to select the names file, certificate template, font file, and output directory.
- Click the "Generate Certificates" button to create the certificates.

6. **Create Executable**

   ```bash
   pyinstaller --onefile --windowed app.py

## Screen Shots

![App](https://github.com/medhedimaaroufi/CertificateGenerator/blob/main/screen.png)

## Copyright

© 2024 medhedimaaroufi. All rights reserved.

