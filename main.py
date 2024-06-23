import os
import subprocess
import json
import random
import time
import requests
import tempfile

def import_json_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)

def start_nonton(videos):
    # Mendapatkan direktori saat ini
    current_directory = os.getcwd()
    for i in range(5):
        os.system(f'Xvfb :{i} -screen {i} 1024x768x24 &')
        os.environ['DISPLAY'] = f':{i}'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.114 Safari/537.36"
        profile_dir = f'Profile{i}'
        
        random_video = random.choice(videos)
        url = random_video['url']
        
        if profile_dir == 'Profile1':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.61 Safari/537.36"
        elif profile_dir == 'Profile2':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.55 Safari/537.36"
        elif profile_dir == 'Profile3':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.3"
        elif profile_dir == 'Profile4':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.141 Safari/537.36"
        elif profile_dir == 'Profile0':
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.76 Safari/537.36"

        # Membuat perintah untuk menjalankan Google Chrome
        start_time_yt = random.randrange(1, 400)
        Url_browser = f'https://youtu.be/{url}&t={start_time_yt}'
        print(f'start Url: {Url_browser}')
        window_size = '600,400'
        command_start_chrome = [
            'google-chrome',
            '--no-sandbox',
            '--disable-gpu',
            f'--user-data-dir={current_directory}/profiles/{profile_dir}',
            f'--profile-directory={profile_dir}',
            f'--app={Url_browser}',
            '--autoplay-policy=no-user-gesture-required',
            f'--user-agent={user_agent}',
            '--disable-extensions'
        ]
        try:
            # shutil.rmtree(f'profiles/{profile_dir}')
            print(f'del {profile_dir}')
        except Exception as e:
            print(f'Error on delete last profile folder: {e}')
        
        chrome_process = subprocess.Popen(command_start_chrome)
        time.sleep(10)
        os.system('xdotool key enter')
        time.sleep(1)
        
        #with mss.mss() as sct:
        #    with tempfile.TemporaryDirectory() as tmpdirname:
        #        screenshot_path = os.path.join(tmpdirname, 'screenshot.png')
        #        screenshot = sct.shot(output=screenshot_path)
        #        print(f'Screenshot saved to {screenshot_path}')

if __name__ == "__main__":
    url_json = 'https://raw.githubusercontent.com/mooghen2s/xra/main/videos.json'
    videos = import_json_from_url(url_json)
    start_nonton(videos)
    os.system('killall chrome')
    os.system('killall Xvfb')
    for start_loops in range(115):
        start_nonton(videos)
        time.sleep(1000)
        os.system('killall chrome')
        os.system('killall Xvfb')
