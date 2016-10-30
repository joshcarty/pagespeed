class Response(object):
    """ Base Response Object

    Attributes:
        self.json (dict): JSON representation of response
        self._request (str): URL of
        self._response (`requests.models.Response` object): Response object from requests module
    """
    def __init__(self, response):
        response.raise_for_status()

        self._response = response
        self._request = response.url
        self.json = response.json()

    def __repr__(self):
        return '<Response>'


class PageSpeedResponse(Response):
    """ PageSpeed Response Object

    Attributes:
        self.url (str):
        self.title (str):
        self.locale (str):
        self.version (str):
        self.speed (int):
        self.statistics (`Statistics` object):
    """

    @property
    def url(self):
        return self.json.get('id')

    @property
    def title(self):
        return self.json.get('title')

    @property
    def locale(self):
        return self.json.get('formattedResults').get('locale')

    @property
    def version(self):
        major = self.json.get('version').get('major')
        minor = self.json.get('version').get('minor')
        return '{0}.{1}'.format(major, minor)

    @property
    def speed(self):
        return self.json.get('ruleGroups').get('SPEED').get('score')

    @property
    def statistics(self):
        page_stats = self.json.get('pageStats')
        return Statistics(page_stats)

    def to_csv(self, path):
        pass

    def pretty_print(self):
        pass

    def __repr__(self):
        return '<Response(url={0})>'.format(self.url)


class DesktopPageSpeed(PageSpeedResponse):

    def __repr__(self):
        return '<DesktopPageSpeed(url={0})>'.format(self.url)


class MobilePageSpeed(PageSpeedResponse):

    @property
    def usability(self):
        return self.json.get('ruleGroups').get('USABILITY').get('score')

    def __repr__(self):
        return '<MobilePageSpeed(url={0})>'.format(self.url)


class Statistics(object):
    def __init__(self, page_stats):
        self.page_stats = page_stats

    @property
    def css_response_bytes(self):
        return self.page_stats.get('cssResponseBytes')

    @property
    def html_response_bytes(self):
        return self.page_stats.get('htmlResponseBytes')

    @property
    def image_response_bytes(self):
        return self.page_stats.get('imageResponseBytes')

    @property
    def javascript_response_bytes(self):
        return self.page_stats.get('javascriptResponseBytes')

    @property
    def number_css_resources(self):
        return self.page_stats.get('numberCssResources')

    @property
    def number_hosts(self):
        return self.page_stats.get('numberHosts')

    @property
    def number_js_resources(self):
        return self.page_stats.get('numberJsResources')

    @property
    def number_resources(self):
        return self.page_stats.get('numberResources')

    @property
    def number_static_resources(self):
        return self.page_stats.get('numberStaticResources')

    @property
    def other_response_bytes(self):
        return self.page_stats.get('otherResponseBytes')

    @property
    def text_response_bytes(self):
        return self.page_stats.get('textResponseBytes')

    @property
    def total_request_bytes(self):
        return self.page_stats.get('totalRequestBytes')