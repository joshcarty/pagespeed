import requests
from pagespeed.responses import DesktopPageSpeed, MobilePageSpeed


class PageSpeed(object):
    """Google PageSpeed analysis client

    Attributes:
        api_key (str): Optional API key for client account.
        endpoint (str): Endpoint for HTTP request
    """

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.endpoint = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed'

    def analyse(self, url, filter_third_party_resources=False, screenshot=False,
                strategy='desktop'):
        """Run PageSpeed test

        Args:
            url (str): The URL to fetch and analyse.
            filter_third_party_resources (bool, optional): Indicates if third party
                resources should be filtered out before PageSpeed analysis. (Default: false)
            locale (str, optional): The locale used to localize formatted results.
            rule (list, optional): A PageSpeed rule to run; if none are given, all rules are run
            screenshot (bool, optional): Indicates if binary data containing a screenshot should
                be included (Default: false)
            strategy (str, optional): The analysis strategy to use. Acceptable values: 'desktop', 'mobile'

        """

        params = {
            'filter_third_party_resources': filter_third_party_resources,
            'screenshot': screenshot,
            'strategy': strategy,
            'url': url
        }

        response = requests.get(self.endpoint, params=params)

        if strategy == 'desktop':
            return DesktopPageSpeed(response)
        elif strategy == 'mobile':
            return MobilePageSpeed(response)
        else:
            raise ValueError('invalid strategy: {0}'.format(strategy))