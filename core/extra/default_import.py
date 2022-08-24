from pathlib import Path
from core.models import Category, County


def readfile(dir):
    with open(dir) as f:
        lines = f.readlines()
    return lines


def import_category():
    file = Path(__file__).parent.joinpath('files/category.txt')
    lines = readfile(file)
    for line in lines:
        data = line.replace("\n", "").split(",")
        cate = Category.objects.get_or_create(sn=data[0], name=data[1])
        print(cate)


def import_county():
    file = Path(__file__).parent.joinpath('files/country.txt')
    lines = readfile(file)
    for line in lines:
        data = line.replace("\n", "").split(",")
        county = County.objects.get_or_create(sn=data[0], name=data[1])
        print(county)

