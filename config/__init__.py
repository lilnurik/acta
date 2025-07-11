import os

if os.environ.get('RUN_MAIN') == 'true':  # Чтобы не дублировалось при autoreload
    from .read import show_docs_urls
    show_docs_urls()