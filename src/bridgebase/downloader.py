
import urllib.request


class VugraphDownloader(object):
    @staticmethod
    def get(vugraph_id):
        conn = urllib.request.urlopen('https://www.bridgebase.com/tools/vugraph_linfetch.php?id={}'.format(vugraph_id))
        vugraph_data = conn.read()
        response_code = conn.getcode()
        conn.close()
        if response_code != 200:
            return None
        return vugraph_data.decode('utf-8')

