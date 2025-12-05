# FileEclipse

FileEclipse is a command line utility that detects the true file type of a file by reading its magic number. File extensions can be misleading or intentionally changed, so this tool identifies files based on their actual binary signature.

This tool is useful for security analysis, malware investigation, digital forensics and general file verification.

---

## **Features**

* **Three-Layer Detection System**

  1. **Magic Number Detection** – Reads the first bytes of the file and matches them against a built-in signature database.
  2. **Heuristic Extension Validation** – Cross-checks file extensions against known patterns for extra verification.
  3. **Programming Language Detection** – Uses a pattern-scoring system to identify text-based code files such as Python, JavaScript, C, etc.

* **Accurate Binary Identification**
  Detects documents, images, archives, executables, audio/video, certificates, and script formats based on real binary signatures.

* **Hexadecimal Magic Number Display**
  Shows the extracted magic number in uppercase hexadecimal for clarity and debugging.

* **Cross-Platform Support**
  Works on Windows, Linux, and macOS—anywhere Python runs.

* **Extensible Signature Database**
  Add new file types easily by expanding the `magic_dict` and language patterns.

* **Useful for Security & Forensics**
  Ideal for malware analysis, digital forensics, penetration testing, and secure file inspection.


---

## Installation

Clone the repository and install the required environment.

```
git clone https://github.com/EpicNerdGuy/FileEclipse.git
cd FileEclipse
```

---

## Usage

Run the tool by providing a file with the `-f` or `--file` option.

```
python FileEclipse.py -f <path_to_file>
```

Example:

```
python FileEclipse.py -f test.py
```

Output example:

```
Magic Number of the file '.\test.py': 696D706F727420756E6974746573740D
File type detected: Python script, ASCII text executable, with CRLF line terminators
FILE DETECTION COMPLETED.
```

Another example with a text file:

```
python FileEclipse.py -f ".\file.txt"
```

Output:

```
Magic Number of the file '.\file.txt': 2166756E6374696F6E28297B66756E63
File type detected: ASCII text, with very long lines, with no line terminators
FILE DETECTION COMPLETED.
```

## How It Works

<img width="1127" height="753" alt="image" src="https://github.com/user-attachments/assets/e026ee15-0a45-4374-b2ab-72b1cb0aa9e6" />


---

## Vid Sample



https://github.com/user-attachments/assets/27e7f8a2-6620-4190-9722-8b4587b9fc70



## **Supported File Types**

| Category                  | File Types                                                              |
| ------------------------- | ----------------------------------------------------------------------- |
| **Documents**             | PDF, DOC, DOCX, RTF, XML, HTML, JSON, YAML                              |
| **Images**                | PNG, JPEG, GIF, BMP, TIFF, WebP                                         |
| **Archives / Compressed** | ZIP, RAR, 7z, TAR, GZIP, BZIP2                                          |
| **Executables**           | ELF (Linux), EXE/PE (Windows), Java `.class`, Mach-O (macOS*)           |
| **Audio / Video**         | MP3, FLAC, WAV, OGG, MP4, MKV                                           |
| **Scripts / Code**        | Bash, Python, JavaScript, TypeScript, Java, C, C++, Ruby, PHP, Go, Rust |
| **Certificates**          | X.509 (DER, PEM), PKCS#7, PKCS#12                                       |

*Add Mach-O only if you include its magic number signature.


---


---
