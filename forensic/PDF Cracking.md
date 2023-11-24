# PDFCrypt
Find the file hash
```bash
python pdf2john.py encrypted.pdf > pdfhash.txt
```

Edit the file to leave only the hash

Encryption used
```
10500
```

Attack the pdf
```bash
hashcat -a 0 -m 10500 pdfhash.txt /usr/share/wordlists/rockyou.txt
```