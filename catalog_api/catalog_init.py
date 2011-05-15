# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import catalog

c = catalog.Catalog('example_songs', type='song')

print 'Initialized Catalog: "%s" with id %s.' % (c.name, c.id)

print 'Items in catalog: %s' % (c.read.total, )
print 'Items in catalog: %s' % (c.read_items().total, )

print 'Catalog profile:'
cp = c.profile
for key, val in cp.iteritems():
    print '    %-15s %s' % (key, val)
