from hdfs import InsecureClient
from hdfs.ext.avro import AvroWriter

#connection to web HDFS
def conn():
    client = InsecureClient('http://test-bigdata.us-central1-a.c.bigdatalearn-274318.internal:9870', user='admin')
    return client

#Make dictionaries out of two lists
def MakeStringDict(keys,vals):
    v_dict = dict(zip(keys, vals))
    return v_dict

#AVRO Schema Fields builder
def FieldsConstructor(header,p_dt_type):
    field_list = [{'name':k,'type':p_dt_type} for k in header]
    return field_list

#Set Schema name based on File name
def schema_set_name(schema,name_val):
    schema.update(name = name_val)
    return schema

#updating schema for AVRO based on headers from csv
def schema_make_fields_from_file_header(client,path,schema):
    x=0
    with client.read(path,encoding='utf-8', delimiter='\n') as reader:
        for i in reader:
            x+=1
            if x == 1:
                line = i.split(',')
                keys = line
                v_field_constructor = FieldsConstructor(keys, 'string')
                schema.update(fields=v_field_constructor)
            break
    return schema

#Conversion function based on input and output files and schema
def file_conversion_to_avro(client,fp_to_write,fp_to_read,schema):
    x=0
    with AvroWriter(client, fp_to_write, schema) as writer:
        with client.read(fp_to_read, encoding='utf-8', delimiter='\n') as reader:
            for i in reader:
                x += 1
                line = i.split(',')
                if len(line) == 1: continue
                if x == 1:
                    keys = line
                    continue
                dict_to_write = MakeStringDict(keys, line)
                print(dict_to_write)
                writer.write(dict_to_write)


#main part
template_schema = {
    "namespace":"BigData101",
    "type": "record"
        }
client = conn()
hdfs_path = '/user/input_files/'

for i in client.list(hdfs_path):
    hdfs_path_to_read = hdfs_path + i
    schema_set_name(template_schema,i.partition('.')[0])
    #building avro schema for current file
    schema_ex = schema_make_fields_from_file_header(client, hdfs_path_to_read, template_schema)
    #conversion
    file_conversion_to_avro(client, hdfs_path_to_read.partition('.')[0]+'.avro', hdfs_path_to_read, schema_ex)



