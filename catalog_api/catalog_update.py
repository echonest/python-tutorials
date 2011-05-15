# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import catalog, song
import time

c = catalog.Catalog('example_songs', type='song')

song_artist_pairs = [('Lust For Life', 'Iggy Pop'), ('Under Cover Of Darkness', 'The Strokes'), ('B.O.B.', 'Outkast'), ('Help!', 'The Beatles')]

item_id = 0
items = []

for song_artist in song_artist_pairs:
   items += [{ 'item': 
                { 
                    'item_id': str(item_id),
                    'song_name': song_artist[0],
                    'artist_name': song_artist[1]
                }
            }]
   item_id += 1

ticket = c.update(items)

for i in range(0,12):
    time.sleep(5)
    if c.status(ticket)['ticket_status'] == 'complete':
        break

if c.status(ticket)['ticket_status'] == 'complete':
    print 'Updated. read_items() titles:'
    for item in c.read_items():
        if type(item) is song.Song:
            print '    "%s"' % (item.title, )
        else:
            print '    "%s" not resolved' % (item['request']['song_name'])
            print '        %s' % (item,)
    cp = c.get_profile()
    print '\nCatalog profile:'
    for key, val in cp.iteritems():
        print '    %-15s %s' % (key, val)
else:
    print 'Update did not complete within 60 seconds.'
