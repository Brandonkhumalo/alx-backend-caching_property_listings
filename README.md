# alx-backend-caching_property_listings

## Overview

This Django project implements a property listing app with PostgreSQL and Redis configured via Docker. It demonstrates caching strategies including view-level caching, low-level caching with Redis, cache invalidation using Django signals, and Redis cache metrics analysis.

---

## Setup

### Requirements

- Docker & Docker Compose
- Python 3.8+
- `pip` and virtual environment tools

### Install Python Dependencies

```bash
pip install django psycopg2-binary django-redis graphene graphene-django


# Features

1. **Property Model**  
- title (CharField)  
- description (TextField)  
- price (DecimalField)  
- location (CharField)  
- created_at (DateTimeField)  

2. **Property List View with Caching**  
- View cached for 15 minutes using Django's `@cache_page` decorator.  
- Endpoint: `/properties/`  
- Returns JSON list of properties.  

3. **Low-Level Queryset Caching**  
- Property queryset cached in Redis for 1 hour using Django’s low-level cache API.  
- Cache key: `all_properties`  
- Cache invalidated on create/update/delete using Django signals.  

4. **Cache Invalidation**  
- Implemented via `post_save` and `post_delete` signals on `Property` model.  
- Clears the Redis cache key `all_properties` on changes.  

5. **Redis Cache Metrics Analysis**  
- Function `get_redis_cache_metrics()` in `properties/utils.py` retrieves:  
  - `keyspace_hits`  
  - `keyspace_misses`  
  - Cache hit ratio  
- Logs metrics for monitoring.  
