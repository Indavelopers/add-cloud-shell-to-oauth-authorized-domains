#!/usr/bin/env python3

from google.cloud import shell_v1


def sample_get_environment():
    # Create a client
    client = shell_v1.CloudShellServiceClient()

    # Initialize request argument(s)
    request = shell_v1.GetEnvironmentRequest(
        name="name_value",
    )

    # Make the request
    response = client.get_environment(request=request)

    # Handle the response
    print(response)


if __name__ == '__main__':
    sample_get_environment()
