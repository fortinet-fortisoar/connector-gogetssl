"""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('gogetssl')


class GoGetSSL(object):

    def __init__(self, config):
        self.server_url = config.get('server_url', '').strip('/')
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl', False)
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def make_api_call(self, endpoint, method='POST', payload=None, params={}):
        if self.api_key:
            params.update({'auth_key': self.api_key})
        headers = self.headers if method.lower() == 'post' else {}
        service_endpoint = self.server_url + endpoint
        try:
            response = requests.request(method, service_endpoint, data=payload, headers=headers, params=params,
                                        verify=self.verify_ssl)
            logger.debug('API Service Endpoint: {0}'.format(service_endpoint))
            logger.debug('API Response Status code: {0}'.format(response.status_code))
            logger.debug('API Response: {0}'.format(response.text))
            if response.ok:
                return response.json()
            else:
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response.text})
        except requests.exceptions.SSLError as err:
            logger.error(err)
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout as err:
            logger.error(err)
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout as err:
            logger.error(err)
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError as err:
            logger.error(err)
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))


def get_domain_alternative(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/domain/alternative/', payload=payload)


def get_domain_emails(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/domain/emails', payload=payload)


def get_domain_emails_for_geo_trust(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/domain/emails/geotrust/', payload=payload)


def get_domain_from_whois(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/domain_get_from_whois/', payload=payload)


def get_all_products(config, params):
    client = GoGetSSL(config)
    return client.make_api_call('/api/products', method='GET')


def get_product_details(config, params):
    client = GoGetSSL(config)
    product_id = params.pop('product_id')
    endpoint = f'/api/products/details/{product_id}'
    return client.make_api_call(endpoint, method='GET')


def get_orders_metadata(config, params):
    client = GoGetSSL(config)
    return client.make_api_call('/api/orders', method='GET')


def get_orders_details(config, params):
    client = GoGetSSL(config)
    order_id = params.pop('order_id', '')
    endpoint = f'/api/orders/status/{order_id}'
    return client.make_api_call(endpoint, method='GET')


def get_all_orders_status(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/orders/statuses', payload=payload)


def get_total_order_count(config, params):
    client = GoGetSSL(config)
    return client.make_api_call('/api/account/total_orders', method='GET')


def generate_csr(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/csr/generate', payload=payload)


def validate_csr(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/csr/validate', payload=payload)


def decode_csr(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/tools/csr/decode', payload=payload)


def add_ssl_order(config, params):
    client = GoGetSSL(config)
    additional_field = params.pop('additional_field', '')
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = {**params, **additional_field} if additional_field else params
    return client.make_api_call('/api/orders/add_ssl_order', payload=payload)


def reissue_ssl_order(config, params):
    client = GoGetSSL(config)
    order_id = params.pop('order_id')
    endpoint = f'/api/orders/ssl/reissue/{order_id}'
    additional_field = params.pop('additional_field', '')
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = {**params, **additional_field} if additional_field else params
    return client.make_api_call(endpoint, payload=payload)


def add_ssl_renew_order(config, params):
    client = GoGetSSL(config)
    additional_field = params.pop('additional_field', '')
    params = {k: v for k, v in params.items() if v is not None and v != ''}
    payload = {**params, **additional_field} if additional_field else params
    return client.make_api_call('/api/orders/add_ssl_renew_order', payload=payload)


def add_ssl_san_order(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/orders/add_ssl_san_order', payload=payload)


def cancel_order(config, params):
    client = GoGetSSL(config)
    payload = {k: v for k, v in params.items() if v is not None and v != ''}
    return client.make_api_call('/api/orders/cancel_ssl_order', payload=payload)


def _check_health(config):
    return get_total_order_count(config, {})


operations = {
    'get_domain_alternative': get_domain_alternative,
    'get_domain_emails': get_domain_emails,
    'get_domain_emails_for_geo_trust': get_domain_emails_for_geo_trust,
    'get_domain_from_whois': get_domain_from_whois,
    'get_all_products': get_all_products,
    'get_product_details': get_product_details,
    'get_orders_metadata': get_orders_metadata,
    'get_orders_details': get_orders_details,
    'get_all_orders_status': get_all_orders_status,
    'get_total_order_count': get_total_order_count,
    'generate_csr': generate_csr,
    'validate_csr': validate_csr,
    'decode_csr': decode_csr,
    'add_ssl_order': add_ssl_order,
    'reissue_ssl_order': reissue_ssl_order,
    'add_ssl_renew_order': add_ssl_renew_order,
    'add_ssl_san_order': add_ssl_san_order,
    'cancel_order': cancel_order
}
