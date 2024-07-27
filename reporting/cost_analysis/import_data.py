from google.cloud import billing_v1
import requests

client = billing_v1.CloudBillingClient()
project_id = 'your_project_id'
billing_account_name = 'billingAccounts/your_billing_account_id'

def get_google_cloud_costs():
    project_name = f'projects/{project_id}'
    response = client.get_project_billing_info(name=project_name)
    return response.billing_account_name

def get_cloudflare_costs():
    url = 'https://api.cloudflare.com/client/v4/billing/profile'
    headers = {
        'Authorization': 'Bearer your_api_key',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_clickup_costs():
    url = 'https://api.clickup.com/api/v2/team/team_id/billing'
    headers = {
        'Authorization': 'Bearer your_api_key'
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_zapier_costs():
    url = 'https://api.zapier.com/v1/billing/usage'
    headers = {
        'Authorization': 'Bearer your_api_key'
    }
    response = requests.get(url, headers=headers)
    return response.json()

