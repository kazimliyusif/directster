# Directory Brute Forcing Tool

## Description
Directster is a command-line tool written in Python for brute-forcing directories on web servers to discover hidden paths.

## Features
- Brute-force directories using a wordlist
- Customizable options for URL, wordlist file

## Installation
1. Clone the repository:
   git clone https://github.com/your-username/dirbuster-tool.git
   

## Usage

python dirbuster.py -u <URL> -w <wordlist_file> 
-u, --url: Specify the URL to scan.
-w, --wordlist: Specify the wordlist file containing directory paths.

## Example

python dirbuster.py -u http://example.com -w wordlist.txt -v
