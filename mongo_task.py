import csv
from mongoengine import *
import pymongo


class OneExample(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    url = StringField(required=True)
    published_at = StringField(required=True)


class GetData(Document):

    def row_list(self):
        with open('raw_data.csv', 'r') as file:
            row_list = []
            unique_url = []
            reader = csv.reader(file)
            for row in reader:
                pymongo.MongoClient(host=['localhost:27017'])
                if row[4] not in unique_url:
                    row_list.append(row)
                else:
                    pass
        return row_list[1:]

    def job_propositions(self, row_list):
        self.row_list = row_list
        connect('scrap')
        for obj in self.row_list:
            user = {'title': obj[2], 'url': obj[4], 'published_at': obj[5], 'description': obj[6]}
            if not OneExample.objects.filter(url=user['url']).count():
                unique_user = OneExample(**user)
                unique_user.save()
        disconnect_all()


result = GetData()
data = result.row_list()
result = result.job_propositions(data)
