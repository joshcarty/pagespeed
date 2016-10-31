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

    def analyse(self, url, **kwargs):
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

        kwargs.setdefault('filter_third_party_resources', False)
        kwargs.setdefault('screenshot', False)
        kwargs.setdefault('strategy', 'desktop')

        params = kwargs.copy()
        params.update({'url': url})

        response = requests.get(self.endpoint, params=params)

        if kwargs.get('strategy') == 'desktop':
            return DesktopPageSpeed(response)
        elif kwargs.get('strategy') == 'mobile':
            return MobilePageSpeed(response)
        else:
            raise ValueError('invalid strategy: {0}'.format(kwargs.get('strategy')))