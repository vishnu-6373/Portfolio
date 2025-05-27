import os
from portfolio.wsgi import application
import json

def handler(event, context):
    """Netlify Function handler that wraps Django WSGI app"""
    
    # Get HTTP method and path
    method = event.get('httpMethod', 'GET')
    path = event.get('path', '/')
    
    # Prepare the Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    
    # Prepare headers
    headers = event.get('headers', {})
    headers['HTTP_HOST'] = headers.get('host', '')
    headers['SERVER_NAME'] = headers['HTTP_HOST']
    headers['SERVER_PORT'] = '443'
    headers['CONTENT_LENGTH'] = str(len(event.get('body', '') or ''))
    headers['CONTENT_TYPE'] = headers.get('content-type', '')
    headers['REQUEST_METHOD'] = method
    headers['PATH_INFO'] = path
    headers['QUERY_STRING'] = event.get('queryStringParameters', {}) or ''
    headers['X-Forwarded-For'] = headers.get('client-ip', '')
    headers['X-Forwarded-Proto'] = headers.get('x-forwarded-proto', '')
    
    # Call the Django application
    response = application(headers, lambda x, y: None)
    
    # Get the status code and response body
    status_code = int(response.status_code)
    response_body = b''.join(response)
    
    # Prepare response headers
    response_headers = {}
    for key, value in response.items():
        response_headers[key] = value
    
    return {
        'statusCode': status_code,
        'headers': response_headers,
        'body': response_body.decode('utf-8')
    }
