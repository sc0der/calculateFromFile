import csv
import glob


class CsvParser:

    def __init__(self, filename) -> None:
        self.rows = []
        self.filename = filename
        self.objects = []
        self.keys = []
        self.objs = self._data
        self.datas = self.getUsefulData
    
    @property
    def _data(self):
        file = open(self.filename)
        csvreader = csv.reader(file)
        for row in csvreader:
            self.rows.append(row)
        file.close()
        return self.rows
    
    @property
    def getUsefulData(self):
        for row in self.objs:
            key = str(row).split(";")[6]
            val = str(row).split(";")[7]
            self.objects.append({ f"{key}":f"{val}" })

        return self.objects

    @property
    def getKeys(self):
        for row in self.datas:
            for k in dict(row):
                self.keys.append(k)
        return set(self.keys)
# 1802873
    def counter(self):
        data = self.datas
        real_data = []
        for item in self.getKeys:
            value = 0
            for row in data:
                if item == list(row.keys())[0]:
                        value += int(list(row.values())[0])

            real_data.append(
                {
                    "key": item,
                    "value":value
                }
            )
        return real_data

class Sliyanie():
    def __init__(self) -> None:
        self.keys = [] 
        self.csvFilenamesList = glob.glob('*.csv')
    
    @property
    def combineData(self):
        data = []
        keys = []
        for filename in self.csvFilenamesList:
            parser = CsvParser(filename)
            for item in parser.counter():
                data.append(item)
                keys.append(item['key'])
        return data, keys

    def _data(self):
        for row in set(self.combineData[1]):
            value = 0
            for item in self.combineData[0]:
                if row == item["key"]:
                    value += int(item["value"])
            print(row, " : ", value)

        return True

    def run(self):
        self._data()    

if __name__ == "__main__":
    s = Sliyanie()
    s.run()