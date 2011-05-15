# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import catalog

c = catalog.Catalog('example_songs', type='song')

older_news = c.get_feed(buckets=['news'], since='2011-03-01', start=20)
newer_news = c.get_feed(buckets=['news'], since='2011-04-01', start=20)

newer = False
for feed_list in [older_news, newer_news]:
    if not newer:
        print 'Older news items:'
        print '    Full example item:'
        for key, val in feed_list[0].iteritems():
            print '         %-12s %s' % (key, val)
        print ''
        newer = True
    else:
        print '\nNewer news items:'

    print '    Date posted for each news item:'
    for feed_item in feed_list:
        print '        %s about %s' % (feed_item['date_posted'],feed_item['references'][0]['artist_name'])
