    
from keystoneauth1 import session
from keystoneclient.v3 import client as kc
from keystoneauth1.identity import v3
from osc_lib import utils



# keystone authentication
def keystone_authentication():
    # authentication parameters
    kwargs = utils.build_kwargs_dict('interface', 'public')
    auth_url = "https://keystone.tcsecp.com:5000/v3"
    username = "admin"
    password = "c0ntrail123"
    project_id = "86fcc0b3839b45029dd325641ddc2a09"
    project_domain_id = "admin_domain"
    user_domain_id = "admin_domain"
    cert_path = "/home/ubuntu/cacert.pem"


    # Authenticated and receive a token from Keystone
    auth = v3.Password(auth_url=auth_url, username=username, password=password, project_id=project_id,
                       user_domain_name=user_domain_id, project_domain_name=project_domain_id)
    sess = session.Session(auth=auth, verify=cert_path)
    keystone = kc.Client(session=sess, **kwargs)
    return keystone



# get the project data
def user_project_data():
    user_project_name = ""
    keystone = keystone_authentication()
    users_data = keystone.users.list(domain="7472a5c073a048e8a4f634cb5e250fac")
    user_list= []
#    print(users_data)
    for user in users_data:
        user_list.append(user.id)
#    print(user_list)
    data_list= []
    for user1 in user_list:
        project_data = keystone.projects.list(domain="7472a5c073a048e8a4f634cb5e250fac",user=str(user1))
        for i in project_data:
            l= []
            l.append(user1)
            l.append(i.name)
            data_list.append(l)  
#    print(data_
    user_pro_data= []
    for i in data_list:
        for j in users_data:
            if i[0] == j.id:
                print(j.name,i[1])
 
# get the domain id
user_project_data()
