# coding: utf-8
import json, sys, os, watson_developer_cloud
from time import clock
from time import time as tim
def query(discovery, environment_id, collection_id, q):
    ll=[]
    try:
        ## query_options = {'query': 'best', 'highlight':'true','passages':'false', 'return':'title,url','count':'2'}
        query_options = {'query': q, 'passages':'true'}
        results = discovery.query(environment_id, collection_id, query_options)
        # print(json.dumps(results, indent=2))
        result_count = results['matching_results']
        print("result_count = " + str(result_count))
        
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
                        print("text len = " + str(len(text)))
                        l.append(offset)
                        l.append(file_name)
                        l.append(text)### added on 15th april
                        break
                if len(l)==3:##==2  changed on 15th april
                    ll.append(l)
        print("ll.size() = " + str(len(ll)))
        return ll
    except:
    	print("Error in Watson")
        return ll
    

    # path = "/home/brojokm/Downloads/video/html/" + file_name    
    # file_name = file_name[:-10] + ".webm"
    # print(file_name)

def get_time(filename, offset, filepath, timepath):
    try:
        file = filepath + filename + "_punc.html"
        time = timepath + filename + "_time.txt"
        sentence_offset = 1
        text = ""
        # with open(file, 'r') as file:
        #     for line in file:
        #         text = text + line
        #     file.close()

        # for i in range(offset):
        #     if text[i]==' ':
        #         sentence_offset += 1
        
        ########## added on 13th May 
        with open(file, 'r') as f:
            text1 = f.read()
            text1 = text1[14:-16]
        text = text1.split('. ')
        text = text[:-1]
        lines = len(text)
        print("lines=" + str(lines))
        sentence_offsets = []
        sentence_offsets.append(0)
        for i in range(1, lines):
            sentence_offsets.append(sentence_offsets[i-1] + len(text[i-1].split(' ')))
        sentence_number = 0
        for i in range(offset):
            if text1[i] == '.':
                sentence_number += 1
        print(sentence_number)
        sentence_offset = sentence_offsets[sentence_number]

        sresponse = text[sentence_number] + ". "
        try:              
            sresponse += text[sentence_number + 1] + ". " + text[sentence_number + 2] + ". " + text[sentence_number + 3] + ". "
        except:
            try:
                sresponse += text[sentence_number + 1] + ". " + text[sentence_number + 2] + ". "
            except:
                try:
                    sresponse += text[sentence_number + 1] + ". "
                except:
                    print("This is the last sentence")
        ###########
        print("sentence_offset = " + str(sentence_offset))
        ans=0
        word_count=0
        with open(time,'r') as file:
            for line in file:
                word_count +=1
                if word_count == sentence_offset :
                    ans = line
                    break
        print("time= " + str(ans))
        return ans, sresponse
    except:
        return 0 , ""




def upload(discovery, environment_id,collection_id):
    for file in os.listdir("/home/brojo/Flask/flask/localizer/html/"):
        with open(os.path.join(os.getcwd(),'/home/brojo/Flask/flask/localizer/html/', file)) as fileinfo:
           res = discovery.add_document(environment_id=environment_id, collection_id=collection_id, file_info=fileinfo)
           print(res)

def create_delete(discovery, environment_id):
    # res = discovery.delete_collection(environment_id=environment_id, collection_id=collection_id)
    collection = discovery.create_collection(environment_id=environment_id, name='Thesis', description="Thesis. Created on 10th Feb")



def query_aug(q):
    q = q.rstrip()
    ql = q.lower()
    ql = ql.split()

    if "running" in ql and "time" in ql:
        q = q + " complexity"

    if "complexity" in ql:
        q = q + " running time"

    if "bfs" in ql:
        q = q + " breadth first search"
    if "breadth" in ql and "first" in ql and "search" in ql:
        q = q + " bfs"    

    if "dfs" in ql:
        q = q + " depth first search"
    if "depth" in ql and "first" in ql and "search" in ql:
        q = q + " dfs"

    if "mts" in ql:
        q = q + " minimum spanning tree"
    if "minimum" in ql and "spanning" in ql and "tree" in ql:
        q = q + " mts"

    if "dag" in ql:
        q = q + " directed acyclic graph"
    if "directed" in ql and "acyclic" in ql and "graph" in ql:
        q = q + " dag"

    if "fifo" in ql:
        q = q + " first in first out"

    if "lifo" in ql:
        q = q + " last in first out"

    return q
    

def localizer(q): ## 2016-11-07    
# def main():
    llst =[]
    try:
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
        # collection_id = '5d59fead-1f8f-46bd-8ee5-c6418bb961e5' ##iitd
        collection_id = 'a65e74f6-dd7a-4684-a2dc-7019722c90b8' ##mit

        q = query_aug(q)
        ll = query(discovery, environment_id, collection_id, q)

        filepath = "/home/brojo/Flask/flask/localizer/html/"
        timepath = "/home/brojo/Flask/flask/localizer/time/"

        print("getting time")
        

        for l in ll:
            lst = []
            # print("---------------")
            # print(l[0])
            # print(l[1])
            print("---------------------------------")
            time, text2 = get_time(l[1], l[0], filepath, timepath)
            lst.append(l[1]) ##filename
            lst.append(time)
            lst.append(text2) ###added on 15th april--text
            llst.append(lst)

        end_time = tim()
        executeion_time = end_time - start_time
        print("Total time taken ") + str(executeion_time) +" seconds"
        print("--------------------------------------------------------------------------------------------------------")
        return llst
    except:
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
