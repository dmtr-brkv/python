import requests

# login = "dmtr.brkv.4@gmail.com"
# password = "екл48сийй"
# company_name = "Поток_100"
# key = "pCvbGF3AfocmkbcHr6N3S12qaAgzdmmVIYAy7pppNkbkrrMEPvy4st46tBTkCn9B"
key = "XDNF8ZJi7QZVvWMW9tDTaB07+D70MoeYWTqeP99wdcKTrLxxgUKPGX7ochHEGcHw"

# body_company = {
#         "login": login,
#         "password": password,
#         "name": company_name
#         }

headers = {"Authorization" : "Bearer {key}",
           "Content-Type": "application/json"}
data = {"title": "Круги на поле"}
data_new = {"deleted": False, "title": "Круги в поле",}

base_url = "https://ru.yougile.com/api-v2"

def test_create_projects():
    create = requests.post(f'{base_url}/projects', headers=headers, data=data)
    list = requests.get(f'{base_url}/projects', headers=headers)
    response = list.json()
    assert response != 0

def test_get_id():
    create = requests.post(f'{base_url}/projects', headers=headers, data=data)
    id_json = create.json()
    new_id = id_json["id"]
    get_id = requests.get(f'{base_url}/projects/{new_id}', headers=headers)
    get_json = get_id.json()
    title = get_json["title"]
    assert title == "Круги на поле"


def test_add_projects():
    list = requests.get(f'{base_url}/projects',headers=headers)
    response = list.json()
    to_be = response["paging"]["count"]
    create = requests.post(f'{base_url}/projects',headers=headers, data=data)
    last_list = requests.get(f'{base_url}/projects', headers=headers)
    response = last_list.json()
    to_end = response["paging"]["count"]
    assert to_end - to_be == 1


def test_change_id():
    create = requests.post(f'{base_url}/projects', headers=headers, data=data)
    create_json = create.json()
    create_id = create_json["id"]
    create_new = requests.post(f'{base_url}/projects/{create_id}',headers=headers, data=data_new)
    get_create = requests.get(f'{base_url}/projects/{create_id}', headers=headers)
    create_json_last = get_create.json()
    title_create = create_json_last["title"]
    assert title_create == "Круги в поле"

# negative

headers_negative = {"Authorization" : "Bearer 123",
           "Content-Type": "application/json"}

def test_crete_negative_key():
    create = requests.post(f'{base_url}/projects', headers=headers_negative, data=data)
    list = requests.get(f'{base_url}/projects', headers=headers_negative)
    assert list.status_code == 401

negative_id = 0000

def test_get_negative_id():
    get_id = requests.get(f'{base_url}/projects/{negative_id}', headers=headers)
    assert get_id.status_code == 404

data_negative = {"deleted": True, "title": "Круги в поле",}

def test_change_negative_id():
    create = requests.post(f'{base_url}/projects', headers=headers, data=data)
    create_json = create.json()
    create_id = create_json["id"]
    create_new = requests.post(f'{base_url}/projects/{create_id}',headers=headers, data=data_negative)
    get_create = requests.get(f'{base_url}/projects/{create_id}', headers=headers)
    create_json_last = get_create.json()
    title_create = create_json_last["title"]
    assert title_create == "Круги в поле"









# def test_get_company_list():
#     resp = requests.post(f'{base_url} /auth/companies',
#                          headers=headers,
#                          json=body_company)
#     response = resp.json()
#     first_company = response["content"][0]
#     company_id = first_company.get("id")
#     assert bool(company_id)
#
# def get_key():
#     resp = requests.post(f'{base_url} /auth/companies',
#                          headers=headers,
#                          json=body_company)
#     company_id = resp.json()["content"][0]["id"]
#     body_key = {
#         "login": login,
#         "password": password,
#         "companyId": company_id
#         }
#     resp_key = requests.post(f'{base_url}/auth/keys", headers=headers,
#                              json=body_key)
#     key = resp_key.json()["key"]
#     return key
#
# def create_project():
#     body_create_project = {
#         "title": "YouGile",
#         "users": user_role
#              }
#     resp = requests.post(f'{base_url}/projects",
#                          headers=headers_for_projects,
#                          json=body_create_project)
#     return resp
