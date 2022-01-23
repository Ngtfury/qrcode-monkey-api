class QrCodeImage:
    BASE = 'https:'

    def __init__(self, url):
        self._url = f'{self.BASE}{url}'

    def __str__(self) -> str:
        return self._url
        
    def __repr__(self):
        shorten = self._url.replace(self.BASE, '')
        return f'<QrCodeImage url={shorten!r}>'

    def __hash__(self):
        return hash(self._url)


    @property
    def url(self):
        return self._url
