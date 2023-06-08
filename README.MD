# MystrKl33n - Wordlist Smallerizer

MystrKl33n is a Python script that allows you to manipulate a word list file by removing duplicates, filtering words based on a blacklist, performing English word checks, and optionally saving the processed word list to a file.

## Features

- Remove duplicate words from the word list.
- Filter out words based on a blacklist.
- Perform English word checks using multiple dictionaries.
- Support for case-insensitive checks.
- Print the resulting word list to stdout or save it to a file.

## Prerequisites

Ensure you have the following packages installed:

- `enchant` library
    - **Debian-based** systems
    `sudo apt-get install enchant`
    
    - **Red Hat-based** systems: 
    `sudo dnf install enchant`
    
    - **Arch Linux**: 
    `sudo pacman -S enchant`
    
    - **Gentoo**: 
    `sudo emerge enchant`
    
    - **Alpine**: 
    `sudo apk add enchant`
    
    - **openSUSE**: 
    `sudo zypper install enchant`


## Usage

1. Install the required dependencies by running the following command:

   ```plaintext
   pip install -r requirements.txt
   ```

2. Run the script with the desired options and arguments:

   ```plaintext
   python main.py [OPTIONS] WORDLIST
   ```

   - `WORDLIST`: Path to the word list file.

   Available Options:

   - `-d, --remove-duplicates`: Remove duplicate words from the word list.
   - `-b, --blacklist FILE`: Path to the blacklist file for filtering out words.
   - `-o, --output FILE`: Output file path for saving the processed word list.
   - `-e, --english-check DICTS`: Comma-separated list of dictionaries for English word check.
   - `-c, --case-insensitive`: Perform case-insensitive checks.
   - `-s, --show-stats`: Shows some stats. 

## Examples

1. Remove duplicate words from a word list file and print the resulting list:

   ```plaintext
   python main.py wordlist.txt -d
   ```

2. Filter out words from a word list file based on a blacklist file and save the result to a new file:

   ```plaintext
   python main.py wordlist.txt -b blacklist.txt -o filtered_wordlist.txt
   ```

3. Perform English word checks using multiple dictionaries and print the resulting list:

   ```plaintext
   python main.py wordlist.txt -e "en_US,en_GB"
   ```

   This example assumes that the `en_US` and `en_GB` dictionaries are available.

4. Perform case-insensitive checks when comparing words in the blacklist:

   ```plaintext
   python main.py wordlist.txt -b blacklist.txt -c
   ```

   This example will perform case-insensitive checks when filtering out words based on the blacklist.

## Thank You

A special shout out to ChatGPT and OpenAI for doing most of the heavy-lifting with this one. :muscle:

## License

This project is licensed under the [MIT License](LICENSE).

