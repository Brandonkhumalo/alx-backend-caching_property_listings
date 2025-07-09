from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all())  # Queryset evaluated to list for caching
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour (3600 seconds)
    return properties

def get_redis_cache_metrics():
    try:
        redis_conn = get_redis_connection("default")  # use your default cache alias
        info = redis_conn.info()

        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total = hits + misses

        hit_ratio = (hits / total) if total > 0 else 0.0

        metrics = {
            'keyspace_hits': hits,
            'keyspace_misses': misses,
            'hit_ratio': hit_ratio,
        }

        logger.info(f"Redis Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio:.2%}")

        return metrics

    except Exception as e:
        logger.error(f"Failed to get Redis cache metrics: {e}")
        return {
            'keyspace_hits': 0,
            'keyspace_misses': 0,
            'hit_ratio': 0.0,
        }