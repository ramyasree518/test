from keystoneauth1 import session 
from keystoneclient.v3 import client as kc 
from keystoneauth1.identity import v3 
from osc_lib import utils

config = None 

def openstack_access_token(): 
 auth = v3.Password(user_domain_name="admin_domain", username="admin", password="c0ntrail123", auth_url="https://keystone.tcsecp.com:5000/v3", project_name="admin",project_domain_name="admin_name",project_id="86fcc0b3839b45029dd325641ddc2a09")
 kwargs = utils.build_kwargs_dict('interface', 'public')
 sess = session.Session(auth=auth,verify="/home/ubuntu/cacert.pem") 
 
 keystone = kc.Client(session=sess,**kwargs) 
 users_data = keystone.users.list()
 projects_list = keystone.projects.list()
 role_list =  keystone.role_assignments.list()
 user_list= []
 project_list= []

 for pro in projects_list:
     if pro.domain_id == '1e59a4057fb24003a902bc4df6247d3c':
         proj= []
         proj.append(pro.id)
         proj.append(pro.name)
         project_list.append(proj)
   #  print("id:" +  pro.id + "   name:" + pro.name)

 for user in users_data: 
     if user.domain_id == '1e59a4057fb24003a902bc4df6247d3c':
         list=[]
         list.append(user.id)
         list.append(user.name)
         user_list.append(list)
    #print("id:" +user.id + "   name:" + user.name) 
 user_project=[]
 for role in role_list:
     list1=[]
     list2=[]
     if 'project' in role.scope :
        for pro_id in project_list:
            
            if role.scope['project']['id'] == pro_id[0]:
                #list1.append(pro_id[1])
                try:
                    for user_id in user_list:
                        if role.user['id'] == user_id[0]:
                            list1.append(user_id[1])
                            user_project.append(list1)
                
                except AttributeError:
                    list1.append('None')
                    #user_project.append(list1)
                list1.append(pro_id[1])
 main_list= []
 for i in user_project:
     if i not in main_list:
         main_list.append(i)

 for i in main_list:
     print(i[0]+","+i[1])
openstack_access_token()
