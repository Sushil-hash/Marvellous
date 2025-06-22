import datetime
import hashlib
import os.path
import sys


class Ass22:
    def __init__(self):
        self.time = datetime.datetime.now()
        logfilename = str(self.time).replace(":","_").replace("-","_").replace(".","_")
        logfilename = logfilename + ".txt"
        self.lobj = open(logfilename,"w")

    def validate_dir(self,dir):
        if not os.path.isabs(dir):
            dir = os.path.abspath(dir)
        if not os.path.exists(dir) and not os.path.isdir(dir):
            print("Invalid path")
        return dir

    def findchecksum(self,dir):
        res = {}

        for folder, sf, files in os.walk(dir):
            for file in files:
                algo = hashlib.md5()
                filename = os.path.join(dir,file)
                fobj = open(filename,"rb")
                buffer = fobj.read(1000)
                while len(buffer)>0:
                    algo.update(buffer)
                    buffer = fobj.read(1000)
                checksum = algo.hexdigest()
                if checksum in res:
                    res[checksum].append(filename)
                else:
                    res[checksum] = [filename]
        return res

    def deleteduplicate(self,dres):
        filecount = 0
        deletecount = 0
        deletedfilelist = []
        for key,value in dres.items():
            for file in value:
                filecount = filecount + 1
                if filecount > 1:
                    deletedfilelist.append(file)
                    os.remove(file)
                    deletecount = deletecount + 1
            filecount = 0
        msg = f"Total deleted files : {deletecount}"
        print(msg)
        return deletedfilelist

    def writelog(self,dres):
        fcont = str(dres)
        self.lobj.write(fcont)
        self.lobj.close()

    def main(self):
        dir = sys.argv[1]
        dir =  self.validate_dir(dir)
        fres = self.findchecksum(dir)
        dres = self.deleteduplicate(fres)
        self.writelog(dres)

if __name__ == "__main__":
    obj = Ass22()
    obj.main()