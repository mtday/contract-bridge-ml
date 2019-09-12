
import os


class VugraphLocalCache(object):
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

