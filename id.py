# coding: utf-8
import json, sys, os, watson_developer_cloud
from time import clock
from time import time as tim

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-11-07',
    username='01322091-01ae-4545-85e2-3fc1934f1b5f',
    password='jIMKNOUH3Bwh')
start_time = tim()

environments = discovery.get_environments()
environments = [x for x in environments['environments']]    
environment_id = environments[0]['environment_id']
# print(environment_id)
collection = discovery.list_collections(environment_id)
collections = [x for x in collection['collections']]
collection_id = collections[1]['collection_id']
print(collection_id)

#### hard coding the ids to make it faster
environment_id = '168946e2-4f0b-4398-8a56-b6799d99c2c3'
# collection_id = '8baa0d9c-57e8-479e-970c-8f95fca99ba5' ##old
# collection_id = '9df12949-305b-4b4f-90a1-bf6e5e43c3ff'
collection_id = '5d59fead-1f8f-46bd-8ee5-c6418bb961e5' ##iitd


