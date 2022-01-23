import requests
import typing
from typing import Literal, Optional


class Asset:
    BASE = 'https:'

    def __init__(self, url):
        self._url = f'{self.BASE}{url}'

    def __str__(self) -> str:
        return self._url
        
    def __repr__(self):
        shorten = self._url.replace(self.BASE, '')
        return f'<Asset url={shorten!r}>'

    def __hash__(self):
        return hash(self._url)


    @property
    def url(self):
        return self._url


class QrCode:
    def __init__(
        self,
        data: str,
        size: int = 300,
        file: str = 'png',
        download: bool = False
    ):
        self.data = data
        self.size = size
        self.file = file
        self.download = download



    def generate(
        self,
        body: Literal[
            'square',
            'circle',
            'circular',
            'japnese',
            'pointed-edge-cut',
            'pointed-smooth',
            'rounded-in-smooth',
            'diamond',
            'mosaic',
            'circle-zebra',
            'edge-cut',
            'leaf',
            'pointed-in',
            'round',
            'rounded-pointed',
            'dot',
            'circle-zebra-vertical',
            'edge-cut-smooth',
            'pointed',
            'pointed-in-smooth',
            'rounded-in',
            'star'
        ] = 'square',
        eye: Literal[
            'frame0',
            'frame1',
            'frame2',
            'frame3',
            'frame4',
            'frame5',
            'frame6',
            'frame7',
            'frame8',
            'frame10',
            'frame11',
            'frame12'
            'frame13',
            'frame14',
            'frame16'
        ] = 'frame0',
        eyeBall: Literal[
            'ball0',
            'ball1',
            'ball2',
            'ball3',
            'ball5',
            'ball6',
            'ball7'
            'ball8',
            'ball10',
            'ball11',
            'ball12',
            'ball13',
            'ball14',
            'ball15',
            'ball16',
            'ball17',
            'ball18',
            'ball19'
        ] = 'ball0',
        erf1: Optional[list] = [],
        erf2: Optional[list] = [],
        erf3: Optional[list] = [],
        brf1: Optional[list] = [],
        brf2: Optional[list] = [],
        brf3: Optional[list] = [],
        bodyColor: typing.Union[str, hex] = '#000000',
        bgColor: typing.Union[str, hex] = '#ffffff',
        eye1Color: typing.Union[str, hex] = '#000000',
        eye2Color: typing.Union[str, hex] = '#000000',
        eye3Color: typing.Union[str, hex] = '#000000',
        eyeBall1Color: typing.Union[str, hex] = '#000000',
        eyeBall2Color: typing.Union[str, hex] = '#000000',
        eyeBall3Color: typing.Union[str, hex] = '#000000',
        gradientColor1: typing.Union[str, hex] = None,
        gradientColor2: typing.Union[str, hex] = None,
        gradientType: Literal['linear', 'radial'] = 'linear',
        gradientOnEyes: bool = False,
        logo: str = None,
        logoMode: Literal['default', 'clean'] = 'default'
    ) -> str:
        json = {
            "data": self.data,
            "config": {
                "body": body,
                "eye" : eye,
                "eyeBall": eyeBall,
                "erf1": erf1,
                "erf2": erf2,
                "erf3": erf3,
                "brf1": brf1,
                "brf2": brf2,
                "brf3": brf3,
                "bodyColor": bodyColor,
                "bgColor": bgColor,
                "eye1Color": eye1Color,
                "eye2Color": eye2Color,
                "eye3Color": eye3Color,
                "eyeBall1Color": eyeBall1Color,
                "eyeBall2Color": eyeBall2Color,
                "eyeBall3Color": eyeBall3Color,
                "gradientColor1": gradientColor1,
                "gradientColor2": gradientColor2,
                "gradientType": gradientType,
                "gradientOnEyes": gradientOnEyes,
                "logo": logo,
                "logoMode": logoMode
            },
            "size": self.size,
            "download": self.download,
            "file": self.file
        }

        req = requests.post(
            'https://api.qrcode-monkey.com/qr/custom',
            json = json
        )
        if self.download:
            _url = req.json()['imageUrl']
            return Asset(_url)

        return req.content