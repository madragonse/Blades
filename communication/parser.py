

import json
from typing import List, final


def from_bytes_list(stream:List)->List:
    ret = []
    for data in stream:
        sp_dat = data.decode('utf-8').split('|')
        for pac_b in sp_dat:
            if pac_b == '':
                break
            try:
                ret.append(json.loads(pac_b))
            except Exception as e:
                print('Bytes on error: ' + str(pac_b))
                raise e

    return ret

class LOCollector:
    def __init__(self):
        self.__LO = None

    def from_bytes_list(self, stream:List)->List:
        ret = []
        

        for data in stream:
            sp_dat = data.decode('utf-8').split('|')
            if self.__LO != None:
                # print('-----------------------------------------------------------------++')
                # print('LO: '+str(self.__LO))
                # print("o bef and af: ")
                # print(sp_dat[0])
                sp_dat[0] = str(self.__LO) + sp_dat[0]
                # print(sp_dat[0])
                # print('-----------------')
                # print(sp_dat)
                self.__LO = None
                #raise Exception('ende')
            for pac_b in sp_dat:
                if pac_b == '':
                    break
                try:
                    ret.append(json.loads(pac_b))
                except Exception as e:
                    self.__LO = (pac_b)
                    # print(self.__LO)
                    # print('Bytes on error: ' + str(pac_b))
                    #raise e

        return ret