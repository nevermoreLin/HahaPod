# The HahaPod Dataset

The HahaPod dataset is non-verbal laughter-based test dataset obtained from YouTube platform. This repository provides guidelines and scripts for downloading the dataset. 

## Download
The following procedures show how to collect Haha-pod
### Pre-requisites
* Install **ffmpeg**:
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install ffmpeg
```
* Clone Repo:
```bash
git clone https://github.com/nevermoreLin/HahaPod
```
* Install the latest yt-dlp:
```bash
python3 -m pip install yt-dlp==2023.7.6
```
* Start download:
```python
python downloader.py 
```

## License

The dataset is licensed under the **CC BY-NC-SA 4.0** license. This means that you can share and adapt the dataset for non-commercial purposes as long as you provide appropriate attribution and distribute your contributions under the same license. Detailed terms can be found [here](LICENSE).

## Important Notes

The information within this repository is accurate as of February 2023, but we do not guarantee that these videos may not be deleted or removed by the original authors or the platform at a later date. Additionally, if you do not wish for your voice to appear in the dataset or have any other concerns, you can contact us via email at yuke.lin@dukekunshan.edu.cn or ming.li369@dukekunshan.edu.cn.

## Citation

Please cite the paper below if you make use of the dataset:

```
@article{lin2023haha,
  title={Haha-Pod: An Attempt for Laughter-based Non-Verbal Speaker Verification},
  author={Lin, Yuke and Qin, Xiaoyi and Jiang, Ning and Zhao, Guoqing and Li, Ming},
  journal={arXiv preprint arXiv:2309.14109},
  year={2023}
}
```
