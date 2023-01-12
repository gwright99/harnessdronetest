import httpx
import argparse

parser  = argparse.ArgumentParser(description='Test Nextflow Tower Label limit (default 100)')
parser.add_argument("--action", help="Specify `create` or `delete`")
parser.add_argument("--token", help="Tower PAT token")

# tower_token = "YOUR_TOWER_TOKEN"
tower_base_url = "dc.seqera.grahamwright.net"
tower_workspace_id = "66352837741840"

# Some comment

# JSON Payload to create a label.
create_label_data = {
  "name": "",
  # "value": "test",
  "resource": False
}


if __name__ == '__main__':

    '''
    Testing if a Tower Instance's workspace label limit has increased:
        - By default, each workspace is allowed to have 100 labels.
        - This value can be increased via the tower.yml value.
        - As of Jan 6/23, the tw cli does not offer a method to interact with labels.
    
    USAGE:
        1. Create a throwaway workspace to use for testing purposes.
        2. Get the workspaceId via the Tower UI: (Workspaces tab of the Org, use the value tied to 'Id')
        3. Update the tower variables at the top of this script.
        4. Run `python3 test_tower_label_limit.py --action create` 
            - If you do not see an error, your custom configuration should be assumed to be in effect.
            - If you see an error, your custom configuration is not in effect.
        5. Run `python3 test_tower_label_limits.py --action delete` to destroy any labels in the workspace.

    CONSTRAINTS:
        - I used a hardcoded `max=500` config value when retrieving workspace labels. If you decide to conduct testing which involves
          more than 500 labels, you will need to modify this value too.
    '''

    args = parser.parse_args()

    headers={
        "Authorization": f"Bearer {args.token}",
        "Accept_Version": "1.0",
        "Content_Type": "application/json"
    }

    if args.action == 'create':
        # Set the Create Label API target
        url = f"https://{tower_base_url}/api/labels?workspaceId={tower_workspace_id}"

        # Create labels
        for i in range (105):
            create_label_data['name'] = f"test-{i}"
            resp = httpx.post(url=url, json=create_label_data, headers=headers)
            resp = resp.json()
            print(resp)

            if 'message' in resp.keys():
                if resp['message'] == 'Limit of 100 labels reached':
                    print('[ERROR] - Your custom >100 workspace label limit is not in effect.')
                    exit()


    if args.action == 'delete':
        # Set the Get Label API target
        url = f"https://{tower_base_url}/api/labels?workspaceId={tower_workspace_id}&max=500&type=labels"

        resp = httpx.get(url=url, headers=headers)
        resp = resp.json()
        print(resp)\

        for label in resp['labels']:
            label_id = label['id']
            url = f"https://{tower_base_url}/api/labels/{label_id}?workspaceId={tower_workspace_id}"
            resp = httpx.delete(url=url, headers=headers)
            # resp = resp.json()  # Return payload is No Content
            print(f"Deleting label {label_id} - {resp}")
