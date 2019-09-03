from WebDriverModule import WebDriverModule
from OsModule import OsModule
# webDriverModule = WebDriverModule()
osModule = OsModule() 
# driver = webDriverModule.getChromeDriver()
# fileUrl = 'http://www.soumu.go.jp/johotsusintokei/whitepaper/ja/h30/pdf/30daijin.pdf'
# driver.get(fileUrl)

print(osModule.getLatestDownloadedFileName())
assert False