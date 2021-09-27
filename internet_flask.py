import speedtest

st = speedtest.Speedtest()
servernames = []
st.get_servers(servernames)

d = str(st.download())
u = str(st.upload())
p = str(st.results.ping)

download = f"{d[0:2]}.{d[9:11]}"
upload = f"{u[0:2]}.{u[9:11]}"
ping = f"{p[0:2]}"