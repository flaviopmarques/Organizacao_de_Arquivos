import struct
import hashlib
import os
import time

print time.strftime('%X')

hashSize = 12000000
fileName = "recorteBolsa201704_10000000.txt"
indexName = "recorteBolsa201704-hash_10000000.txt"
#dataFormat = "5s5s30s5s5s5s5s15s40s32s10s8s2s"
indexFormat = "14sLL"
keyColumnIndex = 7

#dataStruct = struct.Struct(dataFormat)
indexStruct = struct.Struct(indexFormat)

def h(key):
    global hashSize
    return int(hashlib.sha1(key).hexdigest(),16)%hashSize

fi = open(indexName,"wb")
emptyIndexRecord = indexStruct.pack("",0,0)
for i in range(0,hashSize):
    fi.write(emptyIndexRecord)
fi.close()

f = open(fileName,"rb")
fi = open(indexName,"r+b")

fi.seek(0,os.SEEK_END)
fileIndexSize = fi.tell()
print "IndexFileSize", fileIndexSize
#fi.seek(0,os.SEEK_END)

recordNumber = 0
while True:
    #line = f.read(dataStruct.size)
    
    line = f.readline()
    #print line
    if line == "": # EOF
        break
    #record = dataStruct.unpack(line)
    #p = h(record[keyColumnIndex])
    record = line.split("\t")
    p = h(record[keyColumnIndex])
    fi.seek(p*indexStruct.size,os.SEEK_SET)
    indexRecord = indexStruct.unpack(fi.read(indexStruct.size))
    fi.seek(p*indexStruct.size,os.SEEK_SET)
    if indexRecord[0][0] == "\0":
        fi.write(indexStruct.pack(record[keyColumnIndex],recordNumber,0))
    else:
        nextPointer = indexRecord[2]
        fi.write(indexStruct.pack(indexRecord[0],indexRecord[1],fileIndexSize))
        fi.seek(0,os.SEEK_END)
        fi.write(indexStruct.pack(record[keyColumnIndex],recordNumber,nextPointer))
        fileIndexSize = fi.tell()
    recordNumber += 1
f.close()
fi.close()

print time.strftime('%X')
