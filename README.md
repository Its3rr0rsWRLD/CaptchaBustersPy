# CaptchaBusters Python Package

This Python package provides a convenient way to interact with the CaptchaBusters API for solving captcha types.

## Installation

To use this package, install it via pip:

```bash
pip install captchabusters
```

## Usage

```python
from captchabusters import CaptchaBusters

# Initialize CaptchaBusters client with your API key
client = CaptchaBusters(api_key='YOUR_API_KEY')

# Create a task
task = {
    'type': 'FunCaptchaTask',
    'websiteURL': 'https://www.roblox.com',
    'websitePublicKey': 'A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F',
    'websiteSubdomain': 'roblox-api.arkoselabs.com',
    'proxy': 'username:password@ip:port',
    'data': '{"blob": "data_exchange_blob"}'
}
task_response = client.create_task(task)
print('Task created:', task_response)

# Poll for task result
while True:
    task_result = client.get_task_result(task_response['taskId'])
    print('Task result:', task_result)
    if task_result.get('solution'):
        solved_token = task_result['solution']['data']
        print('Solved token:', solved_token)
        break

# Get account balance
balance = client.get_balance()
print('Account balance:', balance)
```

Replace `'YOUR_API_KEY'`, `'username:password@ip:port'`, and other placeholders with your actual credentials and configurations.

## API

### `create_task(task)`

Creates a task for solving the selected captcha type.

- `task`: Task dictionary containing details of the captcha to solve.

### `get_task_result(task_id)`

Retrieves the result of a task.

- `task_id`: ID of the task to retrieve the result for.

### `get_balance()`

Retrieves the account balance using the provided account key.