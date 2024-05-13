from optparse import OptionParser
import requests
import time

print("""


  _____  _               _       _            
 |  __ \(_)             | |     | |           
 | |  | |_ _ __ ___  ___| |_ ___| |_ ___ _ __ 
 | |  | | | '__/ _ \/ __| __/ __| __/ _ \ '__|
 | |__| | | | |  __/ (__| |_\__ \ ||  __/ |   
 |_____/|_|_|  \___|\___|\__|___/\__\___|_|__ 
         | |           \ \   / /       (_)/ _|
         | |__  _   _   \ \_/ /   _ ___ _| |_ 
         | '_ \| | | |   \   / | | / __| |  _|
         | |_) | |_| |    | || |_| \__ \ | |  
         |_.__/ \__, |    |_| \__,_|___/_|_|  
                 __/ |                        
                |___/                         
                  
""")

print("Program başlayır...")
 
time.sleep(4)


def directster(url, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            path = line.strip()
            full_url = url + "/" + path
            response = requests.get(full_url)
            if response.status_code == 200:
                print("[*] Tapıldı: " + full_url)

def main(): 
    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="Skan ediləcək URL-i qeyd edin.")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Wordlist faylını qeyd edin.")
    (options, _) = parser.parse_args()
    
    url = options.url
    wordlist = options.wordlist

    if not url or not wordlist:
        parser.error("URL və wordlist təyin edilməlidir.")

    directster(url, wordlist)

if __name__ == "__main__":
    main()
