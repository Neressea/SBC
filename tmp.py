from requestHandler import requestSPARQL


res = requestSPARQL(gene="PA107", drug="PA449053")
# if res.status_code == 200:
#     print "\t[OK]"
# else:
#     print "\t\t[FAIL]",
# print "\n",
# print res.content
