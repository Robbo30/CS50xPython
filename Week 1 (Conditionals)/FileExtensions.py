fileName = input("Enter the full name of a file: ")
fileName = fileName.lower()

if ".gif" in fileName:
    print("image/gif")
elif ".pg" in fileName:
    print("image/jpg")
elif ".jpeg" in fileName:
    print("image/jpeg")
elif ".png" in fileName:
    print("image/png")
elif ".pdf" in fileName:
    print("application/pdf")
elif ".txt" in fileName:
    print("text/txt")
elif ".zip" in fileName:
    print("application/zip")
else:
    print("application/octet-stream")
