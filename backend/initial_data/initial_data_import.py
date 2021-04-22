import json
import os
import mimetypes
import requests
import argparse
import subprocess
import string
import random


def parser_files(path):
    files = []
    products = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if 'text/plain' in mimetypes.guess_type(filename):
                files.append(os.path.join(dirpath, filename))

    for filename in files:
        file = open(filename)
        lines = file.readlines()
        for line in lines[2:]:
            product = dict()
            list_text = line.split()
            product['name'] = ' '.join(list_text[:-4])
            product['quantity'], product['proteins'], product['carbohydrates'], product['fats'] = [
                int(value) for value in list_text[-4:]]
            products.append(product)
        file.close()

    return products


def create_superuser(username, password):
    proc = subprocess.Popen(
        ["python", "/app/manage.py", "create_superuser", username, password], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    print(out.decode("utf-8"))


def delete_superuser(username):
    proc = subprocess.Popen(
        ["python", "/app/manage.py", "delete_superuser", username], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    print(out.decode("utf-8"))


def create_user_token(username):
    proc = subprocess.Popen(
        ["python", "/app/manage.py", "drf_create_token", username], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out.split()[2].decode("utf-8")


def register_products(products, token):
    url_service = 'http://localhost:9000/api/food/'
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Token {token}'
    }
    for product in products:
        r = requests.post(url_service, data=json.dumps(
            product), headers=headers)
        print(r.json())


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-u", "--user", required=True)
    # args = parser.parse_args()
    string_random = ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=10))
    username = string_random
    password = string_random
    path = os.getcwd() + '/alimentos'
    products = parser_files(path)
    if products:
        create_superuser(username, password)
        token = create_user_token(username)
        if token:
            register_products(products, token)
            delete_superuser(username)
