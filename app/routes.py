def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('mds_root', '/mds/')
    config.add_route('mds', '/mds/{number}')
    config.add_route('mds_update', '/mds/{number}/{name}')
