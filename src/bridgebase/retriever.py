
from .downloader import VugraphDownloader
from .localcache import VugraphLocalCache
from vugraph import Vugraph


class VugraphRetriever(object):
    @staticmethod
    def get(vugraph_id):
        # Fetch from local cache first
        vugraph_data = VugraphLocalCache.get(vugraph_id)
        if vugraph_data is not None:
            return Vugraph(vugraph_data)

        # Attempt to download
        vugraph_data = VugraphDownloader.get(vugraph_id)
        if vugraph_data is not None:
            vugraph = Vugraph(vugraph_data)
            # Save in local cache
            VugraphLocalCache.save(vugraph_id, vugraph_data)
            return vugraph

        # Failed to find vugraph
        return None
