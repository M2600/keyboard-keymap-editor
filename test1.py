import webbrowser

class link_opener():
    def __init__(self):
        pass

    def open_link_in_default_browser(self, url):
        webbrowser.open(url, new=2)