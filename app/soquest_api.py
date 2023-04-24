#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
from flask import current_app


def send_request(method, api_url, params=None, data=None):
    api_key = current_app.config['SOQUEST_APIKEY']
    api_url = '{api_url}?api-key={key}'.format(api_url=api_url, key=api_key)

    r = None
    if method == 'POST':
        r = requests.post(api_url, data=data, timeout=60).json()
    elif method == 'GET':
        r = requests.get(api_url, params=params, timeout=60).json()
    return r

def get_candidates(campaign_code):
    api_url = 'https://api.sograph.xyz/api/campaign/{campaign_code}/candidates'.format(
            campaign_code=campaign_code)
    try:
        r = send_request('GET', api_url)
        current_app.logger.debug(r)
    except:
        current_app.logger.exception('get candidates fail')
        return None

    return r['data']

def get_winners(campaign_code, prize_code):
    api_url = 'https://api.sograph.xyz/api/campaign/{campaign_code}/prize/{prize_code}/winners'.format(
            campaign_code=campaign_code, prize_code=prize_code)
    try:
        r = send_request('GET', api_url)
        current_app.logger.debug(r)
    except:
        current_app.logger.exception('get winners fail')
        return None

    return r['data']

