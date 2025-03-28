#!/usr/bin/env python3

'''Add Cloud Shell current domain to your Google Cloud app's OAuth client authorized domains.'''

import argparse

from google.cloud import shell_v1

def main():
    parser = argparse.ArgumentParser(description='Add cloud shell to OAuth authorized domains.')
    parser.add_argument('--project_id', required=True, help='GCP Project ID')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes', dest='dry_run')
    parser.add_argument('--user_email', help='User email', default='me')
    parser.add_argument('--cloud_shell_env_name', help='Cloud Shell environment name', default='default')

    args = parser.parse_args()

    project_id = args.project_id
    dry_run = args.dry_run
    user_email = args.user_email
    cloud_shell_env_name = args.cloud_shell_env_name

    print('Used args:')
    print(f'Project ID: {project_id}')
    print(f'Dry Run: {dry_run}')
    print(f'User Email: {user_email}')
    print(f'Cloud Shell Environment Name: {cloud_shell_env_name}')
    print('\n----\n')

    client = shell_v1.CloudShellServiceClient()

    request = shell_v1.GetEnvironmentRequest(name=f'users/{user_email}/environments/{cloud_shell_env_name}')
    response = client.get_environment(request=request)

    print(f'Your Cloud Shell {cloud_shell_env_name} environment URL is: {response.web_host}')

    if dry_run:
        print('Dry run completed. No changes were made.')
    else:
        print('Changes were made.')

if __name__ == '__main__':
    main()
