import json
modulesInfo = {}
modules = []
def runString(code):
    global modules
    quoteOpen = False
    specialCharOpen = False
    buildingKeyword = False
    keywordBuild = ""
    quoteBuild = ""
    keywords = []
    quotes = []
    for i in code:
        char = i
        if char == "\"":
            if quoteOpen:
                quoteOpen = False
                quotes.append(quoteBuild)
                quoteBuild = ""
            else:
                quoteOpen = True
        elif quoteOpen:
            quoteBuild = quoteBuild + char
        elif not " " == char:
            keywordBuild = keywordBuild + char
        elif " " == char:
            keywords.append(keywordBuild)
            keywordBuild = ""
    for i in keywords:
        keyword = i.lower()
        if keyword == "print":
            for i1 in quotes:
                print(i1)
        elif keyword == "add":
            for i1 in quotes:
                quote = i1.lower()
                if quote == "python":
                    modulesInfo["python"] = {"runLang":"pythondebug","runpy":"%quote%"}
                    modules.append("python")
                else:
                    print("koolCode WARN: custom modules not supported/module not found.")
        else:
            for i1 in modules:
                if modulesInfo[i1]["runLang"] == "python":
                    try:
                        for i2 in quotes:
                            quote = i2
                            code = modulesInfo[str(i1)][keyword].replace("%quote%", quote).replace("%nl%","\n")
                            eval(code)
                    except:
                        print(f"koolCode ERROR: Unknown keyword or module fail. Enable debug in your module settings if you are a module developer.")
                elif modulesInfo[i1]["runLang"] == "pythondebug":
                    try:
                        for i2 in quotes:
                            quote = i2
                            code = modulesInfo[str(i1)][keyword].replace("%quote%", quote)
                            eval(code)
                    except BaseException as error:
                        print(f"koolCode ERROR: Unknown keyword or module fail. Got {error}")

def runFile(dir):
    try:
        file = open(dir)
        content = file.readlines()
        content = [x.strip() for x in content]
        for i in content:
            runString(i) 
    except:
        print(f"koolCode ERROR: File not found ({dir})")
def noFile():
    runString(input("koolCode>"))
option = input("Welcome to koolCode console.\nWould you like to open a file? y/n\n")
if not option.lower() == "y":
    print("A file will not be opened. Type any commands below.")
    while True:
        noFile()
else:
    runFile(input("Our offcial file extention is .koc however you can open any file. Please type in the directory of the file. See Open Files in our guide for more info.\nFILE DIRECTORY:"))