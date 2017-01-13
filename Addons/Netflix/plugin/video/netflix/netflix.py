# http://openelec.tv

# http://kodi.wiki/view/Add-on_development
# http://kodi.wiki/view/Add-on_structure
# http://kodi.wiki/view/Addon.xml

# https://en.wikipedia.org/wiki/Python_syntax_and_semantics

from NetflixLogger import *

class Netflix:
    def __init__(self):
        self.Logger = NetflixLogger()
        self.SiteUrl = "https://netflix.com"
        self.LoginUrl = "https://netflix.com/Login"

        self.Logger.Verbose("Netflix class Initialization")
    
    def LoadLoginPage(self, message):
        try:
            if(message == ""):
                raise Exception("Argument Null Exception::[message]")

            print(self.LoginUrl)
        except Exception as ex:
            self.Logger.Error(repr(ex))


netflix = Netflix()
netflix.LoadLoginPage("")