import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        
        allFiles = os.walk(file_from)
        for root, directories, files in allFiles:
            for fil in files:
                start = file_from
                filePath = os.path.join(root, fil)
                f = open(filePath, "rb")
                relative_path = os.path.relpath(filePath, start)
                file_path_upload = os.path.join(file_to, relative_path)
                dbx.files_upload(f.read(), file_path_upload, mode=dropbox.files.WriteMode.overwrite)
                print("Files uploaded Successfully")

def main():
    access_token = "-wc2-QNFbW0AAAAAAAAAAYLNJYlHuuCHnbIedfQrIHhgPpvAPF4r_Oi_aGijINTq"

    transferdata = TransferData(access_token)

    file_from = input("Enter the folder path to upload files: ")
    file_to = input("Enter the name of the folder in which you want to upload files: ")

    if(os.path.exists(file_from)):
        if(file_to == ""):
            print("File name for the dropbox is empty")
        else:
            transferdata.upload_files(file_from, file_to)
    else:
        print("File Not Found")
        

main()