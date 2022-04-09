import dropbox
class TransferData:
    def __init__(self,access_token):
       self.access_token=access_token
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(fileFrom,'rb')
        dbx.fileUpload(f.read(),fileTo)
def main():
    access_token="sl.BFUM0_0mmBQjtt4kfgi2Qy_KRMi8yt3XzZSIx6lApr1AsbPdyoy9WAxGSQ7rrvLA7gmnxJ-OLPp-kzDkYtbV1fdyjCykOZPtijgQmz1WvV2NERFj3HC0nGNP9qStQyeFlZrt7oo"
    transferData=TransferData(access_token)  
    fileFrom=input("Enter File to transfer: ")
    fileTo=input("Enter Path to upload to DBX: ")
    transferData.uploadFile(fileFrom,fileTo)
    print("File Has Been Moved")
main()      