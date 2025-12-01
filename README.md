# FileEclipse

FileEclipse is a command line utility that detects the true file type of a file by reading its magic number. File extensions can be misleading or intentionally changed, so this tool identifies files based on their actual binary signature.

This tool is useful for security analysis, malware investigation, digital forensics and general file verification.

---

## Features

* Reads the first bytes of a file to extract the magic number
* Compares extracted magic number with a built in signature database
* Detects document formats, images, archives, executables, audio, video and scripts
* Shows the magic number in uppercase hexadecimal
* Works cross platform on any system that runs Python

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
python main.py -f <path_to_file>
```

Example:

```
python main.py -f test.pdf
```

Output example:

```
Magic Number of the file 'test.pdf': 25504446
File type detected: PDF Document
File type detection completed.
```

Another example with an image:

```
python main.py -f image.png
```

Output:

```
Magic Number of the file 'image.png': 89504E470D0A1A0A
File type detected: PNG Image
File type detection completed.
```

Example for unknown or unsupported file types:

```
python main.py -f random.bin
```

Output:

```
Magic Number of the file 'random.bin': 4F2A7C11A93400AC
File type could not be determined
File type detection completed.
```

---

## How It Works

1. The program opens the file in binary mode.
2. It reads the first N bytes (default is 16).
3. It converts those bytes to uppercase hexadecimal.
4. It checks whether the beginning of that hex string matches known magic numbers.
5. If a match is found, the corresponding file type is displayed.
6. If no match is found, the file is marked as unknown.

---

## Vid Sample

https://github.com/user-attachments/assets/52108e5c-9c21-4a2b-a10a-2712514329be

## Supported File Types

FileEclipse currently detects:

* Documents including PDF, DOC, DOCX and XML
* Images including PNG, JPEG, GIF, TIFF and BMP
* Archives including ZIP, RAR, 7z, TAR and GZIP
* Executables including ELF, EXE and Java class files
* Audio and video containers such as MP3, FLAC, MP4 and MKV
* Certificates and scripts

You can extend this list by adding more magic numbers in the `magic_dict` dictionary.

---

## Future Improvements

* Automatic fallback to file extension guessing
* Support for deeper signature detection beyond the first bytes
* Optional verbose output
* Logging to external files

---
