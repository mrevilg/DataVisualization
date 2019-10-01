import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries of North America'
wm.add('North America', {'ca' : 3412600, 'us':309349000, 'mx':113423000})

wm.render_to_file('na_populations.svg')