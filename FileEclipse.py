import argparse
import magic
from lang_detect import detect_programming_language

banner=r'''
░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓██████▓▒░ ░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░ 
                                                                                                                                  
                                                                                                                            
'''

arg=argparse.ArgumentParser(description="A simple command-line tool to check the extension of a given file using magic numbers.")
arg.add_argument("--file", "-f", type=str, required=True, help="Path to the file to be checked.")

args=arg.parse_args()

file=args.file 

def get_magic_number(file,num_bytes=16):
    try:
        with open(file,'rb') as f:
            magic_bytes=f.read(num_bytes)
            return magic_bytes.hex().upper()
    except FileNotFoundError:
        print(f"Error: The file was not found")

def main():
    print(banner)
    magic_bytes=get_magic_number(file)
    print(f"Magic Number of the file '{file}': {magic_bytes}")
    magic_dict={
   
    "25504446": "PDF Document",                     # PDF
    "D0CF11E0A1B1": "MS Office (Legacy DOC/XLS/PPT)",
    "504B0304": "ZIP Archive / DOCX / XLSX / PPTX",
    "504B34": "ZIP Archive (Variation)",
    "7B5C727466": "RTF Document",
    "3C3F786D6C": "XML Document",
    "EFBBBF": "UTF-8 BOM Text",
    "FFFE": "UTF-16 LE Text",
    "FEFF": "UTF-16 BE Text",

    "89504E47": "PNG Image",
    "FFD8FFE0": "JPEG Image (JFIF)",
    "FFD8FFE1": "JPEG Image (EXIF)",
    "FFD8FFDB": "JPEG Image",
    "FFD8FFEE": "JPEG Image",
    "47494638": "GIF Image",
    "49492A00": "TIFF Image",
    "4D4D002A": "TIFF Image (Big Endian)",
    "424D": "BMP Image",
    "52494646": "RIFF Container (WebP, AVI, etc)",

  
    "494433": "MP3 Audio (ID3 Tag)",
    "FFFB": "MP3 Audio (MPEG-1 Layer 3)",
    "4F676753": "OGG Audio",
    "664C6143": "FLAC Audio",
    "1A45DFA3": "MKV / WebM Video",
    "66747970": "MP4 / MOV Video",
    "000001BA": "MPEG Video",
    "000001B3": "MPEG Video (VOB)",


    "1F8B08": "GZIP Archive",
    "425A68": "BZIP2 Archive",
    "52617221": "RAR Archive v1.5",
    "52417221": "RAR Archive v5",
    "377ABCAF271C": "7-Zip Archive",
    "75737461": "TAR Archive (ustar)",


    "7F454C46": "ELF Executable",
    "4D5A": "Windows Executable (MZ Header)",
    "CAFEBABE": "Java Class File",
    "23": "Script / Shebang Possible",
    "3C3F706870": "PHP Script",
    "4D534346": "MSC (Microsoft Cabinet)",

    "53514C697465": "SQLite Database",
    "000100005374": "STL 3D Model (Binary)",

    "3082": "ASN.1 DER Certificate",
    "2D2D2D2D2D424547494E": "PEM Certificate / Key",
        
    }
    detected=False
    for Magic,file_type in magic_dict.items():
        if magic_bytes.startswith(Magic):
            print(f"File type detected: {file_type}")
            detected=True
            break
    if not detected:
        file_type=magic.from_buffer(open(file,'rb').read(2048))
        detected=True
        if(file_type=="ASCII text, with no line terminators"):
            print("File is probably a programming or scripting text file.")
            detected_lang=detect_programming_language(file)
            print(f"Detected programming language: {detected_lang}")    
        else:
            print(f"File type detected: {file_type}")
        if not detected:
            print("File type could not be determined.")
    print("FILE DETECTION COMPLETED.")

if __name__ == "__main__":
    main()
