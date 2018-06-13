# coding: utf-8
import json, sys, os, watson_developer_cloud
from time import clock
from time import time as tim
def query(discovery, environment_id, collection_id, q):
    ## query_options = {'query': 'best', 'highlight':'true','passages':'false', 'return':'title,url','count':'2'}
    query_options = {'query': q, 'passages':'true'}
    results = discovery.query(environment_id, collection_id, query_options)
    # print(json.dumps(results, indent=2))

    result_count = results['matching_results']
    print("result_count = " + str(result_count))
    ll=[]
    passages_array=results['passages']
    passages_array_len = len(passages_array)
    # print("passage= " +  passages_array)
    print("Number of passages= " + str(passages_array_len))

    for i in range(passages_array_len):
        l=[]
        field = results['passages'][i]['field']
        if field == 'text' :
            doc_id_p = results['passages'][i]['document_id']
            offset = results['passages'][i]['start_offset']
            text = results['passages'][i]['passage_text']
            
            # for j in range(result_count):
            for j in range(passages_array_len):
                doc_id_r = results['results'][j]['id']
                if doc_id_p == doc_id_r :
                    file_name = results['results'][j]['extracted_metadata']['filename'] 
                    file_name = file_name[:-10] # + ".webm"
                    print("file_name= " + file_name)
                    # print("file_id= " + doc_id_p)
                    print("offset= " + str(offset))
                    print(text)
                    l.append(offset)
                    l.append(file_name)
                    l.append(text)### added on 15th april
                    break
            if len(l)==3:##==2  changed on 15th april
                ll.append(l)
    print("ll.size() = " + str(len(ll)))
    return ll

    # path = "/home/brojokm/Downloads/video/html/" + file_name    
    # file_name = file_name[:-10] + ".webm"
    # print(file_name)

def get_time(filename, offset, filepath, timepath):
    file = filepath + filename + "_punc.html"
    time = timepath + filename + "_time.txt"
    word_offset = 1
    text = ""
    with open(file) as file:
        for line in file:
            text = text + line

    for i in range(offset):
        if text[i]==' ':
            word_offset += 1

    print("word_offset = " + str(word_offset))
    ans=0
    word_count=0
    with open(time) as file:
        for line in file:
            word_count +=1
            if word_count == word_offset :
                ans = line
                break
    print("time= " + str(ans))
    return ans




def upload(discovery, environment_id,collection_id):
    for file in os.listdir("/home/brojo/Flask/flask/localizer/html/"):
        with open(os.path.join(os.getcwd(),'/home/brojo/Flask/flask/localizer/html/', file)) as fileinfo:
           res = discovery.add_document(environment_id=environment_id, collection_id=collection_id, file_info=fileinfo)
           print(res)

def create_delete(discovery, environment_id):
    # res = discovery.delete_collection(environment_id=environment_id, collection_id=collection_id)
    collection = discovery.create_collection(environment_id=environment_id, name='Thesis', description="Thesis. Created on 10th Feb")





def localizer(q): ## 2016-11-07    
# def main():
    discovery = watson_developer_cloud.DiscoveryV1(
        '2016-11-07',
        username='01322091-01ae-4545-85e2-3fc1934f1b5f',
        password='jIMKNOUH3Bwh')
    start_time = tim()

    # environments = discovery.get_environments()
    # environments = [x for x in environments['environments']]    
    # environment_id = environments[0]['environment_id']
    # print(environment_id)
    # collection = discovery.list_collections(environment_id)
    # collections = [x for x in collection['collections']]
    # collection_id = collections[0]['collection_id']
    # print(collection_id)

    #### hard coding the ids to make it faster
    environment_id = '168946e2-4f0b-4398-8a56-b6799d99c2c3'
    # collection_id = '8baa0d9c-57e8-479e-970c-8f95fca99ba5' ##old
    collection_id = '9df12949-305b-4b4f-90a1-bf6e5e43c3ff'


    ll = query(discovery, environment_id, collection_id, q)

    filepath = "/home/brojo/Flask/flask/localizer/html/"
    timepath = "/home/brojo/Flask/flask/localizer/time/"

    print("getting time")
    llst =[]

    for l in ll:
        lst = []
        print("---------------")
        print(l[0])
        print(l[1])
        print("---------------------------------")
        time = get_time(l[1], l[0], filepath, timepath)
        lst.append(l[1]) ##filename
        lst.append(time)
        lst.append(l[2]) ###added on 15th april--text
        llst.append(lst)

    end_time = tim()
    executeion_time = end_time - start_time
    print("Total time taken ") + str(executeion_time) +" seconds"
    print("--------------------------------------------------------------------------------------------------------")
    return llst


 
# def main():
#     discovery = watson_developer_cloud.DiscoveryV1(
#         '2016-11-07',
#         username='01322091-01ae-4545-85e2-3fc1934f1b5f',
#         password='jIMKNOUH3Bwh')
#     # environment = discovery.create_environment(name="Thesis-env", description="This will be used for thesis")

#     environments = discovery.get_environments()
#     # print(json.dumps(environments['environments'][0]['index_capacity']['documents'], indent=2))

#     environments = [x for x in environments['environments']]
#     environment_id = environments[0]['environment_id']
#     # print(environment_id)
#     # create_delete(discovery, environment_id)
#     collection = discovery.list_collections(environment_id)
#     collections = [x for x in collection['collections']]
#     # print(json.dumps(collections, indent=2))
#     # collection_id = collections[0]['collection_id']
#     # print(collection_id)
#     # configuration_id = collections[0]['configuration_id']
#     collection_id = collections[1]['collection_id']
#     print(collection_id)
#     import pprint
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(collections)
#     # upload(discovery, environment_id, collection_id)

#     # q = "nucleon"

#     # ll = query(discovery, environment_id, collection_id, q)

#     # filepath = "/home/brojokm/Downloads/video/html/"
#     # timepath = "/home/brojokm/Downloads/video/time/"

#     # print("getting time")
#     # for l in ll:
#     #     get_time(l[1], l[0], filepath, timepath)

# if __name__ == "__main__":
#     sys.exit(main())






# new_environment = discovery.create_environment(name="new env", description="bogus env")
# print(new_environment)

# if (discovery.get_environment(environment_id=new_environment['environment_id'])['status'] == 'active'):
#    writable_environment_id = new_environment['environment_id']
#    new_collection = discovery.create_collection(environment_id=writable_environment_id,
#                                                name='Example Collection',
#                                                description="just a test")

#    print(new_collection)
    #print(discovery.get_collections(environment_id=writable_environment_id))
    #res = discovery.delete_collection(environment_id='10b733d0-1232-4924-a670-e6ffaed2e641',
    #                                  collection_id=new_collection['collection_id'])
#    print(res)

# collections = discovery.list_collections(environment_id=writable_environment_id)
# print(collections)

#with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
#    print(discovery.test_document(environment_id=writable_environment_id, fileinfo=fileinfo))


# In[25]:

# with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
#     res = discovery.add_document(environment_id=writable_environment_id,
#                                 collection_id=collections['collections'][0]['collection_id'],
#                                 fileinfo=fileinfo)
#    print(res)


#res = discovery.get_collection(environment_id=writable_environment_id,
#                               collection_id=collections['collections'][0]['collection_id'])
#print(res['document_counts'])


#res = discovery.delete_environment(environment_id=writable_environment_id)
#print(res)
