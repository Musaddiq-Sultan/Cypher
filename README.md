# Cypher

**Cypher** is a modern, dark-themed desktop file encryption utility built with Python. Powered by `pyAesCrypt` and styled with `ttkbootstrap`'s *Superhero* theme, Cypher provides robust AES-256 file encryption and decryption with configurable memory buffer sizes and live operation logging.

---

## Features

* **Standalone Executable:** Ready-to-run Windows `.exe`—no Python installation required.
* **AES Encryption:** Secure file encryption using `pyAesCrypt`.


* **Auto Detection:** Automatically detects whether a selected file is encrypted (`.aes`) or unencrypted and toggles decryption/encryption modes accordingly.


* **Modern UI:** Clean desktop interface built with `ttkbootstrap` using the *Superhero* theme.


* **Configurable Buffer Sizes:** Choose custom memory buffer allocations (4 KB, 16 KB, 64 KB, 256 KB, 1 MB) to optimize performance for files of any size.


* **Multithreaded Operations:** File processing runs in background threads to keep the user interface responsive during heavy tasks.


* **Live Output Logs:** Embedded console panel providing real-time status updates and file operation reports.



---

## Downloads

For Windows users who prefer not to run Python scripts directly, grab the compiled standalone executable:

1. Go to the [Releases](https://www.google.com/search?q=https://github.com/your-username/cypher/releases) tab.
2. Download `Cypher.exe`.
3. Double-click `Cypher.exe` to run the application instantly.

---

## Requirements (Running from Source)

If you prefer building or running the Python source code directly:

* **Python:** 3.x
* **Libraries:**
* `ttkbootstrap`
* `pyAesCrypt`
* `tkinter` (included with standard Python installations)



### Source Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/cypher.git
cd cypher

```


2. **Install required dependencies:**
```bash
pip install ttkbootstrap pyAesCrypt

```


3. **Run the application:**
```bash
python gui.py

```



---

## Usage

1. **Launch the application** via `Cypher.exe` or `python gui.py`.
2. **Encrypting a File:**
* Click **Select File** and pick any unencrypted file.


* Select your desired **Buffer Size** (default is 64 KB).


* Enter a password in the **Password** field.


* Click **Submit**. Cypher will generate a `.aes` encrypted version and safely remove the original unencrypted file.




3. **Decrypting a File:**
* Click **Select File** and choose a `.aes` file.


* Enter the original password.


* Click **Submit**. Cypher will restore the original file and remove the `.aes` container.





---

## Building the Executable

If you modify the source code and want to recompile the `.exe` yourself using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --icon=icon.png --add-data "icon.png;." gui.py

```

The output executable will be created inside the `dist/` directory.

---

## Security & Workflow Notes

> **Warning:** Encrypting or decrypting a file with Cypher automatically deletes the source file upon successful completion. Ensure you remember your password, as files encrypted without the correct key cannot be recovered.
> 
> 

---

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
