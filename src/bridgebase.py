
from vugraph import Vugraph
import os
import urllib.request


class BridgeBaseVugraphLocalCache(object):
    @staticmethod
    def get(vugraph_id):
        vugraph_path = os.path.join('/opt/vugraphs', vugraph_id + '.lin')
        if not os.access(vugraph_path, os.F_OK):
            return None
        with open(vugraph_path, 'r') as vugraph_file:
            return vugraph_file.read()

    @staticmethod
    def save(vugraph_id, vugraph_data):
        vugraph_dir = '/opt/vugraphs'
        if not os.access(vugraph_dir, os.F_OK):
            os.makedirs(vugraph_dir)
        vugraph_path = os.path.join(vugraph_dir, vugraph_id + '.lin')
        if os.access(vugraph_path, os.F_OK):
            os.remove(vugraph_path)
        with open(vugraph_path, 'wb') as vugraph_file:
            vugraph_file.write(vugraph_data.encode('utf-8'))

    @staticmethod
    def delete(vugraph_id):
        vugraph_path = '/opt/vugraphs/{}.lin'.format(vugraph_id)
        if os.access(vugraph_path, os.F_OK):
            os.remove(vugraph_path)


class BridgeBaseVugraphDownloader(object):
    @staticmethod
    def get(vugraph_id):
        conn = urllib.request.urlopen('https://www.bridgebase.com/tools/vugraph_linfetch.php?id={}'.format(vugraph_id))
        vugraph_data = conn.read()
        response_code = conn.getcode()
        conn.close()
        if response_code != 200:
            return None
        return vugraph_data.decode('utf-8')


class BridgeBaseVugraphRetriever(object):
    @staticmethod
    def get(vugraph_id):
        # Fetch from local cache first
        vugraph_data = BridgeBaseVugraphLocalCache.get(vugraph_id)
        if vugraph_data is not None:
            return Vugraph(vugraph_data)

        # Attempt to download
        vugraph_data = BridgeBaseVugraphDownloader.get(vugraph_id)
        if vugraph_data is not None:
            vugraph = Vugraph(vugraph_data)
            # Save in local cache
            BridgeBaseVugraphLocalCache.save(vugraph_id, vugraph_data)
            return vugraph

        # Failed to find vugraph
        return None
