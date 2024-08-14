from obspy.core import read

st = read("Package_1587487399437.mseed")
for tr in st:
    fname = "%s.%s.%s.%s.SAC" % (tr.stats.network, tr.stats.station, tr.stats.location, tr.stats.channel)
    tr.write(fname, format="SAC")
