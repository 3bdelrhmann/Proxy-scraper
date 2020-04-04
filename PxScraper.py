import requests
def WebsitesList():
    with open("Px-webs.txt", "r") as pxWebs:
        pxWebs = pxWebs.read().split("\n")
    return pxWebs

def GetRawData(WebLink):
    R = requests.get(WebLink)
    webContent = R.content
    return webContent

def WriteProxy(proxy):
    with open("Results.txt", "a") as p:
        p.write(proxy+"\n")

def RawToList(RawData):
    RawData = str(RawData)
    toBeReplaced = list("<>!@#$%^&*()+=\ /,|;:'\"-")
    for Sign in toBeReplaced:
        RawData = RawData.replace(Sign, " ")
    SplitedRawData = RawData.split(" ")
    return SplitedRawData

def CheckIfProxy(proxy):
    isProxy = False
    StrL = proxy.split(".")
    for Num in StrL:
        if Num.isdigit():
            isProxy = True
    return isProxy

def AnalyseRawData(RawData):
    getPort = False
    proxy = ''
    for Str in RawData:
        if getPort:
            if Str.isdigit():  # == that`s is port of our proxy in proxy variable now
                proxy += Str
                WriteProxy(proxy)
                proxy = ''
                getPort = False
        elif (Str+'x')[0].isdigit() and Str.count(".") == 3:
            isProxy = CheckIfProxy(Str)
            if isProxy == True:
                proxy += Str + ':'
                getPort = True
	
def Run():
    Websites = WebsitesList()
    for website in Websites:
        try:
            RawData = GetRawData(website)
            List = RawToList(RawData)
            AnalyseRawData(List)
        except:
            pass

Run()
print(datetime.now() - startTime)

