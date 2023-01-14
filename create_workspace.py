import httpx
import argparse
import json

parser  = argparse.ArgumentParser(description='Test Nextflow Tower Label limit (default 100)')
# parser.add_argument("--action", help="Specify `create` or `delete`")
parser.add_argument("--token", help="Tower PAT token")
parser.add_argument("--wsname", help="Name of workspace")
parser.add_argument("--useremail", help="Email of user to add")

# tower_token = "YOUR_TOWER_TOKEN"
tower_base_url = "dc.seqera.grahamwright.net"
tower_org_id = "182463563746108"



# JSON 

def create_org_data(wsname: str, useremail: str):
    '''Create the payload data to create a workspace.'''
    create_org_data = {
        "workspace": {
            "name": wsname,
            "fullName": f"Workspace for {useremail}.",
            "visibility": "PRIVATE",
            "description": None
        }
    }
    return create_org_data


if __name__ == '__main__':

    '''
    Fill this out later with usage details.
    '''

    args = parser.parse_args()

    headers={
        "Authorization": f"Bearer {args.token}",
        "Accept_Version": "1.0",
        "Content_Type": "application/json"
    }

    # Add User to Org
    # url = f"https://{tower_base_url}/api/orgs/{tower_org_id}/members/add"
    # payload = { "user": args.useremail }
    # resp = httpx.put(url=url, json=payload, headers=headers)
    # print(resp)

    # Create Workspace
    # url = f"https://{tower_base_url}/api/orgs/{tower_org_id}/workspaces"
    # payload = create_org_data(wsname=args.wsname, useremail=args.useremail)
    # resp = httpx.post(url=url, json=payload, headers=headers)
    # print(resp.content)
    # # Response comes back as b'{json}'. Convert to json to grab keys.
    # resp_json = json.loads(resp.content.decode('utf-8'))
    # workspace_id = resp_json['workspace']['id']
    # print(workspace_id)

    # Add user to workspace
    workspace_id="248571532740296"
    # url = f"https://{tower_base_url}/api/orgs/{tower_org_id}/workspaces/{workspace_id}/participants/add"
    # payload = { "userNameOrEmail": args.useremail }
    # resp = httpx.put(url=url, json=payload, headers=headers)
    # print(resp.content)
    # # Response comes back as b'{json}'. Convert to json to grab keys.
    # resp_json = json.loads(resp.content.decode('utf-8'))
    # participant_id = resp_json['participant']['participantId']
    # print(participant_id)

    # Modify participant role
    participant_id="251006506325678"
    # url = f"https://{tower_base_url}/api/orgs/{tower_org_id}/workspaces/{workspace_id}/participants/{participant_id}/role"
    # payload = { "role": "owner" }
    # resp = httpx.put(url=url, json=payload, headers=headers)
    # print(resp.content)
    # Response comes back as b'{json}'. Convert to json to grab keys.
    # resp_json = json.loads(resp.content.decode('utf-8'))
    # participant_id = resp_json['participantId']['id']
    # print(participant_id)