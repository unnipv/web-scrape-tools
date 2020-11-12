import requests
import img2pdf
import sys
import os
import glob

#Image Downloader
def img_get(ch_num):
    j = 1
    user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    headers = {
    'User-Agent': user_agent,
    }
    while j<1000:
        if j<10:
            img_ind = "00" + str(j)
        elif j>=10 and j<100:
            img_ind = "0" + str(j)
        else:
            img_ind = str(j)
        URL = "https://cdn.read7deadlysins.com/file/AnimeRleases/OP_C_" + str(ch_num)+ "_" + img_ind + ".jpg"
        filename = "D:\One Piece\Downloads\\" + str(j)+".jpg"
        r = requests.get(URL,headers=headers)
        if r.ok:
            with open(filename, 'wb') as f:
                f.write(r.content)
            j+=1
        else:
            return j-1


#PDF maker
def img2PDF(ch_num,max_ind):
    dirname = "D:\One Piece\Downloads"
    ch_file_name="D:\One Piece\\" + str(ch_num)+ ".pdf"
    with open(ch_file_name,"wb") as f:
        imgs=[]
        for fname in os.listdir(dirname):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        imgs_sorted = sorted(imgs, key=lambda file_ind: int(file_ind.split("Downloads\\")[1].split(".")[0]))
        # print(imgs_sorted)
        f.write(img2pdf.convert(imgs_sorted[:max_ind]))
    print("Chapter ",ch_num," downloaded.")
    # files = glob.glob(dirname + "*")
    # for f in files:
    #     os.remove(f)
    # print("Deleted image files")

def main():
    chapters = list(map(int,sys.argv[1:]))
    for i in range(chapters[0],chapters[1]+1):
        img_ind = img_get(i)
        img2PDF(i,img_ind)
    print("Download Complete")

if __name__ == "__main__":
    main()
