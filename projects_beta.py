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
    projects_list = keystone.projects.list()
    project_list= []

    for pro in projects_list:
        if pro.domain_id == '7472a5c073a048e8a4f634cb5e250fac':
            print(pro.name)
openstack_access_token()
