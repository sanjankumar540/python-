"""
#dumps and loads
import json
python_data = {'name':'pranav','course':'pfs','age':21,'gender':'male'}
print(type(python_data))
json_data = json.dumps(python_data)
python_data1 = json.loads(json_data)
print(python_data)
print(json_data)
print(type(json_data))
print(python_data1)
print(type(python_data1))  """



#PICKLING
import pickle
details = {'e_name' : 'manoj','dept':'trainer'}
print(details)
print(type(details))
print("---------------------")

pickle_data = pickle.dumps(details)
print(type(pickle_data))
print(pickle_data)
python_data = pickle.loads(pickle_data)
print(python_data)
