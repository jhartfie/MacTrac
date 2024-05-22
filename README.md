# MacTrac

Track Clicks and KeyStrokes from Mac TaskBar

# MacTrac

MacTrac is a macOS menu bar application that counts keystrokes and mouse clicks. This application runs in the background and updates the counts in real-time.

## Prerequisites

- Python 3.12 or later
- `pyinstaller` package
- `rumps` package
- `pynput` package

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

git clone https://github.com/jhartfie/mactrac.git
cd mactrac

### 2. Create and Activate a Virtual Environment

Create a virtual environment and activate it:

python3 -m venv myenv
source myenv/bin/activate

### 3. Install Required Packages

Install the required Python packages:

pip install rumps pynput pyinstaller

### 4. Build the Application with PyInstaller

Use PyInstaller to build the application:

pyinstaller --onefile --windowed mactrac.spec

### 5. Move the Application to the Applications Folder

Move the built application to the /Applications folder:

mv dist/MacTrac.app /Applications/

### 6. Create a Launch Agent

Create a Launch Agent to run the application in the background and ensure it starts at login:

Create a .plist file for the Launch Agent:

nano ~/Library/LaunchAgents/com.mactrac.app.plist

Add the following content to the .plist file:

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.mactrac.app</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Applications/MacTrac.app/Contents/MacOS/MacTrac</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>

Save and close the file by pressing Ctrl + O, Enter, and then Ctrl + X.

### 7. Load the Launch Agent

Load the Launch Agent to start the application immediately and ensure it runs at startup:

launchctl load ~/Library/LaunchAgents/com.mactrac.app.plist

### 8. Verify the Application

You can verify that the Launch Agent is loaded and running:

launchctl list | grep com.mactrac.app

If the application is running correctly, you should see an entry like com.mactrac.app in the output.

## Troubleshooting

Application Freezes: If the live counter freezes, you may need to restart the application by unloading and reloading the Launch Agent:

launchctl unload ~/Library/LaunchAgents/com.mactrac.app.plist
launchctl load ~/Library/LaunchAgents/com.mactrac.app.plist

Edit Info.plist: If you need to modify the Info.plist file to hide the Dock icon, you can edit it directly in the application bundle:

sudo nano /Applications/MacTrac.app/Contents/Info.plist
Ensure it includes the following key:

<key>LSUIElement</key>
<string>1</string>

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
