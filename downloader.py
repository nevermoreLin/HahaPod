import yt_dlp
# -------------
import time, argparse, os, json
from tqdm import tqdm
from yt_dlp.utils import download_range_func
import logging
logging.basicConfig(level=logging.INFO)  # configure logging level to INFO

parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--data_path', 
                    default='data/timestamp', 
                    type=str,
                    help="timestamp location")
parser.add_argument('--save_path', 
                    default='backup', 
                    type=str,
                    help="where to save files")
args = parser.parse_args()
def job_video(urls,base_path,utt,start,end):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(base_path,utt+'.%(ext)s'),
        'download_ranges': download_range_func(None, [(start, end)]),
        # 'download_ranges': download_range_func([], [(100, 200), (250, 300)]),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192', }],
        'force_keyframes_at_cuts': True,
        'postprocessor_args': [
            '-ac', '1',
            '-ar', '16000',
            '-f', 'WAV',
        ],
        'ignoreerrors': True,
        # 'sleep_interval_requests': 0.5,
        'sleep_interval': 0.5,
        'max_sleep_interval': 1,
        'verbose': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)
    return error_code
if __name__ == '__main__':
    
    print("*"*15)
    print("* Download Starts *")
    print("*"*15)
    os.makedirs(args.save_path,exist_ok=True)
    os.makedirs(os.path.join(args.save_path,"laugh"),exist_ok=True)
    os.makedirs(os.path.join(args.save_path,"speech"),exist_ok=True)
    for wd in ['speech','laugh']:
        with open(os.path.join(args.data_path,wd)) as file:
            for line in file:
                [utt,url,start,end] = line.strip().split()
                start, end = float(start), float(end)
                err_code = job_video(url,os.path.join(args.save_path,wd),utt,start,end)
                if err_code != 0:
                    logging.error("Video %s not available!"%url)
