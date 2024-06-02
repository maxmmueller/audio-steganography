<h1 align="center">
WaveWhisper
</h1>

<p align="center">
<a href="https://pypi.org/project/WaveWhisper/"><img src="https://img.shields.io/pypi/dw/wavewhisper?label=PyPi downloads"/></a>
<a href="https://github.com/maxmmueller/WaveWhisper/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache%202-blue"/></a>
</p>

<p align="center" style="font-size: 18px;">WaveWhisper is a lightweight Python library for steganographic encryption of text within the spectrogram of an audio file.</p>


<p align="center">
<img src="https://raw.githubusercontent.com/maxmmueller/WaveWhisper/main/images/screenshot.png">
</p>


## Note
This project was originally created for the German competition [*Explore Science Mannheim 2022*](https://www.explore-science.info/downloads/esma2022datensicherheit.pdf) in the category *data security* where it was ranked 2nd. I then made some small changes to turn it into this open source library.

In my attempt to make this library as lightweight as possible, it can currently operate without any external dependencies.


## Installation
To use this library, install the latest release from PyPi:
```
pip install wavewhisper
```

## Code example:

```python
from wavewhisper import Message

message = Message("My secret text")
message.encrypt("song.wav", "encrypted.wav") # carrier path and output path
```

!! FUll DOCS COMING SOON !!


## Contributing
Contributions to this project are welcome!

If you encounter any problems, find a bug or have feature requests, please open an [issue](https://github.com/maxmmueller/wavewhisper/issues/new).


## Support
If you find this project helpful, consider supporting its development by making a donation:

<a href="https://www.buymeacoffee.com/maxmmueller" target="_blank">
  <img src="https://raw.githubusercontent.com/maxmmueller/WaveWhisper/main/images/bmac.png" alt="Buy Me A Coffee" style="width: 140px;">
</a>
