#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import warnings
warnings.simplefilter("ignore")
import elasticsearch
import elasticsearch.helpers

from elasticsearch import Elasticsearch
es = Elasticsearch(hosts = [
    'http://localhost:9201'
])


# In[83]:




import streamlit as st


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("lit_s.jpeg", width=250 )

with col3:
    st.write(' ')

# =============================================================================
# 
# 
#       enter the query
# 
# 
# =============================================================================


# display the query when the submit button is clicked
# .title() is used to get the input text string


# In[80]:


from datetime import datetime

#2016-10-07T05:54:22Z
def datee(date_time_str):
    return datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%SZ')


# In[ ]:


from fse import Vectors, Average, IndexedList
vecs = Vectors.from_pretrained("glove-wiki-gigaword-300")
model = Average(vecs)


# In[ ]:


def searchElastic(query, pp=400):
    

    query_vector = model.infer([(str(query).split(), 0)])[0]

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, doc['title_vec']) + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }

    response = es.search(
        index="so-vec-ret",
        body={
            "size": pp,
            "query": script_query,
            #"_source": {"includes": ["title", "body"]}
        }
    )

    return response


# In[73]:


# #query= "python program"

# def searchElastic(query, pp=400):
# 	result = es.search(
# 	index = "so_retrieval",
# 	body = {
# 		"query": {
# 			"bool": {

# 				"should": [{
# 						"match_phrase": {
# 							"Title": query
# 						}
# 					},
# 					{
# 						"match_phrase": {
# 							"Tags": query
# 						}
# 					}
# 				]


# 			}

# 		},
# 		"sort": {
#         "_score"  : {
#           "order": "desc"
#         }
#       }
		
		
	
			
# 		},
		
# 		size=pp

# 		)
# 	return result


# In[77]:


name = st.text_input("Enter Your query here", "")
if(st.button('Submit')):
	query = name.title()

	


# In[ ]:


st.markdown("#### Use the below dropdown to select number of results required")

number = st.selectbox("Number of results: ",
                     ['Top 10', 'Top 50', 'Top 100', 'All'])
 
pp = 10
# print the selected hobby
st.write("You wish to see ", number, " results")

if(number == 'Top 10'):
    pp = 10
    
elif(number == 'Top 50'):
    pp = 50
    
elif(number == 'Top 100'):
    pp = 100
    
else:
    pp = 500



# In[81]:


def sortAccordingly(lst, field, pp, score = False):
    lst = [i['_source'] for i in lst]
    if score:
        lst = sorted(lst, key = lambda x: float(x[field]), reverse=True)
    else:
        lst = sorted(lst, key = lambda x: x[field], reverse=True)
    
    lst = list({v['Id']:v for v in lst}.values())[:pp]

    return lst


# In[ ]:


st.markdown("#### Use the below buttons to filter the results (by default-relevent).")

col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    a1 = st.button('Relevent', key='2')

with col2:
    a2 = st.button('Popular', key='3')

with col3:
    a3 = st.button('Newest', key='4')




if(a1):
    query = name.title()
    tmp = searchElastic(query, pp*3)
    st.title(str(float(tmp['took'])/1000) + " second(s)")
    all_data = tmp['hits']['hits']
    all_data = list({v['_source']['Id']:v for v in all_data}.values())[:pp]
    #st.write("[Question](https://stackoverflow.com/questions/27505280)")
    if(len(all_data) != 0):
        for i in range(len(all_data)):
            #st.write(i)
            uri = "https://stackoverflow.com/questions/"+str(all_data[i]['_source']['Id'])
            placeholder = str(all_data[i]['_source']['Title'])
            st.write(str(i+1)+'.'," [%s](%s)"%(placeholder, uri))
               
            #st.write(all_data[i]['_source']['Id'], all_data[i]['_source']['Title'], all_data[i]['_score'])
	

if(a2):
   # all_data = searchElastic(query, pp)
    query = name.title()
    tmp = searchElastic(query, pp*3)
    st.title(str(float(tmp['took'])/1000) + " second(s)")
    all_data = tmp['hits']['hits']

    all_data = sortAccordingly(all_data, 'Score', pp, score=True)
    if(len(all_data) != 0):
        for i in range(len(all_data)):
            uri = "https://stackoverflow.com/questions/"+str(all_data[i]['Id'])
            placeholder = str(all_data[i]['Title'])
            st.write(str(i+1)+'.'," [%s](%s)"%(placeholder, uri))
     
if(a3):
    query = name.title()
    tmp = searchElastic(query, pp*3)
    st.title(str(float(tmp['took'])/1000) + " second(s)")
    all_data = tmp['hits']['hits']

    all_data = sortAccordingly(all_data, 'CreationDate', pp)
    if(len(all_data) != 0):
        for i in range(len(all_data)):
            #st.write(i)
            uri = "https://stackoverflow.com/questions/"+str(all_data[i]['Id'])
            placeholder = str(all_data[i]['Title'])
            st.write(str(i+1)+'.'," [%s](%s)"%(placeholder, uri))

    


# In[ ]:





# In[ ]:





# In[ ]:




