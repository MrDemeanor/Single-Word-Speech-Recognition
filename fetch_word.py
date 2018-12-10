from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import os
import string
import random
from random import randint
from progress.bar import Bar

bar = Bar('Adding ' + sys.argv[1] + ' to the dataset', fill='=', suffix='%(percent)d%%')

# Initialize chrome web browser
driver = webdriver.Chrome()
# Go to the website
driver.get("https://lingojam.com/RobotVoiceGenerator")

# Click the speak button so we can download .wav files instead of .html
speak = driver.find_element_by_id("play")
speak.click()

# Input a word into the text box so we can generate waveforms
input_word = driver.find_element_by_id("english-text")
input_word.send_keys(sys.argv[1])

# Get the pitch bar ready to be incremented
pitch = driver.find_element_by_id("voice_pitch")

# Identify where the download button is
download = driver.find_element_by_xpath('//*[@id="download_link"]')

# Wait for the previous line to register
time.sleep(3)

# Download the file, then increment the pitch
for x in range(0, 100):
    bar.next()
    speak.click()
    # Change the name of each downloaded file every 50 downloads
    if x % 50 == 0 and x is not 0:
        files = os.listdir('/Users/brentredmon/Downloads')
        for file in files:
            if(file[:5] == 'audio' and "download" not in file and "html" not in file):
                modified_name = ""
                for i in range(0, 10):
                    modified_name += random.choice(string.ascii_letters)
                    modified_name += random.choice(string.ascii_letters)
                    modified_name += str(randint(0, 1000))
                
                try:
                    os.rename('/Users/brentredmon/Downloads/' + file[:5] + ' ' + file[6:], '/Users/brentredmon/Downloads/' + modified_name + '.wav')
                except Exception:
                    os.rename('/Users/brentredmon/Downloads/' + file[:5] + '.wav', '/Users/brentredmon/Downloads/' + modified_name + '.wav')
                except Exception as e:
                    print('Whoops!')
    
    download.click()
    for i in range(5):
        pitch.send_keys(Keys.ARROW_RIGHT)

# Removes stray 
files = os.listdir('/Users/brentredmon/Downloads')
for file in files:
    if "html" in file:
        os.remove('/Users/brentredmon/Downloads/' + file)
    
    elif file[:5] == 'audio' and "download" not in file and "html" not in file:
        modified_name = ""
        for i in range(0, 10):
            modified_name += random.choice(string.ascii_letters)
            modified_name += random.choice(string.ascii_letters)
            modified_name += str(randint(0, 1000))
                
        try:
            os.rename('/Users/brentredmon/Downloads/' + file[:5] + ' ' + file[6:], '/Users/brentredmon/Downloads/' + modified_name + '.wav')
        except Exception:
            os.rename('/Users/brentredmon/Downloads/' + file[:5] + '.wav', '/Users/brentredmon/Downloads/' + modified_name + '.wav')
        except Exception as e:
            print('Whoops!')

bar.finish()

driver.close()

# files = os.listdir('/Users/brentredmon/Downloads')
# os.mkdir('/Users/brentredmon/Documents/School/Fall_2018/ML/Final_Project/dataset/' + sys.argv[1])
# counter = 0
# for file in files:
#     try:
#         if file[0] is not '.':
#             link = '/Users/brentredmon/Downloads/' + file
#             y, sr = librosa.load(link, 44100, duration=2.0)
#             librosa.output.write_wav('/Users/brentredmon/Documents/School/Fall_2018/ML/Final_Project/dataset/' + str(sys.argv[1]) + '/' + str(counter) + '.wav', y, sr)
#             counter += 1
#     except:
#         print('Messed up on file ' + file)