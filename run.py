# vim: ai ts=4 sts=4 et sw=4

from eve import Eve

def after_insert_downloads_callback(downloads):
    for download in downloads:
        print "An item has been inserted %s" % download

app = Eve()
app.on_inserted_downloads += after_insert_downloads_callback

if __name__ == '__main__':
    app.run()
