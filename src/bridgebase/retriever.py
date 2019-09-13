
from .downloader import VugraphDownloader
from .localcache import VugraphLocalCache
from vugraph import Vugraph

"""
Retrieves a parsed Vugraph based on id from the local cache (if it exists locally) or by fetching it from the
BridgeBase web site.
"""


class VugraphRetriever(object):
    @staticmethod
    def get(vugraph_id):
        # Fetch from local cache first
        vugraph_data = VugraphLocalCache.get(vugraph_id)
        if vugraph_data is not None:
            return Vugraph.parse(vugraph_data)

        # Attempt to download
        vugraph_data = VugraphDownloader.get(vugraph_id)
        if vugraph_data is not None:
            vugraph = Vugraph.parse(vugraph_data)
            # Save in local cache
            VugraphLocalCache.save(vugraph_id, vugraph_data)
            return vugraph

        # Failed to find vugraph
        return None
